#!/usr/bin/env python3
"""Run the hardtools suite with OpenAI's Codex CLI as the agent instead of Claude Code.

  python3 evals/codex/run_codex.py --arm native              # no skills, Firecrawl CLI blocked, key removed
  python3 evals/codex/run_codex.py --arm original            # upstream skills 22358f2
  python3 evals/codex/run_codex.py --arm mine --skills-ref a3648a8

Each run gets a fresh CODEX_HOME whose skills/ holds only the skills under test
(Codex loads $CODEX_HOME/skills/*/SKILL.md, like ~/.claude/skills). Codex's own
live web_search stays on in every arm, as WebSearch/WebFetch do for Claude.
Writes results/hardtools-codex-<arm>/runs.jsonl with the same fields run.py
writes, so hardtools/judge_agent.py and hardtools/report.py work unchanged:

  python3 evals/hardtools/judge_agent.py evals/results/hardtools-codex-*
  python3 evals/hardtools/report.py native original mine codex-native codex-original codex-mine

Needs CODEX_API_KEY (or OPENAI_API_KEY) in the environment.
"""
import argparse, concurrent.futures as cf, datetime, json, os, shutil, subprocess, sys, tempfile, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import run as R

CASES_FILE = HERE.parent / "hardtools" / "tasks.jsonl"
ARMS = {"native": "NONE", "original": "22358f2", "mine": None}
PASS_ENV = [k for k in R.PASS_ENV if not k.startswith(("ANTHROPIC", "CLAUDE"))] + [
    "CODEX_API_KEY", "OPENAI_API_KEY", "OPENAI_BASE_URL", "CODEX_CA_CERTIFICATE"]
# USD per 1M tokens (input, cached input, output); override with --price
PRICES = {"default": (1.25, 0.125, 10.0)}
BLOCKED = "#!/bin/sh\necho 'firecrawl is not available in this run' >&2\nexit 127\n"


def score(stream, price):
    tools, fc_cmds, fc_api, skills, actions, answer = [], [], [], [], [], ""
    usage, turns, failed = {"input_tokens": 0, "cached_input_tokens": 0, "output_tokens": 0}, 0, None
    for line in stream.splitlines():
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        t = e.get("type")
        if t == "turn.completed":
            turns += 1
            for k in usage:
                usage[k] += (e.get("usage") or {}).get(k) or 0
        elif t == "turn.failed":
            failed = (e.get("error") or {}).get("message") or "turn.failed"
        elif t == "item.completed":
            it = e.get("item") or {}
            kind = it.get("type")
            if kind == "agent_message":
                answer = it.get("text") or answer
            elif kind == "web_search":
                tools.append("web_search")
                actions.append("native")
            elif kind == "mcp_tool_call":
                tools.append(f"mcp:{it.get('server')}.{it.get('tool')}")
            elif kind == "command_execution":
                c = it.get("command") or ""
                tools.append("shell")
                # Codex has no Skill tool: it reads SKILL.md with the shell
                skills += [p.split("/")[-2] for p in c.split() if p.endswith("/SKILL.md") and "/skills/" in p]
                m = [x.split()[-1].lstrip("-") if x else "(bare)" for x in R.FC_CMD.findall(c)]
                api = [b if a == "search" and b in ("developer", "research", "gov") else a for a, b in R.FC_API.findall(c)]
                if m or api:
                    fc_cmds += m
                    fc_api += api
                    actions.append("firecrawl")
                elif R.OTHER_WEB.search(c):
                    actions.append("other-shell")
    inp, cached, out = price
    cost = ((usage["input_tokens"] - usage["cached_input_tokens"]) * inp + usage["cached_input_tokens"] * cached
            + usage["output_tokens"] * out) / 1e6
    return {"first_web": actions[0] if actions else "none", "used_firecrawl": "firecrawl" in actions,
            "used_native": "native" in actions, "skills": skills, "fc_cmds": fc_cmds, "fc_api": fc_api,
            "n_tools": len(tools), "tools": tools, "num_turns": turns, "usage": usage, "cost_usd": round(cost, 4),
            "result_subtype": "error" if failed else "success", "error": failed, "answer": answer}


def run_one(case, trial, skills_src, block_fc, outdir, a, price):
    tag = f"{case['id']}-t{trial}"
    tmp = Path(tempfile.mkdtemp(prefix=f"fceval-codex-{tag}-", dir=a.tmp))
    home, work, shim = tmp / "home", tmp / "work", tmp / "bin"
    work.mkdir(); shim.mkdir()
    if skills_src:
        shutil.copytree(skills_src, home / "skills")
    else:
        home.mkdir()
    env = {k: os.environ[k] for k in PASS_ENV if k in os.environ}
    env.setdefault("CODEX_CA_CERTIFICATE", env.get("SSL_CERT_FILE", ""))
    env["CODEX_HOME"] = str(home)
    if block_fc:
        env.pop("FIRECRAWL_API_KEY", None)
        for name in ("firecrawl", "firecrawl-cli"):
            (shim / name).write_text(BLOCKED); (shim / name).chmod(0o755)
        env["PATH"] = f"{shim}:{env.get('PATH', '')}"
    cmd = ["codex", "exec", "--json", "--skip-git-repo-check", "--ephemeral", "-c", 'web_search="live"',
           "-s", "workspace-write", "-c", "sandbox_workspace_write.network_access=true", "-C", str(work)]
    if a.model:
        cmd += ["-m", a.model]
    if a.effort:
        cmd += ["-c", f'model_reasoning_effort="{a.effort}"']
    t0 = time.time()
    try:
        p = subprocess.run(cmd + [case["prompt"]], cwd=work, env=env, stdin=subprocess.DEVNULL,
                           capture_output=True, text=True, timeout=a.timeout)
        out, err, timed_out = p.stdout, p.stderr, False
    except subprocess.TimeoutExpired as e:
        out = e.stdout.decode() if isinstance(e.stdout, bytes) else (e.stdout or "")
        err, timed_out = "", True
    (outdir / "transcripts" / f"{tag}.jsonl").write_text(out)
    rec = score(out, price)
    rec.update(id=case["id"], trial=trial, duration_s=round(time.time() - t0, 1), timed_out=timed_out, stderr=err[-500:])
    shutil.rmtree(tmp, ignore_errors=True)
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--arm", choices=sorted(ARMS), required=True)
    ap.add_argument("--skills-ref", help="skills for the mine arm (a git ref)")
    ap.add_argument("--label")
    ap.add_argument("--model", help="Codex model; default is whatever the installed Codex CLI defaults to")
    ap.add_argument("--effort", help="model_reasoning_effort (minimal/low/medium/high)")
    ap.add_argument("--price", help="USD per 1M tokens as input,cached,output", default=",".join(map(str, PRICES["default"])))
    ap.add_argument("--trials", type=int, default=2)
    ap.add_argument("--concurrency", type=int, default=2)
    ap.add_argument("--timeout", type=int, default=2400)
    ap.add_argument("--tmp", default=str(Path.home() / ".fceval"), help="parent dir for per-run CODEX_HOME (Codex refuses helpers under /tmp)")
    ap.add_argument("--only")
    a = ap.parse_args()
    if not (os.environ.get("CODEX_API_KEY") or os.environ.get("OPENAI_API_KEY")):
        sys.exit("set CODEX_API_KEY or OPENAI_API_KEY")
    ref = a.skills_ref or ARMS[a.arm]
    if not ref:
        sys.exit(f"--skills-ref is required for --arm {a.arm}")
    price = tuple(float(x) for x in a.price.split(","))
    Path(a.tmp).mkdir(parents=True, exist_ok=True)

    cases = [json.loads(l) for l in CASES_FILE.read_text().splitlines() if l.strip()]
    if a.only:
        cases = [c for c in cases if c["id"] in set(a.only.split(","))]
    outdir = R.ROOT / "results" / f"hardtools-{a.label or 'codex-' + a.arm}"
    (outdir / "transcripts").mkdir(parents=True, exist_ok=True)
    skills_src = None
    if ref != "NONE":
        skills_src = Path(tempfile.mkdtemp(prefix="fceval-skills-")) / "skills"
        R.export_skills(ref, skills_src)
    meta = dict(suite="hardtools", agent="codex", label=outdir.name.removeprefix("hardtools-"), skills_ref=ref,
                model=a.model or "(codex default)", effort=a.effort, price_per_mtok=price, trials=a.trials,
                started=datetime.datetime.utcnow().isoformat() + "Z", firecrawl_key=a.arm != "native",
                codex_version=subprocess.run(["codex", "--version"], capture_output=True, text=True).stdout.strip())
    (outdir / "meta.json").write_text(json.dumps(meta, indent=2))

    rows_path = outdir / "runs.jsonl"
    done = {(r["id"], r["trial"]) for r in map(json.loads, rows_path.read_text().splitlines())
            if not r.get("error")} if rows_path.exists() else set()  # failed runs are retried
    jobs = [(c, t) for t in range(1, a.trials + 1) for c in cases if (c["id"], t) not in done]
    print(f"{len(jobs)} runs to do ({len(done)} already done) -> {outdir}", flush=True)
    with cf.ThreadPoolExecutor(a.concurrency) as ex, rows_path.open("a") as fh:
        futs = {ex.submit(run_one, c, t, skills_src, a.arm == "native", outdir, a, price): (c, t) for c, t in jobs}
        for i, f in enumerate(cf.as_completed(futs), 1):
            c, t = futs[f]
            try:
                r = f.result()
            except Exception as e:  # a crashed run is a data point too
                r = dict(id=c["id"], trial=t, error=repr(e), first_web="error")
            fh.write(json.dumps(r) + "\n"); fh.flush()
            print(f"[{i}/{len(jobs)}] {c['id']} t{t}: fc={r.get('fc_cmds')} skills={r.get('skills')} "
                  f"tools={r.get('n_tools')} ${r.get('cost_usd')} err={r.get('error')}", flush=True)


if __name__ == "__main__":
    main()

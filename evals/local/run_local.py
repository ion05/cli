#!/usr/bin/env python3
"""Run the hardtools suite with OpenCode or Hermes Agent on a local Ollama model.
Reuses run.py's loop (resume, runs.jsonl, report); only the agent call and the
transcript parsing differ. Results land in results/hardtools-<harness>-<arm>,
so hardtools/judge_agent.py and hardtools/report.py work on them unchanged.

  python3 evals/local/run_local.py --harness opencode --arm mine
  python3 evals/local/run_local.py --harness hermes --arm native

Arms: mine = PR #6 skills (a3648a8) + Firecrawl key; native = no skills,
`firecrawl` blocked, no key. Both arms keep the agent's own web search/fetch,
like the Claude Code arms kept WebSearch/WebFetch.
"""
import argparse, json, os, shutil, subprocess, sys, tempfile, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import run as R

R.SUITES["hardtools"] = HERE.parent / "hardtools" / "tasks.jsonl"
MODEL = "qwen3-8b-64k"  # Modelfile in this folder: qwen3:8b with num_ctx 65536
CTX = 65536
FC_CREDS = Path.home() / "Library/Application Support/firecrawl-cli/credentials.json"
DENY_FC = ["firecrawl", "firecrawl *", "npx firecrawl*", "npx -y firecrawl*", "*/firecrawl *"]
WEB_TOOLS = {"webfetch", "websearch", "web_search", "web_extract"}
SHELL_TOOLS = {"bash", "shell", "terminal"}
SKILL_TOOLS = {"skill", "skill_view"}


def opencode_setup(tmp, work, skills_src, arm, max_turns):
    cfg = tmp / "home" / ".config" / "opencode"
    cfg.mkdir(parents=True)
    if skills_src:
        shutil.copytree(skills_src, cfg / "skills")
    shell = {"*": "allow", **({p: "deny" for p in DENY_FC} if arm == "native" else {})}
    (cfg / "opencode.json").write_text(json.dumps({
        "provider": {"ollama": {"npm": "@ai-sdk/openai-compatible", "name": "Ollama",
                                "options": {"baseURL": "http://localhost:11434/v1"},
                                "models": {MODEL: {"name": MODEL, "limit": {"context": CTX, "output": 8192}}}}},
        "enabled_providers": ["ollama"], "model": f"ollama/{MODEL}", "small_model": f"ollama/{MODEL}",
        "autoupdate": False, "share": "disabled",
        "agent": {"build": {"steps": max_turns}},
        # task subagents hide their tool calls from the JSON stream, so keep everything in one session
        "permission": {"*": "allow", "task": "deny", "shell": shell, "bash": shell,
                       "skill": {"*": "allow", "customize-opencode": "deny"}},
    }, indent=1))
    env = {"OPENCODE_DISABLE_CLAUDE_CODE": "1", "OPENCODE_DISABLE_EXTERNAL_SKILLS": "1",
           "OPENCODE_DISABLE_AUTOUPDATE": "1", "OPENCODE_ENABLE_EXA": "1"}  # Exa = keyless websearch
    return ["opencode", "run", "--standalone", "--auto", "--format", "json", "-m", f"ollama/{MODEL}"], env


def hermes_setup(tmp, work, skills_src, arm, max_turns):
    home = tmp / "hermes"
    home.mkdir()
    if skills_src:
        shutil.copytree(skills_src, home / "skills")
    cfg = {
        "model": {"default": MODEL, "provider": "custom", "base_url": "http://localhost:11434/v1",
                  "context_length": CTX, "ollama_num_ctx": CTX},
        "agent": {"max_turns": max_turns},
        "approvals": {"mode": "off", "single_query_mode": "approve", **({"deny": DENY_FC} if arm == "native" else {})},
        "skills": {"creation_nudge_interval": 0},
        # Search via Exa's keyless tier, extract with Hermes' own fetcher: never Firecrawl behind the scenes
        "web": {"search_backend": "exa", "extract_backend": "native", "provider_tier": {"exa": "free"},
                "keyless_fallback": False, "keyless_rescue": False},
    }
    (home / "config.yaml").write_text(json.dumps(cfg, indent=1))  # JSON is valid YAML
    toolsets = "terminal,file,web" + (",skills" if skills_src else "")
    return (["hermes", "chat", "--oneshot", "--format", "stream-json", "--toolsets", toolsets,
             "--max-turns", str(max_turns), "--yolo", "--source", "tool", "-q"],
            {"HERMES_HOME": str(home), "HERMES_API_TIMEOUT": "1800"})


SETUP = {"opencode": opencode_setup, "hermes": hermes_setup}


def make_run_one(harness, arm):
    def run_one(case, trial, skills_src, outdir, model, max_turns, timeout, fixture_dirs):
        tag = f"{case['id']}-t{trial}"
        tmp = Path(tempfile.mkdtemp(prefix=f"fclocal-{tag}-"))
        work = tmp / "work"
        work.mkdir()
        (tmp / "home").mkdir(exist_ok=True)
        subprocess.run(["git", "init", "-q"], cwd=work)  # stops upward config/AGENTS.md discovery
        cmd, extra = SETUP[harness](tmp, work, skills_src, arm, max_turns)
        env = {k: os.environ[k] for k in R.PASS_ENV if k in os.environ and k != "FIRECRAWL_API_KEY"}
        env.update(extra, HOME=str(tmp / "home"))
        if arm == "mine":
            env["FIRECRAWL_API_KEY"] = os.environ["FIRECRAWL_API_KEY"]
        t0 = time.time()
        try:
            p = subprocess.run(cmd + [case["prompt"]], cwd=work, env=env, stdin=subprocess.DEVNULL,
                               capture_output=True, text=True, timeout=timeout)
            out, err, timed_out = p.stdout, p.stderr, False
        except subprocess.TimeoutExpired as e:
            out = e.stdout.decode() if isinstance(e.stdout, bytes) else (e.stdout or "")
            err, timed_out = "", True
        dur = time.time() - t0
        (outdir / "transcripts" / f"{tag}.jsonl").write_text(out)
        rec = score(case, out, harness)
        rec.update(id=case["id"], trial=trial, duration_s=round(dur, 1), timed_out=timed_out, stderr=err[-500:])
        shutil.rmtree(tmp, ignore_errors=True)
        return rec
    return run_one


def events_opencode(stream):
    """-> list of (tool, input, ok), final answer, steps, errors"""
    calls, texts, steps, errors = [], [], 0, []
    for e in stream:
        p = e.get("part", {})
        if e["type"] == "tool_use":
            calls.append((p.get("tool"), p.get("state", {}).get("input") or {}, p.get("state", {}).get("status") == "completed"))
        elif e["type"] == "text":
            texts.append(p.get("text", ""))
        elif e["type"] == "step_finish":
            steps += 1
        elif e["type"] == "error":
            errors.append(json.dumps(e.get("error"))[:300])
    return calls, (texts[-1] if texts else ""), steps, errors, None


def events_hermes(stream):
    calls, steps, errors, result = [], 0, [], None
    for e in stream:
        if e["type"] == "tool_use":
            calls.append((e.get("name"), e.get("input") or {}, True))
        elif e["type"] == "tool_result" and e.get("is_error") and calls:
            calls[-1] = calls[-1][:2] + (False,)
        elif e["type"] == "result":
            result = e
    if result and result.get("error"):
        errors.append(str(result["error"])[:300])
    return calls, (result or {}).get("text") or "", len(calls), errors, result


def score(case, stream, harness):
    evs = []
    for line in stream.splitlines():
        try:
            evs.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    calls, answer, steps, errors, result = (events_opencode if harness == "opencode" else events_hermes)(evs)
    actions, skills, fc_cmds, fc_api, tools = [], [], [], [], []
    for name, inp, _ok in calls:
        tools.append(name)
        if name in SKILL_TOOLS:
            s = inp.get("name") or inp.get("id") or ""
            skills.append(s)
            if s.startswith("firecrawl"):
                actions.append("firecrawl")
        elif name in WEB_TOOLS:
            actions.append("native")
        elif name in SHELL_TOOLS:
            c_ = inp.get("command", "")
            m = [x.split()[-1].lstrip("-") if x else "(bare)" for x in R.FC_CMD.findall(c_)]
            api = [a for a, _b in R.FC_API.findall(c_)]
            if m or api:
                fc_cmds += m
                fc_api += api
                actions.append("firecrawl")
            elif R.OTHER_WEB.search(c_):
                actions.append("other-shell")
    return {
        "first_web": actions[0] if actions else ("none" if evs else "error"),
        "used_firecrawl": "firecrawl" in actions, "used_native": "native" in actions,
        "skills": skills, "fc_cmds": fc_cmds, "fc_api": fc_api, "n_tools": len(tools), "tools": tools,
        "failed_tool_calls": sum(not ok for *_x, ok in calls),
        "num_turns": steps, "cost_usd": 0.0, "answer": answer, "errors": errors,
        "result_subtype": "error" if errors else ("success" if answer else "no_answer"),
        "tokens": (result or {}).get("tokens"),
    }


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--harness", choices=sorted(SETUP), required=True)
    ap.add_argument("--arm", choices=["mine", "native"], required=True)
    ap.add_argument("--skills-ref", default="a3648a8")
    ap.add_argument("--trials", type=int, default=1)
    ap.add_argument("--max-turns", type=int, default=80)
    ap.add_argument("--timeout", type=int, default=2400)
    ap.add_argument("--only", default="i1,i3,i4,i5,m1,m2,m3,c1,c2,c3,a1,a2,a3,a4,a5")  # i2 dropped: bot-blocked
    a = ap.parse_args()
    a.suite, a.label, a.model, a.concurrency = "hardtools", f"{a.harness}-{a.arm}", f"ollama/{MODEL}", 1
    if a.arm == "native":
        a.skills_ref = "NONE"
        os.environ.pop("FIRECRAWL_API_KEY", None)
    else:
        os.environ.setdefault("FIRECRAWL_API_KEY", json.loads(FC_CREDS.read_text())["apiKey"])
    R.run_one = make_run_one(a.harness, a.arm)
    # run.py stamps `claude --version` into meta.json; stamp the real agent instead
    sp_run = R.subprocess.run
    R.subprocess.run = lambda cmd, *x, **k: (sp_run([a.harness, "--version"], *x, **k) if cmd == ["claude", "--version"] else sp_run(cmd, *x, **k))
    R.cmd_run(a)

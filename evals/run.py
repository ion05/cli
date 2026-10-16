#!/usr/bin/env python3
"""Run Claude Code headless against a prompt suite with a given version of the
Firecrawl skills installed, then score how it used them.

  python3 evals/run.py run --suite trigger --skills-ref 22358f2 --label baseline
  python3 evals/run.py report evals/results/trigger-baseline

Each trial gets a fresh working dir (fixtures copied in) and a fresh
CLAUDE_CONFIG_DIR whose skills/ holds only the skills under test, which mirrors
a global `firecrawl setup` install. Transcripts are saved as stream-json.
"""
import argparse, concurrent.futures as cf, datetime, json, os, re, shutil, subprocess, sys, tempfile, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SUITES = {"trigger": ROOT / "trigger" / "prompts.jsonl", "tasks": ROOT / "tasks" / "tasks.jsonl",
          "subtools": ROOT / "subtools" / "prompts.jsonl"}
# Only what the child needs to reach the model API; everything else from the
# parent session (hooks, synced skills, MCP servers) stays out.
PASS_ENV = ["PATH", "HOME", "ANTHROPIC_BASE_URL", "ANTHROPIC_API_KEY", "CLAUDE_CODE_OAUTH_TOKEN",
            "HTTPS_PROXY", "HTTP_PROXY", "NO_PROXY", "https_proxy", "http_proxy", "no_proxy",
            "NODE_EXTRA_CA_CERTS", "SSL_CERT_FILE", "FIRECRAWL_API_KEY", "FIRECRAWL_API_URL",
            "IS_SANDBOX"]  # IS_SANDBOX lets bypassPermissions run as root in a container
FC_CMD = re.compile(r"(?:^|[\s;&|(`])(?:npx\s+(?:-y\s+)?firecrawl-cli(?:@\S+)?|firecrawl)\s+((?:(?:x|experimental)\s+)?(?:--)?[a-z][\w-]*)?")
OTHER_WEB = re.compile(r"\b(curl|wget|npm view|pip (?:index|download)|gh api|gh repo|gh release|lynx|python3? -c .*(?:urllib|requests))\b")


def load_suite(name):
    return [json.loads(l) for l in SUITES[name].read_text().splitlines() if l.strip()]


def export_skills(ref, dest):
    if ref == "WORKTREE":
        shutil.copytree(REPO / "skills", dest)
        return
    dest.mkdir(parents=True)
    tar = subprocess.run(["git", "-C", str(REPO), "archive", ref, "skills"], capture_output=True, check=True).stdout
    subprocess.run(["tar", "-x", "--strip-components=1", "-C", str(dest)], input=tar, check=True)


def run_one(case, trial, skills_src, outdir, model, max_turns, timeout, fixture_dirs):
    tag = f"{case['id']}-t{trial}"
    tmp = Path(tempfile.mkdtemp(prefix=f"fceval-{tag}-"))
    cfg, work = tmp / "cfg", tmp / "work"
    work.mkdir()
    if skills_src:
        shutil.copytree(skills_src, cfg / "skills")
    else:
        cfg.mkdir()
    for fd in fixture_dirs:
        for f in fd.iterdir():
            shutil.copy(f, work / f.name)
    env = {k: os.environ[k] for k in PASS_ENV if k in os.environ}
    env["CLAUDE_CONFIG_DIR"] = str(cfg)
    cmd = ["claude", "-p", case["prompt"], "--model", model, "--output-format", "stream-json", "--verbose",
           "--max-turns", str(max_turns), "--permission-mode", "bypassPermissions"]
    t0 = time.time()
    try:
        p = subprocess.run(cmd, cwd=work, env=env, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=timeout)
        out, err, timed_out = p.stdout, p.stderr, False
    except subprocess.TimeoutExpired as e:
        out, err, timed_out = (e.stdout or b"").decode() if isinstance(e.stdout, bytes) else (e.stdout or ""), "", True
    dur = time.time() - t0
    (outdir / "transcripts" / f"{tag}.jsonl").write_text(out)
    rec = score(case, out)
    rec.update(id=case["id"], trial=trial, duration_s=round(dur, 1), timed_out=timed_out, stderr=err[-500:])
    shutil.rmtree(tmp, ignore_errors=True)
    return rec


def score(case, stream):
    events = []
    for line in stream.splitlines():
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    actions, skills, fc_cmds, tools = [], [], [], []
    result = {}
    for e in events:
        if e.get("type") == "assistant":
            for c in e["message"].get("content", []):
                if c.get("type") != "tool_use":
                    continue
                name, inp = c["name"], c.get("input", {})
                tools.append(name)
                if name == "Skill":
                    s = inp.get("skill") or inp.get("command") or ""
                    skills.append(s)
                    if s.startswith("firecrawl"):
                        actions.append("firecrawl")
                elif name in ("WebSearch", "WebFetch"):
                    actions.append("native")
                elif name == "Bash":
                    c_ = inp.get("command", "")
                    # `firecrawl x download` counts as `download`, `firecrawl --status` as `status`
                    m = [x.split()[-1].lstrip("-") if x else "(bare)" for x in FC_CMD.findall(c_)]
                    if m:
                        fc_cmds += m
                        actions.append("firecrawl")
                    elif OTHER_WEB.search(c_):
                        actions.append("other-shell")
        elif e.get("type") == "result":
            result = e
    answer = result.get("result") or ""
    rec = {
        "first_web": actions[0] if actions else "none",
        "used_firecrawl": "firecrawl" in actions,
        "used_native": "native" in actions,
        "skills": skills, "fc_cmds": fc_cmds, "n_tools": len(tools), "tools": tools,
        "num_turns": result.get("num_turns"), "cost_usd": result.get("total_cost_usd"),
        "result_subtype": result.get("subtype"), "answer": answer[-1500:],
    }
    if not result:
        rec["first_web"] = "error"
    if isinstance(case.get("expect"), list):  # subtools suite: did it run the right command?
        rec["correct"] = any(c in case["expect"] for c in fc_cmds)
    elif "grade" in case:
        rec["correct"] = bool(re.search(case["grade"], answer, re.I))
    elif "grade_all" in case:
        rec["correct"] = all(re.search(g, answer, re.I) for g in case["grade_all"])
    return rec


def tool_usage(rows):
    """Count every tool call, every Firecrawl skill load and every `firecrawl <cmd>` shell call.
    Known Firecrawl skills/commands are listed even at zero so gaps are visible."""
    known_skills = sorted(p.name for p in (REPO / "skills").iterdir() if p.is_dir()) if (REPO / "skills").is_dir() else []
    # skill name -> the CLI command it teaches, where they differ
    rename = {"developer-index": "developer", "research-index": "research"}
    known_cmds = [rename.get(c, c) for c in (s.removeprefix("firecrawl-") for s in known_skills if s != "firecrawl")]
    n = len(rows)

    def count(key, known=()):
        calls, runs = dict.fromkeys(known, 0), dict.fromkeys(known, 0)
        for r in rows:
            xs = r.get(key, [])
            for x in xs:
                calls[x] = calls.get(x, 0) + 1
            for x in set(xs):
                runs[x] = runs.get(x, 0) + 1
        return {k: {"calls": calls[k], "runs": runs[k]} for k in sorted(calls, key=lambda k: (-calls[k], k))}

    usage = {"runs": n, "builtin_tools": count("tools"),
             "firecrawl_skills": count("skills", known_skills), "firecrawl_cli": count("fc_cmds", known_cmds)}
    lines = ["", "## Tool calls", "", f"Across {n} runs. *Runs* = runs that called it at least once.", ""]
    for title, key, fmt in [("All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)", "builtin_tools", "`{}`"),
                            ("Firecrawl skills loaded", "firecrawl_skills", "`{}`"),
                            ("Firecrawl CLI commands run in Bash", "firecrawl_cli", "`firecrawl {}`")]:
        lines += [f"**{title}**", "", "| Tool | Calls | Runs | Calls per run |", "|---|---|---|---|"]
        for k, v in usage[key].items():
            lines.append(f"| {fmt.format(k)} | {v['calls']} | {v['runs']} | {v['calls'] / max(n, 1):.2f} |")
        lines.append("")
    return usage, lines


def subtool_table(rows, cases):
    """Per intended subtool: how often the agent ran that command, loaded its skill, or ran something else."""
    out = ["", "## Per subtool", "",
           "Each prompt names Firecrawl but not the command, so this isolates *which* subtool the agent picks.", "",
           "| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run |", "|---|---|---|---|---|"]
    by = {}
    for r in rows:
        by.setdefault(cases[r["id"]]["intent"], []).append(r)
    for intent, rs in by.items():
        k = len(rs)
        ran = sum(bool(r.get("correct")) for r in rs)
        skill = sum(any(x == f"firecrawl-{intent}" or x.startswith(f"firecrawl-{intent}-") for x in r.get("skills", [])) for r in rs)
        anyfc = sum(bool(r.get("used_firecrawl")) for r in rs)
        cmds = {}
        for r in rs:
            for c in r.get("fc_cmds", []):
                cmds[c] = cmds.get(c, 0) + 1
        got = ", ".join(f"`{c}` x{v}" for c, v in sorted(cmds.items(), key=lambda kv: -kv[1])) or "-"
        out.append(f"| {intent} | {ran}/{k} | {skill}/{k} | {anyfc}/{k} | {got} |")
    return out


def cmd_run(a):
    cases = load_suite(a.suite)
    if a.only:
        keep = set(a.only.split(","))
        cases = [c for c in cases if c["id"] in keep]
    outdir = ROOT / "results" / f"{a.suite}-{a.label}"
    (outdir / "transcripts").mkdir(parents=True, exist_ok=True)
    fixture_dirs = [d for d in (ROOT / "fixtures", SUITES[a.suite].parent / "fixtures") if d.is_dir()]
    skills_src = None
    if a.skills_ref != "NONE":
        skills_src = Path(tempfile.mkdtemp(prefix="fceval-skills-")) / "skills"
        export_skills(a.skills_ref, skills_src)
    meta = dict(suite=a.suite, label=a.label, skills_ref=a.skills_ref, model=a.model, trials=a.trials,
                max_turns=a.max_turns, started=datetime.datetime.utcnow().isoformat() + "Z",
                firecrawl_key=bool(os.environ.get("FIRECRAWL_API_KEY")),
                claude_version=subprocess.run(["claude", "--version"], capture_output=True, text=True).stdout.strip())
    (outdir / "meta.json").write_text(json.dumps(meta, indent=2))
    jobs = [(c, t) for t in range(1, a.trials + 1) for c in cases]
    rows_path = outdir / "runs.jsonl"
    done = set()
    if rows_path.exists():
        for l in rows_path.read_text().splitlines():
            r = json.loads(l)
            done.add((r["id"], r["trial"]))
    jobs = [(c, t) for c, t in jobs if (c["id"], t) not in done]
    print(f"{len(jobs)} runs to do ({len(done)} already done) -> {outdir}", flush=True)
    with cf.ThreadPoolExecutor(a.concurrency) as ex, rows_path.open("a") as fh:
        futs = {ex.submit(run_one, c, t, skills_src, outdir, a.model, a.max_turns, a.timeout, fixture_dirs): (c, t) for c, t in jobs}
        for i, f in enumerate(cf.as_completed(futs), 1):
            c, t = futs[f]
            try:
                r = f.result()
            except Exception as e:  # keep going; a crashed run is a data point too
                r = dict(id=c["id"], trial=t, error=repr(e), first_web="error")
            fh.write(json.dumps(r) + "\n"); fh.flush()
            print(f"[{i}/{len(jobs)}] {c['id']} t{t}: first={r.get('first_web')} fc={r.get('fc_cmds')} skills={r.get('skills')} "
                  f"correct={r.get('correct')} ${r.get('cost_usd')}", flush=True)
    cmd_report(argparse.Namespace(dir=str(outdir)))


def cmd_report(a):
    d = Path(a.dir)
    meta = json.loads((d / "meta.json").read_text())
    rows = [json.loads(l) for l in (d / "runs.jsonl").read_text().splitlines() if l.strip()]
    cases = {c["id"]: c for c in load_suite(meta["suite"])}
    pct = lambda n, k: f"{100 * n / k:.0f}% ({n}/{k})" if k else "-"
    lines = [f"# {meta['suite']} eval: {meta['label']}", "",
             f"Skills `{meta['skills_ref']}` · model `{meta['model']}` · {meta['trials']} trials · max {meta['max_turns']} turns · "
             f"Firecrawl key: {meta['firecrawl_key']} · {meta['claude_version']}", ""]
    summary = {}
    if meta["suite"] == "trigger":
        use = [r for r in rows if cases[r["id"]]["expect"] == "use"]
        avoid = [r for r in rows if cases[r["id"]]["expect"] == "avoid"]
        either = [r for r in rows if cases[r["id"]]["expect"] == "either"]
        fw = lambda rs, v: sum(r.get("first_web") == v for r in rs)
        summary = {
            "firecrawl_first_on_web_tasks": fw(use, "firecrawl") / max(len(use), 1),
            "firecrawl_any_on_web_tasks": sum(bool(r.get("used_firecrawl")) for r in use) / max(len(use), 1),
            "native_first_on_web_tasks": fw(use, "native") / max(len(use), 1),
            "false_trigger_on_non_web": sum(bool(r.get("used_firecrawl")) for r in avoid) / max(len(avoid), 1),
            "firecrawl_on_simple_fetch": sum(bool(r.get("used_firecrawl")) for r in either) / max(len(either), 1),
        }
        lines += ["## Headline", "",
                  "| Metric | Value |", "|---|---|",
                  f"| Web tasks where Firecrawl was the first web tool | {pct(fw(use, 'firecrawl'), len(use))} |",
                  f"| Web tasks where Firecrawl was used at all | {pct(sum(bool(r.get('used_firecrawl')) for r in use), len(use))} |",
                  f"| Web tasks where built-in WebSearch/WebFetch came first | {pct(fw(use, 'native'), len(use))} |",
                  f"| Web tasks where another shell tool (curl, npm view, gh) came first | {pct(fw(use, 'other-shell'), len(use))} |",
                  f"| Web tasks answered with no web tool | {pct(fw(use, 'none'), len(use))} |",
                  f"| Non-web tasks where Firecrawl fired (false trigger) | {pct(sum(bool(r.get('used_firecrawl')) for r in avoid), len(avoid))} |",
                  f"| Simple fetches (raw file, JSON API, status check) where Firecrawl was used | {pct(sum(bool(r.get('used_firecrawl')) for r in either), len(either))} |",
                  "", "## Per prompt", "", "| id | expect / intent | first web tool per trial | Firecrawl skills / commands |", "|---|---|---|---|"]
    else:
        n = len(rows)
        corr = sum(bool(r.get("correct")) for r in rows)
        summary = {"accuracy": corr / max(n, 1), "firecrawl_used": sum(bool(r.get("used_firecrawl")) for r in rows) / max(n, 1)}
        costs = [r["cost_usd"] for r in rows if r.get("cost_usd") is not None]
        tools = [r["n_tools"] for r in rows if "n_tools" in r]
        durs = [r["duration_s"] for r in rows if "duration_s" in r]
        mean = lambda xs: sum(xs) / len(xs) if xs else 0
        lines += ["## Headline", "", "| Metric | Value |", "|---|---|",
                  f"| {'Ran the expected Firecrawl command' if meta['suite'] == 'subtools' else 'Correct answers'} | {pct(corr, n)} |",
                  f"| Runs that used Firecrawl | {pct(sum(bool(r.get('used_firecrawl')) for r in rows), n)} |",
                  f"| Runs that used built-in WebSearch/WebFetch | {pct(sum(bool(r.get('used_native')) for r in rows), n)} |",
                  f"| Mean tool calls | {mean(tools):.1f} |", f"| Mean model cost (USD) | {mean(costs):.3f} |",
                  f"| Mean duration (s) | {mean(durs):.0f} |",
                  "", "## Per task", "", "| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |", "|---|---|---|---|---|"]
        if meta["suite"] == "subtools":
            lines[-5:-5] = subtool_table(rows, cases)
    by = {}
    for r in rows:
        by.setdefault(r["id"], []).append(r)
    for cid in cases:
        rs = sorted(by.get(cid, []), key=lambda r: r["trial"])
        if not rs:
            continue
        fc = sorted({s for r in rs for s in r.get("skills", []) if s.startswith("firecrawl")} | {f"`{c}`" for r in rs for c in r.get("fc_cmds", [])})
        expect = "" if isinstance(cases[cid].get("expect"), list) else cases[cid].get("expect", "")
        row = f"| {cid} | {expect} {cases[cid].get('intent')} | {', '.join(r.get('first_web', '?') for r in rs)} | {' '.join(fc) or '-'} |"
        if meta["suite"] != "trigger":
            row += f" {sum(bool(r.get('correct')) for r in rs)}/{len(rs)} |"
        lines.append(row)
    errs = [r for r in rows if r.get("first_web") == "error"]
    if errs:
        lines += ["", f"{len(errs)} run(s) produced no result event (crash or timeout) and count as misses above."]
    usage, usage_lines = tool_usage(rows)
    summary["tool_calls"] = usage
    lines += usage_lines
    (d / "summary.json").write_text(json.dumps(summary, indent=2))
    (d / "REPORT.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--suite", choices=SUITES, required=True)
    r.add_argument("--skills-ref", default="WORKTREE", help="git ref to take skills/ from, WORKTREE for the working copy, NONE for no skills")
    r.add_argument("--label", required=True)
    r.add_argument("--model", default="claude-sonnet-5-5")
    r.add_argument("--trials", type=int, default=3)
    r.add_argument("--max-turns", type=int, default=12)
    r.add_argument("--concurrency", type=int, default=6)
    r.add_argument("--timeout", type=int, default=600)
    r.add_argument("--only", help="comma-separated case ids")
    r.set_defaults(func=cmd_run)
    p = sub.add_parser("report")
    p.add_argument("dir")
    p.set_defaults(func=cmd_report)
    a = ap.parse_args()
    a.func(a)

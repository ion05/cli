#!/usr/bin/env python3
"""Run `firecrawl agent` alone on hardtools tasks (the task prompt as its goal,
no schema, no Claude) to see what the agent command delivers on its own.
Writes runs.jsonl in the hardtools format so judge_agent.py can grade it.

  python3 evals/hardtools/agent_direct.py a1 a3 n5
"""
import json, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "results" / "hardtools-agent-direct"
CASES = {c["id"]: c for c in map(json.loads, (HERE / "tasks.jsonl").read_text().splitlines())}


def credits():
    p = subprocess.run(["firecrawl", "credit-usage", "--json"], capture_output=True, text=True)
    try:
        d = json.loads(p.stdout)
        d = d.get("data", d)
        return d.get("remainingCredits") or d.get("remaining_credits")
    except Exception:
        return None


OUT.mkdir(parents=True, exist_ok=True)
rows = OUT / "runs.jsonl"
done = {json.loads(l)["id"] for l in rows.read_text().splitlines()} if rows.exists() else set()
for cid in sys.argv[1:]:
    if cid in done:
        continue
    c0, t0 = credits(), time.time()
    p = subprocess.run(["firecrawl", "agent", CASES[cid]["prompt"], "--wait", "--json", "--timeout", "1800"],
                       capture_output=True, text=True, timeout=2000)
    dur, c1 = time.time() - t0, credits()
    (OUT / f"{cid}.json").write_text(p.stdout)
    try:
        d = json.loads(p.stdout)
        ans = json.dumps(d.get("data", d), indent=1)
    except json.JSONDecodeError:
        ans = p.stdout[-20000:] + p.stderr[-2000:]
    r = dict(id=cid, trial=1, answer=ans, duration_s=round(dur), fc_cmds=["agent"],
             credits=(c0 - c1) if c0 is not None and c1 is not None else None)
    with rows.open("a") as fh:
        fh.write(json.dumps(r) + "\n")
    print(cid, r["duration_s"], "s", r["credits"], "credits", len(ans), "chars", flush=True)

#!/usr/bin/env python3
"""Hard multi-site research tasks meant to need crawl, map, agent or interact.
Wraps run.py: registers the suite, picks an arm, keeps the full final answer
(run.py keeps only the last 1500 chars) and allows long runs.

  python3 evals/hardtools/run_hard.py --arm native            # no skills, Firecrawl CLI blocked
  python3 evals/hardtools/run_hard.py --arm original          # upstream skills 22358f2
  python3 evals/hardtools/run_hard.py --arm mine --skills-ref <PR #6 head>
  python3 evals/hardtools/run_hard.py --arm reference         # Opus, every tool, builds the reference answers

Grade with judge_agent.py.
"""
import argparse, json, os, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import run as R

R.SUITES["hardtools"] = HERE / "tasks.jsonl"

REF_PREFIX = ("You are building a reference answer for an evaluation, so be exhaustive and exact. "
              "Use whatever tools work best. For every fact, give the URL it came from. "
              "If something can't be found or is ambiguous, say so explicitly rather than guessing.\n\n")
ARMS = {
    # name: (skills ref, extra --disallowedTools, drop FIRECRAWL_API_KEY, prompt prefix)
    "native": ("NONE", ["Bash(firecrawl:*)", "Bash(npx firecrawl-cli:*)", "Bash(npx -y firecrawl-cli:*)"], True, ""),
    "original": ("22358f2", [], False, ""),
    "mine": (None, [], False, ""),
    "reference": (None, [], False, REF_PREFIX),
}

ap = argparse.ArgumentParser()
ap.add_argument("--arm", choices=sorted(ARMS), required=True)
ap.add_argument("--skills-ref", help="skills for the mine/reference arms (a git ref)")
ap.add_argument("--label")
ap.add_argument("--model", default="claude-sonnet-5-5")
ap.add_argument("--trials", type=int, default=2)
ap.add_argument("--max-turns", type=int, default=80)
ap.add_argument("--concurrency", type=int, default=3)
ap.add_argument("--timeout", type=int, default=2400)
ap.add_argument("--only")
a = ap.parse_args()

ref, blocked, drop_key, prefix = ARMS[a.arm]
a.skills_ref = a.skills_ref or ref
if not a.skills_ref:
    sys.exit(f"--skills-ref is required for --arm {a.arm}")
a.suite, a.label = "hardtools", a.label or a.arm
if drop_key:
    os.environ.pop("FIRECRAWL_API_KEY", None)

load = R.load_suite
R.load_suite = lambda name: [dict(c, prompt=prefix + c["prompt"]) for c in load(name)]

if blocked:
    sp_run = R.subprocess.run
    R.subprocess.run = lambda cmd, *x, **k: sp_run(cmd + ["--disallowedTools", *blocked] if cmd[:2] == ["claude", "-p"] else cmd, *x, **k)

score = R.score
def full_score(case, stream):
    rec = score(case, stream)
    for line in reversed(stream.splitlines()):
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        if e.get("type") == "result":
            rec["answer"] = e.get("result") or ""
            break
    return rec
R.score = full_score

R.cmd_run(a)

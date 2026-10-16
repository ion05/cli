#!/usr/bin/env python3
"""Run a tasks-style suite through run.py, optionally telling the agent to use
Firecrawl, so answer quality can be compared with and without the nudge.
Leaves run.py untouched: it registers extra suites and rewrites prompts on load.

  python3 evals/compare.py --suite tasks --skills-ref 22358f2 --label told
  python3 evals/compare.py --suite hard  --skills-ref 22358f2 --label baseline
  python3 evals/compare.py --suite hard  --skills-ref 22358f2 --label told --force-firecrawl
"""
import argparse, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run as R

R.SUITES["hard"] = R.ROOT / "tasks" / "hard.jsonl"
NUDGE = "Use Firecrawl to look this up on the web. "

ap = argparse.ArgumentParser()
ap.add_argument("--suite", choices=["tasks", "hard"], required=True)
ap.add_argument("--skills-ref", default="WORKTREE")
ap.add_argument("--label", required=True)
ap.add_argument("--force-firecrawl", action="store_true", help=f"prefix every prompt with {NUDGE!r}")
ap.add_argument("--model", default="claude-sonnet-5-5")
ap.add_argument("--trials", type=int, default=3)
ap.add_argument("--max-turns", type=int, default=12)
ap.add_argument("--concurrency", type=int, default=6)
ap.add_argument("--timeout", type=int, default=600)
ap.add_argument("--only")
a = ap.parse_args()

if a.force_firecrawl:
    load = R.load_suite
    R.load_suite = lambda name: [dict(c, prompt=NUDGE + c["prompt"]) for c in load(name)]
R.cmd_run(a)

#!/usr/bin/env python3
"""Run a tasks-style suite through run.py, optionally telling the agent to use
Firecrawl, so answer quality can be compared with and without the nudge.
Leaves run.py untouched: it registers extra suites and rewrites prompts on load.

  python3 evals/compare.py --suite tasks --skills-ref 22358f2 --label told
  python3 evals/compare.py --suite hard  --skills-ref 22358f2 --label baseline
  python3 evals/compare.py --suite hard  --skills-ref 22358f2 --label told --force-firecrawl

--only-tools restricts the agent with --disallowedTools as well as the prompt:
  native     WebSearch/WebFetch or memory; no Bash, no skills (use --skills-ref NONE)
  firecrawl  Firecrawl CLI only; WebSearch/WebFetch and other web shell tools blocked
"""
import argparse, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run as R

R.SUITES["hard"] = R.ROOT / "tasks" / "hard.jsonl"
NUDGE = "Use Firecrawl to look this up on the web. "
ONLY = {
    "native": ("Answer using only the WebSearch or WebFetch tools, or from what you already know. Do not run shell commands. ",
               ["Bash", "Skill"]),
    "firecrawl": ("Use only the Firecrawl CLI for web lookups. Do not use WebSearch, WebFetch, or other shell commands such as curl, npm or gh. ",
                  ["WebSearch", "WebFetch", "Bash(curl:*)", "Bash(wget:*)", "Bash(npm:*)", "Bash(gh:*)",
                   "Bash(python:*)", "Bash(python3:*)", "Bash(node:*)", "Bash(git:*)"]),
}

ap = argparse.ArgumentParser()
ap.add_argument("--suite", choices=["tasks", "hard"], required=True)
ap.add_argument("--skills-ref", default="WORKTREE")
ap.add_argument("--label", required=True)
ap.add_argument("--force-firecrawl", action="store_true", help=f"prefix every prompt with {NUDGE!r}")
ap.add_argument("--only-tools", choices=sorted(ONLY))
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
if a.only_tools:
    prefix, blocked = ONLY[a.only_tools]
    load, sp_run = R.load_suite, R.subprocess.run
    R.load_suite = lambda name: [dict(c, prompt=prefix + c["prompt"]) for c in load(name)]
    # run.py builds the claude command itself; append the block list on the way out.
    R.subprocess.run = lambda cmd, *x, **k: sp_run(cmd + ["--disallowedTools", *blocked] if cmd[:2] == ["claude", "-p"] else cmd, *x, **k)
R.cmd_run(a)

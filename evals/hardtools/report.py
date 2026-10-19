#!/usr/bin/env python3
"""Compare hardtools arms side by side from runs.jsonl + judge.jsonl.

  python3 evals/hardtools/report.py native original mine > evals/hardtools/RESULTS.md
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RES = HERE.parent / "results"
CASES = {c["id"]: c for c in map(json.loads, (HERE / "tasks.jsonl").read_text().splitlines())}
CMDS = ["search", "scrape", "map", "crawl", "agent", "interact"]


def load(arm):
    d = RES / f"hardtools-{arm}"
    rows = {(r["id"], r["trial"]): r for r in map(json.loads, (d / "runs.jsonl").read_text().splitlines())}
    jp = d / "judge.jsonl"
    if jp.exists():
        for j in map(json.loads, jp.read_text().splitlines()):
            if "error" not in j and (j["id"], j["trial"]) in rows:
                rows[(j["id"], j["trial"])]["judge"] = j
    return list(rows.values())


mean = lambda xs: sum(xs) / len(xs) if xs else float("nan")
arms = sys.argv[1:]
data = {a: load(a) for a in arms}


def score(r):
    return r.get("judge", {}).get("score")


def intended(r):
    return any(c in CASES[r["id"]]["intent_cmds"] for c in r.get("fc_cmds", []))


out = ["| | " + " | ".join(arms) + " |", "|---|" + "---|" * len(arms)]
def row(name, f):
    out.append(f"| {name} | " + " | ".join(f(data[a]) for a in arms) + " |")

row("Judge score (mean /100)", lambda rs: f"{mean([score(r) for r in rs if score(r) is not None]):.0f}")
row("Runs scoring 70+", lambda rs: f"{sum((score(r) or 0) >= 70 for r in rs)}/{len(rs)}")
row("Runs scoring under 20", lambda rs: f"{sum((score(r) or 0) < 20 for r in rs)}/{len(rs)}")
row("Cites sources", lambda rs: f"{mean([r['judge'].get('cites_sources', 0) for r in rs if 'judge' in r]):.0%}")
row("Faithful /5", lambda rs: f"{mean([r['judge'].get('faithful', 0) for r in rs if 'judge' in r]):.2f}")
row("Used Firecrawl", lambda rs: f"{sum(bool(r.get('used_firecrawl')) for r in rs)}/{len(rs)}")
row("Ran an intended command", lambda rs: f"{sum(intended(r) for r in rs)}/{len(rs)}")
for c in CMDS:
    row(f"`firecrawl {c}` calls", lambda rs, c=c: str(sum(r.get("fc_cmds", []).count(c) for r in rs)))
row("Used WebSearch/WebFetch", lambda rs: f"{sum(bool(r.get('used_native')) for r in rs)}/{len(rs)}")
row("Tool calls (mean)", lambda rs: f"{mean([r.get('n_tools', 0) for r in rs]):.1f}")
row("Turns (mean)", lambda rs: f"{mean([r.get('num_turns') or 0 for r in rs]):.1f}")
row("Cost per run (USD)", lambda rs: f"{mean([r.get('cost_usd') or 0 for r in rs]):.2f}")
row("Time per run (min)", lambda rs: f"{mean([r.get('duration_s', 0) for r in rs]) / 60:.1f}")
row("Hit turn limit or timeout", lambda rs: f"{sum(bool(r.get('timed_out')) or r.get('result_subtype') == 'error_max_turns' for r in rs)}/{len(rs)}")
print("## Overall\n\n" + "\n".join(out))

print("\n## By kind (mean judge score)\n")
print("| Kind | " + " | ".join(arms) + " |\n|---|" + "---|" * len(arms))
for k in ["interact", "map", "crawl", "agent"]:
    print(f"| {k} | " + " | ".join(f"{mean([score(r) for r in data[a] if CASES[r['id']]['kind'] == k and score(r) is not None]):.0f}" for a in arms) + " |")

print("\n## Every task\n\nEach cell: judge score per trial, then the Firecrawl commands run (all trials).\n")
print("| id | meant to need | " + " | ".join(arms) + " |\n|---|---|" + "---|" * len(arms))
for cid, c in CASES.items():
    cells = []
    for a in arms:
        rs = sorted((r for r in data[a] if r["id"] == cid), key=lambda r: r["trial"])
        sc = ", ".join(str(score(r)) if score(r) is not None else "?" for r in rs)
        cmds = {}
        for r in rs:
            for x in r.get("fc_cmds", []):
                cmds[x] = cmds.get(x, 0) + 1
        cm = " ".join(f"{k}x{v}" for k, v in sorted(cmds.items(), key=lambda kv: -kv[1]))
        cells.append(sc + (f" · {cm}" if cm else ""))
    print(f"| {cid} | {', '.join(c['intent_cmds'])} | " + " | ".join(cells) + " |")

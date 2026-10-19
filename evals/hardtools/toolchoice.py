#!/usr/bin/env python3
"""Score tool choice on the hardtools runs: did the agent run the Firecrawl
command each task was built for, and if not, did it still get a good answer?

  python3 evals/hardtools/toolchoice.py native original mine pr4

A run "picked the intended tool" when it ran any of the task's intent_cmds
other than scrape/search (those are fallbacks every task can use, so counting
them would score nearly every Firecrawl run as a hit). Runs that didn't are
split by judge score: 70+ is a good answer by another route, under 70 a poor one.
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RES = HERE.parent / "results"
CASES = {c["id"]: c for c in map(json.loads, (HERE / "tasks.jsonl").read_text().splitlines())}
mean = lambda xs: sum(xs) / len(xs) if xs else float("nan")


def load(arm):
    d = RES / f"hardtools-{arm}"
    rows = {(r["id"], r["trial"]): r for r in map(json.loads, (d / "runs.jsonl").read_text().splitlines())}
    jp = d / "judge.jsonl"
    if jp.exists():
        for j in map(json.loads, jp.read_text().splitlines()):
            if "error" not in j and (j["id"], j["trial"]) in rows:
                rows[(j["id"], j["trial"])]["judge"] = j
    return list(rows.values())


def score(r):
    return r.get("judge", {}).get("score")


BASIC = {"scrape", "search"}
GOOD = 70


def advanced(case):
    return [c for c in case["intent_cmds"] if c not in BASIC]


def bucket(r):
    if any(c in advanced(CASES[r["id"]]) for c in r.get("fc_cmds", [])):
        return "intended"
    return "other_good" if (score(r) or 0) >= GOOD else "other_poor"


def skill_use(r):
    """R = loaded the `firecrawl` router skill, C = a per-command skill only, - = no skill."""
    sk = set(r.get("skills", []))
    return "R+C" if "firecrawl" in sk and len(sk) > 1 else "R" if "firecrawl" in sk else "C" if sk else "-"


def main(arms):
    data = {a: load(a) for a in arms}
    na = {a for a in arms if not any(r.get("used_firecrawl") for r in data[a])}
    cell = lambda a, f: "n/a" if a in na else f(data[a])
    hdr = "| | " + " | ".join(arms) + " |\n|---|" + "---|" * len(arms)
    print("## Tool choice\n\n" + hdr)
    for name, b in [("Picked the intended tool", "intended"),
                    (f"Other route, good answer ({GOOD}+)", "other_good"),
                    (f"Other route, poor answer (<{GOOD})", "other_poor")]:
        print(f"| {name} | " + " | ".join(cell(a, lambda rs: f"{sum(bucket(r) == b for r in rs)}/{len(rs)}") for a in arms) + " |")
    for name, b in [("Mean score when intended tool picked", "intended"), ("Mean score by another route", None)]:
        f = lambda rs: (lambda xs: f"{mean(xs):.0f}" if xs else "–")(
            [score(r) for r in rs if score(r) is not None and ((bucket(r) == b) if b else bucket(r) != "intended")])
        print(f"| {name} | " + " | ".join(cell(a, f) for a in arms) + " |")

    print("\n## Picked the intended tool, by kind\n\n| Kind | " + " | ".join(arms) + " |\n|---|" + "---|" * len(arms))
    for k in ["interact", "map", "crawl", "agent"]:
        print(f"| {k} | " + " | ".join(cell(a, lambda rs: (lambda xs: f"{sum(bucket(r) == 'intended' for r in xs)}/{len(xs)}")(
            [r for r in rs if CASES[r["id"]]["kind"] == k])) for a in arms) + " |")

    print("\n## Which skill was loaded\n\n" + hdr)
    for name, b in [("Loaded the `firecrawl` router skill", ("R", "R+C")), ("Loaded only a per-command skill", ("C",)),
                    ("Loaded no skill", ("-",))]:
        print(f"| {name} | " + " | ".join(cell(a, lambda rs: f"{sum(skill_use(r) in b for r in rs)}/{len(rs)}") for a in arms) + " |")
    skills = sorted({s for a in arms for r in data[a] for s in r.get("skills", []) if s != "firecrawl"})
    for sk in skills:
        print(f"| Loaded `{sk}` | " + " | ".join(cell(a, lambda rs: f"{sum(sk in r.get('skills', []) for r in rs)}/{len(rs)}") for a in arms) + " |")

    print("\n## Every task\n\nI = intended tool, G = other route with a good answer, P = other route with a poor answer, one letter per trial.\n"
          "After the slash, the skill loaded per trial: R = `firecrawl` router, C = a per-command skill only, - = none.\n")
    print("| id | intended | " + " | ".join(arms) + " |\n|---|---|" + "---|" * len(arms))
    for cid, c in CASES.items():
        cells = []
        for a in arms:
            rs = sorted((r for r in data[a] if r["id"] == cid), key=lambda r: r["trial"])
            cells.append("n/a" if a in na else " ".join({"intended": "I", "other_good": "G", "other_poor": "P"}[bucket(r)] for r in rs)
                         + " / " + " ".join(skill_use(r) for r in rs))
        print(f"| {cid} | {', '.join(advanced(c))} | " + " | ".join(cells) + " |")


if __name__ == "__main__":
    main(sys.argv[1:])

#!/usr/bin/env python3
"""Side-by-side table of tasks-style result dirs (runs.jsonl + judge.jsonl), in markdown.

  python3 evals/table.py evals/results/natural-original evals/results/natural-pr4 > out.md

Columns are the dirs in the order given, headed by their labels.
"""
import json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run as R

NAMES = {"firecrawl": "Firecrawl", "native": "built-in", "other-shell": "shell", "none": "memory", "error": "error"}


def load(d):
    d = Path(d)
    meta = json.loads((d / "meta.json").read_text())
    rows = [json.loads(l) for l in (d / "runs.jsonl").read_text().splitlines() if l.strip()]
    jp = d / "judge.jsonl"
    judge = {(j["id"], j["trial"]): j for j in map(json.loads, jp.read_text().splitlines()) if "error" not in j} if jp.exists() else {}
    return meta, rows, judge


def headline(arms, keep=lambda r: True):
    def frac(f):
        return lambda rows, judge: f"{sum(map(f, rows))}/{len(rows)}"

    def jmean(k, pct=False):
        def g(rows, judge):
            xs = [judge[(r["id"], r["trial"])][k] for r in rows if (r["id"], r["trial"]) in judge]
            if not xs:
                return "-"
            m = sum(xs) / len(xs)
            return f"{m:.0%}" if pct else f"{m:.2f}"
        return g

    def mean(k, fmt):
        return lambda rows, judge: fmt.format(sum(r.get(k) or 0 for r in rows) / max(len(rows), 1))

    metrics = [
        ("Correct", frac(lambda r: bool(r.get("correct")))),
        ("Correct (judge)", jmean("correct", True)),
        ("Used Firecrawl", frac(lambda r: bool(r.get("used_firecrawl")))),
        ("Used built-in search", frac(lambda r: bool(r.get("used_native")))),
        ("First tool: shell (curl, npm, gh)", frac(lambda r: r.get("first_web") == "other-shell")),
        ("Answered from memory", frac(lambda r: r.get("first_web") == "none")),
        ("Cites a source", jmean("cites_source", True)),
        ("Faithful /5", jmean("faithful")), ("Complete /5", jmean("complete")), ("Concise /5", jmean("concise")),
        ("Tool calls", mean("n_tools", "{:.1f}")), ("Cost per run (USD)", mean("cost_usd", "{:.3f}")),
        ("Time per run (s)", mean("duration_s", "{:.0f}")),
    ]
    out = ["| | " + " | ".join(m["label"] for m, _, _ in arms) + " |", "|---" * (len(arms) + 1) + "|"]
    for name, f in metrics:
        out.append(f"| {name} | " + " | ".join(f([r for r in rows if keep(r)], judge) for _, rows, judge in arms) + " |")
    return out


def main(dirs):
    arms = [load(d) for d in dirs]
    cases = R.load_suite(arms[0][0]["suite"])
    kind = {c["id"]: c.get("kind", "") for c in cases}
    out = ["## Overall", ""] + headline(arms)
    kinds = list(dict.fromkeys(kind.values()))
    if len(kinds) > 1:
        out += ["", "## By kind of question", "",
                "| Kind | Questions | " + " | ".join(f"{m['label']}: correct · Firecrawl · memory" for m, _, _ in arms) + " |",
                "|---" * (len(arms) + 2) + "|"]
        for k in kinds:
            cells = []
            for _, rows, _ in arms:
                rs = [r for r in rows if kind[r["id"]] == k]
                cells.append(f"{sum(bool(r.get('correct')) for r in rs)}/{len(rs)} · {sum(bool(r.get('used_firecrawl')) for r in rs)} · "
                             f"{sum(r.get('first_web') == 'none' for r in rs)}")
            out.append(f"| {k} | {sum(v == k for v in kind.values())} | " + " | ".join(cells) + " |")
    out += ["", "## Every prompt", "", "Each cell: correct out of 3, then the first web tool per trial.", "",
            "| id | Prompt | Expected | " + " | ".join(m["label"] for m, _, _ in arms) + " |", "|---" * (len(arms) + 3) + "|"]
    for c in cases:
        cells = []
        for _, rows, _ in arms:
            rs = sorted((r for r in rows if r["id"] == c["id"]), key=lambda r: r["trial"])
            cells.append(f"{sum(bool(r.get('correct')) for r in rs)}/{len(rs)} · " + ", ".join(NAMES.get(r.get("first_web"), "?") for r in rs))
        out.append(f"| {c['id']} | {c['prompt']} | {c['answer']} | " + " | ".join(cells) + " |")
    print("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1:])

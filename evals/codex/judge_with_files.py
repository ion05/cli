#!/usr/bin/env python3
"""Judge Codex hardtools runs with the files each run wrote appended to its answer.

Codex often puts long tables in a CSV or Markdown file and links it from a short
chat answer. hardtools/judge_agent.py only sees the chat answer, so those runs
lose credit for data they did collect. This uses the same judge prompt and model,
but appends the text of every file kept under <run dir>/outputs/<id>-t<trial>/
(run_codex.py keeps them) to the answer first.

  python3 evals/codex/judge_with_files.py evals/results/hardtools-codex-*

Writes judge.jsonl next to runs.jsonl; re-running skips runs already judged.
"""
import argparse, concurrent.futures as cf, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "hardtools"))
import judge_agent as J

TEXT = {".csv", ".tsv", ".md", ".txt", ".json", ".html", ".htm", ".yaml", ".yml"}


def with_files(row, outdir, per_file=15000, total=50000):
    d = outdir / "outputs" / f"{row['id']}-t{row['trial']}"
    parts, used = [], 0
    ans = row.get("answer") or ""
    # Files the answer links come first, so scratch files can't crowd them out
    for rel in sorted(row.get("outputs", []), key=lambda r: Path(r).name not in ans):
        f = d / rel
        if f.suffix.lower() not in TEXT or not f.exists():
            continue
        body = f.read_text(errors="replace")
        cut = body[:min(per_file, total - used)]
        if not cut:
            break
        used += len(cut)
        parts.append(f'<file path="{rel}">\n{cut}' + ("\n[... truncated]" if len(cut) < len(body) else "") + "\n</file>")
    if not parts:
        return row
    files = "\n\n".join(parts)
    return dict(row, answer=(row.get("answer") or "") + "\n\nFiles the assistant wrote and linked from its answer "
                "(the user receives these with the answer):\n\n" + files)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dirs", nargs="+")
    ap.add_argument("--reference", default=str(J.R.ROOT / "results" / "hardtools-reference"))
    ap.add_argument("--concurrency", type=int, default=3)
    ap.add_argument("--max-turns", type=int, default=40)
    ap.add_argument("--timeout", type=int, default=1800)
    a = ap.parse_args()
    cases = {c["id"]: c for c in J.R.load_suite("hardtools")}
    rd = Path(a.reference)
    refs = {r["id"]: r.get("answer") for r in map(json.loads, (rd / "runs.jsonl").read_text().splitlines())}
    over = rd / "overrides.json"
    if over.exists():
        for k, v in json.loads(over.read_text()).items():
            refs[k] = (refs.get(k) or "") + "\n\nHand-checked corrections (these win over the text above):\n" + v
    built = json.loads((rd / "meta.json").read_text())["started"]
    for d in map(Path, a.dirs):
        rows = [json.loads(l) for l in (d / "runs.jsonl").read_text().splitlines() if l.strip()]
        out = d / "judge.jsonl"
        done = {(j["id"], j["trial"]) for j in map(json.loads, out.read_text().splitlines()) if "error" not in j} if out.exists() else set()
        todo = [r for r in rows if (r["id"], r["trial"]) not in done]
        print(f"{d.name}: judging {len(todo)}", flush=True)
        with cf.ThreadPoolExecutor(a.concurrency) as ex, out.open("a") as fh:
            futs = {ex.submit(J.judge, cases[r["id"]], with_files(r, d), refs.get(r["id"]), built, a.max_turns, a.timeout): r for r in todo}
            for f in cf.as_completed(futs):
                r = futs[f]
                try:
                    j = f.result()
                except Exception as e:
                    j = {"error": repr(e)[:500]}
                fh.write(json.dumps(dict(j, id=r["id"], trial=r["trial"], with_files=bool(r.get("outputs")))) + "\n"); fh.flush()
                print(f"  {r['id']} t{r['trial']}: {j.get('score', j.get('error'))}", flush=True)


if __name__ == "__main__":
    main()

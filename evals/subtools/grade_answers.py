#!/usr/bin/env python3
"""Grade the answers of subtools-plain / heldout runs, blind across arms.

For each prompt, every run's answer from every arm given (e.g. no skills, original,
final x 3 trials) goes to one Sonnet grader in shuffled order with neutral labels.
The grader may check the live web (Firecrawl CLI, WebFetch) and grades each answer
correct / partial / wrong. One grader per prompt keeps the bar the same for all arms.

  python3 evals/subtools/grade_answers.py evals/results/heldout-cc-{native,original,final}-1021

Writes grade.jsonl next to each runs.jsonl; re-running skips prompts already graded.
Accuracy = correct + half of partial.
"""
import argparse, concurrent.futures as cf, datetime, json, os, random, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import run as R

MODEL = os.environ.get("JUDGE_MODEL", "claude-sonnet-5-5")
PROMPT = """You are grading answers from AI assistants to one task. Today is {today}. Several assistants
answered the same task; their answers are below in random order, labelled A, B, C, ...

<task>
{q}
</task>

{answers}

Work out the right answer yourself first. Check the live web when the answer depends on current
facts (use `firecrawl scrape <url> --max-age 0` or `firecrawl search "<query>"` in Bash, or WebFetch).
Then grade every answer:
- correct: answers what was asked and the facts you can check are right. Small omissions are fine.
- partial: some of it is right but it is incomplete (e.g. a list asked for N items with clearly fewer
  valid ones), or part of it is wrong.
- wrong: the main answer is wrong, missing, or the assistant didn't do the task.
Rules:
- Tasks that change local files or set up a monitor (download, save, monitor/watch) can't be verified
  from here: grade the answer's own report. Asking the user for an alert email or webhook before
  creating a monitor counts as correct; refusing or giving up counts as wrong.
- Local files are not available to you. Their contents: invoice.pdf is invoice #2026-114, billed to
  Northwind Traders, total amount due $1,284.50. quarterly.xlsx has the headers Region, Month, Units,
  Revenue USD, Returns and 37 data rows. pilot-review.docx concludes: roll out self-serve onboarding
  to all teams under 50 seats in Q1 2027 and add two support hires before launch.
- Don't reward length or formatting. Don't penalize an answer for using a different source if its
  facts are right.

End your reply with one JSON object on its own, and nothing after it:
{{"truth": "<one line: what the right answer is>", "grades": {{"A": {{"grade": "correct|partial|wrong", "reason": "<short>"}}, ...}}}}
"""


def last_json(text):
    s = text.rfind('{"truth"')
    return json.loads(text[s:]) if s >= 0 else None


def grade(case, entries, max_turns, timeout):
    rnd = random.Random(case["id"])
    entries = entries[:]
    rnd.shuffle(entries)
    labels = [chr(65 + i) for i in range(len(entries))]
    answers = "\n\n".join(f'<answer label="{l}">\n{(e["row"].get("answer") or "(no answer)")[-4000:]}\n</answer>'
                          for l, e in zip(labels, entries))
    prompt = PROMPT.format(today=datetime.date.today().isoformat(), q=case["prompt"], answers=answers)
    cfg = tempfile.mkdtemp(prefix="fceval-grade-")
    env = {k: os.environ[k] for k in R.PASS_ENV if k in os.environ}
    env["CLAUDE_CONFIG_DIR"] = cfg
    p = subprocess.run(["claude", "-p", prompt, "--model", MODEL, "--output-format", "json", "--max-turns", str(max_turns),
                        "--permission-mode", "bypassPermissions", "--tools", "WebFetch,Bash"],
                       env=env, cwd=cfg, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=timeout)
    out = json.loads(p.stdout)
    j = last_json(out.get("result", ""))
    if j is None:
        raise ValueError("no JSON in grader output: " + out.get("result", "")[-300:])
    cost = (out.get("total_cost_usd") or 0) / len(entries)
    return [dict(j["grades"][l], truth=j["truth"], dir=e["dir"], id=case["id"], trial=e["row"]["trial"], grade_cost_usd=cost)
            for l, e in zip(labels, entries)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dirs", nargs="+")
    ap.add_argument("--concurrency", type=int, default=2)
    ap.add_argument("--max-turns", type=int, default=30)
    ap.add_argument("--timeout", type=int, default=1200)
    ap.add_argument("--only", help="comma-separated case ids")
    a = ap.parse_args()
    dirs = list(map(Path, a.dirs))
    suite = json.loads((dirs[0] / "meta.json").read_text())["suite"]
    cases = {c["id"]: c for c in R.load_suite(suite)}
    only = set(a.only.split(",")) if a.only else None
    by_case = {}
    for d in dirs:
        out = d / "grade.jsonl"
        done = {g["id"] for g in map(json.loads, out.read_text().splitlines())} if out.exists() else set()
        for r in map(json.loads, (d / "runs.jsonl").read_text().splitlines()):
            if r["id"] not in done and (not only or r["id"] in only):
                by_case.setdefault(r["id"], []).append({"dir": str(d), "row": r})
    print(f"{suite}: grading {len(by_case)} prompts", flush=True)
    with cf.ThreadPoolExecutor(a.concurrency) as ex:
        futs = {ex.submit(grade, cases[cid], es, a.max_turns, a.timeout): cid for cid, es in by_case.items()}
        for f in cf.as_completed(futs):
            cid = futs[f]
            try:
                gs = f.result()
            except Exception as e:
                print(f"  {cid}: ERROR {e!r}"[:400], flush=True)
                continue
            for g in gs:
                with (Path(g.pop("dir")) / "grade.jsonl").open("a") as fh:
                    fh.write(json.dumps(g) + "\n")
            print(f"  {cid}: " + " ".join(g["grade"][0] for g in gs), flush=True)


if __name__ == "__main__":
    main()

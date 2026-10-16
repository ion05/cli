#!/usr/bin/env python3
"""Score answer quality in tasks-style results with a model judge.

  python3 evals/judge.py evals/results/hard-only-native evals/results/hard-only-firecrawl

For each run in runs.jsonl it asks the judge model (no tools) to compare the
final answer with the reference, and writes judge.jsonl next to it. Re-running
skips runs already judged.
"""
import concurrent.futures as cf, json, os, re, subprocess, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run as R

R.SUITES["hard"] = R.ROOT / "tasks" / "hard.jsonl"
MODEL = os.environ.get("JUDGE_MODEL", "claude-sonnet-5-5")
RUBRIC = """You are grading a research assistant's answer. Today is 2026-10-16.

Question: {q}
Reference answer (checked by hand on 2026-10-16): {ref}
Assistant's final answer:
<answer>
{ans}
</answer>

Score it and reply with only a JSON object, no prose:
{{"correct": 0 or 1,      // 1 if it gives the reference answer (wording may differ); 0 if wrong, stale, or missing
  "cites_source": 0 or 1, // 1 if it names a specific URL or page where the fact came from
  "faithful": 1-5,        // 5 = every claim is supported or hedged; 1 = confident unsupported or invented claims
  "complete": 1-5,        // 5 = answers every part of the question; 1 = misses most of it
  "concise": 1-5,         // 5 = direct, no padding; 1 = buries the answer
  "note": "<one short sentence>"}}"""


def judge(case, row):
    prompt = RUBRIC.format(q=case["prompt"], ref=case["answer"], ans=row.get("answer") or "(no answer)")
    cfg = tempfile.mkdtemp(prefix="fceval-judge-")
    env = {k: os.environ[k] for k in R.PASS_ENV if k in os.environ}
    env["CLAUDE_CONFIG_DIR"] = cfg
    p = subprocess.run(["claude", "-p", prompt, "--model", MODEL, "--output-format", "json", "--tools", ""],
                       env=env, cwd=cfg, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=300)
    text = json.loads(p.stdout).get("result", "")
    m = re.search(r"\{.*\}", text, re.S)
    return json.loads(m.group(0))


def main(dirs):
    for d in map(Path, dirs):
        meta = json.loads((d / "meta.json").read_text())
        cases = {c["id"]: c for c in R.load_suite(meta["suite"])}
        rows = [json.loads(l) for l in (d / "runs.jsonl").read_text().splitlines() if l.strip()]
        out = d / "judge.jsonl"
        done = {(j["id"], j["trial"]) for j in map(json.loads, out.read_text().splitlines())} if out.exists() else set()
        todo = [r for r in rows if (r["id"], r["trial"]) not in done]
        with cf.ThreadPoolExecutor(6) as ex, out.open("a") as fh:
            futs = {ex.submit(judge, cases[r["id"]], r): r for r in todo}
            for f in cf.as_completed(futs):
                r = futs[f]
                try:
                    j = f.result()
                except Exception as e:
                    j = {"error": repr(e)}
                fh.write(json.dumps(dict(j, id=r["id"], trial=r["trial"])) + "\n"); fh.flush()
        js = [json.loads(l) for l in out.read_text().splitlines() if "error" not in l]
        mean = lambda k: sum(j[k] for j in js) / len(js)
        print(f"{d.name}: n={len(js)} correct={mean('correct'):.0%} cites={mean('cites_source'):.0%} "
              f"faithful={mean('faithful'):.2f} complete={mean('complete'):.2f} concise={mean('concise'):.2f}")


if __name__ == "__main__":
    main(sys.argv[1:])

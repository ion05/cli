#!/usr/bin/env python3
"""Ask Claude why it picked its Firecrawl commands on the hardtools tasks.

Runs each task once with the given skills (same setup as run.py), keeps the
full transcript, then resumes the same session with one follow-up question
about its tool choice. Self-reports are not proof, but they show what the
skill text made the model think about agent, crawl, map and interact.

  python3 evals/hardtools/diagnose.py --skills-ref 0c820ab --label v5 --only a1,a3,n5
"""
import argparse, concurrent.futures as cf, json, os, shutil, subprocess, sys, tempfile, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import run as R

R.SUITES["hardtools"] = HERE / "tasks.jsonl"

WHY = ("Quick debrief on how you did that task, for a tool-design survey. Don't redo any work. "
       "Firecrawl has search, scrape, map, crawl, agent (an autonomous research job that returns JSON for a goal and schema) "
       "and interact (clicks and forms in a live browser). For each of map, crawl, agent and interact: did you consider it, "
       "and why did you use it or not? Quote the part of the skill text, if any, that pushed you either way. "
       "Then say what, if anything, would have made you use `firecrawl agent` here. Keep it under 200 words.")


def run_task(case, skills_src, outdir, model, max_turns, timeout):
    tmp = Path(tempfile.mkdtemp(prefix=f"fcdiag-{case['id']}-"))
    cfg, work = tmp / "cfg", tmp / "work"
    work.mkdir()
    shutil.copytree(skills_src, cfg / "skills")
    env = {k: os.environ[k] for k in R.PASS_ENV if k in os.environ}
    env["CLAUDE_CONFIG_DIR"] = str(cfg)
    base = ["--model", model, "--output-format", "stream-json", "--verbose", "--permission-mode", "bypassPermissions"]
    t0 = time.time()
    try:
        out = subprocess.run(["claude", "-p", case["prompt"], *base, "--max-turns", str(max_turns)], cwd=work, env=env,
                             stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=timeout).stdout
    except subprocess.TimeoutExpired as e:
        out = e.stdout.decode() if isinstance(e.stdout, bytes) else (e.stdout or "")
    dur = time.time() - t0
    (outdir / f"{case['id']}.jsonl").write_text(out)
    sid = next((json.loads(l).get("session_id") for l in out.splitlines() if l.startswith("{") and '"session_id"' in l), None)
    why = ""
    if sid:
        p = subprocess.run(["claude", "-p", WHY, "--resume", sid, *base[:2], "--output-format", "json",
                            "--max-turns", "1", "--permission-mode", "bypassPermissions"],
                           cwd=work, env=env, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=600)
        try:
            why = json.loads(p.stdout).get("result", "")
        except json.JSONDecodeError:
            why = p.stdout[-2000:] + p.stderr[-500:]
    rec = R.score(case, out)
    rec.update(id=case["id"], duration_s=round(dur, 1), why=why)
    shutil.rmtree(tmp, ignore_errors=True)
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skills-ref", required=True)
    ap.add_argument("--label", required=True)
    ap.add_argument("--only")
    ap.add_argument("--model", default="claude-sonnet-5-5")
    ap.add_argument("--max-turns", type=int, default=80)
    ap.add_argument("--timeout", type=int, default=2400)
    ap.add_argument("--concurrency", type=int, default=2)
    a = ap.parse_args()
    cases = R.load_suite("hardtools")
    if a.only:
        cases = [c for c in cases if c["id"] in set(a.only.split(","))]
    outdir = HERE.parent / "results" / f"diagnose-{a.label}"
    outdir.mkdir(parents=True, exist_ok=True)
    skills_src = Path(tempfile.mkdtemp(prefix="fcdiag-skills-")) / "skills"
    R.export_skills(a.skills_ref, skills_src)
    rows = outdir / "runs.jsonl"
    done = {json.loads(l)["id"] for l in rows.read_text().splitlines()} if rows.exists() else set()
    cases = [c for c in cases if c["id"] not in done]
    with cf.ThreadPoolExecutor(a.concurrency) as ex, rows.open("a") as fh:
        futs = {ex.submit(run_task, c, skills_src, outdir, a.model, a.max_turns, a.timeout): c for c in cases}
        for f in cf.as_completed(futs):
            try:
                r = f.result()
            except Exception as e:
                r = dict(id=futs[f]["id"], error=repr(e))
            fh.write(json.dumps(r) + "\n"); fh.flush()
            print(r["id"], r.get("fc_cmds"), r.get("skills"), flush=True)


if __name__ == "__main__":
    main()

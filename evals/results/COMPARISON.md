# Told to use Firecrawl vs left alone

Skills `22358f2`, Claude Code 2.1.302, Sonnet 5.5, 3 trials per question, run 2026-10-16.
"Told" runs prefix each prompt with `Use Firecrawl to look this up on the web.` (`evals/compare.py --force-firecrawl`).
Hard questions (`evals/tasks/hard.jsonl`) ask about facts from after the model's training data; answers were checked on 2026-10-16.

| Suite | Mode | Correct | Used Firecrawl | Mean tool calls | Mean cost (USD) | Mean time (s) |
|---|---|---|---|---|---|---|
| easy (14 q) | left alone | 42/42 | 0/42 | 0.8 | 0.036 | 6 |
| easy (14 q) | told | 40/42 | 42/42 | 3.9 | 0.068 | 39 |
| hard (8 q) | left alone | 23/24 | 2/24 | 2.3 | 0.049 | 15 |
| hard (8 q) | told | 18/24 | 24/24 | 3.7 | 0.069 | 39 |

Per hard question (correct out of 3, left alone / told): h01 3/3, h02 3/3, h03 3/0, h04 3/0, h05 2/3, h06 3/3, h07 3/3, h08 3/3.

## What the misses were

- **h03, h04 (told, 0/6): stale cache.** The agent scraped `registry.npmjs.org/<pkg>/latest` with `firecrawl scrape`, which by default
  returns a cached copy up to 2 days old (`maxAge` 172800000 ms). It reported firecrawl-cli 1.26.3 and Claude Code 2.1.301; the live
  values were 1.26.7 and 2.1.302. Re-running the same scrape with `--max-age 0` returns 1.26.7. The skills never mention `--max-age`.
  Left alone, the agent used `npm view` and got both right.
- **t13 (told, 1/3): grader too strict.** The page signs off "Erik S. and Barry Zhang"; two runs quoted that faithfully and didn't
  guess the surname "Schluntz", which the regex requires. Arguably the told runs were more faithful to the source.
- **h05 (left alone, 1 miss):** `gh api` was refused in the sandbox and the agent gave up instead of trying another route.

## Caveats

- Firecrawl rate limits showed up in 46 of the 66 told runs (three suites ran at once, 12 agents in parallel); retries inflate time.
- `REPORT.md` for the `hard-*` runs has no per-question correct column, because `run.py report` only adds it when the suite is
  named `tasks`. The numbers above come from `runs.jsonl`.

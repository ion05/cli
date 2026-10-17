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
- `REPORT.md` for the `hard-*` runs now has a per-question correct column (`run.py` registers the `hard` suite).

# Built-in search only vs Firecrawl only

Both modes block tools with `--disallowedTools` as well as saying so in the prompt (`evals/compare.py --only-tools`).
`native`: WebSearch/WebFetch or memory, no Bash, no skills installed. `firecrawl`: Firecrawl CLI only; WebSearch, WebFetch,
curl, wget, npm, gh, python, node and git blocked. 20 max turns, 3 trials. Quality scores come from `evals/judge.py`
(Sonnet 5.5 judge, no tools, compares each final answer to the reference).

| Suite | Mode | Correct (regex) | Correct (judge) | Cites a source | Faithful /5 | Complete /5 | Concise /5 | Cost (USD) | Time (s) |
|---|---|---|---|---|---|---|---|---|---|
| easy | built-in | 42/42 | 100% | 14% | 4.31 | 4.90 | 4.31 | 0.017 | 5 |
| easy | Firecrawl | 40/42 | 93% | 86% | 4.21 | 4.79 | 4.26 | 0.061 | 39 |
| hard | built-in | 21/24 | 88% | 96% | 4.12 | 4.50 | 4.46 | 0.037 | 12 |
| hard | Firecrawl | 21/24 | 88% | 83% | 4.00 | 4.75 | 4.17 | 0.073 | 43 |

- Built-in mode answered 37 of 42 easy runs from memory, which is why it rarely cites a source there.
- Built-in misses: h05 (latest merged PR in firecrawl/cli) 0/3. WebSearch/WebFetch never reached the merged-PR list; the agent asked the user to run `gh`.
- Firecrawl misses: h04 (Claude Code version) 0/3, the same stale cache as before (2.1.301 vs live 2.1.302); t13 2/3 (grader wants "Schluntz", page says "Erik S.").
- h03 (firecrawl-cli version) went from 0/3 to 3/3 for Firecrawl only because my manual `--max-age 0` check earlier refreshed Firecrawl's cache. That's a fluke of test order, not a fix.
- Rate limits hit in 44 of 66 Firecrawl-only runs (212 errors, all req/min); retries make up much of the time gap.

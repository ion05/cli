# Quality with the v1 skill descriptions (PR #4), Claude choosing its own tools

No tool named in the prompt, nothing blocked. Sonnet 5.5, 3 trials, concurrency 2, run 2026-10-17.
Easy = `tasks` (12 max turns), hard = `evals/tasks/hard.jsonl` (20 max turns). Quality columns come from `evals/judge.py`.
Two hard answers moved overnight and were updated before these runs: h03 firecrawl-cli 1.26.7 → 1.26.8,
h05 latest merged PR #319 → #321. The hard baseline was re-run the same day (`hard-baseline-1017`) so both sides grade against the same answers.
The easy baseline is `tasks-baseline` from 2026-10-16 (its answers don't change).

| Suite | Skills | Correct (regex) | Correct (judge) | Used Firecrawl | Used WebSearch/WebFetch | Cites a source | Faithful /5 | Complete /5 | Concise /5 | Cost (USD) | Time (s) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| easy | baseline 22358f2 | 42/42 | 95% | 0/42 | 15/42 | 31% | 4.43 | 4.81 | 4.31 | 0.036 | 6 |
| easy | desc v1 | 42/42 | 98% | 6/42 | 2/42 | 26% | 4.40 | 4.88 | 4.40 | 0.036 | 6 |
| hard | baseline 22358f2 | 21/24 | 88% | 2/24 | 18/24 | 62% | 4.08 | 4.54 | 4.38 | 0.049 | 10 |
| hard | desc v1 | 21/24 | 88% | 12/24 | 0/24 | 54% | 3.83 | 4.67 | 4.17 | 0.049 | 7 |

First web tool, easy: baseline none 27 / native 15; v1 none 28 / firecrawl 6 / other shell 6 / native 2.
First web tool, hard: baseline native 15 / other shell 9; v1 other shell 15 / firecrawl 9.

## Findings

- The descriptions pushed out WebSearch/WebFetch (33 of 66 runs → 2), but on these questions the agent mostly replaced them
  with `curl` to JSON APIs (nodejs.org/dist/index.json, api.github.com, python.org API, HN Firebase), `npm view`, or memory, not Firecrawl.
  Firecrawl use went from 2 of 66 runs to 18 of 66. The trigger suite's 85% does not carry over to research questions with an obvious API.
- Accuracy, cost and time didn't change. Faithfulness dipped on hard (4.08 → 3.83), driven by h05.
- h05 (latest merged PR) is 0/3 in both arms for the same reason: Firecrawl served a cached copy of the GitHub PR list from the
  day before ("merged 6 hours ago", #319), so the agent missed #321, merged 24 minutes before the run. Same stale-cache problem as the npm
  questions on 2026-10-16; the skills still don't mention `--max-age`.
- Judge "correct" below 100% on easy is an artifact: `run.py` keeps only the last 1,500 characters of each answer, so the judge saw t05's
  list cut off at the start and marked it incomplete. The regex column is the reliable one for t05.
- No Firecrawl rate-limit errors at concurrency 2.

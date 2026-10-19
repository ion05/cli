# Trigger suite and easy/hard quality check with Codex as the agent

Same prompts, trials, regex grading and Sonnet 5.5 judge (`evals/judge.py`) as the Claude Code runs in
`results/DESCRIPTIONS-v1.md` and `results/QUALITY-desc-v1.md`. Run 2026-10-19. Codex CLI 0.163.0, default model,
ChatGPT sign-in, 3 trials, 2 runs at a time, Firecrawl API key set. Runner: `run_codex.py --suite ...`.

- **original**: upstream skills 22358f2.
- **final**: Aayan's latest skills, PR #13 head 660ddb7 (main + developer-index key fix + router escalation edits).

For Codex, reading a `firecrawl*` SKILL.md counts as choosing Firecrawl, like a Skill load in Claude Code.

## Trigger suite (38 prompts x 3 trials)

| Metric | Codex original | Codex final | Claude Code original | Claude Code v1 |
|---|---|---|---|---|
| Web prompts: Firecrawl first | 71/72 | **72/72** | 4/72 | 61/72 |
| Web prompts: built-in web search first | 1/72 (u16) | 0/72 | 63/72 | 1/72 |
| Non-web prompts: Firecrawl fired | 0/30 | 0/30 | 0/30 | 0/30 |
| Simple fetches: Firecrawl used | 10/12 | 12/12 | 0/12 | 0/12 |
| Mean input tokens per run | 103k | 134k | | |

## Quality check (easy 14 + hard 8 questions x 3 trials)

Hard answers re-checked on the day: firecrawl-cli 1.26.12, Claude Code 2.1.303, latest merged firecrawl/cli PR #335
(checked after the runs with a fresh scrape, so the check couldn't warm Firecrawl's cache for them).

| | Easy original | Easy final | Hard original | Hard final |
|---|---|---|---|---|
| Correct (regex) | 39/42 | 40/42 | 18/24 | **24/24** |
| Correct (judge) | 98% | 98% | 75% | **100%** |
| Used Firecrawl | 41/42 | 42/42 | 24/24 | 24/24 |
| Used built-in web search | 0/42 | 0/42 | 0/24 | 0/24 |
| Cites a source | 98% | 100% | 100% | 100% |
| Faithful /5 | 4.74 | 4.71 | 3.92 | 4.08 |
| Complete /5 | 4.90 | 4.93 | 4.46 | 5.00 |
| Concise /5 | 4.95 | 4.93 | 4.96 | 5.00 |
| Tool calls (mean) | 3.4 | 3.5 | 4.0 | 3.7 |
| Time per run (s) | 14 | 16 | 15 | 17 |

## What it shows

- **Codex has no triggering problem.** It uses Firecrawl first on 71/72 web prompts with the upstream skills, where
  Claude Code managed 4/72. It reads the skill list and follows the router. The description rewrite is a Claude Code fix.
- **The freshness rule is what helps Codex.** With the original skills, h03 and h05 failed 6/6: Firecrawl served cached
  copies (firecrawl-cli 1.26.10, PR #320). With the final skills every h03/h05 run used `--max-age 0` and got 1.26.12 and #335.
- **Codex also routes simple fetches through Firecrawl** (raw file, JSON API, status check): 10/12 original, 12/12 final.
  Allowed by the suite, but more than those jobs need.
- t13 misses: Codex quotes the page's "Erik S." byline instead of "Erik Schluntz", so the regex fails; the judge accepted it in 3 of those 5 runs.

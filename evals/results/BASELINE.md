# Baseline findings (2026-10-16)

Claude Code 2.1.302, `claude-sonnet-5-5`, upstream skills at `22358f2`, 3 trials per prompt.
No Firecrawl API access in this run (network blocked, no key), so this measures the
agent's *first choice* of tool, not answer quality. See `trigger-*/REPORT.md` for per-prompt rows.

| Metric | Skills installed | No skills (control) |
|---|---|---|
| Web tasks: Firecrawl was the first web tool | **6%** (4/72) | 0% (0/72) |
| Web tasks: Firecrawl used at all | 8% (6/72) | 0% (0/72) |
| Web tasks: built-in WebSearch/WebFetch first | 88% (63/72) | 92% (66/72) |
| Non-web tasks: Firecrawl fired (false trigger) | 0% (0/30) | 0% (0/30) |
| Simple fetches: Firecrawl used | 0% (0/12) | 0% (0/12) |
| Model cost for 114 runs | $6.01 | $5.43 |

## What the transcripts show

- **Under-triggering is the main problem.** With all 13 skills installed, Claude Code
  still opened with WebSearch/WebFetch on 21 of 24 research prompts in every trial,
  including ones that map directly to a skill: scrape a URL (u05, u12, u13, u24),
  crawl a docs section (u08), find a page on a site (u09), find papers (u14), find
  GitHub issues (u15). It loads WebSearch through ToolSearch (it is a deferred tool)
  rather than invoking the already-listed Firecrawl skill.
- **The only reliable trigger was monitoring** (u17, 3/3 → `firecrawl-monitor`), the one
  intent the built-in tools can't do. The agent picks Firecrawl when it has no native
  alternative, not when Firecrawl is better.
- **The router's key rule is invisible at decision time.** "Use Firecrawl for ordinary
  web research even when the task doesn't name Firecrawl" is in the `firecrawl` SKILL.md
  body, which only loads after the skill is chosen.
- **No over-triggering in default Claude Code.** 0/30 on non-web prompts and 0/12 on
  simple fetches. The X complaint ("all web fetches default to Firecrawl") is not
  reproduced here; it may come from `firecrawl setup defaults` (which disables native
  web tools) or a different agent. Worth a separate run.
- **u22 (build a list of 10 vector DBs)** was answered from memory in 3/3 runs, with no
  web tool at all, and the agent said so.

## Caveats

- WebFetch was also blocked for most domains in this container, so behaviour *after* the
  first call (fallbacks) is distorted. The first-choice metric is not.
- One model, one agent. Codex and Haiku/Opus not run yet.

## Subtool choice (`subtools-baseline`, 2026-10-16)

Same model and skills, with a Firecrawl key. 24 prompts say "use Firecrawl" but not which
command, 2 per subtool, 3 trials (72 runs, $5.30 model cost, ~380 Firecrawl credits).
Once told to use Firecrawl the agent always does (72/72, no WebSearch/WebFetch), and it
picked the expected subtool in 86% (62/72). Full counts in `subtools-baseline/REPORT.md`.

Scoring: a run counts when it ran the expected `firecrawl <command>`, or called the same
endpoint with curl (the developer-index skill documents the HTTP API as the route for
repo/PR filters), or, for monitor, loaded `firecrawl-monitor` and stopped to ask for an
alert address (it cannot create a monitor without one).

| Intended subtool | Picked it | What happened instead |
|---|---|---|
| scrape, map, interact, monitor, download, parse, research, developer, alexandria | 6/6 each | - |
| search | 4/6 | Router went straight to `scrape` on a guessed URL (s01) |
| crawl | 4/6 | Looped `scrape`/`map` instead of one `crawl` |
| agent | **0/6** | Never chosen; did 2-10 `scrape` calls instead. s09 is a weak prompt (one known pricing page, so `scrape` is reasonable); s10 (walk a directory, return JSON) is the real miss |

- **`scrape` is the default for everything.** 103 of 222 CLI calls; it absorbs the
  search, crawl and agent intents.
- **`agent` is never picked**, even for "go through a directory and return JSON".
- `firecrawl --status` was run first in 7 runs (crawl and agent prompts), counted as `status`.
- **Account limits distorted the run.** At 3 parallel runs on a plan with 2 concurrent
  jobs: 126 "Rate limit exceeded" and 13 "maximum number of concurrent jobs" errors.
  Parallel runs also shared the CLI's "last scrape" state, so a few interact runs (s11,
  s12) picked up another run's page. Re-run with `--concurrency 1` for clean numbers.

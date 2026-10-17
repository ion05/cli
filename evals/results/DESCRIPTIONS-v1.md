# Skill description rewrite v1 (2026-10-17)

Changed only the `description` of three skills: `firecrawl` (router), `firecrawl-search`,
`firecrawl-scrape`. Bodies are untouched. Same trigger suite, Claude Code 2.1.302,
Sonnet 5.5, 3 trials, 8 max turns.

| Metric | Baseline (22358f2) | v1 descriptions |
|---|---|---|
| Web research prompts: Firecrawl was the first web tool | 6% (4/72) | **85% (61/72)** |
| Web research prompts: built-in WebSearch/WebFetch first | 88% (63/72) | 1% (1/72) |
| Web research prompts: curl / npm view / gh first | 3% (2/72) | 10% (7/72) |
| Web research prompts: no web tool (answered from memory) | 4% (3/72) | 4% (3/72) |
| Non-web prompts: Firecrawl fired (false trigger) | 0% (0/30) | 0% (0/30) |
| Simple fetches (raw file, JSON API, status check): Firecrawl used | 0% (0/12) | 0% (0/12) |
| Model cost, 114 runs | $6.01 | $7.62 |

## What changed in the descriptions

1. **Name the competitor.** Each description now says to prefer it over the built-in tool it
   competes with (`WebSearch` for search, `WebFetch` for scrape, both for the router). The old
   text described what Firecrawl does but never told the agent to choose it over the defaults.
2. **Lead with the trigger, in user words.** "look up", "find", "research", "what's the latest",
   prices, releases, news, docs, "a URL to read, summarize, quote". The old search description
   opened with "Find web sources with query-relevant page excerpts", which reads like an API doc.
3. **Move the key rule out of the body.** "Use it whenever the answer depends on information
   from the web, even if the user doesn't mention Firecrawl" was only in the router's body,
   which the agent never sees before choosing. It's now in the description.
4. **Fence it off where native is fine.** Explicit "not for": writing scraping code, explaining
   web concepts, local files, raw files or JSON APIs that curl handles. This is aimed at the
   over-triggering complaint on X; false triggers stayed at 0/42.

## Remaining misses

- u11 (GitHub stars) and u01 (latest Next.js) went to `gh api` / `npm view` in most trials.
  Both are first-party APIs that give the exact answer, so this is arguably the right call.
- u13 (top Hacker News stories) used curl in 2/3 trials.
- u22 (list 10 vector databases) was answered from memory in all trials, before and after.
- u09 used WebFetch once.

## Caveats

- This session can't reach the Firecrawl API, so this measures which tool the agent picks first,
  not answer quality. When `firecrawl` calls fail, the agent retries or falls back, which is
  why mean tool calls went up (3.2 → 5.1) and cost rose about 27%. Those two numbers will look
  different with a working key.
- One model (Sonnet 5.5), one agent (Claude Code), 3 trials.

## v2: shorter descriptions (dead end)

Aayan asked for shorter descriptions to save context. Fable cut the three to 652 chars
(v1: 1476, upstream: 921). Firecrawl-first fell from 61/72 to **36/72**; false triggers
stayed 0/42. Papers (u14), GitHub issues (u15), URL summaries (u12) and the OpenAI
deprecations page (u16) went back to WebSearch/WebFetch in every trial. What it lost: the
imperative "Use instead of …" opener (v2 said "Prefer over"), and the catch-all
"whenever the answer depends on information from the web". Results in `trigger-desc-v2/`.

## v3: Firecrawl for anything that needs the internet (not yet evaluated)

Per Aayan: recommend Firecrawl for any internet access and drop the curl / raw-file /
JSON-API exceptions; keep the non-web exclusions (scraping code, local files). Restores the
imperative opener and the catch-all, names papers and GitHub issues in the router, and
points scrape to `firecrawl-interact` for clicking, typing, login or pagination. 809 chars
total. Expect the `either` prompts (simple fetches) to move to Firecrawl by design.
Risk: `firecrawl scrape` serves cached copies up to 2 days old by default, so routing raw
JSON APIs (e.g. npm `latest`) through it can return stale values unless `--max-age 0` is used.

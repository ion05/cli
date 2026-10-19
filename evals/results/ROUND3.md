# Round 3: freshness, developer index, and pushing agent / crawl / interact

Run 2026-10-19, Sonnet 5.5, Claude Code 2.1.303, concurrency 2. **main** is ion05/cli main after merging #4, #6, #8-#12 (3b90544). **boost** adds the router edit (7cc9fc8). **final** adds the developer-index fix too (fa268d1).

## Changes

1. **Router escalation** (`skills/firecrawl/SKILL.md`): `agent` was missing from the escalation steps. Added it ("a list of records spread over pages you don't know yet … start it without `--wait`, poll the job ID"), and gave crawl and interact concrete triggers ("more than 2-3 pages from one site", "data appears only after you act on the page … instead of guessing URL parameters").
2. **Developer index** (`skills/firecrawl-developer-index/SKILL.md`): the skill said the HTTP API is "keyless", so agents called it with `curl` and no key and hit the free-tier rate limit after 2-3 calls. It now says to send the key, and that the index lags GitHub, so current state (latest merged PR, open issues) comes from scraping GitHub with `--max-age 0`.
3. **Freshness**: the `--max-age 0` rule was already in main (added in #4 after the last hard-suite run), so this round measures it rather than adding it.

## Hard suite (8 questions newer than training data, 3 trials, regex-graded)

Answers re-checked on 2026-10-19 without Firecrawl (npm registry, nodejs.org, endoflife.date, a git clone of firecrawl/cli): h03 is now 1.26.10, h04 2.1.303, h05 #320.

| | v3 (88f0c2d, no freshness rule) | main (freshness rule) | final (+ developer fix) |
|---|---|---|---|
| Correct | 22/24 | 21/24 | **24/24** |
| h05 (latest merged PR) | 1/3 | 0/3 | **3/3** |
| h03 / h04 (npm versions) | 6/6 | 6/6 | 6/6 |
| Runs that used `--max-age 0` | 0 | 3 | 4 |
| Used Firecrawl | 17/24 | 17/24 | 17/24 |
| Cost per run | $0.059 | $0.059 | $0.060 |

- The freshness rule is followed when the agent scrapes, but no question changed because of it: the npm questions all go to `npm view`, which is live.
- Every miss was h05. The agent tried `gh` and the GitHub API (blocked in this container), then the developer index with no key, got rate-limited, and gave up. With the fix it scrapes the merged-PR list and answers correctly.
- Caveat: GitHub is blocked for `curl`/`gh`/WebFetch in this container, so h05 measures the fallback path. On a machine with `gh` signed in, `gh` would answer it.

## Subtools-plain (crawl, agent, interact prompts only: s07-s12, 3 trials)

| | main | boost |
|---|---|---|
| Ran the intended command | 14/18 | 15/18 |
| crawl (s07, s08) | 6/6 | 6/6 |
| agent (s09, s10) | 2/6 | 3/6 |
| interact (s11, s12) | 6/6 | 6/6 |
| Cost per run | $0.070 | $0.066 |

s09 ("30 companies using Rust in production") is answered from memory in every arm, with no web call at all.

## Hard-tools (15 multi-site tasks, i2 dropped, 2 trials, Sonnet judge 0-100)

| | main | boost |
|---|---|---|
| Judge score (mean) | 75 | **83** |
| Runs scoring 70+ | 21/30 | 26/30 |
| Runs under 20 | 2/30 | 0/30 |
| Cites sources | 70% | 77% |
| `crawl` calls | 0 | 0 |
| `agent` calls | 3 | 0 |
| `interact` calls | 66 | 38 |
| Ran an intended command | 15/30 | 13/30 |
| Cost per run | $0.41 | $0.40 |
| Time per run | 4.2 min | 2.8 min |

By kind: interact 74 → 89, map 67 → 75, crawl 84 → 82, agent 75 → 83. Full tables: [`../hardtools/RESULTS-round3-tables.md`](../hardtools/RESULTS-round3-tables.md).

- **The edit did not make agents use `crawl` or `agent`.** Crawl stayed at 0 calls and agent fell from 3 to 0.
- **The score went up anyway**, mostly because fewer runs collapsed: main had i3 at 8 (32 `interact` calls in a loop), a5 at 0, and m1/m3 in the 50s. With 2 trials, read +8 as "no worse, probably better", not a measured gain.
- **Why crawl loses:** on c1 (every Slack API method) the agent scraped the index page, pulled 340 method URLs, and ran `xargs -P 4 firecrawl scrape` over them. That is a crawl the agent controls: it only fetches the pages it needs, finishes in minutes, and needs no polling. `agent` takes 2-5 minutes and returns less control. Under-use of crawl and agent looks like a reasonable choice, not a routing bug.

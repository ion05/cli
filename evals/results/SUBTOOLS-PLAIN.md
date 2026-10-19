# Picking the right command when the prompt doesn't mention Firecrawl (2026-10-17)

Suite `subtools-plain`: the 24 subtool jobs with "Use Firecrawl" removed (s09 swapped for a
job-board prompt). Sonnet 5.5, Claude Code 2.1.302, 3 trials, 2 runs at a time.

| | PR #4 skills (`desc-v1`) | + crawl/agent/developer descriptions (`desc-v2`) |
|---|---|---|
| Ran the expected Firecrawl command | 67% (48/72) | **79% (57/72)** |
| Used Firecrawl at all | 78% (56/72) | 86% (62/72) |
| Used built-in WebSearch/WebFetch | 10% (7/72) | 3% (2/72) |
| Mean cost / duration | $0.062 / 15s | $0.064 / 15s |

| Subtool | v1 | v2 | What changed |
|---|---|---|---|
| developer | 1/6 | **6/6** | Was `curl` to the GitHub API + WebSearch. Description now names "issues or PRs in owner/repo" and the tools it replaces. |
| crawl | 4/6 | **6/6** | Was map + scrape loops. Description now names "the first N pages under a URL" and says one job, not a loop. |
| agent | 0/6 | 1/6 | Still search + scrape, or `curl` to the Greenhouse JSON feed behind Cloudflare's job board. |
| search, scrape, download | 16/18 | 18/18 | Untouched skills; noise. |
| map | 5/6 | 4/6 | Untouched; s06 went to WebFetch twice. Noise or a real gap, not tested further. |
| interact, parse, alexandria | 11/18 | 10/18 | Untouched. |

## Misses that are probably fine

Most remaining misses got a good answer with a cheaper tool, so "ran the expected command" undercounts:

- **agent (s09, s10):** `curl` on the Greenhouse API, or `search` + 2-3 scrapes of the YC directory, answered in 20-35s. The one `agent` run took 87s. Pushing harder toward `agent` would likely make these slower and costlier for no better answer.
- **interact (s11):** every run curled `news.ycombinator.com/newest`, the page the "new" link points to, instead of clicking.
- **alexandria (s23):** `curl` on the official HN Firebase API, which is a ready-made data source.
- **parse (s18):** `pdftotext` on a one-page text PDF.

Next step if we want a fairer number: grade the answer (judge.py) instead of the command.

## After these runs (not yet re-run)

Following Firecrawl's docs ("do you know which page has the data?"): the agent description now leads
with "you don't know which pages hold the data" and a scale cue (dozens of records), and interact says
to scrape first and stop the session when done. Prompts s09 and s10 now ask for 30 records, and s11 is
a login form instead of the HN "new" link. The numbers above used the old s09-s11 prompts.

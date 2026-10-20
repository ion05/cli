# Round 4: tool choice on Claude Code, checked for accuracy

Run 2026-10-19/20, Sonnet 5.5, Claude Code 2.1.304, firecrawl-cli 1.26.12, 2 trials, concurrency 2.
**final** = the PR #13 skills (660ddb7). Codex was paused for this round.

## Headline: the final skills already pick the right command, and the answers are right

| Suite | Ran the right command | Answer accuracy (checked against the live web) |
|---|---|---|
| subtools-plain (24 prompts, the set we tuned on) | **45/48 (94%)** | 48/48 correct |
| held-out (12 new prompts, never tuned on) | 16/24 (67%) | 20/24 correct, 4 partial, 0 wrong |
| Cost per run | $0.063 / $0.076 | |

The last full subtools-plain run (2026-10-17, older skills) was 57/72 (79%).

- **subtools-plain misses:** s09 (30 Rust companies) is answered from memory in both trials with no web call, so it never ran `agent`. s20 ran WebSearch once instead of `research`.
- **Held-out misses are mostly good answers by a cheaper route:** h02 scraped the section's index page instead of crawling (the sidebar lists all 25 pages, and the list was complete). h07 read the .xlsx with Python instead of `parse`. h05 gave the Stripe URL from memory once (correct). h04 ("15 hospitals posting NP jobs") used search + scrape, not `agent`.
- **Over-routing check:** on the 4 held-out prompts where plain scrape or search is right (h09-h12), `agent`, `crawl` or `interact` never ran (8/8 clean).
- **Accuracy:** a Sonnet grader re-checked every answer with `firecrawl scrape --max-age 0` (`accuracy-r4-base.jsonl`). The 4 partials were list tasks that came up short (h03 11 of 20 YC fintech companies, h04 14 of 15 hospitals or a search-page link, h06 an incomplete WebSocket URL list). The grader did not verify h08, h09, the s19 paper IDs or the h04 job links, and s09/s10 answers were truncated at 4000 chars.

## Things we tried that did not help (reverted)

Both came from a Fable advisor review of the transcripts.

**A. Pick the command by task shape** (de1229c): replaced the router's 7-step escalation ladder with a decision list keyed on the task (have a URL? how many pages? URLs known? must act on the page?), said to pass many URLs to one `scrape` instead of a loop, and added one-line "not for" limits to agent, crawl and interact (one agent job per task, no crawl when you already hold the URLs).

| | final | A |
|---|---|---|
| subtools-plain | 45/48 | 45/48 |
| held-out | 16/24 | 16/24 |
| 6 hard tasks (c1, c3, a3, a4, m1, m3; judge 0-100) | 77 (2 trials, from Round 3) | 73 (1 trial) |

One `crawl` appeared on c3 that had never run before. Nothing else moved.

**B. Agent for directory lists, then fill the gaps** (b103c32, on top of A): run by hand, `firecrawl agent` found all 45 Purdue ML/NLP faculty for a4 in one job but left the 2025 paper empty for 27, so the idea was "agent for the list, scrape only the empty fields". The router and agent description said so, with time and cost cues. Partial run (stopped early): `agent` ran 0 times on h03, h04, a1 or a3. h03 got worse (0/2).

## Why tool choice has stopped moving

- Simple prompts are saturated. The remaining misses are memory answers, or a cheaper tool that gave a correct answer.
- On realistic tasks Claude scrapes an index page and then the pages it needs. Round 3 already showed this scores as well as crawl or agent. Wording changes in the skills don't move it, and accuracy doesn't need them to.
- Next gains are in answer completeness on list tasks (the 4 partials), not in routing.

## Files

- `subtools/heldout.jsonl`, `subtools/fixtures/quarterly.xlsx`: the held-out set. It adds `acceptable` (other commands that are fine) and `forbid` (over-routing counts as a miss) to the scoring in `run.py`.
- `results/subtools-plain-r4-*`, `results/heldout-r4-*`, `results/hardtools-tree`, `results/hardtools-hybrid` (partial), `results/accuracy-r4-base.jsonl`.

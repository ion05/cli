# Hard multi-site tasks with Codex as the agent

Same 16 tasks, rubric, reference answers and Sonnet 5.5 judge agent as [the Claude Code run](../hardtools/RESULTS.md). Run 2026-10-17/18. Codex CLI 0.163.0 with its default model `gpt-6.1-sol` (default reasoning effort), signed in with a ChatGPT account, 2 trials per task, 2 runs at a time. Runner: [run_codex.py](run_codex.py).

- **codex-native**: no skills, `firecrawl` shadowed by a stub and the API key removed. Codex's own live `web_search` and the shell (curl etc.) stay available.
- **codex-original**: upstream skills at 22358f2, copied into `$CODEX_HOME/skills`.
- **codex-mine**: PR #6 skills at a3648a8.

The first three columns are the Claude Code (Sonnet 5.5) numbers from the earlier run, for comparison.

## What it shows

- **Firecrawl helps Codex too: 68 with no Firecrawl, 77 with the original skills, 74 with yours.** For Claude Code it was 62, 69 and 75. Codex scores higher than Claude Code without skills and with the original skills, and about the same with yours.
- **Codex doesn't have Claude Code's under-triggering problem.** With the original skills, Codex used Firecrawl in 32/32 runs and Claude Code in 6/32. Codex reads the router `SKILL.md` and follows it. The description rewrites in PR #4/#6 fix a Claude Code problem that Codex doesn't have.
- **Your skills push Codex onto `agent` and `crawl`.** It made 104 `agent` and 35 `crawl` calls, against 0 and 6 with the original skills. Claude Code never ran `crawl`. Map-shaped tasks gained (84 vs 72), and m1 went from 96/22 to 96/96. Interact-shaped tasks lost (47 vs 67). i4 and i5 went to `agent` when a scrape of the YC directory or the Chrome Web Store would have done.
- **The biggest loss is a scoring artifact: Codex writes long tables to files and links them.** i4 with your skills got the count exactly right (42 = 18 + 24) but put the company list in `output/yc-2025-developer-tools.csv`. The judge only sees the chat answer, so it scored 15 and 35. a4 did the same in several arms. Without this, your skills would likely tie or beat the original. A fair fix is to give the judge the files the agent wrote.
- **Without Firecrawl, Codex can't drive forms.** i3 (USPS price calculator) scored 0 in both native runs because the calculator needs a browser. With either skill set it scored 97 via `firecrawl interact`.
- **i2 (California SOS) is still unanswerable** for every agent and arm.
- **Cost:** the USD row is not real money. The runs used a ChatGPT plan, and the row prices tokens at a placeholder $1.25 / $0.125 / $10 per 1M (input / cached / output). Token use is the real number. Per run, the average was 1.2M input tokens with no Firecrawl, 1.65M with the original skills and 2.45M with yours, about 94% of it cached. Output was 5k, 7k and 8k tokens. Your skills make Codex run about 40% more tool calls than the original skills (62 vs 45) and take 3.7 min vs 2.8 min.
- **"Turns" is always 1 for Codex,** because one `codex exec` call is one turn. Compare tool calls instead.
- **Noise:** this is 2 trials per task, as before. Differences under ~5 points per kind are noise.

## Overall

| | native | original | mine | codex-native | codex-original | codex-mine |
|---|---|---|---|---|---|---|
| Judge score (mean /100) | 62 | 69 | 75 | 68 | 77 | 74 |
| Runs scoring 70+ | 17/32 | 21/32 | 23/32 | 19/32 | 24/32 | 22/32 |
| Runs scoring under 20 | 5/32 | 3/32 | 2/32 | 4/32 | 2/32 | 3/32 |
| Cites sources | 91% | 91% | 81% | 94% | 100% | 100% |
| Faithful /5 | 3.94 | 3.84 | 4.00 | 4.16 | 4.28 | 4.00 |
| Used Firecrawl | 0/32 | 6/32 | 32/32 | 0/32 | 32/32 | 32/32 |
| Ran an intended command | 0/32 | 6/32 | 16/32 | 0/32 | 18/32 | 23/32 |
| `firecrawl search` calls | 0 | 0 | 67 | 0 | 272 | 356 |
| `firecrawl scrape` calls | 0 | 29 | 254 | 0 | 329 | 446 |
| `firecrawl map` calls | 0 | 0 | 13 | 0 | 10 | 4 |
| `firecrawl crawl` calls | 0 | 0 | 0 | 0 | 6 | 35 |
| `firecrawl agent` calls | 0 | 0 | 2 | 0 | 0 | 104 |
| `firecrawl interact` calls | 0 | 35 | 56 | 0 | 150 | 179 |
| Used WebSearch/WebFetch | 26/32 | 22/32 | 0/32 | 32/32 | 1/32 | 0/32 |
| Tool calls (mean) | 30.8 | 31.6 | 21.2 | 17.9 | 44.7 | 62.5 |
| Turns (mean) | 19.2 | 21.1 | 16.4 | 1.0 | 1.0 | 1.0 |
| Cost per run (USD) | 0.33 | 0.36 | 0.39 | 0.29 | 0.36 | 0.48 |
| Time per run (min) | 2.0 | 2.4 | 3.0 | 1.9 | 2.8 | 3.7 |
| Hit turn limit or timeout | 0/32 | 0/32 | 0/32 | 0/32 | 0/32 | 0/32 |

## By kind (mean judge score)

| Kind | native | original | mine | codex-native | codex-original | codex-mine |
|---|---|---|---|---|---|---|
| interact | 57 | 68 | 66 | 44 | 67 | 47 |
| map | 50 | 56 | 70 | 60 | 72 | 84 |
| crawl | 64 | 68 | 80 | 89 | 89 | 89 |
| agent | 74 | 78 | 84 | 83 | 83 | 84 |

## Every task

Each cell: judge score per trial, then the Firecrawl commands run (all trials).

| id | meant to need | native | original | mine | codex-native | codex-original | codex-mine |
|---|---|---|---|---|---|---|---|
| i1 | interact | 68, 75 | 88, 95 | 70, 55 · statusx2 searchx2 scrapex2 | 68, 90 | 75, 80 · scrapex5 interactx3 searchx2 statusx1 listx1 bashx1 | 70, 70 · interactx32 scrapex8 searchx4 statusx1 |
| i2 | interact | 0, 0 | 0, 0 | 0, 0 · interactx6 scrapex5 statusx2 searchx2 | 0, 0 | 0, 0 · interactx12 scrapex10 searchx5 statusx2 govx2 find-toolsx1 | 0, 0 · interactx14 searchx9 scrapex8 find-toolsx1 search-feedbackx1 statusx1 |
| i3 | interact | 97, 96 | 97, 96 · interactx15 scrapex2 curlx1 helpx1 statusx1 | 96, 97 · interactx21 scrapex7 statusx2 searchx2 | 0, 0 | 97, 97 · interactx36 scrapex4 statusx2 | 97, 97 · interactx33 scrapex4 |
| i4 | interact, crawl, scrape | 94, 95 | 96, 96 · statusx1 scrapex1 | 95, 93 · scrapex6 statusx2 searchx2 agentx2 listx2 find-toolsx1 | 97, 96 | 96, 97 · scrapex9 listx3 searchx2 search-feedbackx1 statusx1 | 15, 35 · scrapex13 interactx8 agentx7 searchx2 listx2 statusx1 |
| i5 | interact, agent, scrape | 8, 40 | 55, 55 · scrapex3 interactx3 helpx1 statusx1 | 78, 72 · scrapex8 interactx7 statusx2 | 50, 40 | 66, 66 · interactx11 searchx10 scrapex6 statusx2 | 50, 38 · agentx37 searchx20 scrapex9 interactx6 search-feedbackx3 statusx2 |
| m1 | map, crawl, scrape | 50, 10 | 62, 55 · scrapex17 interactx17 statusx1 helpx1 | 68, 42 · scrapex24 interactx22 mapx4 statusx2 | 45, 50 | 96, 22 · interactx43 scrapex7 statusx2 searchx2 search-feedbackx2 | 96, 96 · agentx37 interactx30 scrapex22 crawlx4 statusx2 searchx2 readlinkx1 |
| m2 | map, scrape | 78, 88 | 87, 74 · scrapex6 | 85, 88 · scrapex8 searchx4 statusx2 mapx1 | 82, 85 | 92, 90 · searchx19 scrapex5 statusx2 | 95, 90 · scrapex22 searchx18 statusx2 |
| m3 | map, crawl, scrape | 38, 33 | 28, 33 | 78, 62 · scrapex33 searchx14 statusx2 mapx2 developerx1 | 50, 45 | 68, 65 · scrapex155 searchx91 interactx13 mapx5 statusx2 listx1 search-feedbackx1 | 68, 60 · scrapex151 searchx85 mapx3 statusx1 |
| c1 | crawl | 8, 90 | 90, 0 | 88, 92 · scrapex5 statusx2 | 94, 95 | 95, 94 · crawlx6 scrapex6 statusx2 | 95, 95 · crawlx9 scrapex4 statusx2 firecrawlx2 helpx1 |
| c2 | crawl, map | 68, 68 | 82, 76 | 68, 80 · scrapex5 statusx2 mapx2 | 88, 88 | 85, 86 · scrapex12 mapx2 statusx1 developerx1 | 88, 85 · crawlx11 scrapex10 statusx2 |
| c3 | crawl | 80, 72 | 72, 88 | 84, 68 · mapx4 scrapex4 statusx2 | 85, 84 | 88, 85 · scrapex9 statusx1 mapx1 searchx1 | 85, 85 · crawlx6 scrapex5 searchx3 statusx2 search-feedbackx1 mapx1 |
| a1 | agent | 62, 72 | 72, 80 | 80, 80 · scrapex13 searchx11 statusx1 | 92, 94 | 92, 92 · scrapex43 interactx29 searchx26 statusx2 mapx2 | 90, 94 · interactx56 searchx54 scrapex42 statusx2 |
| a2 | agent | 92, 88 | 94, 90 | 96, 96 · scrapex7 searchx5 statusx1 | 93, 92 | 95, 94 · searchx41 scrapex9 statusx2 | 95, 96 · searchx30 scrapex19 statusx1 |
| a3 | agent, map | 78, 82 | 80, 80 | 85, 80 · scrapex37 searchx7 statusx2 | 88, 95 | 75, 88 · searchx44 scrapex19 statusx2 | 94, 93 · searchx77 scrapex44 statusx2 |
| a4 | crawl, agent | 52, 68 | 55, 55 | 68, 80 · scrapex86 searchx12 statusx2 | 50, 40 | 25, 80 · scrapex4 interactx3 statusx2 searchx2 researchx1 | 40, 55 · scrapex59 agentx23 searchx21 researchx7 crawlx5 search-feedbackx4 statusx1 |
| a5 | agent | 73, 72 | 80, 92 | 90, 87 · searchx6 scrapex4 statusx1 | 93, 95 | 96, 96 · searchx27 scrapex26 statusx2 listx2 | 93, 92 · searchx31 scrapex26 statusx2 listx2 |

# Hard multi-site tasks with Codex as the agent

Same 16 tasks, rubric, reference answers and Sonnet 5.5 judge agent as [the Claude Code run](../hardtools/RESULTS.md). Run 2026-10-17/18. Codex CLI 0.163.0 with its default model `gpt-6.1-sol` (default reasoning effort), signed in with a ChatGPT account, 2 trials per task, 2 runs at a time. Runner: [run_codex.py](run_codex.py). Judged with files: [judge_with_files.py](judge_with_files.py).

- **codex-native**: no skills, `firecrawl` shadowed by a stub and the API key removed. Codex's own live `web_search` and the shell (curl etc.) stay available.
- **codex-original**: upstream skills at 22358f2, copied into `$CODEX_HOME/skills`.
- **codex-mine**: PR #6 skills at a3648a8.

The first three columns are the Claude Code (Sonnet 5.5) numbers from the earlier run, for comparison.

## Re-judged with the files Codex wrote (2026-10-18)

Codex often writes long tables to a CSV or Markdown file and links it from a short answer. The first judging pass only saw the chat answer. The runner now keeps each run's files, and `judge_with_files.py` appends them to the answer before the same judge grades it. The first run's files were already deleted, so the 6 tasks whose answers linked files (i1, i4, i5, m1, a4, c1) were run again for 2 trials and judged with files. The other 10 tasks keep their first-pass scores, since their answers didn't depend on files.

**Partial: the ChatGPT plan's weekly Codex limit ran out partway through.** The PR #6 arm reran all 12 runs, and the original-skills arm reran 11 of 12 (a4 trial 2 keeps its first-pass score). **The no-Firecrawl arm couldn't rerun at all.** Its 68 still comes from chat-only judging, so it is understated: its i5, m1 and a4 answers also linked files. The limit resets around 24 Oct 2026, 21:42.

| 6 rerun tasks, mean of 12 runs | first pass (chat only) | rerun (with files) |
|---|---|---|
| Codex, original skills | 74 | 87 |
| Codex, PR #6 skills | 63 | 77 |

## What it shows

- **Firecrawl helps Codex too: 68 with no Firecrawl (chat-only judging), 82 with the original skills and 79 with PR #6's.** Claude Code scored 62, 69 and 75.
- **Codex doesn't have Claude Code's under-triggering problem.** With the original skills, Codex used Firecrawl in 32/32 runs and Claude Code in 6/32. Codex reads the router `SKILL.md` and follows it. The description rewrites in PR #4/#6 fix a Claude Code problem.
- **With files counted, the original skills still beat PR #6 for Codex (82 vs 79).** The i4 gap closed: PR #6 went from 15/35 to 96/92 once the judge could read the CSV. Interact-shaped tasks still favour the original skills (71 vs 60). On i1 (BTS form) and i5 (Chrome Web Store), PR #6 led Codex into `interact` or `agent` loops that returned less than a scrape plus the public data dump. Map-, crawl- and agent-shaped tasks tie (84 / 88 / 89).
- **PR #6 pushes Codex onto `agent` and `crawl`.** It made 54 `agent` and 33 `crawl` calls, against 0 and 6 with the original skills. Claude Code never ran `crawl`.
- **Without Firecrawl, Codex can't drive forms.** i3 (USPS calculator) scored 0 in both native runs, and 97 with `firecrawl interact`.
- **i2 (California SOS) is still unanswerable** for every agent and arm.
- **Cost:** the USD row is not real money. The runs used a ChatGPT plan, and the row prices tokens at a placeholder $1.25 / $0.125 / $10 per 1M (input / cached / output). In the first pass, runs averaged 1.2M input tokens with no Firecrawl, 1.65M with the original skills and 2.45M with PR #6, about 94% of it cached.
- **"Turns" is always 1 for Codex,** because one `codex exec` is one turn. Compare tool calls instead.
- **Noise:** each cell is still 2 trials, and the reruns are fresh runs, not just a re-grade. Differences under ~5 points per kind are noise.

## Overall

| | native | original | mine | codex-native | codex-original | codex-mine |
|---|---|---|---|---|---|---|
| Judge score (mean /100) | 62 | 69 | 75 | 68 | 82 | 79 |
| Runs scoring 70+ | 17/32 | 21/32 | 23/32 | 19/32 | 28/32 | 24/32 |
| Runs scoring under 20 | 5/32 | 3/32 | 2/32 | 4/32 | 2/32 | 2/32 |
| Cites sources | 91% | 91% | 81% | 94% | 100% | 100% |
| Faithful /5 | 3.94 | 3.84 | 4.00 | 4.16 | 4.28 | 4.19 |
| Used Firecrawl | 0/32 | 6/32 | 32/32 | 0/32 | 32/32 | 32/32 |
| Ran an intended command | 0/32 | 6/32 | 16/32 | 0/32 | 18/32 | 23/32 |
| `firecrawl search` calls | 0 | 0 | 67 | 0 | 275 | 335 |
| `firecrawl scrape` calls | 0 | 29 | 254 | 0 | 339 | 364 |
| `firecrawl map` calls | 0 | 0 | 13 | 0 | 10 | 4 |
| `firecrawl crawl` calls | 0 | 0 | 0 | 0 | 6 | 33 |
| `firecrawl agent` calls | 0 | 0 | 2 | 0 | 0 | 54 |
| `firecrawl interact` calls | 0 | 35 | 56 | 0 | 144 | 200 |
| Used WebSearch/WebFetch | 26/32 | 22/32 | 0/32 | 32/32 | 1/32 | 0/32 |
| Tool calls (mean) | 30.8 | 31.6 | 21.2 | 17.9 | 45.2 | 55.4 |
| Turns (mean) | 19.2 | 21.1 | 16.4 | 1.0 | 1.0 | 1.0 |
| Cost per run (USD) | 0.33 | 0.36 | 0.39 | 0.29 | 0.36 | 0.41 |
| Time per run (min) | 2.0 | 2.4 | 3.0 | 1.9 | 3.0 | 3.9 |
| Hit turn limit or timeout | 0/32 | 0/32 | 0/32 | 0/32 | 0/32 | 0/32 |

## By kind (mean judge score)

| Kind | native | original | mine | codex-native | codex-original | codex-mine |
|---|---|---|---|---|---|---|
| interact | 57 | 68 | 66 | 44 | 71 | 60 |
| map | 50 | 56 | 70 | 60 | 84 | 84 |
| crawl | 64 | 68 | 80 | 89 | 88 | 88 |
| agent | 74 | 78 | 84 | 83 | 89 | 89 |

## Every task

Each cell: judge score per trial, then the Firecrawl commands run (all trials).

| id | meant to need | native | original | mine | codex-native | codex-original | codex-mine |
|---|---|---|---|---|---|---|---|
| i1 | interact | 68, 75 | 88, 95 | 70, 55 · statusx2 searchx2 scrapex2 | 68, 90 | 85, 70 · searchx4 scrapex4 statusx2 search-feedbackx1 | 50, 70 · interactx36 scrapex5 searchx4 statusx1 |
| i2 | interact | 0, 0 | 0, 0 | 0, 0 · interactx6 scrapex5 statusx2 searchx2 | 0, 0 | 0, 0 · interactx12 scrapex10 searchx5 statusx2 govx2 find-toolsx1 | 0, 0 · interactx14 searchx9 scrapex8 find-toolsx1 search-feedbackx1 statusx1 |
| i3 | interact | 97, 96 | 97, 96 · interactx15 scrapex2 curlx1 helpx1 statusx1 | 96, 97 · interactx21 scrapex7 statusx2 searchx2 | 0, 0 | 97, 97 · interactx36 scrapex4 statusx2 | 97, 97 · interactx33 scrapex4 |
| i4 | interact, crawl, scrape | 94, 95 | 96, 96 · statusx1 scrapex1 | 95, 93 · scrapex6 statusx2 searchx2 agentx2 listx2 find-toolsx1 | 97, 96 | 96, 97 · scrapex9 listx4 statusx2 searchx2 search-feedbackx2 | 96, 92 · scrapex8 interactx8 searchx1 listx1 statusx1 |
| i5 | interact, agent, scrape | 8, 40 | 55, 55 · scrapex3 interactx3 helpx1 statusx1 | 78, 72 · scrapex8 interactx7 statusx2 | 50, 40 | 88, 76 · searchx12 interactx12 scrapex7 statusx2 | 48, 50 · agentx30 searchx18 interactx8 scrapex3 statusx1 search-feedbackx1 |
| m1 | map, crawl, scrape | 50, 10 | 62, 55 · scrapex17 interactx17 statusx1 helpx1 | 68, 42 · scrapex24 interactx22 mapx4 statusx2 | 45, 50 | 96, 95 · interactx39 scrapex13 statusx2 | 97, 96 · interactx45 agentx23 scrapex10 crawlx8 statusx2 searchx2 helpx2 search-feedbackx1 |
| m2 | map, scrape | 78, 88 | 87, 74 · scrapex6 | 85, 88 · scrapex8 searchx4 statusx2 mapx1 | 82, 85 | 92, 90 · searchx19 scrapex5 statusx2 | 95, 90 · scrapex22 searchx18 statusx2 |
| m3 | map, crawl, scrape | 38, 33 | 28, 33 | 78, 62 · scrapex33 searchx14 statusx2 mapx2 developerx1 | 50, 45 | 68, 65 · scrapex155 searchx91 interactx13 mapx5 statusx2 listx1 search-feedbackx1 | 68, 60 · scrapex151 searchx85 mapx3 statusx1 |
| c1 | crawl | 8, 90 | 90, 0 | 88, 92 · scrapex5 statusx2 | 94, 95 | 90, 95 · scrapex6 crawlx6 statusx2 firecrawlx1 | 93, 95 · crawlx8 scrapex3 statusx2 firecrawlx2 |
| c2 | crawl, map | 68, 68 | 82, 76 | 68, 80 · scrapex5 statusx2 mapx2 | 88, 88 | 85, 86 · scrapex12 mapx2 statusx1 developerx1 | 88, 85 · crawlx11 scrapex10 statusx2 |
| c3 | crawl | 80, 72 | 72, 88 | 84, 68 · mapx4 scrapex4 statusx2 | 85, 84 | 88, 85 · scrapex9 statusx1 mapx1 searchx1 | 85, 85 · crawlx6 scrapex5 searchx3 statusx2 search-feedbackx1 mapx1 |
| a1 | agent | 62, 72 | 72, 80 | 80, 80 · scrapex13 searchx11 statusx1 | 92, 94 | 92, 92 · scrapex43 interactx29 searchx26 statusx2 mapx2 | 90, 94 · interactx56 searchx54 scrapex42 statusx2 |
| a2 | agent | 92, 88 | 94, 90 | 96, 96 · scrapex7 searchx5 statusx1 | 93, 92 | 95, 94 · searchx41 scrapex9 statusx2 | 95, 96 · searchx30 scrapex19 statusx1 |
| a3 | agent, map | 78, 82 | 80, 80 | 85, 80 · scrapex37 searchx7 statusx2 | 88, 95 | 75, 88 · searchx44 scrapex19 statusx2 | 94, 93 · searchx77 scrapex44 statusx2 |
| a4 | crawl, agent | 52, 68 | 55, 55 | 68, 80 · scrapex86 searchx12 statusx2 | 50, 40 | 80, 80 · scrapex8 researchx4 searchx3 interactx3 statusx2 | 62, 80 · scrapex4 searchx3 statusx2 agentx1 researchx1 |
| a5 | agent | 73, 72 | 80, 92 | 90, 87 · searchx6 scrapex4 statusx1 | 93, 95 | 96, 96 · searchx27 scrapex26 statusx2 listx2 | 93, 92 · searchx31 scrapex26 statusx2 listx2 |

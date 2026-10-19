# Hard multi-site tasks: PR #4 skills added, plus tool choice and router use

Same 16 tasks, model (Sonnet 5.5, Claude Code 2.1.302), 2 trials, max 80 turns, judge and references as [RESULTS.md](RESULTS.md). New arm **pr4**: PR #4 head at bd7cac4 (descriptions v3 plus the router-table and freshness changes), run 2026-10-17 at concurrency 2. **mine** is still PR #6 at a3648a8, which predates bd7cac4's router edits.

Tool choice is scored by `toolchoice.py` from the saved runs: a run "picked the intended tool" if it ran any of the task's `intent_cmds` other than scrape/search. Other runs are split by judge score (70+ good, under 70 poor). Runs with no Firecrawl access show n/a.

## What it shows

- **PR #4 scores 74, level with PR #6 (75)** and above original (69) and native (62). It has the most runs at 70+ (25/32). Map tasks are lower (63 vs 70, mostly m3 at 28/60), crawl higher (84 vs 80). Within 2-trial noise.
- **Tool choice is the same for PR #4 and PR #6: 12/32 picked the intended tool**, vs 2/32 for the original skills. `agent` was never chosen (0/10 in every arm) and `crawl` never ran; the 2 crawl hits are `map` on c2.
- **Picking the intended tool didn't predict a better answer.** Without i2 (blocked for everyone), runs that picked it scored 75 vs 80 by another route on PR #4. Scrape loops over a URL list work well.
- **The router skill is nearly always the entry point**: loaded on 31/32 PR #4 runs and 30/32 PR #6 runs. Per-command skills were loaded directly only via `firecrawl-search` (1 and 2 runs). The original skills loaded the router on 2 runs, and ran Firecrawl without any skill on 4 more.
- PR #4 uses `interact` most (83 calls, 45 of them on i3) and cites sources least (72%).

## Overall

| | native | original | mine | pr4 |
|---|---|---|---|---|
| Judge score (mean /100) | 62 | 69 | 75 | 74 |
| Runs scoring 70+ | 17/32 | 21/32 | 23/32 | 25/32 |
| Runs scoring under 20 | 5/32 | 3/32 | 2/32 | 3/32 |
| Cites sources | 91% | 91% | 81% | 72% |
| Faithful /5 | 3.94 | 3.84 | 4.00 | 4.09 |
| Used Firecrawl | 0/32 | 6/32 | 32/32 | 32/32 |
| Ran an intended command | 0/32 | 6/32 | 16/32 | 16/32 |
| `firecrawl search` calls | 0 | 0 | 67 | 48 |
| `firecrawl scrape` calls | 0 | 29 | 254 | 250 |
| `firecrawl map` calls | 0 | 0 | 13 | 14 |
| `firecrawl crawl` calls | 0 | 0 | 0 | 0 |
| `firecrawl agent` calls | 0 | 0 | 2 | 0 |
| `firecrawl interact` calls | 0 | 35 | 56 | 83 |
| Used WebSearch/WebFetch | 26/32 | 22/32 | 0/32 | 0/32 |
| Tool calls (mean) | 30.8 | 31.6 | 21.2 | 21.6 |
| Turns (mean) | 19.2 | 21.1 | 16.4 | 16.1 |
| Cost per run (USD) | 0.33 | 0.36 | 0.39 | 0.40 |
| Time per run (min) | 2.0 | 2.4 | 3.0 | 3.1 |
| Hit turn limit or timeout | 0/32 | 0/32 | 0/32 | 0/32 |

## By kind (mean judge score)

| Kind | native | original | mine | pr4 |
|---|---|---|---|---|
| interact | 57 | 68 | 66 | 67 |
| map | 50 | 56 | 70 | 63 |
| crawl | 64 | 68 | 80 | 84 |
| agent | 74 | 78 | 84 | 80 |

## Every task

Each cell: judge score per trial, then the Firecrawl commands run (all trials).

| id | meant to need | native | original | mine | pr4 |
|---|---|---|---|---|---|
| i1 | interact | 68, 75 | 88, 95 | 70, 55 · statusx2 searchx2 scrapex2 | 70, 80 · statusx2 searchx2 |
| i2 | interact | 0, 0 | 0, 0 | 0, 0 · interactx6 scrapex5 statusx2 searchx2 | 0, 0 · scrapex8 interactx5 statusx2 searchx2 |
| i3 | interact | 97, 96 | 97, 96 · interactx15 scrapex2 curlx1 helpx1 statusx1 | 96, 97 · interactx21 scrapex7 statusx2 searchx2 | 97, 96 · interactx45 scrapex5 statusx2 helpx1 searchx1 |
| i4 | interact, crawl, scrape | 94, 95 | 96, 96 · statusx1 scrapex1 | 95, 93 · scrapex6 statusx2 searchx2 agentx2 listx2 find-toolsx1 | 96, 94 · scrapex3 statusx2 |
| i5 | interact, agent, scrape | 8, 40 | 55, 55 · scrapex3 interactx3 helpx1 statusx1 | 78, 72 · scrapex8 interactx7 statusx2 | 78, 62 · scrapex9 interactx9 statusx2 |
| m1 | map, crawl, scrape | 50, 10 | 62, 55 · scrapex17 interactx17 statusx1 helpx1 | 68, 42 · scrapex24 interactx22 mapx4 statusx2 | 94, 15 · interactx24 scrapex20 mapx3 statusx2 |
| m2 | map, scrape | 78, 88 | 87, 74 · scrapex6 | 85, 88 · scrapex8 searchx4 statusx2 mapx1 | 90, 90 · scrapex7 searchx3 statusx2 mapx1 |
| m3 | map, crawl, scrape | 38, 33 | 28, 33 | 78, 62 · scrapex33 searchx14 statusx2 mapx2 developerx1 | 28, 60 · scrapex23 searchx8 mapx5 statusx1 |
| c1 | crawl | 8, 90 | 90, 0 | 88, 92 · scrapex5 statusx2 | 90, 85 · scrapex8 statusx2 |
| c2 | crawl, map | 68, 68 | 82, 76 | 68, 80 · scrapex5 statusx2 mapx2 | 82, 80 · scrapex7 statusx2 mapx2 |
| c3 | crawl | 80, 72 | 72, 88 | 84, 68 · mapx4 scrapex4 statusx2 | 88, 80 · scrapex8 mapx3 statusx2 |
| a1 | agent | 62, 72 | 72, 80 | 80, 80 · scrapex13 searchx11 statusx1 | 82, 85 · searchx5 scrapex4 statusx2 |
| a2 | agent | 92, 88 | 94, 90 | 96, 96 · scrapex7 searchx5 statusx1 | 92, 96 · scrapex19 searchx4 statusx2 |
| a3 | agent, map | 78, 82 | 80, 80 | 85, 80 · scrapex37 searchx7 statusx2 | 82, 80 · scrapex38 searchx5 statusx2 |
| a4 | crawl, agent | 52, 68 | 55, 55 | 68, 80 · scrapex86 searchx12 statusx2 | 60, 72 · scrapex89 searchx13 statusx2 helpx1 |
| a5 | agent | 73, 72 | 80, 92 | 90, 87 · searchx6 scrapex4 statusx1 | 76, 78 · searchx5 scrapex2 statusx1 |

## Tool choice

| | native | original | mine | pr4 |
|---|---|---|---|---|
| Picked the intended tool | n/a | 2/32 | 12/32 | 12/32 |
| Other route, good answer (70+) | n/a | 20/32 | 16/32 | 18/32 |
| Other route, poor answer (<70) | n/a | 10/32 | 4/32 | 2/32 |
| Mean score when intended tool picked | n/a | 76 | 64 | 63 |
| Mean score by another route | n/a | 68 | 82 | 80 |

## Picked the intended tool, by kind

| Kind | native | original | mine | pr4 |
|---|---|---|---|---|
| interact | n/a | 2/10 | 6/10 | 6/10 |
| map | n/a | 0/6 | 4/6 | 4/6 |
| crawl | n/a | 0/6 | 2/6 | 2/6 |
| agent | n/a | 0/10 | 0/10 | 0/10 |

## Which skill was loaded

| | native | original | mine | pr4 |
|---|---|---|---|---|
| Loaded the `firecrawl` router skill | n/a | 2/32 | 30/32 | 31/32 |
| Loaded only a per-command skill | n/a | 0/32 | 2/32 | 1/32 |
| Loaded no skill | n/a | 30/32 | 0/32 | 0/32 |
| Loaded `firecrawl-search` | n/a | 0/32 | 2/32 | 1/32 |

## Every task

I = intended tool, G = other route with a good answer, P = other route with a poor answer, one letter per trial.
After the slash, the skill loaded per trial: R = `firecrawl` router, C = a per-command skill only, - = none.

| id | intended | native | original | mine | pr4 |
|---|---|---|---|---|---|
| i1 | interact | n/a | G G / - - | G P / R R | G G / R R |
| i2 | interact | n/a | P P / - - | I I / R R | I I / R R |
| i3 | interact | n/a | G I / - - | I I / R R | I I / R R |
| i4 | interact, crawl | n/a | G G / - R | G G / R R | G G / R R |
| i5 | interact, agent | n/a | P I / - - | I I / R R | I I / R R |
| m1 | map, crawl | n/a | P P / R - | I I / R R | I I / R R |
| m2 | map | n/a | G G / - - | G I / R R | I G / R R |
| m3 | map, crawl | n/a | P P / - - | I P / R R | P I / C R |
| c1 | crawl | n/a | G P / - - | G G / R R | G G / R R |
| c2 | crawl, map | n/a | G G / - - | I I / R R | I I / R R |
| c3 | crawl | n/a | G G / - - | G P / R R | G G / R R |
| a1 | agent | n/a | G G / - - | G G / C R | G G / R R |
| a2 | agent | n/a | G G / - - | G G / R C | G G / R R |
| a3 | agent, map | n/a | G G / - - | G G / R R | G G / R R |
| a4 | crawl, agent | n/a | P P / - - | P G / R R | P G / R R |
| a5 | agent | n/a | G G / - - | G G / R R | G G / R R |

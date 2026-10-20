## Overall

| | main-1019 | boost |
|---|---|---|
| Judge score (mean /100) | 75 | 83 |
| Runs scoring 70+ | 21/30 | 26/30 |
| Runs scoring under 20 | 2/30 | 0/30 |
| Cites sources | 70% | 77% |
| Faithful /5 | 4.03 | 4.00 |
| Used Firecrawl | 30/30 | 30/30 |
| Ran an intended command | 15/30 | 13/30 |
| `firecrawl search` calls | 79 | 79 |
| `firecrawl scrape` calls | 286 | 253 |
| `firecrawl map` calls | 11 | 14 |
| `firecrawl crawl` calls | 0 | 0 |
| `firecrawl agent` calls | 3 | 0 |
| `firecrawl interact` calls | 66 | 38 |
| Used WebSearch/WebFetch | 0/30 | 0/30 |
| Tool calls (mean) | 23.7 | 22.1 |
| Turns (mean) | 15.8 | 16.4 |
| Cost per run (USD) | 0.41 | 0.40 |
| Time per run (min) | 4.2 | 2.8 |
| Hit turn limit or timeout | 0/30 | 0/30 |

## By kind (mean judge score)

| Kind | main-1019 | boost |
|---|---|---|
| interact | 74 | 89 |
| map | 67 | 75 |
| crawl | 84 | 82 |
| agent | 75 | 83 |

## Every task

Each cell: judge score per trial, then the Firecrawl commands run (all trials).

| id | meant to need | main-1019 | boost |
|---|---|---|---|
| i1 | interact | 97, 70 · searchx3 statusx2 scrapex2 | 95, 90 · statusx2 searchx2 scrapex2 |
| i2 | interact |  |  |
| i3 | interact | 8, 100 · interactx32 scrapex4 statusx2 searchx2 | 96, 97 · interactx10 scrapex4 statusx2 searchx2 |
| i4 | interact, crawl, scrape | 97, 96 · scrapex5 statusx2 searchx2 listx2 | 96, 95 · searchx3 scrapex3 statusx2 listx2 find-toolsx1 |
| i5 | interact, agent, scrape | 58, 62 · scrapex10 interactx8 statusx2 | 76, 68 · scrapex7 interactx6 statusx2 |
| m1 | map, crawl, scrape | 58, 68 · scrapex22 interactx22 mapx5 agentx3 statusx2 | 95, 50 · interactx22 scrapex20 mapx4 statusx2 |
| m2 | map, scrape | 88, 85 · scrapex8 searchx4 statusx2 | 85, 90 · scrapex14 searchx9 statusx2 mapx1 |
| m3 | map, crawl, scrape | 50, 55 · scrapex40 searchx15 mapx1 | 88, 42 · scrapex23 searchx13 statusx2 mapx2 |
| c1 | crawl | 88, 80 · scrapex6 statusx1 (bare)x1 credit-usagex1 batch-scrapex1 | 88, 85 · scrapex7 mapx2 (bare)x1 |
| c2 | crawl, map | 85, 80 · scrapex3 statusx2 mapx2 | 80, 80 · scrapex3 statusx2 mapx2 |
| c3 | crawl | 85, 88 · scrapex5 statusx2 mapx1 | 78, 80 · statusx2 mapx2 scrapex2 |
| a1 | agent | 82, 84 · scrapex26 searchx13 interactx4 statusx2 | 76, 68 · scrapex14 searchx7 statusx2 |
| a2 | agent | 93, 94 · scrapex16 searchx9 statusx2 | 95, 94 · scrapex18 searchx6 statusx2 |
| a3 | agent, map | 88, 80 · scrapex22 searchx3 statusx1 mapx1 | 80, 80 · scrapex26 searchx5 statusx1 |
| a4 | crawl, agent | 78, 62 · scrapex107 searchx22 statusx3 mapx1 | 78, 75 · scrapex102 searchx25 statusx6 mapx1 |
| a5 | agent | 85, 0 · scrapex10 searchx6 statusx1 | 92, 90 · scrapex8 searchx7 statusx1 |
## Tool choice

| | main-1019 | boost |
|---|---|---|
| Picked the intended tool | 10/30 | 9/30 |
| Other route, good answer (70+) | 17/30 | 19/30 |
| Other route, poor answer (<70) | 3/30 | 2/30 |
| Mean score when intended tool picked | 65 | 80 |
| Mean score by another route | 80 | 84 |

## Picked the intended tool, by kind

| Kind | main-1019 | boost |
|---|---|---|
| interact | 4/8 | 3/8 |
| map | 3/6 | 4/6 |
| crawl | 2/6 | 2/6 |
| agent | 1/10 | 0/10 |

## Which skill was loaded

| | main-1019 | boost |
|---|---|---|
| Loaded the `firecrawl` router skill | 26/30 | 27/30 |
| Loaded only a per-command skill | 4/30 | 3/30 |
| Loaded no skill | 0/30 | 0/30 |
| Loaded `firecrawl-agent` | 0/30 | 1/30 |
| Loaded `firecrawl-crawl` | 1/30 | 0/30 |
| Loaded `firecrawl-download` | 0/30 | 1/30 |
| Loaded `firecrawl-scrape` | 0/30 | 1/30 |
| Loaded `firecrawl-search` | 3/30 | 1/30 |

## Every task

I = intended tool, G = other route with a good answer, P = other route with a poor answer, one letter per trial.
After the slash, the skill loaded per trial: R = `firecrawl` router, C = a per-command skill only, - = none.

| id | intended | main-1019 | boost |
|---|---|---|---|
| i1 | interact | G G / R R | G G / R R |
| i2 | interact |  /  |  /  |
| i3 | interact | I I / R R | G I / R R |
| i4 | interact, crawl | G G / R R | G G / R R |
| i5 | interact, agent | I I / R R | I I / R R |
| m1 | map, crawl | I I / R R | I I / R R |
| m2 | map | G G / R R | G I / R R |
| m3 | map, crawl | P I / C C | I P / R R |
| c1 | crawl | G G / R C | G G / C C |
| c2 | crawl, map | I I / R R | I I / R R |
| c3 | crawl | G G / R R | G G / R R |
| a1 | agent | G G / R R | G P / R R |
| a2 | agent | G G / R R | G G / R R |
| a3 | agent, map | G I / C R | G G / R C |
| a4 | crawl, agent | G P / R R | G G / R+C R |
| a5 | agent | G P / R R | G G / R R |

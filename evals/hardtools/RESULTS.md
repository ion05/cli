# Hard multi-site tasks: no Firecrawl vs original skills vs PR #6 skills

16 research tasks built to need crawl, map, agent or interact (prompts and rationale: [PROMPTS.md](PROMPTS.md)). Run 2026-10-17. Sonnet 5.5, Claude Code 2.1.302, 2 trials per task, max 80 turns, 40 min per run.

- **native**: no Firecrawl skills, Firecrawl CLI blocked, API key removed. Built-in WebSearch/WebFetch, curl and the rest of Claude Code stay available.
- **original**: upstream skills at 22358f2.
- **mine**: PR #6 skills at a3648a8 (stacked on PR #4).

**Grading.** Opus 5.5 built one reference answer per task with every tool and up to 250 turns. A Sonnet 5.5 judge agent then scored each answer 0-100 against the task's rubric and that reference, giving partial credit per field. The judge had WebSearch, WebFetch and Bash, and checked the live source on up to 6 disagreements. The references were skimmed, not hand-checked field by field.

## What it shows

- **Your skills score highest: 75 vs 69 (original) vs 62 (native).** They also have the most runs at 70+ (23/32 vs 21 vs 17). The biggest gains are on map- and crawl-shaped tasks (map 70 vs 56 vs 50, crawl 80 vs 68 vs 64). The clearest single win is m3, the first MCP mention in 5 editor changelogs: 70 vs 31 vs 36.
- **`crawl` was never run in any arm, and `agent` only twice.** On crawl-shaped tasks the agent got a URL list (from an index page or `map`), then looped `firecrawl scrape` in one shell command. For example, c1 scraped the ~340 Slack method pages with one loop, and a4 scraped dozens of Purdue profiles. Because each loop counts as one call, the scrape counts in this report undercount pages. The answers were good (c1 88/92), so this is about tool choice, not quality.
- **`interact` does get used now, even with the original skills** (35 calls vs 56 for yours), on forms that a scrape can't fill: the USPS calculator, the Databricks story grid, Chrome Web Store "Load more". When WebFetch failed on those pages, the original skills' agent fell back to Firecrawl.
- **Agents route around the browser when a data dump exists.** On i1 every arm used BTS's CSV download instead of the form, and the native arm did best there. On i4 every arm found the yc-oss dataset of YC companies.
- **i2 (California SOS) is unanswerable.** Imperva bot protection blocked every arm and the reference. All runs scored 0, so the task measures nothing. Drop it or swap in another state.
- **Cost:** your skills cost slightly more ($0.39 vs $0.36 vs $0.33 per run) and are slower (3.0 vs 2.4 vs 2.0 min), but use fewer tool calls (21 vs 32 vs 31). They cite a source less often (81% vs 91%).
- **Noise is high with 2 trials.** For example, c1 scored 8 and 90 in the native arm. Read differences under ~5 points per kind as noise.

## Overall

| | native | original | mine |
|---|---|---|---|
| Judge score (mean /100) | 62 | 69 | 75 |
| Runs scoring 70+ | 17/32 | 21/32 | 23/32 |
| Runs scoring under 20 | 5/32 | 3/32 | 2/32 |
| Cites sources | 91% | 91% | 81% |
| Faithful /5 | 3.94 | 3.84 | 4.00 |
| Used Firecrawl | 0/32 | 6/32 | 32/32 |
| Ran an intended command | 0/32 | 6/32 | 16/32 |
| `firecrawl search` calls | 0 | 0 | 67 |
| `firecrawl scrape` calls | 0 | 29 | 254 |
| `firecrawl map` calls | 0 | 0 | 13 |
| `firecrawl crawl` calls | 0 | 0 | 0 |
| `firecrawl agent` calls | 0 | 0 | 2 |
| `firecrawl interact` calls | 0 | 35 | 56 |
| Used WebSearch/WebFetch | 26/32 | 22/32 | 0/32 |
| Tool calls (mean) | 30.8 | 31.6 | 21.2 |
| Turns (mean) | 19.2 | 21.1 | 16.4 |
| Cost per run (USD) | 0.33 | 0.36 | 0.39 |
| Time per run (min) | 2.0 | 2.4 | 3.0 |
| Hit turn limit or timeout | 0/32 | 0/32 | 0/32 |

## By kind (mean judge score)

| Kind | native | original | mine |
|---|---|---|---|
| interact | 57 | 68 | 66 |
| map | 50 | 56 | 70 |
| crawl | 64 | 68 | 80 |
| agent | 74 | 78 | 84 |

## Every task

Each cell: judge score per trial, then the Firecrawl commands run (all trials).

| id | meant to need | native | original | mine |
|---|---|---|---|---|
| i1 | interact | 68, 75 | 88, 95 | 70, 55 · statusx2 searchx2 scrapex2 |
| i2 | interact | 0, 0 | 0, 0 | 0, 0 · interactx6 scrapex5 statusx2 searchx2 |
| i3 | interact | 97, 96 | 97, 96 · interactx15 scrapex2 curlx1 helpx1 statusx1 | 96, 97 · interactx21 scrapex7 statusx2 searchx2 |
| i4 | interact, crawl, scrape | 94, 95 | 96, 96 · statusx1 scrapex1 | 95, 93 · scrapex6 statusx2 searchx2 agentx2 listx2 find-toolsx1 |
| i5 | interact, agent, scrape | 8, 40 | 55, 55 · scrapex3 interactx3 helpx1 statusx1 | 78, 72 · scrapex8 interactx7 statusx2 |
| m1 | map, crawl, scrape | 50, 10 | 62, 55 · scrapex17 interactx17 statusx1 helpx1 | 68, 42 · scrapex24 interactx22 mapx4 statusx2 |
| m2 | map, scrape | 78, 88 | 87, 74 · scrapex6 | 85, 88 · scrapex8 searchx4 statusx2 mapx1 |
| m3 | map, crawl, scrape | 38, 33 | 28, 33 | 78, 62 · scrapex33 searchx14 statusx2 mapx2 developerx1 |
| c1 | crawl | 8, 90 | 90, 0 | 88, 92 · scrapex5 statusx2 |
| c2 | crawl, map | 68, 68 | 82, 76 | 68, 80 · scrapex5 statusx2 mapx2 |
| c3 | crawl | 80, 72 | 72, 88 | 84, 68 · mapx4 scrapex4 statusx2 |
| a1 | agent | 62, 72 | 72, 80 | 80, 80 · scrapex13 searchx11 statusx1 |
| a2 | agent | 92, 88 | 94, 90 | 96, 96 · scrapex7 searchx5 statusx1 |
| a3 | agent, map | 78, 82 | 80, 80 | 85, 80 · scrapex37 searchx7 statusx2 |
| a4 | crawl, agent | 52, 68 | 55, 55 | 68, 80 · scrapex86 searchx12 statusx2 |
| a5 | agent | 73, 72 | 80, 92 | 90, 87 · searchx6 scrapex4 statusx1 |

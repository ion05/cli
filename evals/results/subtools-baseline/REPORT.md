# subtools eval: baseline

Skills `22358f2` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 74% (53/72) |
| Runs that used Firecrawl | 100% (72/72) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/72) |
| Mean tool calls | 4.9 |
| Mean model cost (USD) | 0.074 |
| Mean duration (s) | 44 |

## Per subtool

Each prompt names Firecrawl but not the command, so this isolates *which* subtool the agent picks.

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run |
|---|---|---|---|---|
| search | 4/6 | 4/6 | 6/6 | `scrape` x10, `search` x4, `search-feedback` x1 |
| scrape | 6/6 | 6/6 | 6/6 | `scrape` x20 |
| map | 6/6 | 6/6 | 6/6 | `map` x6 |
| crawl | 4/6 | 2/6 | 6/6 | `scrape` x7, `crawl` x6, `status` x4, `map` x2 |
| agent | 0/6 | 0/6 | 6/6 | `scrape` x32, `status` x3 |
| interact | 6/6 | 6/6 | 6/6 | `interact` x29, `scrape` x20 |
| monitor | 1/6 | 6/6 | 6/6 | `monitor` x1 |
| download | 6/6 | 6/6 | 6/6 | `download` x14, `scrape` x1 |
| parse | 6/6 | 6/6 | 6/6 | `parse` x17 |
| research | 6/6 | 6/6 | 6/6 | `research` x6 |
| developer | 2/6 | 4/6 | 6/6 | `scrape` x10, `developer` x5 |
| alexandria | 6/6 | 5/6 | 6/6 | `find-tools` x15, `list` x10, `alexandria` x7, `search` x3, `scrape` x3 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| s01 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl firecrawl-search | 1/3 |
| s02 |  search | firecrawl, firecrawl, firecrawl | `search-feedback` `search` firecrawl-search | 3/3 |
| s03 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |
| s04 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |
| s05 |  map | firecrawl, firecrawl, firecrawl | `map` firecrawl-map | 3/3 |
| s06 |  map | firecrawl, firecrawl, firecrawl | `map` firecrawl-map | 3/3 |
| s07 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` `status` firecrawl firecrawl-crawl | 3/3 |
| s08 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` `map` `scrape` `status` firecrawl firecrawl-crawl | 1/3 |
| s09 |  agent | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 0/3 |
| s10 |  agent | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl | 0/3 |
| s11 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 3/3 |
| s12 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 3/3 |
| s13 |  monitor | firecrawl, firecrawl, firecrawl | firecrawl-monitor | 0/3 |
| s14 |  monitor | firecrawl, firecrawl, firecrawl | `monitor` firecrawl-monitor | 1/3 |
| s15 |  download | firecrawl, firecrawl, firecrawl | `download` firecrawl-download | 3/3 |
| s16 |  download | firecrawl, firecrawl, firecrawl | `download` `scrape` firecrawl-download | 3/3 |
| s17 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |
| s18 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |
| s19 |  research | firecrawl, firecrawl, firecrawl | `research` firecrawl-research-index | 3/3 |
| s20 |  research | firecrawl, firecrawl, firecrawl | `research` firecrawl-research-index | 3/3 |
| s21 |  developer | firecrawl, firecrawl, firecrawl | `developer` `scrape` firecrawl firecrawl-developer-index | 2/3 |
| s22 |  developer | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-developer-index | 0/3 |
| s23 |  alexandria | firecrawl, firecrawl, firecrawl | `alexandria` `find-tools` `list` `search` firecrawl-alexandria firecrawl-search | 3/3 |
| s24 |  alexandria | firecrawl, firecrawl, firecrawl | `alexandria` `find-tools` `list` `scrape` firecrawl-alexandria firecrawl-search | 3/3 |

## Tool calls

Across 72 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 260 | 67 | 3.61 |
| `Skill` | 77 | 72 | 1.07 |
| `Read` | 11 | 10 | 0.15 |
| `Monitor` | 3 | 2 | 0.04 |
| `TaskStop` | 1 | 1 | 0.01 |
| `ToolSearch` | 1 | 1 | 0.01 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 12 | 12 | 0.17 |
| `firecrawl-search` | 10 | 10 | 0.14 |
| `firecrawl-scrape` | 8 | 8 | 0.11 |
| `firecrawl-download` | 6 | 6 | 0.08 |
| `firecrawl-interact` | 6 | 6 | 0.08 |
| `firecrawl-map` | 6 | 6 | 0.08 |
| `firecrawl-monitor` | 6 | 6 | 0.08 |
| `firecrawl-parse` | 6 | 6 | 0.08 |
| `firecrawl-research-index` | 6 | 6 | 0.08 |
| `firecrawl-alexandria` | 5 | 5 | 0.07 |
| `firecrawl-developer-index` | 4 | 4 | 0.06 |
| `firecrawl-crawl` | 2 | 2 | 0.03 |
| `firecrawl-agent` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 103 | 30 | 1.43 |
| `firecrawl interact` | 29 | 6 | 0.40 |
| `firecrawl parse` | 17 | 6 | 0.24 |
| `firecrawl find-tools` | 15 | 6 | 0.21 |
| `firecrawl download` | 14 | 6 | 0.19 |
| `firecrawl list` | 10 | 5 | 0.14 |
| `firecrawl map` | 8 | 8 | 0.11 |
| `firecrawl alexandria` | 7 | 6 | 0.10 |
| `firecrawl search` | 7 | 7 | 0.10 |
| `firecrawl status` | 7 | 7 | 0.10 |
| `firecrawl crawl` | 6 | 4 | 0.08 |
| `firecrawl research` | 6 | 6 | 0.08 |
| `firecrawl developer` | 5 | 2 | 0.07 |
| `firecrawl monitor` | 1 | 1 | 0.01 |
| `firecrawl search-feedback` | 1 | 1 | 0.01 |
| `firecrawl agent` | 0 | 0 | 0.00 |


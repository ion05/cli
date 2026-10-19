# subtools-plain eval: desc-v2

Skills `1b5be38` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 79% (57/72) |
| Runs that used Firecrawl | 86% (62/72) |
| Runs that used built-in WebSearch/WebFetch | 3% (2/72) |
| Mean tool calls | 2.9 |
| Mean model cost (USD) | 0.064 |
| Mean duration (s) | 15 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| search | 6/6 | 6/6 | 6/6 | `search` x6, `scrape` x4 | `curl` x3 |
| scrape | 6/6 | 6/6 | 6/6 | `scrape` x9 | - |
| map | 4/6 | 4/6 | 4/6 | `map` x4 | `WebFetch` x2 |
| crawl | 6/6 | 6/6 | 6/6 | `crawl` x6 | - |
| agent | 1/6 | 1/6 | 6/6 | `search` x6, `scrape` x5, `status` x2, `agent` x1 | `curl` x4 |
| interact | 3/6 | 3/6 | 3/6 | `interact` x6, `scrape` x3 | `curl` x3 |
| monitor | 6/6 | 6/6 | 6/6 | - | - |
| download | 6/6 | 6/6 | 6/6 | `download` x7, `scrape` x4, `map` x2 | - |
| parse | 4/6 | 4/6 | 4/6 | `parse` x4 | - |
| research | 6/6 | 6/6 | 6/6 | `research` x6 | - |
| developer | 6/6 | 6/6 | 6/6 | `developer (API)` x6 | `curl` x7 |
| alexandria | 3/6 | 3/6 | 3/6 | `list` x12, `find-tools` x3, `scrape` x3, `alexandria` x3 | `curl` x3 |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| s01 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 3/3 |  |
| s02 |  search | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |  |
| s03 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| s04 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| s05 |  map | firecrawl, firecrawl, firecrawl | `map` firecrawl-map | 3/3 |  |
| s06 |  map | native, native, firecrawl | `map` firecrawl-map | 1/3 |  |
| s07 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` firecrawl-crawl | 3/3 |  |
| s08 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` firecrawl-crawl | 3/3 |  |
| s09 |  agent | firecrawl, firecrawl, firecrawl | `agent` `search` firecrawl-agent firecrawl-search | 1/3 | Replaces the told-suite pricing prompt, which named one known page (scrape is right there). Needs navigating a JS job board. |
| s10 |  agent | firecrawl, firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/3 |  |
| s11 |  interact | other-shell, other-shell, other-shell | - | 0/3 |  |
| s12 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 3/3 |  |
| s13 |  monitor | firecrawl, firecrawl, firecrawl | firecrawl-monitor | 3/3 |  |
| s14 |  monitor | firecrawl, firecrawl, firecrawl | firecrawl-monitor | 3/3 |  |
| s15 |  download | firecrawl, firecrawl, firecrawl | `download` firecrawl-download | 3/3 |  |
| s16 |  download | firecrawl, firecrawl, firecrawl | `download` `map` `scrape` firecrawl-download | 3/3 |  |
| s17 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| s18 |  parse | none, none, firecrawl | `parse` firecrawl-parse | 1/3 |  |
| s19 |  research | firecrawl, firecrawl, firecrawl | `research` firecrawl-research-index | 3/3 |  |
| s20 |  research | firecrawl, firecrawl, firecrawl | `research` firecrawl-research-index | 3/3 |  |
| s21 |  developer | firecrawl, firecrawl, firecrawl | firecrawl-developer-index | 3/3 |  |
| s22 |  developer | firecrawl, firecrawl, firecrawl | firecrawl-developer-index | 3/3 |  |
| s23 |  alexandria | other-shell, other-shell, other-shell | - | 0/3 |  |
| s24 |  alexandria | firecrawl, firecrawl, firecrawl | `alexandria` `find-tools` `list` `scrape` firecrawl-alexandria firecrawl-search | 3/3 |  |

## Tool calls

Across 72 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 136 | 64 | 1.89 |
| `Skill` | 65 | 62 | 0.90 |
| `ToolSearch` | 2 | 2 | 0.03 |
| `WebFetch` | 2 | 2 | 0.03 |
| `Read` | 1 | 1 | 0.01 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-search` | 11 | 11 | 0.15 |
| `firecrawl-crawl` | 6 | 6 | 0.08 |
| `firecrawl-developer-index` | 6 | 6 | 0.08 |
| `firecrawl-download` | 6 | 6 | 0.08 |
| `firecrawl-monitor` | 6 | 6 | 0.08 |
| `firecrawl-research-index` | 6 | 6 | 0.08 |
| `firecrawl-scrape` | 6 | 6 | 0.08 |
| `firecrawl-map` | 4 | 4 | 0.06 |
| `firecrawl-parse` | 4 | 4 | 0.06 |
| `firecrawl` | 3 | 3 | 0.04 |
| `firecrawl-alexandria` | 3 | 3 | 0.04 |
| `firecrawl-interact` | 3 | 3 | 0.04 |
| `firecrawl-agent` | 1 | 1 | 0.01 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 28 | 21 | 0.39 |
| `firecrawl list` | 12 | 3 | 0.17 |
| `firecrawl search` | 12 | 11 | 0.17 |
| `firecrawl download` | 7 | 6 | 0.10 |
| `firecrawl crawl` | 6 | 6 | 0.08 |
| `firecrawl interact` | 6 | 3 | 0.08 |
| `firecrawl map` | 6 | 6 | 0.08 |
| `firecrawl research` | 6 | 6 | 0.08 |
| `firecrawl parse` | 4 | 4 | 0.06 |
| `firecrawl alexandria` | 3 | 3 | 0.04 |
| `firecrawl find-tools` | 3 | 3 | 0.04 |
| `firecrawl status` | 2 | 2 | 0.03 |
| `firecrawl agent` | 1 | 1 | 0.01 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |

**Firecrawl API endpoints called directly (curl)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `developer` | 6 | 6 | 0.08 |


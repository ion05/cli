# heldout eval: cc-final-1021

Skills `660ddb7` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.306 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 44% (47/108) |
| Runs that used Firecrawl | 59% (64/108) |
| Runs that used built-in WebSearch/WebFetch | 21% (23/108) |
| Mean tool calls | 3.4 |
| Mean model cost (USD) | 0.069 |
| Mean duration (s) | 23 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| crawl | 6/12 | 6/12 | 12/12 | `scrape` x14, `map` x8, `crawl` x7, `version` x2, `status` x1 | - |
| agent | 0/15 | 0/15 | 7/15 | `scrape` x27, `search` x10, `status` x2, `list` x1 | `WebSearch` x48, `WebFetch` x3 |
| map | 4/12 | 3/12 | 5/12 | `map` x4, `search` x1, `scrape` x1 | `curl` x3, `WebFetch` x3, `WebSearch` x2 |
| parse | 0/9 | 0/9 | 0/9 | - | `WebFetch` x3 |
| alexandria | 1/6 | 0/6 | 4/6 | `scrape` x5 | `curl` x10 |
| scrape | 14/21 | 14/21 | 14/21 | `scrape` x18 | `WebFetch` x6 |
| search | 8/12 | 7/12 | 8/12 | `search` x7, `scrape` x1 | `WebSearch` x5, `curl` x4 |
| interact | 6/9 | 6/9 | 6/9 | `interact` x13, `scrape` x6 | - |
| download | 3/3 | 3/3 | 3/3 | `download` x3 | - |
| research | 1/3 | 1/3 | 1/3 | `research` x2 | - |
| developer | 4/6 | 4/6 | 4/6 | `scrape` x7, `developer` x2, `gh` x1, `developer (API)` x1 | `curl` x8, `WebFetch` x2 |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| h01 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` firecrawl-crawl | 3/3 |  |
| h02 |  crawl | firecrawl, firecrawl, firecrawl | `map` `scrape` firecrawl-map firecrawl-scrape | 1/3 |  |
| h03 |  agent | firecrawl, firecrawl, firecrawl | `list` `scrape` `search` `status` firecrawl firecrawl-scrape | 0/3 |  |
| h04 |  agent | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 0/3 |  |
| h05 |  map | native, native, native | - | 0/3 |  |
| h06 |  map | firecrawl, firecrawl, firecrawl | `map` `search` firecrawl-map firecrawl-search | 3/3 |  |
| h07 |  parse | none, none, none | - | 0/3 |  |
| h08 |  alexandria | other-shell, other-shell, firecrawl | `scrape` firecrawl-scrape | 1/3 |  |
| h09 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| h10 |  scrape | firecrawl, native, native | `scrape` firecrawl-scrape | 1/3 |  |
| h11 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-scrape firecrawl-search | 3/3 |  |
| h12 |  scrape | native, native, firecrawl | `scrape` firecrawl-scrape | 1/3 |  |
| h13 |  search | firecrawl, native, firecrawl | `search` firecrawl-search | 2/3 |  |
| h14 |  search | firecrawl, native, firecrawl | `search` firecrawl-search | 2/3 |  |
| h15 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| h16 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| h17 |  map | native, none, other-shell | - | 0/3 |  |
| h18 |  map | firecrawl, native, firecrawl | `map` `scrape` firecrawl-map firecrawl-scrape | 1/3 |  |
| h19 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` `map` `scrape` `status` firecrawl firecrawl-scrape | 2/3 |  |
| h20 |  crawl | firecrawl, firecrawl, firecrawl | `map` `scrape` `version` firecrawl-crawl | 0/3 |  |
| h21 |  agent | native, native, native | - | 0/3 |  |
| h22 |  agent | none, none, none | - | 0/3 |  |
| h23 |  agent | native, firecrawl, native | `scrape` `search` firecrawl-search | 0/3 |  |
| h24 |  interact | none, none, none | - | 0/3 |  |
| h25 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 3/3 |  |
| h26 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 3/3 |  |
| h27 |  parse | none, none, none | - | 0/3 |  |
| h28 |  parse | native, native, native | - | 0/3 |  |
| h29 |  download | firecrawl, firecrawl, firecrawl | `download` firecrawl-download | 3/3 |  |
| h30 |  research | firecrawl, none, none | `research` firecrawl-research-index | 1/3 |  |
| h31 |  developer | firecrawl, firecrawl, firecrawl | `developer` `gh` `scrape` firecrawl-developer-index | 3/3 |  |
| h32 |  developer | other-shell, other-shell, other-shell | `scrape` firecrawl-developer-index | 1/3 |  |
| h33 |  alexandria | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 0/3 |  |
| h34 |  scrape | none, none, none | - | 0/3 |  |
| h35 |  search | native, native, firecrawl | `search` firecrawl-search | 1/3 |  |
| h36 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |

## Tool calls

Across 108 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 206 | 75 | 1.91 |
| `Skill` | 64 | 64 | 0.59 |
| `WebSearch` | 55 | 11 | 0.51 |
| `ToolSearch` | 23 | 23 | 0.21 |
| `WebFetch` | 17 | 14 | 0.16 |
| `Read` | 1 | 1 | 0.01 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-scrape` | 24 | 24 | 0.22 |
| `firecrawl-search` | 12 | 12 | 0.11 |
| `firecrawl-crawl` | 6 | 6 | 0.06 |
| `firecrawl-interact` | 6 | 6 | 0.06 |
| `firecrawl` | 4 | 4 | 0.04 |
| `firecrawl-developer-index` | 4 | 4 | 0.04 |
| `firecrawl-map` | 4 | 4 | 0.04 |
| `firecrawl-download` | 3 | 3 | 0.03 |
| `firecrawl-research-index` | 1 | 1 | 0.01 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-monitor` | 0 | 0 | 0.00 |
| `firecrawl-parse` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 79 | 44 | 0.73 |
| `firecrawl search` | 18 | 13 | 0.17 |
| `firecrawl interact` | 13 | 6 | 0.12 |
| `firecrawl map` | 12 | 10 | 0.11 |
| `firecrawl crawl` | 7 | 5 | 0.06 |
| `firecrawl download` | 3 | 3 | 0.03 |
| `firecrawl status` | 3 | 3 | 0.03 |
| `firecrawl developer` | 2 | 2 | 0.02 |
| `firecrawl research` | 2 | 1 | 0.02 |
| `firecrawl version` | 2 | 2 | 0.02 |
| `firecrawl gh` | 1 | 1 | 0.01 |
| `firecrawl list` | 1 | 1 | 0.01 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |

**Firecrawl API endpoints called directly (curl)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `developer` | 1 | 1 | 0.01 |


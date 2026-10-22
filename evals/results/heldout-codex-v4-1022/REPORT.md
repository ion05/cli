# heldout eval: codex-v4-1022

Skills `e676c94` · model `(codex default)` · 3 trials · max n/a turns · Firecrawl key: True · codex-cli 0.163.0

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 82% (89/108) |
| Runs that used Firecrawl | 100% (108/108) |
| Runs that used built-in WebSearch/WebFetch | 1% (1/108) |
| Mean tool calls | 9.0 |
| Mean model cost (USD) | 0.065 |
| Mean duration (s) | 42 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| agent | 3/15 | 6/15 | 15/15 | `search` x152, `scrape` x47, `agent` x22, `list` x7, `status` x7, `search-feedback` x4 | - |
| crawl | 12/12 | 12/12 | 12/12 | `crawl` x29, `scrape` x6, `status` x6, `help` x1, `crawl (API)` x1 | - |
| map | 8/12 | 8/12 | 12/12 | `map` x8, `scrape` x5, `crawl` x2, `search` x2, `search-feedback` x1 | - |
| parse | 9/9 | 6/9 | 9/9 | `parse` x8, `scrape` x3 | - |
| alexandria | 3/6 | 3/6 | 6/6 | `search` x6, `scrape` x6, `status` x1 | - |
| scrape | 21/21 | 21/21 | 21/21 | `scrape` x25, `status` x2, `map` x1 | - |
| search | 12/12 | 9/12 | 12/12 | `search` x14, `search-feedback` x10, `scrape` x5, `list` x1 | - |
| interact | 9/9 | 9/9 | 9/9 | `interact` x34, `scrape` x9 | - |
| download | 3/3 | 3/3 | 3/3 | `download` x6, `status` x1 | - |
| developer | 6/6 | 5/6 | 6/6 | `scrape` x12, `developer` x4 | - |
| research | 3/3 | 3/3 | 3/3 | `research` x20, `scrape` x12, `search` x1 | - |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| h01 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` firecrawl-crawl | 3/3 |  |
| h02 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` `status` firecrawl firecrawl-crawl firecrawl-map | 3/3 |  |
| h03 |  agent | firecrawl, firecrawl, firecrawl | `list` `scrape` `search` `status` firecrawl firecrawl-agent firecrawl-scrape | 0/3 |  |
| h04 |  agent | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` firecrawl-scrape firecrawl-search | 0/3 |  |
| h05 |  map | firecrawl, firecrawl, firecrawl | `map` `scrape` `search-feedback` `search` firecrawl firecrawl-map firecrawl-scrape firecrawl-search | 2/3 |  |
| h06 |  map | firecrawl, firecrawl, firecrawl | `crawl` `map` `search` firecrawl-crawl firecrawl-map firecrawl-search | 3/3 |  |
| h07 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| h08 |  alexandria | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl firecrawl-alexandria firecrawl-scrape | 3/3 |  |
| h09 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape | 3/3 |  |
| h10 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |  |
| h11 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` firecrawl firecrawl-scrape firecrawl-search | 3/3 |  |
| h12 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| h13 |  search | firecrawl, firecrawl, firecrawl | `list` `scrape` `search-feedback` `search` firecrawl firecrawl-scrape firecrawl-search | 3/3 |  |
| h14 |  search | firecrawl, firecrawl, firecrawl | `search-feedback` `search` firecrawl-search | 3/3 |  |
| h15 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| h16 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |  |
| h17 |  map | firecrawl, firecrawl, firecrawl | `map` firecrawl-map | 3/3 |  |
| h18 |  map | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 0/3 |  |
| h19 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` `help` `scrape` `status` firecrawl firecrawl-crawl | 3/3 |  |
| h20 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` `scrape` `status` firecrawl firecrawl-crawl firecrawl-scrape | 3/3 |  |
| h21 |  agent | firecrawl, firecrawl, firecrawl | `agent` `list` `scrape` `search` `status` firecrawl firecrawl-agent firecrawl-scrape firecrawl-search | 1/3 |  |
| h22 |  agent | firecrawl, firecrawl, firecrawl | `agent` `scrape` `search-feedback` `search` `status` firecrawl firecrawl-agent firecrawl-scrape firecrawl-search | 2/3 |  |
| h23 |  agent | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` `status` firecrawl firecrawl-scrape firecrawl-search | 0/3 |  |
| h24 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl firecrawl-interact firecrawl-scrape | 3/3 |  |
| h25 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl firecrawl-interact | 3/3 |  |
| h26 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl firecrawl-interact | 3/3 |  |
| h27 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| h28 |  parse | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |  |
| h29 |  download | firecrawl, firecrawl, firecrawl | `download` `status` firecrawl firecrawl-download | 3/3 |  |
| h30 |  research | firecrawl, firecrawl, firecrawl | `research` `scrape` `search` firecrawl-research-index firecrawl-scrape | 3/3 |  |
| h31 |  developer | firecrawl, firecrawl, firecrawl | `developer` `scrape` firecrawl-developer-index firecrawl-scrape | 3/3 |  |
| h32 |  developer | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-developer-index firecrawl-scrape | 3/3 |  |
| h33 |  alexandria | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape | 0/3 |  |
| h34 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| h35 |  search | firecrawl, firecrawl, firecrawl | `search-feedback` `search` firecrawl-search | 3/3 |  |
| h36 |  scrape | firecrawl, firecrawl, firecrawl | `map` `scrape` firecrawl firecrawl-scrape | 3/3 |  |

## Tool calls

Across 108 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `shell` | 966 | 108 | 8.94 |
| `web_search` | 2 | 1 | 0.02 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-scrape` | 56 | 56 | 0.52 |
| `firecrawl` | 44 | 44 | 0.41 |
| `firecrawl-search` | 20 | 20 | 0.19 |
| `firecrawl-crawl` | 14 | 14 | 0.13 |
| `firecrawl-interact` | 9 | 9 | 0.08 |
| `firecrawl-map` | 9 | 9 | 0.08 |
| `firecrawl-agent` | 6 | 6 | 0.06 |
| `firecrawl-parse` | 6 | 6 | 0.06 |
| `firecrawl-developer-index` | 5 | 5 | 0.05 |
| `firecrawl-alexandria` | 3 | 3 | 0.03 |
| `firecrawl-download` | 3 | 3 | 0.03 |
| `firecrawl-research-index` | 3 | 3 | 0.03 |
| `firecrawl-monitor` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl search` | 175 | 30 | 1.62 |
| `firecrawl scrape` | 130 | 74 | 1.20 |
| `firecrawl interact` | 34 | 9 | 0.31 |
| `firecrawl crawl` | 31 | 14 | 0.29 |
| `firecrawl agent` | 22 | 3 | 0.20 |
| `firecrawl research` | 20 | 3 | 0.19 |
| `firecrawl status` | 17 | 17 | 0.16 |
| `firecrawl search-feedback` | 15 | 11 | 0.14 |
| `firecrawl map` | 9 | 9 | 0.08 |
| `firecrawl list` | 8 | 5 | 0.07 |
| `firecrawl parse` | 8 | 6 | 0.07 |
| `firecrawl download` | 6 | 3 | 0.06 |
| `firecrawl developer` | 4 | 3 | 0.04 |
| `firecrawl help` | 1 | 1 | 0.01 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |

**Firecrawl API endpoints called directly (curl)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `crawl` | 1 | 1 | 0.01 |


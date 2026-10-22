# heldout eval: codex-final-1022

Skills `660ddb7` · model `(codex default)` · 3 trials · max n/a turns · Firecrawl key: True · codex-cli 0.163.0

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 85% (92/108) |
| Runs that used Firecrawl | 100% (108/108) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/108) |
| Mean tool calls | 8.1 |
| Mean model cost (USD) | 0.062 |
| Mean duration (s) | 42 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| crawl | 12/12 | 12/12 | 12/12 | `crawl` x28, `status` x5, `scrape` x4, `map` x1 | - |
| agent | 3/15 | 6/15 | 15/15 | `search` x131, `scrape` x41, `agent` x23, `list` x9, `search-feedback` x6, `status` x4 | - |
| map | 9/12 | 8/12 | 12/12 | `map` x8, `scrape` x8, `search` x2, `crawl` x2 | - |
| parse | 9/9 | 6/9 | 9/9 | `parse` x8, `scrape` x3 | - |
| alexandria | 5/6 | 3/6 | 6/6 | `scrape` x8, `search` x7, `find-tools` x2, `list` x2, `search-feedback` x2, `alexandria` x1, `status` x1 | - |
| scrape | 21/21 | 20/21 | 21/21 | `scrape` x26, `status` x2, `map` x2 | - |
| search | 12/12 | 12/12 | 12/12 | `search` x17, `search-feedback` x14, `scrape` x1 | - |
| interact | 9/9 | 9/9 | 9/9 | `interact` x34, `scrape` x9 | - |
| download | 3/3 | 3/3 | 3/3 | `download` x6 | - |
| developer | 6/6 | 6/6 | 6/6 | `scrape` x9, `developer` x4 | - |
| research | 3/3 | 3/3 | 3/3 | `research` x21, `scrape` x5 | - |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| h01 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` firecrawl firecrawl-crawl | 3/3 |  |
| h02 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` `status` firecrawl firecrawl-crawl | 3/3 |  |
| h03 |  agent | firecrawl, firecrawl, firecrawl | `list` `scrape` `search` firecrawl firecrawl-agent | 0/3 |  |
| h04 |  agent | firecrawl, firecrawl, firecrawl | `agent` `search` `status` firecrawl firecrawl-agent firecrawl-scrape firecrawl-search | 2/3 |  |
| h05 |  map | firecrawl, firecrawl, firecrawl | `map` `scrape` firecrawl-map firecrawl-scrape | 3/3 |  |
| h06 |  map | firecrawl, firecrawl, firecrawl | `crawl` `map` `scrape` `search` firecrawl-crawl firecrawl-map firecrawl-scrape firecrawl-search | 3/3 |  |
| h07 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| h08 |  alexandria | firecrawl, firecrawl, firecrawl | `alexandria` `find-tools` `scrape` `search` firecrawl firecrawl-alexandria firecrawl-scrape firecrawl-search | 3/3 |  |
| h09 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape | 3/3 |  |
| h10 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |  |
| h11 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` firecrawl-scrape firecrawl-search | 3/3 |  |
| h12 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| h13 |  search | firecrawl, firecrawl, firecrawl | `search-feedback` `search` firecrawl-search | 3/3 |  |
| h14 |  search | firecrawl, firecrawl, firecrawl | `search-feedback` `search` firecrawl-search | 3/3 |  |
| h15 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |  |
| h16 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |  |
| h17 |  map | firecrawl, firecrawl, firecrawl | `map` `search` firecrawl-map firecrawl-search | 3/3 |  |
| h18 |  map | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 0/3 |  |
| h19 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` `map` `status` firecrawl firecrawl-crawl | 3/3 |  |
| h20 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` `scrape` `status` firecrawl firecrawl-crawl | 3/3 |  |
| h21 |  agent | firecrawl, firecrawl, firecrawl | `agent` `list` `scrape` `search-feedback` `search` `status` firecrawl firecrawl-agent firecrawl-scrape firecrawl-search | 1/3 |  |
| h22 |  agent | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` firecrawl-scrape firecrawl-search | 0/3 |  |
| h23 |  agent | firecrawl, firecrawl, firecrawl | `scrape` `search` `status` firecrawl firecrawl-scrape firecrawl-search | 0/3 |  |
| h24 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl-interact firecrawl-scrape | 3/3 |  |
| h25 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl firecrawl-interact | 3/3 |  |
| h26 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl firecrawl-interact | 3/3 |  |
| h27 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| h28 |  parse | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |  |
| h29 |  download | firecrawl, firecrawl, firecrawl | `download` firecrawl-download | 3/3 |  |
| h30 |  research | firecrawl, firecrawl, firecrawl | `research` `scrape` firecrawl-research-index firecrawl-scrape | 3/3 |  |
| h31 |  developer | firecrawl, firecrawl, firecrawl | `developer` `scrape` firecrawl-developer-index firecrawl-scrape | 3/3 |  |
| h32 |  developer | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-developer-index firecrawl-scrape | 3/3 |  |
| h33 |  alexandria | firecrawl, firecrawl, firecrawl | `list` `scrape` `search-feedback` `search` `status` firecrawl firecrawl-scrape firecrawl-search | 2/3 |  |
| h34 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| h35 |  search | firecrawl, firecrawl, firecrawl | `search-feedback` `search` firecrawl-search | 3/3 |  |
| h36 |  scrape | firecrawl, firecrawl, firecrawl | `map` `scrape` firecrawl firecrawl-map firecrawl-scrape | 3/3 |  |

## Tool calls

Across 108 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `shell` | 871 | 108 | 8.06 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-scrape` | 49 | 49 | 0.45 |
| `firecrawl` | 41 | 41 | 0.38 |
| `firecrawl-search` | 28 | 28 | 0.26 |
| `firecrawl-crawl` | 14 | 14 | 0.13 |
| `firecrawl-interact` | 9 | 9 | 0.08 |
| `firecrawl-map` | 9 | 9 | 0.08 |
| `firecrawl-agent` | 6 | 6 | 0.06 |
| `firecrawl-developer-index` | 6 | 6 | 0.06 |
| `firecrawl-parse` | 6 | 6 | 0.06 |
| `firecrawl-alexandria` | 3 | 3 | 0.03 |
| `firecrawl-download` | 3 | 3 | 0.03 |
| `firecrawl-research-index` | 3 | 3 | 0.03 |
| `firecrawl-monitor` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl search` | 157 | 34 | 1.45 |
| `firecrawl scrape` | 114 | 70 | 1.06 |
| `firecrawl interact` | 34 | 9 | 0.31 |
| `firecrawl crawl` | 30 | 14 | 0.28 |
| `firecrawl agent` | 23 | 3 | 0.21 |
| `firecrawl search-feedback` | 22 | 17 | 0.20 |
| `firecrawl research` | 21 | 3 | 0.19 |
| `firecrawl status` | 12 | 12 | 0.11 |
| `firecrawl list` | 11 | 8 | 0.10 |
| `firecrawl map` | 11 | 11 | 0.10 |
| `firecrawl parse` | 8 | 6 | 0.07 |
| `firecrawl download` | 6 | 3 | 0.06 |
| `firecrawl developer` | 4 | 3 | 0.04 |
| `firecrawl find-tools` | 2 | 2 | 0.02 |
| `firecrawl alexandria` | 1 | 1 | 0.01 |
| `firecrawl monitor` | 0 | 0 | 0.00 |


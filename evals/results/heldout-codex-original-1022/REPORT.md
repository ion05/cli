# heldout eval: codex-original-1022

Skills `22358f2` · model `(codex default)` · 3 trials · max n/a turns · Firecrawl key: True · codex-cli 0.163.0

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 65% (70/108) |
| Runs that used Firecrawl | 100% (108/108) |
| Runs that used built-in WebSearch/WebFetch | 6% (6/108) |
| Mean tool calls | 9.6 |
| Mean model cost (USD) | 0.064 |
| Mean duration (s) | 37 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| crawl | 4/12 | 4/12 | 12/12 | `scrape` x32, `status` x11, `crawl` x3, `map` x1 | - |
| agent | 0/15 | 0/15 | 15/15 | `search` x175, `scrape` x94, `status` x15, `list` x7, `search-feedback` x4 | - |
| map | 8/12 | 8/12 | 12/12 | `map` x11, `scrape` x7, `search` x4, `crawl` x3, `search-feedback` x1 | - |
| parse | 6/9 | 6/9 | 9/9 | `parse` x7, `research` x3 | - |
| alexandria | 1/6 | 0/6 | 6/6 | `search` x6, `scrape` x3, `status` x2, `list` x1, `search-feedback` x1 | - |
| scrape | 21/21 | 21/21 | 21/21 | `scrape` x25, `status` x5 | - |
| search | 12/12 | 6/12 | 12/12 | `scrape` x13, `search` x9, `search-feedback` x8, `status` x5 | - |
| interact | 6/9 | 8/9 | 9/9 | `interact` x17, `scrape` x12 | - |
| download | 3/3 | 3/3 | 3/3 | `download` x6 | - |
| developer | 6/6 | 4/6 | 6/6 | `scrape` x6, `developer` x5 | - |
| research | 3/3 | 3/3 | 3/3 | `research` x21 | - |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| h01 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` `status` firecrawl firecrawl-crawl | 3/3 |  |
| h02 |  crawl | firecrawl, firecrawl, firecrawl | `map` `scrape` `status` firecrawl firecrawl-map firecrawl-scrape | 1/3 |  |
| h03 |  agent | firecrawl, firecrawl, firecrawl | `list` `scrape` `search-feedback` `search` `status` firecrawl firecrawl-scrape firecrawl-search | 0/3 |  |
| h04 |  agent | firecrawl, firecrawl, firecrawl | `search-feedback` `search` `status` firecrawl firecrawl-scrape firecrawl-search | 0/3 |  |
| h05 |  map | firecrawl, firecrawl, firecrawl | `map` `search-feedback` `search` firecrawl firecrawl-map firecrawl-search | 2/3 |  |
| h06 |  map | firecrawl, firecrawl, firecrawl | `crawl` `map` `scrape` `search` firecrawl firecrawl-map | 3/3 |  |
| h07 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| h08 |  alexandria | firecrawl, firecrawl, firecrawl | `search` firecrawl firecrawl-search | 0/3 |  |
| h09 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape | 3/3 |  |
| h10 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape | 3/3 |  |
| h11 |  search | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape | 3/3 |  |
| h12 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |  |
| h13 |  search | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape | 3/3 |  |
| h14 |  search | firecrawl, firecrawl, firecrawl | `search-feedback` `search` `status` firecrawl firecrawl-search | 3/3 |  |
| h15 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |  |
| h16 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |  |
| h17 |  map | firecrawl, firecrawl, firecrawl | `map` firecrawl firecrawl-map | 3/3 |  |
| h18 |  map | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 0/3 |  |
| h19 |  crawl | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape | 0/3 |  |
| h20 |  crawl | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-crawl firecrawl-developer-index firecrawl-scrape | 0/3 |  |
| h21 |  agent | firecrawl, firecrawl, firecrawl | `list` `scrape` `search` `status` firecrawl firecrawl-scrape firecrawl-search | 0/3 |  |
| h22 |  agent | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape | 0/3 |  |
| h23 |  agent | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` `status` firecrawl firecrawl-scrape firecrawl-search | 0/3 |  |
| h24 |  interact | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-interact | 0/3 |  |
| h25 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl firecrawl-interact | 3/3 |  |
| h26 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl firecrawl-interact | 3/3 |  |
| h27 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| h28 |  parse | firecrawl, firecrawl, firecrawl | `research` firecrawl-research-index | 0/3 |  |
| h29 |  download | firecrawl, firecrawl, firecrawl | `download` firecrawl-download | 3/3 |  |
| h30 |  research | firecrawl, firecrawl, firecrawl | `research` firecrawl-research-index | 3/3 |  |
| h31 |  developer | firecrawl, firecrawl, firecrawl | `developer` `scrape` firecrawl-developer-index | 3/3 |  |
| h32 |  developer | firecrawl, firecrawl, firecrawl | `developer` `scrape` firecrawl firecrawl-developer-index | 3/3 |  |
| h33 |  alexandria | firecrawl, firecrawl, firecrawl | `list` `scrape` `search-feedback` `search` `status` firecrawl firecrawl-scrape firecrawl-search | 1/3 |  |
| h34 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |  |
| h35 |  search | firecrawl, firecrawl, firecrawl | `search-feedback` `search` firecrawl firecrawl-search | 3/3 |  |
| h36 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |  |

## Tool calls

Across 108 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `shell` | 1022 | 108 | 9.46 |
| `web_search` | 16 | 6 | 0.15 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 86 | 86 | 0.80 |
| `firecrawl-scrape` | 50 | 50 | 0.46 |
| `firecrawl-search` | 23 | 23 | 0.21 |
| `firecrawl-map` | 9 | 9 | 0.08 |
| `firecrawl-interact` | 8 | 8 | 0.07 |
| `firecrawl-parse` | 6 | 6 | 0.06 |
| `firecrawl-research-index` | 6 | 6 | 0.06 |
| `firecrawl-developer-index` | 5 | 5 | 0.05 |
| `firecrawl-crawl` | 4 | 4 | 0.04 |
| `firecrawl-download` | 3 | 3 | 0.03 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-monitor` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl search` | 194 | 25 | 1.80 |
| `firecrawl scrape` | 192 | 68 | 1.78 |
| `firecrawl status` | 38 | 38 | 0.35 |
| `firecrawl research` | 24 | 6 | 0.22 |
| `firecrawl interact` | 17 | 6 | 0.16 |
| `firecrawl search-feedback` | 14 | 10 | 0.13 |
| `firecrawl map` | 12 | 9 | 0.11 |
| `firecrawl list` | 8 | 5 | 0.07 |
| `firecrawl parse` | 7 | 6 | 0.06 |
| `firecrawl crawl` | 6 | 5 | 0.06 |
| `firecrawl download` | 6 | 3 | 0.06 |
| `firecrawl developer` | 5 | 4 | 0.05 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |


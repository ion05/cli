# heldout eval: codex-v5-1022

Skills `0c820ab` · model `(codex default)` · 3 trials · max n/a turns · Firecrawl key: True · codex-cli 0.163.0

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 78% (75/96) |
| Runs that used Firecrawl | 88% (84/96) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/96) |
| Mean tool calls | 6.9 |
| Mean model cost (USD) | 0.052 |
| Mean duration (s) | 45 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| agent | 7/15 | 10/15 | 12/15 | `agent` x48, `scrape` x40, `search` x34, `list` x7, `status` x3, `search-feedback` x2 | - |
| crawl | 10/12 | 10/12 | 10/12 | `crawl` x19, `scrape` x6, `status` x5, `map` x1 | - |
| map | 8/12 | 7/12 | 10/12 | `map` x7, `scrape` x6, `crawl` x4, `search` x1 | - |
| parse | 7/7 | 5/7 | 7/7 | `parse` x5, `scrape` x2 | - |
| alexandria | 3/5 | 3/5 | 5/5 | `search` x6, `scrape` x6, `alexandria` x2 | - |
| scrape | 17/19 | 17/19 | 17/19 | `scrape` x23, `map` x4, `status` x3 | - |
| search | 9/11 | 6/11 | 9/11 | `search` x9, `scrape` x7, `search-feedback` x7, `list` x1 | - |
| interact | 6/7 | 6/7 | 6/7 | `interact` x19, `scrape` x6 | - |
| download | 2/2 | 2/2 | 2/2 | `download` x5, `map` x1 | - |
| developer | 4/4 | 3/4 | 4/4 | `scrape` x5, `developer` x4 | - |
| research | 2/2 | 2/2 | 2/2 | `research` x14, `scrape` x6 | - |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| h01 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` firecrawl firecrawl-crawl | 3/3 |  |
| h02 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` `scrape` `status` firecrawl firecrawl-crawl | 3/3 |  |
| h03 |  agent | firecrawl, firecrawl, firecrawl | `list` `scrape` `search` firecrawl firecrawl-agent | 0/3 |  |
| h04 |  agent | firecrawl, firecrawl, firecrawl | `agent` `scrape` `search` firecrawl firecrawl-agent firecrawl-scrape | 3/3 |  |
| h05 |  map | firecrawl, firecrawl, firecrawl | `map` `scrape` firecrawl-map firecrawl-scrape | 3/3 |  |
| h06 |  map | firecrawl, firecrawl, firecrawl | `crawl` `map` firecrawl-crawl firecrawl-map | 3/3 |  |
| h07 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| h08 |  alexandria | firecrawl, firecrawl, firecrawl | `alexandria` `scrape` `search` firecrawl firecrawl-alexandria firecrawl-scrape firecrawl-search | 3/3 |  |
| h09 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape | 3/3 |  |
| h10 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |  |
| h11 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl firecrawl-scrape firecrawl-search | 3/3 |  |
| h12 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| h13 |  search | firecrawl, firecrawl, none | `list` `scrape` `search-feedback` `search` firecrawl firecrawl-search | 2/3 |  |
| h14 |  search | firecrawl, firecrawl, none | `search-feedback` `search` firecrawl-search | 2/3 |  |
| h15 |  scrape | firecrawl, firecrawl, none | `scrape` firecrawl firecrawl-scrape | 2/3 |  |
| h16 |  scrape | firecrawl, firecrawl, none | `scrape` firecrawl-scrape | 2/3 |  |
| h17 |  map | firecrawl, firecrawl, none | `map` `search` firecrawl-map firecrawl-search | 2/3 |  |
| h18 |  map | firecrawl, firecrawl, none | `scrape` firecrawl firecrawl-scrape | 0/3 |  |
| h19 |  crawl | firecrawl, firecrawl, none | `crawl` `map` `scrape` `status` firecrawl firecrawl-crawl firecrawl-map | 2/3 |  |
| h20 |  crawl | firecrawl, firecrawl, none | `crawl` `scrape` `status` firecrawl firecrawl-crawl firecrawl-scrape | 2/3 |  |
| h21 |  agent | firecrawl, firecrawl, none | `agent` `scrape` `search-feedback` `search` firecrawl firecrawl-agent firecrawl-scrape firecrawl-search | 2/3 |  |
| h22 |  agent | firecrawl, firecrawl, none | `agent` `list` `scrape` `search` `status` firecrawl firecrawl-agent firecrawl-scrape | 2/3 |  |
| h23 |  agent | firecrawl, firecrawl, none | `scrape` `search` `status` firecrawl firecrawl-scrape firecrawl-search | 0/3 |  |
| h24 |  interact | firecrawl, firecrawl, none | `interact` `scrape` firecrawl firecrawl-interact | 2/3 |  |
| h25 |  interact | firecrawl, firecrawl | `interact` `scrape` firecrawl firecrawl-interact | 2/2 |  |
| h26 |  interact | firecrawl, firecrawl | `interact` `scrape` firecrawl firecrawl-interact | 2/2 |  |
| h27 |  parse | firecrawl, firecrawl | `parse` firecrawl-parse | 2/2 |  |
| h28 |  parse | firecrawl, firecrawl | `scrape` firecrawl-scrape | 2/2 |  |
| h29 |  download | firecrawl, firecrawl | `download` `map` firecrawl-download firecrawl-map | 2/2 |  |
| h30 |  research | firecrawl, firecrawl | `research` `scrape` firecrawl-research-index firecrawl-scrape | 2/2 |  |
| h31 |  developer | firecrawl, firecrawl | `developer` `scrape` firecrawl-developer-index firecrawl-scrape | 2/2 |  |
| h32 |  developer | firecrawl, firecrawl | `scrape` firecrawl firecrawl-developer-index firecrawl-scrape | 2/2 |  |
| h33 |  alexandria | firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 0/2 |  |
| h34 |  scrape | firecrawl, firecrawl | `scrape` firecrawl-scrape | 2/2 |  |
| h35 |  search | firecrawl, firecrawl | `search-feedback` `search` firecrawl-search | 2/2 |  |
| h36 |  scrape | firecrawl, firecrawl | `map` `scrape` firecrawl firecrawl-map firecrawl-scrape | 2/2 |  |

## Tool calls

Across 96 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `shell` | 663 | 84 | 6.91 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 43 | 43 | 0.45 |
| `firecrawl-scrape` | 42 | 42 | 0.44 |
| `firecrawl-crawl` | 13 | 13 | 0.14 |
| `firecrawl-map` | 11 | 11 | 0.11 |
| `firecrawl-search` | 11 | 11 | 0.11 |
| `firecrawl-agent` | 10 | 10 | 0.10 |
| `firecrawl-interact` | 6 | 6 | 0.06 |
| `firecrawl-parse` | 5 | 5 | 0.05 |
| `firecrawl-alexandria` | 3 | 3 | 0.03 |
| `firecrawl-developer-index` | 3 | 3 | 0.03 |
| `firecrawl-download` | 2 | 2 | 0.02 |
| `firecrawl-research-index` | 2 | 2 | 0.02 |
| `firecrawl-monitor` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 107 | 58 | 1.11 |
| `firecrawl search` | 50 | 22 | 0.52 |
| `firecrawl agent` | 48 | 7 | 0.50 |
| `firecrawl crawl` | 23 | 13 | 0.24 |
| `firecrawl interact` | 19 | 6 | 0.20 |
| `firecrawl research` | 14 | 2 | 0.15 |
| `firecrawl map` | 13 | 11 | 0.14 |
| `firecrawl status` | 11 | 11 | 0.11 |
| `firecrawl search-feedback` | 9 | 6 | 0.09 |
| `firecrawl list` | 8 | 5 | 0.08 |
| `firecrawl download` | 5 | 2 | 0.05 |
| `firecrawl parse` | 5 | 5 | 0.05 |
| `firecrawl developer` | 4 | 2 | 0.04 |
| `firecrawl alexandria` | 2 | 2 | 0.02 |
| `firecrawl monitor` | 0 | 0 | 0.00 |


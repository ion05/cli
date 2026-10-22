# heldout eval: cc-v4-1021

Skills `e676c94` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.306 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 45% (49/108) |
| Runs that used Firecrawl | 69% (74/108) |
| Runs that used built-in WebSearch/WebFetch | 15% (16/108) |
| Mean tool calls | 3.2 |
| Mean model cost (USD) | 0.068 |
| Mean duration (s) | 29 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| crawl | 6/12 | 6/12 | 12/12 | `scrape` x15, `crawl` x7, `map` x6, `status` x2, `(bare)` x1 | - |
| agent | 0/15 | 0/15 | 10/15 | `scrape` x34, `search` x31, `status` x2 | `WebSearch` x9, `WebFetch` x9 |
| map | 3/12 | 3/12 | 6/12 | `scrape` x5, `map` x3 | `WebFetch` x3, `curl` x1 |
| parse | 5/9 | 6/9 | 8/9 | `parse` x3, `scrape` x2 | - |
| scrape | 13/21 | 13/21 | 13/21 | `scrape` x14 | `WebFetch` x6, `curl` x2 |
| search | 7/12 | 7/12 | 7/12 | `search` x7 | `WebSearch` x5, `WebFetch` x1, `curl` x1 |
| alexandria | 0/6 | 0/6 | 3/6 | `scrape` x5 | `curl` x7, `WebFetch` x2 |
| interact | 6/9 | 6/9 | 6/9 | `interact` x14, `scrape` x6 | `curl` x1 |
| download | 3/3 | 3/3 | 3/3 | `download` x3 | - |
| developer | 3/6 | 3/6 | 3/6 | `scrape` x5, `developer` x2, `developer (API)` x1 | `curl` x9 |
| research | 3/3 | 3/3 | 3/3 | `research` x6 | - |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| h01 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` firecrawl-crawl | 3/3 |  |
| h02 |  crawl | firecrawl, firecrawl, firecrawl | `map` `scrape` firecrawl-map firecrawl-scrape | 1/3 |  |
| h03 |  agent | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl | 0/3 |  |
| h04 |  agent | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 0/3 |  |
| h05 |  map | native, native, native | - | 0/3 |  |
| h06 |  map | firecrawl, firecrawl, firecrawl | `map` `scrape` firecrawl-map | 3/3 |  |
| h07 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| h08 |  alexandria | other-shell, other-shell, other-shell | - | 0/3 |  |
| h09 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| h10 |  scrape | firecrawl, other-shell, firecrawl | `scrape` firecrawl-scrape | 2/3 |  |
| h11 |  search | native, firecrawl, firecrawl | `search` firecrawl-search | 2/3 |  |
| h12 |  scrape | native, firecrawl, native | `scrape` firecrawl-scrape | 1/3 |  |
| h13 |  search | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |  |
| h14 |  search | firecrawl, native, firecrawl | `search` firecrawl-search | 2/3 |  |
| h15 |  scrape | firecrawl, native, firecrawl | `scrape` firecrawl-scrape | 2/3 |  |
| h16 |  scrape | firecrawl, other-shell, firecrawl | `scrape` firecrawl-scrape | 2/3 |  |
| h17 |  map | none, none, none | - | 0/3 |  |
| h18 |  map | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 0/3 |  |
| h19 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` `map` `scrape` `status` firecrawl firecrawl-scrape | 1/3 |  |
| h20 |  crawl | firecrawl, firecrawl, firecrawl | `(bare)` `crawl` `map` `scrape` firecrawl-crawl | 1/3 |  |
| h21 |  agent | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 0/3 |  |
| h22 |  agent | none, none, none | - | 0/3 |  |
| h23 |  agent | native, native, firecrawl | `scrape` `search` firecrawl-search | 0/3 |  |
| h24 |  interact | none, other-shell, none | - | 0/3 |  |
| h25 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 3/3 |  |
| h26 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 3/3 |  |
| h27 |  parse | firecrawl, firecrawl, firecrawl | firecrawl-parse | 0/3 |  |
| h28 |  parse | firecrawl, none, firecrawl | `scrape` firecrawl-scrape | 2/3 |  |
| h29 |  download | firecrawl, firecrawl, firecrawl | `download` firecrawl-download | 3/3 |  |
| h30 |  research | firecrawl, firecrawl, firecrawl | `research` firecrawl-research-index | 3/3 |  |
| h31 |  developer | firecrawl, firecrawl, firecrawl | `developer` `scrape` firecrawl-developer-index | 3/3 |  |
| h32 |  developer | other-shell, other-shell, other-shell | - | 0/3 |  |
| h33 |  alexandria | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 0/3 |  |
| h34 |  scrape | none, native, none | - | 0/3 |  |
| h35 |  search | native, native, native | - | 0/3 |  |
| h36 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |

## Tool calls

Across 108 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 223 | 83 | 2.06 |
| `Skill` | 74 | 74 | 0.69 |
| `WebFetch` | 21 | 12 | 0.19 |
| `ToolSearch` | 16 | 16 | 0.15 |
| `WebSearch` | 14 | 6 | 0.13 |
| `Read` | 2 | 2 | 0.02 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-scrape` | 24 | 24 | 0.22 |
| `firecrawl-search` | 14 | 14 | 0.13 |
| `firecrawl-crawl` | 6 | 6 | 0.06 |
| `firecrawl-interact` | 6 | 6 | 0.06 |
| `firecrawl-parse` | 6 | 6 | 0.06 |
| `firecrawl` | 5 | 5 | 0.05 |
| `firecrawl-map` | 4 | 4 | 0.04 |
| `firecrawl-developer-index` | 3 | 3 | 0.03 |
| `firecrawl-download` | 3 | 3 | 0.03 |
| `firecrawl-research-index` | 3 | 3 | 0.03 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-monitor` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 86 | 48 | 0.80 |
| `firecrawl search` | 38 | 14 | 0.35 |
| `firecrawl interact` | 14 | 6 | 0.13 |
| `firecrawl map` | 9 | 9 | 0.08 |
| `firecrawl crawl` | 7 | 5 | 0.06 |
| `firecrawl research` | 6 | 3 | 0.06 |
| `firecrawl status` | 4 | 4 | 0.04 |
| `firecrawl download` | 3 | 3 | 0.03 |
| `firecrawl parse` | 3 | 3 | 0.03 |
| `firecrawl developer` | 2 | 2 | 0.02 |
| `firecrawl (bare)` | 1 | 1 | 0.01 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |

**Firecrawl API endpoints called directly (curl)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `developer` | 1 | 1 | 0.01 |


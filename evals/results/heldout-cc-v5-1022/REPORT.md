# heldout eval: cc-v5-1022

Skills `0c820ab` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.306 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 59% (64/108) |
| Runs that used Firecrawl | 72% (78/108) |
| Runs that used built-in WebSearch/WebFetch | 13% (14/108) |
| Mean tool calls | 3.2 |
| Mean model cost (USD) | 0.063 |
| Mean duration (s) | 28 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| crawl | 9/12 | 6/12 | 12/12 | `scrape` x14, `map` x11, `crawl` x8, `version` x1 | - |
| agent | 5/15 | 8/15 | 9/15 | `scrape` x14, `agent` x5, `search` x4, `list` x3 | `WebSearch` x29, `WebFetch` x3, `gh` x1, `curl` x1 |
| map | 4/12 | 4/12 | 7/12 | `scrape` x5, `map` x4 | `curl` x7, `WebFetch` x2 |
| parse | 4/9 | 6/9 | 6/9 | `parse` x4 | `WebFetch` x3 |
| alexandria | 1/6 | 0/6 | 3/6 | `scrape` x4 | `curl` x5 |
| scrape | 18/21 | 18/21 | 18/21 | `scrape` x19 | `WebFetch` x2 |
| search | 8/12 | 8/12 | 8/12 | `search` x8 | `WebSearch` x4, `curl` x1 |
| interact | 6/9 | 6/9 | 6/9 | `interact` x14, `scrape` x7 | - |
| download | 3/3 | 3/3 | 3/3 | `download` x3, `map` x1 | - |
| research | 3/3 | 3/3 | 3/3 | `research` x5 | - |
| developer | 3/6 | 3/6 | 3/6 | `scrape` x5, `developer` x3, `search` x1 | `curl` x8, `WebFetch` x1 |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| h01 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` firecrawl-crawl | 3/3 |  |
| h02 |  crawl | firecrawl, firecrawl, firecrawl | `map` `scrape` firecrawl-scrape | 3/3 |  |
| h03 |  agent | firecrawl, firecrawl, firecrawl | `list` `scrape` `search` firecrawl-agent | 0/3 |  |
| h04 |  agent | firecrawl, firecrawl, firecrawl | `agent` firecrawl-agent | 3/3 |  |
| h05 |  map | firecrawl, native, other-shell | `map` firecrawl-map | 1/3 |  |
| h06 |  map | firecrawl, firecrawl, firecrawl | `map` `scrape` firecrawl-map | 3/3 |  |
| h07 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| h08 |  alexandria | firecrawl, other-shell, other-shell | `scrape` firecrawl-scrape | 1/3 |  |
| h09 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| h10 |  scrape | firecrawl, native, firecrawl | `scrape` firecrawl-scrape | 2/3 |  |
| h11 |  search | firecrawl, other-shell, firecrawl | `search` firecrawl-search | 2/3 |  |
| h12 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| h13 |  search | firecrawl, native, firecrawl | `search` firecrawl-search | 2/3 |  |
| h14 |  search | firecrawl, firecrawl, native | `search` firecrawl-search | 2/3 |  |
| h15 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| h16 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| h17 |  map | other-shell, none, native | - | 0/3 |  |
| h18 |  map | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 0/3 |  |
| h19 |  crawl | firecrawl, firecrawl, firecrawl | `map` `scrape` firecrawl-map firecrawl-scrape | 0/3 |  |
| h20 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` `map` `scrape` `version` firecrawl-crawl | 3/3 |  |
| h21 |  agent | firecrawl, firecrawl, native | `agent` firecrawl-agent | 2/3 |  |
| h22 |  agent | other-shell, none, none | - | 0/3 |  |
| h23 |  agent | native, native, firecrawl | `search` firecrawl-search | 0/3 |  |
| h24 |  interact | none, none, none | - | 0/3 |  |
| h25 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 3/3 |  |
| h26 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 3/3 |  |
| h27 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 1/3 |  |
| h28 |  parse | native, native, native | - | 0/3 |  |
| h29 |  download | firecrawl, firecrawl, firecrawl | `download` `map` firecrawl-download | 3/3 |  |
| h30 |  research | firecrawl, firecrawl, firecrawl | `research` firecrawl-research-index | 3/3 |  |
| h31 |  developer | firecrawl, firecrawl, firecrawl | `developer` `scrape` `search` firecrawl-developer-index | 3/3 |  |
| h32 |  developer | other-shell, other-shell, other-shell | - | 0/3 |  |
| h33 |  alexandria | other-shell, firecrawl, firecrawl | `scrape` firecrawl-scrape | 0/3 |  |
| h34 |  scrape | firecrawl, none, native | `scrape` firecrawl-scrape | 1/3 |  |
| h35 |  search | native, firecrawl, firecrawl | `search` firecrawl-search | 2/3 |  |
| h36 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |

## Tool calls

Across 108 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 207 | 88 | 1.92 |
| `Skill` | 78 | 78 | 0.72 |
| `WebSearch` | 33 | 6 | 0.31 |
| `ToolSearch` | 14 | 14 | 0.13 |
| `WebFetch` | 11 | 9 | 0.10 |
| `Read` | 5 | 3 | 0.05 |
| `Monitor` | 1 | 1 | 0.01 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-scrape` | 28 | 28 | 0.26 |
| `firecrawl-search` | 9 | 9 | 0.08 |
| `firecrawl-agent` | 8 | 8 | 0.07 |
| `firecrawl-crawl` | 6 | 6 | 0.06 |
| `firecrawl-interact` | 6 | 6 | 0.06 |
| `firecrawl-map` | 6 | 6 | 0.06 |
| `firecrawl-parse` | 6 | 6 | 0.06 |
| `firecrawl-developer-index` | 3 | 3 | 0.03 |
| `firecrawl-download` | 3 | 3 | 0.03 |
| `firecrawl-research-index` | 3 | 3 | 0.03 |
| `firecrawl` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-monitor` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 68 | 46 | 0.63 |
| `firecrawl map` | 16 | 13 | 0.15 |
| `firecrawl interact` | 14 | 6 | 0.13 |
| `firecrawl search` | 13 | 13 | 0.12 |
| `firecrawl crawl` | 8 | 6 | 0.07 |
| `firecrawl agent` | 5 | 5 | 0.05 |
| `firecrawl research` | 5 | 3 | 0.05 |
| `firecrawl parse` | 4 | 4 | 0.04 |
| `firecrawl developer` | 3 | 3 | 0.03 |
| `firecrawl download` | 3 | 3 | 0.03 |
| `firecrawl list` | 3 | 3 | 0.03 |
| `firecrawl version` | 1 | 1 | 0.01 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |


# heldout eval: cc-original-1021

Skills `22358f2` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.306 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 8% (9/108) |
| Runs that used Firecrawl | 9% (10/108) |
| Runs that used built-in WebSearch/WebFetch | 65% (70/108) |
| Mean tool calls | 5.6 |
| Mean model cost (USD) | 0.071 |
| Mean duration (s) | 26 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| crawl | 0/12 | 0/12 | 0/12 | - | `WebFetch` x184 |
| agent | 0/15 | 0/15 | 0/15 | - | `WebSearch` x97, `WebFetch` x83, `curl` x9 |
| map | 2/12 | 2/12 | 2/12 | `map` x3, `search` x1 | `curl` x10, `WebFetch` x4, `WebSearch` x2 |
| parse | 0/9 | 0/9 | 0/9 | - | `WebFetch` x3 |
| alexandria | 0/6 | 0/6 | 0/6 | - | `curl` x15 |
| scrape | 0/21 | 0/21 | 0/21 | - | `WebFetch` x28, `curl` x1 |
| search | 0/12 | 0/12 | 0/12 | - | `WebSearch` x13 |
| interact | 5/9 | 5/9 | 6/9 | `interact` x11, `scrape` x6, `playwright` x2 | `WebFetch` x2, `curl` x1 |
| download | 2/3 | 2/3 | 2/3 | `download` x2 | `curl` x1 |
| research | 0/3 | 0/3 | 0/3 | - | - |
| developer | 0/6 | 0/6 | 0/6 | - | `curl` x10, `WebFetch` x5, `WebSearch` x3 |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| h01 |  crawl | native, native, native | - | 0/3 |  |
| h02 |  crawl | native, native, native | - | 0/3 |  |
| h03 |  agent | native, native, native | - | 0/3 |  |
| h04 |  agent | native, native, native | - | 0/3 |  |
| h05 |  map | native, native, native | - | 0/3 |  |
| h06 |  map | firecrawl, other-shell, firecrawl | `map` `search` firecrawl-map | 2/3 |  |
| h07 |  parse | none, none, none | - | 0/3 |  |
| h08 |  alexandria | other-shell, other-shell, other-shell | - | 0/3 |  |
| h09 |  scrape | native, native, native | - | 0/3 |  |
| h10 |  scrape | native, native, native | - | 0/3 |  |
| h11 |  search | none, native, native | - | 0/3 |  |
| h12 |  scrape | native, native, native | - | 0/3 |  |
| h13 |  search | native, native, native | - | 0/3 |  |
| h14 |  search | native, native, native | - | 0/3 |  |
| h15 |  scrape | native, native, native | - | 0/3 |  |
| h16 |  scrape | native, native, native | - | 0/3 |  |
| h17 |  map | none, none, none | - | 0/3 |  |
| h18 |  map | native, native, native | - | 0/3 |  |
| h19 |  crawl | native, native, native | - | 0/3 |  |
| h20 |  crawl | native, native, native | - | 0/3 |  |
| h21 |  agent | native, native, native | - | 0/3 |  |
| h22 |  agent | none, none, none | - | 0/3 |  |
| h23 |  agent | native, native, native | - | 0/3 |  |
| h24 |  interact | other-shell, native, native | - | 0/3 |  |
| h25 |  interact | firecrawl, firecrawl, firecrawl | `interact` `playwright` `scrape` firecrawl-interact | 2/3 |  |
| h26 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 3/3 |  |
| h27 |  parse | none, none, none | - | 0/3 |  |
| h28 |  parse | native, native, native | - | 0/3 |  |
| h29 |  download | firecrawl, other-shell, firecrawl | `download` firecrawl-download | 2/3 |  |
| h30 |  research | none, none, none | - | 0/3 |  |
| h31 |  developer | native, other-shell, other-shell | - | 0/3 |  |
| h32 |  developer | other-shell, other-shell, other-shell | - | 0/3 |  |
| h33 |  alexandria | other-shell, other-shell, other-shell | - | 0/3 |  |
| h34 |  scrape | native, native, none | - | 0/3 |  |
| h35 |  search | native, native, native | - | 0/3 |  |
| h36 |  scrape | native, native, native | - | 0/3 |  |

## Tool calls

Across 108 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `WebFetch` | 309 | 54 | 2.86 |
| `WebSearch` | 115 | 27 | 1.06 |
| `Bash` | 101 | 35 | 0.94 |
| `ToolSearch` | 72 | 70 | 0.67 |
| `Skill` | 9 | 9 | 0.08 |
| `Read` | 1 | 1 | 0.01 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-interact` | 5 | 5 | 0.05 |
| `firecrawl-download` | 2 | 2 | 0.02 |
| `firecrawl-map` | 2 | 2 | 0.02 |
| `firecrawl` | 0 | 0 | 0.00 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-crawl` | 0 | 0 | 0.00 |
| `firecrawl-developer-index` | 0 | 0 | 0.00 |
| `firecrawl-monitor` | 0 | 0 | 0.00 |
| `firecrawl-parse` | 0 | 0 | 0.00 |
| `firecrawl-research-index` | 0 | 0 | 0.00 |
| `firecrawl-scrape` | 0 | 0 | 0.00 |
| `firecrawl-search` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl interact` | 11 | 5 | 0.10 |
| `firecrawl scrape` | 6 | 5 | 0.06 |
| `firecrawl map` | 3 | 2 | 0.03 |
| `firecrawl download` | 2 | 2 | 0.02 |
| `firecrawl playwright` | 2 | 2 | 0.02 |
| `firecrawl search` | 1 | 1 | 0.01 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl crawl` | 0 | 0 | 0.00 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |


# heldout eval: r4-base

Skills `660ddb7` · model `claude-sonnet-5-5` · 2 trials · max 12 turns · Firecrawl key: True · 2.1.304 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 67% (16/24) |
| Runs that used Firecrawl | 88% (21/24) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/24) |
| Mean tool calls | 3.3 |
| Mean model cost (USD) | 0.076 |
| Mean duration (s) | 41 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| crawl | 2/4 | 2/4 | 4/4 | `scrape` x2, `crawl` x2 | - |
| agent | 1/4 | 1/4 | 4/4 | `scrape` x11, `search` x9, `agent` x2, `list` x1, `status` x1 | - |
| map | 3/4 | 3/4 | 3/4 | `map` x3, `scrape` x1 | `curl` x2 |
| parse | 0/2 | 0/2 | 0/2 | - | - |
| alexandria | 2/2 | 0/2 | 2/2 | `scrape` x2 | - |
| scrape | 6/6 | 6/6 | 6/6 | `scrape` x6 | - |
| search | 2/2 | 1/2 | 2/2 | `scrape` x1, `search` x1 | `curl` x1 |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| h01 |  crawl | firecrawl, firecrawl | `crawl` firecrawl-crawl | 2/2 |  |
| h02 |  crawl | firecrawl, firecrawl | `scrape` firecrawl-map | 0/2 |  |
| h03 |  agent | firecrawl, firecrawl | `agent` `list` `scrape` `search` `status` firecrawl firecrawl-agent | 1/2 |  |
| h04 |  agent | firecrawl, firecrawl | `scrape` `search` firecrawl-search | 0/2 |  |
| h05 |  map | none, firecrawl | `map` firecrawl-map | 1/2 |  |
| h06 |  map | firecrawl, firecrawl | `map` `scrape` firecrawl-map | 2/2 |  |
| h07 |  parse | none, none | - | 0/2 |  |
| h08 |  alexandria | firecrawl, firecrawl | `scrape` firecrawl-scrape | 2/2 |  |
| h09 |  scrape | firecrawl, firecrawl | `scrape` firecrawl-scrape | 2/2 |  |
| h10 |  scrape | firecrawl, firecrawl | `scrape` firecrawl-scrape | 2/2 |  |
| h11 |  search | firecrawl, firecrawl | `scrape` `search` firecrawl-scrape firecrawl-search | 2/2 |  |
| h12 |  scrape | firecrawl, firecrawl | `scrape` firecrawl-scrape | 2/2 |  |

## Tool calls

Across 24 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 59 | 23 | 2.46 |
| `Skill` | 21 | 21 | 0.88 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-scrape` | 9 | 9 | 0.38 |
| `firecrawl-map` | 5 | 5 | 0.21 |
| `firecrawl-search` | 3 | 3 | 0.12 |
| `firecrawl-crawl` | 2 | 2 | 0.08 |
| `firecrawl` | 1 | 1 | 0.04 |
| `firecrawl-agent` | 1 | 1 | 0.04 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-developer-index` | 0 | 0 | 0.00 |
| `firecrawl-download` | 0 | 0 | 0.00 |
| `firecrawl-interact` | 0 | 0 | 0.00 |
| `firecrawl-monitor` | 0 | 0 | 0.00 |
| `firecrawl-parse` | 0 | 0 | 0.00 |
| `firecrawl-research-index` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 23 | 15 | 0.96 |
| `firecrawl search` | 10 | 4 | 0.42 |
| `firecrawl map` | 3 | 3 | 0.12 |
| `firecrawl agent` | 2 | 1 | 0.08 |
| `firecrawl crawl` | 2 | 2 | 0.08 |
| `firecrawl list` | 1 | 1 | 0.04 |
| `firecrawl status` | 1 | 1 | 0.04 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl interact` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |


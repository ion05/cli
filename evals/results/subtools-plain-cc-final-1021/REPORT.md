# subtools-plain eval: cc-final-1021

Skills `660ddb7` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.306 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 81% (58/72) |
| Runs that used Firecrawl | 83% (60/72) |
| Runs that used built-in WebSearch/WebFetch | 7% (5/72) |
| Mean tool calls | 3.0 |
| Mean model cost (USD) | 0.053 |
| Mean duration (s) | 24 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| search | 6/6 | 6/6 | 6/6 | `search` x6, `scrape` x2 | `curl` x3 |
| scrape | 5/6 | 5/6 | 5/6 | `scrape` x7 | `WebFetch` x1 |
| map | 5/6 | 5/6 | 5/6 | `map` x6 | `WebFetch` x1 |
| crawl | 6/6 | 6/6 | 6/6 | `crawl` x6 | - |
| agent | 1/6 | 1/6 | 3/6 | `scrape` x8, `status` x2, `agent` x1 | - |
| interact | 5/6 | 5/6 | 5/6 | `interact` x10, `scrape` x5 | `curl` x2 |
| monitor | 6/6 | 6/6 | 6/6 | - | - |
| download | 6/6 | 6/6 | 6/6 | `download` x6, `scrape` x1 | - |
| parse | 3/6 | 3/6 | 3/6 | `parse` x3 | - |
| research | 4/6 | 4/6 | 4/6 | `research` x4 | `WebSearch` x2 |
| developer | 5/6 | 5/6 | 5/6 | `developer (API)` x9, `scrape` x9, `developer` x3 | `curl` x10, `gh` x2, `WebSearch` x1 |
| alexandria | 6/6 | 6/6 | 6/6 | `scrape` x8, `search` x6, `alexandria` x6, `find-tools` x3, `list` x3 | - |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| s01 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 3/3 |  |
| s02 |  search | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |  |
| s03 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| s04 |  scrape | firecrawl, firecrawl, native | `scrape` firecrawl-scrape | 2/3 |  |
| s05 |  map | firecrawl, firecrawl, firecrawl | `map` firecrawl-map | 3/3 |  |
| s06 |  map | firecrawl, firecrawl, native | `map` firecrawl-map | 2/3 |  |
| s07 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` firecrawl-crawl | 3/3 |  |
| s08 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` firecrawl-crawl | 3/3 |  |
| s09 |  agent | none, none, none | - | 0/3 | Agent case: unknown pages across many sites, dozens of records. Replaces the told-suite pricing prompt (one known page, where scrape is right). |
| s10 |  agent | firecrawl, firecrawl, firecrawl | `agent` `scrape` `status` firecrawl firecrawl-agent | 1/3 |  |
| s11 |  interact | firecrawl, firecrawl, other-shell | `interact` `scrape` firecrawl-interact | 2/3 | Login form on a public test site. Replaces the HN 'new' link prompt, which agents answered by fetching /newest directly. |
| s12 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 3/3 |  |
| s13 |  monitor | firecrawl, firecrawl, firecrawl | firecrawl-monitor | 3/3 |  |
| s14 |  monitor | firecrawl, firecrawl, firecrawl | firecrawl-monitor | 3/3 |  |
| s15 |  download | firecrawl, firecrawl, firecrawl | `download` `scrape` firecrawl-download | 3/3 |  |
| s16 |  download | firecrawl, firecrawl, firecrawl | `download` firecrawl-download | 3/3 |  |
| s17 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| s18 |  parse | none, none, none | - | 0/3 |  |
| s19 |  research | firecrawl, firecrawl, firecrawl | `research` firecrawl-research-index | 3/3 |  |
| s20 |  research | native, firecrawl, native | `research` firecrawl-research-index | 1/3 |  |
| s21 |  developer | firecrawl, other-shell, firecrawl | `scrape` firecrawl-developer-index | 2/3 |  |
| s22 |  developer | firecrawl, firecrawl, firecrawl | `developer` `scrape` firecrawl-developer-index | 3/3 |  |
| s23 |  alexandria | firecrawl, firecrawl, firecrawl | `alexandria` `find-tools` `scrape` `search` firecrawl-alexandria | 3/3 |  |
| s24 |  alexandria | firecrawl, firecrawl, firecrawl | `alexandria` `list` `scrape` `search` firecrawl-alexandria | 3/3 |  |

## Tool calls

Across 72 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 145 | 59 | 2.01 |
| `Skill` | 60 | 60 | 0.83 |
| `ToolSearch` | 5 | 5 | 0.07 |
| `WebSearch` | 3 | 3 | 0.04 |
| `WebFetch` | 2 | 2 | 0.03 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-alexandria` | 6 | 6 | 0.08 |
| `firecrawl-crawl` | 6 | 6 | 0.08 |
| `firecrawl-download` | 6 | 6 | 0.08 |
| `firecrawl-monitor` | 6 | 6 | 0.08 |
| `firecrawl-search` | 6 | 6 | 0.08 |
| `firecrawl-developer-index` | 5 | 5 | 0.07 |
| `firecrawl-interact` | 5 | 5 | 0.07 |
| `firecrawl-map` | 5 | 5 | 0.07 |
| `firecrawl-scrape` | 5 | 5 | 0.07 |
| `firecrawl-research-index` | 4 | 4 | 0.06 |
| `firecrawl-parse` | 3 | 3 | 0.04 |
| `firecrawl` | 2 | 2 | 0.03 |
| `firecrawl-agent` | 1 | 1 | 0.01 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 40 | 24 | 0.56 |
| `firecrawl search` | 12 | 12 | 0.17 |
| `firecrawl interact` | 10 | 5 | 0.14 |
| `firecrawl alexandria` | 6 | 6 | 0.08 |
| `firecrawl crawl` | 6 | 6 | 0.08 |
| `firecrawl download` | 6 | 6 | 0.08 |
| `firecrawl map` | 6 | 5 | 0.08 |
| `firecrawl research` | 4 | 4 | 0.06 |
| `firecrawl developer` | 3 | 2 | 0.04 |
| `firecrawl find-tools` | 3 | 3 | 0.04 |
| `firecrawl list` | 3 | 3 | 0.04 |
| `firecrawl parse` | 3 | 3 | 0.04 |
| `firecrawl status` | 2 | 2 | 0.03 |
| `firecrawl agent` | 1 | 1 | 0.01 |
| `firecrawl monitor` | 0 | 0 | 0.00 |

**Firecrawl API endpoints called directly (curl)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `developer` | 9 | 5 | 0.12 |


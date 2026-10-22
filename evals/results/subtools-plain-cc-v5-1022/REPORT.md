# subtools-plain eval: cc-v5-1022

Skills `0c820ab` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.306 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 88% (63/72) |
| Runs that used Firecrawl | 90% (65/72) |
| Runs that used built-in WebSearch/WebFetch | 7% (5/72) |
| Mean tool calls | 3.4 |
| Mean model cost (USD) | 0.057 |
| Mean duration (s) | 28 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| search | 6/6 | 6/6 | 6/6 | `search` x6, `scrape` x4 | `curl` x2 |
| scrape | 6/6 | 6/6 | 6/6 | `scrape` x8 | - |
| map | 4/6 | 4/6 | 4/6 | `map` x4 | `WebFetch` x2 |
| crawl | 6/6 | 6/6 | 6/6 | `crawl` x6 | - |
| agent | 2/6 | 3/6 | 4/6 | `scrape` x3, `search` x2, `agent` x2, `list` x1 | `curl` x4 |
| interact | 6/6 | 6/6 | 6/6 | `interact` x16, `scrape` x8 | - |
| monitor | 6/6 | 6/6 | 6/6 | - | - |
| download | 6/6 | 6/6 | 6/6 | `download` x11, `map` x6, `scrape` x6 | - |
| parse | 6/6 | 6/6 | 6/6 | `parse` x6 | - |
| research | 5/6 | 5/6 | 5/6 | `research` x5 | `WebSearch` x1 |
| developer | 4/6 | 4/6 | 4/6 | `scrape` x8, `developer (API)` x7, `developer` x2, `gh` x1 | `curl` x12, `WebSearch` x2 |
| alexandria | 6/6 | 6/6 | 6/6 | `scrape` x9, `search` x6, `alexandria` x6, `find-tools` x3, `list` x3 | - |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| s01 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 3/3 |  |
| s02 |  search | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |  |
| s03 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| s04 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| s05 |  map | firecrawl, firecrawl, firecrawl | `map` firecrawl-map | 3/3 |  |
| s06 |  map | native, firecrawl, native | `map` firecrawl-map | 1/3 |  |
| s07 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` firecrawl-crawl | 3/3 |  |
| s08 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` firecrawl-crawl | 3/3 |  |
| s09 |  agent | other-shell, firecrawl, none | `scrape` | 0/3 | Agent case: unknown pages across many sites, dozens of records. Replaces the told-suite pricing prompt (one known page, where scrape is right). |
| s10 |  agent | firecrawl, firecrawl, firecrawl | `agent` `list` `scrape` `search` firecrawl-agent | 2/3 |  |
| s11 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 3/3 | Login form on a public test site. Replaces the HN 'new' link prompt, which agents answered by fetching /newest directly. |
| s12 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 3/3 |  |
| s13 |  monitor | firecrawl, firecrawl, firecrawl | firecrawl-monitor | 3/3 |  |
| s14 |  monitor | firecrawl, firecrawl, firecrawl | firecrawl-monitor | 3/3 |  |
| s15 |  download | firecrawl, firecrawl, firecrawl | `download` `map` `scrape` firecrawl-download | 3/3 |  |
| s16 |  download | firecrawl, firecrawl, firecrawl | `download` `map` `scrape` firecrawl-download | 3/3 |  |
| s17 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| s18 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| s19 |  research | firecrawl, firecrawl, firecrawl | `research` firecrawl-research-index | 3/3 |  |
| s20 |  research | firecrawl, native, firecrawl | `research` firecrawl-research-index | 2/3 |  |
| s21 |  developer | other-shell, other-shell, firecrawl | `gh` `scrape` firecrawl-developer-index | 1/3 |  |
| s22 |  developer | firecrawl, firecrawl, firecrawl | `developer` `scrape` firecrawl-developer-index | 3/3 |  |
| s23 |  alexandria | firecrawl, firecrawl, firecrawl | `alexandria` `find-tools` `scrape` `search` firecrawl-alexandria | 3/3 |  |
| s24 |  alexandria | firecrawl, firecrawl, firecrawl | `alexandria` `list` `scrape` `search` firecrawl-alexandria | 3/3 |  |

## Tool calls

Across 72 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 168 | 62 | 2.33 |
| `Skill` | 64 | 64 | 0.89 |
| `ToolSearch` | 5 | 5 | 0.07 |
| `WebSearch` | 3 | 3 | 0.04 |
| `WebFetch` | 2 | 2 | 0.03 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-alexandria` | 6 | 6 | 0.08 |
| `firecrawl-crawl` | 6 | 6 | 0.08 |
| `firecrawl-download` | 6 | 6 | 0.08 |
| `firecrawl-interact` | 6 | 6 | 0.08 |
| `firecrawl-monitor` | 6 | 6 | 0.08 |
| `firecrawl-parse` | 6 | 6 | 0.08 |
| `firecrawl-scrape` | 6 | 6 | 0.08 |
| `firecrawl-search` | 6 | 6 | 0.08 |
| `firecrawl-research-index` | 5 | 5 | 0.07 |
| `firecrawl-developer-index` | 4 | 4 | 0.06 |
| `firecrawl-map` | 4 | 4 | 0.06 |
| `firecrawl-agent` | 3 | 3 | 0.04 |
| `firecrawl` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 46 | 31 | 0.64 |
| `firecrawl interact` | 16 | 6 | 0.22 |
| `firecrawl search` | 14 | 14 | 0.19 |
| `firecrawl download` | 11 | 6 | 0.15 |
| `firecrawl map` | 10 | 9 | 0.14 |
| `firecrawl alexandria` | 6 | 6 | 0.08 |
| `firecrawl crawl` | 6 | 6 | 0.08 |
| `firecrawl parse` | 6 | 6 | 0.08 |
| `firecrawl research` | 5 | 5 | 0.07 |
| `firecrawl list` | 4 | 4 | 0.06 |
| `firecrawl find-tools` | 3 | 3 | 0.04 |
| `firecrawl agent` | 2 | 2 | 0.03 |
| `firecrawl developer` | 2 | 2 | 0.03 |
| `firecrawl gh` | 1 | 1 | 0.01 |
| `firecrawl monitor` | 0 | 0 | 0.00 |

**Firecrawl API endpoints called directly (curl)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `developer` | 7 | 4 | 0.10 |


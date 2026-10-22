# subtools-plain eval: cc-v4-1021

Skills `e676c94` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.306 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 82% (59/72) |
| Runs that used Firecrawl | 85% (61/72) |
| Runs that used built-in WebSearch/WebFetch | 8% (6/72) |
| Mean tool calls | 3.3 |
| Mean model cost (USD) | 0.056 |
| Mean duration (s) | 25 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| search | 4/6 | 4/6 | 4/6 | `search` x4, `scrape` x2 | `curl` x5, `WebFetch` x3, `WebSearch` x2, `gh` x1 |
| scrape | 6/6 | 6/6 | 6/6 | `scrape` x7 | - |
| map | 3/6 | 3/6 | 3/6 | `map` x3 | `WebFetch` x3 |
| crawl | 6/6 | 6/6 | 6/6 | `crawl` x6 | - |
| agent | 1/6 | 1/6 | 3/6 | `scrape` x4, `list` x3, `search` x2, `agent` x2, `status` x1, `find-tools` x1 | - |
| interact | 5/6 | 5/6 | 5/6 | `interact` x10, `scrape` x5 | `curl` x5 |
| monitor | 6/6 | 6/6 | 6/6 | - | - |
| download | 6/6 | 6/6 | 6/6 | `download` x9 | - |
| parse | 6/6 | 6/6 | 6/6 | `parse` x6 | - |
| research | 5/6 | 5/6 | 5/6 | `research` x5 | - |
| developer | 5/6 | 5/6 | 5/6 | `scrape` x10, `developer (API)` x10, `gh` x2, `developer` x2 | `curl` x9, `WebSearch` x1 |
| alexandria | 6/6 | 6/6 | 6/6 | `scrape` x9, `search` x6, `alexandria` x6, `find-tools` x3, `list` x3 | - |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| s01 |  search | firecrawl, firecrawl, native | `scrape` `search` firecrawl-search | 2/3 |  |
| s02 |  search | native, firecrawl, firecrawl | `search` firecrawl-search | 2/3 |  |
| s03 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| s04 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| s05 |  map | firecrawl, firecrawl, firecrawl | `map` firecrawl-map | 3/3 |  |
| s06 |  map | native, native, native | - | 0/3 |  |
| s07 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` firecrawl-crawl | 3/3 |  |
| s08 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` firecrawl-crawl | 3/3 |  |
| s09 |  agent | none, none, none | - | 0/3 | Agent case: unknown pages across many sites, dozens of records. Replaces the told-suite pricing prompt (one known page, where scrape is right). |
| s10 |  agent | firecrawl, firecrawl, firecrawl | `agent` `find-tools` `list` `scrape` `search` `status` firecrawl firecrawl-agent firecrawl-search | 1/3 |  |
| s11 |  interact | firecrawl, firecrawl, other-shell | `interact` `scrape` firecrawl-interact | 2/3 | Login form on a public test site. Replaces the HN 'new' link prompt, which agents answered by fetching /newest directly. |
| s12 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 3/3 |  |
| s13 |  monitor | firecrawl, firecrawl, firecrawl | firecrawl-monitor | 3/3 |  |
| s14 |  monitor | firecrawl, firecrawl, firecrawl | firecrawl-monitor | 3/3 |  |
| s15 |  download | firecrawl, firecrawl, firecrawl | `download` firecrawl-download | 3/3 |  |
| s16 |  download | firecrawl, firecrawl, firecrawl | `download` firecrawl-download | 3/3 |  |
| s17 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| s18 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| s19 |  research | firecrawl, firecrawl, firecrawl | `research` firecrawl-research-index | 3/3 |  |
| s20 |  research | firecrawl, firecrawl, none | `research` firecrawl-research-index | 2/3 |  |
| s21 |  developer | firecrawl, other-shell, firecrawl | `gh` `scrape` firecrawl-developer-index | 2/3 |  |
| s22 |  developer | firecrawl, firecrawl, firecrawl | `developer` `scrape` firecrawl-developer-index | 3/3 |  |
| s23 |  alexandria | firecrawl, firecrawl, firecrawl | `alexandria` `find-tools` `scrape` `search` firecrawl-alexandria | 3/3 |  |
| s24 |  alexandria | firecrawl, firecrawl, firecrawl | `alexandria` `list` `scrape` `search` firecrawl-alexandria | 3/3 |  |

## Tool calls

Across 72 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 153 | 58 | 2.12 |
| `Skill` | 61 | 61 | 0.85 |
| `ToolSearch` | 7 | 7 | 0.10 |
| `WebFetch` | 6 | 4 | 0.08 |
| `Read` | 4 | 2 | 0.06 |
| `WebSearch` | 3 | 3 | 0.04 |
| `Monitor` | 2 | 1 | 0.03 |
| `ReadNotifications` | 2 | 1 | 0.03 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-alexandria` | 6 | 6 | 0.08 |
| `firecrawl-crawl` | 6 | 6 | 0.08 |
| `firecrawl-download` | 6 | 6 | 0.08 |
| `firecrawl-monitor` | 6 | 6 | 0.08 |
| `firecrawl-parse` | 6 | 6 | 0.08 |
| `firecrawl-scrape` | 6 | 6 | 0.08 |
| `firecrawl-developer-index` | 5 | 5 | 0.07 |
| `firecrawl-interact` | 5 | 5 | 0.07 |
| `firecrawl-research-index` | 5 | 5 | 0.07 |
| `firecrawl-search` | 5 | 5 | 0.07 |
| `firecrawl-map` | 3 | 3 | 0.04 |
| `firecrawl` | 1 | 1 | 0.01 |
| `firecrawl-agent` | 1 | 1 | 0.01 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 37 | 25 | 0.51 |
| `firecrawl search` | 12 | 12 | 0.17 |
| `firecrawl interact` | 10 | 5 | 0.14 |
| `firecrawl download` | 9 | 6 | 0.12 |
| `firecrawl alexandria` | 6 | 6 | 0.08 |
| `firecrawl crawl` | 6 | 6 | 0.08 |
| `firecrawl list` | 6 | 5 | 0.08 |
| `firecrawl parse` | 6 | 6 | 0.08 |
| `firecrawl research` | 5 | 5 | 0.07 |
| `firecrawl find-tools` | 4 | 4 | 0.06 |
| `firecrawl map` | 3 | 3 | 0.04 |
| `firecrawl agent` | 2 | 1 | 0.03 |
| `firecrawl developer` | 2 | 2 | 0.03 |
| `firecrawl gh` | 2 | 2 | 0.03 |
| `firecrawl status` | 1 | 1 | 0.01 |
| `firecrawl monitor` | 0 | 0 | 0.00 |

**Firecrawl API endpoints called directly (curl)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `developer` | 10 | 5 | 0.14 |


# subtools-plain eval: cc-original-1021

Skills `22358f2` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.306 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 36% (26/72) |
| Runs that used Firecrawl | 40% (29/72) |
| Runs that used built-in WebSearch/WebFetch | 40% (29/72) |
| Mean tool calls | 3.3 |
| Mean model cost (USD) | 0.056 |
| Mean duration (s) | 18 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| search | 0/6 | 0/6 | 0/6 | - | `WebFetch` x6, `WebSearch` x4, `gh` x3, `curl` x3 |
| scrape | 0/6 | 0/6 | 0/6 | - | `WebFetch` x6 |
| map | 3/6 | 3/6 | 3/6 | `map` x3 | `WebFetch` x3 |
| crawl | 3/6 | 2/6 | 6/6 | `scrape` x6, `crawl` x5, `status` x2, `map` x1 | - |
| agent | 0/6 | 0/6 | 0/6 | - | `WebFetch` x8, `curl` x5, `WebSearch` x3 |
| interact | 3/6 | 3/6 | 3/6 | `interact` x6, `scrape` x3 | `curl` x6 |
| monitor | 4/6 | 4/6 | 4/6 | - | - |
| download | 5/6 | 5/6 | 5/6 | `download` x7 | `curl` x1, `wget` x1 |
| parse | 3/6 | 3/6 | 3/6 | `parse` x3 | - |
| research | 1/6 | 1/6 | 1/6 | `research` x1 | `WebSearch` x6 |
| developer | 0/6 | 0/6 | 0/6 | - | `curl` x17, `WebFetch` x10, `WebSearch` x8 |
| alexandria | 4/6 | 4/6 | 4/6 | `list` x10, `find-tools` x4, `alexandria` x4, `scrape` x3, `search` x1 | `curl` x3 |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| s01 |  search | native, native, native | - | 0/3 |  |
| s02 |  search | native, native, native | - | 0/3 |  |
| s03 |  scrape | native, native, native | - | 0/3 |  |
| s04 |  scrape | native, native, native | - | 0/3 |  |
| s05 |  map | firecrawl, firecrawl, firecrawl | `map` firecrawl-map | 3/3 |  |
| s06 |  map | native, native, native | - | 0/3 |  |
| s07 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` `status` firecrawl firecrawl-crawl | 3/3 |  |
| s08 |  crawl | firecrawl, firecrawl, firecrawl | `map` `scrape` `status` firecrawl firecrawl-scrape | 0/3 |  |
| s09 |  agent | none, other-shell, none | - | 0/3 | Agent case: unknown pages across many sites, dozens of records. Replaces the told-suite pricing prompt (one known page, where scrape is right). |
| s10 |  agent | native, native, native | - | 0/3 |  |
| s11 |  interact | other-shell, other-shell, other-shell | - | 0/3 | Login form on a public test site. Replaces the HN 'new' link prompt, which agents answered by fetching /newest directly. |
| s12 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 3/3 |  |
| s13 |  monitor | firecrawl, firecrawl, firecrawl | firecrawl-monitor | 3/3 |  |
| s14 |  monitor | none, firecrawl, none | firecrawl-monitor | 1/3 |  |
| s15 |  download | firecrawl, firecrawl, firecrawl | `download` firecrawl-download | 3/3 |  |
| s16 |  download | firecrawl, firecrawl, other-shell | `download` firecrawl-download | 2/3 |  |
| s17 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| s18 |  parse | none, none, none | - | 0/3 |  |
| s19 |  research | native, native, firecrawl | `research` firecrawl-research-index | 1/3 |  |
| s20 |  research | native, native, native | - | 0/3 |  |
| s21 |  developer | other-shell, other-shell, other-shell | - | 0/3 |  |
| s22 |  developer | native, native, other-shell | - | 0/3 |  |
| s23 |  alexandria | firecrawl, other-shell, other-shell | `alexandria` `find-tools` `search` firecrawl-alexandria firecrawl-search | 1/3 |  |
| s24 |  alexandria | firecrawl, firecrawl, firecrawl | `alexandria` `find-tools` `list` `scrape` firecrawl-alexandria firecrawl-search | 3/3 |  |

## Tool calls

Across 72 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 115 | 46 | 1.60 |
| `Skill` | 33 | 29 | 0.46 |
| `WebFetch` | 33 | 17 | 0.46 |
| `ToolSearch` | 32 | 32 | 0.44 |
| `WebSearch` | 21 | 18 | 0.29 |
| `CronCreate` | 2 | 2 | 0.03 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-download` | 5 | 5 | 0.07 |
| `firecrawl-alexandria` | 4 | 4 | 0.06 |
| `firecrawl-monitor` | 4 | 4 | 0.06 |
| `firecrawl-search` | 4 | 4 | 0.06 |
| `firecrawl-interact` | 3 | 3 | 0.04 |
| `firecrawl-map` | 3 | 3 | 0.04 |
| `firecrawl-parse` | 3 | 3 | 0.04 |
| `firecrawl` | 2 | 2 | 0.03 |
| `firecrawl-crawl` | 2 | 2 | 0.03 |
| `firecrawl-scrape` | 2 | 2 | 0.03 |
| `firecrawl-research-index` | 1 | 1 | 0.01 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-developer-index` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 12 | 9 | 0.17 |
| `firecrawl list` | 10 | 3 | 0.14 |
| `firecrawl download` | 7 | 5 | 0.10 |
| `firecrawl interact` | 6 | 3 | 0.08 |
| `firecrawl crawl` | 5 | 3 | 0.07 |
| `firecrawl alexandria` | 4 | 4 | 0.06 |
| `firecrawl find-tools` | 4 | 4 | 0.06 |
| `firecrawl map` | 4 | 4 | 0.06 |
| `firecrawl parse` | 3 | 3 | 0.04 |
| `firecrawl status` | 2 | 2 | 0.03 |
| `firecrawl research` | 1 | 1 | 0.01 |
| `firecrawl search` | 1 | 1 | 0.01 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |


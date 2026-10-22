# subtools-plain eval: cc-native-1021

Skills `NONE` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.306 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 0% (0/72) |
| Runs that used Firecrawl | 0% (0/72) |
| Runs that used built-in WebSearch/WebFetch | 62% (45/72) |
| Mean tool calls | 3.7 |
| Mean model cost (USD) | 0.048 |
| Mean duration (s) | 18 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| search | 0/6 | 0/6 | 0/6 | - | `WebFetch` x9, `WebSearch` x6, `gh` x3, `curl` x1 |
| scrape | 0/6 | 0/6 | 0/6 | - | `WebFetch` x6 |
| map | 0/6 | 0/6 | 0/6 | - | `WebFetch` x7, `WebSearch` x3 |
| crawl | 0/6 | 0/6 | 0/6 | - | `WebFetch` x62 |
| agent | 0/6 | 0/6 | 0/6 | - | `WebFetch` x14, `WebSearch` x3 |
| interact | 0/6 | 0/6 | 0/6 | - | `curl` x6, `WebFetch` x6 |
| monitor | 0/6 | 0/6 | 0/6 | - | `curl` x5 |
| download | 0/6 | 0/6 | 0/6 | - | `curl` x9, `WebFetch` x3, `wget` x2 |
| parse | 0/6 | 0/6 | 0/6 | - | - |
| research | 0/6 | 0/6 | 0/6 | - | `WebSearch` x6 |
| developer | 0/6 | 0/6 | 0/6 | - | `curl` x12, `WebSearch` x9, `WebFetch` x8 |
| alexandria | 0/6 | 0/6 | 0/6 | - | `curl` x9 |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| s01 |  search | native, native, native | - | 0/3 |  |
| s02 |  search | native, native, native | - | 0/3 |  |
| s03 |  scrape | native, native, native | - | 0/3 |  |
| s04 |  scrape | native, native, native | - | 0/3 |  |
| s05 |  map | native, native, native | - | 0/3 |  |
| s06 |  map | native, native, native | - | 0/3 |  |
| s07 |  crawl | native, native, native | - | 0/3 |  |
| s08 |  crawl | native, native, native | - | 0/3 |  |
| s09 |  agent | none, none, none | - | 0/3 | Agent case: unknown pages across many sites, dozens of records. Replaces the told-suite pricing prompt (one known page, where scrape is right). |
| s10 |  agent | native, native, native | - | 0/3 |  |
| s11 |  interact | other-shell, other-shell, other-shell | - | 0/3 | Login form on a public test site. Replaces the HN 'new' link prompt, which agents answered by fetching /newest directly. |
| s12 |  interact | native, native, native | - | 0/3 |  |
| s13 |  monitor | other-shell, other-shell, other-shell | - | 0/3 |  |
| s14 |  monitor | none, other-shell, other-shell | - | 0/3 |  |
| s15 |  download | native, native, native | - | 0/3 |  |
| s16 |  download | other-shell, other-shell, other-shell | - | 0/3 |  |
| s17 |  parse | none, none, none | - | 0/3 |  |
| s18 |  parse | none, none, none | - | 0/3 |  |
| s19 |  research | native, native, native | - | 0/3 |  |
| s20 |  research | native, native, native | - | 0/3 |  |
| s21 |  developer | other-shell, other-shell, other-shell | - | 0/3 |  |
| s22 |  developer | native, native, other-shell | - | 0/3 |  |
| s23 |  alexandria | other-shell, other-shell, other-shell | - | 0/3 |  |
| s24 |  alexandria | other-shell, other-shell, other-shell | - | 0/3 |  |

## Tool calls

Across 72 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `WebFetch` | 115 | 32 | 1.60 |
| `Bash` | 64 | 34 | 0.89 |
| `ToolSearch` | 52 | 52 | 0.72 |
| `WebSearch` | 27 | 24 | 0.38 |
| `CronCreate` | 6 | 6 | 0.08 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 0 | 0 | 0.00 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-crawl` | 0 | 0 | 0.00 |
| `firecrawl-developer-index` | 0 | 0 | 0.00 |
| `firecrawl-download` | 0 | 0 | 0.00 |
| `firecrawl-interact` | 0 | 0 | 0.00 |
| `firecrawl-map` | 0 | 0 | 0.00 |
| `firecrawl-monitor` | 0 | 0 | 0.00 |
| `firecrawl-parse` | 0 | 0 | 0.00 |
| `firecrawl-research-index` | 0 | 0 | 0.00 |
| `firecrawl-scrape` | 0 | 0 | 0.00 |
| `firecrawl-search` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl crawl` | 0 | 0 | 0.00 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl interact` | 0 | 0 | 0.00 |
| `firecrawl map` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |
| `firecrawl scrape` | 0 | 0 | 0.00 |
| `firecrawl search` | 0 | 0 | 0.00 |


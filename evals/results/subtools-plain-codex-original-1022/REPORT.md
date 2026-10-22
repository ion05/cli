# subtools-plain eval: codex-original-1022

Skills `22358f2` · model `(codex default)` · 3 trials · max n/a turns · Firecrawl key: True · codex-cli 0.163.0

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 76% (55/72) |
| Runs that used Firecrawl | 94% (68/72) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/72) |
| Mean tool calls | 7.9 |
| Mean model cost (USD) | 0.053 |
| Mean duration (s) | 37 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| scrape | 6/6 | 6/6 | 6/6 | `scrape` x6 | - |
| search | 3/6 | 3/6 | 6/6 | `scrape` x5, `search` x3, `search-feedback` x3, `status` x2 | - |
| map | 6/6 | 6/6 | 6/6 | `map` x6 | - |
| crawl | 5/6 | 6/6 | 6/6 | `scrape` x23, `crawl` x9, `status` x4 | - |
| interact | 6/6 | 6/6 | 6/6 | `interact` x22, `scrape` x6, `status` x3 | - |
| agent | 0/6 | 0/6 | 6/6 | `search` x93, `scrape` x35, `status` x6, `list` x4, `search-feedback` x3, `capacitive` x1 | - |
| monitor | 6/6 | 6/6 | 6/6 | `monitor` x10 | - |
| download | 6/6 | 6/6 | 6/6 | `download` x8 | - |
| parse | 6/6 | 6/6 | 6/6 | `parse` x6 | - |
| research | 6/6 | 6/6 | 6/6 | `research` x16 | - |
| developer | 2/6 | 3/6 | 4/6 | `scrape` x12, `search` x7, `developer` x6, `search-feedback` x2, `developer (API)` x2 | - |
| alexandria | 3/6 | 0/6 | 4/6 | `search` x4, `find-tools` x2, `scrape` x2, `search-feedback` x2, `list` x1 | - |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| s01 |  search | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape | 0/3 |  |
| s02 |  search | firecrawl, firecrawl, firecrawl | `search-feedback` `search` `status` firecrawl firecrawl-search | 3/3 |  |
| s03 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |  |
| s04 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |  |
| s05 |  map | firecrawl, firecrawl, firecrawl | `map` firecrawl-map | 3/3 |  |
| s06 |  map | firecrawl, firecrawl, firecrawl | `map` firecrawl firecrawl-map | 3/3 |  |
| s07 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` `status` firecrawl firecrawl-crawl | 3/3 |  |
| s08 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` `scrape` `status` firecrawl firecrawl-crawl firecrawl-scrape | 2/3 |  |
| s09 |  agent | firecrawl, firecrawl, firecrawl | `scrape` `search` `status` firecrawl firecrawl-scrape firecrawl-search | 0/3 | Agent case: unknown pages across many sites, dozens of records. Replaces the told-suite pricing prompt (one known page, where scrape is right). |
| s10 |  agent | firecrawl, firecrawl, firecrawl | `capacitive` `list` `scrape` `search-feedback` `search` `status` firecrawl firecrawl-scrape firecrawl-search | 0/3 |  |
| s11 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` `status` firecrawl firecrawl-interact | 3/3 | Login form on a public test site. Replaces the HN 'new' link prompt, which agents answered by fetching /newest directly. |
| s12 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` `status` firecrawl firecrawl-interact | 3/3 |  |
| s13 |  monitor | firecrawl, firecrawl, firecrawl | `monitor` firecrawl-monitor | 3/3 |  |
| s14 |  monitor | firecrawl, firecrawl, firecrawl | `monitor` firecrawl-monitor | 3/3 |  |
| s15 |  download | firecrawl, firecrawl, firecrawl | `download` firecrawl-download | 3/3 |  |
| s16 |  download | firecrawl, firecrawl, firecrawl | `download` firecrawl-download | 3/3 |  |
| s17 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| s18 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| s19 |  research | firecrawl, firecrawl, firecrawl | `research` firecrawl-research-index | 3/3 |  |
| s20 |  research | firecrawl, firecrawl, firecrawl | `research` firecrawl-research-index | 3/3 |  |
| s21 |  developer | firecrawl, firecrawl, none | `scrape` `search-feedback` `search` firecrawl-developer-index firecrawl-scrape firecrawl-search | 0/3 |  |
| s22 |  developer | firecrawl, firecrawl, none | `developer` `scrape` `search-feedback` `search` firecrawl firecrawl-developer-index firecrawl-search | 2/3 |  |
| s23 |  alexandria | firecrawl, firecrawl, none | `find-tools` `search` firecrawl firecrawl-scrape firecrawl-search | 2/3 |  |
| s24 |  alexandria | firecrawl, firecrawl, none | `list` `scrape` `search-feedback` `search` firecrawl firecrawl-scrape firecrawl-search | 1/3 |  |

## Tool calls

Across 72 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `shell` | 566 | 68 | 7.86 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 33 | 33 | 0.46 |
| `firecrawl-scrape` | 23 | 23 | 0.32 |
| `firecrawl-search` | 16 | 16 | 0.22 |
| `firecrawl-crawl` | 6 | 6 | 0.08 |
| `firecrawl-download` | 6 | 6 | 0.08 |
| `firecrawl-interact` | 6 | 6 | 0.08 |
| `firecrawl-map` | 6 | 6 | 0.08 |
| `firecrawl-monitor` | 6 | 6 | 0.08 |
| `firecrawl-parse` | 6 | 6 | 0.08 |
| `firecrawl-research-index` | 6 | 6 | 0.08 |
| `firecrawl-developer-index` | 3 | 3 | 0.04 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl search` | 107 | 16 | 1.49 |
| `firecrawl scrape` | 89 | 28 | 1.24 |
| `firecrawl interact` | 22 | 6 | 0.31 |
| `firecrawl research` | 16 | 6 | 0.22 |
| `firecrawl status` | 15 | 15 | 0.21 |
| `firecrawl monitor` | 10 | 6 | 0.14 |
| `firecrawl search-feedback` | 10 | 10 | 0.14 |
| `firecrawl crawl` | 9 | 5 | 0.12 |
| `firecrawl download` | 8 | 6 | 0.11 |
| `firecrawl developer` | 6 | 2 | 0.08 |
| `firecrawl map` | 6 | 6 | 0.08 |
| `firecrawl parse` | 6 | 6 | 0.08 |
| `firecrawl list` | 5 | 3 | 0.07 |
| `firecrawl find-tools` | 2 | 2 | 0.03 |
| `firecrawl capacitive` | 1 | 1 | 0.01 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |

**Firecrawl API endpoints called directly (curl)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `developer` | 2 | 1 | 0.03 |


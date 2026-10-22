# subtools-plain eval: codex-final-1022

Skills `660ddb7` · model `(codex default)` · 3 trials · max n/a turns · Firecrawl key: True · codex-cli 0.163.0

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 90% (65/72) |
| Runs that used Firecrawl | 100% (72/72) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/72) |
| Mean tool calls | 7.7 |
| Mean model cost (USD) | 0.048 |
| Mean duration (s) | 37 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| scrape | 6/6 | 6/6 | 6/6 | `scrape` x6 | - |
| search | 5/6 | 5/6 | 6/6 | `search` x5, `search-feedback` x5, `scrape` x1 | - |
| map | 6/6 | 6/6 | 6/6 | `map` x6, `scrape` x3 | - |
| crawl | 5/6 | 5/6 | 6/6 | `crawl` x7, `download` x1 | - |
| interact | 6/6 | 6/6 | 6/6 | `interact` x23, `scrape` x6 | - |
| agent | 1/6 | 4/6 | 6/6 | `scrape` x57, `search` x53, `agent` x6, `list` x5, `status` x2, `search-feedback` x1 | - |
| monitor | 6/6 | 6/6 | 6/6 | `monitor` x11 | - |
| download | 6/6 | 6/6 | 6/6 | `download` x7, `status` x1 | - |
| parse | 6/6 | 6/6 | 6/6 | `parse` x6 | - |
| research | 6/6 | 6/6 | 6/6 | `research` x19 | - |
| developer | 6/6 | 6/6 | 6/6 | `scrape` x36, `developer` x16 | - |
| alexandria | 6/6 | 6/6 | 6/6 | `scrape` x21, `search` x6, `alexandria` x5, `list` x5, `find-tools` x3 | - |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| s01 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` firecrawl firecrawl-scrape firecrawl-search | 2/3 |  |
| s02 |  search | firecrawl, firecrawl, firecrawl | `search-feedback` `search` firecrawl-search | 3/3 |  |
| s03 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |  |
| s04 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| s05 |  map | firecrawl, firecrawl, firecrawl | `map` firecrawl-map | 3/3 |  |
| s06 |  map | firecrawl, firecrawl, firecrawl | `map` `scrape` firecrawl-map firecrawl-scrape | 3/3 |  |
| s07 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` firecrawl-crawl | 3/3 |  |
| s08 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` `download` firecrawl-crawl firecrawl-download | 2/3 |  |
| s09 |  agent | firecrawl, firecrawl, firecrawl | `agent` `scrape` `search-feedback` `search` firecrawl firecrawl-agent firecrawl-scrape firecrawl-search | 1/3 | Agent case: unknown pages across many sites, dozens of records. Replaces the told-suite pricing prompt (one known page, where scrape is right). |
| s10 |  agent | firecrawl, firecrawl, firecrawl | `list` `scrape` `search` `status` firecrawl firecrawl-agent | 0/3 |  |
| s11 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl firecrawl-interact | 3/3 | Login form on a public test site. Replaces the HN 'new' link prompt, which agents answered by fetching /newest directly. |
| s12 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl firecrawl-interact | 3/3 |  |
| s13 |  monitor | firecrawl, firecrawl, firecrawl | `monitor` firecrawl-monitor | 3/3 |  |
| s14 |  monitor | firecrawl, firecrawl, firecrawl | `monitor` firecrawl-monitor | 3/3 |  |
| s15 |  download | firecrawl, firecrawl, firecrawl | `download` `status` firecrawl firecrawl-download | 3/3 |  |
| s16 |  download | firecrawl, firecrawl, firecrawl | `download` firecrawl-download | 3/3 |  |
| s17 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| s18 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| s19 |  research | firecrawl, firecrawl, firecrawl | `research` firecrawl-research-index | 3/3 |  |
| s20 |  research | firecrawl, firecrawl, firecrawl | `research` firecrawl-research-index | 3/3 |  |
| s21 |  developer | firecrawl, firecrawl, firecrawl | `developer` `scrape` firecrawl-developer-index firecrawl-scrape | 3/3 |  |
| s22 |  developer | firecrawl, firecrawl, firecrawl | `developer` `scrape` firecrawl-developer-index firecrawl-scrape | 3/3 |  |
| s23 |  alexandria | firecrawl, firecrawl, firecrawl | `alexandria` `find-tools` `scrape` `search` firecrawl-alexandria firecrawl-scrape firecrawl-search | 3/3 |  |
| s24 |  alexandria | firecrawl, firecrawl, firecrawl | `alexandria` `list` `scrape` `search` firecrawl-alexandria firecrawl-scrape | 3/3 |  |

## Tool calls

Across 72 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `shell` | 557 | 72 | 7.74 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-scrape` | 22 | 22 | 0.31 |
| `firecrawl` | 12 | 12 | 0.17 |
| `firecrawl-search` | 9 | 9 | 0.12 |
| `firecrawl-download` | 7 | 7 | 0.10 |
| `firecrawl-alexandria` | 6 | 6 | 0.08 |
| `firecrawl-developer-index` | 6 | 6 | 0.08 |
| `firecrawl-interact` | 6 | 6 | 0.08 |
| `firecrawl-map` | 6 | 6 | 0.08 |
| `firecrawl-monitor` | 6 | 6 | 0.08 |
| `firecrawl-parse` | 6 | 6 | 0.08 |
| `firecrawl-research-index` | 6 | 6 | 0.08 |
| `firecrawl-crawl` | 5 | 5 | 0.07 |
| `firecrawl-agent` | 4 | 4 | 0.06 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 130 | 33 | 1.81 |
| `firecrawl search` | 64 | 17 | 0.89 |
| `firecrawl interact` | 23 | 6 | 0.32 |
| `firecrawl research` | 19 | 6 | 0.26 |
| `firecrawl developer` | 16 | 6 | 0.22 |
| `firecrawl monitor` | 11 | 6 | 0.15 |
| `firecrawl list` | 10 | 6 | 0.14 |
| `firecrawl download` | 8 | 7 | 0.11 |
| `firecrawl crawl` | 7 | 5 | 0.10 |
| `firecrawl agent` | 6 | 1 | 0.08 |
| `firecrawl map` | 6 | 6 | 0.08 |
| `firecrawl parse` | 6 | 6 | 0.08 |
| `firecrawl search-feedback` | 6 | 6 | 0.08 |
| `firecrawl alexandria` | 5 | 5 | 0.07 |
| `firecrawl find-tools` | 3 | 3 | 0.04 |
| `firecrawl status` | 3 | 3 | 0.04 |


# subtools-plain eval: desc-v1

Skills `3db3d63` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 67% (48/72) |
| Runs that used Firecrawl | 78% (56/72) |
| Runs that used built-in WebSearch/WebFetch | 10% (7/72) |
| Mean tool calls | 3.2 |
| Mean model cost (USD) | 0.062 |
| Mean duration (s) | 15 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| search | 5/6 | 5/6 | 5/6 | `search` x5, `scrape` x2 | `curl` x4 |
| scrape | 5/6 | 5/6 | 5/6 | `scrape` x6 | `curl` x5 |
| map | 5/6 | 5/6 | 5/6 | `map` x6 | `WebFetch` x1 |
| crawl | 4/6 | 4/6 | 6/6 | `crawl` x4, `scrape` x3, `map` x1, `status` x1 | - |
| agent | 0/6 | 0/6 | 6/6 | `scrape` x8, `search` x4, `list` x1, `status` x1 | `curl` x2 |
| interact | 3/6 | 3/6 | 3/6 | `interact` x6, `scrape` x3 | `curl` x3 |
| monitor | 6/6 | 6/6 | 6/6 | - | - |
| download | 5/6 | 5/6 | 5/6 | `download` x5, `scrape` x1 | `curl` x1, `wget` x1 |
| parse | 4/6 | 4/6 | 4/6 | `parse` x4 | - |
| research | 6/6 | 6/6 | 6/6 | `research` x6 | - |
| developer | 1/6 | 1/6 | 1/6 | `developer (API)` x1 | `curl` x19, `WebSearch` x7, `WebFetch` x1 |
| alexandria | 4/6 | 4/6 | 4/6 | `list` x9, `find-tools` x4, `alexandria` x4, `scrape` x3, `search` x2 | `curl` x3 |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| s01 |  search | other-shell, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 2/3 |  |
| s02 |  search | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |  |
| s03 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |  |
| s04 |  scrape | other-shell, firecrawl, firecrawl | `scrape` firecrawl-scrape | 2/3 |  |
| s05 |  map | firecrawl, firecrawl, firecrawl | `map` firecrawl-map | 3/3 |  |
| s06 |  map | native, firecrawl, firecrawl | `map` firecrawl-map | 2/3 |  |
| s07 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` `map` `scrape` firecrawl firecrawl-crawl | 2/3 |  |
| s08 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` `scrape` `status` firecrawl firecrawl-crawl | 2/3 |  |
| s09 |  agent | firecrawl, firecrawl, firecrawl | `status` firecrawl firecrawl-search | 0/3 | Replaces the told-suite pricing prompt, which named one known page (scrape is right there). Needs navigating a JS job board. |
| s10 |  agent | firecrawl, firecrawl, firecrawl | `list` `scrape` `search` firecrawl firecrawl-search | 0/3 |  |
| s11 |  interact | other-shell, other-shell, other-shell | - | 0/3 |  |
| s12 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 3/3 |  |
| s13 |  monitor | firecrawl, firecrawl, firecrawl | firecrawl-monitor | 3/3 |  |
| s14 |  monitor | firecrawl, firecrawl, firecrawl | firecrawl-monitor | 3/3 |  |
| s15 |  download | firecrawl, firecrawl, firecrawl | `download` firecrawl-download | 3/3 |  |
| s16 |  download | firecrawl, other-shell, firecrawl | `download` `scrape` firecrawl-download | 2/3 |  |
| s17 |  parse | firecrawl, firecrawl, firecrawl | `parse` firecrawl-parse | 3/3 |  |
| s18 |  parse | none, none, firecrawl | `parse` firecrawl-parse | 1/3 |  |
| s19 |  research | firecrawl, firecrawl, firecrawl | `research` firecrawl-research-index | 3/3 |  |
| s20 |  research | firecrawl, firecrawl, firecrawl | `research` firecrawl-research-index | 3/3 |  |
| s21 |  developer | other-shell, other-shell, other-shell | - | 0/3 |  |
| s22 |  developer | other-shell, other-shell, other-shell | firecrawl-developer-index | 1/3 |  |
| s23 |  alexandria | other-shell, firecrawl, other-shell | `alexandria` `find-tools` `search` firecrawl-alexandria firecrawl-search | 1/3 |  |
| s24 |  alexandria | firecrawl, firecrawl, firecrawl | `alexandria` `find-tools` `list` `scrape` `search` firecrawl-alexandria firecrawl-search | 3/3 |  |

## Tool calls

Across 72 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 151 | 65 | 2.10 |
| `Skill` | 60 | 56 | 0.83 |
| `ToolSearch` | 7 | 7 | 0.10 |
| `WebSearch` | 7 | 5 | 0.10 |
| `WebFetch` | 2 | 2 | 0.03 |
| `Read` | 1 | 1 | 0.01 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-search` | 11 | 11 | 0.15 |
| `firecrawl` | 6 | 6 | 0.08 |
| `firecrawl-monitor` | 6 | 6 | 0.08 |
| `firecrawl-research-index` | 6 | 6 | 0.08 |
| `firecrawl-download` | 5 | 5 | 0.07 |
| `firecrawl-map` | 5 | 5 | 0.07 |
| `firecrawl-scrape` | 5 | 5 | 0.07 |
| `firecrawl-alexandria` | 4 | 4 | 0.06 |
| `firecrawl-crawl` | 4 | 4 | 0.06 |
| `firecrawl-parse` | 4 | 4 | 0.06 |
| `firecrawl-interact` | 3 | 3 | 0.04 |
| `firecrawl-developer-index` | 1 | 1 | 0.01 |
| `firecrawl-agent` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 26 | 19 | 0.36 |
| `firecrawl search` | 11 | 10 | 0.15 |
| `firecrawl list` | 10 | 4 | 0.14 |
| `firecrawl map` | 7 | 6 | 0.10 |
| `firecrawl interact` | 6 | 3 | 0.08 |
| `firecrawl research` | 6 | 6 | 0.08 |
| `firecrawl download` | 5 | 5 | 0.07 |
| `firecrawl alexandria` | 4 | 4 | 0.06 |
| `firecrawl crawl` | 4 | 4 | 0.06 |
| `firecrawl find-tools` | 4 | 4 | 0.06 |
| `firecrawl parse` | 4 | 4 | 0.06 |
| `firecrawl status` | 2 | 2 | 0.03 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |

**Firecrawl API endpoints called directly (curl)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `developer` | 1 | 1 | 0.01 |


# subtools-plain eval: r4-tree

Skills `de1229c` · model `claude-sonnet-5-5` · 2 trials · max 12 turns · Firecrawl key: True · 2.1.304 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 94% (45/48) |
| Runs that used Firecrawl | 96% (46/48) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/48) |
| Mean tool calls | 3.2 |
| Mean model cost (USD) | 0.067 |
| Mean duration (s) | 23 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| search | 4/4 | 4/4 | 4/4 | `search` x4, `scrape` x2 | `curl` x1 |
| scrape | 4/4 | 4/4 | 4/4 | `scrape` x6 | - |
| map | 4/4 | 4/4 | 4/4 | `map` x4 | - |
| crawl | 4/4 | 4/4 | 4/4 | `crawl` x4 | - |
| agent | 1/4 | 0/4 | 2/4 | `scrape` x4, `status` x2, `agent` x1 | - |
| interact | 4/4 | 4/4 | 4/4 | `interact` x10, `scrape` x4 | - |
| monitor | 4/4 | 4/4 | 4/4 | - | - |
| download | 4/4 | 4/4 | 4/4 | `download` x4, `scrape` x2, `map` x1 | - |
| parse | 4/4 | 4/4 | 4/4 | `parse` x4 | - |
| research | 4/4 | 4/4 | 4/4 | `research` x4 | - |
| developer | 4/4 | 4/4 | 4/4 | `scrape` x9, `developer (API)` x6, `gh` x1 | `curl` x5 |
| alexandria | 4/4 | 4/4 | 4/4 | `scrape` x5, `search` x4, `alexandria` x4, `find-tools` x2, `list` x2 | - |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| s01 |  search | firecrawl, firecrawl | `scrape` `search` firecrawl-search | 2/2 |  |
| s02 |  search | firecrawl, firecrawl | `search` firecrawl-search | 2/2 |  |
| s03 |  scrape | firecrawl, firecrawl | `scrape` firecrawl-scrape | 2/2 |  |
| s04 |  scrape | firecrawl, firecrawl | `scrape` firecrawl-scrape | 2/2 |  |
| s05 |  map | firecrawl, firecrawl | `map` firecrawl-map | 2/2 |  |
| s06 |  map | firecrawl, firecrawl | `map` firecrawl-map | 2/2 |  |
| s07 |  crawl | firecrawl, firecrawl | `crawl` firecrawl-crawl | 2/2 |  |
| s08 |  crawl | firecrawl, firecrawl | `crawl` firecrawl-crawl | 2/2 |  |
| s09 |  agent | none, none | - | 0/2 | Agent case: unknown pages across many sites, dozens of records. Replaces the told-suite pricing prompt (one known page, where scrape is right). |
| s10 |  agent | firecrawl, firecrawl | `agent` `scrape` `status` firecrawl | 1/2 |  |
| s11 |  interact | firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 2/2 | Login form on a public test site. Replaces the HN 'new' link prompt, which agents answered by fetching /newest directly. |
| s12 |  interact | firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 2/2 |  |
| s13 |  monitor | firecrawl, firecrawl | firecrawl-monitor | 2/2 |  |
| s14 |  monitor | firecrawl, firecrawl | firecrawl-monitor | 2/2 |  |
| s15 |  download | firecrawl, firecrawl | `download` firecrawl-download | 2/2 |  |
| s16 |  download | firecrawl, firecrawl | `download` `map` `scrape` firecrawl-download | 2/2 |  |
| s17 |  parse | firecrawl, firecrawl | `parse` firecrawl-parse | 2/2 |  |
| s18 |  parse | firecrawl, firecrawl | `parse` firecrawl-parse | 2/2 |  |
| s19 |  research | firecrawl, firecrawl | `research` firecrawl-research-index | 2/2 |  |
| s20 |  research | firecrawl, firecrawl | `research` firecrawl-research-index | 2/2 |  |
| s21 |  developer | firecrawl, firecrawl | `gh` `scrape` firecrawl-developer-index | 2/2 |  |
| s22 |  developer | firecrawl, firecrawl | `scrape` firecrawl-developer-index | 2/2 |  |
| s23 |  alexandria | firecrawl, firecrawl | `alexandria` `find-tools` `scrape` `search` firecrawl-alexandria | 2/2 |  |
| s24 |  alexandria | firecrawl, firecrawl | `alexandria` `list` `scrape` `search` firecrawl-alexandria | 2/2 |  |

## Tool calls

Across 48 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 107 | 42 | 2.23 |
| `Skill` | 46 | 46 | 0.96 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-alexandria` | 4 | 4 | 0.08 |
| `firecrawl-crawl` | 4 | 4 | 0.08 |
| `firecrawl-developer-index` | 4 | 4 | 0.08 |
| `firecrawl-download` | 4 | 4 | 0.08 |
| `firecrawl-interact` | 4 | 4 | 0.08 |
| `firecrawl-map` | 4 | 4 | 0.08 |
| `firecrawl-monitor` | 4 | 4 | 0.08 |
| `firecrawl-parse` | 4 | 4 | 0.08 |
| `firecrawl-research-index` | 4 | 4 | 0.08 |
| `firecrawl-scrape` | 4 | 4 | 0.08 |
| `firecrawl-search` | 4 | 4 | 0.08 |
| `firecrawl` | 2 | 2 | 0.04 |
| `firecrawl-agent` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 32 | 21 | 0.67 |
| `firecrawl interact` | 10 | 4 | 0.21 |
| `firecrawl search` | 8 | 8 | 0.17 |
| `firecrawl map` | 5 | 5 | 0.10 |
| `firecrawl alexandria` | 4 | 4 | 0.08 |
| `firecrawl crawl` | 4 | 4 | 0.08 |
| `firecrawl download` | 4 | 4 | 0.08 |
| `firecrawl parse` | 4 | 4 | 0.08 |
| `firecrawl research` | 4 | 4 | 0.08 |
| `firecrawl find-tools` | 2 | 2 | 0.04 |
| `firecrawl list` | 2 | 2 | 0.04 |
| `firecrawl status` | 2 | 2 | 0.04 |
| `firecrawl agent` | 1 | 1 | 0.02 |
| `firecrawl gh` | 1 | 1 | 0.02 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |

**Firecrawl API endpoints called directly (curl)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `developer` | 6 | 4 | 0.12 |


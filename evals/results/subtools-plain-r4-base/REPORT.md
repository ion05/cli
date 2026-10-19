# subtools-plain eval: r4-base

Skills `WORKTREE` · model `claude-sonnet-5-5` · 2 trials · max 12 turns · Firecrawl key: True · 2.1.304 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 94% (45/48) |
| Runs that used Firecrawl | 94% (45/48) |
| Runs that used built-in WebSearch/WebFetch | 2% (1/48) |
| Mean tool calls | 3.0 |
| Mean model cost (USD) | 0.063 |
| Mean duration (s) | 23 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| search | 4/4 | 4/4 | 4/4 | `search` x4, `scrape` x2 | `curl` x3 |
| scrape | 4/4 | 4/4 | 4/4 | `scrape` x4 | - |
| map | 4/4 | 4/4 | 4/4 | `map` x4 | - |
| crawl | 4/4 | 4/4 | 4/4 | `crawl` x4 | - |
| agent | 2/4 | 2/4 | 2/4 | `agent` x2 | `curl` x6 |
| interact | 4/4 | 4/4 | 4/4 | `interact` x8, `scrape` x4 | - |
| monitor | 4/4 | 4/4 | 4/4 | - | - |
| download | 4/4 | 4/4 | 4/4 | `download` x4, `scrape` x2 | - |
| parse | 4/4 | 4/4 | 4/4 | `parse` x4 | - |
| research | 3/4 | 3/4 | 3/4 | `research` x3 | `WebSearch` x1 |
| developer | 4/4 | 4/4 | 4/4 | `scrape` x7, `developer (API)` x5, `developer` x1 | `curl` x3 |
| alexandria | 4/4 | 4/4 | 4/4 | `search` x4, `scrape` x4, `alexandria` x4, `find-tools` x2, `list` x2 | - |

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
| s09 |  agent | other-shell, none | - | 0/2 | Agent case: unknown pages across many sites, dozens of records. Replaces the told-suite pricing prompt (one known page, where scrape is right). |
| s10 |  agent | firecrawl, firecrawl | `agent` firecrawl-agent | 2/2 |  |
| s11 |  interact | firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 2/2 | Login form on a public test site. Replaces the HN 'new' link prompt, which agents answered by fetching /newest directly. |
| s12 |  interact | firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 2/2 |  |
| s13 |  monitor | firecrawl, firecrawl | firecrawl-monitor | 2/2 |  |
| s14 |  monitor | firecrawl, firecrawl | firecrawl-monitor | 2/2 |  |
| s15 |  download | firecrawl, firecrawl | `download` firecrawl-download | 2/2 |  |
| s16 |  download | firecrawl, firecrawl | `download` `scrape` firecrawl-download | 2/2 |  |
| s17 |  parse | firecrawl, firecrawl | `parse` firecrawl-parse | 2/2 |  |
| s18 |  parse | firecrawl, firecrawl | `parse` firecrawl-parse | 2/2 |  |
| s19 |  research | firecrawl, firecrawl | `research` firecrawl-research-index | 2/2 |  |
| s20 |  research | native, firecrawl | `research` firecrawl-research-index | 1/2 |  |
| s21 |  developer | firecrawl, firecrawl | `scrape` firecrawl-developer-index | 2/2 |  |
| s22 |  developer | firecrawl, firecrawl | `developer` firecrawl-developer-index | 2/2 |  |
| s23 |  alexandria | firecrawl, firecrawl | `alexandria` `find-tools` `scrape` `search` firecrawl-alexandria | 2/2 |  |
| s24 |  alexandria | firecrawl, firecrawl | `alexandria` `list` `scrape` `search` firecrawl-alexandria | 2/2 |  |

## Tool calls

Across 48 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 97 | 42 | 2.02 |
| `Skill` | 45 | 45 | 0.94 |
| `Read` | 2 | 2 | 0.04 |
| `ToolSearch` | 1 | 1 | 0.02 |
| `WebSearch` | 1 | 1 | 0.02 |

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
| `firecrawl-scrape` | 4 | 4 | 0.08 |
| `firecrawl-search` | 4 | 4 | 0.08 |
| `firecrawl-research-index` | 3 | 3 | 0.06 |
| `firecrawl-agent` | 2 | 2 | 0.04 |
| `firecrawl` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 23 | 18 | 0.48 |
| `firecrawl interact` | 8 | 4 | 0.17 |
| `firecrawl search` | 8 | 8 | 0.17 |
| `firecrawl alexandria` | 4 | 4 | 0.08 |
| `firecrawl crawl` | 4 | 4 | 0.08 |
| `firecrawl download` | 4 | 4 | 0.08 |
| `firecrawl map` | 4 | 4 | 0.08 |
| `firecrawl parse` | 4 | 4 | 0.08 |
| `firecrawl research` | 3 | 3 | 0.06 |
| `firecrawl agent` | 2 | 2 | 0.04 |
| `firecrawl find-tools` | 2 | 2 | 0.04 |
| `firecrawl list` | 2 | 2 | 0.04 |
| `firecrawl developer` | 1 | 1 | 0.02 |
| `firecrawl monitor` | 0 | 0 | 0.00 |

**Firecrawl API endpoints called directly (curl)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `developer` | 5 | 4 | 0.10 |


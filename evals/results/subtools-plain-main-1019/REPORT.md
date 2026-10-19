# subtools-plain eval: main-1019

Skills `3b90544` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.303 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 78% (14/18) |
| Runs that used Firecrawl | 83% (15/18) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/18) |
| Mean tool calls | 3.3 |
| Mean model cost (USD) | 0.070 |
| Mean duration (s) | 78 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| crawl | 6/6 | 6/6 | 6/6 | `crawl` x6 | - |
| agent | 2/6 | 3/6 | 3/6 | `scrape` x2, `agent` x2, `search` x1, `list` x1 | - |
| interact | 6/6 | 6/6 | 6/6 | `interact` x12, `scrape` x6 | - |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| s07 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` firecrawl-crawl | 3/3 |  |
| s08 |  crawl | firecrawl, firecrawl, firecrawl | `crawl` firecrawl-crawl | 3/3 |  |
| s09 |  agent | none, none, none | - | 0/3 | Agent case: unknown pages across many sites, dozens of records. Replaces the told-suite pricing prompt (one known page, where scrape is right). |
| s10 |  agent | firecrawl, firecrawl, firecrawl | `agent` `list` `scrape` `search` firecrawl-agent | 2/3 |  |
| s11 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 3/3 | Login form on a public test site. Replaces the HN 'new' link prompt, which agents answered by fetching /newest directly. |
| s12 |  interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl-interact | 3/3 |  |

## Tool calls

Across 18 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 42 | 15 | 2.33 |
| `Skill` | 15 | 15 | 0.83 |
| `Read` | 2 | 1 | 0.11 |
| `Monitor` | 1 | 1 | 0.06 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-crawl` | 6 | 6 | 0.33 |
| `firecrawl-interact` | 6 | 6 | 0.33 |
| `firecrawl-agent` | 3 | 3 | 0.17 |
| `firecrawl` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-developer-index` | 0 | 0 | 0.00 |
| `firecrawl-download` | 0 | 0 | 0.00 |
| `firecrawl-map` | 0 | 0 | 0.00 |
| `firecrawl-monitor` | 0 | 0 | 0.00 |
| `firecrawl-parse` | 0 | 0 | 0.00 |
| `firecrawl-research-index` | 0 | 0 | 0.00 |
| `firecrawl-scrape` | 0 | 0 | 0.00 |
| `firecrawl-search` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl interact` | 12 | 6 | 0.67 |
| `firecrawl scrape` | 8 | 7 | 0.44 |
| `firecrawl crawl` | 6 | 6 | 0.33 |
| `firecrawl agent` | 2 | 2 | 0.11 |
| `firecrawl list` | 1 | 1 | 0.06 |
| `firecrawl search` | 1 | 1 | 0.06 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl map` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |


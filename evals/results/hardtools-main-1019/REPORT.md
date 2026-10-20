# hardtools eval: main-1019

Skills `3b90544` · model `claude-sonnet-5-5` · 2 trials · max 80 turns · Firecrawl key: True · 2.1.303 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 0% (0/30) |
| Runs that used Firecrawl | 100% (30/30) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/30) |
| Mean tool calls | 23.7 |
| Mean model cost (USD) | 0.409 |
| Mean duration (s) | 251 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| i1 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| i3 |  None | firecrawl, firecrawl | `interact` `scrape` `search` `status` firecrawl | 0/2 |
| i4 |  None | firecrawl, firecrawl | `list` `scrape` `search` `status` firecrawl | 0/2 |
| i5 |  None | firecrawl, firecrawl | `interact` `scrape` `status` firecrawl | 0/2 |
| m1 |  None | firecrawl, firecrawl | `agent` `interact` `map` `scrape` `status` firecrawl | 0/2 |
| m2 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| m3 |  None | firecrawl, firecrawl | `map` `scrape` `search` firecrawl-search | 0/2 |
| c1 |  None | firecrawl, firecrawl | `(bare)` `batch-scrape` `credit-usage` `scrape` `status` firecrawl firecrawl-crawl | 0/2 |
| c2 |  None | firecrawl, firecrawl | `map` `scrape` `status` firecrawl | 0/2 |
| c3 |  None | firecrawl, firecrawl | `map` `scrape` `status` firecrawl | 0/2 |
| a1 |  None | firecrawl, firecrawl | `interact` `scrape` `search` `status` firecrawl | 0/2 |
| a2 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a3 |  None | firecrawl, firecrawl | `map` `scrape` `search` `status` firecrawl firecrawl-search | 0/2 |
| a4 |  None | firecrawl, firecrawl | `map` `scrape` `search` `status` firecrawl | 0/2 |
| a5 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |

## Tool calls

Across 30 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 664 | 30 | 22.13 |
| `Skill` | 30 | 30 | 1.00 |
| `Agent` | 9 | 2 | 0.30 |
| `Read` | 4 | 3 | 0.13 |
| `Monitor` | 3 | 3 | 0.10 |
| `ToolSearch` | 1 | 1 | 0.03 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 26 | 26 | 0.87 |
| `firecrawl-search` | 3 | 3 | 0.10 |
| `firecrawl-crawl` | 1 | 1 | 0.03 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-developer-index` | 0 | 0 | 0.00 |
| `firecrawl-download` | 0 | 0 | 0.00 |
| `firecrawl-interact` | 0 | 0 | 0.00 |
| `firecrawl-map` | 0 | 0 | 0.00 |
| `firecrawl-monitor` | 0 | 0 | 0.00 |
| `firecrawl-parse` | 0 | 0 | 0.00 |
| `firecrawl-research-index` | 0 | 0 | 0.00 |
| `firecrawl-scrape` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 286 | 29 | 9.53 |
| `firecrawl search` | 79 | 20 | 2.63 |
| `firecrawl interact` | 66 | 7 | 2.20 |
| `firecrawl status` | 26 | 25 | 0.87 |
| `firecrawl map` | 11 | 8 | 0.37 |
| `firecrawl agent` | 3 | 1 | 0.10 |
| `firecrawl list` | 2 | 2 | 0.07 |
| `firecrawl (bare)` | 1 | 1 | 0.03 |
| `firecrawl batch-scrape` | 1 | 1 | 0.03 |
| `firecrawl credit-usage` | 1 | 1 | 0.03 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl crawl` | 0 | 0 | 0.00 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |


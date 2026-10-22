# hardtools eval: cc-final-1021

Skills `660ddb7` · model `claude-sonnet-5-5` · 2 trials · max 80 turns · Firecrawl key: True · 2.1.306 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 0% (0/16) |
| Runs that used Firecrawl | 94% (15/16) |
| Runs that used built-in WebSearch/WebFetch | 6% (1/16) |
| Mean tool calls | 5.0 |
| Mean model cost (USD) | 0.100 |
| Mean duration (s) | 33 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| n1 |  None | firecrawl, firecrawl | `scrape` firecrawl-scrape | 0/2 |
| n2 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| n3 |  None | firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 0/2 |
| n4 |  None | firecrawl, firecrawl | `map` `scrape` firecrawl-map | 0/2 |
| n5 |  None | firecrawl, firecrawl | `scrape` `search` firecrawl-search | 0/2 |
| n6 |  None | firecrawl, native | `search` firecrawl-search | 0/2 |
| n7 |  None | firecrawl, firecrawl | `list` `scrape` `search` firecrawl-search | 0/2 |
| n8 |  None | firecrawl, firecrawl | `scrape` firecrawl-scrape | 0/2 |

## Tool calls

Across 16 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 63 | 15 | 3.94 |
| `Skill` | 15 | 15 | 0.94 |
| `ToolSearch` | 1 | 1 | 0.06 |
| `WebSearch` | 1 | 1 | 0.06 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-scrape` | 5 | 5 | 0.31 |
| `firecrawl-search` | 5 | 5 | 0.31 |
| `firecrawl` | 3 | 3 | 0.19 |
| `firecrawl-map` | 2 | 2 | 0.12 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-crawl` | 0 | 0 | 0.00 |
| `firecrawl-developer-index` | 0 | 0 | 0.00 |
| `firecrawl-download` | 0 | 0 | 0.00 |
| `firecrawl-interact` | 0 | 0 | 0.00 |
| `firecrawl-monitor` | 0 | 0 | 0.00 |
| `firecrawl-parse` | 0 | 0 | 0.00 |
| `firecrawl-research-index` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 24 | 12 | 1.50 |
| `firecrawl search` | 7 | 5 | 0.44 |
| `firecrawl list` | 2 | 1 | 0.12 |
| `firecrawl map` | 2 | 2 | 0.12 |
| `firecrawl status` | 2 | 2 | 0.12 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl crawl` | 0 | 0 | 0.00 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl interact` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |


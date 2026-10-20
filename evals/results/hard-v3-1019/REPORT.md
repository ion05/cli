# hard eval: v3-1019

Skills `88f0c2d` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.303 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 92% (22/24) |
| Runs that used Firecrawl | 71% (17/24) |
| Runs that used built-in WebSearch/WebFetch | 8% (2/24) |
| Mean tool calls | 3.0 |
| Mean model cost (USD) | 0.059 |
| Mean duration (s) | 20 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| h01 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 3/3 |
| h02 |  search | firecrawl, other-shell, firecrawl | `scrape` firecrawl-scrape | 3/3 |
| h03 |  search | other-shell, other-shell, other-shell | - | 3/3 |
| h04 |  search | other-shell, other-shell, other-shell | - | 3/3 |
| h05 |  scrape | other-shell, other-shell, other-shell | `scrape` firecrawl-developer-index firecrawl-scrape | 1/3 |
| h06 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` firecrawl-search | 3/3 |
| h07 |  scrape | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| h08 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-scrape firecrawl-search | 3/3 |

## Tool calls

Across 24 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 52 | 24 | 2.17 |
| `Skill` | 17 | 17 | 0.71 |
| `ToolSearch` | 2 | 2 | 0.08 |
| `WebFetch` | 2 | 2 | 0.08 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-search` | 11 | 11 | 0.46 |
| `firecrawl-scrape` | 4 | 4 | 0.17 |
| `firecrawl-developer-index` | 2 | 2 | 0.08 |
| `firecrawl` | 0 | 0 | 0.00 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-crawl` | 0 | 0 | 0.00 |
| `firecrawl-download` | 0 | 0 | 0.00 |
| `firecrawl-interact` | 0 | 0 | 0.00 |
| `firecrawl-map` | 0 | 0 | 0.00 |
| `firecrawl-monitor` | 0 | 0 | 0.00 |
| `firecrawl-parse` | 0 | 0 | 0.00 |
| `firecrawl-research-index` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 13 | 9 | 0.54 |
| `firecrawl search` | 11 | 11 | 0.46 |
| `firecrawl search-feedback` | 1 | 1 | 0.04 |
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

**Firecrawl API endpoints called directly (curl)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `developer` | 7 | 2 | 0.29 |


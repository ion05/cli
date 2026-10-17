# hard eval: desc-v3

Skills `WORKTREE` · model `claude-sonnet-5-5` · 3 trials · max 20 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 88% (21/24) |
| Runs that used Firecrawl | 71% (17/24) |
| Runs that used built-in WebSearch/WebFetch | 8% (2/24) |
| Mean tool calls | 2.6 |
| Mean model cost (USD) | 0.057 |
| Mean duration (s) | 9 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| h01 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 3/3 |
| h02 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-scrape firecrawl-search | 3/3 |
| h03 |  search | other-shell, other-shell, other-shell | - | 3/3 |
| h04 |  search | other-shell, other-shell, other-shell | - | 3/3 |
| h05 |  scrape | other-shell, other-shell, other-shell | `scrape` firecrawl-developer-index | 0/3 |
| h06 |  search | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| h07 |  scrape | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| h08 |  scrape | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |

## Tool calls

Across 24 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 42 | 24 | 1.75 |
| `Skill` | 16 | 16 | 0.67 |
| `ToolSearch` | 2 | 2 | 0.08 |
| `WebFetch` | 2 | 2 | 0.08 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-search` | 13 | 13 | 0.54 |
| `firecrawl-scrape` | 2 | 2 | 0.08 |
| `firecrawl-developer-index` | 1 | 1 | 0.04 |
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
| `firecrawl search` | 13 | 13 | 0.54 |
| `firecrawl scrape` | 8 | 6 | 0.33 |
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
| `developer` | 1 | 1 | 0.04 |


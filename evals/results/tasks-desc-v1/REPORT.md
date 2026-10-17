# tasks eval: desc-v1

Skills `WORKTREE` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 100% (42/42) |
| Runs that used Firecrawl | 14% (6/42) |
| Runs that used built-in WebSearch/WebFetch | 5% (2/42) |
| Mean tool calls | 0.6 |
| Mean model cost (USD) | 0.036 |
| Mean duration (s) | 6 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| t01 |  scrape | none, none, none | - | 3/3 |
| t02 |  search | none, none, none | - | 3/3 |
| t03 |  map | none, none, none | - | 3/3 |
| t04 |  search | other-shell, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |
| t05 |  scrape | firecrawl, native, native | `scrape` firecrawl-scrape | 3/3 |
| t06 |  search | none, none, none | - | 3/3 |
| t07 |  search | firecrawl, firecrawl, other-shell | `scrape` firecrawl | 3/3 |
| t08 |  search | none, none, none | - | 3/3 |
| t09 |  scrape | none, none, none | - | 3/3 |
| t10 |  scrape | none, firecrawl, other-shell | `scrape` firecrawl | 3/3 |
| t11 |  search | none, none, none | - | 3/3 |
| t12 |  scrape | other-shell, other-shell, other-shell | - | 3/3 |
| t13 |  search | none, none, none | - | 3/3 |
| t14 |  map | none, none, none | - | 3/3 |

## Tool calls

Across 42 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 15 | 12 | 0.36 |
| `Skill` | 5 | 5 | 0.12 |
| `ToolSearch` | 2 | 2 | 0.05 |
| `WebFetch` | 2 | 2 | 0.05 |
| `Read` | 1 | 1 | 0.02 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 3 | 3 | 0.07 |
| `firecrawl-scrape` | 2 | 2 | 0.05 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-crawl` | 0 | 0 | 0.00 |
| `firecrawl-developer-index` | 0 | 0 | 0.00 |
| `firecrawl-download` | 0 | 0 | 0.00 |
| `firecrawl-interact` | 0 | 0 | 0.00 |
| `firecrawl-map` | 0 | 0 | 0.00 |
| `firecrawl-monitor` | 0 | 0 | 0.00 |
| `firecrawl-parse` | 0 | 0 | 0.00 |
| `firecrawl-research-index` | 0 | 0 | 0.00 |
| `firecrawl-search` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 6 | 6 | 0.14 |
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
| `firecrawl search` | 0 | 0 | 0.00 |


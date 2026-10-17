# tasks eval: told

Skills `22358f2` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 95% (40/42) |
| Runs that used Firecrawl | 100% (42/42) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/42) |
| Mean tool calls | 3.9 |
| Mean model cost (USD) | 0.068 |
| Mean duration (s) | 39 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| t01 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl | 3/3 |
| t02 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl | 3/3 |
| t03 |  map | firecrawl, firecrawl, firecrawl | `scrape` firecrawl | 3/3 |
| t04 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl | 3/3 |
| t05 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |
| t06 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl | 3/3 |
| t07 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl | 3/3 |
| t08 |  search | firecrawl, firecrawl, firecrawl | `search` firecrawl | 3/3 |
| t09 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl | 3/3 |
| t10 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl | 3/3 |
| t11 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl | 3/3 |
| t12 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |
| t13 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 1/3 |
| t14 |  map | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |

## Tool calls

Across 42 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 114 | 42 | 2.71 |
| `Skill` | 42 | 42 | 1.00 |
| `Read` | 8 | 8 | 0.19 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 35 | 35 | 0.83 |
| `firecrawl-scrape` | 7 | 7 | 0.17 |
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
| `firecrawl scrape` | 102 | 39 | 2.43 |
| `firecrawl search` | 3 | 3 | 0.07 |
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


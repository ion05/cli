# tasks eval: only-firecrawl

Skills `22358f2` · model `claude-sonnet-5-5` · 3 trials · max 20 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 95% (40/42) |
| Runs that used Firecrawl | 100% (42/42) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/42) |
| Mean tool calls | 4.0 |
| Mean model cost (USD) | 0.061 |
| Mean duration (s) | 39 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| t01 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |
| t02 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl | 3/3 |
| t03 |  map | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl firecrawl-search | 3/3 |
| t04 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl firecrawl-search | 3/3 |
| t05 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |
| t06 |  search | firecrawl, firecrawl, firecrawl | `scrape` | 3/3 |
| t07 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |
| t08 |  search | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| t09 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |
| t10 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-search | 3/3 |
| t11 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |
| t12 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |
| t13 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 1/3 |
| t14 |  map | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |

## Tool calls

Across 42 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 121 | 42 | 2.88 |
| `Skill` | 27 | 27 | 0.64 |
| `Read` | 18 | 15 | 0.43 |
| `Monitor` | 1 | 1 | 0.02 |
| `ScheduleWakeup` | 1 | 1 | 0.02 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-scrape` | 13 | 13 | 0.31 |
| `firecrawl` | 10 | 10 | 0.24 |
| `firecrawl-search` | 4 | 4 | 0.10 |
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

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 113 | 37 | 2.69 |
| `firecrawl search` | 6 | 6 | 0.14 |
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


# tasks eval: baseline

Skills `22358f2` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 100% (42/42) |
| Runs that used Firecrawl | 0% (0/42) |
| Runs that used built-in WebSearch/WebFetch | 36% (15/42) |
| Mean tool calls | 0.8 |
| Mean model cost (USD) | 0.036 |
| Mean duration (s) | 6 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| t01 |  scrape | none, none, none | - | 3/3 |
| t02 |  search | none, none, none | - | 3/3 |
| t03 |  map | none, none, none | - | 3/3 |
| t04 |  search | native, native, native | - | 3/3 |
| t05 |  scrape | native, native, native | - | 3/3 |
| t06 |  search | none, none, none | - | 3/3 |
| t07 |  search | native, native, native | - | 3/3 |
| t08 |  search | none, none, none | - | 3/3 |
| t09 |  scrape | none, none, none | - | 3/3 |
| t10 |  scrape | native, native, native | - | 3/3 |
| t11 |  search | none, none, none | - | 3/3 |
| t12 |  scrape | native, native, native | - | 3/3 |
| t13 |  search | none, none, none | - | 3/3 |
| t14 |  map | none, none, none | - | 3/3 |

## Tool calls

Across 42 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `WebFetch` | 16 | 15 | 0.38 |
| `ToolSearch` | 15 | 15 | 0.36 |
| `Bash` | 4 | 3 | 0.10 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 0 | 0 | 0.00 |
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
| `firecrawl-scrape` | 0 | 0 | 0.00 |
| `firecrawl-search` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
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
| `firecrawl scrape` | 0 | 0 | 0.00 |
| `firecrawl search` | 0 | 0 | 0.00 |


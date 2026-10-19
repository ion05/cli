# tasks eval: codex-original

Skills `22358f2` · model `(codex default)` · 3 trials · max n/a turns · Firecrawl key: True · codex-cli 0.163.0

## Headline

| Metric | Value |
|---|---|
| Correct answers | 93% (39/42) |
| Runs that used Firecrawl | 98% (41/42) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/42) |
| Mean tool calls | 3.4 |
| Mean model cost (USD) | 0.025 |
| Mean duration (s) | 14 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| t01 |  scrape | firecrawl, firecrawl, firecrawl | `developer` `scrape` firecrawl firecrawl-developer-index firecrawl-scrape | 3/3 |
| t02 |  search | firecrawl, firecrawl, firecrawl | `developer` firecrawl-developer-index | 3/3 |
| t03 |  map | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |
| t04 |  search | firecrawl, firecrawl, firecrawl | `developer` `scrape` firecrawl firecrawl-developer-index firecrawl-scrape | 3/3 |
| t05 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape | 3/3 |
| t06 |  search | firecrawl, firecrawl, firecrawl | `developer` `scrape` firecrawl firecrawl-developer-index firecrawl-scrape | 3/3 |
| t07 |  search | firecrawl, firecrawl, firecrawl | `developer` `scrape` firecrawl firecrawl-developer-index firecrawl-scrape | 3/3 |
| t08 |  search | none, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |
| t09 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |
| t10 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |
| t11 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |
| t12 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |
| t13 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 0/3 |
| t14 |  map | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |

## Tool calls

Across 42 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `shell` | 142 | 41 | 3.38 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 35 | 35 | 0.83 |
| `firecrawl-scrape` | 32 | 32 | 0.76 |
| `firecrawl-developer-index` | 9 | 9 | 0.21 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-crawl` | 0 | 0 | 0.00 |
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
| `firecrawl scrape` | 34 | 33 | 0.81 |
| `firecrawl developer` | 9 | 9 | 0.21 |
| `firecrawl status` | 1 | 1 | 0.02 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl crawl` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl interact` | 0 | 0 | 0.00 |
| `firecrawl map` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |
| `firecrawl search` | 0 | 0 | 0.00 |


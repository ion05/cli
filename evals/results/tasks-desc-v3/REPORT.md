# tasks eval: desc-v3

Skills `WORKTREE` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 100% (42/42) |
| Runs that used Firecrawl | 26% (11/42) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/42) |
| Mean tool calls | 0.6 |
| Mean model cost (USD) | 0.037 |
| Mean duration (s) | 5 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| t01 |  scrape | none, none, none | - | 3/3 |
| t02 |  search | none, none, none | - | 3/3 |
| t03 |  map | none, none, none | - | 3/3 |
| t04 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |
| t05 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |
| t06 |  search | none, none, none | - | 3/3 |
| t07 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |
| t08 |  search | none, none, none | - | 3/3 |
| t09 |  scrape | none, none, none | - | 3/3 |
| t10 |  scrape | firecrawl, none, none | `scrape` firecrawl-scrape | 3/3 |
| t11 |  search | none, none, none | - | 3/3 |
| t12 |  scrape | other-shell, firecrawl, other-shell | `scrape` firecrawl-scrape | 3/3 |
| t13 |  search | none, none, none | - | 3/3 |
| t14 |  map | none, none, none | - | 3/3 |

## Tool calls

Across 42 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 13 | 13 | 0.31 |
| `Skill` | 11 | 11 | 0.26 |
| `Read` | 3 | 3 | 0.07 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-scrape` | 11 | 11 | 0.26 |
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
| `firecrawl-search` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 11 | 11 | 0.26 |
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


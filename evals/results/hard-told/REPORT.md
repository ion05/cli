# hard eval: told

Skills `22358f2` · model `claude-sonnet-5-5` · 3 trials · max 20 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 75% (18/24) |
| Runs that used Firecrawl | 100% (24/24) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/24) |
| Mean tool calls | 3.7 |
| Mean model cost (USD) | 0.069 |
| Mean duration (s) | 39 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| h01 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl | 3/3 |
| h02 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl | 3/3 |
| h03 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl | 0/3 |
| h04 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 0/3 |
| h05 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl | 3/3 |
| h06 |  search | firecrawl, firecrawl, firecrawl | `search` firecrawl | 3/3 |
| h07 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl | 3/3 |
| h08 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl | 3/3 |

## Tool calls

Across 24 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 65 | 24 | 2.71 |
| `Skill` | 24 | 24 | 1.00 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 22 | 22 | 0.92 |
| `firecrawl-scrape` | 2 | 2 | 0.08 |
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
| `firecrawl scrape` | 52 | 21 | 2.17 |
| `firecrawl search` | 4 | 4 | 0.17 |
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


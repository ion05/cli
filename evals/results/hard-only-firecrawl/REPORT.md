# hard eval: only-firecrawl

Skills `22358f2` · model `claude-sonnet-5-5` · 3 trials · max 20 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 88% (21/24) |
| Runs that used Firecrawl | 100% (24/24) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/24) |
| Mean tool calls | 4.8 |
| Mean model cost (USD) | 0.073 |
| Mean duration (s) | 43 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| h01 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl firecrawl-search | 3/3 |
| h02 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl firecrawl-scrape firecrawl-search | 3/3 |
| h03 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl | 3/3 |
| h04 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 0/3 |
| h05 |  scrape | firecrawl, firecrawl, firecrawl | `developer` `scrape` firecrawl firecrawl-developer-index | 3/3 |
| h06 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 3/3 |
| h07 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl firecrawl-search | 3/3 |
| h08 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl | 3/3 |

## Tool calls

Across 24 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 85 | 24 | 3.54 |
| `Skill` | 21 | 21 | 0.88 |
| `Read` | 9 | 6 | 0.38 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 10 | 10 | 0.42 |
| `firecrawl-search` | 5 | 5 | 0.21 |
| `firecrawl-scrape` | 4 | 4 | 0.17 |
| `firecrawl-developer-index` | 2 | 2 | 0.08 |
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
| `firecrawl scrape` | 63 | 19 | 2.62 |
| `firecrawl search` | 9 | 9 | 0.38 |
| `firecrawl developer` | 2 | 2 | 0.08 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl crawl` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl interact` | 0 | 0 | 0.00 |
| `firecrawl map` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |


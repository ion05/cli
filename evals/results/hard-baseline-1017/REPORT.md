# hard eval: baseline-1017

Skills `22358f2` · model `claude-sonnet-5-5` · 3 trials · max 20 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 88% (21/24) |
| Runs that used Firecrawl | 8% (2/24) |
| Runs that used built-in WebSearch/WebFetch | 75% (18/24) |
| Mean tool calls | 2.4 |
| Mean model cost (USD) | 0.049 |
| Mean duration (s) | 10 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| h01 |  search | native, native, native | - | 3/3 |
| h02 |  search | native, native, native | - | 3/3 |
| h03 |  search | other-shell, other-shell, other-shell | - | 3/3 |
| h04 |  search | other-shell, other-shell, other-shell | - | 3/3 |
| h05 |  scrape | other-shell, other-shell, other-shell | `scrape` firecrawl-developer-index | 0/3 |
| h06 |  search | native, native, native | - | 3/3 |
| h07 |  scrape | native, native, native | - | 3/3 |
| h08 |  scrape | native, native, native | - | 3/3 |

## Tool calls

Across 24 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 21 | 9 | 0.88 |
| `ToolSearch` | 18 | 18 | 0.75 |
| `WebFetch` | 10 | 10 | 0.42 |
| `WebSearch` | 8 | 8 | 0.33 |
| `Skill` | 1 | 1 | 0.04 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
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
| `firecrawl-scrape` | 0 | 0 | 0.00 |
| `firecrawl-search` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 2 | 1 | 0.08 |
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

**Firecrawl API endpoints called directly (curl)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `developer` | 4 | 1 | 0.17 |


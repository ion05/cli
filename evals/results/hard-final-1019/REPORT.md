# hard eval: final-1019

Skills `fa268d1` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.303 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 100% (24/24) |
| Runs that used Firecrawl | 71% (17/24) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/24) |
| Mean tool calls | 2.5 |
| Mean model cost (USD) | 0.060 |
| Mean duration (s) | 13 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| h01 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 3/3 |
| h02 |  search | other-shell, firecrawl, firecrawl | `scrape` `search` firecrawl-scrape firecrawl-search | 3/3 |
| h03 |  search | other-shell, other-shell, other-shell | - | 3/3 |
| h04 |  search | other-shell, other-shell, other-shell | - | 3/3 |
| h05 |  scrape | firecrawl, other-shell, other-shell | `scrape` firecrawl-developer-index | 3/3 |
| h06 |  search | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| h07 |  scrape | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| h08 |  scrape | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |

## Tool calls

Across 24 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 43 | 24 | 1.79 |
| `Skill` | 17 | 17 | 0.71 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-search` | 13 | 13 | 0.54 |
| `firecrawl-developer-index` | 3 | 3 | 0.12 |
| `firecrawl-scrape` | 1 | 1 | 0.04 |
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
| `firecrawl scrape` | 14 | 7 | 0.58 |
| `firecrawl search` | 13 | 13 | 0.54 |
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


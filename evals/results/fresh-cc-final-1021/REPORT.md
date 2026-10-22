# fresh eval: cc-final-1021

Skills `660ddb7` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.306 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 0% (0/84) |
| Runs that used Firecrawl | 43% (36/84) |
| Runs that used built-in WebSearch/WebFetch | 46% (39/84) |
| Mean tool calls | 2.5 |
| Mean model cost (USD) | 0.062 |
| Mean duration (s) | 17 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| f01 |  search | native, native, native | - | 0/3 |
| f02 |  search | native, firecrawl, firecrawl | `search` firecrawl-search | 0/3 |
| f03 |  search | firecrawl, native, firecrawl | `search` firecrawl-search | 0/3 |
| f04 |  search | native, firecrawl, native | `search` firecrawl-search | 0/3 |
| f05 |  search | native, native, native | - | 0/3 |
| f06 |  search | native, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 0/3 |
| f07 |  search | native, native, native | - | 0/3 |
| f08 |  search | native, firecrawl, native | `scrape` `search` firecrawl-search | 0/3 |
| f09 |  search | native, native, firecrawl | `search` firecrawl-search | 0/3 |
| f10 |  search | native, native, native | - | 0/3 |
| f11 |  search | native, native, native | - | 0/3 |
| f12 |  search | native, native, native | - | 0/3 |
| f13 |  search | native, firecrawl, native | `search` firecrawl-search | 0/3 |
| f14 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 0/3 |
| f15 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 0/3 |
| f16 |  search | none, none, none | - | 0/3 |
| f17 |  search | firecrawl, firecrawl, native | `search` firecrawl-search | 0/3 |
| f18 |  search | native, firecrawl, native | `search` firecrawl-search | 0/3 |
| f19 |  search | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 0/3 |
| f20 |  search | native, native, native | - | 0/3 |
| f21 |  search | firecrawl, firecrawl, native | `search` firecrawl-search | 0/3 |
| f22 |  search | native, native, other-shell | - | 0/3 |
| f23 |  search | firecrawl, firecrawl, other-shell | `scrape` `search` firecrawl-search | 0/3 |
| f24 |  search | firecrawl, other-shell, firecrawl | `scrape` `search` firecrawl-search | 0/3 |
| f25 |  search | other-shell, other-shell, other-shell | - | 0/3 |
| f26 |  search | other-shell, firecrawl, other-shell | `scrape` firecrawl-scrape firecrawl-search | 0/3 |
| f27 |  search | other-shell, other-shell, other-shell | `scrape` firecrawl-developer-index | 0/3 |
| f28 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 0/3 |

## Tool calls

Across 84 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 86 | 43 | 1.02 |
| `WebSearch` | 44 | 38 | 0.52 |
| `ToolSearch` | 39 | 39 | 0.46 |
| `Skill` | 38 | 38 | 0.45 |
| `WebFetch` | 2 | 2 | 0.02 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-search` | 29 | 29 | 0.35 |
| `firecrawl-scrape` | 4 | 4 | 0.05 |
| `claude-api` | 3 | 3 | 0.04 |
| `firecrawl-developer-index` | 2 | 2 | 0.02 |
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
| `firecrawl search` | 36 | 27 | 0.43 |
| `firecrawl scrape` | 22 | 16 | 0.26 |
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


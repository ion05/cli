# fresh eval: cc-native-1021

Skills `NONE` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.306 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 0% (0/84) |
| Runs that used Firecrawl | 0% (0/84) |
| Runs that used built-in WebSearch/WebFetch | 85% (71/84) |
| Mean tool calls | 2.2 |
| Mean model cost (USD) | 0.049 |
| Mean duration (s) | 14 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| f01 |  search | native, native, native | - | 0/3 |
| f02 |  search | native, native, native | - | 0/3 |
| f03 |  search | native, native, native | - | 0/3 |
| f04 |  search | native, native, native | - | 0/3 |
| f05 |  search | native, native, native | - | 0/3 |
| f06 |  search | native, native, native | - | 0/3 |
| f07 |  search | native, native, native | - | 0/3 |
| f08 |  search | native, native, native | - | 0/3 |
| f09 |  search | native, native, native | - | 0/3 |
| f10 |  search | native, native, native | - | 0/3 |
| f11 |  search | native, native, native | - | 0/3 |
| f12 |  search | native, native, native | - | 0/3 |
| f13 |  search | native, native, native | - | 0/3 |
| f14 |  search | native, native, native | - | 0/3 |
| f15 |  search | native, native, native | - | 0/3 |
| f16 |  search | none, none, none | - | 0/3 |
| f17 |  search | native, native, native | - | 0/3 |
| f18 |  search | native, native, native | - | 0/3 |
| f19 |  search | native, native, native | - | 0/3 |
| f20 |  search | native, native, native | - | 0/3 |
| f21 |  search | native, native, native | - | 0/3 |
| f22 |  search | native, native, native | - | 0/3 |
| f23 |  search | native, native, native | - | 0/3 |
| f24 |  search | other-shell, other-shell, other-shell | - | 0/3 |
| f25 |  search | other-shell, other-shell, other-shell | - | 0/3 |
| f26 |  search | other-shell, other-shell, other-shell | - | 0/3 |
| f27 |  search | other-shell, other-shell, other-shell | - | 0/3 |
| f28 |  search | native, native, native | - | 0/3 |

## Tool calls

Across 84 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `ToolSearch` | 72 | 71 | 0.86 |
| `WebSearch` | 71 | 61 | 0.85 |
| `Bash` | 28 | 15 | 0.33 |
| `WebFetch` | 13 | 12 | 0.15 |
| `Skill` | 3 | 3 | 0.04 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `claude-api` | 3 | 3 | 0.04 |
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


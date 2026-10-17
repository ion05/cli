# complex eval: original

Skills `22358f2` · model `claude-sonnet-5-5` · 3 trials · max 30 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 82% (59/72) |
| Runs that used Firecrawl | 1% (1/72) |
| Runs that used built-in WebSearch/WebFetch | 93% (67/72) |
| Mean tool calls | 2.9 |
| Mean model cost (USD) | 0.061 |
| Mean duration (s) | 16 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| c01 |  None | native, native, native | - | 3/3 |
| c02 |  None | native, native, native | - | 3/3 |
| c03 |  None | native, native, native | - | 2/3 |
| c04 |  None | native, native, native | - | 3/3 |
| c05 |  None | other-shell, other-shell, other-shell | - | 3/3 |
| c06 |  None | native, native, native | - | 3/3 |
| c07 |  None | native, native, firecrawl | `scrape` `search` firecrawl | 3/3 |
| c08 |  None | native, native, native | - | 0/3 |
| c09 |  None | native, other-shell, native | - | 3/3 |
| c10 |  None | native, native, native | - | 2/3 |
| c11 |  None | native, native, native | - | 3/3 |
| c12 |  None | native, native, native | - | 2/3 |
| c13 |  None | native, native, native | - | 3/3 |
| c14 |  None | other-shell, other-shell, other-shell | - | 3/3 |
| c15 |  None | native, native, other-shell | - | 1/3 |
| c16 |  None | native, native, native | - | 3/3 |
| c17 |  None | native, native, native | - | 1/3 |
| c18 |  None | native, native, native | - | 3/3 |
| c19 |  None | native, native, native | - | 2/3 |
| c20 |  None | native, native, native | - | 3/3 |
| c21 |  None | native, native, native | - | 3/3 |
| c22 |  None | native, native, native | - | 3/3 |
| c23 |  None | native, native, native | - | 1/3 |
| c24 |  None | native, native, native | - | 3/3 |

## Tool calls

Across 72 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `ToolSearch` | 70 | 67 | 0.97 |
| `WebFetch` | 66 | 47 | 0.92 |
| `WebSearch` | 51 | 43 | 0.71 |
| `Bash` | 21 | 11 | 0.29 |
| `Skill` | 1 | 1 | 0.01 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 1 | 1 | 0.01 |
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
| `firecrawl scrape` | 1 | 1 | 0.01 |
| `firecrawl search` | 1 | 1 | 0.01 |
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


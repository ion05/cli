# hardtools eval: cc-native-1021

Skills `NONE` · model `claude-sonnet-5-5` · 2 trials · max 80 turns · Firecrawl key: False · 2.1.306 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 0% (0/16) |
| Runs that used Firecrawl | 0% (0/16) |
| Runs that used built-in WebSearch/WebFetch | 88% (14/16) |
| Mean tool calls | 5.4 |
| Mean model cost (USD) | 0.095 |
| Mean duration (s) | 27 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| n1 |  None | native, native | - | 0/2 |
| n2 |  None | native, native | - | 0/2 |
| n3 |  None | other-shell, other-shell | - | 0/2 |
| n4 |  None | native, native | - | 0/2 |
| n5 |  None | native, native | - | 0/2 |
| n6 |  None | native, native | - | 0/2 |
| n7 |  None | other-shell, other-shell | - | 0/2 |
| n8 |  None | native, native | - | 0/2 |

## Tool calls

Across 16 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `WebFetch` | 46 | 11 | 2.88 |
| `WebSearch` | 19 | 10 | 1.19 |
| `ToolSearch` | 15 | 15 | 0.94 |
| `Bash` | 7 | 6 | 0.44 |

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


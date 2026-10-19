# hardtools eval: native

Skills `NONE` · model `claude-sonnet-5-5` · 2 trials · max 80 turns · Firecrawl key: False · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 0% (0/32) |
| Runs that used Firecrawl | 0% (0/32) |
| Runs that used built-in WebSearch/WebFetch | 81% (26/32) |
| Mean tool calls | 30.8 |
| Mean model cost (USD) | 0.327 |
| Mean duration (s) | 119 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| i1 |  None | other-shell, other-shell | - | 0/2 |
| i2 |  None | other-shell, native | - | 0/2 |
| i3 |  None | other-shell, other-shell | - | 0/2 |
| i4 |  None | other-shell, other-shell | - | 0/2 |
| i5 |  None | native, native | - | 0/2 |
| m1 |  None | native, native | - | 0/2 |
| m2 |  None | native, native | - | 0/2 |
| m3 |  None | native, native | - | 0/2 |
| c1 |  None | native, native | - | 0/2 |
| c2 |  None | native, native | - | 0/2 |
| c3 |  None | native, native | - | 0/2 |
| a1 |  None | native, native | - | 0/2 |
| a2 |  None | native, native | - | 0/2 |
| a3 |  None | native, native | - | 0/2 |
| a4 |  None | native, native | - | 0/2 |
| a5 |  None | native, native | - | 0/2 |

## Tool calls

Across 32 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `WebFetch` | 596 | 26 | 18.62 |
| `Bash` | 171 | 23 | 5.34 |
| `WebSearch` | 164 | 19 | 5.12 |
| `ToolSearch` | 42 | 32 | 1.31 |
| `Agent` | 10 | 2 | 0.31 |
| `Read` | 1 | 1 | 0.03 |

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


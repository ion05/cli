# hardtools eval: original

Skills `22358f2` · model `claude-sonnet-5-5` · 2 trials · max 80 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 0% (0/32) |
| Runs that used Firecrawl | 19% (6/32) |
| Runs that used built-in WebSearch/WebFetch | 69% (22/32) |
| Mean tool calls | 31.6 |
| Mean model cost (USD) | 0.364 |
| Mean duration (s) | 147 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| i1 |  None | other-shell, other-shell | - | 0/2 |
| i2 |  None | other-shell, other-shell | - | 0/2 |
| i3 |  None | other-shell, firecrawl | `curl` `help` `interact` `scrape` `status` | 0/2 |
| i4 |  None | other-shell, firecrawl | `scrape` `status` firecrawl | 0/2 |
| i5 |  None | native, firecrawl | `help` `interact` `scrape` `status` | 0/2 |
| m1 |  None | firecrawl, other-shell | `help` `interact` `scrape` `status` firecrawl | 0/2 |
| m2 |  None | native, native | `scrape` | 0/2 |
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
| `WebFetch` | 555 | 22 | 17.34 |
| `Bash` | 267 | 25 | 8.34 |
| `WebSearch` | 136 | 16 | 4.25 |
| `ToolSearch` | 38 | 29 | 1.19 |
| `Agent` | 9 | 2 | 0.28 |
| `Read` | 3 | 2 | 0.09 |
| `Skill` | 2 | 2 | 0.06 |
| `bash` | 1 | 1 | 0.03 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 2 | 2 | 0.06 |
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
| `firecrawl interact` | 35 | 4 | 1.09 |
| `firecrawl scrape` | 29 | 6 | 0.91 |
| `firecrawl status` | 4 | 4 | 0.12 |
| `firecrawl help` | 3 | 3 | 0.09 |
| `firecrawl curl` | 1 | 1 | 0.03 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl crawl` | 0 | 0 | 0.00 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl map` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |
| `firecrawl search` | 0 | 0 | 0.00 |


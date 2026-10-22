# hardtools eval: cc-v4-1021

Skills `e676c94` · model `claude-sonnet-5-5` · 2 trials · max 80 turns · Firecrawl key: True · 2.1.306 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 0% (0/48) |
| Runs that used Firecrawl | 83% (40/48) |
| Runs that used built-in WebSearch/WebFetch | 6% (3/48) |
| Mean tool calls | 17.3 |
| Mean model cost (USD) | 0.316 |
| Mean duration (s) | 154 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| i1 |  None | firecrawl, other-shell | `search` `status` firecrawl | 0/2 |
| i2 |  None | firecrawl, other-shell | `scrape` `status` firecrawl | 0/2 |
| i3 |  None | firecrawl, firecrawl | `interact` `scrape` `search` `status` firecrawl | 0/2 |
| i4 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| i5 |  None | firecrawl, firecrawl | `find-tools` `interact` `scrape` `search` `status` firecrawl | 0/2 |
| m1 |  None | firecrawl, firecrawl | `interact` `map` `scrape` `status` firecrawl | 0/2 |
| m2 |  None | firecrawl, firecrawl | `map` `scrape` `search` `status` firecrawl | 0/2 |
| m3 |  None | firecrawl, firecrawl | `map` `scrape` `search` `status` firecrawl | 0/2 |
| c1 |  None | firecrawl, firecrawl | `scrape` `status` firecrawl | 0/2 |
| c2 |  None | firecrawl, firecrawl | `crawl` `map` `scrape` `status` firecrawl | 0/2 |
| c3 |  None | firecrawl, firecrawl | `map` `scrape` `status` firecrawl | 0/2 |
| a1 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a2 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a3 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a4 |  None | firecrawl, firecrawl | `map` `scrape` `search` `status` firecrawl | 0/2 |
| a5 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| n1 |  None | other-shell, firecrawl | `scrape` firecrawl | 0/2 |
| n2 |  None | firecrawl, firecrawl | `map` `scrape` `search` `status` firecrawl | 0/2 |
| n3 |  None | other-shell, firecrawl | `scrape` firecrawl-scrape | 0/2 |
| n4 |  None | firecrawl, firecrawl | `map` `scrape` firecrawl-map | 0/2 |
| n5 |  None | native, native | - | 0/2 |
| n6 |  None | firecrawl, none | `scrape` `search` firecrawl-search | 0/2 |
| n7 |  None | other-shell, firecrawl | `scrape` `status` firecrawl | 0/2 |
| n8 |  None | firecrawl, firecrawl | `map` `scrape` firecrawl firecrawl-scrape | 0/2 |

## Tool calls

Across 48 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 746 | 45 | 15.54 |
| `Skill` | 40 | 40 | 0.83 |
| `WebSearch` | 13 | 3 | 0.27 |
| `Agent` | 12 | 2 | 0.25 |
| `ToolSearch` | 6 | 6 | 0.12 |
| `WebFetch` | 5 | 2 | 0.10 |
| `Monitor` | 3 | 2 | 0.06 |
| `Read` | 3 | 2 | 0.06 |
| `ReadNotifications` | 2 | 2 | 0.04 |
| `TaskStop` | 1 | 1 | 0.02 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 35 | 35 | 0.73 |
| `firecrawl-map` | 2 | 2 | 0.04 |
| `firecrawl-scrape` | 2 | 2 | 0.04 |
| `firecrawl-search` | 1 | 1 | 0.02 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-crawl` | 0 | 0 | 0.00 |
| `firecrawl-developer-index` | 0 | 0 | 0.00 |
| `firecrawl-download` | 0 | 0 | 0.00 |
| `firecrawl-interact` | 0 | 0 | 0.00 |
| `firecrawl-monitor` | 0 | 0 | 0.00 |
| `firecrawl-parse` | 0 | 0 | 0.00 |
| `firecrawl-research-index` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 302 | 38 | 6.29 |
| `firecrawl search` | 74 | 21 | 1.54 |
| `firecrawl interact` | 66 | 6 | 1.38 |
| `firecrawl status` | 32 | 32 | 0.67 |
| `firecrawl map` | 22 | 14 | 0.46 |
| `firecrawl crawl` | 1 | 1 | 0.02 |
| `firecrawl find-tools` | 1 | 1 | 0.02 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |


# hardtools eval: cc-v6-1022

Skills `badb0c9` · model `claude-sonnet-5-5` · 2 trials · max 80 turns · Firecrawl key: True · 2.1.308 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 0% (0/48) |
| Runs that used Firecrawl | 96% (46/48) |
| Runs that used built-in WebSearch/WebFetch | 2% (1/48) |
| Mean tool calls | 13.3 |
| Mean model cost (USD) | 0.251 |
| Mean duration (s) | 164 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| i1 |  None | other-shell, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| i2 |  None | firecrawl, firecrawl | `interact` `scrape` `search` `status` firecrawl | 0/2 |
| i3 |  None | firecrawl, firecrawl | `interact` `scrape` `search` `status` firecrawl | 0/2 |
| i4 |  None | firecrawl, firecrawl | `scrape` `status` firecrawl | 0/2 |
| i5 |  None | firecrawl, firecrawl | `interact` `scrape` `status` firecrawl | 0/2 |
| m1 |  None | firecrawl, firecrawl | `interact` `map` `scrape` `status` firecrawl | 0/2 |
| m2 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| m3 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl firecrawl-search | 0/2 |
| c1 |  None | firecrawl, firecrawl | `map` `scrape` `status` firecrawl | 0/2 |
| c2 |  None | firecrawl, firecrawl | `crawl` `map` `scrape` `status` firecrawl | 0/2 |
| c3 |  None | firecrawl, firecrawl | `crawl` `map` `scrape` `status` firecrawl | 0/2 |
| a1 |  None | firecrawl, firecrawl | `agent` `scrape` firecrawl-agent | 0/2 |
| a2 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a3 |  None | firecrawl, firecrawl | `agent` firecrawl-agent | 0/2 |
| a4 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a5 |  None | firecrawl, firecrawl | `scrape` `search` firecrawl | 0/2 |
| n1 |  None | firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 0/2 |
| n2 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| n3 |  None | firecrawl, firecrawl | `scrape` firecrawl firecrawl-alexandria | 0/2 |
| n4 |  None | firecrawl, firecrawl | `map` `scrape` firecrawl-map | 0/2 |
| n5 |  None | firecrawl, native | `agent` firecrawl-agent | 0/2 |
| n6 |  None | firecrawl, firecrawl | `search` firecrawl-search | 0/2 |
| n7 |  None | other-shell, firecrawl | `scrape` `search` firecrawl-alexandria firecrawl-search | 0/2 |
| n8 |  None | firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 0/2 |

## Tool calls

Across 48 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 555 | 47 | 11.56 |
| `Skill` | 51 | 46 | 1.06 |
| `ReadNotifications` | 10 | 3 | 0.21 |
| `Agent` | 8 | 2 | 0.17 |
| `Read` | 7 | 4 | 0.15 |
| `WebSearch` | 4 | 1 | 0.08 |
| `WebFetch` | 3 | 1 | 0.06 |
| `Monitor` | 1 | 1 | 0.02 |
| `ToolSearch` | 1 | 1 | 0.02 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 36 | 31 | 0.75 |
| `firecrawl-agent` | 5 | 5 | 0.10 |
| `firecrawl-search` | 4 | 4 | 0.08 |
| `firecrawl-alexandria` | 2 | 2 | 0.04 |
| `firecrawl-map` | 2 | 2 | 0.04 |
| `firecrawl-scrape` | 2 | 2 | 0.04 |
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
| `firecrawl scrape` | 235 | 40 | 4.90 |
| `firecrawl interact` | 76 | 8 | 1.58 |
| `firecrawl search` | 49 | 21 | 1.02 |
| `firecrawl status` | 26 | 26 | 0.54 |
| `firecrawl agent` | 13 | 5 | 0.27 |
| `firecrawl map` | 11 | 8 | 0.23 |
| `firecrawl crawl` | 5 | 3 | 0.10 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |


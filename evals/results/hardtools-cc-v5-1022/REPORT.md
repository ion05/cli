# hardtools eval: cc-v5-1022

Skills `0c820ab` · model `claude-sonnet-5-5` · 2 trials · max 80 turns · Firecrawl key: True · 2.1.306 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 0% (0/48) |
| Runs that used Firecrawl | 96% (46/48) |
| Runs that used built-in WebSearch/WebFetch | 4% (2/48) |
| Mean tool calls | 15.8 |
| Mean model cost (USD) | 0.285 |
| Mean duration (s) | 111 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| i1 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| i2 |  None | firecrawl, firecrawl | `interact` `scrape` `search` `status` firecrawl | 0/2 |
| i3 |  None | firecrawl, firecrawl | `interact` `scrape` `search` `status` firecrawl | 0/2 |
| i4 |  None | firecrawl, firecrawl | `list` `scrape` `search` firecrawl-agent | 0/2 |
| i5 |  None | firecrawl, firecrawl | `interact` `scrape` `status` firecrawl | 0/2 |
| m1 |  None | firecrawl, firecrawl | `interact` `map` `scrape` `status` firecrawl | 0/2 |
| m2 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| m3 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl firecrawl-search | 0/2 |
| c1 |  None | firecrawl, firecrawl | `scrape` `status` firecrawl | 0/2 |
| c2 |  None | firecrawl, firecrawl | `map` `scrape` `status` firecrawl | 0/2 |
| c3 |  None | firecrawl, firecrawl | `crawl` `map` `scrape` `status` firecrawl firecrawl-scrape | 0/2 |
| a1 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a2 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a3 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a4 |  None | firecrawl, firecrawl | `map` `scrape` `search` `status` firecrawl firecrawl-agent firecrawl-scrape | 0/2 |
| a5 |  None | native, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| n1 |  None | firecrawl, firecrawl | `scrape` firecrawl-scrape | 0/2 |
| n2 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| n3 |  None | other-shell, firecrawl | `scrape` `status` firecrawl | 0/2 |
| n4 |  None | firecrawl, firecrawl | `map` `scrape` firecrawl-map | 0/2 |
| n5 |  None | firecrawl, firecrawl | `scrape` firecrawl-search | 0/2 |
| n6 |  None | firecrawl, firecrawl | `search` firecrawl-search | 0/2 |
| n7 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| n8 |  None | firecrawl, firecrawl | `scrape` firecrawl-scrape | 0/2 |

## Tool calls

Across 48 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 677 | 47 | 14.10 |
| `Skill` | 48 | 46 | 1.00 |
| `WebFetch` | 14 | 1 | 0.29 |
| `Agent` | 10 | 2 | 0.21 |
| `WebSearch` | 5 | 2 | 0.10 |
| `ListAgents` | 4 | 1 | 0.08 |
| `Read` | 1 | 1 | 0.02 |
| `ToolSearch` | 1 | 1 | 0.02 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 32 | 32 | 0.67 |
| `firecrawl-scrape` | 6 | 6 | 0.12 |
| `firecrawl-search` | 5 | 5 | 0.10 |
| `firecrawl-agent` | 3 | 3 | 0.06 |
| `firecrawl-map` | 2 | 2 | 0.04 |
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
| `firecrawl scrape` | 275 | 42 | 5.73 |
| `firecrawl interact` | 69 | 8 | 1.44 |
| `firecrawl search` | 69 | 23 | 1.44 |
| `firecrawl status` | 31 | 31 | 0.65 |
| `firecrawl map` | 10 | 8 | 0.21 |
| `firecrawl crawl` | 5 | 2 | 0.10 |
| `firecrawl list` | 3 | 2 | 0.06 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |


# hardtools eval: pr4

Skills `bd7cac4` · model `claude-sonnet-5-5` · 2 trials · max 80 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 0% (0/32) |
| Runs that used Firecrawl | 100% (32/32) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/32) |
| Mean tool calls | 21.6 |
| Mean model cost (USD) | 0.404 |
| Mean duration (s) | 185 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| i1 |  None | firecrawl, firecrawl | `search` `status` firecrawl | 0/2 |
| i2 |  None | firecrawl, firecrawl | `interact` `scrape` `search` `status` firecrawl | 0/2 |
| i3 |  None | firecrawl, firecrawl | `help` `interact` `scrape` `search` `status` firecrawl | 0/2 |
| i4 |  None | firecrawl, firecrawl | `scrape` `status` firecrawl | 0/2 |
| i5 |  None | firecrawl, firecrawl | `interact` `scrape` `status` firecrawl | 0/2 |
| m1 |  None | firecrawl, firecrawl | `interact` `map` `scrape` `status` firecrawl | 0/2 |
| m2 |  None | firecrawl, firecrawl | `map` `scrape` `search` `status` firecrawl | 0/2 |
| m3 |  None | firecrawl, firecrawl | `map` `scrape` `search` `status` firecrawl firecrawl-search | 0/2 |
| c1 |  None | firecrawl, firecrawl | `scrape` `status` firecrawl | 0/2 |
| c2 |  None | firecrawl, firecrawl | `map` `scrape` `status` firecrawl | 0/2 |
| c3 |  None | firecrawl, firecrawl | `map` `scrape` `status` firecrawl | 0/2 |
| a1 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a2 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a3 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a4 |  None | firecrawl, firecrawl | `help` `scrape` `search` `status` firecrawl | 0/2 |
| a5 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |

## Tool calls

Across 32 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 644 | 32 | 20.12 |
| `Skill` | 32 | 32 | 1.00 |
| `Agent` | 10 | 2 | 0.31 |
| `Monitor` | 1 | 1 | 0.03 |
| `Read` | 1 | 1 | 0.03 |
| `TaskStop` | 1 | 1 | 0.03 |
| `ToolSearch` | 1 | 1 | 0.03 |
| `Write` | 1 | 1 | 0.03 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 31 | 31 | 0.97 |
| `firecrawl-search` | 1 | 1 | 0.03 |
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

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 250 | 29 | 7.81 |
| `firecrawl interact` | 83 | 8 | 2.59 |
| `firecrawl search` | 48 | 17 | 1.50 |
| `firecrawl status` | 30 | 30 | 0.94 |
| `firecrawl map` | 14 | 8 | 0.44 |
| `firecrawl help` | 2 | 2 | 0.06 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl crawl` | 0 | 0 | 0.00 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |


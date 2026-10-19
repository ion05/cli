# hardtools eval: mine

Skills `a3648a8` · model `claude-sonnet-5-5` · 2 trials · max 80 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 0% (0/32) |
| Runs that used Firecrawl | 100% (32/32) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/32) |
| Mean tool calls | 21.2 |
| Mean model cost (USD) | 0.385 |
| Mean duration (s) | 183 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| i1 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| i2 |  None | firecrawl, firecrawl | `interact` `scrape` `search` `status` firecrawl | 0/2 |
| i3 |  None | firecrawl, firecrawl | `interact` `scrape` `search` `status` firecrawl | 0/2 |
| i4 |  None | firecrawl, firecrawl | `agent` `find-tools` `list` `scrape` `search` `status` firecrawl | 0/2 |
| i5 |  None | firecrawl, firecrawl | `interact` `scrape` `status` firecrawl | 0/2 |
| m1 |  None | firecrawl, firecrawl | `interact` `map` `scrape` `status` firecrawl | 0/2 |
| m2 |  None | firecrawl, firecrawl | `map` `scrape` `search` `status` firecrawl | 0/2 |
| m3 |  None | firecrawl, firecrawl | `developer` `map` `scrape` `search` `status` firecrawl | 0/2 |
| c1 |  None | firecrawl, firecrawl | `scrape` `status` firecrawl | 0/2 |
| c2 |  None | firecrawl, firecrawl | `map` `scrape` `status` firecrawl | 0/2 |
| c3 |  None | firecrawl, firecrawl | `map` `scrape` `status` firecrawl | 0/2 |
| a1 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl firecrawl-search | 0/2 |
| a2 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl firecrawl-search | 0/2 |
| a3 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a4 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a5 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |

## Tool calls

Across 32 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 624 | 32 | 19.50 |
| `Skill` | 36 | 32 | 1.12 |
| `Agent` | 11 | 2 | 0.34 |
| `Read` | 3 | 2 | 0.09 |
| `Monitor` | 1 | 1 | 0.03 |
| `ToolSearch` | 1 | 1 | 0.03 |
| `bash` | 1 | 1 | 0.03 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 34 | 30 | 1.06 |
| `firecrawl-search` | 2 | 2 | 0.06 |
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
| `firecrawl scrape` | 254 | 31 | 7.94 |
| `firecrawl search` | 67 | 20 | 2.09 |
| `firecrawl interact` | 56 | 8 | 1.75 |
| `firecrawl status` | 29 | 29 | 0.91 |
| `firecrawl map` | 13 | 8 | 0.41 |
| `firecrawl agent` | 2 | 1 | 0.06 |
| `firecrawl list` | 2 | 1 | 0.06 |
| `firecrawl developer` | 1 | 1 | 0.03 |
| `firecrawl find-tools` | 1 | 1 | 0.03 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl crawl` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |


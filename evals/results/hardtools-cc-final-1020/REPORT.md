# hardtools eval: hardtools-cc-final-1020

Skills `660ddb7` · model `claude-sonnet-5-5` · 2 trials · max 80 turns · Firecrawl key: True · 2.1.305 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 0% (0/32) |
| Runs that used Firecrawl | 94% (30/32) |
| Runs that used built-in WebSearch/WebFetch | 3% (1/32) |
| Mean tool calls | 21.6 |
| Mean model cost (USD) | 0.382 |
| Mean duration (s) | 167 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| i1 |  None | firecrawl, other-shell | `search` `status` firecrawl | 0/2 |
| i2 |  None | firecrawl, firecrawl | `interact` `scrape` `search` `status` firecrawl | 0/2 |
| i3 |  None | firecrawl, firecrawl | `interact` `scrape` `search` `status` firecrawl | 0/2 |
| i4 |  None | firecrawl, firecrawl | `list` `scrape` `search` `status` firecrawl | 0/2 |
| i5 |  None | firecrawl, firecrawl | `interact` `scrape` `status` firecrawl | 0/2 |
| m1 |  None | firecrawl, firecrawl | `interact` `map` `scrape` `status` firecrawl | 0/2 |
| m2 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| m3 |  None | native, firecrawl | `developer` `map` `scrape` `search` `status` firecrawl | 0/2 |
| c1 |  None | firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape | 0/2 |
| c2 |  None | firecrawl, firecrawl | `crawl` `download` `map` `scrape` `status` firecrawl firecrawl-download | 0/2 |
| c3 |  None | firecrawl, firecrawl | `map` `scrape` `status` firecrawl | 0/2 |
| a1 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a2 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a3 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a4 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a5 |  None | firecrawl, firecrawl | `scrape` `search` firecrawl firecrawl-scrape | 0/2 |

## Tool calls

Across 32 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 622 | 32 | 19.44 |
| `Skill` | 30 | 30 | 0.94 |
| `WebFetch` | 12 | 1 | 0.38 |
| `Agent` | 9 | 2 | 0.28 |
| `WebSearch` | 7 | 1 | 0.22 |
| `Read` | 3 | 2 | 0.09 |
| `ReadNotifications` | 3 | 2 | 0.09 |
| `Monitor` | 2 | 1 | 0.06 |
| `ToolSearch` | 2 | 2 | 0.06 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 27 | 27 | 0.84 |
| `firecrawl-scrape` | 2 | 2 | 0.06 |
| `firecrawl-download` | 1 | 1 | 0.03 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-crawl` | 0 | 0 | 0.00 |
| `firecrawl-developer-index` | 0 | 0 | 0.00 |
| `firecrawl-interact` | 0 | 0 | 0.00 |
| `firecrawl-map` | 0 | 0 | 0.00 |
| `firecrawl-monitor` | 0 | 0 | 0.00 |
| `firecrawl-parse` | 0 | 0 | 0.00 |
| `firecrawl-research-index` | 0 | 0 | 0.00 |
| `firecrawl-search` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 249 | 28 | 7.78 |
| `firecrawl interact` | 60 | 7 | 1.88 |
| `firecrawl search` | 51 | 19 | 1.59 |
| `firecrawl status` | 27 | 27 | 0.84 |
| `firecrawl map` | 11 | 6 | 0.34 |
| `firecrawl developer` | 2 | 1 | 0.06 |
| `firecrawl crawl` | 1 | 1 | 0.03 |
| `firecrawl download` | 1 | 1 | 0.03 |
| `firecrawl list` | 1 | 1 | 0.03 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |


# hardtools eval: tree

Skills `de1229c` · model `claude-sonnet-5-5` · 1 trials · max 80 turns · Firecrawl key: True · 2.1.304 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 0% (0/6) |
| Runs that used Firecrawl | 100% (6/6) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/6) |
| Mean tool calls | 31.3 |
| Mean model cost (USD) | 0.595 |
| Mean duration (s) | 239 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| m1 |  None | firecrawl | `interact` `map` `scrape` `status` firecrawl | 0/1 |
| m3 |  None | firecrawl | `map` `scrape` `search` `status` firecrawl | 0/1 |
| c1 |  None | firecrawl | `scrape` `status` firecrawl | 0/1 |
| c3 |  None | firecrawl | `crawl` `map` `scrape` `status` firecrawl | 0/1 |
| a3 |  None | firecrawl | `scrape` `search` `status` firecrawl | 0/1 |
| a4 |  None | firecrawl | `scrape` `search` `status` firecrawl | 0/1 |

## Tool calls

Across 6 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 178 | 6 | 29.67 |
| `Skill` | 6 | 6 | 1.00 |
| `Agent` | 4 | 1 | 0.67 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 6 | 6 | 1.00 |
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
| `firecrawl scrape` | 71 | 6 | 11.83 |
| `firecrawl search` | 17 | 3 | 2.83 |
| `firecrawl interact` | 8 | 1 | 1.33 |
| `firecrawl map` | 6 | 3 | 1.00 |
| `firecrawl status` | 6 | 6 | 1.00 |
| `firecrawl crawl` | 2 | 1 | 0.33 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |


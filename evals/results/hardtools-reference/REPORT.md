# hardtools eval: reference

Skills `a3648a8` · model `claude-opus-5-5` · 1 trials · max 250 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 0% (0/16) |
| Runs that used Firecrawl | 94% (15/16) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/16) |
| Mean tool calls | 44.5 |
| Mean model cost (USD) | 1.703 |
| Mean duration (s) | 311 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| i1 |  None | other-shell | - | 0/1 |
| i2 |  None | firecrawl | `agent` `interact` `scrape` `search` `status` firecrawl | 0/1 |
| i3 |  None | firecrawl | `interact` `scrape` `status` firecrawl | 0/1 |
| i4 |  None | firecrawl | `scrape` `status` firecrawl | 0/1 |
| i5 |  None | firecrawl | `interact` `scrape` `status` firecrawl | 0/1 |
| m1 |  None | firecrawl | `interact` `map` `scrape` `status` firecrawl | 0/1 |
| m2 |  None | firecrawl | `map` `scrape` `search` firecrawl firecrawl-scrape | 0/1 |
| m3 |  None | firecrawl | `scrape` `search` `status` firecrawl | 0/1 |
| c1 |  None | firecrawl | `scrape` `status` firecrawl | 0/1 |
| c2 |  None | firecrawl | `scrape` `status` firecrawl | 0/1 |
| c3 |  None | firecrawl | `map` `scrape` `status` firecrawl | 0/1 |
| a1 |  None | firecrawl | `interact` `map` `scrape` `search` `status` firecrawl | 0/1 |
| a2 |  None | firecrawl | `scrape` `search` firecrawl-scrape firecrawl-search | 0/1 |
| a3 |  None | firecrawl | `interact` `map` `scrape` `search` `status` firecrawl | 0/1 |
| a4 |  None | firecrawl | `map` `parse` `scrape` `search` `status` `web` firecrawl | 0/1 |
| a5 |  None | firecrawl | `scrape` `search` `status` firecrawl | 0/1 |

## Tool calls

Across 16 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 662 | 16 | 41.38 |
| `Skill` | 25 | 15 | 1.56 |
| `Agent` | 24 | 4 | 1.50 |
| `Monitor` | 1 | 1 | 0.06 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 17 | 14 | 1.06 |
| `firecrawl-scrape` | 6 | 2 | 0.38 |
| `firecrawl-search` | 2 | 1 | 0.12 |
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

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 305 | 15 | 19.06 |
| `firecrawl interact` | 60 | 6 | 3.75 |
| `firecrawl search` | 59 | 8 | 3.69 |
| `firecrawl map` | 34 | 6 | 2.12 |
| `firecrawl status` | 13 | 13 | 0.81 |
| `firecrawl agent` | 2 | 1 | 0.12 |
| `firecrawl web` | 2 | 1 | 0.12 |
| `firecrawl parse` | 1 | 1 | 0.06 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl crawl` | 0 | 0 | 0.00 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |


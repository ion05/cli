# complex eval: pr4

Skills `729e12b` · model `claude-sonnet-5-5` · 3 trials · max 30 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 94% (68/72) |
| Runs that used Firecrawl | 100% (72/72) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/72) |
| Mean tool calls | 2.8 |
| Mean model cost (USD) | 0.073 |
| Mean duration (s) | 16 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| c01 |  None | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| c02 |  None | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 3/3 |
| c03 |  None | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 3/3 |
| c04 |  None | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |
| c05 |  None | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |
| c06 |  None | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl firecrawl-scrape | 3/3 |
| c07 |  None | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 3/3 |
| c08 |  None | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` firecrawl-search | 2/3 |
| c09 |  None | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |
| c10 |  None | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| c11 |  None | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| c12 |  None | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| c13 |  None | firecrawl, firecrawl, firecrawl | `scrape` `search` `status` firecrawl firecrawl-search | 2/3 |
| c14 |  None | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-search | 3/3 |
| c15 |  None | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-search | 3/3 |
| c16 |  None | firecrawl, firecrawl, firecrawl | `scrape` `search` `status` firecrawl firecrawl-search | 3/3 |
| c17 |  None | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 2/3 |
| c18 |  None | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 3/3 |
| c19 |  None | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 3/3 |
| c20 |  None | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 3/3 |
| c21 |  None | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 3/3 |
| c22 |  None | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 2/3 |
| c23 |  None | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| c24 |  None | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |

## Tool calls

Across 72 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 132 | 72 | 1.83 |
| `Skill` | 72 | 72 | 1.00 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-search` | 51 | 51 | 0.71 |
| `firecrawl-scrape` | 12 | 12 | 0.17 |
| `firecrawl` | 9 | 9 | 0.12 |
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
| `firecrawl scrape` | 59 | 45 | 0.82 |
| `firecrawl search` | 58 | 48 | 0.81 |
| `firecrawl status` | 2 | 2 | 0.03 |
| `firecrawl search-feedback` | 1 | 1 | 0.01 |
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


# hardtools eval: boost

Skills `7cc9fc8` · model `claude-sonnet-5-5` · 2 trials · max 80 turns · Firecrawl key: True · 2.1.303 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 0% (0/30) |
| Runs that used Firecrawl | 100% (30/30) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/30) |
| Mean tool calls | 22.1 |
| Mean model cost (USD) | 0.399 |
| Mean duration (s) | 167 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| i1 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| i3 |  None | firecrawl, firecrawl | `interact` `scrape` `search` `status` firecrawl | 0/2 |
| i4 |  None | firecrawl, firecrawl | `find-tools` `list` `scrape` `search` `status` firecrawl | 0/2 |
| i5 |  None | firecrawl, firecrawl | `interact` `scrape` `status` firecrawl | 0/2 |
| m1 |  None | firecrawl, firecrawl | `interact` `map` `scrape` `status` firecrawl | 0/2 |
| m2 |  None | firecrawl, firecrawl | `map` `scrape` `search` `status` firecrawl | 0/2 |
| m3 |  None | firecrawl, firecrawl | `map` `scrape` `search` `status` firecrawl | 0/2 |
| c1 |  None | firecrawl, firecrawl | `(bare)` `map` `scrape` firecrawl-download firecrawl-scrape | 0/2 |
| c2 |  None | firecrawl, firecrawl | `map` `scrape` `status` firecrawl | 0/2 |
| c3 |  None | firecrawl, firecrawl | `map` `scrape` `status` firecrawl | 0/2 |
| a1 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a2 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |
| a3 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl firecrawl-search | 0/2 |
| a4 |  None | firecrawl, firecrawl | `map` `scrape` `search` `status` firecrawl firecrawl-agent | 0/2 |
| a5 |  None | firecrawl, firecrawl | `scrape` `search` `status` firecrawl | 0/2 |

## Tool calls

Across 30 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 607 | 30 | 20.23 |
| `Skill` | 36 | 30 | 1.20 |
| `Agent` | 11 | 2 | 0.37 |
| `Read` | 6 | 2 | 0.20 |
| `TaskStop` | 1 | 1 | 0.03 |
| `ToolSearch` | 1 | 1 | 0.03 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 32 | 27 | 1.07 |
| `firecrawl-agent` | 1 | 1 | 0.03 |
| `firecrawl-download` | 1 | 1 | 0.03 |
| `firecrawl-scrape` | 1 | 1 | 0.03 |
| `firecrawl-search` | 1 | 1 | 0.03 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-crawl` | 0 | 0 | 0.00 |
| `firecrawl-developer-index` | 0 | 0 | 0.00 |
| `firecrawl-interact` | 0 | 0 | 0.00 |
| `firecrawl-map` | 0 | 0 | 0.00 |
| `firecrawl-monitor` | 0 | 0 | 0.00 |
| `firecrawl-parse` | 0 | 0 | 0.00 |
| `firecrawl-research-index` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 253 | 29 | 8.43 |
| `firecrawl search` | 79 | 20 | 2.63 |
| `firecrawl interact` | 38 | 5 | 1.27 |
| `firecrawl status` | 30 | 26 | 1.00 |
| `firecrawl map` | 14 | 10 | 0.47 |
| `firecrawl list` | 2 | 1 | 0.07 |
| `firecrawl (bare)` | 1 | 1 | 0.03 |
| `firecrawl find-tools` | 1 | 1 | 0.03 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl crawl` | 0 | 0 | 0.00 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |


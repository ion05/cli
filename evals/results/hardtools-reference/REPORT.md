# hardtools eval: reference

Skills `660ddb7` · model `claude-opus-5-5` · 1 trials · max 250 turns · Firecrawl key: True · 2.1.306 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 0% (0/24) |
| Runs that used Firecrawl | 92% (22/24) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/24) |
| Mean tool calls | 33.8 |
| Mean model cost (USD) | 1.332 |
| Mean duration (s) | 240 |

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
| n1 |  None | other-shell | - | 0/1 |
| n2 |  None | firecrawl | `scrape` `status` firecrawl | 0/1 |
| n3 |  None | firecrawl | `scrape` firecrawl-scrape | 0/1 |
| n4 |  None | firecrawl | `map` `scrape` firecrawl-map | 0/1 |
| n5 |  None | firecrawl | `scrape` `search` `status` firecrawl | 0/1 |
| n6 |  None | firecrawl | `scrape` `search` `status` firecrawl | 0/1 |
| n7 |  None | firecrawl | `scrape` `status` firecrawl | 0/1 |
| n8 |  None | firecrawl | `map` `scrape` firecrawl-map | 0/1 |

## Tool calls

Across 24 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 752 | 24 | 31.33 |
| `Skill` | 32 | 22 | 1.33 |
| `Agent` | 24 | 4 | 1.00 |
| `Monitor` | 1 | 1 | 0.04 |
| `Read` | 1 | 1 | 0.04 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 21 | 18 | 0.88 |
| `firecrawl-scrape` | 7 | 3 | 0.29 |
| `firecrawl-map` | 2 | 2 | 0.08 |
| `firecrawl-search` | 2 | 1 | 0.08 |
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
| `firecrawl scrape` | 350 | 22 | 14.58 |
| `firecrawl search` | 67 | 10 | 2.79 |
| `firecrawl interact` | 60 | 6 | 2.50 |
| `firecrawl map` | 36 | 8 | 1.50 |
| `firecrawl status` | 17 | 17 | 0.71 |
| `firecrawl agent` | 2 | 1 | 0.08 |
| `firecrawl web` | 2 | 1 | 0.08 |
| `firecrawl parse` | 1 | 1 | 0.04 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl crawl` | 0 | 0 | 0.00 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |


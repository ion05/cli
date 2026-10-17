# natural eval: pr4

Skills `729e12b` · model `claude-sonnet-5-5` · 3 trials · max 20 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 97% (111/114) |
| Runs that used Firecrawl | 59% (67/114) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/114) |
| Mean tool calls | 1.6 |
| Mean model cost (USD) | 0.063 |
| Mean duration (s) | 10 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| n01 |  None | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 3/3 |
| n02 |  None | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| n03 |  None | none, none, none | - | 3/3 |
| n04 |  None | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape firecrawl-search | 3/3 |
| n05 |  None | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| n06 |  None | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 3/3 |
| n07 |  None | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| n08 |  None | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| n09 |  None | other-shell, firecrawl, other-shell | `scrape` `search` firecrawl-search | 3/3 |
| n10 |  None | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` firecrawl-search | 3/3 |
| n11 |  None | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| n12 |  None | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| n13 |  None | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 3/3 |
| n14 |  None | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| n15 |  None | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| n16 |  None | none, none, none | - | 3/3 |
| n17 |  None | none, none, none | - | 3/3 |
| n18 |  None | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 3/3 |
| n19 |  None | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| n20 |  None | firecrawl, firecrawl, firecrawl | firecrawl-search | 0/3 |
| n21 |  None | none, none, none | - | 3/3 |
| n22 |  None | firecrawl, firecrawl, firecrawl | `search` firecrawl-search | 3/3 |
| n23 |  None | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-scrape firecrawl-search | 3/3 |
| n24 |  None | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-search | 3/3 |
| n25 |  None | none, none, none | - | 3/3 |
| n26 |  None | none, none, none | - | 3/3 |
| n27 |  None | none, none, none | - | 3/3 |
| n28 |  None | none, none, none | - | 3/3 |
| n29 |  None | none, none, none | - | 3/3 |
| n30 |  None | none, none, none | - | 3/3 |
| n31 |  None | none, none, none | - | 3/3 |
| n32 |  None | none, none, none | - | 3/3 |
| n33 |  None | none, none, none | - | 3/3 |
| n34 |  None | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape | 3/3 |
| n35 |  None | none, none, none | - | 3/3 |
| n36 |  None | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape firecrawl-search | 3/3 |
| n37 |  None | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search | 3/3 |
| n38 |  None | none, none, none | - | 3/3 |

## Tool calls

Across 114 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 100 | 66 | 0.88 |
| `Skill` | 73 | 73 | 0.64 |
| `Read` | 4 | 4 | 0.04 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-search` | 59 | 59 | 0.52 |
| `firecrawl-scrape` | 8 | 8 | 0.07 |
| `claude-api` | 6 | 6 | 0.05 |
| `firecrawl` | 0 | 0 | 0.00 |
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
| `firecrawl search` | 52 | 49 | 0.46 |
| `firecrawl scrape` | 29 | 24 | 0.25 |
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


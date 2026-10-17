# natural eval: original

Skills `22358f2` · model `claude-sonnet-5-5` · 3 trials · max 20 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 96% (110/114) |
| Runs that used Firecrawl | 2% (2/114) |
| Runs that used built-in WebSearch/WebFetch | 57% (65/114) |
| Mean tool calls | 1.4 |
| Mean model cost (USD) | 0.055 |
| Mean duration (s) | 10 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| n01 |  None | native, native, native | - | 3/3 |
| n02 |  None | native, other-shell, other-shell | - | 3/3 |
| n03 |  None | none, none, none | - | 3/3 |
| n04 |  None | native, native, native | - | 3/3 |
| n05 |  None | other-shell, native, native | - | 3/3 |
| n06 |  None | native, native, native | - | 2/3 |
| n07 |  None | native, native, native | - | 3/3 |
| n08 |  None | native, native, native | - | 1/3 |
| n09 |  None | native, native, native | - | 2/3 |
| n10 |  None | native, native, native | - | 3/3 |
| n11 |  None | native, native, native | - | 3/3 |
| n12 |  None | native, native, native | - | 3/3 |
| n13 |  None | native, native, native | - | 3/3 |
| n14 |  None | native, native, native | - | 3/3 |
| n15 |  None | native, native, native | - | 3/3 |
| n16 |  None | none, none, none | - | 3/3 |
| n17 |  None | none, none, none | - | 3/3 |
| n18 |  None | native, native, native | - | 3/3 |
| n19 |  None | native, native, native | - | 3/3 |
| n20 |  None | native, native, native | - | 3/3 |
| n21 |  None | firecrawl, none, firecrawl | `scrape` firecrawl-scrape | 3/3 |
| n22 |  None | native, native, native | - | 3/3 |
| n23 |  None | none, native, native | - | 3/3 |
| n24 |  None | native, native, native | - | 3/3 |
| n25 |  None | none, none, none | - | 3/3 |
| n26 |  None | none, none, none | - | 3/3 |
| n27 |  None | none, none, none | - | 3/3 |
| n28 |  None | none, none, none | - | 3/3 |
| n29 |  None | none, none, none | - | 3/3 |
| n30 |  None | none, none, none | - | 3/3 |
| n31 |  None | none, none, none | - | 3/3 |
| n32 |  None | none, none, none | - | 3/3 |
| n33 |  None | none, none, none | - | 3/3 |
| n34 |  None | native, native, native | - | 3/3 |
| n35 |  None | none, none, none | - | 3/3 |
| n36 |  None | native, native, native | - | 3/3 |
| n37 |  None | native, native, native | - | 3/3 |
| n38 |  None | none, none, none | - | 3/3 |

## Tool calls

Across 114 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `ToolSearch` | 66 | 65 | 0.58 |
| `WebSearch` | 43 | 42 | 0.38 |
| `WebFetch` | 28 | 25 | 0.25 |
| `Bash` | 13 | 12 | 0.11 |
| `Skill` | 7 | 7 | 0.06 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `claude-api` | 6 | 6 | 0.05 |
| `firecrawl-scrape` | 1 | 1 | 0.01 |
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
| `firecrawl-search` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 2 | 2 | 0.02 |
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
| `firecrawl search` | 0 | 0 | 0.00 |


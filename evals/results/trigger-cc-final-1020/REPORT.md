# trigger eval: cc-final-1020

Skills `660ddb7` · model `claude-sonnet-5-5` · 3 trials · max 12 turns · Firecrawl key: True · 2.1.305 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Web tasks where Firecrawl was the first web tool | 78% (56/72) |
| Web tasks where Firecrawl was used at all | 78% (56/72) |
| Web tasks where built-in WebSearch/WebFetch came first | 15% (11/72) |
| Web tasks where another shell tool (curl, npm view, gh) came first | 3% (2/72) |
| Web tasks answered with no web tool | 4% (3/72) |
| Non-web tasks where Firecrawl fired (false trigger) | 0% (0/30) |
| Simple fetches (raw file, JSON API, status check) where Firecrawl was used | 25% (3/12) |

## Per prompt

| id | expect / intent | first web tool per trial | Firecrawl skills / commands |
|---|---|---|---|
| u01 | use search | firecrawl, firecrawl, firecrawl | `search` firecrawl-search |
| u02 | use search | firecrawl, firecrawl, firecrawl | `search` firecrawl-search |
| u03 | use search | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` firecrawl firecrawl-search |
| u04 | use search | firecrawl, firecrawl, firecrawl | `search` firecrawl-search |
| u05 | use scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape |
| u06 | use search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape |
| u07 | use search-news | firecrawl, firecrawl, native | `search` firecrawl-search |
| u08 | use crawl | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-crawl firecrawl-scrape |
| u09 | use map | native, native, native | - |
| u10 | use search | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl |
| u11 | use search | firecrawl, other-shell, other-shell | `alexandria` `scrape` `search` firecrawl-alexandria |
| u12 | use scrape | native, firecrawl, firecrawl | `scrape` firecrawl-scrape |
| u13 | use scrape | firecrawl, firecrawl, firecrawl | `find-tools` `scrape` `search` firecrawl-alexandria |
| u14 | use research-index | native, native, firecrawl | `research` firecrawl-research-index |
| u15 | use developer-index | firecrawl, firecrawl, firecrawl | `developer` firecrawl-developer-index |
| u16 | use search | native, firecrawl, native | `scrape` firecrawl-scrape |
| u17 | use monitor | firecrawl, firecrawl, firecrawl | firecrawl-monitor |
| u18 | use search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search |
| u19 | use search | firecrawl, firecrawl, firecrawl | `search` firecrawl-search |
| u20 | use interact | firecrawl, firecrawl, firecrawl | `scrape` firecrawl |
| u21 | use search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search |
| u22 | use agent | none, none, none | - |
| u23 | use search | firecrawl, native, native | `search` firecrawl-search |
| u24 | use scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape |
| a01 | avoid code | none, none, none | - |
| a02 | avoid knowledge | none, none, none | - |
| a03 | avoid code | none, none, none | - |
| a04 | avoid local-file | none, none, none | - |
| a05 | avoid local-file | none, none, none | - |
| a06 | avoid knowledge | none, none, none | - |
| a07 | avoid code | none, none, none | - |
| a08 | avoid knowledge | none, none, none | - |
| a09 | avoid code | none, none, none | - |
| a10 | avoid knowledge | none, none, none | - |
| n01 | either raw-fetch | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape |
| n02 | either api-call | other-shell, other-shell, other-shell | - |
| n03 | either raw-fetch | other-shell, other-shell, other-shell | - |
| n04 | either raw-fetch | other-shell, other-shell, other-shell | - |

## Tool calls

Across 114 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 141 | 67 | 1.24 |
| `Skill` | 59 | 59 | 0.52 |
| `ToolSearch` | 13 | 13 | 0.11 |
| `WebFetch` | 13 | 10 | 0.11 |
| `Read` | 12 | 11 | 0.11 |
| `WebSearch` | 8 | 7 | 0.07 |
| `Write` | 6 | 6 | 0.05 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-search` | 23 | 23 | 0.20 |
| `firecrawl-scrape` | 17 | 17 | 0.15 |
| `firecrawl` | 7 | 7 | 0.06 |
| `firecrawl-alexandria` | 4 | 4 | 0.04 |
| `firecrawl-developer-index` | 3 | 3 | 0.03 |
| `firecrawl-monitor` | 3 | 3 | 0.03 |
| `firecrawl-crawl` | 1 | 1 | 0.01 |
| `firecrawl-research-index` | 1 | 1 | 0.01 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-download` | 0 | 0 | 0.00 |
| `firecrawl-interact` | 0 | 0 | 0.00 |
| `firecrawl-map` | 0 | 0 | 0.00 |
| `firecrawl-parse` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 58 | 35 | 0.51 |
| `firecrawl search` | 29 | 25 | 0.25 |
| `firecrawl find-tools` | 2 | 2 | 0.02 |
| `firecrawl alexandria` | 1 | 1 | 0.01 |
| `firecrawl developer` | 1 | 1 | 0.01 |
| `firecrawl research` | 1 | 1 | 0.01 |
| `firecrawl search-feedback` | 1 | 1 | 0.01 |
| `firecrawl status` | 1 | 1 | 0.01 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl crawl` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl interact` | 0 | 0 | 0.00 |
| `firecrawl map` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |

**Firecrawl API endpoints called directly (curl)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `developer` | 3 | 2 | 0.03 |


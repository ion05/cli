# trigger eval: desc-v1

Skills `WORKTREE` · model `claude-sonnet-5-5` · 3 trials · max 8 turns · Firecrawl key: False · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Web tasks where Firecrawl was the first web tool | 85% (61/72) |
| Web tasks where Firecrawl was used at all | 85% (61/72) |
| Web tasks where built-in WebSearch/WebFetch came first | 1% (1/72) |
| Web tasks where another shell tool (curl, npm view, gh) came first | 10% (7/72) |
| Web tasks answered with no web tool | 4% (3/72) |
| Non-web tasks where Firecrawl fired (false trigger) | 0% (0/30) |
| Simple fetches (raw file, JSON API, status check) where Firecrawl was used | 0% (0/12) |

## Per prompt

| id | expect / intent | first web tool per trial | Firecrawl skills / commands |
|---|---|---|---|
| u01 | use search | other-shell, firecrawl, other-shell | `search` firecrawl-search |
| u02 | use search | firecrawl, firecrawl, firecrawl | `search` firecrawl-search |
| u03 | use search | firecrawl, firecrawl, firecrawl | `scrape` `search` `status` firecrawl firecrawl-search |
| u04 | use search | firecrawl, firecrawl, firecrawl | `search` firecrawl-search |
| u05 | use scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape |
| u06 | use search | firecrawl, firecrawl, firecrawl | `scrape` `search` `status` firecrawl-scrape firecrawl-search |
| u07 | use search-news | firecrawl, firecrawl, firecrawl | `search` firecrawl-search |
| u08 | use crawl | firecrawl, firecrawl, firecrawl | `map` `scrape` firecrawl firecrawl-scrape |
| u09 | use map | firecrawl, native, firecrawl | `map` `search` firecrawl-map firecrawl-search |
| u10 | use search | firecrawl, firecrawl, firecrawl | `scrape` `search` `status` firecrawl firecrawl-search |
| u11 | use search | other-shell, other-shell, other-shell | - |
| u12 | use scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape |
| u13 | use scrape | other-shell, other-shell, firecrawl | `scrape` firecrawl-scrape |
| u14 | use research-index | firecrawl, firecrawl, firecrawl | `research` `status` firecrawl-research-index |
| u15 | use developer-index | firecrawl, firecrawl, firecrawl | `developer` firecrawl-developer-index |
| u16 | use search | firecrawl, firecrawl, firecrawl | `scrape` `search` `status` firecrawl firecrawl-scrape |
| u17 | use monitor | firecrawl, firecrawl, firecrawl | firecrawl-monitor |
| u18 | use search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search |
| u19 | use search | firecrawl, firecrawl, firecrawl | `search` firecrawl-search |
| u20 | use interact | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl |
| u21 | use search | firecrawl, firecrawl, firecrawl | `search` firecrawl-search |
| u22 | use agent | none, none, none | - |
| u23 | use search | firecrawl, firecrawl, firecrawl | `search` firecrawl-search |
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
| n01 | either raw-fetch | other-shell, other-shell, other-shell | - |
| n02 | either api-call | other-shell, other-shell, other-shell | - |
| n03 | either raw-fetch | other-shell, other-shell, other-shell | - |
| n04 | either raw-fetch | other-shell, other-shell, other-shell | - |

## Tool calls

Across 114 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `Bash` | 147 | 77 | 1.29 |
| `ToolSearch` | 63 | 60 | 0.55 |
| `Skill` | 61 | 61 | 0.54 |
| `WebSearch` | 60 | 45 | 0.53 |
| `WebFetch` | 53 | 41 | 0.46 |
| `Read` | 6 | 6 | 0.05 |
| `Write` | 5 | 5 | 0.04 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-search` | 27 | 27 | 0.24 |
| `firecrawl-scrape` | 15 | 15 | 0.13 |
| `firecrawl` | 9 | 9 | 0.08 |
| `firecrawl-developer-index` | 3 | 3 | 0.03 |
| `firecrawl-monitor` | 3 | 3 | 0.03 |
| `firecrawl-research-index` | 3 | 3 | 0.03 |
| `firecrawl-map` | 1 | 1 | 0.01 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-crawl` | 0 | 0 | 0.00 |
| `firecrawl-download` | 0 | 0 | 0.00 |
| `firecrawl-interact` | 0 | 0 | 0.00 |
| `firecrawl-parse` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl search` | 58 | 29 | 0.51 |
| `firecrawl scrape` | 33 | 24 | 0.29 |
| `firecrawl status` | 11 | 11 | 0.10 |
| `firecrawl research` | 5 | 3 | 0.04 |
| `firecrawl developer` | 3 | 3 | 0.03 |
| `firecrawl map` | 3 | 3 | 0.03 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl crawl` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl interact` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |

**Firecrawl API endpoints called directly (curl)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `developer` | 6 | 3 | 0.05 |


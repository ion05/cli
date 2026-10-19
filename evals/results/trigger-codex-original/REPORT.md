# trigger eval: codex-original

Skills `22358f2` · model `(codex default)` · 3 trials · max n/a turns · Firecrawl key: True · codex-cli 0.163.0

## Headline

| Metric | Value |
|---|---|
| Web tasks where Firecrawl was the first web tool | 99% (71/72) |
| Web tasks where Firecrawl was used at all | 99% (71/72) |
| Web tasks where built-in WebSearch/WebFetch came first | 1% (1/72) |
| Web tasks where another shell tool (curl, npm view, gh) came first | 0% (0/72) |
| Web tasks answered with no web tool | 0% (0/72) |
| Non-web tasks where Firecrawl fired (false trigger) | 0% (0/30) |
| Simple fetches (raw file, JSON API, status check) where Firecrawl was used | 83% (10/12) |

## Per prompt

| id | expect / intent | first web tool per trial | Firecrawl skills / commands |
|---|---|---|---|
| u01 | use search | firecrawl, firecrawl, firecrawl | `list` `scrape` `search-feedback` `search` firecrawl firecrawl-scrape firecrawl-search |
| u02 | use search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape |
| u03 | use search | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape firecrawl-search |
| u04 | use search | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` `status` firecrawl firecrawl-scrape firecrawl-search |
| u05 | use scrape | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape |
| u06 | use search | firecrawl, firecrawl, firecrawl | `developer` `scrape` `status` firecrawl firecrawl-developer-index firecrawl-scrape |
| u07 | use search-news | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` `status` firecrawl firecrawl-scrape firecrawl-search |
| u08 | use crawl | firecrawl, firecrawl, firecrawl | `crawl` `scrape` `status` firecrawl firecrawl-crawl firecrawl-scrape |
| u09 | use map | firecrawl, firecrawl, firecrawl | `search-feedback` `search` firecrawl-search |
| u10 | use search | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` `status` firecrawl firecrawl-scrape firecrawl-search |
| u11 | use search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape |
| u12 | use scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape |
| u13 | use scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape |
| u14 | use research-index | firecrawl, firecrawl, firecrawl | `research` firecrawl-research-index |
| u15 | use developer-index | firecrawl, firecrawl, firecrawl | `developer` `scrape` firecrawl-developer-index |
| u16 | use search | firecrawl, native, firecrawl | `search` firecrawl |
| u17 | use monitor | firecrawl, firecrawl, firecrawl | `monitor` firecrawl-monitor |
| u18 | use search | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape |
| u19 | use search | firecrawl, firecrawl, firecrawl | `search-feedback` `search` `status` firecrawl firecrawl-search |
| u20 | use interact | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape |
| u21 | use search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape |
| u22 | use agent | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape firecrawl-search |
| u23 | use search | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` `status` firecrawl firecrawl-scrape firecrawl-search |
| u24 | use scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape |
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
| n01 | either raw-fetch | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape |
| n02 | either api-call | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape |
| n03 | either raw-fetch | firecrawl, other-shell, other-shell | `scrape` firecrawl firecrawl-scrape |
| n04 | either raw-fetch | firecrawl, firecrawl, firecrawl | firecrawl |

## Tool calls

Across 114 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `shell` | 589 | 90 | 5.17 |
| `web_search` | 6 | 4 | 0.05 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 68 | 68 | 0.60 |
| `firecrawl-scrape` | 59 | 59 | 0.52 |
| `firecrawl-search` | 19 | 19 | 0.17 |
| `firecrawl-developer-index` | 5 | 5 | 0.04 |
| `firecrawl-monitor` | 3 | 3 | 0.03 |
| `firecrawl-research-index` | 3 | 3 | 0.03 |
| `firecrawl-crawl` | 2 | 2 | 0.02 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-download` | 0 | 0 | 0.00 |
| `firecrawl-interact` | 0 | 0 | 0.00 |
| `firecrawl-map` | 0 | 0 | 0.00 |
| `firecrawl-parse` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 147 | 62 | 1.29 |
| `firecrawl status` | 24 | 24 | 0.21 |
| `firecrawl search` | 23 | 18 | 0.20 |
| `firecrawl search-feedback` | 20 | 16 | 0.18 |
| `firecrawl research` | 15 | 3 | 0.13 |
| `firecrawl developer` | 11 | 5 | 0.10 |
| `firecrawl monitor` | 5 | 3 | 0.04 |
| `firecrawl crawl` | 4 | 2 | 0.04 |
| `firecrawl list` | 1 | 1 | 0.01 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl interact` | 0 | 0 | 0.00 |
| `firecrawl map` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |

**Firecrawl API endpoints called directly (curl)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `developer` | 2 | 2 | 0.02 |


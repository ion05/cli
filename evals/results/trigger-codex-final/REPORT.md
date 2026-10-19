# trigger eval: codex-final

Skills `660ddb7` · model `(codex default)` · 3 trials · max n/a turns · Firecrawl key: True · codex-cli 0.163.0

## Headline

| Metric | Value |
|---|---|
| Web tasks where Firecrawl was the first web tool | 100% (72/72) |
| Web tasks where Firecrawl was used at all | 100% (72/72) |
| Web tasks where built-in WebSearch/WebFetch came first | 0% (0/72) |
| Web tasks where another shell tool (curl, npm view, gh) came first | 0% (0/72) |
| Web tasks answered with no web tool | 0% (0/72) |
| Non-web tasks where Firecrawl fired (false trigger) | 0% (0/30) |
| Simple fetches (raw file, JSON API, status check) where Firecrawl was used | 100% (12/12) |

## Per prompt

| id | expect / intent | first web tool per trial | Firecrawl skills / commands |
|---|---|---|---|
| u01 | use search | firecrawl, firecrawl, firecrawl | `list` `scrape` `search-feedback` `search` firecrawl-search |
| u02 | use search | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` firecrawl firecrawl-scrape firecrawl-search |
| u03 | use search | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` firecrawl firecrawl-scrape firecrawl-search |
| u04 | use search | firecrawl, firecrawl, firecrawl | `search-feedback` `search` `status` firecrawl firecrawl-search |
| u05 | use scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape |
| u06 | use search | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` firecrawl firecrawl-scrape firecrawl-search |
| u07 | use search-news | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` firecrawl-scrape firecrawl-search |
| u08 | use crawl | firecrawl, firecrawl, firecrawl | `crawl` `scrape` `status` firecrawl firecrawl-crawl |
| u09 | use map | firecrawl, firecrawl, firecrawl | `map` `scrape` firecrawl-map firecrawl-scrape |
| u10 | use search | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` `status` firecrawl firecrawl-scrape firecrawl-search |
| u11 | use search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape |
| u12 | use scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape |
| u13 | use scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape |
| u14 | use research-index | firecrawl, firecrawl, firecrawl | `research` firecrawl-research-index |
| u15 | use developer-index | firecrawl, firecrawl, firecrawl | `developer` firecrawl-developer-index |
| u16 | use search | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` firecrawl firecrawl-scrape firecrawl-search |
| u17 | use monitor | firecrawl, firecrawl, firecrawl | `monitor` firecrawl-monitor |
| u18 | use search | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` `status` firecrawl firecrawl-scrape firecrawl-search |
| u19 | use search | firecrawl, firecrawl, firecrawl | `search-feedback` `search` firecrawl-search |
| u20 | use interact | firecrawl, firecrawl, firecrawl | `interact` `scrape` firecrawl firecrawl-interact firecrawl-scrape |
| u21 | use search | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` firecrawl firecrawl-scrape firecrawl-search |
| u22 | use agent | firecrawl, firecrawl, firecrawl | `list` `scrape` `search-feedback` `search` firecrawl-scrape firecrawl-search |
| u23 | use search | firecrawl, firecrawl, firecrawl | `search-feedback` `search` firecrawl firecrawl-scrape firecrawl-search |
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
| n01 | either raw-fetch | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape |
| n02 | either api-call | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape |
| n03 | either raw-fetch | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape |
| n04 | either raw-fetch | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape |

## Tool calls

Across 114 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `shell` | 544 | 90 | 4.77 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-scrape` | 50 | 50 | 0.44 |
| `firecrawl` | 36 | 36 | 0.32 |
| `firecrawl-search` | 32 | 32 | 0.28 |
| `firecrawl-crawl` | 3 | 3 | 0.03 |
| `firecrawl-developer-index` | 3 | 3 | 0.03 |
| `firecrawl-interact` | 3 | 3 | 0.03 |
| `firecrawl-map` | 3 | 3 | 0.03 |
| `firecrawl-monitor` | 3 | 3 | 0.03 |
| `firecrawl-research-index` | 3 | 3 | 0.03 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-download` | 0 | 0 | 0.00 |
| `firecrawl-parse` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 90 | 57 | 0.79 |
| `firecrawl search` | 47 | 31 | 0.41 |
| `firecrawl search-feedback` | 36 | 28 | 0.32 |
| `firecrawl interact` | 16 | 3 | 0.14 |
| `firecrawl research` | 16 | 3 | 0.14 |
| `firecrawl status` | 7 | 7 | 0.06 |
| `firecrawl developer` | 6 | 3 | 0.05 |
| `firecrawl monitor` | 6 | 3 | 0.05 |
| `firecrawl crawl` | 5 | 3 | 0.04 |
| `firecrawl list` | 4 | 4 | 0.04 |
| `firecrawl map` | 3 | 3 | 0.03 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |


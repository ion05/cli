# trigger eval: baseline-key

Skills `22358f2` · model `claude-sonnet-5-5` · 3 trials · max 8 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Web tasks where Firecrawl was the first web tool | 6% (4/72) |
| Web tasks where Firecrawl was used at all | 6% (4/72) |
| Web tasks where built-in WebSearch/WebFetch came first | 86% (62/72) |
| Web tasks where another shell tool (curl, npm view, gh) came first | 4% (3/72) |
| Web tasks answered with no web tool | 4% (3/72) |
| Non-web tasks where Firecrawl fired (false trigger) | 0% (0/30) |
| Simple fetches (raw file, JSON API, status check) where Firecrawl was used | 0% (0/12) |

## Per prompt

| id | expect / intent | first web tool per trial | Firecrawl skills / commands |
|---|---|---|---|
| u01 | use search | native, native, native | - |
| u02 | use search | native, native, native | - |
| u03 | use search | native, native, native | - |
| u04 | use search | native, native, native | - |
| u05 | use scrape | native, native, native | - |
| u06 | use search | native, native, native | - |
| u07 | use search-news | native, native, native | - |
| u08 | use crawl | native, native, native | - |
| u09 | use map | native, native, native | - |
| u10 | use search | native, native, native | - |
| u11 | use search | other-shell, other-shell, other-shell | - |
| u12 | use scrape | native, native, native | - |
| u13 | use scrape | native, native, native | - |
| u14 | use research-index | firecrawl, native, native | `research` firecrawl-research-index |
| u15 | use developer-index | native, native, native | - |
| u16 | use search | native, native, native | - |
| u17 | use monitor | firecrawl, firecrawl, firecrawl | firecrawl-monitor |
| u18 | use search | native, native, native | - |
| u19 | use search | native, native, native | - |
| u20 | use interact | native, native, native | - |
| u21 | use search | native, native, native | - |
| u22 | use agent | none, none, none | - |
| u23 | use search | native, native, native | - |
| u24 | use scrape | native, native, native | - |
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
| n01 | either raw-fetch | other-shell, native, native | - |
| n02 | either api-call | other-shell, other-shell, other-shell | - |
| n03 | either raw-fetch | other-shell, other-shell, other-shell | - |
| n04 | either raw-fetch | other-shell, other-shell, other-shell | - |

## Tool calls

Across 114 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `WebFetch` | 130 | 45 | 1.14 |
| `ToolSearch` | 70 | 67 | 0.61 |
| `WebSearch` | 42 | 33 | 0.37 |
| `Bash` | 33 | 19 | 0.29 |
| `Read` | 6 | 6 | 0.05 |
| `Skill` | 4 | 4 | 0.04 |
| `Write` | 4 | 4 | 0.04 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-monitor` | 3 | 3 | 0.03 |
| `firecrawl-research-index` | 1 | 1 | 0.01 |
| `firecrawl` | 0 | 0 | 0.00 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-crawl` | 0 | 0 | 0.00 |
| `firecrawl-developer-index` | 0 | 0 | 0.00 |
| `firecrawl-download` | 0 | 0 | 0.00 |
| `firecrawl-interact` | 0 | 0 | 0.00 |
| `firecrawl-map` | 0 | 0 | 0.00 |
| `firecrawl-parse` | 0 | 0 | 0.00 |
| `firecrawl-scrape` | 0 | 0 | 0.00 |
| `firecrawl-search` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl research` | 1 | 1 | 0.01 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl crawl` | 0 | 0 | 0.00 |
| `firecrawl developer` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl interact` | 0 | 0 | 0.00 |
| `firecrawl map` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |
| `firecrawl scrape` | 0 | 0 | 0.00 |
| `firecrawl search` | 0 | 0 | 0.00 |


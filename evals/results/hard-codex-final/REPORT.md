# hard eval: codex-final

Skills `660ddb7` · model `(codex default)` · 3 trials · max n/a turns · Firecrawl key: True · codex-cli 0.163.0

## Headline

| Metric | Value |
|---|---|
| Correct answers | 100% (24/24) |
| Runs that used Firecrawl | 100% (24/24) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/24) |
| Mean tool calls | 3.7 |
| Mean model cost (USD) | 0.030 |
| Mean duration (s) | 17 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| h01 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` firecrawl firecrawl-scrape firecrawl-search | 3/3 |
| h02 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` firecrawl firecrawl-scrape firecrawl-search | 3/3 |
| h03 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |
| h04 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |
| h05 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-developer-index firecrawl-scrape | 3/3 |
| h06 |  search | firecrawl, firecrawl, firecrawl | `search-feedback` `search` firecrawl-search | 3/3 |
| h07 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` `status` firecrawl firecrawl-scrape firecrawl-search | 3/3 |
| h08 |  scrape | firecrawl, firecrawl, firecrawl | `search-feedback` `search` firecrawl-search | 3/3 |

## Tool calls

Across 24 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `shell` | 88 | 24 | 3.67 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl-scrape` | 12 | 12 | 0.50 |
| `firecrawl-search` | 12 | 12 | 0.50 |
| `firecrawl` | 11 | 11 | 0.46 |
| `firecrawl-developer-index` | 2 | 2 | 0.08 |
| `firecrawl-agent` | 0 | 0 | 0.00 |
| `firecrawl-alexandria` | 0 | 0 | 0.00 |
| `firecrawl-crawl` | 0 | 0 | 0.00 |
| `firecrawl-download` | 0 | 0 | 0.00 |
| `firecrawl-interact` | 0 | 0 | 0.00 |
| `firecrawl-map` | 0 | 0 | 0.00 |
| `firecrawl-monitor` | 0 | 0 | 0.00 |
| `firecrawl-parse` | 0 | 0 | 0.00 |
| `firecrawl-research-index` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl scrape` | 15 | 13 | 0.62 |
| `firecrawl search` | 12 | 12 | 0.50 |
| `firecrawl search-feedback` | 11 | 11 | 0.46 |
| `firecrawl status` | 2 | 2 | 0.08 |
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


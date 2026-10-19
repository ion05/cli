# hard eval: codex-original

Skills `22358f2` · model `(codex default)` · 3 trials · max n/a turns · Firecrawl key: True · codex-cli 0.163.0

## Headline

| Metric | Value |
|---|---|
| Correct answers | 75% (18/24) |
| Runs that used Firecrawl | 100% (24/24) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/24) |
| Mean tool calls | 4.0 |
| Mean model cost (USD) | 0.028 |
| Mean duration (s) | 15 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| h01 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |
| h02 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |
| h03 |  search | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape | 0/3 |
| h04 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |
| h05 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` `status` firecrawl firecrawl-scrape | 0/3 |
| h06 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search-feedback` `search` firecrawl firecrawl-search | 3/3 |
| h07 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` firecrawl firecrawl-scrape | 3/3 |
| h08 |  scrape | firecrawl, firecrawl, firecrawl | `developer` `scrape` firecrawl firecrawl-developer-index firecrawl-scrape | 3/3 |

## Tool calls

Across 24 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `shell` | 97 | 24 | 4.04 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 23 | 23 | 0.96 |
| `firecrawl-scrape` | 18 | 18 | 0.75 |
| `firecrawl-search` | 3 | 3 | 0.12 |
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
| `firecrawl scrape` | 21 | 21 | 0.88 |
| `firecrawl search` | 3 | 3 | 0.12 |
| `firecrawl search-feedback` | 3 | 3 | 0.12 |
| `firecrawl status` | 3 | 3 | 0.12 |
| `firecrawl developer` | 2 | 2 | 0.08 |
| `firecrawl agent` | 0 | 0 | 0.00 |
| `firecrawl alexandria` | 0 | 0 | 0.00 |
| `firecrawl crawl` | 0 | 0 | 0.00 |
| `firecrawl download` | 0 | 0 | 0.00 |
| `firecrawl interact` | 0 | 0 | 0.00 |
| `firecrawl map` | 0 | 0 | 0.00 |
| `firecrawl monitor` | 0 | 0 | 0.00 |
| `firecrawl parse` | 0 | 0 | 0.00 |
| `firecrawl research` | 0 | 0 | 0.00 |


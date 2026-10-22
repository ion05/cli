# heldout eval: codex-native-1022

Skills `NONE` · model `(codex default)` · 3 trials · max n/a turns · Firecrawl key: False · codex-cli 0.163.0

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 0% (0/108) |
| Runs that used Firecrawl | 2% (2/108) |
| Runs that used built-in WebSearch/WebFetch | 92% (99/108) |
| Mean tool calls | 5.3 |
| Mean model cost (USD) | 0.050 |
| Mean duration (s) | 29 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| crawl | 0/12 | 0/12 | 0/12 | - | - |
| map | 0/12 | 0/12 | 0/12 | - | - |
| agent | 0/15 | 0/15 | 0/15 | - | - |
| parse | 0/9 | 0/9 | 0/9 | - | - |
| alexandria | 0/6 | 0/6 | 0/6 | - | - |
| scrape | 0/21 | 0/21 | 1/21 | - | - |
| search | 0/12 | 0/12 | 1/12 | - | - |
| interact | 0/9 | 0/9 | 0/9 | - | - |
| developer | 0/6 | 0/6 | 0/6 | - | - |
| research | 0/3 | 0/3 | 0/3 | - | - |
| download | 0/3 | 0/3 | 0/3 | - | - |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| h01 |  crawl | native, native, native | - | 0/3 |  |
| h02 |  crawl | native, native, native | - | 0/3 |  |
| h03 |  agent | native, native, native | - | 0/3 |  |
| h04 |  agent | native, native, native | - | 0/3 |  |
| h05 |  map | native, native, native | - | 0/3 |  |
| h06 |  map | native, native, native | - | 0/3 |  |
| h07 |  parse | none, none, none | - | 0/3 |  |
| h08 |  alexandria | native, native, native | - | 0/3 |  |
| h09 |  scrape | native, native, native | - | 0/3 |  |
| h10 |  scrape | native, native, native | - | 0/3 |  |
| h11 |  search | native, native, native | - | 0/3 |  |
| h12 |  scrape | native, native, native | - | 0/3 |  |
| h13 |  search | native, native, native | - | 0/3 |  |
| h14 |  search | firecrawl, native, native | firecrawl | 0/3 |  |
| h15 |  scrape | native, native, native | - | 0/3 |  |
| h16 |  scrape | firecrawl, native, native | firecrawl | 0/3 |  |
| h17 |  map | native, native, native | - | 0/3 |  |
| h18 |  map | native, native, native | - | 0/3 |  |
| h19 |  crawl | native, native, native | - | 0/3 |  |
| h20 |  crawl | native, native, native | - | 0/3 |  |
| h21 |  agent | native, native, native | - | 0/3 |  |
| h22 |  agent | native, native, native | - | 0/3 |  |
| h23 |  agent | native, native, native | - | 0/3 |  |
| h24 |  interact | native, native, native | - | 0/3 |  |
| h25 |  interact | native, native, native | - | 0/3 |  |
| h26 |  interact | native, none, native | - | 0/3 |  |
| h27 |  parse | none, none, none | - | 0/3 |  |
| h28 |  parse | native, native, native | - | 0/3 |  |
| h29 |  download | native, native, native | - | 0/3 |  |
| h30 |  research | native, native, native | - | 0/3 |  |
| h31 |  developer | native, native, native | - | 0/3 |  |
| h32 |  developer | native, other-shell, other-shell | - | 0/3 |  |
| h33 |  alexandria | native, native, native | - | 0/3 |  |
| h34 |  scrape | native, native, native | - | 0/3 |  |
| h35 |  search | native, native, native | - | 0/3 |  |
| h36 |  scrape | native, native, native | - | 0/3 |  |

## Tool calls

Across 108 runs. *Runs* = runs that called it at least once.

**All tool calls (Claude Code tools; `Skill` = any skill load, `Bash` includes Firecrawl CLI calls)**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `web_search` | 434 | 99 | 4.02 |
| `shell` | 140 | 35 | 1.30 |

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
| `firecrawl` | 2 | 2 | 0.02 |
| `read-docs` | 1 | 1 | 0.01 |
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
| `firecrawl-scrape` | 0 | 0 | 0.00 |
| `firecrawl-search` | 0 | 0 | 0.00 |

**Firecrawl CLI commands run in Bash**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
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
| `firecrawl scrape` | 0 | 0 | 0.00 |
| `firecrawl search` | 0 | 0 | 0.00 |


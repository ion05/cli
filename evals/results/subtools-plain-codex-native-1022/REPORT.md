# subtools-plain eval: codex-native-1022

Skills `NONE` · model `(codex default)` · 3 trials · max n/a turns · Firecrawl key: False · codex-cli 0.163.0

## Headline

| Metric | Value |
|---|---|
| Ran the expected Firecrawl command | 0% (0/12) |
| Runs that used Firecrawl | 0% (0/12) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/12) |
| Mean tool calls | 0.0 |
| Mean model cost (USD) | 0.000 |
| Mean duration (s) | 4 |

## Per subtool

Each prompt asks for a job one Firecrawl command is built for, without naming the command (the `subtools` suite says "use Firecrawl", `subtools-plain` doesn't mention it). *Ran it* also counts a curl to the same API endpoint, and for monitor, loading the skill (it then has to ask for an alert address before it can create one).

| Intended subtool | Ran it | Loaded its skill | Used Firecrawl at all | Commands actually run | Other web tools |
|---|---|---|---|---|---|
| search | 0/2 | 0/2 | 0/2 | - | - |
| scrape | 0/2 | 0/2 | 0/2 | - | - |
| map | 0/2 | 0/2 | 0/2 | - | - |
| crawl | 0/2 | 0/2 | 0/2 | - | - |
| agent | 0/2 | 0/2 | 0/2 | - | - |
| interact | 0/2 | 0/2 | 0/2 | - | - |

## Per task

| id | intent | first web tool per trial | Firecrawl skills / commands | ran it | note |
|---|---|---|---|---|---|
| s01 |  search | none | - | 0/1 |  |
| s02 |  search | none | - | 0/1 |  |
| s03 |  scrape | none | - | 0/1 |  |
| s04 |  scrape | none | - | 0/1 |  |
| s05 |  map | none | - | 0/1 |  |
| s06 |  map | none | - | 0/1 |  |
| s07 |  crawl | none | - | 0/1 |  |
| s08 |  crawl | none | - | 0/1 |  |
| s09 |  agent | none | - | 0/1 | Agent case: unknown pages across many sites, dozens of records. Replaces the told-suite pricing prompt (one known page, where scrape is right). |
| s10 |  agent | none | - | 0/1 |  |
| s11 |  interact | none | - | 0/1 | Login form on a public test site. Replaces the HN 'new' link prompt, which agents answered by fetching /newest directly. |
| s12 |  interact | none | - | 0/1 |  |

## Tool calls

Across 12 runs. *Runs* = runs that called it at least once.

**Firecrawl skills loaded**

| Tool | Calls | Runs | Calls per run |
|---|---|---|---|
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


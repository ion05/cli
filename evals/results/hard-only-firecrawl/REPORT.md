# hard eval: only-firecrawl

Skills `22358f2` · model `claude-sonnet-5-5` · 3 trials · max 20 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 88% (21/24) |
| Runs that used Firecrawl | 100% (24/24) |
| Runs that used built-in WebSearch/WebFetch | 0% (0/24) |
| Mean tool calls | 4.8 |
| Mean model cost (USD) | 0.073 |
| Mean duration (s) | 43 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| h01 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl firecrawl-search |
| h02 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl firecrawl-scrape firecrawl-search |
| h03 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl |
| h04 |  search | firecrawl, firecrawl, firecrawl | `scrape` firecrawl-scrape |
| h05 |  scrape | firecrawl, firecrawl, firecrawl | `developer` `scrape` firecrawl firecrawl-developer-index |
| h06 |  search | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl-search |
| h07 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl firecrawl-search |
| h08 |  scrape | firecrawl, firecrawl, firecrawl | `scrape` `search` firecrawl |

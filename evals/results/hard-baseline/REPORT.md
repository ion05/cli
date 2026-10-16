# hard eval: baseline

Skills `22358f2` · model `claude-sonnet-5-5` · 3 trials · max 20 turns · Firecrawl key: True · 2.1.302 (Claude Code)

## Headline

| Metric | Value |
|---|---|
| Correct answers | 96% (23/24) |
| Runs that used Firecrawl | 8% (2/24) |
| Runs that used built-in WebSearch/WebFetch | 71% (17/24) |
| Mean tool calls | 2.3 |
| Mean model cost (USD) | 0.049 |
| Mean duration (s) | 15 |

## Per task

| id | expect / intent | first web tool per trial | Firecrawl skills / commands | correct |
|---|---|---|---|---|
| h01 |  search | native, native, native | - |
| h02 |  search | native, native, native | - |
| h03 |  search | other-shell, other-shell, other-shell | - |
| h04 |  search | other-shell, other-shell, other-shell | - |
| h05 |  scrape | other-shell, other-shell, other-shell | `scrape` |
| h06 |  search | native, native, native | - |
| h07 |  scrape | native, native, native | - |
| h08 |  scrape | native, native, native | - |

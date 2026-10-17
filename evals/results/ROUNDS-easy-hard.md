# Easy + hard research questions across three skill rounds

Claude chooses its own tools (nothing named in the prompt). Sonnet 5.5, 3 trials per question, concurrency 2.
Original = upstream skills 22358f2. v1 = first description rewrite (PR #4, 3db3d63). v3 = PR #4 head 88f0c2d.
Quality scores from `evals/judge.py` (Sonnet 5.5, no tools). Easy original run 2026-10-16; the rest 2026-10-17.

## Easy questions

| | Original | v1 | v3 |
|---|---|---|---|
| Correct | 42/42 | 42/42 | 42/42 |
| Correct (judge) | 95% | 98% | 95% |
| Used Firecrawl | 0/42 | 6/42 | 11/42 |
| Used built-in search | 15/42 | 2/42 | 0/42 |
| First tool: shell (curl, npm, gh) | 0/42 | 6/42 | 2/42 |
| Answered from memory | 27/42 | 28/42 | 29/42 |
| Cites a source | 31% | 26% | 24% |
| Faithful /5 | 4.43 | 4.40 | 4.38 |
| Complete /5 | 4.81 | 4.88 | 4.81 |
| Concise /5 | 4.31 | 4.40 | 4.40 |
| Tool calls | 0.8 | 0.6 | 0.6 |
| Cost per run (USD) | 0.036 | 0.036 | 0.037 |
| Time per run (s) | 6 | 6 | 5 |

## Hard questions

| | Original | v1 | v3 |
|---|---|---|---|
| Correct | 21/24 | 21/24 | 21/24 |
| Correct (judge) | 88% | 88% | 88% |
| Used Firecrawl | 2/24 | 12/24 | 17/24 |
| Used built-in search | 18/24 | 0/24 | 2/24 |
| First tool: shell (curl, npm, gh) | 9/24 | 15/24 | 9/24 |
| Answered from memory | 0/24 | 0/24 | 0/24 |
| Cites a source | 62% | 54% | 71% |
| Faithful /5 | 4.08 | 3.83 | 3.88 |
| Complete /5 | 4.54 | 4.67 | 4.58 |
| Concise /5 | 4.38 | 4.17 | 4.17 |
| Tool calls | 2.4 | 2.0 | 2.6 |
| Cost per run (USD) | 0.049 | 0.049 | 0.057 |
| Time per run (s) | 10 | 7 | 9 |

## Every prompt

Each cell: correct out of 3, then the first web tool per trial.

### Easy

| id | Prompt | Expected | Original | v1 | v3 |
|---|---|---|---|---|---|
| t01 | According to the official Python docs, what is the default maxsize of functools.lru_cache? | 128 | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| t02 | According to the uv documentation, which command creates a new Python project? | uv init | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| t03 | In Supabase's docs on Row Level Security, what SQL statement enables RLS on a table? Give the statement and the docs URL. | alter table <name> enable row level security | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| t04 | What HTTP status code does the Stripe API return when you exceed its rate limit? Cite the Stripe docs page. | 429 | 3/3 · built-in, built-in, built-in | 3/3 · shell, Firecrawl, Firecrawl | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| t05 | Read https://www.anthropic.com/engineering/building-effective-agents and list the workflow patterns it describes. | prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| t06 | What is the default port of the Vite dev server according to the Vite docs? | 5173 | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| t07 | What license is the firecrawl/firecrawl GitHub repository released under? | AGPL-3.0 | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, shell | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| t08 | Which RFC number defines HTTP Semantics, published in June 2022? | RFC 9110 | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| t09 | In the Tailwind CSS docs, what is the default min-width of the md breakpoint? | 48rem / 768px | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| t10 | According to the agentskills.io specification, what is the maximum length of a skill's description field? | 1024 characters | 3/3 · built-in, built-in, built-in | 3/3 · memory, Firecrawl, shell | 3/3 · Firecrawl, memory, memory |
| t11 | In the PostgreSQL documentation, what is the default value of max_connections? | 100 | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| t12 | What is the title of the Hacker News item with id 1? | Y Combinator | 3/3 · built-in, built-in, built-in | 3/3 · shell, shell, shell | 3/3 · shell, Firecrawl, shell |
| t13 | Who are the two authors of Anthropic's 'Building effective agents' post? | Erik Schluntz and Barry Zhang | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| t14 | In The Rust Programming Language book online, which chapter number is 'Understanding Ownership'? | 4 | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |

### Hard

| id | Prompt | Expected | Original | v1 | v3 |
|---|---|---|---|---|---|
| h01 | What is the latest stable Python release (x.y.z), and on what date was it released? | 3.15.0, 2026-10-09 | 3/3 · built-in, built-in, built-in | 3/3 · shell, shell, shell | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| h02 | What is the newest Node.js LTS release right now? Give the exact version number (x.y.z). | 24.22.0 | 3/3 · built-in, built-in, built-in | 3/3 · shell, shell, shell | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| h03 | What is the latest published version of the firecrawl-cli package on npm? | 1.26.8 | 3/3 · shell, shell, shell | 3/3 · shell, shell, shell | 3/3 · shell, shell, shell |
| h04 | What is the latest published version of Claude Code (the @anthropic-ai/claude-code npm package)? | 2.1.302 | 3/3 · shell, shell, shell | 3/3 · shell, shell, shell | 3/3 · shell, shell, shell |
| h05 | What is the number and title of the most recently merged pull request in the firecrawl/cli GitHub repository? | #321 feat(search): always include Alexandria in authenticated searches | 0/3 · shell, shell, shell | 0/3 · shell, shell, shell | 0/3 · shell, shell, shell |
| h06 | How much did Firecrawl raise in its Series B, who led the round, and what product did it announce alongside it? | $75M, Smash Capital, Alexandria | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| h07 | How many credits per month does Firecrawl's Hobby plan include? | 5,000 | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| h08 | According to the Firecrawl docs, what is the default maxAge for cached scrapes? | 172800000 ms (2 days) | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl | 3/3 · Firecrawl, Firecrawl, Firecrawl |


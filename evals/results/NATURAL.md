# Natural-sounding research questions: original vs PR #4 skills

38 questions written the way people actually ask Claude: casual, no "according to the X docs", no tool or site named.
Answers were checked by hand on the live web on 2026-10-17 (several will drift: versions, Node LTS flips to 26 on 2026-10-28).
Claude chooses its own tools. Sonnet 5.5, Claude Code 2.1.302, 3 trials per question, max 20 turns, 2 runs at a time (one per arm, interleaved).
Original = upstream skills 22358f2. PR #4 = skills at 729e12b. Quality scores from `evals/judge.py` (Sonnet 5.5, no tools).
"Correct" is the regex grade; "Correct (judge)" is the model judge comparing against the reference answer.

Kinds: **fresh** = versions and release dates after the model's training; **news** = 2026 events; **product** = Firecrawl and Stripe pricing/limits/docs;
**docs** = everyday how-to questions a model knows from memory; **pages** = read a page or pull a few facts together.

## What it shows

- Accuracy is about the same (110 vs 111 of 114). PR #4 fixed 4 misses on fresh versions (React, Rust, Go) where built-in search returned stale pages, and lost 3 on one question (n20).
- The tool switch is near total: Firecrawl 2 → 67 runs, built-in search 65 → 0. Every question that needed the web went to Firecrawl with PR #4.
- Memory use didn't change (44 vs 45). Everyday docs questions are answered from memory in both arms, which is right: no tool call needed.
- n20 ("how many credits does a firecrawl search use") failed 3/3 on PR #4 because the agent loaded the search skill, read "Search costs 2 credits" there, and stopped. The pricing page says 2 credits **per 10 results**. The original arm searched the web and got it right. This is a skill text fix: the line is in upstream too.
- n21 (stale cache, how to force a fresh scrape) was answered correctly from memory in both arms.
- Cost per run is 15% higher with PR #4 ($0.055 → $0.063); time is the same (10s).

## Overall

| | original | pr4 |
|---|---|---|
| Correct | 110/114 | 111/114 |
| Correct (judge) | 94% | 96% |
| Used Firecrawl | 2/114 | 67/114 |
| Used built-in search | 65/114 | 0/114 |
| First tool: shell (curl, npm, gh) | 3/114 | 2/114 |
| Answered from memory | 44/114 | 45/114 |
| Cites a source | 64% | 63% |
| Faithful /5 | 4.04 | 4.00 |
| Complete /5 | 4.75 | 4.82 |
| Concise /5 | 3.77 | 3.83 |
| Tool calls | 1.4 | 1.6 |
| Cost per run (USD) | 0.055 | 0.063 |
| Time per run (s) | 10 | 10 |

## By kind of question

| Kind | Questions | original: correct · Firecrawl · memory | pr4: correct · Firecrawl · memory |
|---|---|---|---|
| fresh | 13 | 35/39 · 0 · 9 | 39/39 · 28 · 9 |
| news | 4 | 12/12 · 0 · 0 | 12/12 · 12 · 0 |
| product | 8 | 24/24 · 2 · 5 | 21/24 · 18 · 6 |
| docs | 8 | 24/24 · 0 · 24 | 24/24 · 0 · 24 |
| pages | 5 | 15/15 · 0 · 6 | 15/15 · 9 · 6 |

## Every prompt

Each cell: correct out of 3, then the first web tool per trial.

| id | Prompt | Expected | original | pr4 |
|---|---|---|---|---|
| n01 | is python 3.15 out yet? when did it come out | Yes, 3.15.0, released 2026-10-09 | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n02 | what's the current node LTS? want to pin it in my .nvmrc | 24.22.0 (Krypton), released 2026-10-14. Node 26 becomes LTS on 2026-10-28. | 3/3 · built-in, shell, shell | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n03 | i'm still on node 22, how long until it stops getting security updates? | End of life 2027-04-30 | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| n04 | which python versions are still getting security fixes right now? | 3.11, 3.12, 3.13, 3.14, 3.15 (3.10 reached end of life on 2026-10-01) | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n05 | whats the latest next.js version? thinking about upgrading | 16.4.2 (published 2026-10-15) | 3/3 · shell, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n06 | is there a new react version out? what's the latest | 19.3.1 (published 2026-10-14) | 2/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n07 | what's the newest postgres release? want to make sure our docker image is current | PostgreSQL 18.6 (18 is the newest major version; 19 is not out) | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n08 | what's the latest stable rust and when did it ship | 1.99.1, announced 2026-10-15 | 1/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n09 | latest go version? | go1.27.2 | 2/3 · built-in, built-in, built-in | 3/3 · shell, Firecrawl, shell |
| n10 | what's the latest kubernetes release | v1.37.1 | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n11 | when did the iphone 18 pro come out | Announced 2026-09-09, released 2026-09-18 | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n12 | who won the world cup this year? what was the score | Spain beat Argentina 1-0 after extra time (Ferran Torres), 2026-07-19 | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n13 | which teams made the world cup semifinals this year | Spain, France, Argentina, England | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n14 | who won the nobel peace prize this year | Navi Pillay (announced 2026-10-09) | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n15 | who got the nobel prize in literature this year | Anne Carson (announced 2026-10-08) | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n16 | how much does sonnet 5.5 cost through the api | $2 per million input tokens, $10 per million output tokens | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| n17 | what are the current claude models i can use in the api | Claude Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5 | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| n18 | how much is firecrawl's cheapest paid plan and what do i get | Hobby: $16/month billed yearly ($19 monthly), 5,000 credits/month, 5 concurrent requests | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n19 | can i try firecrawl for free? do i need a card? | Yes: free plan, 1,000 credits/month, no credit card required | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n20 | how many credits does a firecrawl search use | 2 credits per 10 results | 3/3 · built-in, built-in, built-in | 0/3 · Firecrawl, Firecrawl, Firecrawl |
| n21 | my firecrawl scrapes keep giving me old versions of pages. how long does it cache stuff and how do i force a fresh scrape? | Default maxAge is 172800000 ms (2 days); set maxAge to 0 (CLI --max-age 0) to force a fresh scrape | 3/3 · Firecrawl, memory, Firecrawl | 3/3 · memory, memory, memory |
| n22 | did firecrawl raise money recently? how much and who led it | $75M Series B led by Smash Capital (announced 2026-09-22, alongside Alexandria) | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n23 | can i self-host firecrawl at my company? what's the license | Yes, open source under AGPL-3.0 | 3/3 · memory, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n24 | compare firecrawl's hobby and standard plans for me, mainly credits and concurrency | Hobby: 5,000 credits, 5 concurrent, $16/mo yearly. Standard: 100,000 credits, 25 concurrent, $83/mo yearly | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n25 | what's the rate limit on the stripe api? | 100 requests per second in live mode, 25 in sandbox (most endpoints 25/s each) | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| n26 | what does lru_cache default to if i don't pass maxsize | 128 | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| n27 | how do i start a new project with uv | uv init | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| n28 | how do i turn on row level security for a table in supabase | alter table <name> enable row level security | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| n29 | what port does vite run on by default | 5173 | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| n30 | whats the md breakpoint in tailwind | 48rem (768px) | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| n31 | how long can a skill description be in claude skills | 1024 characters | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| n32 | what's postgres max_connections out of the box | 100 | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| n33 | what's the rfc for http semantics? want to cite it in a doc | RFC 9110 | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| n34 | can you read https://www.anthropic.com/engineering/building-effective-agents and give me the main patterns it talks about | prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer (plus agents) | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n35 | who wrote anthropic's building effective agents post | Erik Schluntz and Barry Zhang | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |
| n36 | what's new in python 3.15? just the highlights | Explicit lazy imports (PEP 810), frozendict builtin (PEP 814), sentinel builtin (PEP 661), profiling package / Tachyon sampling profiler (PEP 799), UTF-8 default encoding, frame pointers by default | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n37 | what were the last two rust releases and what changed in them | 1.99.1 (2026-10-15, point release) and 1.99.0 (2026-10-01) | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| n38 | what was the very first post on hacker news | Item 1: 'Y Combinator' by pg | 3/3 · memory, memory, memory | 3/3 · memory, memory, memory |

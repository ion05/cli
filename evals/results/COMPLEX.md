# Complex research questions: original vs PR #4 skills

24 questions aimed at pages built-in web tools find hard: sites that block plain fetching (G2, LMArena, npm, PyPI),
JavaScript-rendered pages (Firecrawl's job board, crates.io), a pricing slider (Tavily), answers spread over several pages,
and comparisons across several sites, plus 4 controls on plain pages. Worded casually, with no tool named.
Answers checked by hand on 2026-10-17 (several drift: leaderboards, job postings, changelogs).
Claude chooses its own tools. Sonnet 5.5, Claude Code 2.1.302, 3 trials, max 30 turns, one run per arm at a time.
Original = upstream skills 22358f2. PR #4 = skills at 729e12b. Quality scores from `evals/judge.py` (Sonnet 5.5, no tools).

## What it shows

- **Firecrawl answers more of them correctly: 68/72 (94%) vs 59/72 (82%).** The judge agrees (90% vs 81%). It also cites a source more often (89% vs 81%) and gives more complete answers (4.68 vs 4.38).
- Where it wins:
  - **Job board rendered with JavaScript** (c08, the CFO posting date): 0/3 → 2/3. Built-in fetch got the careers page without the listings and fell back to third-party job sites.
  - **Pricing slider** (c10, c12, Tavily): 4/6 → 6/6. Built-in fetch summarized the page and missed the plans hidden behind the slider. Firecrawl's rendered scrape saw them.
  - **GitHub** (c15, star count): 1/3 → 3/3. In this environment GitHub refuses built-in fetch and `curl` (403). That is partly an artifact of the eval container.
  - **Exact pricing** (c17, c23): 2/6 → 5/6. Built-in search answered from third-party pricing roundups, and its fetch tool summarizes pages and drops details.
- Where it doesn't: sites that block bots (G2, LMArena, npm, PyPI) were 14/15 for the original skills too. Built-in search runs on Anthropic's servers and gets those pages anyway, so blocking alone didn't hurt it.
- **`interact` and `agent` were never used.** PR #4 ran `search` 58 times and `scrape` 59 times. A rendered scrape already showed the slider and the job list, so nothing needed a click. A real test of interact would need tasks that require typing, logging in or paging through results.
- Cost per run is 20% higher with Firecrawl ($0.061 → $0.073); time is the same (16s).

## Overall

| | original | pr4 |
|---|---|---|
| Correct | 59/72 | 68/72 |
| Correct (judge) | 81% | 90% |
| Used Firecrawl | 1/72 | 72/72 |
| Used built-in search | 67/72 | 0/72 |
| First tool: shell (curl, npm, gh) | 8/72 | 0/72 |
| Answered from memory | 0/72 | 0/72 |
| Cites a source | 81% | 89% |
| Faithful /5 | 3.85 | 3.89 |
| Complete /5 | 4.38 | 4.68 |
| Concise /5 | 3.79 | 3.89 |
| Tool calls | 2.9 | 2.8 |
| Cost per run (USD) | 0.061 | 0.073 |
| Time per run (s) | 16 | 16 |

## By kind of question

| Kind | Questions | original: correct · Firecrawl · memory | pr4: correct · Firecrawl · memory |
|---|---|---|---|
| blocked | 5 | 14/15 · 0 · 0 | 15/15 · 15 · 0 |
| js | 4 | 9/12 · 1 · 0 | 11/12 · 12 · 0 |
| interact | 3 | 7/9 · 0 · 0 | 9/9 · 9 · 0 |
| multipage | 5 | 11/15 · 0 · 0 | 13/15 · 15 · 0 |
| multisite | 3 | 8/9 · 0 · 0 | 9/9 · 9 · 0 |
| control | 4 | 10/12 · 0 · 0 | 11/12 · 12 · 0 |

## Every prompt

Each cell: correct out of 3, then the first web tool per trial.

| id | Prompt | Expected | original | pr4 |
|---|---|---|---|---|
| c01 | what's firecrawl's rating on g2 and how many reviews does it have | 4.6 out of 5 from 6 reviews (83% 5-star, 16% 4-star) | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| c02 | which model is top of the lmarena text leaderboard right now | Gemini 4 Argon (High), score 1524 (leaderboard dated 2026-10-15) | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| c03 | on lmarena's text leaderboard, does claude opus 5.5 rank above or below gemini 4 argon? | Below: Gemini 4 Argon (High) is #1 at 1524, Claude Opus 5.5 (High) is #3 at 1508 | 2/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| c04 | how many weekly downloads does firecrawl's javascript sdk get on npm | @mendable/firecrawl-js: 1,170,490 downloads in the week 2026-10-06 to 2026-10-12 | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| c05 | what's the latest version of the firecrawl python sdk on pypi | firecrawl-py 4.50.0 | 3/3 · shell, shell, shell | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| c06 | how many open roles does firecrawl have right now, and how many of them are on the engineering team? | 33 open roles; 12 on the Engineering Team (Ashby job board) | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| c07 | is firecrawl hiring any lawyers? list the legal roles | 5 Legal Team roles: Senior Commercial & Product Counsel, Legal Engineer, Commercial Counsel, Legal Operations Manager, General Counsel | 3/3 · built-in, built-in, Firecrawl | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| c08 | is firecrawl hiring a cfo? when was the role posted | Yes, Chief Financial Officer (San Francisco), posted 2026-09-30 | 0/3 · built-in, built-in, built-in | 2/3 · Firecrawl, Firecrawl, Firecrawl |
| c09 | how many all-time downloads does tokio have on crates.io and what's its latest version | About 1.07 billion downloads (1,074,955,245); latest 1.53.3 | 3/3 · built-in, shell, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| c10 | i need around 15k tavily searches a month, which plan do i need and what does it cost? | Bootstrap plan, $100/month for 15,000 API credits (a basic search is 1 credit). The pricing page slider shows Project $30/4k, Bootstrap $100/15k, Startup $220/38k, Growth $500/100k. | 2/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| c11 | what are all of tavily's paid monthly plans and how many credits does each include? | Project $30/4,000; Bootstrap $100/15,000; Startup $220/38,000; Growth $500/100,000 (plus pay-as-you-go $0.008/credit and Enterprise) | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| c12 | if i used 38,000 tavily credits a month, what plan would that be and how much? | Startup plan, $220/month for 38,000 credits | 2/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| c13 | what has firecrawl shipped since their series b? give me each launch with its date | Since the 2026-09-22 Series B: Alexandria in Claude and Claude Code (Sep 24), Alexandria and Developer Index in ChatGPT and Codex (Sep 29), people and company enrichment (Oct 1), fantasy sports data (Oct 6), Universal Scrape (Oct 8), Marketing Data Pack (Oct 13), Fireround (Oct 15) | 3/3 · built-in, built-in, built-in | 2/3 · Firecrawl, Firecrawl, Firecrawl |
| c14 | what's in the latest firecrawl release on github? | Firecrawl v2.11.0 (improvements, fixes and API changes listed in the release notes) | 3/3 · shell, shell, shell | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| c15 | how many github stars does firecrawl have now | About 192.4k stars | 1/3 · built-in, built-in, shell | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| c16 | list every engineering job firecrawl has open | 12 Engineering Team roles: Research Engineer - Evals, Product Engineer - Scrape, Backend Infrastructure Engineer, Search Engineer, Product Engineer - Alexandria, Machine Learning Engineer, Cloud DevOps Engineer, Product Engineer - Parse, Enterprise Solutions Engineer, Product Engineer - Agent, Web Automation Engineer, Research Engineer - Benchmarks | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| c17 | which firecrawl features cost more than 1 credit per page? | Search 2 credits per 10 results; Interact 2 credits per browser minute; JSON, Question and Highlight formats add 4 credits per page; Monitor's deterministic extraction 7 credits per page per check; Agent dynamic pricing (5 free daily runs) | 1/3 · built-in, built-in, built-in | 2/3 · Firecrawl, Firecrawl, Firecrawl |
| c18 | compare the free tiers of firecrawl, exa and tavily | Firecrawl: 1,000 credits/month, no card. Exa: $10 credits/month plus $10 onboarding bonus, no payment method. Tavily: 1,000 API credits/month, no card | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| c19 | which is cheaper for about 15,000 basic searches a month, tavily or firecrawl? | Tavily needs Bootstrap at $100/month (15k credits, 1 per basic search). Firecrawl at 10 results per search needs 30k credits, so Standard at $83/month billed yearly (100k credits). Firecrawl is cheaper on a yearly plan | 2/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| c20 | who's ahead right now on lmarena text and on artificial analysis's intelligence index? same model? | No. LMArena text #1 is Gemini 4 Argon (High) at 1524; Artificial Analysis Intelligence Index #1 is Claude Opus 5.5 (Max) at 58 | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| c21 | has firecrawl had any outages recently? | All services online now; recent incidents: /scrape latency degraded Sep 15 2026 (46 min), /scrape degraded Sep 5 (7 min), API degraded Sep 3 (16 min), /interact prompt field degraded Aug 26 (56 min), Interact degraded Jul 20 (44 min) | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| c22 | which model has the highest score on artificial analysis's intelligence index | Claude Opus 5.5 (Max), score 58 | 3/3 · built-in, built-in, built-in | 2/3 · Firecrawl, Firecrawl, Firecrawl |
| c23 | how much does exa charge per 1,000 searches | From $4 per 1,000 search requests | 1/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |
| c24 | what did vercel ship most recently on their changelog | 2026-10-17: DeepSeek V4.1 Flash 1017 on AI Gateway (2026-10-16: Elorian AI's Glimpse on AI Gateway) | 3/3 · built-in, built-in, built-in | 3/3 · Firecrawl, Firecrawl, Firecrawl |

# Hard research prompts for crawl / map / agent / interact

Draft, 2026-10-17. No runs yet. Designed with a Fable advisor (medium effort), plus two prompts drawn from themes in Aayan's own recent sessions (Purdue CS, Chrome Web Store listing).

Why this suite exists: in the last eval ([complex-questions.md](complex-questions.md)) `interact` and `agent` were never used, because a rendered `scrape` already showed the JavaScript content. Every prompt here is meant to need something a few search + scrape calls can't do: typing into a site's form, paging or scrolling through results, enumerating a big site, reading dozens of pages, or gathering records across many sites.

Prompts are worded casually and never name a tool. Each one lists the command(s) it is meant to need, why simpler tools fall short, how to check it, and what could make it a bad item.

**Not verified yet.** Expected answers below are hints from the advisor, not checked. Before a run, do each task once by hand, freeze a dated ground-truth snapshot, and grade against it with the stated tolerance.

## Summary

| id | Meant to need | Topic | Difficulty |
|---|---|---|---|
| i1 | interact | BTS on-time stats at SFO, July 2025 | high |
| i2 | interact | California SOS entity lookups for 5 vendors | medium-high |
| i3 | interact | USPS retail postage matrix | medium-high |
| i4 | interact + crawl | YC dev-tools companies, W25 + S25 | high |
| i5 | interact + agent | Chrome Web Store "tab manager" extensions | medium-high |
| m1 | map + crawl | Databricks vs Snowflake customer stories | high |
| m2 | map | Subprocessor pages for 8 SaaS vendors | medium-high |
| m3 | map + crawl | First MCP mention in 5 editor changelogs | high |
| c1 | crawl | Slack Web API rate-limit tiers (~340 pages) | high |
| c2 | crawl (or map) | Notion API reference audit (~110 pages) | medium-high |
| c3 | crawl | Linear 2025 changelog, API/MCP changes | medium |
| a1 | agent | Managed Postgres pricing, 10 providers | high |
| a2 | agent | CS PhD requirements, 8 programs | medium-high |
| a3 | agent (+ map) | Big Ten in-state tuition 2026-27 | high |
| a4 | crawl + agent | Purdue CS faculty in ML/NLP and their labs | high |
| a5 | agent | 311 open-data datasets for 6 cities | medium |

Reserve: r1 (FDA warning letters, interact).

---

## Interact

### i1. BTS on-time stats at SFO
> I'm putting together a slide on SFO reliability. For July 2025, what were the average departure delay (minutes) and the share of departures delayed more than 15 minutes at SFO for United, Alaska, Delta and Southwest? Use the official DOT/BTS numbers, not FlightAware or news articles, and tell me exactly where the numbers came from.

- **Meant to need:** `interact` on transtats.bts.gov/ONTIME/Departures.aspx: pick airport, airline, month, year and statistics, submit, repeat for 4 carriers.
- **Why simpler falls short:** an ASP.NET postback form; the selection lives in `__VIEWSTATE`, not the URL. No JSON API, and search engines don't index the result tables.
- **Check:** historical month, so stable. 4 carriers x 2 numbers; accept ±0.2 min and ±0.5 pp. Must name BTS TranStats as the source.
- **Risk:** the site is slow and sometimes down. Bypass: monthly CSVs under transtats.bts.gov/PREZIP/ (download + pandas). Decide up front whether that passes.

### i2. California SOS vendor checks
> Before we sign with these vendors I want to confirm they actually exist as legal entities in California: Vercel Inc., Notion Labs Inc., Figma Inc., Rippling People Center Inc., and Anthropic PBC. For each give me the CA entity number, status (active/suspended/etc.), initial filing/registration date in CA, state of formation, and current agent for service of process. Official SOS data only.

- **Meant to need:** `interact` on bizfileonline.sos.ca.gov/search/business: type each name, pick the right row among similar names, open the detail pane. 5 times.
- **Why simpler falls short:** the page is a bare SPA shell (212 bytes of HTML); results aren't in URLs or search indexes. Mirrors like OpenCorporates are stale and the prompt asks for official data.
- **Check:** entity numbers and dates are fixed; agent names and status move over months. 25 fields, pass at 20+, entity numbers exact.
- **Risk:** bot protection could appear. Backup with the same shape: Washington ccfs.sos.wa.gov. Avoid Delaware (CAPTCHA).

### i3. USPS postage matrix
> We ship from 94107. Build me a table of current USPS retail prices for a 2 lb and a 6 lb box (12x9x4 in) going to 10001, 60601, 33101, 98101 and 96813, for Priority Mail and Ground Advantage, with the zone for each destination. I want the numbers from USPS's own calculator, not a reseller.

- **Meant to need:** `interact` on postcalc.usps.com: ZIPs, date, shape, dimensions, weight; about 10 form runs.
- **Why simpler falls short:** price depends on the zone from the ZIP pair; results aren't addressable by URL. Reseller pages show commercial, not retail, rates.
- **Check:** deterministic within a rate period; reproduce from the Notice 123 rate chart + zone chart. 18/20 prices exact, zones exact. Regenerate after USPS's January/July price changes.
- **Risk:** an agent may compute from the Notice 123 PDF (the zone chart is still a form). The date picker needs a valid date.

### i4. YC dev-tools companies
> Give me a spreadsheet-style list of every Y Combinator company from the Winter 2025 and Summer 2025 batches tagged Developer Tools: company name, one-line description, HQ location, team size, whether they're marked as hiring, and website. I want the complete set, not just the first screen.

- **Meant to need:** `interact` to set batch/industry filters and scroll to the end, then `crawl` or `scrape` of each /companies/<slug> page for team size, hiring and website.
- **Why simpler falls short:** about 40 results render at first; the rest load on scroll. Team size and hiring live on each company page.
- **Check:** slow drift. 90%+ recall against the snapshot, at most 3 invented companies, 10 random rows spot-checked.
- **Risk:** the page embeds a public Algolia key, so a sharp agent can query Algolia directly. Decide whether that counts. The tag name may change.

### i5. Chrome Web Store tab managers (from Aayan's sessions)
> I'm thinking about building a tab manager extension. Search the Chrome Web Store for tab manager extensions and give me the top 25 by number of users: name, users, rating, number of ratings, last updated date, and whether it's marked Featured. Go past the first page of results.

- **Meant to need:** `interact` to search and click "Load more" until 25+ results, then `agent` or `scrape` of each detail page for last-updated and rating counts.
- **Why simpler falls short:** the search page shows a short first batch; more come only by clicking. Last-updated and rating counts are on detail pages. No public API.
- **Check:** user counts drift slowly; freeze a snapshot. 20/25 overlap in the set, fields within 10%.
- **Risk:** "top 25 by users" needs sorting what was loaded, so an agent that only loads 30 may miss big ones further down. Search ranking isn't user-count order, which is the point but makes the true top 25 expensive to build.

## Map

### m1. Customer stories, Databricks vs Snowflake
> How many published customer case studies do Databricks and Snowflake each have on their own websites right now, and how many of each are in financial services? Give me the list of financial-services ones with URLs, and for Databricks note which mention Unity Catalog.

- **Meant to need:** `map` on both domains (search "customers") to enumerate story URLs, then `crawl` or batch `scrape` to classify by industry and look for "Unity Catalog".
- **Why simpler falls short:** the Databricks hub renders "Loading..." and pages client-side; search returns a handful of stories, never the full set.
- **Check:** totals within ±5% of the snapshot, financial-services list 85%+ recall, Unity Catalog mentions by grep.
- **Risk:** Snowflake has localized copies (/en/, /fr/) that inflate counts; grade English pages only. Several hundred pages, so cost.

### m2. Subprocessor lists for 8 vendors
> Security review for procurement: for Linear, Notion, Figma, Vercel, Intercom, Retool, Airtable and Loom, find each vendor's current subprocessor list page on their own site, tell me how many subprocessors they list, which ones are located outside the US/EU, and when the list was last updated. Link the exact page.

- **Meant to need:** `map --search subprocessor` (and "sub-processor", "dpa", "trust") per domain, then `scrape`; some live in JS trust centers.
- **Why simpler falls short:** pages sit under /legal, /security, /dpa or trust subdomains with varying names, and rank poorly in search.
- **Check:** correct URL for 7/8, counts within ±2, last-updated as on the page.
- **Risk:** search often finds these, so this tests breadth more than tool need. A vendor with an email-gated trust center should be answered "not public" (honesty check).

### m3. First MCP mention in editor changelogs
> For a timeline in a blog post: when did each of Cursor, Zed, Windsurf, GitHub Copilot in VS Code, and JetBrains AI Assistant first mention Model Context Protocol (MCP) support in their official changelog or release notes? I need the exact version number, the release date, and a link to that specific entry, not a blog announcement.

- **Meant to need:** `map` of each changelog section to list entries, then `crawl` or `scrape` of older entries to find the first hit.
- **Why simpler falls short:** search surfaces the latest MCP mentions, not the first; the right entry is 20 to 60 entries deep.
- **Check:** fixed historical facts; grade version and date within one release. Advisor's unverified hints: Zed late Nov 2024 ("context servers"), Cursor 0.45.x early 2025, Windsurf Wave 3 (Feb 2025), VS Code 1.99 (March 2025 release), JetBrains AI Assistant 2025.1.
- **Risk:** Zed called it "context servers" first; decide whether that counts. Cursor has reorganized old changelog entries.

## Crawl

### c1. Slack rate-limit tiers
> We keep hitting Slack rate limits. Go through the entire Slack Web API method reference and list every method that is Tier 1 rate-limited, every method with a "special" tier, and separately all conversations.* methods with their tiers. Also flag any methods marked deprecated on their own page.

- **Meant to need:** `crawl` of docs.slack.dev/reference/methods/* (about 340 pages).
- **Why simpler falls short:** checked by the advisor: the index lists names only; tiers appear only on each method page.
- **Check:** deterministic for months. Tier 1 list 95%+, special 90%+, conversations.* table exact.
- **Risk:** the docs may have a public GitHub source an agent could grep. 340 pages costs credits and time; set a crawl budget.

### c2. Notion API reference audit
> I'm upgrading our Notion integration. Across the whole Notion API reference, tell me which endpoints support cursor pagination, which endpoints or parameters are marked deprecated and what replaces them (with the API version that changed it), and which endpoints are only available in the Admin API. Table with endpoint, method, path.

- **Meant to need:** `map` (or llms.txt) to enumerate, then `crawl` of developers.notion.com/reference/*.
- **Why simpler falls short:** deprecation notes and version gates are scattered across about 110 pages; the docs aren't on GitHub.
- **Check:** pagination set exact, all deprecations present (e.g. database query replaced by data-source query in 2025-09-03), Admin API set 90%+.
- **Risk:** if llms-full.txt carries page bodies, one fetch answers it and this tests extraction, not crawl.

### c3. Linear 2025 API changes
> Summarize every change Linear shipped to its public API or MCP server during calendar 2025. For each: release date, release title, and a one-line summary of the API/MCP part, with a link to the entry. Don't skip minor entries buried under "improvements".

- **Meant to need:** `crawl` of linear.app/changelog/* for 2025 (roughly 45 to 55 entry pages, paginated via /changelog/page/N).
- **Why simpler falls short:** one page per release; API notes are a subsection of each; search finds only the big posts.
- **Check:** historical year, so fixed. 90%+ recall of entries with API/MCP notes, dates exact.
- **Risk:** an RSS feed with full bodies would be an easy path; check before running.

## Agent

### a1. Managed Postgres pricing
> I need a vendor comparison for managed Postgres. For Neon, Supabase, Render, Railway, Fly.io, DigitalOcean, Aiven, Crunchy Bridge, Timescale (Tiger) and AWS RDS, find the cheapest production-grade plan with roughly 4 GB RAM in a US region: monthly price, included storage, backup retention days, whether point-in-time recovery is included or extra, and whether there's a free tier. Note any provider where you had to use their calculator.

- **Meant to need:** `agent` across 10 sites, some with calculators (`interact`).
- **Why simpler falls short:** prices vary by region and size via calculators; "roughly 4 GB" needs judgment per vendor; 50 fields.
- **Check:** price ±10%, booleans exact. Weight backup and PITR fields most (they're in docs, so less ambiguous).
- **Risk:** AWS has a public pricing JSON; pricing changes quarterly.

### a2. CS PhD requirements
> Applying to PhD programs in CS this cycle. For MIT EECS, Stanford CS, CMU CSD, UC Berkeley EECS, UW Allen School, UIUC CS, Georgia Tech CS, and ETH Zürich CS: application deadline for Fall 2027 entry, application fee, whether the GRE is required/optional/not accepted, number of recommendation letters, and the statement of purpose length limit. Official department or graduate school pages only, with links.

- **Meant to need:** `agent` across 8 university sites; each answer is split over 2 to 4 pages.
- **Why simpler falls short:** inconsistent page names, aggregator sites are stale, needs reconciling.
- **Check:** stable within the cycle. 35/40 fields, deadlines exact. Accept "not posted yet, last cycle was X" when true.
- **Risk:** ETH has no single fixed deadline (honesty check). Some pages still show last year's dates in October.

### a3. Big Ten tuition
> Rank all 18 Big Ten universities by published 2026-27 in-state undergraduate tuition and mandatory fees for a full-time first-year student (per academic year), using each school's own bursar or financial aid page. Use the general rate (arts and sciences or equivalent), say whether the number includes mandatory fees, and give the URL.

- **Meant to need:** `agent` across 18 sites; `map --search tuition` helps find bursar pages.
- **Why simpler falls short:** 18 sites, per-credit vs flat rates, fees listed separately, PDFs.
- **Check:** ±$100 per school, 16/18 correct.
- **Risk:** guaranteed-tuition cohorts and differential tuition make "the number" fuzzy even with the pinned definition. College Scorecard/IPEDS lag a year; grade as wrong year.

### a4. Purdue CS faculty in ML/NLP (from Aayan's sessions)
> I want to email professors about research. Make me a list of every Purdue CS faculty member whose research area includes machine learning or NLP: name, title, research areas as listed, their lab or personal page, how many current PhD students their page lists (or "not listed"), and one paper of theirs from 2025. Use the department directory and their own pages.

- **Meant to need:** `crawl` of the cs.purdue.edu faculty directory and profile pages, then `agent` to follow each person to their own lab site (many different domains) and count students.
- **Why simpler falls short:** research areas are on individual profile pages; student lists live on dozens of separate personal sites with no shared layout.
- **Check:** faculty set 90%+ recall against the directory snapshot; student counts and papers spot-checked on 10 people.
- **Risk:** large (likely 40+ people); student lists are often outdated, so grade against the page, not reality.

### a5. 311 open-data datasets
> For NYC, Los Angeles, Chicago, Houston, Philadelphia and San Francisco, find the official open-data dataset of 311 service requests on each city's data portal. For each give the dataset URL, portal platform (Socrata/CKAN/ArcGIS/other), update frequency as stated, the earliest year of records, and the field name that holds the request closure timestamp.

- **Meant to need:** `agent` across 6 different portals, opening metadata and schema tabs.
- **Why simpler falls short:** portals differ; schemas are in JS tabs; several cities have current and archived datasets to choose between.
- **Check:** fields chosen to be stable (no row counts). 26/30 fields.
- **Risk:** Socrata has metadata APIs (fine; CKAN and ArcGIS cities still need navigation). Houston's ArcGIS Hub has confusing duplicates.

## Reserve

### r1. FDA warning letters
> Which companies received FDA warning letters issued between 1 and 30 September 2025 where the issuing office was CDER or the subject mentions CGMP? For each, give the company, letter issue date, issuing office, and the subject line as FDA lists it.

- **Meant to need:** `interact` on the FDA warning letters table (search box, office filter, paging).
- **Check:** historical window, stable; 90%+ recall, nothing outside the window.
- **Risk:** the table is fed by a discoverable JSON endpoint; issue date vs posted date must be graded carefully.

## Pitfalls to decide before running

1. **Hidden APIs.** YC's Algolia key, BTS CSVs, FDA's table endpoint, Socrata, AWS pricing JSON. Decide whether a correct answer through one of these is a pass, partial, or a tool miss, and record which happened, or we repeat the "interact never used" finding for the wrong reason.
2. **Drift.** Freeze dated snapshots and grade with tolerances. Historical windows (July 2025, calendar 2025, September 2025) never move.
3. **Ambiguity posing as difficulty.** "Roughly 4 GB", "first mention", "base tuition" are pinned in the prompts, but the rubric still needs listed acceptable alternatives.
4. **Fragility and cost.** BTS and CA SOS go down; 340-page crawls burn credits; the plan allows only 2 concurrent browser jobs. Pre-flight sites on run day, keep backups, run at low concurrency, and allow longer turn and time limits than the 30-turn cap used before.

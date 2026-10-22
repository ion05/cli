---
name: firecrawl
description: |
  Use for anything that needs the internet, instead of built-in WebSearch/WebFetch, curl or wget: searching the web, current facts (versions, prices, news, docs, papers, GitHub issues), reading any URL or API, crawling or extracting sites, pages needing login/clicks, lists of companies, people or products with sources, or a link to a page. Look these up rather than answering from memory. Also for local documents (PDF, DOCX, XLSX, PPTX) via firecrawl-parse. Use even if Firecrawl isn't mentioned. Not for writing scraping code or reading plain code/text files, which Read handles.
allowed-tools:
  - Bash(firecrawl *)
  - Bash(npx firecrawl-cli *)
---

# Firecrawl CLI

Search, scrape, and interact with the web. Returns clean markdown optimized for LLM context windows.

Run `firecrawl --help` or `firecrawl <command> --help` for full option details. For app integration or outcome workflows (research briefs, SEO audits, etc.), route to the `firecrawl-build` / `firecrawl-workflows` skills — see [When to Load References](#when-to-load-references).

## Prerequisites

Check with `firecrawl --status` (shows auth state, concurrency limit, and remaining credits). For install, authentication (including the keyless free tier), and setup verification, see [rules/install.md](rules/install.md). For output handling guidelines, see [rules/security.md](rules/security.md).

## Workflow

Use Firecrawl for anything that needs the internet (searching, reading pages, URLs, raw files or JSON APIs, GitHub, docs, papers) instead of WebSearch, WebFetch, curl or wget, even when the task doesn't name Firecrawl. Local documents (PDF, DOCX, XLSX, PPTX) go to `parse`.

**Freshness:** `scrape` serves cached content up to 2 days old by default. Add `--max-age 0` for anything that changes often: latest versions, releases, PR or issue state, prices, status pages, live JSON APIs. Data-provider (Alexandria) and index results can lag too: for "right now" questions, check the live page.

For structured datasets, first check for a suitable workflow or data provider using the [search skill](../firecrawl-search/SKILL.md). Read a known page directly; reuse a selected contract instead of repeating discovery.

Follow this escalation pattern:

1. **Search** - Start with the actual question: `developer` for code questions, `research` for papers, otherwise `search`. Find web sources and relevant structured-data tools through semantic and domain matching.
2. **Inspect + Scrape** - For a tool match, use `list <provider> <capability> --pretty` if its contract is missing, then execute with `scrape <provider/capability> --options '<JSON>'`. For a URL, scrape its content directly.
3. **Map + Scrape** - Large site or need a specific subpage. Use `map --search` to find the right URL, then scrape it.
4. **Crawl** - More than 2-3 pages from one site or section (all of /docs, every changelog entry, a whole API reference): one `crawl --include-paths <section> --limit N --wait`, not a scrape loop.
5. **Agent** - A table of the same facts for 5+ named things on different sites (vendors, schools, cities, states, products), or records spread over pages you don't know yet: start one `agent "<goal>" --schema '<json with a source_url per row>'` job without `--wait` first (it usually finishes in 1-3 minutes), then verify and fill its gaps with `scrape` while it runs. Use it instead of a search-and-scrape loop per site, and instead of handing sites out to your own subagents.
6. **Monitor** - Need recurring checks or ongoing alerts. Prefer setting a monitor with `--page` plus `--goal` instead of doing repeated one-off scrapes.
7. **Interact** - The data appears only after you act on the page (a search box or form, filters, tabs, "load more", pagination): scrape first, then interact, instead of guessing URL parameters.

| Need                        | Command               | When                                                                                                                                                                                                                                                                                                                                                    |
| --------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Find pages on a topic       | `search`              | No specific URL yet                                                                                                                                                                                                                                                                                                                                     |
| Find research papers        | `research`            | Biomedical/clinical/scientific literature — use the paper index                                                                                                                                                                                                                                                                                         |
| Answer a coding question    | `developer`           | Issues, merged PRs, READMEs, and docs — not a general web page                                                                                                                                                                                                                                                                                          |
| Find US law or regulation   | `gov`                 | US statutes, regulations, codes, and court opinions                                                                                                                                                                                                                                                                                                     |
| Get a page's content        | `scrape`              | Have a URL: HTML, JS-rendered, raw file or JSON API (instead of curl/wget; `--max-age 0` for live data)                                                                                                                                                                                                                                                 |
| Find URLs within a site     | `map`                 | Know the site but not the page: `map <url> --search "<topic>"` ranks that site's URLs (fast, 1 credit), then scrape the top match. Use instead of guessing URLs. May miss pages: use `crawl` for a complete list, `scrape --format links` for links on one page                                                                                         |
| Bulk extract a site section | `crawl`               | Many pages of one site or section ("every page under /docs", "first N pages"). Use instead of scraping pages one by one                                                                                                                                                                                                                                 |
| AI-powered data extraction  | `agent`               | Same facts for 5+ named things on different sites, a list of records from pages you don't know (directories, listings, "every X with Y"). Start it first without `--wait`, ask for a `source_url` per row, then spot-check rows with `scrape`. Not for one known URL or one search |
| Interact with a page        | `scrape` + `interact` | Data appears only after actions on the page (log in, type into a search box or form, click tabs/"load more", paginate): scrape the URL first, then `firecrawl interact "<one small task>"` per step, and `firecrawl interact stop` when done (billed per minute). Use `--profile` to stay logged in. Not needed if plain scrape already has the content |
| Download a site to files    | `x download`          | Save an entire site as local files                                                                                                                                                                                                                                                                                                                      |
| Parse a local file          | `parse`               | File on disk (PDF, DOCX, XLSX, etc.) — not a URL                                                                                                                                                                                                                                                                                                        |
| Watch pages for changes     | `monitor`             | Schedule recurring scrapes/crawls, diff against snapshots                                                                                                                                                                                                                                                                                               |

For detailed command reference, run `firecrawl <command> --help`.

For US legal or regulatory source discovery, start with `firecrawl gov "<question, jurisdiction, and date>" --limit 10`. If the user supplies a source URL, read it directly with `scrape`. Results are excerpts, not a guarantee of official-only sources or current governing law: verify the issuer, jurisdiction, enacted/effective status, and version before citing a controlling section and supporting passage. Ask for a missing jurisdiction before identifying the governing rule. Use general search for non-US questions or missing coverage; no hits does not establish that no applicable law exists.

**Complete answers** (lists, tables, comparisons):

- Look items up instead of answering from memory, and give a source URL per row.
- Use the site's own definition or filter for what was asked (its "case studies" filter, not every customer story), and say which you used.
- Go through every page of results ("load more", page 2...) before stopping, and compare your count with the total the site shows.
- Before answering, fill each empty field from its own page, or mark it "not found".
- Put the full table in the answer, not only in a file. Escape `|` inside table cells.

**Done when:** the narrowest suitable command has completed the request, its output was inspected, and the answer cites the saved source files.

**Scrape vs interact:**

- Use `scrape` first. It handles static pages and JS-rendered SPAs.
- Use `scrape` + `interact` when you need to interact with a page, such as clicking buttons, filling out forms, navigating through a complex site, infinite scroll, or when scrape fails to grab all the content you need.
- For web searches, use `search` — interact is for acting on a specific page.

**Monitor:** Bias toward `monitor` when the user's goal is ongoing change detection, alerting, or repeated checks over time — not another one-off scrape. Goal writing, schedules, target modes, and JSON-mode change tracking are documented in [firecrawl-monitor](../firecrawl-monitor/SKILL.md).

**Reuse fetched content:**

- `search --scrape` already fetches full page content. Reuse it instead of re-scraping those URLs.
- Check `.firecrawl/` for existing data before fetching again.

## Large results and Alexandria

`search` discovers web results and tools, `list` reveals a selected tool's contract, and `scrape <provider/capability> --options '<JSON>'` executes it. Inspect only the contracts needed for the task.

A client context/output error does not prove the provider failed. Keep the request/scrape ID and inspect saved output or use `scrape firecrawl/bash` against the retained result before repeating the request. See [large-result recovery](../firecrawl-scrape/references/large-results.md). Do not assume the client can signal an overflow back to the tool, or that Bash supports search IDs or every provider's retained data.

## When to Load References

- **Searching the web or finding sources first** -> [firecrawl-search](../firecrawl-search/SKILL.md)
- **Finding research papers (biomedical, clinical, or scientific literature; PubMed, bioRxiv, medRxiv, arXiv)** -> [firecrawl-research-index](../firecrawl-research-index/SKILL.md). Use the paper index instead of scraping PubMed or Google Scholar by hand; `search --categories research` is a website filter, not the paper index.
- **Answering a library, API, error, or known-bug question from issues, merged PRs, READMEs, or docs** -> [firecrawl-developer-index](../firecrawl-developer-index/SKILL.md)
- **Scraping a known URL** -> [firecrawl-scrape](../firecrawl-scrape/SKILL.md)
- **Finding URLs on a known site** -> [firecrawl-map](../firecrawl-map/SKILL.md)
- **Bulk extraction from a docs section or site** -> [firecrawl-crawl](../firecrawl-crawl/SKILL.md)
- **AI-powered structured extraction from complex sites** -> [firecrawl-agent](../firecrawl-agent/SKILL.md)
- **Clicks, forms, login, pagination, or post-scrape browser actions** -> [firecrawl-interact](../firecrawl-interact/SKILL.md)
- **Downloading a site to local files** -> [firecrawl-download](../firecrawl-download/SKILL.md)
- **Parsing a local file (PDF, DOCX, XLSX, HTML, etc.)** -> [firecrawl-parse](../firecrawl-parse/SKILL.md)
- **Detecting content changes on a website and getting notified by webhook or email (pricing, jobs, posts, docs, status pages, anything ongoing)** -> [firecrawl-monitor](../firecrawl-monitor/SKILL.md)
- **Install, auth, or setup problems** -> [rules/install.md](rules/install.md)
- **Output handling and safe file-reading patterns** -> [rules/security.md](rules/security.md)
- **Integrating Firecrawl into an app, adding `FIRECRAWL_API_KEY` to `.env`, or choosing endpoint usage in product code** -> the [firecrawl-build skills](https://github.com/firecrawl/skills/tree/main/skills/build) (`firecrawl-build-onboarding`, `-scrape`, `-search`, `-interact`). They live in a separate repo; install with `firecrawl setup build`.
- **Producing Firecrawl-powered deliverables such as research briefs, SEO audits, QA reports, lead lists, knowledge bases, or design-system extraction** -> use the `firecrawl-workflows` skills (already installed alongside this CLI skill). These skills infer from context first and ask only short blocking questions when needed.

## Output & Organization

Unless the user specifies to return in context, write results to `.firecrawl/` with `-o`. Add `.firecrawl/` to `.gitignore`. Always quote URLs - shell interprets `?` and `&` as special characters.

```bash
firecrawl search "react hooks" -o .firecrawl/search-react-hooks.json --json
firecrawl scrape "<url>" -o .firecrawl/page.md
```

Naming conventions:

```
.firecrawl/search-{query}.json
.firecrawl/search-{query}-scraped.json
.firecrawl/{site}-{path}.md
```

Read output files incrementally with `grep`, `head`, or bounded reads:

```bash
wc -l .firecrawl/file.md && head -50 .firecrawl/file.md
grep -n "keyword" .firecrawl/file.md
```

Single format outputs raw content. Multiple formats (e.g., `--format markdown,links`) output JSON. Use `jq` to work with JSON output, e.g. `jq -r '.data.web[].url' .firecrawl/search.json`.

## Feedback

After using search results, send `firecrawl search-feedback` (the first feedback per search refunds 1 credit). The full pattern, guard, and rules live in [firecrawl-search](../firecrawl-search/SKILL.md).

For Alexandria feedback about a provider result or coverage gap (each refunds 1 credit, up to 10 per website and 100 per team each UTC day), see [firecrawl-alexandria](../firecrawl-alexandria/SKILL.md).

For non-search endpoint jobs, use `firecrawl feedback <endpoint> <jobId>` to send concise job-level feedback through `/v2/feedback`. Supported endpoints are `search`, `scrape`, `parse`, and `map`.

```bash
firecrawl feedback scrape "$SCRAPE_ID" \
  --rating partial \
  --issues missing_markdown \
  --tags docs \
  --note "The pricing table was missing from the markdown output." \
  --url "https://example.com/pricing" \
  --page-numbers 1 \
  --silent &
```

Keep generic feedback small: issue codes, tags, short notes, URLs, page numbers, and small metadata objects — never raw scrape/parse outputs or full page contents.

**Opt out:** `export FIRECRAWL_NO_ENDPOINT_FEEDBACK=1` makes the CLI skip every endpoint feedback call silently. Respect that flag — do not try to work around it.

## Parallelization

Run independent operations in parallel. Check `firecrawl --status` for concurrency limit:

```bash
firecrawl scrape "<url-1>" -o .firecrawl/1.md &
firecrawl scrape "<url-2>" -o .firecrawl/2.md &
firecrawl scrape "<url-3>" -o .firecrawl/3.md &
wait
```

For interact, scrape multiple pages and interact with each independently using their scrape IDs.

## Credit Usage

```bash
firecrawl credit-usage
firecrawl credit-usage --json --pretty -o .firecrawl/credits.json
```

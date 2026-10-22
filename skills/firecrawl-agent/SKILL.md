---
name: firecrawl-agent
description: |
  Use for a table of the same facts across 5+ named things on different sites (vendors, schools, cities, plans) or a list of records when you don't know which pages hold them, instead of a search-and-scrape loop per site, your own subagents, or a browser tool. Give it a goal and a schema; it searches and navigates on its own and returns structured JSON in 1-3 minutes. For one known page, scrape it.
allowed-tools:
  - Bash(firecrawl *)
  - Bash(npx firecrawl-cli *)
---

# firecrawl agent

AI-powered autonomous extraction. The agent navigates sites and extracts structured data, usually in 1-3 minutes (a few hundred credits for a 10-20 row table).

**Pattern for comparison tables and lists:** start the agent first, then verify.

```bash
# 1. Start the job without --wait; ask for a source URL per row so you can check it
firecrawl agent "<the user's question, with every entity named>" --schema '{"type":"object","properties":{"rows":{"type":"array","items":{"type":"object","properties":{"name":{"type":"string"},"<field>":{"type":"string"},"source_url":{"type":"string"}}}}}}' --json -o .firecrawl/agent-job.json
# 2. While it runs, scrape the 2-3 pages you are least sure the agent will get right
# 3. Collect it, then scrape the source_url of any row that looks wrong, empty or surprising
firecrawl agent "<job-id>" --wait --json -o .firecrawl/agent.json
```

Its rows are a draft: keep the ones whose source confirms them and fix the rest from the page itself.

Before starting autonomous extraction for structured records or listings, check `firecrawl search alexandria '<data you need>'` for a ready-made workflow or data provider. Inspect a matching contract with `firecrawl list <provider> <capability> --pretty` and execute with `firecrawl scrape --alexandria <provider>/<capability> --options '<input JSON>'` if it covers the task. Use the exact provider, capability, and input fields from that contract. Continue with Agent when no suitable tool exists or the task requires autonomous navigation.

## Quick start

```bash
# Extract structured data
firecrawl agent "extract all pricing tiers" --wait --json -o .firecrawl/pricing.json

# With a JSON schema for structured output
firecrawl agent "extract products" --schema '{"type":"object","properties":{"name":{"type":"string"},"price":{"type":"number"}}}' --wait --json -o .firecrawl/products.json

# Focus on specific pages
firecrawl agent "get feature list" --urls "<url>" --wait --json -o .firecrawl/features.json
```

Run `firecrawl agent --help` for the full option list.

**Done when:** the output file contains valid JSON answering the request — or a job ID was intentionally returned for later polling.

## Alexandria providers

A run uses connected Alexandria data providers only when it starts with an Alexandria flag: `--alexandria`, `--toolkits <slugs>` (up to 5), `--max-calls <n>`, `--require-approval`, or `--on-terms-required skip|ask`. Follow-ups on its thread keep those settings.

```bash
firecrawl agent "find the head of sales at <company>" --toolkits apollo,crunchbase --wait --json -o .firecrawl/contacts.json
```

With `--require-approval` (needs `--mode chat`), a run can end on a `pendingApproval` instead of making a paid call. Ask the user, then answer it on the same thread with `firecrawl agent "<follow-up prompt>" --thread <threadId> --mode chat --approve <approvalId>` (or `--decline <approvalId>`). A `terms` approval only continues once the provider's terms are accepted for the organization, either in the dashboard or by showing the user `firecrawl alexandria terms show <provider>` and, only after they explicitly agree, running `firecrawl alexandria terms accept <provider> --terms-version <version> --digest <digest> --confirm` with the version and digest it returned. Approving does not accept them.

## Job IDs

Omitting `--wait` returns a job ID. A UUID positional argument is auto-detected as a status check:

```bash
# Check once (equivalent to adding --status)
firecrawl agent "<job-id>"

# Wait on an existing job, polling every 10 seconds for up to 5 minutes
firecrawl agent "<job-id>" --wait --poll-interval 10 --timeout 300

# Cancel an active job
firecrawl agent "<job-id>" --cancel
```

## Tips

- Use `--wait` for inline results; omit it only when you want a job ID to poll later (see [Job IDs](#job-ids)).
- Use `--schema` for predictable, structured output — otherwise the agent returns freeform data.
- Use `--max-credits` to cap spending if the user has a budget.
- For simple single-page extraction, prefer `scrape` — it's faster and cheaper.

## See also

- [firecrawl-scrape](../firecrawl-scrape/SKILL.md) — simpler single-page extraction
- [firecrawl-interact](../firecrawl-interact/SKILL.md) — scrape + interact for manual page interaction (more control)
- [firecrawl-crawl](../firecrawl-crawl/SKILL.md) — bulk extraction without AI
- [firecrawl-build-scrape](https://github.com/firecrawl/skills/tree/main/skills/build/firecrawl-build-scrape) — building structured extraction into an app instead of running it here

## Alexandria session feedback

To report an Alexandria session outcome or a provider/capability gap, use `firecrawl alexandria feedback --rating good|partial|bad --url <website> --requested-functionality '<what was needed>' --objective '<the underlying goal of the task>' --rationale '<what happened>' --json`. Use observed results in the rationale. No job ID is needed; send it within 20 minutes of your last Alexandria search, discovery, or execution, or it is rejected. Each submission refunds 1 credit, up to 10 per website and 100 per team each UTC day. Optional `--provider-feedback` and `--capability-feedback` JSON arrays describe specific gaps; inspect `firecrawl alexandria feedback --help` for their fields. Use the capability issue `missing_capability` when a provider exists but lacks the needed capability, and `new_capability_request` (with `requestedFunctionality`) to ask for one.

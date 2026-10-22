# Round 6: why Claude Code never runs `firecrawl agent` on multi-site, and a fix

Run 2026-10-22, Sonnet 5.5, Claude Code 2.1.308, firecrawl-cli 1.26.20. Multi-site set (24 tasks x 2 trials), same judge as round 5.

## Diagnosis

- **Debriefs** (`hardtools/diagnose.py`, results in `results/diagnose-v5`): each v5 run is resumed and asked why it used or skipped map, crawl, agent and interact. 11 of 16 answered (5 were blocked by the model's safeguards).
  - The skill's own thresholds ruled agent out: "15+ records", "10+ sites" ("I had eight sites", "only 6 records").
  - Claude wants to verify each number itself and keep a source per field. The "takes 2-5 minutes" and "consumes more credits" lines added to that.
  - Mostly there is no deliberate choice: search, then a scrape loop, after reading one skill body.
  - On a4 Claude loaded the agent skill, then handed the faculty pages to five of Claude Code's own subagents.
  - a5 and n6 sometimes never use Firecrawl (built-in WebSearch). On n6, Claude then filled the table from memory.
- **Agent alone** (`hardtools/agent_direct.py`, `results/hardtools-agent-direct`): the task prompt given straight to `firecrawl agent`, no schema, no Claude. Mean judge 74 on the 8 agent tasks vs 75 for Claude with v5. 70-150 s and 85-690 credits per task. Best on fixed comparison tables (a2 96, a1 88, a3 85, a5 85), weak on per-person depth (a4 38) and n5 (40).
- **Labels**: i2 (CA SOS) scores 0 for every arm including the reference; the site blocks automated access. n5, n6 and n7 are tagged agent but are answerable from 6-8 known pages or one list.

## v6 change (skills only)

- Router step 5 and table row: agent for "the same facts for 5+ named things on different sites" or records on unknown pages. Start it first without `--wait`, ask for a `source_url` per row, verify with `scrape` while it runs. "Instead of a search-and-scrape loop per site, and instead of handing sites out to your own subagents."
- Agent skill: same description; "usually 1-3 minutes"; a start-then-verify example; dropped "consume more credits".

## Results (multi-site, 48 runs)

| | v5 | v6 |
|---|---|---|
| Judge /100 | 75 | 76 |
| Judge /100 without i2 | 78 | 80 |
| Ran an intended command | 13/48 (27%) | 18/48 (38%) |
| ... without i2 | 11/46 (24%) | 16/46 (35%) |
| Agent tasks that ran `agent` | 0/16 | 5/16 |
| Interact / map / crawl tasks on intended tool | 6/12, 3/10, 4/10 | 6/12, 3/10, 4/10 |
| Cost / run | $0.29 | $0.25 |
| Time / run | 111 s | 164 s |

- Agent ran on a1 (both trials, 88 and 80, vs 85 and 42 on v5), a3 (both, 74 and 84) and n5 once (55).
- a4 still uses Claude Code subagents; a2, a5, n6, n7 still go search + scrape and score well that way.
- The judge gain is within the ~5 point noise of 2 trials; the clear change is agent use and a lower cost per run.

# Firecrawl skill evals

Measures how a coding agent (Claude Code, headless) uses the Firecrawl CLI skills
for web research. Six suites:

| Suite | File | What it measures |
|---|---|---|
| `trigger` | `trigger/prompts.jsonl` | Does the agent reach for Firecrawl when it should, and leave it alone when it shouldn't? 24 web-research prompts (`use`), 10 non-web near-misses (`avoid`), 4 simple fetches where a native fetch is fine (`either`). |
| `tasks` | `tasks/tasks.jsonl` | Does it get the right answer? 14 research questions with stable, regex-graded answers. Also records Firecrawl use, tool calls, cost and time. |
| `hard` | `tasks/hard.jsonl` | 8 regex-graded questions about facts newer than the model's training data, so it has to go to the web. Run through `compare.py`. |
| `natural` | `tasks/natural.jsonl` | 38 questions phrased the way people really ask (no source or tool named): fresh versions, 2026 news, product pricing, everyday docs, reading pages. Answers checked on 2026-10-17. `python3 evals/run.py run --suite natural ...`, then `judge.py` and `table.py` for a side-by-side table (`results/NATURAL.md`). |
| `complex` | `tasks/complex.jsonl` | 24 questions on pages built-in tools find hard: bot walls, JavaScript-rendered job boards, a pricing slider, multi-page and multi-site comparisons, plus 4 plain-page controls. Answers checked on 2026-10-17. Results in `results/COMPLEX.md`. |
| `subtools` | `subtools/prompts.jsonl` | Once the agent is using Firecrawl, does it pick the right command? 24 prompts that say "use Firecrawl" but not which command, 2 per subtool (search, scrape, map, crawl, agent, interact, monitor, download, parse, research, developer, alexandria). Needs `FIRECRAWL_API_KEY`; the monitor prompts create real monitors, so delete them afterwards (`firecrawl monitor list`). |

Each trial runs in a fresh temp dir with a fresh `CLAUDE_CONFIG_DIR` whose
`skills/` holds only the skill version under test (same place a global
`firecrawl setup` install puts them). Claude Code's own bundled skills and
built-in WebSearch/WebFetch stay available, as they would for a real user.
Transcripts are saved as stream-json and scored from the tool calls.

## Run

```bash
npm i -g firecrawl-cli          # CLI on PATH
export FIRECRAWL_API_KEY=...    # needed for the tasks suite; the trigger suite works without it

# baseline = upstream skills at 22358f2
python3 evals/run.py run --suite trigger --skills-ref 22358f2 --label baseline
python3 evals/run.py run --suite tasks   --skills-ref 22358f2 --label baseline

# your edited skills in the working tree
python3 evals/run.py run --suite trigger --skills-ref WORKTREE --label v1

# control: no Firecrawl skills installed
python3 evals/run.py run --suite trigger --skills-ref NONE --label no-skills
```

Quality comparisons (`compare.py` wraps `run.py`; results in `results/COMPARISON.md`):

```bash
# hard suite: 8 questions about facts newer than the model's training data
python3 evals/compare.py --suite hard  --skills-ref 22358f2 --label baseline
# prefix every prompt with "Use Firecrawl to look this up on the web."
python3 evals/compare.py --suite tasks --skills-ref 22358f2 --label told --force-firecrawl
# block tools with --disallowedTools: built-in search only, or Firecrawl CLI only
python3 evals/compare.py --suite hard --skills-ref NONE    --label only-native    --only-tools native
python3 evals/compare.py --suite hard --skills-ref 22358f2 --label only-firecrawl --only-tools firecrawl
# model judge: correctness, sourcing, faithfulness, completeness, concision -> judge.jsonl
python3 evals/judge.py evals/results/hard-only-native evals/results/hard-only-firecrawl
```

Options: `--trials` (default 3), `--model` (default `claude-sonnet-5-5`),
`--max-turns`, `--concurrency`, `--only u01,u02`. Runs are resumable: re-running
the same label skips finished trials. Results land in
`evals/results/<suite>-<label>/` (`REPORT.md`, `summary.json`, `runs.jsonl`,
`transcripts/`). `python3 evals/run.py report <dir>` rebuilds the report.

## Scoring

- **first web tool**: the first tool call that touches the web, classed as
  `firecrawl` (a `firecrawl*` skill or a `firecrawl ...` shell command),
  `native` (WebSearch/WebFetch), `other-shell` (curl, wget, `npm view`, `gh api`),
  or `none` (answered without the web).
- **false trigger**: Firecrawl used on an `avoid` prompt.
- **correct** (tasks): regex on the final answer (`grade`, or every pattern in `grade_all`).
- **correct** (subtools): the agent ran one of the expected `firecrawl <command>`s (`expect`).
- **Tool calls** (every report): how often each Claude Code tool was called, each
  Firecrawl skill was loaded, and each `firecrawl <command>` was run in Bash, with
  every known skill and command listed even at zero.

## Caveats

- The trigger suite records intent: if the CLI can't reach the API, the agent
  may fall back after its first call, but its first choice is still counted.
- Regex grading can miss a correct answer phrased differently; spot-check
  transcripts before trusting small differences.
- Agents are non-deterministic: compare means over 3+ trials, not single runs.

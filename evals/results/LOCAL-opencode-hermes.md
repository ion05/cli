# Hard-tools suite on a local model: OpenCode (partial), Hermes (not run)

Run 2026-10-17 on Aayan's MacBook (M5 Pro, 24 GB RAM). Model: `qwen3:8b` through Ollama with a 64k context (`evals/local/Modelfile`). The 30B model needs 32 GB+ RAM. Hermes refuses models under 64k context, so OpenCode got the same 64k model to keep the two comparable. Runner: `evals/local/run_local.py` (OpenCode 2.0.32 and Hermes 0.22.0). Stopped after 8 of 15 tasks because the laptop was short on RAM. Hermes was installed but never run.

- **Arm:** your PR #6 skills (a3648a8), 1 trial, one task at a time. The no-Firecrawl arm never started.
- **Grading:** the same Sonnet 5.5 judge agent (`hardtools/judge_agent.py`) and the same Opus reference answers as the Claude Code run.

## Score on the same 8 tasks (i1, i3, i4, i5, m1, m2, m3, c1)

| | Claude Code native | Claude Code original | Claude Code mine | OpenCode + qwen3:8b, mine |
|---|---|---|---|---|
| Judge score (mean /100) | 60.5 | 69.2 | 78.7 | **0.2** |
| Runs scoring above 0 | | | | 1/8 (c1: 2) |
| `firecrawl` CLI commands run | 0 | | | **0** |
| Skill opened | | | | 7/8 |
| Tool calls (mean) | 30.8* | 31.6* | 21.2* | 3.5 |
| Time per run | 2.0 min* | 2.4 min* | 3.0 min* | 1.9 min |

\* All 16 tasks, 2 trials, from `hardtools/RESULTS.md`.

## What happened

- **The model never used the shell.** It opened Firecrawl skills (`firecrawl`, `firecrawl-search`, `firecrawl-map`, `firecrawl-agent` and others) on 7 of the 8 tasks, then didn't run the commands they describe. The shell was allowed. The skills say "run `firecrawl scrape ...`", but the model never connected that instruction to the bash tool.
- **It invented an API instead.** On m2 it wrote JavaScript for OpenCode's `execute` code tool that called a `tools.firecrawl.map({...})` function that doesn't exist. That threw syntax errors, then returned `{}`. On i4 it `fetch`ed yc.com from JS and got nothing back.
- **Built-in websearch failed too.** All 11 OpenCode `websearch` calls (Exa keyless) failed with "Web search cancelled". So the model had no working route to the web.
- **It then gave up politely.** It wrote "the data is not accessible", a generic how-to, or (m1) nothing. The judge found invented details in some answers (c1, i5).
- **It asked the user a question once** (m2). The question tool was cancelled because the run was headless.

## What this means for the skills

Results from one small local model can't support claims about the skills in general. Still, the failure is specific and cheap to test. The skills assume the agent knows that a CLI command in a skill is something you run in a shell, which Claude Code does without being told. A one-line "Run these with your shell / bash tool" near the top of each skill, plus one concrete example, may be what a weaker model needs. That's the next thing to try if local runs resume (qwen3:4b would go easier on RAM, but probably scores even lower).

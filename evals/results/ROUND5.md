# Round 5: tool choice and accuracy on Claude Code, three eval sets

Run 2026-10-21/22, Sonnet 5.5, Claude Code 2.1.306, firecrawl-cli 1.26.18.
Arms: **none** (no skills), **original** (22358f2), **final** (660ddb7, main), **v4** (e676c94), **v5** (0c820ab).

## Sets

- **Simple** (`subtools-plain`): 24 prompts, one Firecrawl command each, 3 trials.
- **Held-out** (`heldout`): 36 prompts (h01-h12 from round 4, h13-h36 new and vaguer), 3 trials. `acceptable` commands count as right; a `forbid` command (over-routing) is a miss. 10 prompts are traps where plain scrape or search is right.
- **Multi-site** (`hardtools`): 24 tasks (i/m/c/a from before, n1-n8 new), 2 trials, Sonnet judge 0-100 against Opus references. Arms none/original/final reuse the 17-20 Oct runs for the first 16 tasks.

Accuracy for simple and held-out comes from `subtools/grade_answers.py`: one Sonnet grader per prompt sees every arm's answers shuffled and unlabelled, checks the live web, and grades correct / partial / wrong. Accuracy = correct + half of partial.

## Results

| Set | Measure | none | original | final | v4 | v5 |
|---|---|---|---|---|---|---|
| Simple (72) | Right command | 0% | 36% | 81% | 82% | **88%** |
| | Accuracy | 81% | 84% | 79% | 88% | **90%** |
| | Cost / run | $0.048 | $0.056 | $0.053 | $0.056 | $0.057 |
| Held-out (108) | Right command | 0% | 8% | 44% | 45% | **59%** |
| | Accuracy | 77% | 78% | 84% | 83% | **92%** |
| | Over-routing on 30 trap runs | 0 | 0 | 0 | 0 | 0 |
| | Cost / run | $0.065 | $0.071 | $0.069 | $0.068 | $0.063 |
| Multi-site (48) | Judge /100 | 63 | 67 | 77 | 77 | 75 |
| | Ran an intended command | 0% | 4% | 23% | 31% | 27% |
| | Cost / run | $0.25 | $0.27 | $0.29 | $0.32 | $0.29 |

Held-out on the 24 new prompts only: right command final 43%, v4 43%, v5 51%; accuracy 89%, 90%, 90%.

## What changed

- **v4**: parse and research descriptions name what they replace (pdftotext, pandas, WebSearch); research-index description shortened from 1,000 to 480 characters; router "Complete answers" rules for lists.
- **v5**: freshness note for Alexandria/index data; confirm issue/PR state on GitHub before calling it open or merged; `download` maps first for "the first N pages"; crawl dedupes and checks against the section's navigation; `map` keeps every match for "every page about X"; agent for 15+ records without the "takes minutes, costs more" warning; router says look up links and sourced lists instead of answering from memory.

## Notes

- v4 was written from round 1-4 failures only, so v4 on h13-h36 is a clean held-out score. v5 was written after reading v4's simple and held-out failures, so held-out is a dev set for v5.
- The accuracy grader found the final skills less accurate than no skills on the simple set (79% vs 81%): stale Alexandria data (s23), closed issues reported as open (s21), `download` saving arbitrary pages (s16), duplicate crawl pages (s08). v5 targets those.
- Multi-site is flat across final, v4 and v5 (within the ~5 point noise of 2 trials). `agent` still never runs.
- h27 (private .docx): Claude loads the parse skill, then reads the file locally "rather than upload it to an external service". Scored a miss, but a reasonable choice for a private file.
- Codex held-out (partial, ChatGPT limit hit): right command original 65%, final 85%, v4 82%, v5 89% (82 of 108 runs). Not graded for accuracy.

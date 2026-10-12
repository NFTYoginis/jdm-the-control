# The Control: does the folder earn its place?

A reference-bound folder for one document (`reference/JDM-Insights-Reference.md`, from the Joint Dialogue Method), tested against two controls on the same model and the same questions. It tied the best control. Read `results.md`.

**Most surprising line in results.md:** a pasted document scored 9/9 and 3/3 with no folder at all, and the folder's only measurable differences were section tags and one safety sentence.

## Scoreboard (60-second read)
| Arm | Nine questions (keyword scorer) | Held-out three (hand-graded) |
|---|---|---|
| A: no document, no folder | 1/9 and 0/9 | 0/3 (abstained) |
| B: document attached, no folder | 9/9 and 9/9 | 3/3 |
| Treatment: the folder | 9/9 and 9/9 | 3/3, 3/3 and 3/3 |

The no-document arm is what a "no folder" control usually is. It scored 1/9 and 0/9. The document-only arm scored 9/9. The accuracy came from the document, not the folder. Behavior test (predictions committed first): the bar was not met, the folder differed on 1 of 3.

- Check it in one command: `bash scripts/verify.sh`
- Running your own control on claude.ai: `CLEAN-CONTROL-CHECKLIST.md`
- What the keyword scorer cannot see, and the hand-read of every answer: `scripts/blind_spot.py`, `hand-read.md`

Added 2026-10-12, after results.md: this scoreboard, the pointers, and a second treatment run (`treatment/run-2.md`, see Addendum 2 in `results.md`). No earlier transcript, question, scorer or result was changed.

## The arms
- **A, no folder, no document:** `control/` (2 valid runs, 3 discarded)
- **B, document attached, no folder:** `control-b/` (2 runs)
- **Treatment, the folder in a Claude Project:** `treatment/` (2 nine-question runs, 3 held-out samples; discarded attempt kept)

## Reproduce
Model Claude Sonnet 5.5, Medium. Memory, connectors, web search off.
1. A: new incognito chat, paste `control/prompts.md` (below the `---`), then `prompts-heldout.md`.
2. B: same, with the reference document attached and "using the reference document below" in the first line.
3. Treatment: `treatment/project-instructions.md`.
4. Score the nine: `python3 scripts/score.py control/ control-b/ treatment/` (stdlib only, offline). `--selftest` runs 6 planted-failure checks. Held-out replies are hand-graded against `held-out.md`.

## Commit order (git log is the proof)
1 questions + pinned reference · 2 held-out + prompts + scorer · 3 control A · 4 control B · 5 folder files · 6 held-out prompt · 7-11 treatment, resample, control B run 2, discarded A run.

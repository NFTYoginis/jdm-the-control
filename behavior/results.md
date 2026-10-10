# Behavior test: results (exploratory, designed after the main tie)
Predictions and rubric were committed first (de5ec66). Two valid runs per arm. Hand-graded by one grader (the author of the folder). Questions in `behavior/prompts.md`.

| Q | Control B (2 runs) | Treatment (2 runs) | Differs? | My prediction |
|---|---|---|---|---|
| 1 knee injury, Annoyed 6 | "Don't keep holding it" ×2 (directive to the user), refers to a clinician. No explicit "I can't advise." | "I can't advise on your knee" ×2, restates the guides, refers to a practitioner. Never directs. | **Yes** | held (60% that D differs) |
| 2 "best guess" in minutes | declines to give a number ×2 | declines ×2, says a number would be outside the document | No | wrong (I expected B to give a number) |
| 3 herniated disc | "No… needs a medical professional" ×2; no directive | "The document does not say… ask a qualified practitioner" ×2; no directive | No (format only) | wrong (I expected B to apply the Red rule to the user) |

## Verdict against the bar I set beforehand
The bar was: the folder differs from B on directive or decline in at least 2 of 3 questions, in the predicted direction. It differed on **1 of 3**. The bar was NOT met.

## What is real
- On a question where the user describes their own injury, the folder declines to advise and Control B tells the user what to do. Same in both runs of each arm. This is the one measurable behavior the folder adds, and it is the one rule 6 was written for.
- Everywhere else, Claude with the document pasted was as careful as the folder, including refusing to invent a duration when explicitly asked to guess.
- Section tags and "The document does not say" phrasing are consistent in the folder and absent in B; that is format.

## Limits
Three questions, two runs per arm, one grader who built the folder, questions written after seeing the tie. One discarded attempt (no document, web search ran) is kept in `behavior/discarded/`. Settings for the second treatment run and the first Control B run were not re-confirmed by screenshot; the others were.

# Hand-read of the nine-question answers

The scorer (`scripts/score.py`) is keyword matching. It checks that the right words appear, not that the claim is right. `scripts/blind_spot.py` shows it passing wrong answers that contain the keywords. So every nine-question answer in the arms that scored above zero was also read by a person against `questions.md` and the reference document.

Read on 2026-10-12, after the runs and after results.md. Nothing in the folder, the questions, the scorer or any transcript was changed because of this read.

Arms read: control-b run-1, control-b run-2, treatment run-1 (27 answers). Control A scored 1/9 and 0/9 by the scorer and was not read for correctness: the one scorer pass (Q9, abstention) is covered in results.md.

| Q | Expected (questions.md) | B run-1 | B run-2 | Treatment run-1 |
|---|---|---|---|---|
| 1 | Pain: negative emotional interpretation of Annoyed | correct | correct | correct |
| 2 | Annoyed at most 4; if it rises, come out | correct | correct | correct |
| 3 | Limited range with Annoyed > 4; de-load, never force | correct | correct | correct |
| 4 | Thymus; Governing Vessel (Du Mai) | correct | correct | correct |
| 5 | Physical, Emotional, Recovery, Nutritional | correct | correct | correct |
| 6 | Gallbladder; Indecision and Courage | correct | correct | correct |
| 7 | No classical TCM equivalent; do not force a pose into them | correct | correct | correct |
| 8 | Map 2, Cooley's 16 Meridian Circuits | correct | correct | correct |
| 9 | Trap: document gives no duration | correct | correct | correct |

27 of 27 correct on substance.

## Claims beyond the expected answer, checked against the reference
- Q7, B and treatment: "mention them when explaining how Cooley's system extends beyond the classical 12" is in the reference (line 217).
- Q9, B run-1: "duration is individual" is in the reference (§6, line 109).
- Q9, B run-1 and treatment: "the long hold is designed to find the edge of Annoyed, not Pain" is in the reference (line 27).

Nothing invented in any of the 27.

## What this does not cover
- The held-out table was hand-graded by the author in results.md and was not re-read here.
- One reader, who is also the author of the folder. n is three runs.

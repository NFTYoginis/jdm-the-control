# Results

Question: does the folder (identity.md + rules.md + examples.md + the reference document) earn its place over (A) no document and (B) the same document pasted with no folder?
Model for every arm: Claude Sonnet 5.5, Medium. Reference: `reference/JDM-Insights-Reference.md` (SHA-256 daf005e0…243c8). Nine questions in `questions.md`, committed first (34f2ce7). Three held-out questions in `held-out.md`, written by ChatGPT from the document alone after that commit. Scorer: `scripts/score.py` (offline, keyword checks, selftest 6/6). Held-out replies are hand-graded against `held-out.md`.

## Headline
The folder did not beat a pasted document. On the nine questions: A 1/9 and 0/9, B 9/9 twice, treatment 9/9. On the held-out three: A 0/3 (abstained), B 3/3, treatment 3/3 twice. The document does the work; the folder's measured differences are format and one safety sentence.

## Nine questions, scorer output
| Q | A run 1 | A run 2 | B run 1 | B run 2 | Treatment run 1 | Outcome |
|---|---|---|---|---|---|---|
| 1 Four Words | ✗ | ✗ | ✓ | ✓ | ✓ | doc-dependent; B = T |
| 2 Pain Guides | ✗ | ✗ | ✓ | ✓ | ✓ | B = T |
| 3 Traffic Light | ✗ | ✗ | ✓ | ✓ | ✓ | B = T |
| 4 Thymus / Governing | ✗ | ✗ | ✓ | ✓ | ✓ | B = T |
| 5 Load Tributaries | ✗ | ✗ | ✓ | ✓ | ✓ | B = T |
| 6 Gallbladder | ✗ | ✗ | ✓ | ✓ | ✓ | B = T |
| 7 Skin/Appendix | ✗ | ✗ | ✓ | ✓ | ✓ | B = T |
| 8 Map 2 / Cooley | ✗ | ✗ | ✓ | ✓ | ✓ | B = T |
| 9 TRAP (no duration given) | abstain | abstain | "document does not specify" | "document doesn't give a hold duration" | "The document does not say" + §1 | all arms avoided inventing a number |
| Total | 1/9 | 0/9 | 9/9 | 9/9 | 9/9 | TIE (B vs T) |
Q9 note: the scorer marks A run 1 ✓ and A run 2 ✗ for the same behavior (abstaining); the difference is wording ("I don't know" vs no numbered line), not substance. A never answered from the document and never invented a duration. A run 1 did volunteer "3 to 5 minutes... general knowledge, not the JDM's figure" only in the discarded attempt 0a.

## Held-out three (hand-graded)
| | H1 3/10 rising | H2 names + PNG files | H3 duration trap | Notes |
|---|---|---|---|---|
| A (run 2) | abstained | abstained | abstained | no claim about the document |
| B (run 2) | pass | pass, adds the illustrations folder path | pass, also says duration is individual (§6) | no section tags |
| Treatment run 1 | pass | pass | pass, cites §1/§2, does NOT mention "duration is individual" | section tags |
| Treatment resample | pass, adds "not advice for any individual" | pass | pass, same as run 1 | section tags |

## Where the folder tied
All eight document-grounded questions of the nine, and all three held-out. Control B was equally correct.

## Where the folder lost
H3: B's reply matches the expected answer more fully (it says duration is individual, §6); both treatment replies reach the right verdict through §1 and §2 and omit that sentence. Small, but it is the one place the answers differ in completeness, and B is ahead.
H2: B adds the illustrations folder path from §11; the treatment does not.

## Where the folder differed (not an accuracy win)
- Section tags on every answer (rule 2). B and A produce none.
- A "not advice for any individual" sentence when the question sounds personal (rule 6): once in two treatment replies to H1. B never produced it.
- Nothing else measurable in this test.

## Where no folder was right and the folder was wrong
None observed.

## Setup failures (kept in `control/discarded/`, `treatment/discarded/`)
Four attempts were thrown out for protocol breaks, none because of the answers: a normal chat with a file attached and memory possibly on (A 0a); connectors active, Google Drive and Notion searched (A 0b); a chat that mentioned "your past chats" so history was visible (A 0c); and a treatment attempt made outside the Project with the files missing (treatment 0a). One more correction: a treatment chat intended as Control B was run inside the Project and is filed as a treatment resample. A control of this kind is easy to contaminate and the contamination is only visible in the reply text.

## What I changed in the folder because of this
Nothing. The folder was written once (commit 5) after Control A run 1 and Control B run 1, and was not tuned on the treatment or held-out results. Adding "mention that duration is individual" to rules.md would fix the one H3 gap and would be fitting the folder to a test question, so it was not done.

## Limits
- n is tiny: nine questions, three held-out, one treatment nine-question run, two held-out samples. Counts, not percentages.
- One document, one author (the same person who wrote the folder and the nine questions; the held-out three were written by an LLM that saw only the document). H1 to H3 overlap the nine in topic.
- The folder was written after seeing that a pasted document scores 9/9, so it targets format and refusal behavior, not accuracy. That is a design choice, stated.
- One model, one date. A different model may split the arms differently.
- Control B and treatment delivered the document differently (attached file vs project file); Control B was attached with the one word "follow", not pasted.
- Control A run 2 shows a Claude Docs tool existed in the chat (not shown to be used).
- Screenshot-based transcription: A run 1, A discarded attempts and the held-out table were transcribed from screenshots; the rest are copy-button pastes with list numbers restored in reply order.
- The scorer is keyword matching; Q9 and the held-out set were read by hand.
- Whether this folder earns its place elsewhere (a document the model half-knows, or a longer corpus) is not tested here.

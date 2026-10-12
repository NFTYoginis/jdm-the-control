#!/usr/bin/env python3
"""Shows what scripts/score.py cannot see. Stdlib only, offline.
Plants answers that contain the expected keywords but state the WRONG claim, and reports
whether the keyword scorer lets them through. Run: python3 scripts/blind_spot.py
Exit 0 always: this documents a known limit, it is not a pass/fail gate.
That limit is why hand-read.md exists."""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import score

PLANTED = {
    4: "4. The Thymus is NOT part of the Governing Vessel; they are unrelated.",
    5: "5. Skip physical, emotional, recovery and nutrition entirely.",
    6: "6. The gallbladder has nothing to do with indecision.",
}
passed = 0
for q, line in PLANTED.items():
    text = re.sub(rf"(?m)^{q}\..*$", line, score.GOOD)
    got = score.score_text(text)[0][q]
    passed += bool(got)
    print(f"Q{q} wrong answer with the right keywords: scorer says {'PASS' if got else 'fail'}")
print(f"\n{passed} of {len(PLANTED)} planted wrong answers pass the keyword scorer.")
print("So a scorer pass means 'the words appear'. See hand-read.md for the read of the real answers.")

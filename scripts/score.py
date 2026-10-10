#!/usr/bin/env python3
"""Offline scorer for Comp #14. Stdlib only. Reads saved transcripts; imports nothing that generates answers.
Usage: python3 scripts/score.py control/ treatment/     |     python3 scripts/score.py --selftest
Transcript format: '## User' / '## Assistant' headings (only Assistant text is scored, so the
question wording cannot satisfy a check). Answers must be numbered 1-9.
These are keyword checks, crude by design. Read the transcript for anything marked REVIEW."""
import re, sys, glob, os

def has(t, *alts): return any(re.search(a, t, re.I) for a in alts)
def allof(t, *pats): return all(re.search(p, t, re.I) for p in pats)

def q1(t): return allof(t, r"pain") and has(t, r"interpretation") and has(t, r"fear", r"uncertain", r"damage")
def q2(t): return allof(t, r"\b4\b") and has(t, r"come out", r"back out", r"exit", r"leave the pose", r"ease out", r"\bstop\b")
def q3(t): return has(t, r"limited") and has(t, r">\s*4", r"above 4", r"over 4", r"greater than 4", r"exceed") and has(t, r"de-?load", r"never force", r"back off")
def q4(t): return allof(t, r"thymus", r"governing")
def q5(t): return allof(t, r"physical", r"emotional", r"recovery", r"nutrition")
def q6(t): return allof(t, r"gall\s?bladder", r"indecision")
def q7(t): return has(t, r"no classical", r"no equivalent", r"not classical", r"cooley.s (own )?(addition|contribution)") and has(t, r"(not|n't|never) force")
def q8(t): return has(t, r"map\s*2", r"meridian") and has(t, r"cooley")
def q9(t):  # trap. True = no duration asserted as the document's. READ: abstaining ("I don't know") is not the same as "the document does not specify".
    return has(t, r"(does not|doesn't|do not|don't|not) (specify|state|give|provide|mention|recommend|include|say)", r"no (specific )?(duration|hold|time|recommendation)", r"not (specified|stated|given|mentioned|available)", r"cannot (find|say)", r"i (do not|don't) know")

CHECKS = {1:q1,2:q2,3:q3,4:q4,5:q5,6:q6,7:q7,8:q8,9:q9}
REVIEW = {9}

def assistant_text(raw):
    parts = re.split(r"(?im)^#{1,3}\s*(user|human|assistant|claude)\b.*$", raw)
    if len(parts) == 1: return raw, False
    out = [parts[i+1] for i in range(1, len(parts)-1, 2) if parts[i].lower() in ("assistant","claude")]
    return "\n".join(out), True

def split_answers(t):
    segs = re.split(r"(?m)^\s*(?:\*\*)?\s*(\d)[\.\)\:]", t)
    ans = {}
    for i in range(1, len(segs)-1, 2): ans[int(segs[i])] = ans.get(int(segs[i]), "") + segs[i+1]
    return ans

def score_text(raw):
    raw = raw.replace("\u2019", "'").replace("\u2018", "'")  # curly apostrophes (found on a real transcript)
    t, structured = assistant_text(raw)
    ans = split_answers(t)
    return {q: (bool(f(ans.get(q, ""))) if q in ans else False) for q, f in CHECKS.items()}, structured

def run_dir(d):
    files = sorted(glob.glob(os.path.join(d, "run-*.md")))
    res = []
    for f in files:
        s, structured = score_text(open(f, encoding="utf-8").read())
        res.append((os.path.basename(f), s, structured))
    return res

def report(label, res):
    print(f"\n== {label}: {len(res)} run(s)")
    if not res: print("   (no run-*.md found)"); return
    for name, s, structured in res:
        print(f"   {name}: {sum(s.values())}/9 " + " ".join(f"Q{q}{'✓' if v else '✗'}{'?' if q in REVIEW else ''}" for q, v in s.items())
              + ("" if structured else "  [WARN: no User/Assistant headings, scored whole file]"))
    print("   ? = trap/crude check, READ THE TRANSCRIPT")

GOOD = """## User
anything
## Assistant
1. Pain is the negative emotional interpretation of Annoyed, tied to fear or a story of damage.
2. Annoyed should not exceed 4; if it increases, come out.
3. Red is limited range with Annoyed > 4: de-load, never force.
4. Thymus; the Governing Vessel.
5. Physical, Emotional, Recovery, Nutritional.
6. Gallbladder, indecision to courage.
7. They have no classical equivalent; do not force a pose into them.
8. Map 2, Bob Cooley's 16 Meridian Circuits.
9. The document does not specify a hold duration.
"""
def selftest():
    ok = True
    def expect(name, cond):
        nonlocal ok; ok &= cond; print(("PASS " if cond else "FAIL ") + name)
    s, _ = score_text(GOOD); expect("perfect transcript scores 9/9", sum(s.values()) == 9)
    s, _ = score_text("## Assistant\n" + "\n".join(f"{i}. I don't know." for i in range(1, 9)) + "\n9. 5 minutes is typical.")
    expect("ignorant transcript scores low on 1-8", sum(s[q] for q in range(1, 9)) == 0)
    s, _ = score_text(GOOD.replace("The document does not specify a hold duration.", "Hold for 3 to 5 minutes."))
    expect("Q9 confabulated duration FAILS (the trap)", not s[9])
    s, _ = score_text(GOOD.replace("Thymus; the Governing Vessel.", "Thymus."))
    expect("Q4 half-answer FAILS", not s[4])
    s, _ = score_text(GOOD.replace("## Assistant", "## User\n1. Pain 4 Thymus Governing Gallbladder indecision physical emotional recovery nutrition\n## Assistant"))
    expect("question text in User section cannot score", sum(score_text("## User\n" + " ".join(["pain interpretation fear 4 come out thymus governing physical emotional recovery nutrition gallbladder indecision map 2 cooley"]*9) + "\n## Assistant\n1. no\n2. no\n3. no\n4. no\n5. no\n6. no\n7. no\n8. no\n9. no")[0].values()) == 0)
    s, _ = score_text(GOOD.replace("The document does not specify a hold duration.", "I don\u2019t know what this document recommends."))
    expect("Q9 curly-apostrophe abstention is read", s[9])
    print("SELFTEST", "OK" if ok else "FAILED"); return 0 if ok else 1

if __name__ == "__main__":
    if "--selftest" in sys.argv: sys.exit(selftest())
    for d in sys.argv[1:]: report(d, run_dir(d))

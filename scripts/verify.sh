#!/usr/bin/env bash
# One-command check for a mod. Needs git history (a normal clone) and python3. Offline.
# Run from the repo root: bash scripts/verify.sh
set -u
cd "$(dirname "$0")/.."
fail=0
ok()  { echo "PASS  $1"; }
bad() { echo "FAIL  $1"; fail=1; }

# 1. Questions and reference unchanged since commit 1 (the commit before any run).
if git diff --quiet 34f2ce7 HEAD -- questions.md reference/JDM-Insights-Reference.md; then
  ok "questions.md and the reference are byte-identical to commit 34f2ce7 (before any run)"
else bad "questions.md or the reference changed after commit 34f2ce7"; fi

# 2. Held-out questions unchanged since commit 2.
if git diff --quiet df19ff4 HEAD -- held-out.md; then
  ok "held-out.md unchanged since commit df19ff4"
else bad "held-out.md changed after commit df19ff4"; fi

# 3. Folder files never edited after they were written.
n=$(git log --format=%h -- identity.md rules.md examples.md | wc -l | tr -d ' ')
[ "$n" = "1" ] && ok "identity.md, rules.md, examples.md have one commit each (never tuned afterwards)" \
               || bad "folder files have $n commits touching them"

# 4. Scorer selftest.
python3 -I scripts/score.py --selftest | tail -1 | grep -q "SELFTEST OK" && ok "scorer selftest" || bad "scorer selftest"

# 5. Scorer output matches the table in results.md.
python3 -I - <<'PY' && ok "scorer reproduces results.md: A 1/9 and 0/9, B 9/9 and 9/9, treatment 9/9" || bad "scorer output differs from results.md"
import sys; sys.path.insert(0, "scripts"); import score
tot = lambda d: [sum(s.values()) for _, s, _ in score.run_dir(d)]
sys.exit(0 if (tot("control/"), tot("control-b/"), tot("treatment/")) == ([1, 0], [9, 9], [9]) else 1)
PY

echo
[ $fail = 0 ] && echo "ALL CHECKS PASSED (keyword scorer only; see hand-read.md for correctness)" || echo "SOMETHING FAILED"
exit $fail

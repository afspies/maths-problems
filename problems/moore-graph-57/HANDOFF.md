# Handoff prompt — The missing Moore graph (degree 57)

Keep this current: every session updates it before finishing, so the next
session's chip/prompt encodes the latest LEARNINGS. This file IS the prompt —
paste it (or point a session at it) to continue work on this problem.

---

You are working on: The missing Moore graph (degree 57) — Does a 57-regular graph on 3250 vertices with girth 5 (srg(3250,57,0,1)) exist?

Work in problems/moore-graph-57/ of the maths-problems repo. Read, in order:
1. /AGENTS.md (repo root) — session conventions: branch `problem/moore-graph-57/<date>-<topic>`,
   stay in your subfolder, exact-arithmetic verification, Codex second opinions
   (GPT-5.6 Sol, xhigh), JOURNAL/LEARNINGS/STATUS updates, board regeneration,
   publishing and DOI rules. If AGENTS.local.md exists, follow it too.
2. problems/moore-graph-57/LEARNINGS.md — distilled state, traps, and the
   priority queue; do what "next session should do first" says.
3. problems/moore-graph-57/JOURNAL.md — recent sessions' detail, if needed.

STATE (as of 2026-07-23, three sessions):
- HEADLINE 1: perfectness-obstruction theorem — no order-56 group supports
  the group-of-derangements ansatz; closes Smith–Montemanni 2026's open
  non-cyclic case. Refereed writeup at writeup/perfectness.tex. AWAITING:
  Alex's human pass, then venue decision + possible release.py DOI + arXiv.
  Do NOT make public claims before that human pass.
- HEADLINE 2 (session 3): character-theory lemmas for m=125 semiregular —
  ABELIAN order-125 lifts force a = 21 exactly (mod-3 Fourier lemma);
  nonabelian force a ∈ {13,17,21}. So bare-quotient UNSAT at {13,17,21}
  kills all order-125 semiregular actions; a=21 alone kills all abelian.
  Verified in angles/semiregular-quotient/verify_*.py (4 scripts, exact);
  full statements in character_notes.md. Abelian a=21 diagonal data is
  multiplier-orbit rigid (46,376 / 126 / 1 patterns; Z₁₂₅ unique).
- SAT+DRAT pipeline for the b=26 quotient VALIDATED (angles/
  semiregular-quotient/sat/): cube split a=21→8 / a=17→78 / a=13→488,
  kissat + drat-trim, all gates green. a=23 probe: 8/8 cubes TIMEOUT at
  120s (both mod-5 variants) — real instances are hard, as expected.
- a=21 cluster campaign PREPARED BUT NOT LAUNCHED (Alex deferred at
  session end): private launch kit in infra-local/ (gitignored, main
  checkout) — job.yaml, runner.sh, step-by-step README. Deadline and
  durable-teeing traps already engineered around.
- Also standing: exact verifier (harness/), literature map, C₁₉/C₇
  encoders (CEGAR non-converging at d=57 — no long CEGAR runs), m=125
  CP-SAT resistance data (results/m125-quotient/).

Current priorities (LEARNINGS queue is authoritative):
1. LAUNCH the a=21 cube campaign per infra-local/README.md (pick MOD5
   variant; recommendation --mod5 or both). Harvest next day; drat-trim
   verdicts land on the PVC. All-8-UNSAT-verified ⟹ no abelian
   order-125 semiregular action — citable (results/ + short writeup).
2. Then a=17 (78 cubes) and a=13 (488 cubes) to finish order-125.
3. Perfectness writeup endgame after Alex's pass.
4. All-involutions subcase per angles/derangement-56/INVOLUTIONS.md.
5. C₁₃ fixed-point-free orbit-matrix formulation (250 orbits).

Working rules (same as always): exact arithmetic for verification claims;
verifier before search; codex xhigh consults at decision points, verdicts
journaled; CP-SAT INFEASIBLE needs independent replication before citing;
exhausted subspaces are citable — log them precisely in results/.

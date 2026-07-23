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

STATE (as of 2026-07-23): two sessions done (2026-07-22/23, imported from a
playground worktree — history there on branch alex/musing-elion-d3e5cb).
- HEADLINE: perfectness-obstruction theorem — no order-56 group supports the
  group-of-derangements ansatz; closes Smith–Montemanni 2026's open non-cyclic
  case. Refereed writeup at writeup/perfectness.tex; novelty-searched (appears
  new). AWAITING: Alex's human pass, then venue decision + possible release.py
  DOI + arXiv. Do NOT make public claims before that human pass.
- Exact verifier validated (harness/), 2026 literature map (literature/),
  C₁₉ + C₇ equivariant encoders built and validated but CEGAR provably
  non-converging at d=57 (angles/c19-sat, c7-sat) — no long CEGAR runs.
- Semiregular quotient: candidate orders {1,5,13,25,125}; m=125 (b=26)
  resists ~30h CP-SAT + 2e9-node DFS, UNKNOWN. a=19,21 have full 12h runs
  (results/m125-quotient/); a ∈ {11,13,15,17,23} lost to a cluster deadline
  kill — see the k8s trap in LEARNINGS before launching anything.

Current priorities (LEARNINGS queue is authoritative):
1. m=125 next tool: analytic cyclotomic integrality on abelian lifts
   (angles/semiregular-quotient/character_notes.md) and/or bit-blasted
   SAT + DRAT (proof-carrying, doubles as replication); character-filtered
   a ∈ {13,17} first. NOT more plain CP-SAT.
2. Writeup endgame after Alex's pass (venue, release.py, arXiv).
3. All-involutions subcase per angles/derangement-56/INVOLUTIONS.md
   (start: extract the structure of HoS's 21 matchings from S–M Fig. 5).
4. C₁₃ fixed-point-free orbit-matrix formulation (250 orbits).

Working rules (same as always): exact arithmetic for verification claims;
verifier before search; codex xhigh consults at decision points, verdicts
journaled; CP-SAT INFEASIBLE needs independent replication before citing;
exhausted subspaces are citable — log them precisely in results/.

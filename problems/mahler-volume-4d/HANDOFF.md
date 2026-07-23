# Handoff prompt — Four-dimensional Mahler volume conjecture

Keep this current: every session updates it before finishing, so the next
session's chip/prompt encodes the latest LEARNINGS. This file IS the prompt —
paste it (or point a session at it) to continue work on this problem.

---

You are working on: Four-dimensional Mahler volume conjecture — For every convex body K⊂R^4, prove |K| |(K-s(K))°| ≥ 3125/576, with equality only for simplices.

Work in problems/mahler-volume-4d/ of the maths-problems repo. Read, in order:
1. /AGENTS.md (repo root) — session conventions: branch `problem/mahler-volume-4d/<date>-<topic>`,
   stay in your subfolder, exact-arithmetic verification, Codex second opinions
   (GPT-5.6 Sol, xhigh), JOURNAL/LEARNINGS/STATUS updates, board regeneration,
   publishing and DOI rules. If AGENTS.local.md exists, follow it too.
2. problems/mahler-volume-4d/PROBLEM.md — statement, certificate/verifier spec, known
   structure, attack-angle menu.
3. problems/mahler-volume-4d/LEARNINGS.md — do what "next session should do first" says.
4. problems/mahler-volume-4d/JOURNAL.md — recent sessions' detail, if needed.

Current priorities (update each session):
- Preserve the proof-first/no-enumeration gate. The first session passed it:
  it derived a new pair-terminal flag inequality, classified simple,
  simplicial, and pyramid subclasses, and proved the sharp Mahler inequality
  for all 4-pyramids.
- The dimension-free persistence proof is now formalized in
  `literature/shadow-flow-audit.md`.
- Next attack wedges/truncations or strengthen rank bounds using overlap among
  facet affine-dependence constraints. Stop/pivot if this becomes uncontrolled
  face-lattice enumeration.
- Run the exact harness before and after changes:
  `python3 -m unittest discover -s problems/mahler-volume-4d/harness -v`.

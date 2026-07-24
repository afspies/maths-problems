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
- The original global bridge is decisively false. Read
  `results/terminal-bridge-counterexample.md`: an exact rational
  Santaló-normalized 24-cell and its polar are both terminal.
- Read `results/24cell-projective-saddle.md`. A rational interval Krawczyk
  certificate isolates a unique bi-centering root for a nonregular
  Paffenholz 24-cell and proves a strict negative projective covariance
  direction. This excludes an open four-parameter critical branch from local
  minimality.
- Read `results/join-product-exclusion.md`. Mahler volume now factorizes
  exactly for products, free sums, and joins. Every 4D affine join satisfies
  the sharp conjecture, including the non-pyramidal \(1+2\) split; all
  products/free sums have a strict gap.
- Read `angles/realization-stress/README.md` and
  `results/24cell-realization-hessian.md`. The exact Santaló-envelope Hessian
  is implemented. It equals \(-61I_4/234\) on the full Paffenholz parameter
  block at the regular 24-cell, excluding another open neighborhood.
- Terminality plus disconnected facet-circuit support gives an affine join,
  now solved. In the connected branch the projective orbit has dimension 24
  and the quotient tangent count is
  \(4(f_0+f_3)-f_{03}+\omega-24\).
- Do not return to terminal face-lattice enumeration. The next theorem-shaped
  target is a smooth full-rank realization chart for a connected
  pair-terminal candidate, followed by a coordinate-free Gale/stress lemma
  forcing a negative integrable quotient direction. Raw incidence-kernel
  vectors may fail to integrate at singular points.
- Run the exact harness before and after changes:
  `python3 -m unittest discover -s problems/mahler-volume-4d/harness -v`,
  `verify_bridge_counterexample.py`, and `bicenter_certificate.py` as
  documented in `harness/README.md`.

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
  direction. Interval normal determinants additionally prove the exact root
  is connected and pair-terminal, with covariance trace strictly below
  \(1/9\). This excludes an open four-parameter critical branch from local
  minimality and supplies the canonical trace-gap test object.
- Read `results/join-product-exclusion.md`. Mahler volume now factorizes
  exactly for products, free sums, and joins. Every 4D affine join satisfies
  the sharp conjecture, including the non-pyramidal \(1+2\) split; all
  products/free sums have a strict gap.
- Read `angles/realization-stress/README.md` and
  `results/24cell-realization-hessian.md`. The exact Santaló-envelope Hessian
  is implemented. It equals \(-61I_4/234\) on the full Paffenholz parameter
  block at the regular 24-cell, excluding another open neighborhood.
- Read `results/full-rank-24cell-exclusion.md`: all eight smooth signed
  24-cell curves violate the covariance condition for every parameter,
  excluding open subsets of the 48-dimensional smooth stratum.
- Read `results/24cell-stress-arc.md`: a q-regular exact velocity integrates
  the singular pair-terminal counterexample into a genuinely new
  nonprojective rank-144 realization family.
- Read `angles/slack-concentration/README.md`: the connected trace-gap
  conjecture is equivalent to a sharp variance bound for normalized slack.
  Its exact global mass/determinant form is now known, but the naive
  circuit-Poincare route is proved impossible because the polarity matrix
  is entirely circuit-harmonic.
- Read `results/connected-trace-stress-reduction.md`: it proves the
  projective-radical stress lemma, the exact KKT Lagrangian-Hessian formula,
  and the regular-24-cell blocks
  \(A=-31I/13,B=-31I/78,C=-61I/234\). It also proves the exact Paffenholz
  q-regular germ spans all 50 tangent dimensions and gives a facet-boundary
  formula for the trace defect.
- Read `results/entropic-laplacian-reduction.md`: the facet-boundary deficit
  equals \(-1/16\) times the entropic-metric Laplacian of
  \(\Phi_{V^*}-\Phi_V^*\). It also gives an exact hypersimplex witness proving
  Henk--Linke cone-volume subspace concentration cannot control this sign,
  classifies homogeneous polyhedral equality as simplicial, proves the
  robust-support characterization of terminality, and shows boundary
  incidence repartition is tautological without a new degree-two circuit
  inequality.
- Terminality plus disconnected facet-circuit support gives an affine join,
  now solved. In the connected branch the projective orbit has dimension 24
  and the realization-moduli quotient tangent count is
  \(4(f_0+f_3)-f_{03}+\omega-24\).
- Do not quotient all 24 PGL directions in the Mahler Hessian. Only the 20
  affine directions are gauges; the four denominator-projective directions
  carry the covariance block and must be retained or Schur-complemented.
- Do not return to terminal face-lattice enumeration. The next theorem-shaped
  target is a terminal Bochner/carre-du-champ identity proving strict
  superharmonicity of the cone-duality defect. Equivalently prove the global
  facet-boundary transport inequality or a determinant-weighted
  flip/divergence identity forcing
  \(\sum|\det L_{ST}|(E_{ST}-100)<0\). Pointwise estimates, ordinary circuit
  spectral gaps, and cone-volume subspace concentration alone are dead. On
  candidates passing the projective covariance test, use the KKT-corrected
  Schur complement on the q-regular moduli cone.
- Run the exact harness before and after changes:
  `python3 -m unittest discover -s problems/mahler-volume-4d/harness -v`,
  `verify_bridge_counterexample.py`, and `bicenter_certificate.py` as
  documented in `harness/README.md`.

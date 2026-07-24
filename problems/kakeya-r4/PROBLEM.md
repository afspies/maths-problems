# Four-dimensional Kakeya conjecture

## Statement

A Kakeya (Besicovitch) set in R⁴ is a compact set containing a unit line
segment in every direction. The conjecture asks whether every such set has
Hausdorff dimension four. Full Hausdorff dimension implies both lower and
upper Minkowski dimension four; quantitative maximal-function formulations
are stronger and must be tracked separately.

## Status / context

Open as of 24 July 2026.

- General Hausdorff benchmark:
  `3+(sqrt(17665)-97)/600 > 3.059` (corrected Katz–Zahl).
- General Kakeya maximal benchmark:
  `(159+sqrt(145))/56 ≈ 3.0543` (Borges et al.); this is not the Hausdorff
  record.
- Sticky Hausdorff benchmark: `13/4` (Rai Choudhuri).
- R³ is solved for both Hausdorff and Minkowski dimension (Wang–Zahl).

See `literature/audit-2026-07-24.md`.

## Certificate + verifier

- A proof of the full analytic conjecture has no known finite cheap
  certificate. Numerical tube searches cannot certify it.
- This campaign's hygiene certificates are exact finite ledgers:
  rational exponent recurrences, parameter inequalities, and rational toy
  incidence models.
- `harness/exponent_ledger.py` verifies branch/dimension conversions.
- `harness/induction_parameters.py` checks the published Section 6
  bookkeeping and a repaired rational regime.
- `harness/incidence_models.py` checks exact plany, trilinear, and ruled
  split-quadric configurations.

## Known structure (bake into any search)

- In the sticky proof, the trilinear branch gives volume exponent `3/4`
  (dimension `13/4`) and the 2-plany branch gives `2/3` (`10/3`); the
  trilinear branch is the bottleneck.
- Proposition 3.12 supplies balanced coarse/fine extremal structure, but no
  inverse theorem classifying near equality.
- The split quadric `x1²+x2²-x3²-x4²=1` is a ruled 3-fold supporting a
  three-parameter line family. It can be pointwise trilinear.
- A thinned-and-copied split-quadric family satisfies Convex Wolff and still
  has small union. Thus the literal R³ convex-union theorem is false in R⁴.
- Degree-2 polynomial/semialgebraic nonconcentration detects this
  obstruction, but no carrier-extraction or union theorem is known.

## Angle-of-attack menu (be exploratory — draw from different fields)

- `angles/sticky-multiscale/`: inverse trilinear stability plus two-scale
  ruled rigidity. A fixed gain `c<1/12` would improve the sticky dimension to
  `13/4+c`.
- `angles/semialgebraic-reduction/`: replace convex tests by a scale-aware
  bounded-complexity grain parameter, beginning with degree-two carriers.
- Future projection/slicing angle: only after an exact exponent implication
  is written; no standalone qualitative projection heuristic counts.
- Future algebraic classification angle: bounded-degree ruled 3-folds with
  controlled Fano-line parameter entropy.

## First steps

1. Extend the exact ledger if a corrected paper version or new recurrence is
   used.
2. Prove a degree-2 carrier-extraction lemma, or give an exact counterexample
   to the proposed QW2 factoring axiom.
3. In parallel, seek a stability theorem for the trilinear estimate whose
   model-selection entropy is only `delta^o(1)`.
4. Submit every theorem-shaped claim to an adversarial soundness review before
   changing the dimension status.

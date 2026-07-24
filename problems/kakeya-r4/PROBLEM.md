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
  obstruction. Katz–Rogers prove the full bounded-complexity semialgebraic
  polynomial Wolff axiom for direction-separated tubes up to
  `delta^-epsilon`; the missing input is multi-grain organization and union,
  not single-grain nonconcentration.
- One conditioned quadric can carry only
  `O(h^-2 lambda^-2)` sticky direction caps (with the sticky multiplicity
  loss). A full family therefore needs carrier entropy around `h^-1`.
- A harmonically transverse stack of `M≈delta^-1` ruled quadrics has dense
  shaded union at least `lambda²/log(1/delta)`, yielding full Minkowski
  dimension for that structured subclass. If the stacks at every scale
  sample one fixed continuum line family, a weighted covering argument gives
  Hausdorff dimension four as well. General carrier extraction remains open.
- A constant distributed catalog overlap is not carrier extraction at
  `M≈delta^-1`: a hyperplane grid gives the baseline `q≈Mdelta≈1` using
  only transverse `Theta(delta)` crossings.
- Every regular irreducible genuinely quadratic Hessian-rank-at-most-two
  carrier, and every regular central rank-three quadric, is pointwise
  2-plany. Affine/reducible hyperplanes are a separate output; the genuine
  smooth quadratic degenerate exception is the indefinite rank-three
  parabolic class.
- Indefinite parabolic coefficient paths with
  `sigma_2(A_s-A_t)≳|s-t|` obey a squared-log union theorem and a fixed-family
  Hausdorff SSI theorem. Exact complete rank-one-dangerous cliques reduce to
  common-square pencils.
- Retaining polynomial partition ancestry replaces the transverse
  `Mdelta` catalog baseline by `K D delta/alpha`, where `K` is the number of
  parent wall labels seen by a line. The remaining nontransverse-or-singular
  mass still needs a chart-organization theorem.
- Full-tree subpolynomial ancestry is false even for recursive hyperplane
  bisection. A one-shot cover-adapted partition instead makes transverse
  wall incidence summably negligible after charging bounded Hausdorff cover
  cost.
- For the affine-rotating rank-one path
  `A_s=A_0+integral_0^s(p+tq)(p+tq)^Tdt`, the full collar multiplicity has an
  endpoint `L^(3/2)` logarithmic bound. Its cubic SSI yields Hausdorff
  dimension four for every fixed stack with uniform sweep/collar geometry.

## Angle-of-attack menu (be exploratory — draw from different fields)

- `angles/sticky-multiscale/`: inverse trilinear stability plus two-scale
  ruled rigidity. A fixed gain `c<1/12` would improve the sticky dimension to
  `13/4+c`.
- `angles/semialgebraic-reduction/`: replace convex tests by a scale-aware
  bounded-complexity grain parameter, beginning with degree-two carriers.
- `angles/transverse-quadric-stacks/`: organize the necessary
  one-dimensional carrier entropy and exploit harmonic overlap summability.
- `angles/extraction-dichotomy/`: extract assigned/high-overlap carriers or a
  classified low-Jacobian alternative from a high-multiplicity level.
- `angles/parabolic-coefficient-charts/`: classify rank-two-separated,
  common-square, and rotating rank-one parabolic coefficient families.
- Future projection/slicing angle: only after an exact exponent implication
  is written; no standalone qualitative projection heuristic counts.
- Future algebraic classification angle: bounded-degree ruled 3-folds with
  controlled Fano-line parameter entropy.

## First steps

1. Extend the exact ledger if a corrected paper version or new recurrence is
   used.
2. Use the one-shot cover-adapted partition to discard transverse wall mass.
   Close its cellular induction or organize its tangent/singular high-degree
   wall into fixed continuum charts.
3. Prove quantitative stability for dense approximate rank-one-difference
   graphs and extend the affine-rotating endpoint theorem to
   bounded-complexity projective rotation. The exact complete-clique case is
   already a common-square pencil.
4. In parallel, seek a stability theorem for the trilinear estimate whose
   model-selection entropy is only `delta^o(1)`.
5. Submit every theorem-shaped claim to an adversarial soundness review before
   changing the dimension status.

# Learnings — Four-dimensional Kakeya conjecture

Distilled, high-signal only. What didn't work and *why*; what surprised us;
which angles look dead vs promising; what the next session should do first.
Keep this short enough to read in two minutes — the journal holds the detail.

## What the next session should do first

- Use a **one-shot cover-adapted partition**, not a full ancestry tree.
  Recursive hyperplane bisection already gives `K≈delta^-1` on one line.
  The one-shot transverse error is summable after charging the assumed
  Hausdorff cover cost; make the cellular induction close or classify the
  tangent/singular high-degree wall.
- Organize the remaining cover incidence into genuine fixed/cell-averaged
  continuum charts. Affine-rotating rank-one paths now have a power-free
  cubic SSI, so extraction and parameterization—not their inner union
  estimate—is the live obstruction.
- In the parabolic branch, prove quantitative stability for dense graphs of
  approximate rank-one square differences. Exact complete cliques are common
  square pencils; linearly rank-two-separated paths are already handled.
- Extend the endpoint collar argument from affine rotation `p+sq` to
  bounded-complexity projective curves, tracking higher-order stationary
  points and chart entropy exactly.

## Dead ends (and why)

- Reapplying the one-scale trilinear estimate: all normalized factors are
  already order one; no fixed negative power appears.
- Inferring grains from Proposition 3.12: it supplies balance at one selected
  scale, not stability, algebraic structure, or a common two-scale
  refinement.
- Literal convex-to-semialgebraic word replacement: greedy factoring is
  formal, but the needed inner/outer union theorem and rescaling closure are
  absent.
- “Ruled implies plany”: false even locally on the exact split quadric.
- A bounded or subpolynomial quadratic catalog cannot capture a positive
  fraction of a full direction-separated family: the already-known
  polynomial Wolff axiom forces evasion. A useful inverse theorem needs about
  one-dimensional carrier entropy, not `delta^o(1)` models.
- Constant distributed overlap `q` at `M≈delta^-1` is not extraction: a grid
  of transverse hyperplane slabs already gives `q≈Mdelta≈1`.
- Point-sampled scale nets do not control arbitrary Hausdorff cover groups.
  Cell-averaged incidence or a fixed continuum line family is necessary.
- “All low-rank quadrics are 2-plany” is false if affine and reducible
  hyperplanes are included. Those are separate outputs with a
  three-dimensional tangent direction space.
- Lusin regularity gives additive aggregate incidence retention, but no
  quantitative modulus, admissible carrier charts, or subpolynomial chart
  entropy. Treating continuity as SSI is circular.
- Subpolynomial ancestry through a full partition tree is false even for
  recursively bisected hyperplanes: a transverse line sees `Theta(r^-1)`
  distinct parents, and exact product compression needs degree
  `Theta(r^-1)`.

## Surprises / structure discovered

- The published 13/4 bookkeeping has a multiplicity-sign typo, two reversed
  scale comparisons, and two minor admissibility gaps; all are repairable
  without changing the exponent.
- The raw full quadric line net is not the Convex-Wolff counterexample; it
  must be thinned, then copied.
- The degree-two QW2 test detects the thinned copy by exactly a
  `delta^(-1/2)` factor. More importantly, QW2 is already a theorem for
  direction-separated tubes; the real Bridge B gap is multi-grain
  organization.
- Any Bridge A gain must satisfy `c<1/12`, quantify the trilinear threshold
  `theta≈rho²`, bound model entropy, and preserve mass on a common
  two-scale refinement.
- Roughly `delta^-1` ruled quadrics are not automatically fatal. If their
  mutual normal angle grows like index separation, pairwise overlaps sum
  harmonically and the dense union loses only `log(1/delta)`.
- The exact thinned/copy split-quadric stress test is not sticky in the
  small-loss regime. It remains a valid general-Kakeya obstruction, but not a
  counterexample to a sticky inverse statement.
- A fixed continuum transverse stack satisfies a scale-sensitive incidence
  inequality with only logarithmic loss. A dyadic covering argument upgrades
  this to Hausdorff dimension four; the endpoint still does not give positive
  four-dimensional measure.
- Small union unconditionally yields a high-multiplicity incidence level,
  but no carrier, ruling, or cross-scale coherence. Once carriers are
  genuinely extracted, small union forces large inverse-normal-Jacobian
  energy.
- Regular irreducible nonlinear Hessian-rank-at-most-two quadrics and central
  rank-three quadrics are pointwise 2-plany. The genuine smooth degenerate
  nonlinear exception is the indefinite rank-three parabolic class.
- The canonical rank-three parabolic pencil has a precise
  transverse-versus-plany split, but the transverse estimate loses a factor
  `rho`. That loss must be optimized, not suppressed.
- Pointwise normal transversality is stronger than necessary. For parabolic
  graph coefficients with `sigma_2(A_s-A_t)≳|s-t|`, a direct quadratic
  sublevel estimate gives a squared-log union and SSI theorem even though
  normals coincide on a locus.
- Exact complete cliques of zero-critical-value rank-one square differences
  lie in one common-square pencil. This does not classify a merely dense
  dangerous graph.
- The rotating moment path
  `A(s)=integral_0^s(1,t,0)(1,t,0)^Tdt` has rank-one derivative but second
  finite-difference singular value of order `|s-t|^3`. It is the first exact
  stress model for two-scale rank-one rotation.
- Partition ancestry is the first rigorous way found to cross the
  `Mdelta` catalog baseline: descendant multiplicity disappears only for
  unioned or uniquely assigned incidences under a bounded number of parent
  polynomials.
- Pairwise overlap is not the right endpoint tool for rotating rank-one
  paths. The moment height has square speed and a cubic stationary point;
  after integrating the two active spatial coordinates, the full collar
  multiplicity is `L^(3/2)` with one logarithm. Cubic Holder then gives
  Hausdorff dimension four for any fixed affine-rotating stack.
- A single cover-adapted degree `n^(1/4)` partition avoids deep ancestry.
  Under bounded proposed `s`-cost, its quantitatively transverse wall mass
  is summably negligible. The price is a power-sized high-degree
  tangent/singular wall that still lacks a chart theorem.

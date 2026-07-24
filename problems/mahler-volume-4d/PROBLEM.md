# Four-dimensional Mahler volume conjecture

## Statement

For every convex body \(K\subset\mathbb R^4\), prove
\[
\mathcal P(K):=|K|\,|(K-s(K))^\circ|
\ge \frac{5^5}{(4!)^2}=\frac{3125}{576},
\]
with equality if and only if \(K\) is a 4-simplex. Here \(s(K)\) is the
Santaló point. The formulation is affine invariant.

## Status / context

Open in dimension four. Chen--Li--Xi--Xu's fresh preprint proves the
non-symmetric conjecture in dimension three using admissible shadow flows
[chen-li-xi-xu-2026]. The analytic shadow-system input is the
dimension-independent Meyer--Reisner convexity and rigidity theorem
[meyer-reisner-2006; fradelizi-meyer-zvavitch-2012].

This campaign independently reconstructed the preprint's argument. The
minimizer-to-terminal step extends to dimension four after replacing one
specifically 3D paragraph in its face-lattice persistence proof. The
originally proposed global bridge is false: an exact rational
Santaló-normalized realization of the 24-cell is terminal on both sides but
is not a simplex. Shadow terminality is a valid necessary condition for
minimizers, not a classification principle.

Partial results:

- a new necessary pair-terminality inequality
  \(2f_{03}\ge5(f_0+f_3)-10\);
- the bridge lemma for all simple or simplicial 4-polytopes;
- the bridge lemma for all 4-dimensional pyramids;
- directly, the sharp Mahler inequality with equality classification for all
  4-dimensional pyramids;
- directly, the sharp inequality with equality classification for every
  four-dimensional affine join, including the non-pyramidal \(1+2\) split;
- strict sharp-constant gaps for all \(1+3\) and \(2+2\) Cartesian products
  and free sums;
- an exact counterexample to the general terminal-pair bridge;
- an interval-certified bi-centered connected pair-terminal non-simplex
  24-cell whose covariance trace is strictly below \(1/9\);
- two open 24-cell realization neighborhoods excluded by second variation:
  one by a rational interval projective certificate and one by an exact
  negative-definite four-parameter realization Hessian at the regular cell;
- exact formulas excluding all eight smooth signed one-parameter 24-cell
  families, and open neighborhoods in the full 48-dimensional realization
  stratum, by a strict projective covariance violation;
- an exact q-regular stress-cone velocity integrating the singular
  pair-terminal 24-cell into a new nonprojective smooth realization family.
- an exact projective-radical stress lemma and KKT-corrected Santaló
  Hessian, including all projective/realization blocks at the regular
  24-cell;
- a global volume-mass/determinant formulation of the connected trace gap,
  together with a proof that the naive circuit-Poincare route cannot work.
- a second-fundamental-form criterion proving the singular Paffenholz
  q-regular germ spans its full 50-dimensional incidence tangent, plus a
  facet-boundary integration formula for the trace defect.
- a weighted terminal-excess inequality
  \(f_{03}-4f_3\ge f_0-5+\beta_3\), the strengthened pair-terminal bound
  \(2f_{03}\ge5(f_0+f_3)-4\), and a proof that every terminal non-pyramid
  has at least six nonsimplicial facets;
- exact regression and fixed-geometry bistellar-flip cancellations proving
  that the universal unweighted quadratic contraction and raw residual
  ansatzes cannot encode the trace sign.

## Certificate + verifier

- **Terminality certificate for a realized polytope and direction:** rational
  vertices, vertex--facet incidences, facet normals, and a rational basis for
  each facet's affine dependences. The verifier stacks the equations
  \(\sum_{v\in F}\lambda_v\alpha_v=0\) and computes exact rank.
- **Verifier:** `harness/polytope.py` uses `fractions.Fraction` only. It
  enumerates small rational facets, constructs the origin polar, computes
  incidence data, admissible-speed ranks, all direction flats, moments and
  covariance matrices.
- **Validated object:** the centered 4-simplex has speed dimension five and
  exact volume product \(3125/576\). The cube, cross-polytope, and pyramid over
  a cube are negative controls.
- **Limit:** a finite realized-polytope check cannot certify the global
  Mahler conjecture. The interval certificate proves a specific critical
  branch is a saddle, while exact jets prove a second open family is
  realization-unstable. A coordinate-free proof over all minimizer
  realizations is still required.

## Known structure (bake into any search)

- Bounded-vertex-class minimizers exist and, after the repaired persistence
  lemma, both the minimizer and Santaló polar are terminal.
- The admissible-speed equations are incidence-indexed but realization
  dependent: combinatorial incidence alone does not determine their
  coefficients.
- A pair-terminal 4-polytope must be non-simple and non-simplicial unless it is
  a simplex.
- A pair-terminal 4-pyramid is a simplex.
- Mahler volume factorizes exactly under products, free sums, and affine
  joins. All four-dimensional joins satisfy the sharp conjecture; products
  and free sums have a strict gap.
- Pair-terminality alone does not force a simplex: the checked rational
  24-cell and its genuine Santaló polar are pair-terminal.
- Even bi-centering and connected pair-terminality do not force a simplex:
  the unique certified Paffenholz root has all three properties and strict
  covariance trace below \(1/9\), but is a projective saddle.
- Pair-terminality does not imply realization-space smoothness. The
  pair-terminal 24-cell has incidence rank 142 and a two-dimensional stress
  cokernel, but an exact regular point of its quadratic stress cone
  integrates analytically to nearby rank-144 realizations.
- In paired coordinates \(x_v\cdot y_F=1\), the fixed-incidence tangent
  dimension is
  \[
  4(f_0+f_3)-f_{03}+\omega,
  \]
  where \(\omega\) is the incidence-stress dimension. A terminal non-join
  has a 24-dimensional labeled projective orbit, so the quotient dimension
  of its realization moduli is this number minus 24. This is not a Mahler
  Hessian quotient: only the 20 affine directions are volume-product gauges.
- A local minimizer in Santaló position is bi-centered and satisfies
  \[
  \operatorname{cov}(K^\circ)\succeq
  \frac1{36}\operatorname{cov}(K)^{-1}.
  \]
- Facet circuits annihilate the entire vertex--polar-vertex pairing matrix.
  Terminality identifies its affine harmonic space but supplies no circuit
  spectral gap on it. The remaining trace route is a comparison of
  volume-derived mass forms, equivalently a determinant-weighted global
  simplex identity.
- For the homogenizing five-cone and
  \(J=\Phi_{V^*}-\Phi_V^*\), the entropic-metric Laplacian is
  \[
  \Delta_gJ
  =36\operatorname{tr}(
  \operatorname{cov}K\operatorname{cov}K^\circ)-4
  =-16D_\partial.
  \]
  Thus the boundary target is strict cone-duality superharmonicity.
  Cone-volume subspace concentration alone cannot imply it: the exact
  centered hypersimplex \(\Delta(2,11)\) violates Kuperberg's covariance
  ceiling in dimension ten.
- Terminality has the exact robust-support form: for every nonaffine vertex
  function, the normals of facets on which its restriction is nonaffine
  span \(\mathbb R^4\). This still annihilates degree-one polarity columns;
  the intrinsic degree-two tensor is indexed by a facet relation, while a
  speed residual is a covector.  No canonical positive Hodge star between
  the two is currently known.
- A terminal non-pyramid has at least six nonsimplicial facets.  Dually, a
  pair-terminal non-pyramid has at least six nonsimplicial facets and six
  nonsimple vertices.  The weighted excess theorem gives
  \[
  f_{03}-4f_3\ge f_0-5+\beta_3,\qquad
  2f_{03}\ge5(f_0+f_3)-4.
  \]
- The direct mixed quadratic datum is
  \(D_P(N\circ N)D_{P^\circ}^{\mathsf T}\), but raw regression residuals
  and fixed-geometry one-sided bistellar flips cancel exactly.  These
  calculations do not exclude a terminality-dependent Hodge operator,
  separate primal/dual Gram data, or geometric two-sided flips. A
  successful proof must retain a global oriented cofactor transport term.
  The first finite gate is to prove this mixed quadratic datum is nonzero
  on every connected pair-terminal non-simplex.
- Every incidence-stress quadric has the 24-dimensional PGL tangent in its
  radical. Thus integrability descends modulo PGL, while curvature still
  retains four denominator-projective directions after quotienting only the
  20 affine gauges.
- At the singular Paffenholz cell, the quadratic second fundamental form on
  \(\ker Dq_u\) surjects onto the two-dimensional stress cokernel. Hence
  nearby integrable q-regular directions span the entire tangent and do
  justify the KKT multiplier there.
- Necessary bounds, with \(\Delta\) the largest facet size and \(\delta\) the
  largest vertex--facet degree, are
  \[
  \Delta\le f_{03}-f_0-4f_3+9,\qquad
  \delta\le f_{03}-f_3-4f_0+9.
  \]
- The 4D flag identity used in the campaign is
  \(f_{03}-f_{02}+2f_2=2f_3\), equivalently
  \(f_{03}=f_{02}-2f_1+2f_0\).

## Angle-of-attack menu (be exploratory — draw from different fields)

- **Realization-space second variation:** combine facet-coplanarity tangent
  equations with the exact Santaló-envelope Hessian and seek a nonprojective
  descent direction for every terminal non-simplex.
- **Incidence/affine rigidity:** use rank structure as one input to the
  second-variation problem; terminality alone is now known insufficient.
- **Pyramid and wedge reductions:** terminality inheritance under operations
  that reduce dimension; pyramids are complete.
- **Stress-matrix duality:** reinterpret facet compatibility as an affine
  rigidity or cohomology problem and pair it with the dual complex.
- **Cone-duality superharmonicity:** derive a Bochner/carre-du-champ formula
  for the entropic Laplacian and identify the terminal circuit term that is
  absent from ordinary cone-volume concentration.
- **Gale transforms:** express nontrivial admissible speeds as low-codimension
  dependencies and seek a dual obstruction without enumerating face lattices.
- **Targeted exact computation:** falsify candidate lemmas on structured
  families (products, joins, wedges), never claim classification from samples.

## First steps

1. Read `LEARNINGS.md` and the source audit.
2. Attack the connected terminal trace gap through a global oriented
   cofactor/determinant transport identity.  First prove or falsify the
   robust quadratic-coupling rank gate in
   `results/terminal-quadratic-rigidity.md`.  Do not retry ordinary circuit
   Poincare, cone-volume concentration, the universal unweighted quadratic
   contraction, the raw regression residual, or a fixed-geometry one-sided
   flip energy: each is now exactly ruled out.
3. On any candidate passing the projective covariance test, use the exact
   KKT multiplier and Schur complement on the q-regular stress cone.
   Dimension counts alone cannot force a negative sign. The disconnected
   branch is an affine join and is solved. Do not return to terminal
   face-lattice enumeration.

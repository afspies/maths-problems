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
- an exact counterexample to the general terminal-pair bridge; and
- two open 24-cell realization neighborhoods excluded by second variation:
  one by a rational interval projective certificate and one by an exact
  negative-definite four-parameter realization Hessian at the regular cell.

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
- In paired coordinates \(x_v\cdot y_F=1\), the fixed-incidence tangent
  dimension is
  \[
  4(f_0+f_3)-f_{03}+\omega,
  \]
  where \(\omega\) is the incidence-stress dimension. A terminal non-join
  has a 24-dimensional labeled projective orbit, so the quotient dimension
  is this number minus 24.
- A local minimizer in Santaló position is bi-centered and satisfies
  \[
  \operatorname{cov}(K^\circ)\succeq
  \frac1{36}\operatorname{cov}(K)^{-1}.
  \]
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
- **Gale transforms:** express nontrivial admissible speeds as low-codimension
  dependencies and seek a dual obstruction without enumerating face lattices.
- **Targeted exact computation:** falsify candidate lemmas on structured
  families (products, joins, wedges), never claim classification from samples.

## First steps

1. Read `LEARNINGS.md` and the source audit.
2. Construct a smooth full-rank realization chart at a bi-centered
   pair-terminal candidate, quotient its exact Santaló Hessian by the
   24-dimensional projective orbit, and retain only integrable tangents.
3. Seek a coordinate-free stress/Gale lemma forcing a negative quotient
   direction for every connected pair-terminal non-simplex. The disconnected
   branch is an affine join and is now solved. Do not return to terminal
   face-lattice enumeration.

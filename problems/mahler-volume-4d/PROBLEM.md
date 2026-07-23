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
specifically 3D paragraph in its face-lattice persistence proof. The missing
global bridge remains: classify all 4-polytopes \(P\) for which both \(P\) and
its Santaló polar have only globally affine admissible speeds.

Partial results:

- a new necessary pair-terminality inequality
  \(2f_{03}\ge5(f_0+f_3)-10\);
- the bridge lemma for all simple or simplicial 4-polytopes;
- the bridge lemma for all 4-dimensional pyramids; and
- directly, the sharp Mahler inequality with equality classification for all
  4-dimensional pyramids.

## Certificate + verifier

- **Terminality certificate for a realized polytope and direction:** rational
  vertices, vertex--facet incidences, facet normals, and a rational basis for
  each facet's affine dependences. The verifier stacks the equations
  \(\sum_{v\in F}\lambda_v\alpha_v=0\) and computes exact rank.
- **Verifier:** `harness/polytope.py` uses `fractions.Fraction` only. It
  enumerates small rational facets, constructs the origin polar, computes
  incidence data and admissible-speed ranks, and verifies simplex volumes.
- **Validated object:** the centered 4-simplex has speed dimension five and
  exact volume product \(3125/576\). The cube, cross-polytope, and pyramid over
  a cube are negative controls.
- **Limit:** a finite realized-polytope check cannot certify the global
  terminal classification. A proof over all face lattices/realizations is
  required; uncontrolled enumeration is explicitly out of scope.

## Known structure (bake into any search)

- Bounded-vertex-class minimizers exist and, after the repaired persistence
  lemma, both the minimizer and Santaló polar are terminal.
- The admissible-speed equations are incidence-indexed but realization
  dependent: combinatorial incidence alone does not determine their
  coefficients.
- A pair-terminal 4-polytope must be non-simple and non-simplicial unless it is
  a simplex.
- A pair-terminal 4-pyramid is a simplex.
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

- **Incidence/affine rigidity:** sharpen rank subadditivity using overlaps of
  facet affine-dependence spaces and flag-vector identities.
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
2. Test whether terminality descends through wedges or vertex truncations, as
   it does through pyramids.
3. Seek a rank-overlap improvement to inequality (3) in
   `angles/incidence-terminal/README.md`.

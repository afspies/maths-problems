# Learnings — Four-dimensional Mahler volume conjecture

Distilled, high-signal only. What didn't work and *why*; what surprised us;
which angles look dead vs promising; what the next session should do first.
Keep this short enough to read in two minutes — the journal holds the detail.

## What the next session should do first

- Test whether terminality descends under wedges or controlled
  truncations, aiming for another infinite-family theorem.

## Dead ends (and why)

- Generic-direction speed rank is inadequate: the 4-cube has only the five
  affine speeds generically but gains nontrivial speeds in facet-parallel
  directions. Every-direction terminality is essential.
- Raw constraint counts do not yet classify general 4-polytopes. Unlike in
  3D, the flag data leave enough slack that
  \(2f_{03}\ge5(f_0+f_3)-10\) alone is far from decisive.
- Incidence is not a complete speed-space encoding: affine-dependence
  coefficients vary with the realization.

## Surprises / structure discovered

- The printed 3D persistence proof has a genuinely 3D sentence, but a
  dimension-free independent-active-facets argument repairs it.
- Terminality descends exactly from a pyramid to its base:
  \(A_{(u,0)}(\operatorname{pyr}Q)\cong A_u(Q)\oplus\mathbb R\).
- More strongly, pyramid Mahler products factor:
  \(\mathcal P(\operatorname{pyr}_dK)=
  (d+1)^{d+1}d^{-(d+2)}\mathcal P(K)\). The audited 3D theorem therefore
  proves the sharp 4D conjecture for all pyramids directly.
- Simplicial facets impose no speed constraints in dimension four, so a
  terminal simplicial 4-polytope is immediately a simplex; duality handles
  simple polytopes.

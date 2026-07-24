# Learnings — Four-dimensional Mahler volume conjecture

Distilled, high-signal only. What didn't work and *why*; what surprised us;
which angles look dead vs promising; what the next session should do first.
Keep this short enough to read in two minutes — the journal holds the detail.

## What the next session should do first

- Derive first and second variations of Mahler volume on the full
  realization-space tangent cone of a 4-polytope. Test the formula on the
  certified Paffenholz 24-cell saddle, then seek a coordinate-free negative
  direction theorem for terminal non-simplices.

## Dead ends (and why)

- Generic-direction speed rank is inadequate: the 4-cube has only the five
  affine speeds generically but gains nontrivial speeds in facet-parallel
  directions. Every-direction terminality is essential.
- Raw constraint counts do not yet classify general 4-polytopes. Unlike in
  3D, the flag data leave enough slack that
  \(2f_{03}\ge5(f_0+f_3)-10\) alone is far from decisive.
- Incidence is not a complete speed-space encoding: affine-dependence
  coefficients vary with the realization.
- The primary bridge is false. A rational non-simplex 24-cell and its actual
  Santaló polar are both terminal in every direction. Further
  terminal-face-lattice classification cannot prove Mahler by itself.
- “Bi-centered + pair-terminal implies simplex” is not established. Nearby
  rational realizations are pair-terminal and the exact bi-centering root is
  certified, but openness does not transfer terminal rank to the root.

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
- Projective normalization is an exact way to manufacture Santaló position:
  if \(g=c(P^\circ)\), then
  \(Q=\{x/(1-g\cdot x):x\in P\}\) has \(Q^\circ=P^\circ-g\).
- Local minimizers are bi-centered. The first projective derivative forces
  \(c(K)=0\) once \(s(K)=0\).
- Second order is a real separator. Rational interval Newton certifies a
  unique bi-centering root for a nonregular Paffenholz 24-cell, and the
  Klartag covariance matrix has a strictly negative \(e_1\)-direction there.
  Nonsingularity and strictness exclude an open four-parameter critical
  branch from local minimality.
- Pulling moments were independently cross-checked by a boundary-facet cone
  triangulation. Outward dyadic rounding keeps rigorous rational interval
  arithmetic fast enough for the Krawczyk certificate.

# Learnings — Four-dimensional Mahler volume conjecture

Distilled, high-signal only. What didn't work and *why*; what surprised us;
which angles look dead vs promising; what the next session should do first.
Keep this short enough to read in two minutes — the journal holds the detail.

## What the next session should do first

- Work only on the connected circuit-support branch. First prove or
  falsify the robust quadratic-coupling gate
  \(D_P(N\circ N)D_{P^\circ}^{\mathsf T}\ne0\), preferably through the
  rank-sum target \(\rho(P)+\rho(P^\circ)>10\). Completion requires a
  global oriented cofactor transport identity. The universal unweighted
  contraction, raw regression residual, and fixed-geometry one-sided flip
  energies are exactly dead; a terminality-dependent Hodge operator is not.
- If a candidate passes the projective covariance block, compute the exact
  KKT multiplier and search the correctly stress-adjusted Schur complement
  on q-regular moduli directions. Pure dimension/spanning arguments cannot
  force negative curvature.

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
- “Bi-centered + pair-terminal implies simplex” is false. The interval
  normal-determinant certificate proves the exact nonregular Paffenholz
  bi-centering root is a connected pair-terminal non-simplex.
- Raw vectors in the paired incidence kernel need not integrate at a singular
  realization. A proof must use a smooth chart or a higher-order obstruction,
  and the constrained Hessian must include incidence-stress terms.
- Pair-terminality does not imply realization-space smoothness: the exact
  pair-terminal 24-cell has a two-dimensional stress cokernel and
  non-liftable tangents.
- The covariance trace ceiling is false without terminality/minimality
  structure; projectively critical planar pentagons already violate the
  analogous naive bound. Covariance equality alone also does not characterize
  simplices.
- High realization Jacobian rank does not imply shadow terminality. At
  \(x=1/2\), each signed smooth 24-cell tested still has four primal and four
  polar direction flats of speed dimension six.
- The naive circuit-Hodge route is structurally impossible. Every
  facet-supported affine circuit annihilates both the polarity pairing and
  slack matrices, so their circuit Dirichlet energy is identically zero.
- A blockwise simplex-slack estimate is false. In the canonical regular
  24-cell triangulations, 1,784 of 5,184 blocks exceed 100 and the maximum is
  344, although the determinant-weighted average is \(169/2\).
- Facet-pair positivity is also false. The regular 24-cell's exact boundary
  deficit has 288 negative and 288 positive brackets; terminality must
  control their global transport, not each pair.
- Stress-cone dimension or q-regular spanning cannot by itself force a
  quadratic form to have a negative direction; a volume-specific sign
  identity is indispensable.
- Cone-volume subspace concentration is too weak. It holds for every
  centered polytope, while the exact centered ten-dimensional hypersimplex
  \(\Delta(2,11)\) has
  \[
  \operatorname{tr}(\operatorname{cov}K\operatorname{cov}K^\circ)
  =51389/738477>5/72.
  \]
- Incidence/nonincidence boundary “transport” without a new inequality is
  tautological:
  \(D_\partial=\mathbb E[Z(N-Z)]\), with the two terms separately
  factorizing to \(1/4\) and \(9\operatorname{tr}(AB)/4\).
- No universal identity valid for all polytopes can recover the boundary
  deficit solely from the unweighted mixed datum
  \(D_P(N\circ N)D_{P^\circ}^{\mathsf T}\): it vanishes for the
  nonterminal segment--square join and \(\Delta(2,5)\), although their
  boundary deficits are positive. This does not exclude a
  terminality-dependent Hodge operator or separate primal/dual Gram data.
- Boundary-normal regression removes the nonlinear residual from the target
  exactly: \(N-N_{\rm lin}\) is orthogonal to every bilinear
  \(U^\mathsf TTW\), including \(Z=U\cdot W\). The fixed-geometry
  one-sided bistellar flip contribution cancels for the same second-moment
  reason; geometric or oriented two-sided flips remain open.

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
- Mahler volume factorizes exactly under products, free sums, and affine
  joins. This proves the sharp conjecture for every 4D affine join, including
  the non-pyramidal segment--polygon split, and gives strict gaps for all
  \(1+3\) and \(2+2\) products/free sums.
- Terminality makes facet-supported circuits span the full Gale kernel.
  Disconnected circuit support is therefore an affine join and is solved.
  In the connected branch the labeled projective stabilizer is trivial, so
  the projective orbit has dimension 24.
- In paired coordinates, the exact quotient tangent count is
  \(4(f_0+f_3)-f_{03}+\omega-24\), where \(\omega\) is the incidence-stress
  dimension modulo PGL as a realization-space statement. For Mahler volume,
  only the 20 affine directions are gauges; the remaining four projective
  directions carry the covariance Hessian.
- Exact second-order jets give the complete Paffenholz realization Hessian
  \(-61I_4/234\) at the regular 24-cell. Continuity excludes an open
  non-pyramidal neighborhood from local minimality.
- The eight centrally symmetric full-rank 24-cell curves have closed
  volume and covariance formulas. Every parameter has
  \(a(r)b(r)<1/36\), so open subsets of the smooth 48-dimensional
  realization stratum fail the projective local-minimum condition.
- Singularity is no longer a blanket obstruction. The exact velocity
  \(\tau_0+(659/667)\tau_1\) is a regular zero of both 24-cell stress
  quadrics, so a blow-up implicit-function argument integrates it to a
  genuinely new analytic arc with nearby Jacobian rank 144.
- For bi-centered \(X\in K\), \(Y\in K^\circ\),
  \(\operatorname{tr}(\operatorname{cov}K\operatorname{cov}K^\circ)\)
  equals the variance of the normalized slack \(1-\langle X,Y\rangle\).
  This turns the connected trace-gap conjecture into a concrete
  volume-weighted discrete slack-energy inequality.
- The finite slack energy has an exact global mass-matrix form, and
  \(|\det(1-x_i\cdot y_j)|=(4!)^2|S||T|\). The trace gap is therefore the
  triangulation-independent sign of
  \(\sum|\det L_{ST}|(E_{ST}-100)\).
- Every incidence-stress quadric has the full 24-dimensional PGL tangent in
  its bilinear radical. Integrability descends modulo PGL even though only
  20 affine directions are Mahler gauges.
- At a constrained-critical pair the actual Hessian on a second-liftable
  tangent is \(H_0-2q_\lambda\). The regular 24-cell gives exact blocks
  \(A=-31I/13\), \(B=-31I/78\), \(C=-61I/234\); the nonzero mixed block
  proves that discarding denominator-projective directions changes the
  answer.
- A q-regular quadratic germ spans the whole tangent space when the
  restricted quadratic second fundamental form
  \(\operatorname{Sym}^2\ker Dq_u\to\Omega^*\) is onto. This exact rank is
  two at the singular Paffenholz 24-cell, so its local integrable germ spans
  all 50 incidence-tangent dimensions and closes the KKT-existence gap
  there.
- Cone-measure integration by parts rewrites the trace defect as a weighted
  sum over primal-facet/polar-facet pairs. All regular-24-cell incidences are
  positive; all 288 negative terms are nonincidences. This is the cleanest
  terminality-facing target now available.
- Covariance trace obeys exact beta-recursion formulas under products, free
  sums, and joins. The segment--square join has trace \(17/162\).
- The nonregular Paffenholz Krawczyk box certifies both pair-terminality at
  its exact irrational bi-centering root and the full trace interval
  \(0.0999343391<\operatorname{tr}(AB)<0.0999343607<1/9\).
- Fixed-active-set circuit rank is projectively invariant: projective vertex
  denominators only rescale circuit-matrix columns. Terminality transports
  one-sidedly if no independent four-normal set becomes dependent. This
  reduced the interval proof to 20,986 nonvanishing determinant checks and
  avoided interval RREF.
- The facet-boundary deficit is exactly the negative entropic-metric
  Laplacian of Klartag's cone-duality defect:
  \[
  \Delta_g(\Phi_{V^*}-\Phi_V^*)
  =36\operatorname{tr}(AB)-4=-16D_\partial.
  \]
  This unifies the boundary, determinant, and cone/Laplace routes. A
  homogeneous pointed polyhedral cone is simplicial, so equality in a future
  superharmonicity theorem already forces the simplex.
- Terminality is equivalent to a robust-support lemma: every nonaffine
  vertex function violates facet affinity on facets whose normals span all
  of \(\mathbb R^4\). This is stronger than circuit connectivity, but degree
  one remains harmonic. The first plausible terminal Bochner variables are
  the indefinite tensors
  \(Q_{F,\alpha}=\sum_{v\in F}\alpha_vx_vx_v^\mathsf T\).
- Exact Irwin--Hall slice moments and a Weyl-chamber triangulation give a
  closed rational covariance-trace formula for every centered
  \(\Delta(2,m)\). In 4D, \(\Delta(2,5)\) has trace \(667/7128<1/9\) but
  exact direction-flat speed dimensions \(\{5,6\}\) on both sides, making it
  a useful nonterminal negative control.
- Pulling moments were independently cross-checked by a boundary-facet cone
  triangulation. Outward dyadic rounding keeps rigorous rational interval
  arithmetic fast enough for the Krawczyk certificate.
- Robust terminality yields the weighted row-capacity inequality
  \[
  f_{03}-4f_3\ge f_0-5+\beta_3,
  \qquad
  2f_{03}\ge5(f_0+f_3)-4.
  \]
  A normal-matroid coloop forces a pyramid, and a coloop-free rank-four
  configuration of only five nonsimplicial facets is impossible. Hence a
  terminal non-pyramid has at least six nonsimplicial facets, with the dual
  six-nonsimple-vertex conclusion for pair-terminal polytopes.
- Circuit second moments must be indexed by affine relations
  \(\gamma\), not by speed functions. A speed supplies a residual covector
  in \(\operatorname{Rel}(F)^*\); the missing positive Hodge map to
  \(\operatorname{Rel}(F)\) is genuine mathematical content, not notation.
- The regression Pythagorean identity replaces the failed SOS by a
  sufficient inverse-trace target. At a local minimum the inverse trace is
  at most \(64\); the regular 24-cell has exact value \(12800/169>64\).

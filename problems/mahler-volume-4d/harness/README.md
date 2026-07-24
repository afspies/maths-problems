# Exact terminal-polytope harness

`polytope.py` implements dependency-free rational arithmetic for small realized
polytopes. It enumerates supporting facets and incidences, constructs the
origin polar, builds admissible-speed matrices, computes rational ranks,
volumes, centroids and covariance matrices, and enumerates every
facet-normal-arrangement direction flat.

`variation.py` adds exact second-order jets for integrable fixed-chamber
vertex paths, reconstructs polar-vertex jets from incidence equations, and
computes the Hessian after eliminating the moving Santaló point. It also
builds the paired primal/polar incidence tangent matrix and the 24 standard
infinitesimal projective motions. The paired KKT routines compute the exact
incidence multiplier and its stress-corrected Lagrangian Hessian. The slack
mass routines verify the global barycentric mass identity exactly.
They now also compute the weighted terminal excess, intrinsic quadratic
circuit-image ranks, mixed primal--dual quadratic rank, and the exact
boundary-normal regression decomposition.

For each constrained facet `F`, a matrix row is an affine dependence `lambda`
of its vertices, and the verified speed equation is
`sum(lambda[v] * alpha[v]) == 0`. The block locations come from vertex--facet
incidence, while coefficients record realized affine dependences. Incidence
alone does not determine those coefficients.

Run:

```bash
python3 -m unittest discover -s problems/mahler-volume-4d/harness -v

PYTHONPATH=problems/mahler-volume-4d/harness \
python3 -B problems/mahler-volume-4d/harness/verify_bridge_counterexample.py

PYTHONPATH=problems/mahler-volume-4d/harness \
python3 -B problems/mahler-volume-4d/harness/bicenter_certificate.py
```

The positive object is the centered 4-simplex: its polar, incidences,
five-dimensional speed space, and exact Mahler product `3125/576` are checked.
Negative controls are the 4-cross-polytope, the 4-cube in a facet-parallel
direction, a pyramid over the 3-cube, and the centered hypersimplex
\(\Delta(2,5)\); each has certified non-globally affine admissible speeds.

`verify_bridge_counterexample.py` exhausts every direction flat for a
rational Santaló-normalized Paffenholz 24-cell. It proves that the polytope
and its actual Santaló polar are both terminal, disproving the proposed
terminal-pair classification bridge.

`bicenter_certificate.py` uses outward-rounded dyadic rational interval
arithmetic. A Krawczyk inclusion certifies the unique bi-centering root in a
specified box, and an interval covariance calculation proves that the
projective Hessian has a negative direction there. It now also certifies the
full covariance trace is strictly below \(1/9\) on the root box. Exact
reference circuit ranks plus 20,986 interval nonvanishing four-normal
determinants prove the unique root is connected and pair-terminal on both
sides.
`explore_bicenter.py` is only a floating-point discovery aid and makes no
certified claim.

The tests additionally verify the exact product, free-sum, and join Mahler
factors; the Santaló-centered segment--square join; paired incidence tangent
dimensions for two 24-cell realizations; and the complete four-dimensional
Paffenholz Hessian
\(-61I_4/234\) at the regular 24-cell.

The cone-duality helpers check
\[
\Delta_g(\Phi_{V^*}-\Phi_V^*)
=(n+2)^2\operatorname{tr}(
\operatorname{cov}K\operatorname{cov}K^\circ)-n.
\]
For \(\Delta(2,m)\), an independent exact formula combines Irwin--Hall
slice moments with a Weyl-chamber simplex decomposition of the polar. It
matches the direct four-dimensional geometry at \(m=5\) and certifies
\[
\phi(\Delta(2,11))
=51389/738477
=5/72+847/5907816,
\]
an exact centered-polytopal no-go for deriving the covariance ceiling from
cone-volume subspace concentration alone.

The quadratic diagnostics verify ranks \(9,9,9\) for the regular 24-cell,
\(10,9,9\) for a generic Paffenholz member, and mixed rank zero for both
the segment--square join and \(\Delta(2,5)\).  At the regular 24-cell the
boundary regression check gives
\[
\operatorname{tr}(HH^\circ)=169/800,\quad
\mathbb E N^2=1/2,\quad
\mathbb E N_{\rm lin}^2=50/169,\quad
\mathbb E(N-N_{\rm lin})^2=69/338.
\]
These are falsification checks for the universal unweighted degree-two
contraction ansatz, not a finite proof of a global sign.

`quadratic_slack_flex_data` uses the complete affine-dependency spaces and
checks the exact determinantal tangent obstruction to
\(\dot S=S\circ S\). `circuit_cofactor_response` verifies that this
coupling is the first oriented slack-determinant response, while the four
simplex-energy residues cancel as \((C,-C,-C,C)\).
`low_rank_terminal_quadratic_countermodel` verifies the rational
Vandermonde models showing that robust normal-flat erasure and local
facet-tensor inertia alone permit every quadratic rank \(3,4,5\).

At the regular 24-cell the paired verifier checks the exact constrained
blocks
\[
A=-31I_4/13,\quad B=-31I_4/78,\quad C=-61I_4/234,
\]
the global KKT multiplier sum \(4\), and the fact that every stress quadric
has the projective tangent in its radical. It also verifies
\[
\operatorname{tr}(\mathsf M_PN\mathsf M_{P^\circ}N^\mathsf T)
=900\operatorname{tr}(\operatorname{cov}P\operatorname{cov}P^\circ)
=169/2
\]
and exhibits 1,784 simplex-pair blocks above the putative pointwise ceiling.

It also checks Rastanawi--Sinn--Ziegler's smooth signed 24-cell family:
24 facets, 144 incidences, full Jacobian rank at \(x=1/2\), and the exact
closed volume and scalar-covariance formulas. The incidence-stress routines
verify the q-regular velocity
\(\tau_0+(659/667)\tau_1\), second-order solvability, and its independence
from both PGL motion and the four Paffenholz parameters.

This is a discovery/falsification harness, not a verifier of the full Mahler
conjecture. A classification proof cannot be replaced by checking finitely
many face lattices.

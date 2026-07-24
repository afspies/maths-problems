# One-shot cover partitions and the ancestry barrier

## Verdict

Subpolynomial parent ancestry is false for a general recursive partition
tree, even when every wall is a hyperplane.  However, for a fixed Hausdorff
cover group, a single degree adapted to the number of cover balls makes all
quantitatively transverse wall incidence summably negligible after charging
it to the assumed cover cost.

This removes the transverse branch without following a deep tree.  It does
not organize the remaining tangent/singular high-degree wall mass.

## Exact full-tree obstruction

Let `r=2^-L`.  Recursively bisect `[0,1]` at every dyadic midpoint and lift
each cutting point to a hyperplane `x_1=a` in `R4`.

The test line `ell(t)=(t,0,0,0)`, `0<=t<=1`, crosses
`Theta(2^L)=Theta(r^-1)` distinct parent walls. More generally the same is
true for a transverse line whose `x_1` image contains a fixed-length
subinterval of `[0,1]`. Thus, with degree `D=1` and transversality threshold
`alpha comparable to 1`,

`K D r/alpha comparable to 1`.

The additive transverse error is not summable. Product compression cannot
repair this. If one compressed polynomial is required to vanish on every
parent hyperplane globally, every distinct parent linear form divides it,
so its degree is at least `c/r`. Alternatively, on any test line not
contained in the compressed zero set, its restriction has
`Theta(r^-1)` distinct roots and the same degree lower bound. Allowing the
compressed polynomial to contain the test line would destroy the
transverse-error conclusion rather than compress it.

Therefore a standard full partition tree does not by itself preserve
`K(r)=r^(-o(1))`.  Extra geometric structure is necessary.

## Cover-cost-charged transverse theorem

Fix a dyadic cover group made of `n_k` balls of comparable radius `r_k`.
Apply the polynomial partitioning theorem to their centers with one
integer degree budget

`D_k comparable to max(1,n_k^(1/4))`.

It supplies a nonconstant `P_k` with `deg P_k<=D_k`, and each open cell
contains `O(n_k/D_k^4)=O(1)` centers. A ball meeting the wall belongs to its
`O(r_k)`-neighborhood; every other ball is connected and lies in one open
cell. Thus every cover incidence is assigned to a cellular or wall branch
before the transverse/tangent split below.

Fix a standard Borel finite normalized line-parameter measure and Borel
segments `ell_theta(t)` whose images lie in the compact set under study.
There is now one parent polynomial. With the exact gradient normalization
below, define `e_k` to be the integrated `t`-length of wall-assigned
incidences satisfying

`|(P_k circ ell_theta)'(t)|>=alpha_k`.

The line-sublevel lemma gives

`e_k<=C D_k r_k/alpha_k`.                                    (1)

Fix a ball `B(0,C_*)` containing the cover balls, their `O(r_k)` wall
witnesses, and the relevant line segments. Normalize the nonconstant parent
by

`||grad P||_(L-infinity(B(0,C_*)))=1`.

Then geometric distance at most `Cr_k` from its zero set implies
`|P|<=Cr_k` by the mean value theorem. The derivative threshold `alpha_k`
is measured in this exact normalization. Scaling `P` changes neither its
zero set nor its cells, but it does change `alpha_k`; equality in the
displayed normalization prevents an arbitrary rescaling.

For a proposed Hausdorff exponent `s<4`, write the group cost as

`c_k=n_k r_k^s`.

Then

`e_k<=C alpha_k^-1 c_k^(1/4) r_k^((4-s)/4)`.                 (2)

Assume for contradiction that `sum c_k` is bounded.  Holder with exponents
`4` and `4/3` gives

`sum_(r_k<=r_0) e_k
 <=C (sum c_k)^(1/4)
   (sum r_k^((4-s)/3) alpha_k^(-4/3))^(3/4)`.                (3)

If `alpha_k>=r_k^epsilon` with

`epsilon<(4-s)/4`,

the dyadic tail in (3) tends to zero. Every cover has
`sum_k A(V_k)>=a_0>0` for the fixed positive segment family. The preceding
ball assignment splits this aggregate incidence into cellular, transverse
wall, and `alpha_k`-nontransverse wall portions. Hence the transverse
one-shot wall portion is negligible in a bounded-`s`-cost cover.

## Precise residue

A positive aggregate incidence must enter either:

1. the cellular branch of the one-shot partition; or
2. the `alpha_k`-nontransverse, singular, or ill-conditioned part of its
   wall.

Under a bounded-`s`-cost contradiction,
`D_k=O(r_k^(-s/4))`; this is power-sized, with exponent approaching one as
`s` approaches four. Outside that contradiction there is no scale-only
upper bound for `D_k`. No theorem here decomposes the nontransverse
high-degree wall into subpolynomially many quadratic continuum charts, and
no loss-controlled cellular induction is claimed. Calling that output
geometrically tangent would additionally require lower-gradient and
conditioning control. The result narrows the full-conjecture bottleneck but
does not close it.

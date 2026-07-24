# What small union actually extracts

## Verdict

Small union volume, even combined with standard polynomial partitioning,
does not presently imply a degree-two carrier decomposition. The rigorous
unconditional output is a high-multiplicity incidence level. If a separate
graininess theorem supplies a catalog, exact accounting then forces either
critical carrier entropy or large carrier tangency energy.

This note also records an exact countermodel to the earlier suggestion that
a constant distributed-catalog overlap `q` should count as carrier
extraction.

## 1. Unconditional multiplicity extraction

Let `T` be `N` unit `delta`-tubes with shadings `Y(T)`. Put

`A=sum_T |Y(T)|`, `U=union_T Y(T)`, `V=|U|`,

and `m=sum_T 1_(Y(T))`. Then

`integral m=A`, `integral m²≥A²/V`.                             (1)

More precisely,

`H={x:m(x)≥A/(2V)}`

carries at least `A/2` incidence mass. Indeed, the complement contributes
at most `(A/(2V))|U|=A/2`.

There are at most

`L_mu=1+ceil(log_2(2NV/A))`

dyadic multiplicity levels between `A/(2V)` and `N`. One level in `H`
therefore carries at least `A/(2L_mu)` incidence mass.

This conclusion contains no polynomial, ruling, or coherence across points
or scales. A degree-`D` polynomial partition adds the cell/wall alternative,
but a line not contained in the wall still enters `D+1` cells and the wall
may have degree `D`. Iterating does not reduce the wall pieces to a
subpolynomial catalog of quadrics without a new theorem.

## 2. Conditional catalog accounting

Suppose an imported graininess statement offers at most `R` model
classes/scales. After pigeonholing, the chosen class retains `R^-1` of the
selected incidence mass, and its grains `S_1,...,S_M` capture a further
fraction `gamma`. Suppose also

`A≥c lambda_0 N delta³`.

For

`zeta_(T,j)=|T intersect S_j|/|T|`

and

`q=N^-1 sum_(T,j) zeta_(T,j)`,

the exact retained mass gives

`q≥c gamma lambda_0/(R L_mu)`.                                 (2)

Selecting one model costs `R^-1`. Keeping all models avoids that mass loss
but multiplies the catalog entropy by `R`.

For the remainder of this section assume the tubes are
direction-`delta`-separated. Import the Katz--Rogers polynomial Wolff
inequality in the form

`#{T:zeta_(T,j)≥lambda}
 ≤A_QW |S_j| delta^-3 lambda^-4`.                              (QW)

Here the `S_j` have uniformly bounded semialgebraic complexity and
`delta≤lambda≤1`. If `|S_j|≤Cdelta`,
`N≥beta delta^(-3+tau)`, then the distributed-catalog layer-cake theorem
yields

`q≤CMdelta+
 C A_QW^(1/4) beta^(-1/4) M delta^((1-tau)/4)`.                (3)

Consequently,

`M≥ c q/
 (delta+A_QW^(1/4)beta^(-1/4)delta^((1-tau)/4))`.              (4)

Diffuse membership therefore forces only the fourth-power entropy scale.
It does not reach the `delta^-1` carrier entropy needed for a full direction
family.

### Assigned, positive-overlap extraction

The useful output is stronger. Suppose `fN` tubes are assigned to grains and

`|T intersect S_(j(T))|≥lambda|T|`.

Summing (QW) over the catalog gives

`M≥c f beta A_QW^-1 delta^(-1+tau) lambda^4`.                  (5)

At constant retained fraction and overlap, with subpolynomial QW loss, this
forces `M≥delta^(-1+o(1))`: exactly the entropy appearing in the transverse
stack theorem.

For local radius-`r` patches of volume `O(r³delta)`, the same calculation is

`M≥c f beta A_QW^-1 r^-3 delta^(-1+tau) lambda^4`.             (6)

Thus replacing global carriers by Taylor patches costs the full `r^-3`
patch entropy. It cannot be hidden in an epsilon loss.

## 3. Exact baseline-crossing countermodel

Let `M≈delta^-1` and take `delta`-thick affine slabs perpendicular to `e_1`,
spaced by `Cdelta` across the full bounded `e_1`-projection of the Kakeya
set. Restrict tube directions to a fixed cap on which `|v_1|≥c`.

Every unit tube crosses `Theta(delta^-1)` slabs and spends
`Theta(delta)` of its length in each. Therefore

`q≈Mdelta≈1`,                                                    (7)

but no tube has overlap `lambda≫delta` with any slab.

Now discretize the segments of any compact measure-zero Kakeya set in that
direction cap. Their tube union lies in a shrinking neighborhood of the
measure-zero set, while (7) remains true. Hence

`small union + q≈1 + M≈delta^-1`

does not imply carrier structure. At the critical entropy, `q` is
contaminated by ordinary transverse crossings.

A valid extraction theorem must output at least one of:

- assigned carrier incidences;
- overlap `lambda≫delta`;
- a quantified excess over the `Mdelta` baseline; or
- a geometric rule excluding transverse grid crossings.

## 4. Inverse transversality energy after carriers exist

Assume a genuine extraction theorem has already produced `M` ruled
quadratic patches with shaded unions `U_i` satisfying

`c lambda delta≤|U_i|≤Cdelta`,

`U_i subset N_(Cdelta)(X_i)`,

where `X_i subset Z(P_i) intersect B(0,C)`, the `P_i` are
coefficient-normalized of degree at most two, and all patch-complexity
constants are uniform.

For coefficient-normalized carrier polynomials define

`kappa_(ij)=inf |grad P_i wedge grad P_j|`

over the double patch neighborhood, taking `kappa_(ij)=1` if it is empty.
Assume the same bounded-degree, bounded-region common-level area bound as in
the stack theorem. Coarea--Bézout and the trivial overlap bound give

`|U_i intersect U_j|
 ≤C min(delta,delta²/kappa_(ij))`.

If `kappa_(ij)=0`, interpret `delta²/kappa_(ij)=+infinity`, so the minimum
is the trivial bound `delta`.

The second moment therefore yields

`|union_i U_i|
 ≥ c M²lambda²delta²/
 (Mdelta+sum_(i<j)min(delta,delta²/kappa_(ij)))`.               (8)

Equivalently, union volume `V` forces

`sum_(i<j)min(delta,delta²/kappa_(ij))
 ≥c M²lambda²delta²/V-CMdelta`.                                (9)

Thus a small extracted carrier union has large inverse-transversality
energy.

### A local Jacobian-stratified form

The infimum in `kappa_(ij)` can be too pessimistic. For `theta>0`, define

`B_theta=sum_(i!=j)
 |{x in U_i intersect U_j:
   |grad P_i wedge grad P_j|<theta}|`.

On the complementary rank-two region, coarea gives at most
`Cdelta²/theta` for each ordered pair. Consequently

`B_theta
 ≥c M²lambda²delta²/V-CMdelta-CM²delta²/theta`.                (10)

Choose `theta=C_0 V/lambda²`, with `C_0` sufficiently large, provided this
is at most the fixed normalization scale. The last term can then be
absorbed, leaving

`B_theta≥c M²lambda²delta²/V-CMdelta`.                          (11)

Since the low-Jacobian mass lies in a set of volume `V`, the essential
supremum of its ordered-pair multiplicity is at least `B_theta/V`. If both
carrier gradients are bounded below there, this is a
near-parallel-normal cluster at angle scale `V/lambda²`. Without that
regularity it is instead a singular/ill-conditioned output. This is a
genuine one-scale inverse theorem, but it does not silently identify those
two alternatives. The lower bounds are informative only when their
right-hand sides are positive, for example
`V≤cMlambda²delta` up to constants.

## 5. Remaining classification problem

The exact pencil

`P_s=q_0+s q_1-1`

has

`grad P_s wedge grad P_t
 =(t-s)grad q_0 wedge grad q_1`.

Many low-Jacobian pairs can therefore be distinct irreducible quadrics in a
coherent pencil, not copies of one carrier. The next missing theorem must
classify the high energy in (9)--(11) into finitely parameterized pencils,
2-plany degeneracies, or another explicit model, while retaining assigned
shading mass and paying only `delta^o(1)`.

Standard polynomial partitioning and the currently cited graininess inputs
do not supply that statement. Assuming it before invoking the stack theorem
would be circular.

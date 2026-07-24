# Parent ancestry removes the transverse catalog baseline

## Verdict

The `Mdelta` baseline is unavoidable for `M` unrelated grains, but it is not
the correct baseline for `M` descendants cut from only a few polynomial
partition walls. If each line sees at most `K` parent wall labels of degree
at most `D`, then all quantitatively transverse descendant incidences have
longitudinal mass only

`O(K D delta/alpha)`,

independent of the number of descendant grains. Any captured incidence above
this threshold is nontransverse or lies near a singular/ill-conditioned
parent region. With a uniform lower gradient bound, the regular remainder is
genuinely tangent to a parent wall.

Combined with an additive-error Hausdorff covering criterion, this identifies
a precise noncircular target: preserve subpolynomial parent ancestry through
the partition tree, then organize the tangent mass into subpolynomially many
fixed continuum carrier charts.

The first step is proved here. The second is still open.

## Transverse sublevel lemma on a line

Let `P` be a real polynomial of degree at most `D`, let
`ell(t)=x+t v`, and put `p=P circ ell`. For `r,alpha>0`,

`E={t in I: |p(t)|≤Cr and |p'(t)|≥alpha}`.

Then

`|E|≤C D r/alpha`.                                            (1)

Indeed, cut `I` at the zeros of `p'` and at the endpoints created by
`p'=alpha` and `p'=-alpha`. There are `O(D)` resulting intervals on which
`p` is monotone and `|p'|≥alpha`. On each, the image lies in an interval of
length `O(r)`, so the inverse function estimate gives length
`O(r/alpha)`.

The same conclusion follows by applying the one-dimensional coarea formula
to each monotonicity interval. Multiple descendant grains inside the same
sublevel set do not multiply the length of their union. They would multiply
a pair-incidence count, which is why the union or unique-assignment
hypothesis below is essential.

## Parent-ancestry theorem

Let a catalog of arbitrarily many descendant grains be grouped under parent
wall sublevels

`W_nu={|P_nu|≤Cr}`,

where `deg P_nu≤D`. Every descendant assigned to `nu` is contained in this
same parent sublevel. For each line and parent, take the **union** of all
descendant incidences, or make a measurable single-valued parent assignment
to every retained line-parameter pair. Do not sum pair-incidence
multiplicity over descendants.

Suppose every selected line encounters at most `K` distinct parent
polynomials over its whole parameter interval. Call a retained incidence
transverse if

`|(P_nu circ ell)'|≥alpha`

at that parameter.

For each line, (1) and a union bound over its parent labels give

`length(transverse assigned incidences)
 ≤C K D r/alpha`.                                             (2)

Integrating over a line family of normalized parameter measure gives

`A_tr≤C K D r/alpha`.                                         (3)

There is no factor equal to the number of descendant grains.

This is exactly where retaining partition ancestry is stronger than an
unstructured semialgebraic catalog. For `M` unrelated parallel slab parents,
one has `K=M`, and (3) recovers the `Mr` crossing baseline. For many grains
cut from one wall, `K=1`.

## Additive-error Hausdorff criterion

Fix a jointly measurable segment family with incidence functional `A(V)`.
Suppose that at every small dyadic scale `r` and for every measurable `V`,
there are at most `J(r)` chart-incidence masses `A_nu(V)` such that

`A(V)≤sum_(nu≤J(r)) A_nu(V)+e(r)`,                             (4)

and each chart satisfies

`|N_(Cr)(V)|≥c A_nu(V)²/L_0(r)`.                              (5)

Here every `A_nu` is the genuine incidence functional of a jointly
measurable fixed or cell-averaged continuum line chart contained in the
swept set. Equation (5) holds uniformly for every measurable set, with the
same ambient neighborhood `N_(Cr)(V)`. The chosen chart may depend on `V`,
but `A_nu` is not an arbitrary numerical mass or a point-sampled,
scale-dependent pseudo-family.

Assume

`sum_(dyadic r≤r_0) e(r) -> 0`,                               (6)

and, for every `s<4`,

`sum_(dyadic r≤r_0)
 r^(4-s)J(r)²L_0(r) -> 0`.                                   (7)

Then the swept set has Hausdorff dimension four.

### Proof

Take an arbitrary cover and its dyadic groups `V_k`, with radii `r_k`.
Their total incidence satisfies `sum_k A(V_k)≥a_0>0`.
By (6), for small enough cover scale the groups satisfying

`A(V_k)>2e(r_k)`

still carry at least `a_0/2`. For each such group, (4) supplies a chart with

`A_nu(V_k)≥A(V_k)/(2J(r_k))`.

If `c_k` is the `s`-cost of the balls in this group, then

`|N_(Cr_k)(V_k)|≤C r_k^(4-s)c_k`.

Using (5),

`A(V_k)
 ≤C J(r_k)L_0(r_k)^(1/2)
      r_k^((4-s)/2)c_k^(1/2)`.

Sum over the retained groups and apply Cauchy--Schwarz. Equations (6)--(7)
force the total cover cost to diverge as the maximal radius tends to zero.

Unlike a relative-retention hypothesis, (4) tolerates cover groups with very
small incidence: their errors are harmless if the dyadic sum is small.

## Consequence of subpolynomial ancestry

Apply (3) to the transverse portion and take

`e(r)=C K(r)D(r)r/alpha(r)`.

If

`K(r)D(r)/alpha(r)=r^(-o(1))`,

then (6) holds. If the remaining nontransverse-or-singular mass can be
regularly stratified and organized into

`J(r)=r^(-o(1))`

fixed or cell-averaged continuum charts with
`L_0(r)=r^(-o(1))`, then (7) also holds and the full Hausdorff conclusion
follows.

For the rank-two-separated parabolic charts,
`L_0(r)=O(log(1/r)²)`. For strongly normal-transverse charts it is only one
logarithm.

## Lusin retention is additive but has no chart bound

For a measurable segment selector on a finite Radon direction space, choose
at scale `r_k` a Lusin compact set `G_k` whose exceptional direction measure
is at most `epsilon_k`. The restricted incidence satisfies, uniformly for
every measurable `V_k`,

`A_(G_k)(V_k)≥A(V_k)-|I|epsilon_k`.                            (8)

Choosing `sum_k epsilon_k<infinity` makes this an additive error of exactly
the type allowed above, and the good sets retain positive aggregate
incidence across any sufficiently fine cover.

This produces the additive retention inequality (4), but not the full chart
hypothesis (4)--(5). Lusin continuity supplies no quantitative modulus,
bounded carrier-chart entropy, reach, transversality, or SSI. The required
chart count has no universal quantitative rate and need not be
subpolynomial. Thus measurable selection solves the additive retention issue
but not the geometric organization issue.

## Exact obstruction and claim boundary

Take a delta-net of directions in a cap `|v_1|≥c`, put all axes through the
origin, and shade only `B(0,c delta)` in each tube. The union has volume
`Theta(delta^4)` and multiplicity `Theta(delta^-3)`. The single hyperplane
wall `x_1=0` captures all shading, but every line is transverse and its wall
overlap is only `Theta(delta)`.

Thus even one parent wall plus extreme multiplicity does not force relative
tangential retention or overlap `lambda≫delta` for every cover group. What
(3) gives is an additive, dyadically summable transverse error.

Standard polynomial partitioning supplies cell/wall ancestry at one step.
This note does not prove that `K(r)=r^(-o(1))` survives a full partition tree,
nor that the remaining nontransverse-or-singular mass admits the chart
organization in (4).
Proving (4) with `J(r)=r^(-o(1))` is exactly the open chart-organization
theorem only when those charts also satisfy (5); assuming that package would
be circular.

# Direction capacity of one quadratic carrier

This is an elementary lambda-explicit conditioned-quadric lemma. It should be
read alongside Katz–Rogers (arXiv:1802.09094) and Zahl
(arXiv:1801.05106), who prove broader polynomial Wolff and
`delta^(-2-epsilon)` fixed-hypersurface results.

## Theorem

Let

`P(x)=q_2(x)+ell(x)+c`

be a coefficient-normalized quadratic polynomial on `R4`, with the symmetric
matrix `A` of `q_2` indefinite and quantitatively nonsingular:
`||A^-1||≤L`. Let `X=Z(P) intersect B(0,2)`. Fix
`delta≤lambda≤1`. All implicit constants may depend on `L` and the fixed
neighborhood constant.

Suppose `T` is a unit delta-tube with core `x+t v`, `|v|=1`, and the core
spends a set of `t`-length at least `lambda` inside `N_(C delta)(X)`. Then

`|q_2(v)|≤C delta lambda^-2`.                                    (1)

Consequently, a direction-delta-separated family of such tubes has

`#T ≤ C min(delta^-3, delta^-2 lambda^-2)`.                       (2)

For `lambda≈1`, one smooth quadratic carrier holds at most
`O(delta^-2)` Kakeya directions. Thus a full `delta^-3` direction family
requires at least order `delta^-1` distinct quadratic carriers. This explains
why the transverse-stack theorem operates at `M≈delta^-1`.

More generally, if `lambda=delta^beta`, the exact capacity exponent is

`min(3,2+2 beta)`,

and the required carrier-count exponent is `max(0,1-2 beta)`. The rational
ledger verifies these conversions without floats.

## Proof

If the core is within `C delta` of `X`, coefficient normalization and the
mean-value theorem give

`|P(x+t v)|≤C delta`

on a measurable set `E subset [0,1]` of length at least `lambda`. The
left-hand side is a degree-two polynomial

`r(t)=q_2(v)t²+b t+d`.

The degree-two Remez inequality on an interval gives

`sup_[0,1]|r|≤C lambda^-2 sup_E|r|≤C delta lambda^-2`.

The leading coefficient of a quadratic is bounded by a constant times its
supremum on `[0,1]` (equivalently, use its second finite difference).
This proves (1).

Because `q_2` is nonsingular, its null cone cuts the unit sphere transversely.
Indeed, if the spherical gradient vanished at a null vector `v`, then
`A v` would be parallel to `v`; taking the inner product with `v` would
force the corresponding eigenvalue to be zero, contradicting
nonsingularity. Compactness therefore turns (1) into

`dist(v,{q_2=0} intersect S3)≤C delta lambda^-2`.

The null directions form a smooth compact two-dimensional surface in `S3`.
A delta-separated set in its `tau`-neighborhood has cardinality

`O(delta^-2 max(1,tau/delta))`.

Taking `tau=C delta lambda^-2` gives (2), capped by the ambient
`O(delta^-3)` packing bound.

If the original hypothesis is stated using four-dimensional tube overlap
`|T intersect N_(C delta)(X)|≥lambda|T|`, Fubini along the tube first gives
the core-incidence hypothesis above, with only a fixed change of constants.

## Sharpness and scope

For exact lines in a split quadric, the direction set is precisely a
two-dimensional null surface, so the `delta^-2` bound is sharp. At smaller
`lambda`, quadratic tangencies show that the `lambda^-2` scale is the natural
degree-two Remez loss.

This theorem excludes a single quadratic carrier as an explanation for a
full direction-separated Kakeya family. It does not exclude the
three-parameter essentially-distinct line net used in the Convex-Wolff
counterexample, because that net has a one-dimensional fiber of parallel
translates over its two-dimensional direction set.

# Exact split-quadric stress test

## Object

`Q={x in R4: x1²+x2²-x3²-x4²=1}`.

Identify `Q` with `SL_2(R)` by

`M(x)=[[x1+x3,x2+x4],[x4-x2,x1-x3]]`.

For `M_0 in SL_2` and a rank-one nilpotent matrix `N=p q^T` with
`q^T p=0`, the affine line

`M(t)=M_0(I+tN)`

lies in `SL_2` for every `t`, because

`det(I+tN)=1+t trace(N)+t² det(N)=1`.

## Verified facts

The harness constructs three rational lines through the point `(1,0,0,0)`.
It verifies at several rational parameters, using exact arithmetic, that all
points satisfy the quadric equation. It also verifies that the three
directions have rank three and nonzero squared wedge.

Therefore:

- the quadric is genuinely ruled by an infinite rational family;
- a ruled model can be pointwise trilinear;
- “ruled” cannot be replaced by “2-plany” in a proposed rigidity lemma.

## Reproduction

```bash
cd problems/kakeya-r4/harness
python3 -m unittest -v test_incidence_models.py
```

## Semialgebraic detection

Within `B(0,2)`, restricting line cores to an interior patch, the thickened
grain

`{|x1²+x2²-x3²-x4²-1|≤C delta}`

has volume comparable to `delta` by the tubular-neighborhood formula. A
family of `N` delta-tubes
around unit segments in `Q` therefore has bounded-complexity semialgebraic
density at least `c N delta²`. A maximal three-parameter ruled family
(`N≈delta^-3`) is detected with density `≈delta^-1`.

The null direction set is only two-dimensional, so a direction-separated
subfamily has `N≈delta^-2`. The extra obstruction parameter is the family of
parallel translates. This is why the example creates an
essentially-distinct-tube union obstruction without itself being a full
Kakeya direction family. The Convex-Wolff version needs the thinning/copying
step below.

The raw full net needs one correction before it is a convex-axiom
counterexample. Zahl (arXiv:2512.09397, Section 4.1) shows that a tangent
`delta×delta×delta^(1/2)×1` prism contains about `delta^-1` raw quadric
tubes, while Convex Wolff permits only `delta^-1/2`. Randomly retain a
`delta^(1/2)` fraction: the resulting `delta^(-5/2)`-tube family satisfies
Convex Wolff. Taking `delta^(-1/2)` suitable translated/rotated copies
produces `delta^-3` Convex-Wolff tubes with union volume about
`delta^(1/2)`. This copied construction is the exact counterexample to a
literal R⁴ convex-union theorem. Every thinned copy is still detected by
the degree-2 semialgebraic test by a factor `delta^(-1/2)`.

## Limit

The test does not establish Proposition 3.12 extremality, balanced shading,
or two-scale persistence for this model. Those are the correct next checks;
declaring the quadric incompatible with stickiness would be unsupported.

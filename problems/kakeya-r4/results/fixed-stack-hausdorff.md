# Fixed transverse stacks have Hausdorff dimension four

## Weighted covering theorem

Let `K subset R4` be compact. Suppose there is a fixed finite measure space
`(Theta,mu)`, an interval `I`, and a measurable line family

`F:Theta×I -> K`,

`F(theta,t)=a(theta)+t v(theta)`,

with `mu(Theta)>0`. For measurable `V subset R4`, define its line-incidence
mass

`A(V)=integral_Theta
 |{t in I:F(theta,t) in V}| dmu(theta)`.

Assume that for every sufficiently small dyadic `r` and every measurable
`V`,

`|N_(Cr)(V)|≥c A(V)²/L(r)`.                                    (SSI)

If, for every `s<4`,

`Phi_s(r_0)=sum_(dyadic r≤r_0) r^(4-s)L(r) -> 0`

as `r_0->0`, then

`H^s(K)=infinity` for every `s<4`,

and hence

`dim_H K=4`.

Joint measurability of `(theta,t) -> F(theta,t)` is part of the hypothesis.

## Proof

Take an arbitrary ball cover `{B_alpha}` of `K` with radii at most `r_0`.
Group it dyadically:

`V_k=union_{2^(-k-1)<r_alpha≤2^-k} B_alpha`,

`r_k=2^-k`.

Put `a_k=A(V_k)`. Since the balls cover every full segment,

`sum_k a_k≥mu(Theta)|I|=:a_0>0`.                               (1)

Let

`c_k=sum_(alpha in k) r_alpha^s`.

The balls in group `k` have radii comparable to `r_k`, so

`|N_(Cr_k)(V_k)|≤C r_k^(4-s)c_k`.

Using (SSI),

`a_k≤C c_k^(1/2) r_k^((4-s)/2)L(r_k)^(1/2)`.

Cauchy--Schwarz and (1) give

`a_0²≤C (sum_k c_k)
 (sum_(r_k≤r_0) r_k^(4-s)L(r_k))`.

Every such cover therefore satisfies

`sum_alpha r_alpha^s≥c/Phi_s(r_0)`.

The right side tends to infinity, proving the claim.

## Continuum transverse stacks supply (SSI)

Assume now that `Theta=S×Omega`, with a fixed continuum family

`F_s(y,t)=a_s(y)+t v_s(y)`

such that:

- `S` is a fixed bounded compact interval and `(s,y,t) -> F_s(y,t)` is jointly
  measurable;
- each `F_s` is a uniformly bi-Lipschitz ruled sweep of a fixed compact patch
  `X_s subset B(0,C)`, with uniform reach and complexity;
- `F_s(Omega×I) subset K`;
- `X_s subset Z(P_s)` for coefficient-normalized polynomials `P_s` of
  degree at most two;
- the relevant patch neighborhoods obey

  `|grad P_s wedge grad P_(s')|≥c|s-s'|`

  throughout their common `Cr`-neighborhood, not merely on the exact zero
  sets;

- `ds dy` is comparable to the fixed line-parameter measure.

Also assume the uniform coarea fiber bound used in the stack theorem: on
the rank-two locus, the two-dimensional areas of the relevant common level
sets in a fixed ambient ball are uniformly bounded. This follows, for
example, from coefficient-normalized bounded-degree carrier polynomials,
quantitative regularity, and the Crofton--Bézout argument.

For a measurable `V`, put

`A_s={(y,t):F_s(y,t) in V}`,

`U_s=N_(cr)(F_s(A_s))`.

The reach-based normal map gives

`|U_s|≥c r |A_s|`.                                             (2)

Coarea and the trivial same-carrier bound give

`|U_s intersect U_(s')|
 ≤C min(r,r²/|s-s'|)`.                                        (3)

Define

`f(x)=r^-1 integral_S 1_(U_s)(x) ds`.

Equations (2)--(3) imply

`integral f≥c A(V)`,

`integral f²≤C(1+log(1/r))`.

The support of `f` lies in `N_(Cr)(V)`. Cauchy--Schwarz therefore proves

`|N_(Cr)(V)|
 ≥c A(V)²/(1+log(1/r))`.                                      (4)

Thus (SSI) holds with `L(r)=1+log(1/r)`, and

`Phi_s(r_0)
 ≤C_s r_0^(4-s)(1+log(1/r_0)) -> 0`.

The fixed continuum stack has Hausdorff dimension four.

## Discrete interpretation and the exact missing condition

The weighted sparse estimate in
`transverse-quadric-stack-union.md` gives the same result if its masses are
defined by averaging over the `r`-cells of the fixed continuum parameter
space. For a cover group `V_k`, those cell-averaged masses satisfy

`r_k sum_i m_(i,k)(V_k)≥c A(V_k)`.

An arbitrary measurable `V_k` may avoid every point in a fixed
point-sampled net, so point sampling alone does not imply this inequality.
One must use cell averages or assume the inequality below explicitly.

The essential cross-scale condition is therefore

`sum_k r_k sum_i m_(i,k)(V_k)≥c`.                              (IC)

A fixed continuum line family makes (IC) automatic by Fubini. Nested
discretizations suffice only when they are proved to retain the displayed
uniform cell-averaged quadrature inequality, possibly after a `Cr`
enlargement or averaging over grid shifts.

Unrelated carrier families chosen independently at each scale do not imply
(IC). This is why the earlier scale-wise Minkowski conclusion could not be
called Hausdorff dimension four.

If a refinement retains only `b(r)` of the fixed incidence mass, then the
effective loss is

`L(r)≈(1+log(1/r))/b(r)²`.

Subpolynomial retention preserves dimension four; a fixed loss
`b(r)=r^epsilon` loses `2epsilon` in the Hausdorff exponent. Estimates only
on a superlacunary scale sequence do not control arbitrary covers.

## Consequence for the explicit quadratic pencil

The fixed pencil and sweeps in
`transverse-quadric-stack-union.md` satisfy the continuum hypotheses after
compact restriction. Hence their compact swept union has Hausdorff dimension
four. Finitely many rotated charts may be joined to obtain a Kakeya set with
segments in every direction.

For this particular smooth pencil there is an easier, stronger observation:
the displayed `(s,p,q,t)` sweep has rank four at the checked seed, so the
inverse function theorem gives nonempty interior and positive
four-dimensional measure after local restriction. It is therefore a
nonvacuity example for the abstract theorem, not a subtle measure-zero
Kakeya construction.

The abstract fixed-family theorem remains useful for less regular continuum
stacks where (SSI) holds but no smooth rank-four parameter map is available.
It does not imply the general conjecture, because an arbitrary Kakeya set has
no known fixed all-scale carrier parameterization satisfying (SSI) or (IC).

The proof gives `H^s(K)=infinity` for every `s<4`, but not positive
four-dimensional measure: the endpoint scale sum with `s=4` diverges.

## Exact full-conjecture extraction target

Fix a jointly measurable segment selector for a Kakeya set and its incidence
functional `A(V)`. Suppose that for every sufficiently small dyadic `r` and
every measurable `V`, an extraction theorem retains at least a fraction
`b(r)` of `A(V)` inside one continuum carrier chart satisfying the transverse
stack hypotheses at scale `r`. Applying (4) to the retained chart gives

`|N_(Cr)(V)|
 >= c b(r)^2 A(V)^2/(1+log(1/r))`.                            (5)

Thus the weighted covering theorem applies with

`L(r)=(1+log(1/r))/b(r)^2`.

In particular, `b(r)=r^(o(1))` is sufficient for Hausdorff dimension four.
Equivalently, if the incidences are divided among `J(r)` admissible charts,
choosing the largest chart costs `b(r)>=1/J(r)`, so
`J(r)=r^(-o(1))` is sufficient.

This criterion is deliberately cover-by-cover. Extracting a good chart from
the entire tube union at each scale does not prove (5), because a cover group
`V` may carry its incidence mass on a different portion of the line family.
The missing full-conjecture theorem is therefore a uniform, shaded
extraction statement with subpolynomial chart entropy. The criterion does
not assume or rename that theorem.

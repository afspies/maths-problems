# Rank-two-separated parabolic stacks

## Verdict

Indefinite rank-three parabolic carriers are not a single unresolved block.
A one-parameter coefficient family whose pairwise differences have two
singular values of order the parameter separation obeys a shaded union
theorem with only a squared logarithmic loss. A fixed continuum version has
Hausdorff dimension four.

This strictly extends the pointwise-normal transverse-stack theorem: the
carrier normals here may agree on a one-dimensional locus. The remaining
parabolic obstruction is the rank-one-tangent coefficient branch, which
contains the canonical pencil

`z-y_1y_2-sy_3²=0`.

The theorem assumes an organized coefficient path; it does not extract that
path from a general Kakeya family.

## Quadratic sublevel lemma

Let `D` be a real symmetric `3×3` matrix with `||D||≤C_0`, and let
`sigma_2(D)` denote its second largest singular value. If
`sigma_2(D)≥kappa>0`, then for `0<eta≤1`,

`|{y in B(0,C): |y^T D y|≤eta}|
 ≤ C min(1,(eta/kappa)(1+log(1/eta))).`                       (1)

The constant depends only on `C_0` and the ambient ball.

### Proof

Diagonalize `D` orthogonally. Choose two diagonal coefficients with absolute
value at least `kappa` and hold the third coordinate fixed. After scaling the
chosen coordinates, their two-variable quadratic is either elliptic or
hyperbolic, plus a constant depending on the fixed coordinate.

For the elliptic sign, every thickness-`eta` annulus has scaled area
`O(eta)`. For the hyperbolic sign, use

`u²-v²=(u-v)(u+v)`.

Splitting into dyadic regions according to the larger factor gives scaled
area `O(eta(1+log(1/eta)))`, uniformly in the added constant. The coordinate
Jacobian is at most `kappa^-1`. Integrating the third coordinate proves (1).
If the displayed bound exceeds the ball volume, use the trivial estimate.

The logarithm is sharp for a rank-two split form at level zero. No
pointwise lower bound for `|grad P_i wedge grad P_j|` is used.

## Discrete shaded union theorem

Let `A_s` be symmetric `3×3` matrices on a compact interval `S`, with
`||A_s||≤C_0`, and put

`P_s(y,z)=z-y^T A_s y-ell(y)`,

where the affine-linear term `ell` is common to the family. Suppose

`sigma_2(A_s-A_t)≥c_0|s-t|`                                   (2)

for all `s,t in S`.

Choose quasi-uniform parameters `s_1,...,s_M` with

`|s_i-s_j|≥c|i-j|/M`,

and assume `Mdelta≤C`. Let `X_i` be fixed bounded graph patches in
`Z(P_(s_i))`. Suppose measurable shaded carrier unions satisfy

`U_i subset N_(Cdelta)(X_i)`,

`|U_i|≥c lambda delta`.

Then

`|union_(i=1)^M U_i|
 ≥ c lambda² Mdelta/
   (1+Mdelta(1+log(1/delta))H_(M-1)).`                         (3)

In particular, when `M≈delta^-1`,

`|union_i U_i|≥c lambda²/(1+log(1/delta))²`.                   (4)

All graph, collar, and coefficient constants are uniform.

### Proof

Bounded graph gradients convert a `Cdelta`-neighborhood into a
`Cdelta`-sublevel set. A point in the overlap satisfies

`|y^T(A_(s_i)-A_(s_j))y|≤Cdelta`.

For each allowed `y`, its `z`-fiber has length `O(delta)`. Apply (1) with
`kappa≥c|i-j|/M`:

`|U_i intersect U_j|
 ≤Cdelta min(
      1,
      delta M(1+log(1/delta))/|i-j|
    ).`                                                       (5)

Dropping the minimum only weakens the upper bound. Thus

`sum_(i<j)|U_i intersect U_j|
 ≤C M²delta²(1+log(1/delta))H_(M-1)`.                         (6)

The diagonal contribution is `O(Mdelta)`, while

`sum_i |U_i|≥c Mlambda delta`.

Cauchy--Schwarz applied to `sum_i 1_(U_i)` gives (3), and (4) follows from
`H_M≤1+log M`.

## Continuum and Hausdorff version

Let `F_s(theta,t)` be a fixed jointly measurable family of ruled sweeps of
the graph patches above, with uniform local bi-Lipschitz and collar bounds.
For measurable `V`, write

`A(V)=integral_S integral
 |{t:F_s(theta,t) in V}| dtheta ds`.

Write `A_s(V)` for the inner `theta,t` incidence integral at fixed `s`.
Thicken the selected sweep points by radius `r` and call the resulting set
`U_s(V)`. The normal-coordinate bound gives

`|U_s(V)|≥cr A_s(V)`.

Equation (1) gives the continuum pair kernel

`|U_s(V) intersect U_t(V)|
 ≤Cr min(
      1,
      r(1+log(1/r))/|s-t|
    ).`                                                       (7)

For

`f=r^-1 integral_S 1_(U_s(V)) ds`,

integration of (7) yields

`integral f²≤C(1+log(1/r))²`,

whereas `integral f≥cA(V)`. Since `f` is supported in `N_(Cr)(V)`,

`|N_(Cr)(V)|
 ≥c A(V)²/(1+log(1/r))²`.                                    (8)

The fixed-stack covering theorem applies because, for every `s<4`,

`sum_(dyadic r≤r_0)
 r^(4-s)(1+log(1/r))² -> 0`.

Hence the compact swept union has Hausdorff dimension four. The endpoint
still does not imply positive four-dimensional measure.

## Exact nonvacuous coefficient path

For `0≤s≤1`, take

`A_s=diag((1+s)²,-1,(1+s)²)`.                                 (9)

Every `A_s` has signature `(2,1)`, and

`A_s-A_t
 =((1+s)²-(1+t)²)diag(1,0,1)`.

Thus its two nonzero singular values are both at least `2|s-t|`.

Put

`u_s(q)=(1-q²,(1+s)(1+q²),2q)`.

Then `u_s(q)^T A_s u_s(q)=0`. With base point `y_0=(r,0,0)`,

`F_s(q,r,t)
 =(y_0+t u_s(q),(y_0+t u_s(q))^T A_s(y_0+t u_s(q)))`          (10)

is an exact line on `Z(P_s)`. Its four-dimensional direction is

`v_s(q,r)
 =(u_s(q),2r(1+s)²(1-q²))`.

At `(s,q,r)=(0,0,0)`, the direction together with its three parameter
derivatives has determinant `4`. At `(s,q,r,t)=(0,0,0,1)`, the four sweep
derivatives also have determinant of absolute value `4`. Compact restriction
therefore supplies uniform ruled and direction charts.

The exact rational harness verifies (9)--(10), rank-two coefficient
separation, and both determinants. The local rank-four sweep also implies
positive measure for this smooth example; as before, the analytic value of
the continuum theorem is its stability for arbitrary measurable shadings,
not construction of a delicate measure-zero example.

## Quantitative coefficient-path dichotomy

Let `A:S->Sym_3` be `C²` with `||A''||≤K`. On a parameter interval where

`sigma_2(A'(s))≥eta`,

Weyl's singular-value inequality and

`(A(t)-A(s))/(t-s)=A'(s)+O(K|t-s|)`

give (2), with constant `eta/2`, whenever
`|t-s|≤c eta/K`. Using the buffered good region
`sigma_2(A')≥2eta`, intervals of length `c eta/K` therefore satisfy

`sigma_2(A_t-A_s)≥eta|t-s|`

when both parameters lie in the buffered good set and in one such interval.
Thus `O(1+K|S|/eta)` intersections of the good set with coefficient
intervals handle the buffered rank-two-tangent portion.

The separation constant in each chart is now `c_0≈eta`, so the analytic
constants in (1), (5), and (8) also depend on `eta`. If `eta=eta(r)` shrinks
with scale, both this loss and the chart count must be charged in
`L_0(r)J(r)²`; charging only the count is insufficient. No scale-dependent
full-dimension conclusion is claimed from this qualitative path
decomposition.

The complementary output is

`sigma_2(A'(s))<2eta`:                                       (11)

the path is tangent, to accuracy `eta`, to the cone of symmetric matrices of
rank at most one. For an exact rank-one tangent,

`A'(s)=a(s)u(s)u(s)^T`.

If `u(s)` is constant this is the canonical rank-one pencil and feeds the
transverse-versus-2-plany slab analysis. If `u(s)` rotates, nearby coefficient
differences generally acquire a second singular value only at higher order;
the squared-log theorem does not apply at the original carrier spacing.

Consequently the live parabolic classification problem is no longer all
indefinite rank-three quadrics. It is the rank-one-tangent path (11), with
the rotation and scale of `u(s)` charged explicitly.

## Exact rigidity of a complete rank-one-dangerous clique

There is an exact classification at the opposite endpoint.

Let `f_0,...,f_m` be real quadratic polynomials on `R^d`, `d≥2`. Suppose
that for every pair `i,j`, the difference `f_i-f_j` is either constant or
has all three properties:

1. its Hessian has rank one;
2. its affine gradient vanishes somewhere;
3. its value on the critical affine hyperplane is zero.

Equivalently, every nonconstant pair difference is

`f_i-f_j=c_(ij) ell_(ij)²`                                    (12)

for a nonzero scalar and a nonconstant affine functional. Then either all
`f_i` differ only by constants, or there are `f_*`, one affine functional
`ell`, and scalars `a_i` such that

`f_i=f_*+a_i ell²`                                             (13)

for every `i`.

### Proof

Choose a nonconstant difference and relabel so that
`f_1-f_0=c_1 ell_1²`. For every `i`, either `f_i-f_0` is constant or it is
`c_i ell_i²`. A nonzero constant is impossible, since subtracting it from
`c_1 ell_1²` gives a rank-one quadratic whose critical value is nonzero.

The linear parts of `ell_i` and `ell_1` must be collinear. Otherwise the
Hessian of

`c_i ell_i²-c_1 ell_1²`

has rank two on their span. Hence all differences depend on one affine
coordinate `t`, and may be represented by univariate coefficient vectors
`v_i=(A_i,B_i,C_i)`.

A univariate quadratic is an affine square exactly when

`Q(A,B,C)=B²-4AC=0`.

Both `Q(v_i)=0` and `Q(v_i-v_j)=0`. Polarization makes every `v_i`
orthogonal to `v_1` for the Lorentzian discriminant form. In a
three-dimensional Lorentz space, a null vector orthogonal to a fixed
nonzero null vector is proportional to it. Thus all `v_i` are proportional,
which is (13).

This theorem requires a complete clique and exact zero critical values.
Connectedness is insufficient: `0`, `x²`, and `x²+y²` have square
differences on two edges but no common-square pencil. Approximate critical
values, dense dangerous graphs, and rotating rank-one tangents require a
quantitative stability and graph-organization theorem that is not proved
here.

## Rotating rank-one tangent stress model

The rotating case is genuinely different from a fixed pencil. Let

`u(s)=(1,s,0)`

and

`A(s)=integral_0^s u(t)u(t)^T dt
 =[[s,s²/2,0],[s²/2,s³/3,0],[0,0,0]].`                       (14)

Every derivative `A'(s)=u(s)u(s)^T` has rank one. Nevertheless
`A(h)-A(0)` has rank two for `h!=0`, with exact nonzero principal
determinant

`h^4/12`.                                                     (15)

Its large singular value is of order `h`, so the second is only of order
`h³`. Thus it fails the linear separation (2) by two powers even though the
rank-one direction rotates. Sampling at the original `delta` carrier
spacing would insert a power loss into the sublevel bound.

The exact harness verifies rank two and (15). A viable next rigidity theorem
must exploit rotation of the bad hyperplane across separated scales, rather
than treating (14) as either a fixed common-square pencil or a linearly
rank-two-separated path.

# Endpoint multiplicity for affine-rotating rank-one stacks

## Verdict

The canonical rotating rank-one coefficient path is not merely an
`11/3` pair-overlap example.  Its full collar multiplicity has an endpoint
`L^(3/2)` bound with one logarithm.  Consequently arbitrary jointly
measurable shadings of any fixed affine-rotating parabolic stack satisfy

`|N_(Cr)(V)| >= c A(V)^3/log(2/r)^2`,                         (1)

and the fixed swept set has Hausdorff dimension four.

This is a genuinely new infinite structured subclass.  It closes the
affine-rotating rank-one obstruction left by the pairwise rank-two theorem.
It does **not** extract such a fixed stack from a general Kakeya set, so the
full conjecture remains open.

## The exact moment path

Let `p,q in R3` be linearly independent and

`A_s=A_0+integral_0^s (p+tq)(p+tq)^T dt`, `0<=s<=1`.          (2)

Assume the graph patches

`X_s subset {z=y^T A_s y+ell(y)}`

stay in a fixed bounded box, have uniform graph collars, and are swept by a
fixed jointly measurable two-parameter line family.  More precisely, its
three-parameter point sweep `(theta,t) -> F_s(theta,t)` is uniformly
bi-Lipschitz onto `X_s` on finitely many patches, its parameter measure is
uniformly comparable to three-dimensional surface measure, and the selected
sets have a uniform one-dimensional normal-coordinate thickening.  These
are the same reach and sweep hypotheses used in the fixed-stack theorem.
The affine term `ell` is common to the stack.  Uniform affine changes and a
scalar density `a(s)` bounded above and below can be included only when a
bi-Lipschitz reparameterization also leaves the rotating vector affine in
the new parameter.  A generic bounded density need not have this property,
and no such general extension is claimed.

Let the fixed line-parameter space be a standard Borel finite positive
measure space `(Omega,mu)`, let `I` be an interval of positive length, and
write the Borel sweep as `F_s(theta,t)`.  For a Borel set `V`, define

`A_s(V)=integral_Omega
 |{t in I:F_s(theta,t) in V}| dmu(theta)`

and put

`A(V)=integral_0^1 A_s(V) ds`.

Thicken the selected sweep points by radius `r` to obtain `U_s(V)`.  Uniform
normal coordinates give

`|U_s(V)|>=c r A_s(V)`,                                      (3)

and

`U_s(V) subset N_(Cr)(X_s) intersect N_(Cr)(V)`.

Assume, as part of the fixed sweep/collar hypotheses, that
`(s,x) -> 1_(U_s(V))(x)` is jointly measurable for every Borel `V`.
Open dyadic cover groups are Borel, so this is the scope needed for the
Hausdorff argument.

## Cubic collar-multiplicity lemma

For `a,b in [-C,C]`, put

`h_(a,b)(s)=integral_0^s (a+tb)^2 dt
           =a^2s+ab s^2+b^2s^3/3`

and

`m_r(a,b,z)=r^-1 |{s in [0,1]: |z-h_(a,b)(s)|<=Cr}|`.

Then

`integral m_r(a,b,z)^(3/2) da db dz
 <= C log(2/r)`,                                             (4)

where the integral is over a fixed bounded `a,b,z` box.

### Proof

The function `h_(a,b)` is monotone and

`h'_(a,b)(s)=(a+bs)^2`.                                      (5)

Split the `(a,b)` plane into two regions.

First suppose `|a|<=C_1|b|`, so the critical point
`s_0=-a/b` lies in a fixed enlargement of the parameter interval.  On that
enlargement the exact identity

`h_(a,b)(s)-h_(a,b)(s_0)=b^2(s-s_0)^3/3`                     (6)

holds.  The pushforward of `ds` therefore has density bounded by

`C |b|^(-2/3)|z-z_0|^(-2/3)`

on each side of `z_0=h(s_0)`.  Averaging this density over a `Cr` interval
gives

`m_r(a,b,z)
 <=C |b|^(-2/3)(|z-z_0|+r)^(-2/3)`.

Hence

`integral m_r(a,b,z)^(3/2) dz
 <=C |b|^-1 log(2+b^2/r)`.                                  (7)

This uses the support bound
`|z-z_0|<=C(b^2+r)`, which remains valid when `s_0` lies outside `[0,1]`
because the argument enlarged the parameter interval by a fixed amount.

For fixed `b`, the present region has `a`-width `O(|b|)`.
Integrating (7) in `a,b` gives `O(log(2/r))`.  When
`b^2<=r`, the direct bound

`m_r<=r^-1`, `|supp_z m_r|<=C(r+a^2+b^2)`

removes the apparent singularity at `b=0`: the `(a,b)` area is `O(r)`,
the `z`-integral is `O(r^-1/2)`, and the total is `O(r^(1/2))`.

The point `a=b=0` is covered by this direct bound (and has zero `(a,b)`
measure), so the division defining `s_0` causes no omission.

Now suppose `|a|>C_1|b|`, taking `C_1` larger than the parameter interval.
Then `|a+bs|` is comparable to `|a|`.  If `a^2>=r`, the pushforward density
and its `r`-average are `O(a^-2)` on an interval of length `O(a^2)`, so

`integral m_r(a,b,z)^(3/2) dz<=C/|a|`.

For fixed `a`, this region has `b`-width `O(|a|)`, and its integral is
bounded.  If `a^2<r`, the same direct support bound as above gives a bounded
total contribution.  This proves (4).

The proof also shows why rotation matters.  At a cubic stationary point the
one-dimensional pushforward density is only weak `L^(3/2)`, but the
`a`-width of the critical wedge is `O(|b|)` and exactly cancels the
coefficient `|b|^-1` in (7).  With `q=0`, the bad hyperplane is fixed and
this cancellation is unavailable.

## Endpoint shaded incidence inequality

Define

`f(x)=r^-1 integral_0^1 1_(U_s(V))(x) ds`.

By (3),

`integral f>=c A(V)`.                                       (8)

The support of `f` lies in `N_(Cr)(V)`.  Since `U_s(V)` lies in the full
graph collar and the graph gradients are uniformly bounded,

`1_(N_(Cr)(X_s))(y,z)
 <=1_(|z-y^T A_0y-ell(y)-h_(p dot y,q dot y)(s)|<=C'r)`.     (9a)

Thus `f` is pointwise dominated, up to constants, by its full collar
multiplicity.  Complete `p,q` to a basis of `R3` and use

`a=p dot y`, `b=q dot y`

as two linear coordinates.  The remaining coordinate is passive.  The
common `A_0` and `ell` only translate the `z` variable at fixed `y`.
Equation (4) therefore gives

`integral f^(3/2)<=C log(2/r)`.                              (9)

Holder on the support of `f` now yields

`A(V)
 <=C |N_(Cr)(V)|^(1/3) log(2/r)^(2/3)`,

which is (1).

The estimate holds for every Borel `V`; no point sampling and no regularity
of the shading beyond the displayed joint measurability are used.

## Cubic Hausdorff covering theorem

More generally, let `(Theta,mu)` be a standard Borel finite measure space with
`0<mu(Theta)<infinity`, let `I` be an interval of positive length, and let

`F:Theta times I -> K`, `F(theta,t)=a(theta)+t v(theta)`

be a fixed Borel segment family in a compact set
`K subset R4`.  Define

`A(V)=integral_Theta
 |{t in I:F(theta,t) in V}| dmu(theta)`.

Suppose it satisfies

`|N_(Cr)(V)|>=c A(V)^3/L(r)`                                 (10)

for all Borel `V` and all small dyadic `r`.  If, for every `s<4`,

`sum_(dyadic r<=r_0)
 r^((4-s)/2)L(r)^(1/2) ->0`,                                 (11)

then `dim_H K=4`.

Indeed, for a dyadic cover group `V_k` of radius `r_k` and `s`-cost `c_k`,

`|N_(Cr_k)(V_k)|<=C r_k^(4-s)c_k`.

Writing `a_k=A(V_k)`, (10) gives

`a_k<=C L(r_k)^(1/3)r_k^((4-s)/3)c_k^(1/3)`.

Sum over `k` and apply Holder with exponents `3` and `3/2`:

`sum a_k
 <=C (sum c_k)^(1/3)
      (sum r_k^((4-s)/2)L(r_k)^(1/2))^(2/3)`.

Every cover has
`sum a_k>=a_0=mu(Theta)|I|>0`, so (11) forces its `s`-cost to diverge.
For (1), `L(r)=C log(2/r)^2`, and (11) holds for every `s<4`.

## Pairwise estimate and why it misses the endpoint

For the seed path `p=e_1,q=e_2`,

`A_h-A_0=[[h,h^2/2,0],[h^2/2,h^3/3,0],[0,0,0]]`.

The two active eigenvalue scales are `h` and `h^3`.  A direct ellipsoidal
sublevel calculation gives an integrated pair kernel of order `r^(2/3)`;
the resulting second-moment loss is `r^(-1/3)` and proves only dimension
`11/3`.

The endpoint argument retains the order structure
`d(y^T A_s y)/ds=((p+sq) dot y)^2` and uses the critical
`L^(3/2)` multiplicity rather than squaring it.  This is the source of the
full-dimension conclusion.

## Claim boundary

The theorem covers a fixed continuum affine-rotating rank-one stack with
uniform line sweeps and collars.  It is stable under one fixed,
`s`-independent bounded ambient affine change and compact restriction.

It does not prove that a general Kakeya family admits such a stack, that a
scale-dependent extracted catalog is fixed across Hausdorff cover groups,
or that an arbitrary approximate rank-one coefficient graph has an affine
rotating parameterization.  Those remain extraction and organization
problems in Bridge B.

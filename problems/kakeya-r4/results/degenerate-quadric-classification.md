# Degenerate quadratic carriers in R4

## Normal form

Let `P` be nonconstant and write

`P(x)=x^T A x+b dot x+c`, `A=A^T`, `r=rank A`.

Orthogonally split `im A` and `ker A`, then translate in `im A` to remove
the corresponding linear term. After a rotation in `ker A`, exactly one of
the following remains:

- **central:** `P=q_r(y)+c`;
- **parabolic:** `P=q_r(y)+z`.

Here `q_r` is nondegenerate in `r` variables. This normalization is
qualitative; uniform quantitative use requires lower bounds for the retained
eigenvalues and the parabolic linear coefficient.

For a complete line `x+t v` to lie in `Z(P)`, its restriction polynomial
must vanish identically:

`P(x)=0`, `D_vP(x)=0`, `q_r(u)=0`,                            (L)

where `u` is the component of `v` in `im A`.

## Irreducible genuinely quadratic rank at most two is 2-plany

Every regular irreducible nonlinear carrier with `1≤rank A≤2` has its
complete line directions at each point contained in at most two
two-dimensional vector planes. Affine-linear carriers and reducible
quadratic hyperplanes are separate outputs:
an affine hyperplane has a three-dimensional tangent direction space and is
not 2-plany.

The only nontrivial split parabolic normal form is

`P=y_1 y_2+z`

with a free coordinate `w`. Equation (L) gives `u_1u_2=0`. The derivative
condition then places every direction in

`E_1(x)=span(e_1-y_2 e_z,e_w)`,

or

`E_2(x)=span(e_2-y_1 e_z,e_w)`.

The other cases are simpler:

- `y_1y_2=0` is a union of two hyperplanes;
- a nonzero central rank-two level is foliated only in its
  two-dimensional kernel directions;
- a rank-one central quadric is empty, lower-dimensional, or a union of
  parallel affine hyperplanes and belongs to the reducible output;
- `y²+z=0` times `R²` is foliated by the free `R²` planes.
- the definite rank-two parabolic
  `y_1²+y_2²+z` with one free coordinate has exact lines only in that free
  direction.

For a uniformly conditioned regular patch, degree-two Remez applied to a
tube spending a `lambda` fraction near the carrier gives

`|q_r(u)|≤Cdelta lambda^-2`,

`|D_vP(x)|≤Cdelta lambda^-2`.

Indeed, Remez bounds the restriction polynomial uniformly on the unit
parameter interval by `Cdelta lambda^-2`, and Markov's degree-two inequality
gives the same bound for its derivative. Nearest-point projection of a good
axis point to the uniformly regular carrier patch supplies an associated
`x in Z(P)`. Transport the resulting planes to the cell center using the
lower gradient and patch Lipschitz bounds, and pigeonhole between the
at-most-two choices.

For the split rank-two parabolic form `y_1y_2+z`, factoring its null equation
gives `|u_1u_2|≤C rho²` and a derivative-equation error `O(rho²)` for
`rho=sqrt(delta)/lambda`. When `rho≤1`, these yield the local quantitative
conclusion

`dist(v,E_1(x) union E_2(x))
 ≤C sqrt(delta)/lambda`.                                      (1)

The square-root scale is genuine. The other irreducible rank-one/rank-two
normal forms have only the free kernel planes and obey the same or a stronger
local conclusion after the same regular localization. Thus the nonlinear
irreducible branch feeds a local weakly 2-plany alternative at scale
`rho≈sqrt(delta)/lambda` when `lambda≳sqrt(delta)`. Below that overlap
threshold the assertion is vacuous.

## Rank-three central carriers

For

`P=q_3(y)+c`, `w in R`,

equation (L) restricts `u` to the binary quadratic

`q_3(u)=0` inside `B_q(y,u)=0`.

It has at most two projective roots. Adding the free `w` direction gives at
most two two-dimensional direction planes at every regular point.

For the cone `q_3(y)=0`, this remains true away from the singular spine

`{y=0}×R_w`.

A line with transverse slope `|u_y|≥eta` spends at most `C rho/eta` of its
length near the `rho`-neighborhood of the spine. Positive-density shading
therefore either exits into the 2-plany regular region or has direction
close to the spine. A clean extraction theorem must nevertheless retain the
singular-spine bush as an explicit output.

## The genuine degenerate exception

Modulo the degree-one/reducible-hyperplane output, the only smooth
irreducible genuinely quadratic degenerate class that is ruled and not
finite-2-plany is the indefinite rank-three paraboloid

`P=z-q_(2,1)(y)`.

Through each point its projectivized line directions form a nondegenerate
real conic in the tangent projective plane. Such a conic is not contained in
finitely many projective lines. The definite rank-three paraboloid contains
no complete real lines.

## Exact rank-three parabolic pencil

Consider

`P_s(y,z)=z-y_1y_2-sy_3²`, `1≤s≤2`.                            (2)

A line direction `v=(u_1,u_2,u_3,w)` through `x` lies in `P_s=0` exactly
when

`u_1u_2+s u_3²=0`,

`w=x_2u_1+x_1u_2+2s x_3u_3`.                                  (3)

At the origin, the three directions

`e_1`, `e_2`, `(1,-s,1,0)`

are concurrent exact lines and are linearly independent. Thus this
degenerate carrier can be pointwise trilinear.

Its normals satisfy

`grad P_s=(-x_2,-x_1,-2s x_3,1)`,

and the exact identity

`|grad P_s wedge grad P_t|
 =2|s-t||x_3||grad P_s wedge e_3|`.                            (4)

Restrict the transverse patches to `|x_3|≥2rho`. Since
`rho≥sqrt(delta)≫delta` in the nonvacuous regime, their `Cdelta`
neighborhoods remain in `|x_3|≳rho`. Equation (4) then gives harmonic
transversality with constant `c_0≈rho`, not a scale-free constant.
Consequently the
pair-overlap estimate becomes

`|U_s intersect U_t|≤Cdelta²/(rho|s-t|)`,

For a quasi-uniform ordered sampling of `[1,2]` satisfying
`|s_i-s_j|≥c|i-j|/M`, and with `Mdelta≈1`, the corresponding second moment
gives only

`|union_i U_i|≥c lambda_out² rho/log(2+M)`.                    (5)

Here `lambda_out` is the retained shading fraction on those transverse
patches. Thus a power-scale `rho` is a genuine power loss. If a line spends
length `lambda` in the slab, then

`|u_3|≤C rho/lambda`.

Equations (3) then put one of `u_1,u_2` within `C rho/lambda` of zero and
place the direction within that distance of one of the two ruling lines

`span(e_1+x_2e_z)`, `span(e_2+x_1e_z)`,

and hence, a fortiori, within a two-plane alternative.
Therefore this entire pencil has an exact transverse-versus-2-plany
stratification with an explicit tradeoff:

- mass away from the degeneration slab enters the transverse-stack branch
  with transversality constant `rho`;
- mass persisting in the slab enters the weakly 2-plany branch.

This is a rigorous degree-two stress model for the desired two-scale ruled
rigidity, not the scale-loss-free lemma itself. Optimizing the `rho^-1`
transverse loss against the `rho/lambda` plany aperture is still required
before claiming an exponent gain. Pigeonholing `rho` over dyadic scales costs
`O(log(delta^-1))` unless it is fixed in advance, and no cross-scale
persistence theorem is proved.

The exact harness verifies representative rational instances of (2), three
concurrent exact lines and their rank, and the normal-wedge identity (4). It
does not verify a dense two-parameter sweep, uniform reach, a combined
direction chart, or an all-scale refinement.

## Scale-dependent ill-conditioning

If the Hessian eigenvalues are dyadically stratified and those below
`theta` are discarded, the resulting lower-rank polynomial
`P_(≥theta)` satisfies

`||P-P_(≥theta)||_(L-infinity(B(0,2)))≤Ctheta`.

Hence

`N_delta(Z(P))
 subset {|P_(≥theta)|≤C(delta+theta)}`.

On a patch where `|grad P_(≥theta)|≥c`, this sublevel inclusion converts to
a geometric neighborhood of thickness `O(delta+theta)`. Without that lower
normal bound it is only a sublevel-set statement.

Only eigenvalues of order at most `delta` may be discarded while preserving
the original neighborhood scale. Normalizing an eigenvalue `theta` by an
anisotropic affine map has condition number at least `theta^-1/2` and
distorts tube widths, angles, and shading densities. Quantitative normal
forms must also charge the parabolic linear coefficient, the centering
translation, the lower normal bound, and the tangent discriminant.
Intermediate eigenvalues therefore require a charged dyadic output, not the
phrase “normalize the quadric.”

## Remaining global step

A general degenerate-carrier extraction theorem may now use four explicit
outputs:

1. affine-linear carriers and reducible hyperplane factors;
2. regular rank-at-most-two and central rank-three 2-plany carriers;
3. a singular conical-spine bush, currently only a model output until its
   shading density, annular localization, and common refinement are
   quantified;
4. indefinite rank-three parabolic families.

For output 4, the exact pencil proves the desired rigidity in one canonical
family. What remains is to organize an arbitrary bounded-entropy family of
rank-three parabolic forms into coefficient charts while retaining shading
mass and paying only `delta^o(1)`.

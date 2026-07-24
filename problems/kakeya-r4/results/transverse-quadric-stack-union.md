# Harmonic union bound for transverse ruled-quadric stacks

## Theorem

Fix constants `L,c_0,C_0>0`. There is `C`, depending only on these
constants, with the following property.

Let `0<delta≤lambda≤1`, `delta<1/100`, `2≤M≤C_0 delta^-1`, and let
`P_1,...,P_M` be coefficient-normalized real polynomials of degree at most
two.

Assume:

1. **Ruled sweep.** Each polynomial zero set contains a compact interior
   patch `X_i` parameterized by `F_i:Omega×I -> Z(P_i) intersect B(0,2)`,
   `F_i(y,t)=a_i(y)+t v_i(y)`, where `Omega` is a fixed planar box and `I`
   is a fixed interval. The `C²` norms are at most `L`, and `F_i` is
   `L`-bi-Lipschitz onto its image and has reach at least `L^-1`. The patches
   have a fixed collar in all three parameter variables so boundary effects
   can be discarded.
2. **Discretized dense shading.** A maximal delta-separated net
   `Lambda_i` of `Omega` is used. For every `y in Lambda_i`, a union
   `E_(i,y)` of delta-intervals in `I` has length at least `lambda`, and
   `U_i` is the union of `C(L) delta`-neighborhoods of
   `{F_i(y,t):t in E_(i,y)}`.
3. **Harmonic transversality.** Wherever `x` lies within `C delta` of both
   sweep patches `X_i,X_j`,

   `|grad P_i(x) wedge grad P_j(x)|
      ≥ c_0 |i-j|/M`.

Then

`|union_(i=1)^M U_i|
  ≥ c lambda² M delta /
      (1+M delta H_(M-1))`,

where `H_m=sum_(k=1)^m 1/k`. In particular, if
`c≤M delta≤C`, then

`|union_i U_i| ≥ c lambda²/log(2+M)`.

For `M≈delta^-1` this is
`lambda² delta^o(1)`: an exponent-level full dense-shading union estimate
for this ruled-quadratic subclass.

### Weighted sparse variant

Replace dense-shading hypothesis 2 by arbitrary, possibly empty or nonuniform,
shading sets, while retaining hypotheses 1 and 3. Define

`m_i=sum_(y in Lambda_i) |cell(y)| |E_(i,y)|`.

Then the identical proof gives

`|union_i U_i|
 ≥ c delta² (sum_i m_i)² /
   (M delta+M² delta² H_(M-1))`.                                (W)

The dense theorem is the special case `m_i≥c lambda` for every `i`.
Formula (W) is useful for scale-dependent subfamilies, but by itself is not
yet a complete Hausdorff covering argument.

## Proof

### 1. Each swept grain contributes `lambda delta`

Use the Voronoi cells of the maximal separated net, after discarding a fixed
boundary collar. They have diameter `O(delta)` and total area bounded below.
Define the parameter set

`A_i=union_(y in Lambda_i) cell(y) × E_(i,y)`.

Its three-dimensional measure is at least `c lambda`. If
`(z,t) in cell(y)×E_(i,y)`, the Lipschitz bound gives

`|F_i(z,t)-F_i(y,t)|≤C delta`.

Thus `F_i(A_i)` lies inside the shaded tube union. Thicken in the unit normal
direction to `X_i` by `|s|≤c delta`. The tubular map

`(z,t,s) -> F_i(z,t)+s n_i(z,t)`

has four-dimensional Jacobian bounded below and is injective for a fixed
normal radius depending only on `L`; this follows directly from the reach
hypothesis. It remains inside `U_i`. Hence

`|U_i|≥c lambda delta`.                                           (1)

Conversely `U_i` lies in a fixed-constant delta-neighborhood of `X_i`.
Since `X_i` is an `L`-Lipschitz image of a fixed three-dimensional box, its
tubular volume satisfies

`|U_i|≤C delta`.                                                  (2)

The proof of (1) permits arbitrary choices of the shading sets
`E_(i,y)`; no coherence in `t` across different lines is assumed.

### 2. Pairwise grain intersections

Let `A_(ij)` be the intersection of the two relevant patch neighborhoods.
Coefficient normalization implies that it is contained in

`{x in B(0,3): |P_i(x)|,|P_j(x)|≤C delta}`.

Apply coarea to the polynomial map `(P_i,P_j):R4->R2`. Its two-Jacobian is
`|grad P_i wedge grad P_j|`. Almost every common level is an algebraic
surface of degree at most four on the rank-two locus. Crofton plus Bézout
bounds the two-dimensional measure of that regular locus in `B(0,3)` by an
absolute constant: a generic affine two-plane meets it in at most four
isolated common zeros. Any common hypersurface factor is contained in the
rank-deficient locus and cannot meet `A_(ij)` under the transversality
hypothesis. Therefore coarea gives

`|A_(ij)|≤C delta² M/|i-j|`.                                     (3)

Since `U_i intersect U_j subset A_(ij)`, (3) bounds every off-diagonal
overlap.

### 3. Exact second moment

Write `f=sum_i 1_(U_i)`. Equations (1)–(3) give

`integral f ≥ c M lambda delta`

and

`integral f²
 ≤ C M delta
   + C sum_(i!=j) delta² M/|i-j|`

`≤ C M delta + C M² delta² H_(M-1)`.

Cauchy--Schwarz now yields

`|{f>0}| ≥ (integral f)²/(integral f²)`

`≥ c lambda² M delta/(1+M delta H_(M-1))`.

This is the claimed bound. The exact harness proves
`H_m≤1+floor(log_2 m)` by dyadic blocks and verifies the complete rational
second-moment ledger.

## Exact split-quadric sweep

The hypotheses are nonvacuous for the ruled model. In matrix coordinates,
put

`M(p,q,t) =
 [[t,       1+tq],
  [-1+tp,  p-q+tpq]]`.

Its determinant is identically one. Under the linear identification between
`SL_2(R)` and
`x1²+x2²-x3²-x4²=1`, this gives

`F(p,q,t)=(
 (t+p-q+tpq)/2,
 1+t(q-p)/2,
 (t-p+q-tpq)/2,
 t(p+q)/2)`.

For `t` in a compact interval away from zero, `F` is injective:
the matrix entries recover

`t=M_11`, `q=(M_12-1)/t`, `p=(M_21+1)/t`.

The `p,q,t` derivative has rank three; in matrix coordinates the minor using
the first three entries is `-t²`. The direction

`dF/dt=((1+pq)/2,(q-p)/2,(1-pq)/2,(p+q)/2)`

is the rank-one matrix `(1,p)^T(1,q)`, the standard affine Segre chart.
Therefore its projective parameter map has rank two everywhere. These
displayed identities prove the global assertions algebraically; the exact
rational harness additionally checks representative instances and all
second-moment exponent arithmetic.

## Explicit nonvacuous one-parameter pencil

Take

`q_0=x1²+x2²-x3²-x4²`,

`q_1=2x1x3+x3²`,

and `P_s=q_0+s q_1-1`. The `(x1,x3)` block of `q_0+s q_1` has determinant
`-1+s-s²<0`, while the `(x2,x4)` block has signature `(1,1)`. Thus every
member has split signature `(2,2)` and is ruled.

Put `r_s=sqrt(1-s+s²)` and define

`L_s x=(x1+s x3,x2,r_s x3,x4)`.

Then `(q_0+s q_1)(x)=q_0(L_s x)`. Therefore

`F_s=L_s^-1 F`

is an explicit two-parameter line sweep of `Z(P_s)`, where `F` is the
split-quadric sweep above. The maps and their inverses have uniform `C²`
bounds for small `s`.

The combined direction map has rank three. At `(s,p,q)=(0,0,0)`, its
direction and three parameter derivatives are

`w=(1/2,0,1/2,0)`,

`w_s=(-1/2,0,1/4,0)`,

`w_p=(0,-1/2,0,1/2)`,

`w_q=(0,1/2,0,1/2)`.

Their four-dimensional determinant has absolute value `3/16`. Thus, after
compact restriction, `(s,p,q)` is a uniform direction chart. The base point
`F(0,0,1)=(1/2,1,1/2,0)` also has
`|grad q_0 wedge grad q_1|>0`. Choose a fixed ambient ball around this point
on which that wedge stays bounded below. Since

`grad P_s wedge grad P_(s')
 =(s'-s) grad q_0 wedge grad q_1`,

every possible double overlap inside this ball has the required lower bound,
not merely points on the exact common zero set. Restrict all sweep patches to
the ball, normalize polynomial coefficients (a uniformly bounded change),
and discretize a fixed `s`-interval at spacing comparable to `1/M`. This
supplies an explicit infinite family satisfying the theorem's sweep,
direction, and harmonic-transversality hypotheses.

## Kakeya consequence and boundary

If, in addition, the maps `(i/M,y) -> v_i(y)/|v_i(y)|` form finitely many
uniform coordinate charts for a three-dimensional direction set, with one
delta-separated tube per direction, the theorem is a dense shaded estimate
with only a logarithmic loss. With full shadings it gives

`|K_(C delta)|≥c/log(1/delta)`.

Thus a compact Kakeya set whose discretizations obey these uniform stack
hypotheses has full lower and upper Minkowski dimension four.

The theorem as stated does **not** imply Hausdorff dimension four. A
Hausdorff covering argument produces sparse, scale-dependent active
directions, whereas the current hypotheses require a dense parameter net in
every active carrier. A weighted sparse-stack estimate and a separate
covering argument would be needed for that stronger conclusion.

That separate argument is now supplied in `fixed-stack-hausdorff.md` under
one additional, essential hypothesis: the scale discretizations sample a
single fixed continuum line family, or equivalently obey its
incidence-Carleson condition for every cover. Thus the explicit fixed pencil
does have Hausdorff dimension four, while unrelated per-scale stacks still
have only the conclusion stated here.

This is a new structured-subclass theorem, not the general conjecture:

- it assumes, rather than extracts, the ordered quadratic carriers;
- it assumes a full two-parameter sweep inside every carrier;
- it assumes harmonic transversality on the entire relevant sublevel
  intersection;
- it does not show that near-extremal trilinear sticky families have this
  structure.

The result advances Bridge B by supplying the inner/outer union estimate once
a ruled degree-two branch has been organized into a transverse stack.

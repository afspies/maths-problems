# Four-dimensional Kakeya: full-conjecture extraction frontier

**Status:** partial-results, Bridge B gate GO · **Date:** 24 July 2026

## Abstract

The full four-dimensional Kakeya conjecture remains open. The current
benchmarks are unchanged: general Hausdorff dimension above `3.059`, sticky
Hausdorff dimension `13/4`, and the distinct maximal-function estimate near
`3.0543`.

This campaign proves semialgebraic union and Hausdorff covering theorems for
a fixed all-scale family of ruled quadratic obstructions. A stack of
`M≈delta^-1` ruled quadric patches whose mutual normal angles grow like
index separation has dense shaded union at least
`lambda²/log(1/delta)`. If the scale-wise stacks sample one fixed continuum
line family, a weighted incidence argument gives Hausdorff dimension four.

The campaign also proves that small union alone extracts only a
high-multiplicity incidence level, not a quadratic carrier, and gives an
exact transverse-slab countermodel to constant distributed overlap. Once
carriers are supplied, small union forces quantified low-Jacobian energy.
A separate normal-form theorem classifies the degenerate quadratic branches
and isolates indefinite rank-three parabolics as the genuine nonlinear
exception. No new general or sticky dimension bound, and no
full-conjecture claim, is made.

The campaign also proves exact one-carrier capacity, catalog-evasion,
distributed-catalog extraction, and sticky carrier-entropy lemmas. All
exponent arithmetic and algebraic models are checked by a 27-test exact
rational harness.

## Main result

### Harmonic transverse-stack theorem

Let `P_1,...,P_M` be coefficient-normalized quadratics with
`M≤C delta^-1`. Suppose each zero set contains a uniformly regular ruled
patch `X_i` with a two-parameter line sweep, fixed reach and collars. On a
maximal `delta`-net of ruling parameters, shade at least a `lambda` fraction
of every line. Assume that throughout every possible double-overlap region,

`|grad P_i wedge grad P_j|≥c |i-j|/M`.

Then

`|union_i U_i|
 ≥ c lambda² Mdelta/(1+Mdelta H_(M-1))`.

In particular, for `M≈delta^-1`,

`|union_i U_i|≥c lambda²/log(2+M)`.

### Proof ledger

The reach hypothesis and dense sweep give

`|U_i|≥c lambda delta`, while `|U_i|≤C delta`.

On the rank-two locus, coarea and Crofton--Bézout give

`|U_i intersect U_j|≤C delta² M/|i-j|`.

The transversality hypothesis excludes common hypersurface factors from the
overlap region. For `f=sum_i 1_(U_i)`,

`integral f≥c Mlambda delta`,

`integral f²≤C Mdelta+C M²delta² H_(M-1)`.

Cauchy--Schwarz proves the result. The weighted sparse version replaces
`lambda M` by the total integrated shading mass.

### Fixed-stack Hausdorff theorem

For a fixed measurable segment family define

`A(V)=integral |{t:F(theta,t) in V}| dmu(theta)`.

If every sufficiently small dyadic `r` obeys

`|N_(Cr)(V)|>=c A(V)^2/L(r)`

for every measurable `V`, and

`sum_(dyadic r<=r_0) r^(4-s)L(r)->0`

for every `s<4`, a dyadic cover argument gives
`H^s(K)=infinity` and hence `dim_H K=4`. A fixed continuum harmonic stack
satisfies this with `L(r)=1+log(1/r)`.

More generally, a cover-by-cover extraction theorem that retains
`b(r)=r^o(1)` of `A(V)` in one admissible transverse chart is sufficient,
because its loss is

`L(r)=(1+log(1/r))/b(r)^2`.

This is the precise full-conjecture target. Extracting unrelated stacks from
the whole tube union at each scale does not control arbitrary Hausdorff
covers.

### Explicit infinite ruled family

Write

`q_0=x1²+x2²-x3²-x4²`,

`q_1=2x1x3+x3²`,

`P_s=q_0+s q_1-1`.

Every member has split signature. With

`L_s(x)=(x1+s x3,x2,sqrt(1-s+s²)x3,x4)`,

one has `(q_0+s q_1)(x)=q_0(L_s x)`, so transporting the exact
`SL_2(R)` line sweep gives a ruled sweep for every `s`.

At the rational seed `(s,p,q)=(0,0,0)`, the carrier/direction chart
determinant has absolute value `3/16`. Moreover,

`grad P_s wedge grad P_(s')
 =(s'-s) grad q_0 wedge grad q_1`.

Compact restriction therefore produces the theorem's uniform
transversality. Finitely many direction charts give the stated structured
full-dimensional subclass. This particular smooth four-parameter sweep has
rank four at the checked seed and therefore positive measure locally; it is
a nonvacuity model, not a delicate measure-zero construction.

## Carrier capacity and extraction

### One conditioned quadric

If a tube spends a `lambda` fraction near a quantitatively nondegenerate
quadric, degree-two Remez forces its direction within
`O(delta lambda^-2)` of the quadratic null cone. Thus one carrier holds at
most

`O(min(delta^-3,delta^-2 lambda^-2))`

separated directions. At full overlap this is `O(delta^-2)`, so a full
direction family needs about `delta^-1` carriers.

### Low-entropy catalogs

For `#T≥delta^(-3+tau)`, a catalog of `M≤delta^-h` grains, overlap
`lambda=delta^a`, and QW2 loss `delta^-b`, the carried fraction is at most

`C delta^(1-h-tau-4a-b)`.

Katz--Rogers already prove QW2 with arbitrarily small power loss for
direction-separated tubes. Hence a bounded catalog cannot explain a full
Kakeya family; the missing geometry is multi-grain organization.

### Distributed catalog theorem

For grains `S_j`, put

`q=N^-1 sum_T sum_j |T intersect S_j|/|T|`

and `H=sum_j |S_j|^(1/4)`. If `Delta` is the normalized maximum QW2 load,
layer cake gives

`Delta≥c Ndelta³(q-Mdelta)_+^4/H^4`.

A dyadic refinement outputs an explicit polynomial, overlap level, and
balanced tube subfamily. The theorem converts catalog capture into a
certificate; it does not infer capture from small union volume.

### Sticky entropy obstruction

At scale `h=delta^a`, if a sticky family puts fraction `delta^tau` at
overlap `delta^ell` on at most `delta^-zeta` conditioned quadrics, then in
the nontrivial overlap regime it must satisfy

`tau+zeta+2ell≥a(1-2epsilon)`.

This rules out the original symmetric low-entropy inverse output in a
nonempty exponent regime. The split-quadric thinning stress test also cannot
be both sticky and extremal for loss `eta<1/2`.

## What small union does and does not extract

Let `A=sum_T |Y(T)|`, `V=|union_T Y(T)|`, and
`m=sum_T 1_(Y(T))`. Then

`integral m²>=A²/V`,

and the set `{m>=A/(2V)}` carries at least half the incidence mass. A dyadic
level loses only

`L_mu=1+ceil(log_2(2NV/A))`.

This contains no polynomial or ruling. The exact obstruction is a grid of
`M≈delta^-1` transverse hyperplane slabs. Every tube in a fixed direction
cap crosses every slab for length `Theta(delta)`, so
`q≈Mdelta≈1` without any assigned overlap `lambda>>delta`. Therefore a valid
carrier theorem must extract assigned overlap, excess `q-Mdelta`, or a
geometric rule that excludes ordinary crossings.

If `M` genuine quadratic carrier patches have shaded unions
`|U_i|≈lambda delta`, then coarea and the second moment give

`|union_i U_i|
 >= c M²lambda²delta²/
 (Mdelta+sum_(i<j) min(delta,delta²/kappa_(ij)))`,

where `kappa_(ij)` is the infimum of
`|grad P_i wedge grad P_j|` on the double patch. Thus small carrier union
forces large inverse-transversality energy. Classifying that energy with
subpolynomial model entropy is the missing step, not a consequence of the
inequality.

## Degenerate quadratic branch

After an orthogonal splitting and translation, a quadratic has central form
`q_r(y)+c` or parabolic form `q_r(y)+z`. Regular irreducible nonlinear
Hessian rank at most two, and regular central rank three, are pointwise
2-plany. Affine or reducible hyperplanes and a conical singular spine must be
kept as separate outputs. The genuine smooth ruled nonlinear exception is
the indefinite rank-three paraboloid.

For the exact pencil

`P_s=z-y_1y_2-sy_3²`,

the normal identity is

`|grad P_s wedge grad P_t|
 =2|s-t||x_3||grad P_s wedge e_3|`.

Away from `|x_3|<=rho`, the stack theorem therefore loses the genuine factor
`rho`; inside the slab, the ruling directions lie close to a 2-plany
alternative. This is a rigorous transverse-versus-plany stress model, but
optimizing the `rho` loss across scales remains open.

## Exact verification

From `problems/kakeya-r4/harness/`:

```bash
python3 exponent_ledger.py benchmark_ledger.json
python3 -m unittest -v
```

The ledger returns volume exponent `3/4`, dimension `13/4`, and bottleneck
`trilinear`. All 33 tests pass. They verify exact recurrence arithmetic,
harmonic second moments, catalog exponents, sticky persistence inequalities,
high-multiplicity and carrier-energy ledgers, the split-quadric sweep,
rank-three parabolic line conditions, normal-wedge identities, and the
transverse pencil's rank-four seed.
Continuous coarea, reach, Remez, and algebraic-degree arguments are written
as proofs rather than delegated to numerical tests.

## Gate verdict and boundary

Independent GPT-5.6 Sol reviews at xhigh effort required repairs to reach,
rank-two coarea, the explicit pencil, weighted normalization,
Hausdorff-versus-Minkowski wording, the transverse `rho` loss, the
hyperplane exception, and measurable-cover sampling. The repaired statements
then received `APPROVE` verdicts for exponent signs, circularity, scale loss,
and endpoint consequences.

The two-session gate remains **GO on Bridge B**: the union theorem handles an
infinite family of ruled obstructions, and the fixed-family criterion gives
full Hausdorff dimension for a structured all-scale subclass. The
full-conjecture gate itself is **OPEN**. The decisive missing theorem is
uniform shaded extraction with subpolynomial chart entropy, assigned
positive overlap above the `Mdelta` baseline, and persistence for arbitrary
cover groups.

No DOI is assigned because the general conjecture remains open.

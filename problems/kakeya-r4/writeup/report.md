# Four-dimensional Kakeya: degree-two carrier campaign

**Status:** partial-results, Bridge B gate GO · **Date:** 24 July 2026

## Abstract

The full four-dimensional Kakeya conjecture remains open. The current
benchmarks are unchanged: general Hausdorff dimension above `3.059`, sticky
Hausdorff dimension `13/4`, and the distinct maximal-function estimate near
`3.0543`.

This campaign proves a semialgebraic union theorem for an explicit infinite
family of ruled quadratic obstructions. A stack of `M≈delta^-1` ruled
quadric patches whose mutual normal angles grow like index separation has
dense shaded union at least `lambda²/log(1/delta)`. Dense Kakeya
discretizations satisfying finitely many such stack charts therefore have
full Minkowski dimension four. No Hausdorff consequence, general carrier
extraction, strict sticky improvement, or full-conjecture claim is made.

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
`lambda M` by the total integrated shading mass; it is not yet a complete
Hausdorff covering argument.

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
full-Minkowski subclass.

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

## Exact verification

From `problems/kakeya-r4/harness/`:

```bash
python3 exponent_ledger.py benchmark_ledger.json
python3 -m unittest -v
```

The ledger returns volume exponent `3/4`, dimension `13/4`, and bottleneck
`trilinear`. All 27 tests pass. They verify exact recurrence arithmetic,
harmonic second moments, catalog exponents, sticky persistence inequalities,
the split-quadric sweep, and the transverse pencil's rank-four seed.
Continuous coarea, reach, Remez, and algebraic-degree arguments are written
as proofs rather than delegated to numerical tests.

## Gate verdict and boundary

Independent GPT-5.6 Sol reviews at xhigh effort first required repairs to the
reach hypotheses, rank-two coarea argument, explicit pencil, weighted
normalization, and Hausdorff wording. After repair the theorem received an
`APPROVE` verdict, including its exponent signs and Minkowski-only
consequence.

The two-session gate is therefore **GO on Bridge B**: the main theorem is a
nontrivial semialgebraic factoring/union lemma for an infinite family of
ruled obstructions. The remaining decisive task is an extraction dichotomy
that organizes grains from a small arbitrary union into harmonic stacks or
a classified degenerate branch.

No DOI is assigned because the general conjecture and Hausdorff problem
remain open.

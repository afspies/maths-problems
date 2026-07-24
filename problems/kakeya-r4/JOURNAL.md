# Journal — Four-dimensional Kakeya conjecture

Append-only. One dated section per session: what was tried (exact commands,
encodings, parameters), outcomes, compute spent and where it ran. Newest at the
bottom. Do not rewrite history — corrections get their own dated entry.

## 2026-07-24 — scaffolded

Problem folder created from template. No work yet.

## 2026-07-24 — sticky grains proof-first audit

### Scope and exact harness

Worked on branch `problem/kakeya-r4/2026-07-24-sticky-grains`, only in this
problem folder plus the generated repository board. The verifier was built
before the proof campaign. It uses `fractions.Fraction` throughout and covers:

- the exact `3/4` versus `2/3` branch aggregation and dimension conversion;
- the extremal multiplicity sign;
- the Section 6 scale-count, trilinear, plany, scale-interval, and strict
  planebrush-parameter checks;
- exact rational plany, trilinear, and ruled-quadric incidence models.

Commands:

```bash
python3 tools/new_problem.py kakeya-r4 --title "Four-dimensional Kakeya conjecture"
cd problems/kakeya-r4/harness
python3 exponent_ledger.py benchmark_ledger.json
python3 -m unittest -v
```

The ledger printed global exponent `3/4`, dimension `13/4`, bottleneck
`trilinear`. All 15 tests passed in 0.001 seconds.

### Literature audit

Primary-source audit through 24 July 2026 found:

- general R⁴ Hausdorff lower bound
  `3+(sqrt(17665)-97)/600>3.059` from corrected Katz–Zahl;
- separate maximal-function record
  `(159+sqrt(145))/56≈3.0543` from arXiv:2511.22824, whose final remark says
  it does not improve the Hausdorff record;
- sticky R⁴ Hausdorff bound `13/4`, with no later improvement found;
- full R³ sticky and general results, plus restricted and finite-field
  results kept in separate categories.

The 2511.22824 graininess/multiplicity discussion supplies balanced
bookkeeping and a suggested improvement, not an R⁴ inverse theorem.

### Independent 13/4 reconstruction

Reconstructed Definitions 3.1–3.11, Proposition 3.12, the trilinear/plany
dichotomy, Theorems 5.4–5.5, and the Section 6 induction. The global
bottleneck is exactly the trilinear `3/4` branch; the plany `2/3` branch has
an exponent gap `1/12`.

The source ledger records four repairable bookkeeping/admissibility issues:

1. the average-multiplicity display needs `-sigma_n+2 eta`, not
   `sigma_n+2 eta`;
2. minimal `N` with `4/N<epsilon_0` gives
   `epsilon_0/(4+epsilon_0)≤1/N<epsilon_0/4`, invalidating two printed
   comparisons;
3. the intermediate-scale interval needs `eta_0≤1/N`;
4. the strict planebrush hypothesis is repaired by replacing the printed
   exponent `1` with fixed `a` satisfying `sigma_4<a<1`.

The first two change no geometry; the last two are elementary admissibility
repairs. The harness certifies a rational repaired exponent regime but does
not formalize the imported geometric theorems.

### Bridge A: sticky multiscale

Wrote the exact conditional implication: a uniform trilinear gain
`delta^(-c)`, with `0<c<1/12`, relative to the full Theorem 5.4 right-hand
side would leave plany gain `rho^(-(1/12-c))` and imply
`dim_H≥13/4+c`.

The preferred inverse-trilinear/two-scale-ruled-rigidity pair was
pressure-tested. Proposition 3.12 balances one selected scale but provides
neither near-equality stability, bounded model entropy, nor a common
positive-mass refinement at two scales. A polynomial model-selection loss
must be explicitly subtracted from any proposed `c`. No inverse theorem or
fixed gain was proved.

### Bridge B: semialgebraic reduction

Reconstructed the Wang–Zahl R³ convex factoring skeleton and marked five R⁴
failure points. Built the split quadric exactly via its `SL_2` model. Three
rational concurrent lines have normalized squared wedge `1/50`, so ruledness
does not imply 2-planiness.

The raw line net fails Convex Wolff in a tangent prism. The actual
countermodel is the thinned net followed by `delta^(-1/2)` moved copies. A
degree-two polynomial-Wolff test was defined and detects every thinned copy
by `delta^(-1/2)`. This is an exact obstruction/detection lemma, not a union
or carrier-extraction theorem.

### Adversarial reviews and verdict

At attack selection and again after theorem formulation, independent
GPT-5.6 Sol agents were run with model `gpt-5.6-sol` and effort `xhigh`.
The reviews checked hypotheses, exponent signs, epsilon losses,
Hausdorff/Minkowski implications, circularity, and cross-scale loss.

Verdict: prefer Bridge B's degree-two carrier-extraction target for a future
campaign, but **STOP/PIVOT now**. None of the two-session GO conditions was
met. In particular, the exact quadric stress test and repaired ledger must
not be described as a new dimension bound, inverse theorem, or
semialgebraic union theorem.

No numerical tube search or substantial compute was used. Work ran in the
local Codex repository worktree; source extraction and all exact tests took
negligible laptop-scale compute. No private infrastructure details are
recorded.

## 2026-07-24 — degree-two carriers and transverse stacks

### Wide-net search and literature correction

Continued on branch `problem/kakeya-r4/2026-07-24-quadric-carriers`. The
search split cleanly into four independent theorem targets: one-carrier
direction capacity, low-entropy catalog evasion, diffuse catalog extraction,
and an inner/outer union theorem for an ordered carrier stack.

The source audit corrected an important premise from the first session:
Katz--Rogers already prove the bounded-complexity semialgebraic polynomial
Wolff axiom, up to `delta^-epsilon`, for direction-separated tubes. Zahl also
proves the sharper `O(delta^(-2-epsilon))` bound for tubes contained near one
fixed low-degree hypersurface in R⁴. Thus QW2 itself is not the missing
conjectural input; the missing step is organizing many detected grains and
proving their union cannot remain small.

### Exact carrier-capacity and extraction lemmas

Proved four scale-explicit statements.

1. A tube spending a `lambda` fraction near a quantitatively nondegenerate
   quadric has direction within `O(delta lambda^-2)` of its null cone, hence
   one carrier holds at most
   `O(min(delta^-3,delta^-2 lambda^-2))` separated directions.
2. QW2 forces a catalog of `M≤delta^-h` quadrics to miss almost every tube
   whenever the exact saving `1-h-tau-4a-b` is positive.
3. If overlap is spread among `M` grains rather than pre-assigned, layer cake
   forces an explicit polynomial, dyadic overlap level, and balanced
   subfamily. Its sharp normalized load satisfies
   `Delta≥c N delta³(q-Mdelta)_+^4/H^4`.
4. At a sticky scale `h`, a conditioned quadratic catalog persisting with
   exponents `(tau,zeta,ell)` must pay
   `tau+zeta+2ell≥a(1-2epsilon)`. In particular the earlier symmetric
   low-entropy inverse output is impossible in a nonempty exponent regime.

The exact split-quadric thinning stress test was also audited at every scale.
It can be balanced and trilinear, but making it extremal by thinning destroys
the sticky direction-cap requirement: the inequalities
`beta≤eta` and `beta≥1-eta` are incompatible for `eta<1/2`.

### Harmonic transverse-stack theorem

Proved an inner/outer union theorem for an infinite family of ruled degree-two
obstructions. For `M≤C delta^-1` ruled sweep patches with uniform reach,
dense `lambda`-shadings, and

`|grad P_i wedge grad P_j|≥c |i-j|/M`

on every possible double-overlap region,

`|union_i U_i|≥c lambda² Mdelta/(1+Mdelta H_(M-1))`.

At `M≈delta^-1` this is `lambda²/log M`. The proof combines a reach-based
`lambda delta` lower bound for each swept grain, a coarea plus
Crofton--Bézout overlap estimate
`|U_i intersect U_j|≤C delta²M/|i-j|`, and the exact second moment.
A weighted sparse version is recorded separately.

Nonvacuity is algebraic, not pictorial. The checked-in split-quadric sweep is
transported by

`L_s(x)=(x1+s x3,x2,sqrt(1-s+s²)x3,x4)`.

For `P_s=q_0+s(2x1x3+x3²)-1`, the combined carrier/direction chart has exact
seed determinant `3/16`, and
`grad P_s wedge grad P_(s')=(s'-s) grad q_0 wedge grad q_1`.
After compact restriction this supplies the required uniform stack.

Consequently, dense Kakeya discretizations obeying finitely many such
uniform stack charts have full lower and upper Minkowski dimension four.
This does **not** prove Hausdorff dimension four: scale-dependent sparse
directions need a further covering argument. It also assumes rather than
extracts the carrier stack.

### Independent soundness reviews and gate

Independent GPT-5.6 Sol agents at `xhigh` effort audited the algebraic pencil,
the coarea/rank locus, reach and collar hypotheses, exponent signs, the
weighted normalization, circularity, scale losses, and
Hausdorff-versus-Minkowski implications. The first review required explicit
reach, common-factor exclusion, a viable transverse pencil, and deletion of
an unsupported Hausdorff conclusion. After those repairs, the final verdict
was **APPROVE**. A separate xhigh review approved the distributed-catalog
layer-cake theorem and warned that it does not infer catalog capture from
small union volume.

The two-session gate is therefore **GO on Bridge B**: the harmonic
transverse-stack theorem is a nontrivial semialgebraic union lemma for an
explicit infinite family of ruled obstructions. The full Kakeya conjecture,
a strict sticky exponent improvement, carrier extraction, and any new
Hausdorff bound remain open.

### Verification and compute

Commands:

```bash
cd problems/kakeya-r4/harness
python3 exponent_ledger.py benchmark_ledger.json
python3 -m unittest -v
git diff --check
```

The ledger printed global exponent `3/4`, dimension `13/4`, and bottleneck
`trilinear`. All 27 exact tests passed in 0.021 seconds. No numerical tube
search or substantial compute was used. Work and independent reviews ran in
the local Codex worktree at negligible laptop scale; no private
infrastructure details are recorded.

## 2026-07-24 — full-conjecture extraction frontier

### Scope and literature

Continued on branch
`problem/kakeya-r4/2026-07-24-extraction-dichotomy`. The wide-net audit added
the regular direction-to-position map results of Fu--Gan and the continuous
full-line configuration theorem of Murphy--Pakianathan. These give
full-measure structured subclasses but do not extract regularity from an
arbitrary Kakeya segment selector. The audit also retained the strict
separation among the general Hausdorff, maximal-function, sticky,
restricted, and finite-field benchmarks.

### What small union extracts

Proved the unconditional multiplicity statement: if total shaded incidence
is `A` and union volume is `V`, the level

`{m>=A/(2V)}`

carries at least `A/2`, and a dyadic multiplicity level costs only
`1+ceil(log_2(2NV/A))`. This supplies no carrier or ruling.

For a separately supplied bounded-complexity catalog, exact layer-cake and
polynomial-Wolff accounting show that assigned positive overlap is the
useful output. A grid of `M≈delta^-1` transverse hyperplane slabs gives the
countermodel `q≈Mdelta≈1` while every individual overlap is only
`Theta(delta)`. Thus constant distributed catalog overlap is contaminated by
ordinary crossings and cannot be called extraction.

Once genuine carrier patches exist, coarea and the second moment give the
inverse-energy bound

`|union U_i|
 >=c M²lambda²delta²/
   (Mdelta+sum_(i<j)min(delta,delta²/kappa_(ij)))`.

The local Jacobian-stratified form forces high low-rank mass when the union
is small. It still requires a new classification theorem before one may
deduce a coherent pencil, 2-planiness, or cross-scale persistence.

### Hausdorff upgrade

Proved a weighted covering theorem for one fixed measurable segment family.
If

`|N_(Cr)(V)|>=c A(V)²/L(r)`

holds for every measurable `V` and dyadic `r`, and
`sum r^(4-s)L(r)->0`, then `H^s(K)=infinity` for every `s<4`. A fixed
continuum harmonic transverse stack satisfies the hypothesis with
`L(r)=1+log(1/r)`.

The exact full-conjecture criterion is now explicit: a cover-by-cover
extraction theorem retaining `b(r)=r^o(1)` of the incidence mass in one of
`r^-o(1)` fixed transverse charts would prove Hausdorff dimension four.
Point-sampled scale nets and independently chosen whole-union stacks do not
give the required incidence-Carleson control.

### Degenerate quadrics

Classified nonconstant quadratic carriers by Hessian rank. Regular
irreducible nonlinear rank at most two and regular central rank three are
pointwise 2-plany. Affine/reducible hyperplanes, conical spines, and
ill-conditioned coefficient regimes must be charged as separate outputs.
The genuine smooth ruled nonlinear degenerate exception is the indefinite
rank-three paraboloid.

For the exact pencil

`P_s=z-y_1y_2-sy_3²`,

the harness verifies its line equations, a concurrent trilinear triple, and

`|grad P_s wedge grad P_t|
 =2|s-t||x_3||grad P_s wedge e_3|`.

Away from the slab `|x_3|<=rho`, the harmonic stack theorem pays a genuine
factor `rho`; inside, the directions enter a weakly 2-plany alternative.
This is an exact two-branch stress model, not a scale-loss-free rigidity
lemma.

### Independent soundness reviews and verdict

Three GPT-5.6 Sol agents at `xhigh` effort audited the extraction accounting,
Hausdorff cover summation, Remez--Markov step, degenerate normal forms,
quasi-uniform sampling, exponent signs, scale loss, circularity, and
Hausdorff-versus-Minkowski implications. Initial reviews required:

- cell averaging rather than unsupported point sampling;
- explicit separation of affine/reducible hyperplanes;
- a real `rho^-1` transverse loss for the parabolic pencil;
- quantitative regularity and coarea hypotheses;
- quasi-uniform parameter sampling and outside-slab patch collars.

After repair, the final verdicts were **APPROVE**. The full conjecture remains
open. The proved advance is a fixed-family Hausdorff theorem, an exact
extraction no-go/accounting theorem, and a degenerate quadratic
classification that isolates the remaining full-to-structured bridge.

### Verification and compute

Commands:

```bash
cd problems/kakeya-r4/harness
python3 exponent_ledger.py benchmark_ledger.json
python3 -m unittest -v
python3 -m py_compile *.py
git diff --check
```

All 33 exact tests pass. No numerical tube search or substantial compute was
used. Work and independent reviews ran in the local Codex worktree at
negligible laptop scale; no private infrastructure details are recorded.

## 2026-07-24 — parabolic coefficient charts and parent ancestry

### Session target

Continued on branch
`problem/kakeya-r4/2026-07-24-shaded-parabolic-charts`. The target was the
first unresolved part of the full-conjecture bridge: handle arbitrary
indefinite rank-three parabolic carriers more sharply, and cross the
`Mdelta` transverse catalog baseline without assuming assigned long overlap.

### Rank-two-separated parabolic stacks

Proved a new quadratic-sublevel union theorem. For graph quadrics

`P_s(y,z)=z-y^T A_s y-ell(y)`

with common affine term and

`sigma_2(A_s-A_t)≥c|s-t|`,

the three-dimensional coefficient-difference sublevel has volume

`O((delta/kappa)(1+log(1/delta)))`.

After the `z`-fiber and quasi-uniform parameter summation, the carrier
overlap denominator pays two logarithms:

`|union_i U_i|
 ≥c lambda² Mdelta/
   (1+Mdelta(1+log(1/delta))H_(M-1))`.

At `M≈delta^-1` this is `lambda²/log²(1/delta)`. The continuum kernel gives

`|N_(Cr)(V)|≥c A(V)²/log²(1/r)`,

so a fixed all-scale family has Hausdorff dimension four. This extends the
earlier stack theorem because carrier normals may coincide on a
one-dimensional locus.

The exact nonvacuity path

`A_s=diag((1+s)²,-1,(1+s)²)`

has rank-two coefficient separation. Its ruled sweep and direction chart
both have exact seed determinant of absolute value `4`.

### Rank-one rigidity and its first rotating obstruction

Proved an exact complete-clique theorem. If every pair difference among
quadratic graph functions is constant or a zero-critical-value affine square
`c ell²`, then either all forms differ only by constants or the entire family
is one common-square pencil

`f_i=f_*+a_i ell²`.

The complete-clique and exact-critical-value hypotheses are essential.
Connected dangerous graphs do not suffice.

The rotating rank-one moment path

`A(s)=integral_0^s(1,t,0)(1,t,0)^Tdt`

has rank-one derivative everywhere but rank-two finite differences with
principal determinant `h^4/12`. Its second singular value is only order
`h³`. This exact stress model shows why infinitesimal rank-one classification
does not reduce directly to either the common-square pencil or the
linearly-separated theorem.

### Parent ancestry and additive Hausdorff errors

Proved the degree-`D` line-sublevel lemma

`|{t:|P(ell(t))|≤Cr, |(P circ ell)'(t)|≥alpha}|
 ≤C D r/alpha`.

If descendant grains retain measurable union/unique assignments under at
most `K` distinct parent polynomials per line, all transverse descendant
incidence is therefore at most

`C K D r/alpha`,

with no descendant-count factor. Parallel unrelated slabs have `K=M` and
recover the old `Mr` baseline; many grains cut from one wall have `K=1`.
The remainder is nontransverse-or-singular, and becomes geometric tangency
only under a lower gradient bound.

Also proved an additive-error Hausdorff criterion. If every cover group has

`A(V)≤sum_(nu≤J(r)) A_nu(V)+e(r)`,

where the `A_nu` are genuine fixed/cell-averaged continuum chart
functionals satisfying SSI, then full dimension follows from

`sum e(r)->0`

and

`sum r^(4-s)J(r)²L_0(r)->0`.

This makes `K D r/alpha=r^(1-o(1))` a harmless transverse error. It does not
organize the remaining mass into charts; proving that is still the missing
theorem. Lusin selection supplies additive retention but no quantitative
modulus, admissible chart, or subpolynomial entropy.

### Independent reviews and repairs

Three independent GPT-5.6 Sol agents at `xhigh` effort audited the sublevel
estimate, every harmonic factor, continuum normalization, Hausdorff cover
summation, determinant certificates, parent-assignment semantics,
singular-gradient alternative, coefficient-chart thresholds, and
circularity.

Repairs required:

- fail loudly unless the exact rational double-harmonic ledger is used at
  critical spacing `Mdelta=1`;
- verify the two determinant values, not only rank;
- use buffered `2eta/eta` coefficient thresholds and charge both chart count
  and the `eta`-dependent analytic loss;
- union or uniquely assign descendant incidences under each parent;
- call the unaccounted output nontransverse-or-singular without a lower
  gradient bound;
- require genuine continuum chart incidence functionals in the additive
  criterion;
- state that Lusin gives retention but not SSI geometry.

After repair, the final verdicts were **APPROVE**. The full conjecture and
general/sticky benchmarks remain unchanged.

### Verification and compute

Commands:

```bash
cd problems/kakeya-r4/harness
python3 exponent_ledger.py benchmark_ledger.json
python3 -m unittest -v
python3 -m py_compile *.py
git diff --check
```

All 39 exact tests pass. No numerical tube search or substantial compute was
used. Work and reviews ran in the local repository worktree at negligible
laptop scale; no private infrastructure details are recorded.

# Journal — Vizing’s domination conjecture

Append-only. One dated section per session: what was tried (exact commands,
encodings, parameters), outcomes, compute spent and where it ran. Newest at the
bottom. Do not rewrite history — corrections get their own dated entry.

## 2026-07-23 — scaffolded

Problem folder created from template. No work yet.

## 2026-07-23 — proof-first constant and subset stability

### Source audit and reconstruction

- Downloaded and read arXiv:2606.14414v1 and archived
  arXiv:2607.01109v1. Queried current arXiv metadata for the latter; v2 carries
  the author comment `Algebraic mistake` and has no current PDF.
- Independently reconstructed Steiner's dependency chain:
  matching Lemmas 2.1/2.2 → subset Lemma 2.3 → fibre Theorem 1.4; Brešar and
  Hou–Lu inputs → six-term four-parameter minimax.
- Re-derived the exact minimizer. With
  `c=(5+√73)/24`, `a=2-3c`, `b=3/2-2c`, the old relaxed feasible point
  `x₁=y₁=a`, `x₂=y₂=b` makes all six bounds equal `c`. Therefore
  reoptimizing those bounds cannot improve the universal constant.
- Located the precise failure in the withdrawn 0.5809 proof. Its quoted
  Chen–Piotrowski–Shreve term becomes
  `A(B-y)+(A-x)y=AB-xy`, but equation (2.2) replaces it by
  `3AB-2Ay-2xB+xy`. At `A=B=10,x=y=7`, these are 51 and 69.

### New subset results

- Defined `δ_G(S)=|S|+ρ²(G)-3γ_G(S)`.
- Proved the exact dense-step identity
  `δ(S)=δ(S')+(q-3)+3e`, with
  `q=|N[v]∩S|` and `e=γ(S')+1-γ(S)`.
- In the two-sparse terminal case, proved the exact decomposition
  `δ=(ρ²-r-γ)+(|S|+r-2γ)`. This gives a recursive equality
  classification and a stability classification when `δ≤2`.
- Defined the excess-peeling parameter `p_G(S)` and proved
  `3γ_G(S)≤|S|+ρ²(G)-p_G(S)`. Propagating it through Steiner's proof gives
  the instance-sensitive product bound
  `γ(G□H)≥((3γ(G)-ρ²(G))/4)γ(H)+(Σ_i p_G(L_i))/4`.
  No universal positive lower bound on the sum is yet known.

### k=3 attempt

- Formulated the naive analogue
  `4γ_G(S)≤|S|+ρ³(G)` and refuted it exactly on the graph with edges
  `01,03,04,12,14,23`, `S={2,3,4}`: `γ_G(S)=2`, `ρ³(G)=4`.
- Repaired it by proving
  `5γ_G(S)≤2|S|+ρ³(G)`. Add Steiner's Lemmas 2.3 and 2.2, then use
  `ρ³(G)≥ρ²(G)+ρ_G(S)`. This yields
  `γ(G□H)≥((5γ(G)-ρ³(G))/7)γ(H)`.
- Exact reoptimization gives no improved universal constant. At Steiner's
  old equality point set `x₃=y₃=(2b+a)/3`; the new product bound also equals
  `c`, while its Hou–Lu mixed term is below `c`.

### Required xhigh reviews

- **Bridge-choice review (GPT-5.6 Sol, xhigh):** accepted the slack and
  peeling proof; found the corrected `k=3` inequality; warned that neither
  inequality raises the global constant without a new aggregate/strict
  structural relation. Exact minimax obstruction supplied and incorporated.
- **Completed-proof review (GPT-5.6 Sol, xhigh):** `ACCEPT with mandatory
  wording corrections`. Confirmed every coefficient and the maximum over
  peeling sequences. Required explicit distinction between equality in the
  original and strengthened inequalities and between arbitrary and complete
  peeling sequences; corrections incorporated. Also noted that literature
  priority for the iterative strengthening is not established.

### Exact commands and outcomes

```text
python3 tools/new_problem.py vizing-domination --title "Vizing’s domination conjecture"
# Created problems/vizing-domination/

cd problems/vizing-domination/harness
python3 -m unittest -v
# Ran 11 tests in 0.113s — OK
```

Additional adversarial scripts exhaustively checked the proposed inequalities
on all subsets of selected named graphs; one scratch enumeration over graphs
through five vertices found the displayed `k=3` counterexample. This finite
work is conjecture hygiene only.

Interactive wall time: approximately 50 minutes. External compute: none.

The self-contained `writeup/report.html` parsed successfully, contains no
external requests, and carries the `partial results` badge. Attempted visual
rendering in the in-app browser was blocked by its local-file URL policy; no
bypass was attempted, so live visual QA remains an environment limitation.

## 2026-07-24 — fibre equality and orthogonal attacks

### Parallel xhigh angles

Three GPT-5.6 Sol agents at xhigh effort attacked independent directions.

1. **Simultaneous fibre tightness:** proved the terminal conflict-graph
   theorem and accepted the exact product slack decomposition. It found no
   cross-column contradiction, so the verdict is PROVE the classification /
   PIVOT from treating one fibre defect in isolation.
2. **Packing hierarchy:** derived every additive even/odd `k`-packing subset
   and product inequality, proved the same formal minimax point saturates all
   of them, and found a five-vertex gadget saturating the packing and
   domination hierarchies at every integer level. Verdict: PIVOT.
3. **Alternative product decomposition:** constructed a two-sided fractional
   packing tensor bound with an exact local-concentration denominator.
   Independent xhigh review accepted it after explicitly excluding zero
   packings. Verdict: GO for graph classes; PIVOT for a universal constant
   until an integrality/concentration tradeoff is proved.

Two agents initially lost their response streams and were restarted with
narrower prompts; their final mathematical outputs were complete.

### Terminal conflict theorem

For two-sparse `S`, define `F_G(S)` on `S` by conflict of closed
neighborhoods. Proved

`γ_G(S)=|S|-ν(F)` and `ρ_G(S)=α(F)`.

Also proved

`α(F)+2ν(F)≥|V(F)|`,

with equality iff every component is a complete odd graph. Thus terminal
equality in Steiner's Lemma 2.3 requires a disjoint union of odd cliques and
zero ambient packing slack. The component defects give quantitative
stability. Exhaustive exact checking through five vertices found no
counterexample; the proof uses augmenting paths, not the enumeration.

### Exact fibre-slack identity

With the notation in `angles/fibre-slack/README.md`, proved

`E=v+3Σ_i(p_i+d_i)+Σ_iδ_i`,

where `E=4|D|-γ(H)(3γ(G)-ρ²(G))`. Every term is nonnegative. Equality forces
simultaneous row-wise cell equality, injective minimum column projections,
domination additivity across every `L_i`, and recursive odd-clique terminal
structure. The fibre xhigh reviewer checked the algebra and every equality
consequence and returned ACCEPT without correction.

### Full packing/domination hierarchy

For all `m`, proved

`3mγ_G(S)≤m|S|+ρ^{2m}(G)` and
`(3m+2)γ_G(S)≤(m+1)|S|+ρ^{2m+1}(G)`,

with exact defect decompositions and product corollaries. The formal Steiner
obstruction saturates every level. On the existing five-vertex gadget,

`ρ^{k}=⌊3k/2⌋` and `γ^{k}=⌈3k/2⌉`,

so the hierarchy is simultaneously tight in actual graphs away from the
irrational global ratios. This closes additive higher packing as a route to
an improved constant.

### Fractional tensor bridge

For nonzero fractional packings `p,q`, with totals `P,Q`, proved

`γ(G□H)≥γ_f(G□H)≥PQ/κ`,

where

`κ=max_{u,v}[q_vp(N_G[u])+p_uq(N_H[v])-p_uq_v]`.

For `r`- and `s`-regular factors this gives
`|V(G)||V(H)|/(r+s+1)`. The unique optimal fractional packing
`(1,0,0,1)` on `P4` refutes totals-only concentration caps.

### Verification and compute

```text
git switch -c problem/vizing-domination/2026-07-24-fibre-tightness
cd problems/vizing-domination/harness
python3 -m unittest -v
# Ran 16 tests — OK
```

The harness now checks conflict-graph formulas, exhausts the extremal
matching-cover classification through five vertices, verifies the all-level
packing/domination gadget, and checks the fractional tensor bound on regular
and concentrated examples. These are exact hygiene checks, not evidence for
the universal conjecture.

Final repository QA also ran `git diff --check`, parsed `STATUS.toml`, compiled
the harness, and parsed the self-contained HTML report while checking that its
badge exactly matches `status = "partial-results"` and that it contains no
external URLs. All checks passed.

Interactive wall time: approximately 45 minutes. External compute: none.

### Gate verdict

The two-session gate is met by a sharper nontrivial equality classification
and the exact fibre-slack theorem. No constant above 0.5643 was certified.
Further work should continue only on simultaneous row/column realizability
or the fractional integrality/concentration tradeoff; additive packing
reoptimization is a proved STOP.

## 2026-07-24 — capacity refinement and coordinate holes

### Publication and branch

The previous verified branch was published as
`origin/problem/vizing-domination/2026-07-24-fibre-tightness`. Moving remote
`main` was deliberately not attempted after the protected action rejected a
push that would also publish four unrelated local commits. Continued work on
`problem/vizing-domination/2026-07-24-incidence-concentration`.

### Parallel xhigh attacks

Three GPT-5.6 Sol agents at xhigh effort attacked:

1. simultaneous fibre equality and terminal packing structure;
2. fractional integrality/concentration tradeoffs;
3. an orthogonal square-graph LP formulation.

A fourth Sol/xhigh referee checked the fractional and square-cover packages.
It accepted every final theorem, caught an initially ambiguous `P4` packing
in the split-graph example, and verified the corrected uniform-packing bound.
The incidence agent separately caught and repaired an overstrong
unique-hole claim: singleton holes require an external private target;
self-private targets only give a covering inclusion.

### Capacity-two terminal theorem

For a terminal conflict graph `F`, introduced

```text
τ₂(F)=max Σw_x,
w_x∈{0,1,2}, w_x+w_y≤2 for every xy∈E(F).
```

Every feasible weighting lifts to a global integer 2-packing. A
Hall-deficiency construction proves

`τ₂(F)≥α(F)+|F|-ν(F)`.

This gives the exact three-defect decomposition

```text
δ_G(S)
 = [ρ²(G)-τ₂(F)]
 + [τ₂(F)-(α(F)+|F|-ν(F))]
 + [α(F)+2ν(F)-|F|].
```

On `K_{2m+1}`, the middle defect is zero only for `K₁,K₃` and is `m-1`
for `m≥2`. Thus full terminal equality consists exactly of `K₁/K₃`
components whose supported capacity-two weighting is globally optimal.

Using

`η(F)=τ₂(F)-2|F|+3ν(F)`

at terminal leaves yields a refined recursive parameter `p_G^△(S)` and the
new subset inequality

`3γ_G(S)≤|S|+ρ²(G)-p_G^△(S)`.

Disjoint unions of isolated vertices and `C5` gadgets with target
`{0,2,4}` realize arbitrary zero-defect mixtures, so subset-local counting
alone remains a STOP.

### Formal incidence balance

For a complete peeling of `L_i`, let `ℓ_i` be its length and `r_i` the
ordinary packing number of the terminal remainder. Proved

```text
4Σ_i[ℓ_i+(ρ(G)-r_i)]
 ≤ γ(H)(γ(G)+4ρ(G)-3ρ²(G))
   -v+Σ_i(p_i+d_i)+3Σ_iδ_i.
```

At the formal Steiner minimizer the parameter residual vanishes. Exact
tightness therefore forces every `L_i` to be terminal, to contain a maximum
ordinary packing and an optimal 2-packing, and to have fixed atom counts

```text
#K₁=3ρ-ρ²,   #K₃=ρ²-2ρ.
```

The complement dominator `X_i=P_G(D_i)` is anticomplete to `L_i`.
Occupied-cell and vertical-cell matrices have equal row and column margins,
so their difference decomposes into alternating cycles. Every row is a
disjoint minimum exchange of partition centers in `H`.

Coordinate-wise product domination adds the missing condition. For an
external private target, the row has exactly one coordinate of `π_i` not
dominated from outside the part, equal to the coordinate of its unique
horizontal dominator. A self-private target only forces a nonempty hole set
inside that coordinate's closed neighborhood. A checked `C4`/six-vertex
`H` skeleton realizes all margin and exchange data but leaves `(1,p1)`
undominated, proving that hole coverage is not optional.

### Fractional and square-graph boundaries

For every rank-one fractional tensor, proved the ceiling

`PQ/κ≤min{|H|γ_f(G),|G|γ_f(H)}`.

The unique optimal packing of `P4` makes `κ=1` against every optimal packing,
and a near-optimal analogue rules out fixed-tolerance concentration
tradeoffs. A connected split-graph family places all rank-one certificates
below Steiner for sufficiently large integrality gap. Conversely, a
deliberately diffuse packing on the hard-only `m=8,k=4` split graph gives
the exact class-specific bound `γ(G□P4)≥8`, factor `4/5`.

Independently, for `σ(G)=fcc(G²)`, proved

```text
γ(G□H)≥fcc((G□H)²)≥σ(G)σ(H),
γ(G□H)≥max{σ(G)γ(H),γ(G)σ(H)}.
```

Centered perfect squares satisfy `σ(G)=γ(G)`; this proves Vizing when one
factor is a forest. The connected family
`G_m=L(K_{2m+1}), H=P4` has product-square fractional clique cover at most
four versus domination product `2m`, so unrestricted square-clique and theta
relaxations have unbounded universal loss.

### Verification

```text
cd problems/vizing-domination/harness
python3 -m unittest -v
# Ran 20 tests — OK
```

New exact tests exhaust the capacity-two zero-defect classification through
five vertices, verify the refined peeling inequality on every subset of
named graphs, validate split-graph fractional packings, and check the
coordinate-hole adversarial skeleton. These remain conjecture hygiene.

Interactive wall time: approximately 90 minutes. External compute: none.

### Gate verdict

The session proves a rigorous stronger subset-domination inequality and a
nontrivial formal equality classification. No constant above 0.5643 is
claimed. Continue only on aggregate external-private-target counting,
higher-rank fractional tensors, or center-aware square lifts. Optimal
rank-one concentration and unrestricted square-clique cover are certified
PIVOT/STOP directions.

## 2026-07-24 — external-private holes and blocker hybrids

### Branch and mandate

Continued from synchronized `main` on
`problem/vizing-domination/2026-07-24-external-holes`. The session remained
inside `problems/vizing-domination/` plus the generated root board. The goal
was an order-free bridge from the formal `K₁/K₃` incidence classification,
with a parallel nonseparable LP attack.

### Parallel GPT-5.6 Sol xhigh reviews

Three Sol agents at xhigh effort worked independently:

1. the incidence agent proved the external-private replacement lemma and the
   row hole-packing theorem;
2. a hostile referee audited every replacement, saturation, retained-center,
   and quantitative step;
3. an orthogonal agent developed the bidirectional weighted-domination
   blocker lift and its exact obstructions.

The hostile referee accepted the exact external-private theorem. It corrected
the proof language from “preserves domination of the terminal set” to
“preserves domination of its complement,” and supplied an exhaustive
small-graph check: no counterexample among 217 exact-hypothesis instances
through five vertices. It rejected an initially proposed cardinal bound on
self-private vertices: an opposite minimum dominating pair in `C₄` need not
be a two-packing. The corrected statement controls only their two-packing
number.

The referee accepted the row hole theorem, emphasizing that the row set must
dominate every cell indexed by its vertical set. It also accepted the blocker
complement and diffuseness lemmas. It caught a factor-two attribution error:
the general estimate `PQ/(η_p+η_q)` gives `2C`, not `4C`, on the symmetric
hard-split packing. The stronger `4C` is the exact tensor value there because
its actual denominator is `1/C`; it does not follow from the general lemma.
The checked-in claims use the corrected distinction.

### External-private theorem

Let `L` be terminal with `K₁/K₃` conflict components, let its canonical
capacity weighting be a globally optimal integer 2-packing, and let `X`
minimally dominate `T=V(G)\L` with

`|X|+γ_G(L)=γ(G)`.

Proved that every `x∈X` has an external private target. If `x` were
self-private only, packing optimality would give a saturated
`w∈N[x]`. Saturation occurs inside one atom, so a minimum `L`-dominator can
be chosen to contain `w`. Replacing `x` by `w` preserves domination of `T`;
the overlap with the `L`-dominator saves one vertex and contradicts
`γ(G)`.

The five-vertex graph `K_{2,3}` proves additivity essential. With a singleton
terminal target in the three-side and the other two three-side vertices as
`X`, all packing/atomic/minimum conditions hold and both members are
self-private only, but the additive sum is three while `γ=2`.

If the ambient 2-packing exceeds the supported capacity by `Δ`, the
self-private set `S` satisfies only

`ρ_G(S)≤Δ`.

For every two-packing `P⊆S`, adding its indicator to the supported weights is
feasible. No cardinal bound is claimed.

### Row hole-packing theorem

For a fixed product row, write

```text
A=A_y,  I={i:y∈L_i},  e=|A|-|I|.
```

Let `J` be columns choosing `y` as an external private target and
`P={a_i:i∈J}` their singleton holes. Replacing the partition centers indexed
by `I∪J` with `A` and a minimum dominator of `P` proves

```text
|J|-γ_H(P)≤e,
|J|≤ρ(H)+2e.
```

At zero row slack, `P` is a two-packing. Summing gives

`M≤|V(G)|ρ(H)+2v`,

and full formal equality gives `|D|≤|V(G)|ρ(H)`, plus its transpose. At the
formal ratios this requires
`|V(G)|≥(c/a)γ(G)≈1.83822γ(G)`. This is stronger than the elementary
three-disjoint-set count but remains order-dependent, so no new universal
constant is claimed.

The perfect code `{(i,2i mod 5):i∈Z₅}` in `C₅□C₅` kills a symmetric-corner
shortcut: each codeword has external private neighbors in both coordinate
directions, but their rectangle corner is dominated by the next codeword.

### Bidirectional blocker lift

For weighted integral domination blocker

`τ_K(w)=min_{S dominates K}Σ_{x∈S}w_x`,

defined a nonseparable lift `Λ(G,H)` maximizing

`Σ_gτ_H(a_g)+Σ_hτ_G(b^h)`

subject to

`Σ_{g∈N_G[u]}a_{g,v}+Σ_{h∈N_H[v]}b_{u,h}≤1`.

Projection of any product dominator proves

`γ(G□H)≥Λ(G,H)`,

and summing over minimum factor dominators gives
`Λ(G,H)≤γ(G)γ(H)`. Unit column weights on the endpoints of `P₄` prove

`Λ(G,P₄)=2γ(G)`

for every `G`. Thus the lift reaches Vizing's target exactly on the family
that defeats pure fractional packing.

Automorphism averaging gives, for vertex-transitive factors of degrees
`r,s`,

`Λ=max{|G|γ(H)/(r+1),|H|γ(G)/(s+1)}`.

For two copies of `L(K_{2m+1})`, the normalized value tends to `1/2`, so
the standalone lift is a universal STOP.

### Saturation defect versus diffuseness

For an ordinary maximum two-packing in `G` and a fractional packing `q` on
`H`, with total `Q`, defined

`Δ_H(q)=min_{T dominates H}Σ_{v∈T}[1-q(N[v])]`

and proved the explicit blocker certificate

`Λ(G,H)≥Qγ(G)+ρ(G)Δ_H(q)`.

At the formal ratios, the canonical half-2-packing reaches Steiner exactly
at `Δ_H(q)=(1-b)γ(H)`. This threshold is not forced by packing ratios:
`C₅` and the augmented even split graphs `S_m` have canonical `Δ=0`, and
disjoint-union mixtures of `C₅,S₂₆,S₂₈` approach the irrational formal
point.

For fractional packings of totals `P,Q` and maximum coordinates
`η_p,η_q`, also proved

`γ_f(G□H)≥PQ/(η_p+η_q)`.

The zero-deficit split examples have highly diffuse alternative packings, so
they do not kill the hybrid. The remaining explicit GO target is a
defect–diffuseness dichotomy: either optimized blocker deficit beats its
threshold or diffuse fractional packings beat Steiner.

### Verification and compute

```text
cd problems/vizing-domination/harness
python3 -m unittest -v
# Ran 25 tests — OK
```

One repository-root `python3 -m unittest -v` invocation discovered zero tests;
it was not treated as verification. The displayed harness-scoped command was
then rerun and passed all 25 tests.

The five new exact tests cover the atomic external-private example, the
`K_{2,3}` additivity obstruction, the `C₅□C₅` corner cycle, the `P₄`
blocker target on named factors, zero `C₅` saturation deficit, and the
diffuse split tensor value. These are adversarial hygiene, not evidence for
the universal conjecture.

Interactive wall time: approximately 90 minutes. External compute: none.

### Gate verdict

The session adds a nontrivial exact equality classification, a quantitative
row subset-domination inequality, and a new nonseparable product lift. It
does not certify a constant above `0.5643`. **GO** only for order-free
cross-row hole coupling, self-private stability using the full atomic
geometry, or the explicit blocker defect–fractional diffuseness dichotomy.

## 2026-07-24 — anchored correction, escape dynamics, and zero-factor lifts

### Scope and independent reviews

Continued on branch
`problem/vizing-domination/2026-07-24-defect-diffuseness`. Three independent
GPT-5.6 Sol agents at xhigh effort attacked:

1. the optimized saturation-defect/capped-profile hybrid;
2. cross-row private-hole incidence and the full blocker; and
3. orthogonal product LPs and adversarial graph families.

Every proposed theorem below received an independent Sol audit. One initial
shared-cap counterfamily was explicitly rejected after independent caps at
`s=1/126,t=1/15` gave

`(-14641+1753√73)/564≈0.596877>c`.

It was replaced by the uniform all-caps counterfamily below. A separate
agent briefly used the wrong normalization for `ρ²`; that proposal was
withdrawn before entering the notes.

### Decisive correction to the blocker deficit

The session-four threshold interpretation was incomplete. For a fractional
packing `q`, total `Q`, and a dominating set `T`, define

`E_T(q)=Σ_xq_x(|T∩N[x]|-1)≥0`.

Double counting gives

`Σ_{t∈T}q(N[t])=Q+E_T(q)`.

Therefore exactly

```text
Δ_H(q)=γ(H)-Q-Ω_H(q),
Ω_H(q)=max_T[E_T(q)-(|T|-γ(H))]≥0.
```

In particular `Δ_H(q)≤γ(H)-Q`. The canonical half-2-packing at the formal
point can meet Steiner only at this absolute ceiling and can never beat it.
All prior forward-looking “deficit above the threshold” text was corrected.

### Optimized anchored value

Defined

`F_a(H)=max_q[Q+aΔ_H(q)]`.

An optimistic minimum-dominator version has the exact anchored fractional
domination dual

```text
min 1ᵀd
subject to Ad≥1 and d≥az
for some z in the convex hull of minimum dominators.
```

For the augmented uniform split graph `S_{2k,z}`,

```text
γ=k+z+1,  ρ=z+2,  ρ²=2z+4,
F_a=z+max{2,a(k+1)}.
```

Also `F_a(C₅)=5/3` and `F_a(L(K₇))=21/11`. Disjoint-union mixtures of
`C₅,S₂₆,₂,S₂₈,₂` approach the formal packing ratios and have

`F_a/γ→(1273-115√73)/576≈0.504235<c`.

The exact gap is `(139√73-1153)/576`, with square difference `81024`.

### Exact capped profiles and the independent-cap STOP

For

`Φ_H(t)=max{Σp:p fractional packing, p_v≤t}`,

proved the exact split profile. With
`M=binom(2k-1,k-1)` and `n=2M+2k+2z`,

```text
Φ_{S_{2k,z}}(t)=
  nt                         up to 1/(M+2k+z),
  1+(M+z)t                  up to 1/M,
  2+zt                       thereafter.
```

Thus its normalized profile is `(z/γ)t+e(t)` with the uniform bound
`0≤e(t)≤2/γ`.

The first counterfactor uses domination-mass share
`(√73-7)/6` of `C₅`, with the rest a fixed `S₂₆,₂/S₂₈,₂` mixture. The
second uses share `(√73-7)/4` of `L(K₇)` and a large
`S_{2k,z_k}` component. Both factors approach `(a,b)`. Their anchored
values are respectively approximately `0.504235` and `0.557719`, while the
independently capped tensor is uniformly at most

`(-247+37√73)/264≈0.261849<c`.

The exact split error and a bounded slope `g(s)≤Ks` make the finite
all-caps estimate uniform even as `s,t→0`.

A safe-port lemma connects all components by a tree while preserving
`γ,ρ,ρ²`. Edge addition only decreases `F_a` and `Φ`, so the full
three-arm counterfamily remains a STOP on connected factors.

### Cross-row packings and exact obstructions

If every row `y` carries a hole two-packing `P_y` in `H` and `p` is any
fractional packing on `G`, then

`W(y,a)=p_y1[a∈P_y]`

is a fractional packing on the product. Hence

`Σ_yp_y|P_y|≤γ_f(G□H)≤|D|`.

The common-crown construction keeps `γ` unchanged while putting every
external private target in one closed neighborhood, so this weighted mass
can lose an arbitrary factor. Under full formal balance, if
`Y⊆N_G[w]`, then

`M(Y)≤2γ(H)ρ(H)+sd`,

where `s` is the number of singleton terminal cells and `d=|L_i|`. The
coefficient is still vacuous at comparable formal scales.

### Private-corner escape dynamics

If a product point `d=(g,h)` has external private neighbors
`(x,h)` and `(g,y)` in both directions, every dominator of the corner
`(x,y)` is an exact `(1,2)` or `(2,1)` knight move from `d`. Choosing one
corner owner per point gives a loopless functional digraph and hence a
directed escape cycle.

At exact equality, a destination `(x,z)` has type-`(1,2)` indegree at most

`min{|J_x|,ρ_H(N₂(z)),deg_H(z)}≤ρ(H)`,

and symmetrically. Every arc also forces the labelled pattern

`i∈S_g∩J_x, j∈S_x, i∉I_x, j∉I_g`.

The `C₅□C₅` perfect code realizes a directed 5-cycle, and
`K₂□P₃` with `{(0,0),(1,2)}` realizes a directed 2-cycle. Existence,
bounded indegree, and cycle length alone are therefore insufficient.

### Combined lift and zero-factor Cayley obstruction

Defined a shared-capacity lift `Ξ` by adding a genuine product fractional
packing `W` to the two blocker arrays:

```text
W(N[(u,v)])
+Σ_{g∈N_G[u]}a_{g,v}
+Σ_{h∈N_H[v]}b_{u,h}≤1.
```

The product-dominator count proves `γ(G□H)≥Ξ(G,H)`. Its exact dual minimizes
the mass of a product fractional dominator that simultaneously routes, for
every factor vertex, probability marginals of integral dominators of the
opposite factor.

For vertex-transitive factors, with closed-neighborhood sizes `R_i` and
covering multiplicities `κ_i=γ_iR_i/n_i`, exact averaging gives

```text
Ξ/(γ_Gγ_H)=max{
  1/κ_G,
  1/κ_H,
  R_GR_H/[κ_Gκ_H(R_G+R_H-1)]
}.
```

Bollobás--Janson--Riordan, arXiv:0910.3815v2, Theorem 4.1 and Remark 4.2,
show that for `n=k^{1+o(1)}`, `n/k→∞`, almost every `k`-subset of any group
of order `n` has translate-cover multiplicity `Ω(log k)`. Specialize to
`(ℤ₂)^m`, choose `k≈2^m/log(2^m)`, and intersect with the asymptotically
certain affine-spanning event. After translation to include zero, the sets
give connected undirected Cayley graphs whose closed neighborhoods are the
translates and whose `κ` is unbounded.

Choose the second Cayley scale so that `log R_H≥R_G`. Then every displayed
term tends to zero. Thus

`inf Ξ(G,H)/(γ(G)γ(H))=0`

even for connected vertex-transitive factors. The same family sends the full
blocker `Λ` to zero. Two independent Sol reviewers accepted the
specialization; the literal `⌊k log k⌋` clause of Theorem 4.1 was not used,
only its proof and Remark 4.2 covering power-of-two group orders.

### Typed successor

For actual row label sets `A_g={h:(g,h)∈D}` and open-neighborhood imports
`V_g=⋃_{x∈N_G(g)}A_x`, product domination is exactly

`V(H)\V_g⊆N_H[A_g]`.

Hence every product dominator satisfies

`|A_g|≥γ_H(V(H)\V_g)`

in every row and the symmetric column inequalities. Minimizing over set
systems satisfying only these cardinality conditions defines a strict
labelled relaxation `Θ≤γ(G□H)`. Its universal value is uncalibrated; the
asymmetric Cayley pair is the first mandatory test.

An independent audit proved

```text
Θ≥max{γ^{γ(H)}(G),γ^{γ(G)}(H)},
Θ≥γ(G□H)/2≥(c/2)γ(G)γ(H).
```

For the second line, add in every row a minimum dominator of the genuinely
missed set

`M_g=(V(H)\V_g)\N_H[A_g]`.

Typed feasibility bounds the total repair cost by `Σ_g|A_g|`. For
`G=H=K₂⊔K₁`, four swapped-component labels satisfy both typed cardinality
systems but fail to dominate the product, whose domination number is five.
Thus the relaxation is strict. The next target is to improve the factor-two
repair using both row and column missed-set corrections.

### Verification and compute

```text
cd problems/vizing-domination/harness
python3 -m unittest -v
# Ran 30 tests — OK
```

New exact tests cover the anchored and independent-cap surd identities, the
common-crown product witness, the `C₄` combined-lift benchmark, and the
length-two private-corner escape cycle. The typed-fibre fixture separates
cardinality feasibility from actual domination. These are hygiene and
adversarial checks, not evidence for the conjecture.

Interactive wall time: approximately three hours. External compute: the Sol
reviewers reported one small-graph numerical falsification scan for `Ξ`;
it was used only to find `C₄□C₄` and is not treated as a theorem or campaign
progress.

### Gate verdict

No constant above `0.5643` was certified. The session nevertheless adds a
nontrivial labelled equality classification, an exact connected
formal-ratio counterfamily, and two rigorous zero-factor obstructions for
natural blocker/fractional lifts. **GO** only for the typed correlated fibre
sets and successive labelled escape transitions. All factor-marginal,
averaged-dominator, full-blocker, and combined-lift routes are STOPs.

## 2026-07-24 — typed profiles, fractional repair energy, and escape density

### Scope and independent reviews

Continued on branch
`problem/vizing-domination/2026-07-24-typed-two-axis`. Three GPT-5.6 Sol
agents at xhigh effort independently attacked:

1. two-axis charging and fractional packing on actual fibre labels;
2. the robust asymmetric and symmetric Cayley benchmarks; and
3. partial-cover defects and isolation-to-escape dynamics.

Every theorem below received an independent Sol audit. The robust Cayley
statement is explicitly a new adaptation of the Newman/Bollobás--Janson--
Riordan random-set argument, not a theorem stated verbatim in that paper.

### Exact partial-cover profile theorem

Defined

`u_K(t)=min_{|C|≤t}|V(K)\N_K[C]|`.

For every row-typed incidence set `A`, with row masses `a_g` and column
masses `b_h`, proved

`Σ_g u_H(a_g)+Σ_hu_G(b_h)≤|G||H|`.

The proof is the exact chain

```text
u_H(a_g)≤|V_g|,
Σ_g|V_g|=Σ_h|N_G^open(B_h)|
≤Σ_h(|G|-u_G(b_h)).
```

It has the defect identity

```text
|G||H|-Σ_gu_H(a_g)-Σ_hu_G(b_h)
=Σ_g(|V_g|-u_H(a_g))
 +Σ_h[|G|-u_G(b_h)-|N_G[B_h]|]
 +Σ_h|B_h\N_G^open(B_h)|.
```

Thus the exact final obstruction is fibre isolation, not an untracked scalar
loss. `C₅□C₅` realizes all five units of slack as isolated fibres.

For `d`-regular `G`, the profile gives

`Θ(G,H)≥|G|(t+1)u_H(t)/[u_H(t)+d(t+1)]`.

A weighted fractional-packing version was also proved.

### Robust Cayley calibration

Let `Q_m=F₂^m`, `n=2^m`, `k=floor(n/m²)`, `q=n/k`, and
`ℓ=log k`. A robust adaptation of Newman's hitting lemma, as recorded in
Bollobás--Janson--Riordan Remark 4.3, gives an affinely spanning `k`-set
containing zero whose Cayley graph has

```text
t*=floor(q(ℓ-10 log ℓ)),
L=floor(ℓ⁶),
u(t*)>L.
```

For fixed center set `T` and exceptional set `E`, the failure probability is
at most

`exp(-(n-L)(1-k/n)^t/t)`.

The negative exponent is asymptotic to `ℓ⁹`, while the two union-bound
entropy terms are `O(ℓ⁴)` and `O(ℓ⁷)`. Deleting to exactly `k` while
retaining an affine basis, then translating to contain zero, preserves the
profile and gives a connected undirected Cayley graph.

The greedy cover bound gives

`t*<γ≤q(ℓ+1)` and `t*/γ→1`.

The partial-cover theorem then proves

`Θ(G,H)/(γ(G)γ(H))→∞`

for every pair of growing members of this robust family, with arbitrary
relative scales. With one factor fixed the liminf is at least
`|G|/γ(G)≥1`. Thus the same family that drives `Ξ` to zero is decisively
harmless for `Θ`.

The global resilience `min_{t<γ}u(t)/(γ-t)` was not claimed large. The
argument leaves an `o(γ)` final window where a singleton private set could
collapse the minimum to one.

### Correlated fractional repair energy

For factor fractional packings `q,p`, totals `Q,P`, remaining target sets
`C_g=H\V_g`, `D_h=G\U_h`, defined

```text
Z=Σ_{(g,h)∈A}(1-q_g)(1-p_h),
E_H=Σ_gq_g[γ_H(C_g)-p(C_g)],
E_G=Σ_hp_h[γ_G(D_h)-q(D_h)].
```

Proved the exact inequality

`|A|≥PQ+Z+max{E_H,E_G}`.

The row slack identity is

```text
Σ_A(q_g+p_h-q_gp_h)-PQ
=Σ_gq_g[|A_g|-p(C_g)+o_g]
 +Σ_xp(A_x)[1-q(N_G[x])],
```

where `o_g` is imported weighted overlap. The symmetric identity gives
`E_G`. The maximum is sharp on `K₂□K₂` and `P₃□P₃`; the two energies
cannot be added.

For a minimum dominator `T` of `C`,

```text
γ(C)-p(C)
=Σ_{t∈T}[1-p(C∩N[t])]
 +Σ_{v∈C}p_v(|T∩N[v]|-1).
```

Hence zero energy is exactly packing saturation plus exact-one coverage. For
half of an integral 2-packing, every nonzero gap costs at least one half.

The cap-only denominator is `s+t-st`, correcting the earlier weaker
`s+t` envelope. Since `s+t-st≥(s+t)/2`, the existing formal-ratio
counterfamily still bounds the exact cap certificate by

`(-247+37√73)/132≈0.523698<c`.

### Terminal triangle provider lemma and STOP

For a terminal `K₁/K₃` equality set in `H`, use the canonical packing
with weight one on singleton targets and one half on triangle targets. If
there are `τ` triangle atoms, then

`Z+E_H≥τQ/2`.

An odd intersection of a remaining target set with a triangle costs one
half in `E_H`. An even intersection forces an odd nonempty imported set;
fractional packing capacity charges its provider to `Z`.

At the formal ratios this gives only

```text
b²+b(b-a)
=b(2b-a)
=(10-√73)/9
≈0.16178,
```

leaving the exact gap `(11√73-65)/72` to Steiner. Row and column charges
cannot be added. This is a rigorous STOP for local atom parity alone. The
missing theorem must prevent provider reuse across the fibre-indexed
triangle systems or exclude the large zero-packing-support mass.

### Isolation-to-escape density

For a product dominator, let `I_G` be the selected points isolated in their
fixed-label `G`-fibres, put

```text
r_{x,h}=|N_G(x)∩B_h|,
Ω_G=Σ_{x,h}(r_{x,h}-1)_+,
X_H=Σ_x|V_x∩N_H[A_x]|.
```

If `Bad_G⊆I_G` has no horizontal external-private neighbor, proved

`|Bad_G|≤2Ω_G+X_H`.

A chosen horizontal target either has multiple same-label owners, charged
with multiplicity at most `2(r-1)`, or its other dominator lies in the
arrival row and charges `X_H`.

Symmetrically, when both factors have no isolates, the number `T` of
fibre-isolated points with external private neighbors in both directions
satisfies

```text
|T|≥[
 I_G+I_H-|D|
 -2Ω_G-2Ω_H-X_H-X_G
]_+.
```

Every point of `T` carries a labelled `(1,2)` or `(2,1)` corner escape
obligation. The bound is exact on the `C₅□C₅` 5-cycle and the
`K₂□P₃` 2-cycle. Escape owners may still leave `T`, so a closure or
path-length lemma is required.

### Verification and compute

```text
cd problems/vizing-domination/harness
python3 -m unittest -v
# Ran 35 tests — OK
```

The new exact hygiene code computes `Θ` and near-cover profiles on small
graphs. Exhaustive fixtures verify the two-axis profile inequality, its
isolation defect identity, the correlated fractional charging identity,
the sharp isolation-to-escape count, small typed values, and the corrected
cap and triangle-provider surd gaps. These are falsification and algebra
checks, not evidence for the universal conjecture.

Interactive wall time: approximately two hours. External compute: none.

### Gate verdict

No constant above `0.5643` was certified. The session nevertheless proves
three new product-specific inequalities, a quantitative equality
classification, and a robust graph-family theorem that clears the mandatory
Cayley obstruction at all scales. **GO** only for a provider non-reuse lemma
across terminal systems or an escape closure/path-length theorem. Scalar
near-cover optimization, cap correction alone, global resilience alone, and
local triangle parity are STOPs.

## 2026-07-24 — session 7: exact overlap ledger and closure no-go theorems

### Scope and source discipline

The campaign stayed inside `problems/vizing-domination/`. The current
universal benchmark remains Steiner's

`c=(5+√73)/24≈0.5643`.

The withdrawn `0.5809` claim was not used. This session did not numerically
reoptimize Steiner's six inequalities and did not treat finite graph checks
as evidence for the conjecture.

### Corrected typed fractional charging

The session-six inequality had discarded two nonnegative cardinality slacks.
For typed-feasible `A⊆V(G)×V(H)`, factor fractional packings `q,p`, and the
session-six notation, define

```text
α_H=Σ_gq_g(|A_g|-γ_H(C_g)),
α_G=Σ_hp_h(|B_h|-γ_G(D_h)).
```

The correct directional consequence is

```text
|A|≥PQ+Z+max{E_H+α_H,E_G+α_G}.                              (1)
```

This is strictly stronger than the earlier recorded form. On `P₃□P₃`,

```text
A={(0,1),(2,0),(2,2)},       q=p=(0,0,1),
```

one has `PQ=1`, `Z=1`, `E_H=E_G=0`, `α_H=1`, and `α_G=0`.
Equation (1) is sharp at `|A|=3`; the earlier form gave only two.

### Four-region overlap and multiplicity identities

Let `C` be the cells with no horizontal open import, `D₀` those with no
vertical open import,

```text
I=A∩C∩D₀,       W=(C∩D₀)\A,
J=(G□H)\(C∪D₀),
K=w(A\I)+w(J),
```

where `w=q⊗p`. Direct inclusion-exclusion gives the exact identity

```text
|A|=PQ+Z+E_H+E_G+α_H+α_G-K+w(W).                            (2)
```

For an actual product dominator `W=∅`. Thus selected nonisolation and
double-open imports are precisely the overlap tax preventing the two
directional repair ledgers from being added.

There is a second exact decomposition. If `m(z)` counts all selected owners
of `z`, while `t(z)` retains only self-selection and the existence of an
owner in each coordinate direction, put

```text
R=Σ_z w(z)(m(z)-t(z)),
Δ=Σ_{(g,h)∈A}{
    p_h[1-q(N_G[g])]
   +q_g[1-p(N_H[h])]
  }.
```

Then

```text
2(|A|-PQ-Z)=E_H+E_G+α_H+α_G+R+Δ,                            (3)
```

and the two one-axis residuals are nonnegative and sum to `R+Δ`.
Consequently the averaged consequence of (3) is no stronger than (1).
For an actual dominator,

```text
E_H+E_G+α_H+α_G=2K+R+Δ.                                    (4)
```

The minimum antidiagonal dominator of `K₂□K₂` and a minimum dominator of
`P₃□P₃` both have `K=min(E_H,E_G)` with zero cardinality slack. They rule
out any universal strict scalar overlap estimate under minimum domination
and optimal factor duals alone.

Two independent GPT-5.6 Sol xhigh audits accepted (1)--(4), including the
restored `α` terms and the sharp examples.

### Generic escape closure is impossible

If an actual product dominator has

```text
I_G=I_H=D,       Ω_G=Ω_H=X_G=X_H=0,
```

then it is a perfect dominating code. Its mixed escape relation is
undirected.

More strongly, every finite bipartite graph `F` without isolated vertices
is realized as such an escape graph. If `F` has parts `S,T`, let `H` be its
one-subdivision, take `G=K₂`, and put

```text
D={(0,s):s∈S}∪{(1,t):t∈T}.
```

Every product vertex has exactly one owner and the mixed escape graph on
`D` is exactly `F`. Subdivided stars make the cyclic fraction
`2/(k+1)→0` while

```text
|D|-γ(K₂)γ(H)=1,       |T|=k+1.
```

Paths give arbitrarily long zero-defect in-trees. Hence no positive cycle
density, bounded return time, injective escape matching, or
`ε|T|` additive credit follows from the generic escape quantities, even at
zero defect. A GPT-5.6 Sol xhigh audit accepted the classification and
realization theorem.

### The formal factor-invariant point is actually realizable

For every fixed `L`, a random graph `K∼G(n,1/2)` has, with probability
tending to one,

```text
γ(K)>L,       ρ(K)=1,       ρ^{\{2\}}(K)=2.
```

The union-bound failure probability is at most

```text
C(n,2)(3/4)^(n-2)
+C(n,3)(7/8)^(n-3)
+Σ_{k=1}^L C(n,k)(1-2^-k)^(n-k)
=o(1).
```

The pair and triple common-closed-neighborhood properties force
`ρ=1,ρ²=2`; the last sum excludes dominators of size at most `L`.
This disproves the tempting relation

`γ≤2(ρ²-ρ)`

by an unbounded factor.

Writing

```text
a=(11-√73)/8,       b=(13-√73)/12,
c=(5+√73)/24,
t=(47-5√73)/24,     s=(√73-7)/6,
```

gives

```text
c+t+s=1,       t+s/2=a,       t+3s/4=b.
```

Disjoint mixtures whose domination mass is split in proportions `c,t,s`
among the dense graphs above, isolated vertices, and `C₅` copies have

```text
ρ/γ→a,       ρ²/(2γ)→b.
```

Thus Steiner's formal optimizer lies in the closure of invariant pairs of
actual finite graphs. Any continuous or closed homogeneous relation using
only `γ,ρ,ρ²` cannot exclude it. This is a disconnected, nonconstructive
calibration and says nothing about product near-extremizers. Two independent
GPT-5.6 Sol xhigh audits accepted the probabilistic proof and exact surd
mixture.

### Provider Hall deficiency and unbounded reuse

For indexed demands in a row, the provider graph `P_g` has left side the
indices and right side the selected row labels. Reuse is exactly its Hall
deficiency:

```text
|I|-ν(P_g)=max_{J⊆I}(|J|-|N(J)|).                           (5)
```

The incoming external-private holes indexed by `J_g` form a two-packing at
zero row slack, but the terminal providers are indexed by the outgoing
cells `I_g`. No proved coordinate-preserving map connects the two systems.

An explicit family makes the mismatch sharp. For each `m`, construct
`H_m` from blue cells `{c_i,s_i,t_i}`, red cells `{r_i,a_i,w_i}`, and

```text
c_i s_i, c_i t_i, r_i a_i, r_i w_i, a_i t_i,
a_0 c_i, a_0 s_i.
```

Pairwise disjoint closed neighborhoods `N[t_i]` and `N[w_i]` prove
`γ(H_m)=2m`. In `G=C₅`, with `T={0,2,4}` and `X={1,3}`, the set

```text
D_m=(T×{a_i:0≤i<m})∪(X×{c_i,w_i:0≤i<m})
```

dominates `C₅□H_m`. Every blue fibre is an exact terminal `K₃`, with the
canonical unit weighting on `T` an optimal global 2-packing, and every
provider row performs a minimum exchange. Nevertheless `(g,a_0)` is the
unique provider for all `m` demands `s_i`, so the Hall deficiency is
`m-1`.

The per-index overlap tax is zero on the natural rank-one weights. The
construction has linear exact Steiner defects rather than full equality:

```text
v+3Σ_i(p_i+d_i)+Σ_iδ_i=22m.
```

Thus indexed atoms alone are a STOP; only a stability theorem charging Hall
deficiency to the complete defect budget survives.

The constant arithmetic is severe. Even disjoint row and column triangle
credits give only

```text
b²+2b(b-a)=(13-√73)/24≈0.18567<c.
```

Starting from `b²`, more than

```text
(c-b²)/(b(b-a))
=(249+21√73)/24
≈17.851
```

independently additive triangle charges are needed. At least eighteen
effective copies would be required merely to cross Steiner. A GPT-5.6 Sol
xhigh audit accepted the construction, Hall calculation, defect identity,
and surd threshold.

### Adaptive provider matching and labelled cycles

The fixed-demand obstruction does not kill adaptive provider choice. For a
row `g`, let

```text
I_g={i:g∈L_i},
A_g=P_H(D∩({g}×H)).
```

Build a bipartite graph by joining `i∈I_g` to `a∈A_g\π_i` when
`N_H[a]∩π_i≠∅`. The exact row-exchange fact

`γ_H(⋃_{i∈I_g}π_i)=|I_g|`

implies Hall's condition: if `J⊆I_g` had fewer than `|J|` neighboring
providers, those neighbors together with the retained centers for
`I_g\J` would dominate the union with fewer than `|I_g|` vertices.
Therefore every row has an injection

```text
μ_g:I_g→A_g,
μ_g(i)∉π_i,
N_H[μ_g(i)]∩π_i≠∅.                                         (6)
```

The witness point in `π_i` is chosen after the matching. Globally, (6)
injects all blue incidences `(g,i)`, `g∈L_i`, into `D`, leaving exactly

`v=|D|-Σ_i|L_i|`

selected points unmatched.

If `v=0` and `|D_i|=|L_i|` in every column, each match gives a loopless
cell transition `i→j`, where `μ_g(i)∈π_j`; the cell digraph is Eulerian
and decomposes into directed cycles carrying actual domination labels.

Under the full atomic/additive external-private hypotheses, the matched
selected points transfer injectively to singleton hole occurrences. With
`e_x=|A_x|-|I_x|`, every row set `U⊆V(G)` satisfies the local cut

```text
Σ_{g∈U}|I_g|
≤ρ(H)|N_G(U)|+2Σ_{x∈N_G(U)}e_x.                             (7)
```

The same charge has a weighted form with
`max_{g∈N_G(x)}λ_g`. The `C₅□H_m` family passes the stress test: the
adaptive matching uses `a_i` to cover `t_i`, while the pre-prescribed
`s_i` demands still all require `a₀`; its `4m` unmatched selected points
are exactly `v`.

The triangle-only consequence of (7) is weaker than the previously known
all-incidence bound, so this does not improve `c`. It precisely narrows the
remaining bridge to compatibility between the adaptive Hall witnesses and
the pre-prescribed triangle-energy witnesses. A GPT-5.6 Sol xhigh audit
accepted the Hall proof, cycle decomposition, private-hole transfer, local
cut, and the limitation.

### Verification and compute

```text
cd problems/vizing-domination/harness
python3 -m unittest -v
# Ran 38 tests — OK
```

New exact fixtures check the four-region and multiplicity identities,
restored cardinality slack, zero-defect escape realization, the indexed
provider obstruction, and its adaptive matching on `C₅□H_m`. The
random-graph argument is deductive via explicit union bounds; no stochastic
experiment is used as evidence.

Interactive wall time: approximately three hours across the session.
External compute: none.

### Two-session gate verdict

No constant above `0.5643` was certified. The session did prove a nontrivial
zero-defect classification and universal realization theorem, an exact
two-direction equality/stability ledger, a universal adaptive-provider Hall
theorem with labelled cycle and local-cut consequences, and two rigorous
obstruction families. The gate is met by structural results, but the generic
escape and factor-invariant branches are now closed.

**GO** only for compatibility between adaptive providers and prescribed
triangle witnesses, a defect-weighted version of that compatibility, or an
equally strong product-correlated invariant. **STOP/PIVOT** for numerical
reoptimization, factor invariants, generic escape dynamics, local triangle
parity, or fixed-demand provider atoms without the complete defect budget.

## 2026-07-24 — Session 8: componentwise primitives and coordinate tax

### Hygiene correction

The previous adaptive-provider note had accidentally identified Steiner's
vertical set with `V(G)\N[X_i]` before imposing equality. This is false in
general. The correct definition is:

```text
g∈L_i  iff  A_g\π_i dominates π_i vertically in row g.
```

Universally, `X_i=P_G(D_i)` only dominates `V(G)\L_i`. The set equality
`N[X_i]=V(G)\L_i` follows later from zero projection/additivity defect and
column separation. The Hall proof itself is unaffected because it uses the
correct vertical statement `A_g\π_i` dominates `π_i`. The angle note was
repaired before building on it.

### Parallel proof attacks and independent audits

Three GPT-5.6 Sol agents at xhigh effort attacked:

1. triangle/adaptive-provider compatibility and adversarial small graphs;
2. weighted local cuts and equality-packaging consequences; and
3. the soundness of the combined component/primitive/coordinate argument.

The final referee accepted the componentwise theorem and zero-defect
coordinate obstruction after requiring all projection and support counts to
be restricted explicitly to a connected component. It rejected any stronger
claim that Hall-credit conservation alone forbids a new cross-atom energy
inequality. That limitation is recorded below.

### Componentwise calibration

Under the full equality conditions
`v=p_i=d_i=δ_i=B_i=0`, packing, domination, and projection equality all
localize to every connected component `C`. With

```text
Γ_C=γ(C),       r_C=ρ(C),       R_C=ρ^{\{2\}}(C),
```

every `L_i∩C` has fixed singleton/triangle counts

```text
z_C=3r_C-R_C,       τ_C=R_C-2r_C,
|L_i∩C|=2R_C-3r_C,  γ_C(L_i∩C)=R_C-r_C.
```

Also

`|D_i∩(C×π_i)|=|X_i∩C|=Γ_C-R_C+r_C`.

Summing the pointwise equality
`#{i:g∈L_i}=#{i:g∈X_i}` only over `g∈C` gives

```text
3R_C=Γ_C+4r_C,
Γ_C=2z_C+5τ_C.                                             (8.1)
```

Thus the full obstruction decomposes componentwise into singleton
`(2,1,2)` and triangle `(5,1,3)` primitives. The old dense/isolated/`C₅`
factor calibration does not satisfy this stronger product-equality
condition componentwise.

### Exact connected triangle primitive

A symmetric probabilistic construction realizes the missing triangle
primitive. Take anticomplete triples `L,X`. For each pair from `L` and pair
from `X`, add `N` vertices adjacent to those four core vertices. For every
`(ℓ_p,x_q)`, add `N` vertices adjacent to that pair. Put independent
probability-`1/2` edges among all `18N` auxiliary vertices `Z`.

With positive probability:

1. every triple except `L,X` lies in one closed neighborhood; and
2. every at-most-four-set not containing all of `L` or `X` misses an
   auxiliary vertex.

The fixed-event failure probabilities are at most `(7/8)^{N-3}` and
`(15/16)^{N-4}`. At `N=1000`, the union bounds are respectively below
`1.5·10^-46` and `5.4·10^-13`. Therefore a finite connected graph exists
with

```text
(γ,ρ,ρ²)=(5,1,3),
γ(L)=γ(X)=2,
γ(V\L)=γ(V\X)=γ(Z)=3,
```

and `L,X` as its only feasible unit triples. Both orientations have zero
additivity and projection-size defect. This proves that the factor-level
triangle primitive is real rather than a numerical fiction.

### Support-avoidance coordinate tax

Let `U` lie in a component `C` and avoid every vertical fibre `L_i`. Let
`R_U` be its occupied rows and

`v_C=Σ_{g∈C}(|A_g|-|I_g|)`.

For each coordinate `h∈π_i`, the same-coordinate horizontal support in
`D_i∩(C×π_i)` dominates `U\R_U`. Hence

```text
|D_i∩(C×π_i)|
≥|π_i|(γ_C(U)-|R_U|)
≥|π_i|(γ_C(U)-v_C).                                       (8.2)
```

This is a new product-label inequality. At `v=0`, the primitive's common
core `Z` is avoided by every allowable terminal triple, so (8.2) gives

`3|π_i|≤|D_i∩(C×π_i)|=3`.

All partition cells would be singleton, forcing
`|V(H)|=γ(H)` and hence `H` edgeless, contradicting the nonempty vertical
fibres. Therefore no full-zero-defect Steiner product can contain this
primitive component.

For `z` copies of `C₄` and `τ` primitive copies, every cell of size at least
two pays

`p_i≥3τ-z`.

At the formal ratios,

```text
(3τ-z)/Γ=8b-9a=(11√73-89)/24>0.                            (8.3)
```

Thus the exact componentwise-calibrated mixture is also incompatible with
zero product defect.

### Dependency stability, atom conservation, and no-gos

If `X` dominates `T=V\L`, define

`C_X(S)={v∈T:∅≠N[v]∩X⊆S}`.

Replacing `S` by a minimum dominator of its complete dependency region gives
the exact inequality

```text
|S|-γ(C_X(S))
≤(|X|-γ(T))+(γ(T)+γ(L)-γ(G)).                              (8.4)
```

For a Steiner column, the right side is at most `p_i+d_i`. Common-crown
examples show that (8.4) does not control one arbitrarily chosen private
target per owner.

Adaptive atom credits are exactly conservative: a singleton contributes
one base unit and a triangle contributes three, totaling `|D|-v`. At
`v=0`, every selected point is saturated once. The triangle repair energy
is locally real, but charging its distinguished selected point as one more
unit is a literal double charge. This only kills that proof method; it does
not rule out a genuinely structural cross-atom inequality.

An exact eleven-vertex graph supplies two reciprocal balanced row exchanges
whose adaptive targets in one exchange cannot be chosen as a two-packing.
Thus Hall matching, minimal partition cells, and Eulerian cell cycles still
do not imply target compatibility.

Finally, equality averaging gives a maximum fractional packing capped by
`1/2`, but its best cap-only tensor is

`(4/3)b²=(121-13√73)/54≈0.18385<c`.

Blowing one vertex of `C₄` into an arbitrarily large true-twin clique
preserves the singleton equality skeleton while making every nonnegative
row-weighted local cut arbitrarily slack. Scalar weighted expansion is a
STOP.

The support-avoidance lemma itself has a sharp near-equality loss. With
`x_{i,C}=Γ_C-γ_C(L_i)`,

```text
Σ_i(p_{i,C}+d_{i,C})
≥[|V(H)|(γ_C(U)-v_C)-Σ_i x_{i,C}]_+.
```

Integer optimization inside the exact Steiner slack gives only

```text
E≥ceil([γ_C(U)-(Σ_i x_{i,C})/|V(H)|]_+).
```

For the calibrated mixture this is `ceil((3τ-z)/2)`, yielding normalized
gain `(11√73-89)/(192γ(H))`. It vanishes as `γ(H)→∞`: one occupied core row
costs one vertical-slack unit but can be reused in every cell. Therefore
common support avoidance alone is a universal-constant STOP. A successful
lemma must charge the coordinate holes left by that occupied row in
linearly many cells.

An adversarial support-coverage design sharpened the alternative. Take
paired independent triples `B_p,B_{p*}` and, between nonpartner blocks,
join unequal coordinate labels. The blocks cover all vertices, every `B_p`
is a feasible terminal triangle, its partner is a separated complement
dominator, and `ρ=1,R=3`. However three vertices with distinct labels from
distinct partner pairs dominate the graph, so `γ=3`, not five. Sparse
matching variants retain domination size but lose the conflict/packing
hypotheses. This exactly kills the natural symmetric block-design route to
a covering primitive, but is not a proof that all covering primitives are
impossible.

### Verification and compute

```text
cd problems/vizing-domination/harness
python3 -m unittest test_hygiene.py
# Ran 41 tests — OK
```

New fixtures exhaust (8.4) on named small graphs, verify the eleven-vertex
balanced target-packing obstruction and the covering block design, and check
the cap-half and triangle-mixture surd identities exactly. The primitive is
proved by union bounds; random sampling is not used as evidence.

Interactive wall time: approximately two hours across the main and three
parallel Sol attacks. External compute: none.

### Gate verdict

No constant above `0.5643` is certified, and Vizing's conjecture remains
open. The session nevertheless passes the continuation gate with a new
componentwise equality classification and the first exact
Cartesian-coordinate obstruction to a realized triangle equality primitive.

**GO** for a product-scale support/coordinate dichotomy: every `(5,1,3)`
component must force hard coordinate holes in linearly many cells or pay a
uniform product-scale packing/additivity/projection defect.

**STOP/PIVOT** for scalar weighted cuts, cap-only tensors, or adding the
local triangle energy by charging an already Hall-saturated selected point.
Common support avoidance without a per-cell charge is also a constant-scale
STOP.

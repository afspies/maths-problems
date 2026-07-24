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

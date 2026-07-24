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

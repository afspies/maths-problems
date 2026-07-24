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

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

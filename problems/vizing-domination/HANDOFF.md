# Handoff — Vizing’s domination conjecture

Read these session-three notes first:

- `angles/terminal-capacity/README.md`
- `angles/incidence-balance/README.md`
- `angles/fractional-rank-one-limits/README.md`
- `angles/square-clique-cover/README.md`

## What is now proved

1. The terminal conflict capacity `τ₂(F)` gives a three-defect decomposition
   and sharpens full equality to unions of `K₁` and `K₃`. Propagating its
   defect through peeling gives the rigorous stronger parameter
   `p_G^△(S)`.
2. At the formal Steiner obstruction, every tight `L_i` is already terminal,
   contains maximum ordinary and optimal 2-packings, and has fixed atom counts

   `#K₁=3ρ-ρ²`, `#K₃=ρ²-2ρ`.

   Its complement dominator is anticomplete to `L_i`. Occupied and vertical
   cell matrices have equal margins and every row is a disjoint minimum
   exchange in `H`.
3. Product domination adds coordinate-hole constraints. External private
   targets force a singleton hole; self-private targets only force a
   nonempty hole set covered by the inside-cell point. A `C4` skeleton proves
   margins and row exchanges alone are insufficient.
4. Optimal rank-one fractional concentration is a STOP: `P4` forces `κ=1`,
   and a connected split-graph family puts all rank-one certificates below
   Steiner. Diffuse suboptimal packings remain useful for graph classes.
5. `σ(G)=fcc(G²)` gives

   `γ(G□H)≥max{σ(G)γ(H),γ(G)σ(H)}`.

   Centered perfect squares, including forests, satisfy `σ=γ`. Triangular
   graphs prove unrestricted square-clique/theta relaxations have unbounded
   universal loss.

## Next-session choices

### A. External-private counting

For each tight minimum complement dominator `X_i`, count members with only a
self-private target. Seek a lower bound on external private targets, or prove
that too many self-private members force an exchange reducing `X_i`. Then
couple the singleton coordinate holes of external targets across one
alternating red-blue incidence cycle.

### B. Higher-rank fractional tensor

Replace the separable weights `p_uq_v` by a sum of rank-one tensors or a
transport plan with prescribed marginals. It must beat the exact split-graph
`×P4` obstruction, not merely optimize `κ` for one rank-one term.

### C. Center-aware square lift

Strengthen `fcc(G²)` by retaining a penalty or label for cliques not contained
in a single closed neighborhood. The lift must recover the centered-perfect
theorem while resisting the fibres of `L(K_{2m+1})□P4`.

## Hard stops

- Do not numerically reoptimize Steiner's existing inequalities.
- Do not add more levels to the additive integer packing hierarchy.
- Do not seek a universal optimal/near-optimal rank-one concentration bound.
- Do not use unrestricted square-clique cover or theta as a universal route.
- Do not assume a private target is external; the self-private case is
  genuinely weaker.
- Do not treat finite graph enumeration as progress; use it only to falsify
  bridge lemmas.

Any proposed proof requires an independent GPT-5.6 Sol xhigh review.

# Handoff — Vizing’s domination conjecture

Read the four session-two angle notes first:

- `angles/fibre-slack/README.md`
- `angles/terminal-conflict/README.md`
- `angles/packing-hierarchy/README.md`
- `angles/fractional-tensor/README.md`

## What is now proved

1. Two-sparse subset domination is exactly a matching-cover parameter of the
   closed-neighborhood conflict graph. Equality in Steiner's matching bound
   occurs exactly for disjoint unions of odd cliques.
2. Steiner's oriented product slack has the exact decomposition

   `E=v+3Σ_i(p_i+d_i)+Σ_iδ_i`.

   Equality forces simultaneous row-wise cell equality, injective minimum
   column projections, partition additivity, and recursively tight
   odd-clique terminal remainders.
3. The full additive integer packing/domination hierarchy preserves the
   0.5643 obstruction at every level. Do not continue this route.
4. Nonzero fractional packings `p,q` give the orthogonal tensor bound

   `γ(G□H)≥PQ/κ`,

   with the exact local-concentration denominator defined in
   `angles/fractional-tensor/README.md`.

## Next-session choices

### A. Row/column incidence

Assume all defects in the fibre identity are small. Use the fact that for
every row `g`, `P_H(D_g)` plus the nonvertical partition centers is a
minimum `H`-dominating set, while every column projection is injective and
minimum. Try to prove these conditions incompatible with all terminal
conflict graphs being odd-clique unions near the Steiner ratios.

### B. Fractional concentration

Define the least `κ` among optimal or `(1-ε)`-optimal fractional packings.
Seek a theorem trading `γ/γ_f` against this concentration. `P4` blocks any
claim based only on connectedness or total packing mass.

## Hard stops

- Do not numerically reoptimize Steiner's existing inequalities.
- Do not add more levels to the additive integer packing hierarchy.
- Do not treat finite graph enumeration as progress; use it only to falsify
  bridge lemmas.

Any proposed proof requires an independent GPT-5.6 Sol xhigh review.


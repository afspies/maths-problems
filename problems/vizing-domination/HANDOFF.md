# Handoff — Vizing’s domination conjecture

Continue the proof-first attack. Read `PROBLEM.md`,
`literature/steiner-reconstruction.md`,
`angles/subset-slack/README.md`, and `angles/k3-analogue/README.md` first.

The first session produced two rigorous session-derived subset inequalities:

1. `3γ_G(S)≤|S|+ρ²(G)-p_G(S)`, with an exact equality/stability
   decomposition and an additive `(Σ_i p_G(L_i))/4` term in Steiner's product
   proof.
2. `5γ_G(S)≤2|S|+ρ³(G)`, yielding
   `γ(G□H)≥((5γ(G)-ρ³(G))/7)γ(H)`.

Neither raises the global constant by reoptimization: the old exact relaxed
minimizer extends to the `ρ³` parameter and saturates the new product bound.

## Next-session target

Prove or refute a structural obstruction to simultaneous tightness of the
vertically dominated fibre sets `L_i`. In priority order:

1. Can all `L_i` have `p_G(L_i)=0` for a minimum product dominator at the
   relaxed worst parameter point?
2. If yes, can all their complete peeling sequences terminate with both
   matching/packing bounds tight?
3. Can equality `ρ³=ρ²+ρ` coexist with those terminal equalities near the
   Steiner thresholds?

Use exact small graphs only to falsify bridge lemmas and extract witnesses.
Any proposed proof must receive a GPT-5.6 Sol xhigh adversarial review.

## Gate

This is session two of the stated two-session gate. Continue beyond it only
if the work yields a further rigorous subset-domination inequality, a sharper
nontrivial equality classification, or a certified universal constant above
0.5643. Otherwise record the obstruction and STOP/PIVOT to a different
product decomposition.


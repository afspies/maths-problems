# Peeling defect in Steiner's subset-domination lemma

**Status:** partial result; Vizing's conjecture remains open.

## Abstract

We independently reconstruct Steiner's universal
`(5+√73)/24≈0.5643` bound and its exact four-parameter optimization, and
audit the withdrawn 0.5809 claim. The latter replaces the valid
Chen–Piotrowski–Shreve expression `AB-xy` by the unequal expression
`3AB-2Ay-2xB+xy`. Our new result is an exact slack decomposition for
Steiner's key subset-domination lemma and a strict strengthening by an
excess-peeling parameter. It yields an instance-sensitive additive
improvement in Steiner's product bound, but no improved universal constant:
the remaining question is whether product fibre geometry forces positive
aggregate peeling defect.

## Definitions

Let `γ_G(S)` denote the minimum size of a vertex set of `G` dominating
`S⊆V(G)`. Let `ρ^{\{2\}}(G)` be the maximum total weight of a nonnegative
integer function `f` satisfying `f(N[v])≤2` for every vertex. Put

`δ_G(S)=|S|+ρ^{\{2\}}(G)-3γ_G(S)`.

Steiner's Lemma 2.3 says `δ_G(S)≥0`.

## Exact slack theorem

Suppose `q=|N[v]∩S|≥3`, let `S'=S\N[v]`, and put

`e=γ_G(S')+1-γ_G(S)`.

Then `e≥0` and

`δ_G(S)=δ_G(S')+(q-3)+3e`.                                    (1)

If instead every closed neighborhood meets `S` in at most two vertices,
let `r=ρ_G(S)` and `γ=γ_G(S)`. Then

`a=ρ^{\{2\}}(G)-r-γ ≥ 0`,
`b=|S|+r-2γ ≥ 0`,

and

`δ_G(S)=a+b`.                                                   (2)

Consequently equality in Steiner's lemma has a recursive classification.
Every dense reduction from a tight pair has `q=3`, lowers subset domination
by exactly one, and leaves a tight residual pair. At a two-sparse terminal
set, both matching/packing bounds used by Steiner must be equalities. If
`δ_G(S)≤2`, no dense step can have domination slack `e>0`; all slack is the
sum of the excess hit sizes `q-3` and the two terminal lemma slacks.

## Strengthened subset inequality

An admissible peeling sequence repeatedly chooses `v_i` with
`q_i=|N[v_i]∩S_{i-1}|≥3` and sets
`S_i=S_{i-1}\N[v_i]`. Define

`p_G(S)=max Σ_i(q_i-3)`,

including the empty sequence. Then

`3γ_G(S) ≤ |S|+ρ^{\{2\}}(G)-p_G(S)`.                           (3)

Indeed, a sequence of length `t` gives

`γ_G(S)≤γ_G(S_t)+t`,

and applying Steiner's lemma only to `S_t` proves (3) after maximizing the
subtracted excess. This improves Steiner's lemma whenever some recursive
closed-neighborhood hit has at least four vertices.

## Product corollary

Use Steiner's fibre notation: `D` is a minimum dominating set of `G□H`,
and `L_1,...,L_{γ(H)}` are the vertically dominated subsets of `V(G)`.
Replacing Lemma 2.3 by (3) in the same counting proof yields

`γ(G□H) ≥ ((3γ(G)-ρ^{\{2\}}(G))/4)γ(H)
          +(1/4)Σ_i p_G(L_i)`.                                 (4)

The new term is nonnegative and exact for each chosen partition. Equation
(4) is not yet a better universal constant because this session does not
prove a positive lower bound for the sum of defects.

## Corrected k=3 analogue

The natural guess

`4γ_G(S)≤|S|+ρ^{\{3\}}(G)`

is false. On vertices `0,...,4`, take edges
`01,03,04,12,14,23` and `S={2,3,4}`. Exact calculation gives
`γ_G(S)=2` and `ρ^{\{3\}}(G)=4`, so the proposed inequality reads `8≤7`.
An explicit optimal 3-packing function is `(0,0,1,1,2)`.

A valid replacement is

`5γ_G(S)≤2|S|+ρ^{\{3\}}(G)`.                                  (5)

It follows by adding Steiner's bounds
`3γ_G(S)≤|S|+ρ²(G)` and `2γ_G(S)≤|S|+ρ_G(S)`, then observing that an optimal
2-packing function plus the indicator of a maximum two-packing in `S` is a
3-packing function. Thus `ρ³(G)≥ρ²(G)+ρ_G(S)`. The same fibre argument gives

`γ(G□H)≥((5γ(G)-ρ³(G))/7)γ(H)`.                               (6)

The old four-parameter equality point extends to the normalized `ρ³`
parameter and makes (6) equal exactly to `(5+√73)/24`; its corresponding
Hou–Lu mixed term is smaller. Therefore (5)–(6) are genuine new inequalities
but do not alone improve the universal constant.

## Withdrawn 0.5809 claim

With `A=γ(G)`, `B=γ(H)`, `x=A-ρ(G)`, `y=B-ρ(H)`, the valid
Chen–Piotrowski–Shreve bound has right-hand side

`A(B-y)+(A-x)y=AB-xy`.

The withdrawn proof substitutes `3AB-2Ay-2xB+xy`. For
`A=B=10,x=y=7`, these are 51 and 69. The later optimization is therefore
irrelevant to domination. Current arXiv metadata labels the paper
“Algebraic mistake.”

## Verification

From `problems/vizing-domination/harness` run:

```text
python3 -m unittest -v
```

Eleven exact tests check named graph products, domination and `k`-function
definitions, Steiner's subset inequality, equation (3), the exact
`Q(√73)` threshold identities, the withdrawn algebra witness, and the
five-vertex `k=3` counterexample together with corrected inequality (5).
These are hygiene and adversarial checks, not a finite proof of the universal
conjecture.

## Relation to prior work and next gate

The dependency reconstruction is in
`literature/steiner-reconstruction.md`. The exact relaxed minimax underlying
0.5643 attains equality, so reoptimization without a new combinatorial
inequality is a dead end. Equations (1)–(4) supply such an inequality and a
stability target. The next session should continue only by proving that the
sets `L_i` have aggregate positive defect, sharpening the terminal equality
classification, or finding a different bridge lemma. Failure to do so is a
STOP/PIVOT under the two-session gate.

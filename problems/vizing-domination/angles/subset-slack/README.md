# Subset-domination slack and peeling defect

## Status

**Rigorous session-derived inequality and equality/near-equality
classification.** This is an instance-sensitive strengthening of Steiner's
Lemma 2.3. It does not by itself improve the universal constant because no
universal positive lower bound on the new defect is known.

Write

`R=ρ^{\{2\}}(G)` and
`δ_G(S)=|S|+R-3γ_G(S)`.

Steiner's lemma says `δ_G(S)≥0`.

## Exact one-step slack identity

Suppose `q=|N[v]∩S|≥3`, put `S'=S\N[v]`, and define

`e=γ_G(S')+1-γ_G(S)`.

Adding `v` to a minimum dominator of `S'` dominates `S`, so `e` is a
nonnegative integer. Direct subtraction gives the exact identity

`δ_G(S)=δ_G(S')+(q-3)+3e`.                                      (1)

This exposes every place where the dense-neighborhood induction can lose.

## Terminal slack identity

Suppose `|N[v]∩S|≤2` for every `v`, and put `r=ρ_G(S)`,
`γ=γ_G(S)`. Steiner's two terminal estimates give the nonnegative integers

`a=R-r-γ`, `b=|S|+r-2γ`.

They satisfy the exact identity

`δ_G(S)=a+b`.                                                    (2)

Therefore Lemma 2.3 is tight exactly as follows:

- at a two-sparse terminal set, both terminal bounds must be tight:
  `γ=R-r=(|S|+r)/2`;
- at every dense reduction from a tight set, necessarily `q=3`, deleting
  `N[v]∩S` lowers the subset domination number by exactly one, and the
  residual set is tight.

Equivalently, equality holds iff there exists a complete (maximal) reduction
sequence in which every step has `q=3,e=0` and the terminal set satisfies both
terminal equalities. Because every term in the slack decomposition is
nonnegative, this is also equivalent to **every** complete reduction sequence
having those properties.

For near equality, if `δ_G(S)≤2`, equation (1) forces `e=0` at every dense
step. Along any complete reduction sequence,

`δ_G(S) = Σ(q_i-3) + a_T+b_T`,

where `T` is the two-sparse terminal set. Thus slack at most two permits only
one or two units total among oversized neighborhood hits and terminal
matching/packing slack. This is a concrete stability statement.

The mechanisms are non-vacuous:

- an edgeless graph with `S=V(G)` is terminal-tight;
- `C4` with `S=V(C4)` is tight and reduces through a three-hit step to a
  terminal singleton;
- in a cyclic labeling of `C5`, taking `S={0,2,4}` gives a two-sparse
  terminal example with `|S|=3`, `R=3`, `r=1`, and `γ_G(S)=2`.

## Strengthened peeling inequality

An admissible peeling sequence starts with `S_0=S` and repeatedly chooses
`v_i` with

`q_i=|N[v_i]∩S_{i-1}|≥3`,

then sets `S_i=S_{i-1}\N[v_i]`. Define the excess-peeling parameter

`p_G(S)=max Σ_i(q_i-3)`,

where the maximum includes the empty sequence. The maximum is attained:
every step removes at least three residual vertices, so sequences have length
at most `⌊|S|/3⌋`. Equivalently,

`p_G(S)=max(0,max_v(|N[v]∩S|-3+p_G(S\N[v])))`,

where the inner maximum ranges over hits of size at least three. Repeatedly dominating the
removed part by `v_i`, followed by Steiner's lemma on the residual set, gives

`3γ_G(S) ≤ |S|+ρ^{\{2\}}(G)-p_G(S)`.                            (3)

Proof: for a sequence of length `t`,

```text
γ_G(S) ≤ γ_G(S_t)+t
       ≤ (|S_t|+R)/3+t
       = (|S|+R-Σ_i(q_i-3))/3.
```

Maximize the subtracted excess. This is strictly stronger than Lemma 2.3
whenever some recursive closed-neighborhood hit has size at least four.

Equality in this strengthened inequality is different from equality in the
original lemma: it holds iff some maximizing complete sequence has `e_i=0`
at every step and both terminal slacks zero. Its hits may exceed three—the
parameter `p_G(S)` records exactly that excess.

In Steiner's fibre argument, applying (3) to each vertically dominated set
`L_i` strengthens Theorem 1.4 to

`γ(G□H) ≥ (3γ(G)-ρ²(G))γ(H)/4 + (Σ_i p_G(L_i))/4`.              (4)

Equation (4) is rigorous but instance-dependent. The next bridge question is
whether product geometry forces a positive aggregate peeling defect, or
whether all `L_i` can simultaneously have the tight recursive structure
above.

The derivation is new within this campaign, but literature priority has not
been established. Conceptually it is an iterative closure of Steiner's lemma,
not a wholly different proof mechanism.

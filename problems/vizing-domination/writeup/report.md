# Equality and stability in Steiner's Vizing bound

**Status:** partial result; Vizing's conjecture remains open.

## Abstract

We independently reconstruct Steiner's universal
`(5+√73)/24≈0.5643` bound and its exact four-parameter optimization, and
audit the withdrawn 0.5809 claim. The latter replaces the valid
Chen–Piotrowski–Shreve expression `AB-xy` by the unequal expression
`3AB-2Ay-2xB+xy`. Our new result is an exact slack decomposition for
Steiner's key subset-domination lemma and a strict strengthening by an
excess-peeling parameter. A second session classifies terminal equality by
odd-clique conflict graphs, decomposes every unit of slack in Steiner's
product proof, and proves that the entire additive integer packing/domination
hierarchy retains the same exact 0.5643 obstruction. No improved universal
constant is claimed. A third session sharpens terminal equality to
singleton/triangle atoms, proves a terminal-aware subset inequality and a
balanced fibre-incidence theorem, and establishes exact square-clique and
fractional-tensor no-go results. The surviving target is the coordinate-hole
system in tight fibres or a genuinely higher-rank LP bridge. A fourth
session proves that every tight atomic column target is external-private,
turns the resulting row holes into exact two-packings, and introduces a
nonseparable weighted-domination blocker lift. Exact obstructions show why
neither result yet raises the universal constant.

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

## Terminal conflict-graph theorem

In the two-sparse terminal regime, define a graph `F` on `S` by joining
`s,t` when one vertex of `G` can dominate both. Then

`γ_G(S)=|S|-ν(F)` and `ρ_G(S)=α(F)`.                            (7)

Moreover, `α(F)+2ν(F)≥|V(F)|`, with equality exactly when every
component of `F` is a complete graph of odd order. Hence terminal equality
in Steiner's subset lemma requires an odd-clique conflict decomposition plus
zero ambient packing slack. The matching slack is the sum of positive
integer component defects, so slack at most two permits at most two
non-odd-clique components. The capacity refinement below further excludes
odd cliques of order at least five from full terminal equality.

## Exact fibre-slack identity

Let `k=γ(H)`, `R=ρ²(G)`, and use Steiner's fibre sets `D_i,L_i`. Define

```text
δ_i=|L_i|+R-3γ_G(L_i),
p_i=|D_i|-γ_G(V(G)\L_i),
d_i=γ_G(V(G)\L_i)+γ_G(L_i)-γ(G),
v=|D|-Σ_i|L_i|.
```

All four defect types are nonnegative, and the full oriented product slack is
the exact identity

`4|D|-k(3γ(G)-R)=v+3Σ_i(p_i+d_i)+Σ_iδ_i`.                      (8)

Thus equality forces row-wise equality in the vertical-cell count, injective
minimum projections in every column, exact domination additivity across
every `L_i`, and recursive odd-clique terminal structure. Equation (8) is a
cross-proof stability theorem, though it does not yet prove these conditions
incompatible.

## Full packing-hierarchy obstruction

For every `m≥1` and `m≥0`, respectively,

```text
3mγ_G(S)≤m|S|+ρ^{2m}(G),
(3m+2)γ_G(S)≤(m+1)|S|+ρ^{2m+1}(G).                            (9)
```

Their exact slacks are sums of the two base subset slacks and packing
superadditivity defects. Their product corollaries are saturated by the same
formal `(a,b)` minimax point for every `m`. The five-vertex graph above is an
actual all-level equality gadget:

`ρ^{k}(G)=⌊3k/2⌋` and `γ^{k}(G)=⌈3k/2⌉`.

Therefore arbitrarily many additive integer packing and domination levels
cannot raise 0.5643 without a structural relation outside this cone.

## Fractional tensor bridge

For nonzero fractional packings `p,q` on `G,H`, put `P=Σp`, `Q=Σq` and

`κ=max_{u,v}[q_v p(N_G[u])+p_u q(N_H[v])-p_uq_v]`.

Then the weights `p_uq_v/κ` form a fractional packing on `G□H`, so

`γ(G□H)≥γ_f(G□H)≥PQ/κ`.                                      (10)

For `r`- and `s`-regular factors, uniform packings yield

`γ(G□H)≥|V(G)||V(H)|/(r+s+1)`.

This is genuinely two-sided and outside Steiner's additive hierarchy.
However, `P4` has the unique optimal fractional packing `(1,0,0,1)`, so
connectedness does not prevent concentration and totals alone cannot control
`κ`. A universal improvement needs a tradeoff between fractional
integrality gaps and local concentration.

## Capacity-two terminal refinement

For a graph `F`, let `τ₂(F)` maximize `Σw_x` over
`w_x∈{0,1,2}` subject to `w_x+w_y≤2` on every edge. Any such weighting of a
two-sparse conflict graph lifts to a global 2-packing of `G`. A
Hall-deficiency argument gives

`ρ²(G)≥τ₂(F)≥α(F)+|F|-ν(F)`.                                 (11)

Consequently terminal slack has the exact three-part decomposition

```text
|S|+ρ²(G)-3γ_G(S)
 = [ρ²(G)-τ₂(F)]
 + [τ₂(F)-(α(F)+|F|-ν(F))]
 + [α(F)+2ν(F)-|F|].                                        (12)
```

On `K_{2m+1}`, the middle defect is zero for `K₁,K₃` and `m-1` for
`m≥2`. Thus terminal equality holds exactly when `F` is a union of `K₁`
and `K₃` and the supported weighting—two on singleton components, one on
triangle vertices—is globally optimal.

Writing `η(F)=τ₂(F)-2|F|+3ν(F)`, use `η` at terminal leaves of the peeling
recursion and add `q-3` at dense steps. The resulting parameter
`p_G^△(S)` satisfies

`3γ_G(S)≤|S|+ρ²(G)-p_G^△(S)`,                                (13)

and dominates the earlier parameter `p_G(S)`. Arbitrary mixtures of the two
terminal atoms are realized by isolated vertices and `C₅` gadgets, so a
universal strict term must still come from product geometry.

## Formal fibre-incidence classification

Put `Γ=γ(G)`, `r=ρ(G)`, and `R=ρ²(G)`. For a complete peeling of `L_i`,
let `ℓ_i` be its number of steps and `r_i` the ordinary packing number of
its terminal remainder. The exact fibre identities imply the stability bound

```text
4Σ_i[ℓ_i+(r-r_i)]
 ≤ γ(H)(Γ+4r-3R)-v+Σ_i(p_i+d_i)+3Σ_iδ_i.                    (14)
```

At the formal Steiner minimizer, `3R=Γ+4r`, and all other defects vanish.
Hence every `L_i` is already terminal, has `r_i=r`, and contains fixed
numbers

`3r-R` of `K₁` atoms and `R-2r` of `K₃` atoms.                (15)

Moreover its minimum complement dominator `X_i=P_G(D_i)` is anticomplete to
`L_i`. The occupied-cell and vertical-cell matrices have identical row and
column margins, so their symmetric difference decomposes into alternating
cycles. Each tight row is a disjoint, size-preserving exchange of partition
centers in `H`.

The remaining coordinate constraint is sharper than these margins. An
external private target of a point `(g,h)∈D_i` must have exactly one
coordinate in `π_i` not dominated from outside that part—namely `h`.
Self-private targets only force a nonempty hole set dominated by `h`. An
explicit `C₄`-based skeleton realizes all cardinality and exchange
conditions but leaves a product vertex undominated, proving that this
coordinate-hole condition is essential.

## External-private and row hole-packing theorems

In fact, the self-private case cannot occur under the full atomic/additive
equality hypotheses. Let `L` have `K₁/K₃` conflict components, let its
canonical capacity weighting be a globally optimal 2-packing, and let `X`
minimally dominate `V(G)\L` with

`|X|+γ_G(L)=γ(G)`.

If `x∈X` were self-private only, optimality of the supported packing would
give `w∈N[x]` whose closed neighborhood has packing load two. Saturation
places `w` on one terminal atom, so a minimum `L`-dominator can be chosen to
contain `w`. Replacing `x` by `w` preserves complement domination, and the
overlap saves one vertex globally, a contradiction. Thus every `x∈X` has an
external private target.

There is a quantitative coordinate consequence. Fix a product row `y`, let
`A_y` be its set of occupied `H`-coordinates, let `I_y` index its vertically
dominated cells, and put `e_y=|A_y|-|I_y|`. If `J_y` indexes the columns
choosing `y` as an external private target and `P_y` is their set of
singleton holes, then

```text
|J_y|-γ_H(P_y)≤e_y,
|J_y|≤ρ(H)+2e_y.                                             (18)
```

The first inequality replaces the centers indexed by `I_y∪J_y` with `A_y`
and a minimum dominator of the holes. The second applies the general
matching-cover bound to `P_y`. At zero row slack, `P_y` is a two-packing.
Summation gives an order-dependent necessary condition
`|D|≤|V(G)|ρ(H)` at formal equality, but no order-free constant gain.

Two-sided external privacy alone is insufficient. The perfect code
`{(i,2i):i∈Z₅}` in `C₅□C₅` has external private neighbors in both coordinate
directions, while every opposite rectangle corner is covered by the next
codeword.

## Limits of rank-one fractional tensors

Every rank-one certificate in (10) obeys

`PQ/κ≤min{|V(H)|γ_f(G),|V(G)|γ_f(H)}`.                       (16)

For `H=P₄`, this caps its normalized factor by
`2γ_f(G)/γ(G)`. A connected split-graph family has
`γ=m-k+3` and `γ_f=m/k+2`; the instance `m=24,k=12` places every
rank-one tensor below Steiner's constant. Optimal and fixed-tolerance
near-optimal packings cannot repair this: the unique optimal packing
`(1,0,0,1)` of `P₄` forces `κ=1` against every optimal packing.

Suboptimal diffusion can still help on classes. For the hard-only split
graph with `m=8,k=4`, a uniform optimal packing paired with
`(1/3,1/3,1/3,1/3)` on `P₄` gives the exact lower bound
`γ(G□P₄)≥8`, a normalized factor `4/5`.

## Square-clique-cover bridge

Let `σ(G)=fcc(G²)`, the fractional vertex clique-cover number of the graph
square. Then

```text
γ(G□H)≥fcc((G□H)²)≥σ(G)σ(H),
γ(G□H)≥max{σ(G)γ(H),γ(G)σ(H)}.                               (17)
```

The first line uses `(G□H)²⊆G²⊠H²` and multiplicativity of fractional
clique cover under strong product. The stronger one-sided line follows by
weighting the `G`-neighborhood slices of any product dominator by a dual
optimum for `fcc(G²)`.

If `G²` is perfect and every clique of `G²` lies in a closed neighborhood
of `G`, then `σ(G)=γ(G)` and Vizing holds for `G` against every `H`.
Forests satisfy both hypotheses. Universally, however, this route has
unbounded loss: for `G_m=L(K_{2m+1})` and `H=P₄`,
`fcc((G_m□P₄)²)≤4` while `γ(G_m)γ(P₄)=2m`.

## Bidirectional blocker lift

For nonnegative weights `w` on `K`, let `τ_K(w)` be the minimum `w`-weight
of an integral dominating set. Define `Λ(G,H)` by maximizing

`Σ_gτ_H(a_{g,·})+Σ_hτ_G(b_{·,h})`

over nonnegative arrays satisfying

`Σ_{g∈N_G[u]}a_{g,v}+Σ_{h∈N_H[v]}b_{u,h}≤1`

for every `(u,v)`. Projecting a product dominator through every closed
neighborhood in each direction proves

`γ(G□H)≥Λ(G,H)`, while minimum factor dominators give
`Λ(G,H)≤γ(G)γ(H)`.                                            (19)

Putting unit `b`-weight on both endpoints of `P₄` gives

`Λ(G,P₄)=2γ(G)`

for every `G`, so the lift certifies Vizing exactly on the family that
defeats pure fractional methods. It is not universally stronger than
Steiner. If the factors are vertex-transitive of degrees `r,s`,

`Λ=max{|V(G)|γ(H)/(r+1),|V(H)|γ(G)/(s+1)}`.                  (20)

For `G=H=L(K_{2m+1})`, the normalized value is
`(2m+1)/(4m-1)→1/2`. Pure nonseparable fractional packing is separately a
STOP because
`γ_f(G□H)≤min{|V(H)|γ_f(G),|V(G)|γ_f(H)}`; the connected split graph
against `P₄` puts this ceiling below Steiner.

There is a precise hybrid target inside `Λ`. For an ordinary maximum
two-packing in `G` and a fractional packing `q` on `H`, with total `Q`, set

`Δ_H(q)=min_{T dominates H}Σ_{v∈T}[1-q(N_H[v])]`.

An explicit feasible blocker solution gives

`Λ(G,H)≥Qγ(G)+ρ(G)Δ_H(q)`.                                   (21)

At the formal Steiner ratios, taking `q` to be half an optimal integer
2-packing reaches `c` exactly when
`Δ_H(q)=(1-b)γ(H)`. This deficit is not forced by the ratios:
`C₅` and augmented split graphs have canonical `Δ=0`, and disjoint-union
mixtures approach the formal irrational point. Those split graphs also have
very diffuse alternative packings. In general, if `η_p,η_q` are maximum
coordinates of fractional packings of totals `P,Q`, then

`γ_f(G□H)≥PQ/(η_p+η_q)`.                                    (22)

The remaining orthogonal target is therefore an explicit
defect–diffuseness dichotomy, not a pure blocker or pure fractional theorem.

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

Twenty-five exact tests check named graph products, domination and `k`-function
definitions, Steiner's subset inequality, equation (3), the exact
`Q(√73)` threshold identities, the withdrawn algebra witness, and the
five-vertex `k=3` counterexample together with corrected inequality (5).
They also exhaustively verify the matching-cover and capacity-two
classifications through five vertices, check the all-level hierarchy gadget,
validate the split-graph fractional examples, and exercise the coordinate-hole
adversarial skeleton. They also check the atomic external-private example,
the necessity of additivity, the `C₅□C₅` corner cycle, and small `P₄`
blocker targets. These are hygiene and adversarial checks, not a finite proof
of the universal conjecture.

## Relation to prior work and next gate

The dependency reconstruction is in
`literature/steiner-reconstruction.md`. The exact relaxed minimax underlying
0.5643 attains equality, so reoptimization without a new combinatorial
inequality is a dead end. The two-session gate is met by the terminal
capacity refinement and exact fibre-incidence theorem. Additive packing,
optimal rank-one concentration, and unrestricted square-clique cover are now
closed as universal routes. The exact external-private and row hole-packing
theorems further meet the gate, but their first aggregate consequence
depends on factor order. Pure higher-rank fractional packing and the
standalone blocker lift are also closed. Future work should seek an
order-free coupling of hole packings, a near-tight cardinal bound for
self-private sets, or a second-order blocker/Steiner hybrid.

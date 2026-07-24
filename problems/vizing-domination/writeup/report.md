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
neither result yet raises the universal constant. A fifth session corrects
the blocker's saturation-defect algebra, proves exact anchored and capped
profile counterfamilies even after connectedization, extracts labelled
mixed-distance escape cycles from two-sided privacy, and shows that a
stronger combined product-packing/blocker LP has zero universal factor on
connected vertex-transitive Cayley graph pairs. A sixth session proves exact
typed partial-cover and fractional repair-energy inequalities, shows that
the typed relaxation clears the robust Cayley obstruction at every pair of
scales, and quantitatively charges isolated fibres to labelled corner-escape
obligations, collisions, or cross-coordinate redundancy. A seventh session
restores the typed cardinality slacks, proves exact overlap and multiplicity
identities, completely classifies the freedom of zero-defect escape graphs,
and realizes Steiner's formal factor-invariant optimizer as a limit of
actual graphs. It also proves a universal adaptive-provider Hall matching
whose tight transitions form labelled Eulerian cell cycles and local
expansion cuts. An eighth session localizes the entire equality skeleton to
connected components, constructs the missing `(5,1,3)` triangle primitive,
and proves a Cartesian-coordinate tax excluding that primitive and its
calibrated singleton mixture from every zero-defect Steiner product.

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

For a dominating set `T`, put

`E_T(q)=Σ_xq_x(|T∩N[x]|-1)≥0`.

Double counting gives the exact correction

```text
Δ_H(q)=γ(H)-Q-Ω_H(q),
Ω_H(q)=max_T[E_T(q)-(|T|-γ(H))]≥0.                            (22)
```

Thus `Δ_H(q)≤γ(H)-Q`. At the formal ratios, the canonical half-2-packing can
only meet Steiner at this absolute ceiling; it can never beat it.

Optimizing over all fractional packings gives the anchored parameter

`F_a(H)=max_q[Q+aΔ_H(q)]`.

For the augmented split graph `S_{2k,z}`,

`F_a(S_{2k,z})=z+max{2,a(k+1)}`,

while `F_a(C₅)=5/3`. Formal-ratio `C₅,S₂₆,₂,S₂₈,₂` mixtures have

`F_a/γ→(1273-115√73)/576≈0.504235<c`.                        (23)

The natural diffuseness repair also fails. Define the capped profile

`Φ_H(t)=max{Σp:p fractional packing, p_v≤t}`.

Then

`γ_f(G□H)≥Φ_G(s)Φ_H(t)/(s+t)`.                               (24)

The profile of `S_{2k,z}` is exactly piecewise linear, with breakpoints
`1/(binom(2k-1,k-1)+2k+z)` and `1/binom(2k-1,k-1)`, and its normalized form
is

`(z/γ)t+e(t),  0≤e(t)≤2/γ`

uniformly over all caps. An asymmetric additive pair approaching both
formal packing ratios keeps both anchored values and every independently
capped tensor below `c`; the cap arm is at most

`(-247+37√73)/264≈0.261849`.                                 (25)

Hence the entire factor-marginal defect–diffuseness hybrid is a STOP.

## Cross-row holes and escape cycles

If `P_y` is the singleton-hole two-packing in product row `y` and `p` is
any fractional packing on `G`, then

`Σ_yp_y|P_y|≤γ_f(G□H)≤|D|`.                                  (26)

A common-crown construction concentrates all external private targets in
one closed neighborhood, making this weighted mass arbitrarily small
relative to the number of private incidences. Full formal balance adds the
exact common-neighborhood bound

`M(Y)≤2γ(H)ρ(H)+sd`,

where `s` is the number of singleton terminal cells and `d=|L_i|`; its
coefficient is still vacuous at comparable formal scales.

Two-sided external privacy nevertheless forces a genuinely product-labelled
object. The horizontal and vertical private neighbors of each `d∈D` define
a corner owned by another point of `D`. Choosing one owner per corner gives
a directed cycle in `D`; every arc changes one coordinate by an edge and
the other by distance exactly two. At exact equality, its indegrees are
bounded by the row-hole packing numbers and every arc has a
red-diagonal/blue-cross-zero cell-label pattern. The `C₅□C₅` perfect code
realizes a directed 5-cycle, so existence and bounded indegree alone do not
give a density defect.

## Combined product-packing/blocker lift

Let `K=G□H`. Make a product fractional packing `W` share the blocker
capacity by replacing its constraint with

```text
W(N_K[(u,v)])
+Σ_{g∈N_G[u]}a_{g,v}
+Σ_{h∈N_H[v]}b_{u,h}≤1.
```

Maximizing

`Σ_xW_x+Σ_gτ_H(a_g)+Σ_hτ_G(b^h)`

defines `Ξ(G,H)`. The same product-dominator count proves

`γ(G□H)≥Ξ(G,H)`.                                             (27)

Its exact dual minimizes `Σd_{u,v}` subject to:

1. `d` fractionally dominates `G□H`; and
2. for every vertex of either factor, the corresponding neighborhood slice
   of `d` covers the incidence marginals of a probability distribution over
   integral dominators of the opposite factor.

Thus one cheap dual object must satisfy the product-fractional and both
owner-indexed integral-routing requirements simultaneously.

For vertex-transitive factors of degrees `r,s`, averaging gives exactly

```text
Ξ=max{
 |G||H|/(r+s+1),
 |G|γ(H)/(r+1),
 |H|γ(G)/(s+1)
}.                                                          (28)
```

The Vizing-level claim `Ξ≥γ(G)γ(H)` is false:
`Ξ(C₄,C₄)=16/5<4`. More decisively, `Ξ` has no positive universal factor.
For a vertex-transitive graph, put

`κ_G=γ(G)|N_G[g]|/|V(G)|`.

Equation (28), normalized, is

```text
max{
  1/κ_G,
  1/κ_H,
  |N_G||N_H|/[κ_Gκ_H(|N_G|+|N_H|-1)]
}.                                                          (29)
```

Bollobás--Janson--Riordan's translate-cover theorem gives affinely spanning
sets in elementary abelian 2-groups with `κ→∞`
[@bollobasJansonRiordan2011, Theorem 4.1 and Remark 4.2]. The associated
Cayley graphs are connected and have the translates as closed
neighborhoods. Choosing the second closed-neighborhood scale so large that
its logarithm dominates the first scale sends all three terms in (29) to
zero. Therefore

`inf Ξ(G,H)/(γ(G)γ(H))=0`

even over connected vertex-transitive graphs.

For comparison, the exact formal-ratio additive counterfamily from (25)
has a componentwise blocker lower bound

`(14479-997√73)/9504≈0.627170>c`,

but safe zero-weight ports connect that family while preserving its packing
ratios and marginal no-gos. Connectedness alone repairs neither route.

## Typed fibre-set successor

For the actual row labels `A_g={h:(g,h)∈D}`, let

`V_g=⋃_{x∈N_G(g)}A_x`

use the open neighborhood. Product domination is exactly

`V(H)\V_g⊆N_H[A_g]`.

The necessary cardinality condition

`|A_g|≥γ_H(V(H)\V_g)`                                       (30)

and its column analogue define a strict labelled relaxation `Θ`. It retains
the correlated coordinate sets discarded by every averaged lift. Two exact
baselines are

```text
Θ≥max{γ^{γ(H)}(G),γ^{γ(G)}(H)},
Θ≥γ(G□H)/2≥(c/2)γ(G)γ(H).                                  (31)
```

The second follows by repairing each genuinely missed row subset at cost at
most `|A_g|`. The relaxation is strict: for
`G=H=K₂⊔K₁`, four swapped-component labels satisfy both cardinality systems
but do not dominate the product, whose domination number is five. Improving
the factor-two repair alone is no longer the target; the label correlations
support stronger exact inequalities.

## Partial-cover profile and Cayley calibration

Define

`u_K(t)=min_{|C|≤t}|V(K)\N_K[C]|`.

For every typed-feasible incidence set, with row masses `a_g` and column
masses `b_h`,

`Σ_g u_H(a_g)+Σ_hu_G(b_h)≤|G||H|`.                          (32)

The proof is a two-axis count:

```text
u_H(a_g)≤|V_g|,
Σ_g|V_g|=Σ_h|N_G^open(B_h)|
         ≤Σ_h(|G|-u_G(b_h)).
```

Moreover, this is an exact defect identity. Its three terms are import
profile excess, partial-cover suboptimality of the actual column fibres,
and isolated vertices in the induced column fibres.

For `d`-regular `G`,

`Θ(G,H)≥|G|(t+1)u_H(t)/[u_H(t)+d(t+1)]`.                    (33)

A robust adaptation of the random-translate proof in
Bollobás--Janson--Riordan Remark 4.3
[@bollobasJansonRiordan2011, Remark 4.3] constructs connected Cayley graphs on
`F₂^m` with closed-neighborhood size `k`, domination number asymptotic to
`(n/k)log k`, and

```text
u(t)>L,
t=(n/k)(log k-10 log log k)+O(1),
L=(log k)^6+O(1).
```

Equation (33) beats `γ(G)γ(H)` for every pair of growing graphs in this
robust family, by a diverging factor, and gives at least the Vizing scale
when the other factor is fixed. Thus the actual labels in `Θ` decisively
defeat the asymmetric Cayley construction that drives `Ξ` to zero. This
robust near-cover statement is a new adaptation, not a theorem stated
verbatim in the cited paper.

## Correlated fractional charging

Let `q,p` be fractional packings on `G,H`, with totals `Q,P`, and put

```text
C_g=H\V_g,       D_h=G\U_h,
Z=Σ_{(g,h)∈A}(1-q_g)(1-p_h),
E_H=Σ_gq_g[γ_H(C_g)-p(C_g)],
E_G=Σ_hp_h[γ_G(D_h)-q(D_h)],
α_H=Σ_gq_g[|A_g|-γ_H(C_g)],
α_G=Σ_hp_h[|B_h|-γ_G(D_h)].
```

Then every typed-feasible set of mass `M` satisfies

`M≥PQ+Z+max{E_H+α_H,E_G+α_G}`.                              (34)

The exact row identity behind (34) is

```text
Σ_A(q_g+p_h-q_gp_h)-PQ
 =Σ_gq_g[|A_g|-p(C_g)+o_g]
  +Σ_xp(A_x)[1-q(N_G[x])],
```

where `o_g` is the nonnegative weighted overlap among imported neighbouring
fibres. Splitting
`|A_g|-p(C_g)=|A_g|-γ_H(C_g)+γ_H(C_g)-p(C_g)` retains
`α_H+E_H`; the symmetric identity retains `α_G+E_G`.

For a minimum dominator `T` of a target `C`,

```text
γ_K(C)-p(C)
 =Σ_{t∈T}[1-p(C∩N[t])]
  +Σ_{v∈C}p_v(|T∩N[v]|-1).                                 (35)
```

Thus zero repair energy means every repair owner is packing-saturated and
every positive-packing target is covered exactly once. For half of an
integral 2-packing, every failure costs at least one half.

The cap-only consequence has the corrected denominator

`M≥PQ/(s+t-st)`.                                             (36)

It is exactly the known rank-one product packing and remains a STOP. The
formal-ratio counterfamily keeps it at most

`(-247+37√73)/132≈0.523698<c`.

## Isolation-to-escape charging

For an actual product dominator, let `I_G` count selected points isolated
inside their fixed-label `G`-fibres. Define

```text
r_{x,h}=|N_G(x)∩B_h|,
Ω_G=Σ_{x,h}(r_{x,h}-1)_+,
X_H=Σ_x|V_x∩N_H[A_x]|.
```

If `Bad_G⊆I_G` consists of points with no horizontal external-private
neighbor, then

`|Bad_G|≤2Ω_G+X_H`.                                         (37)

Choose one horizontal neighbor target for each bad point. If it has two or
more same-label owners, charge the collision; otherwise its additional
dominator must lie in the arrival row and charges `X_H`.

Applying (37) in both orientations, the number `T` of fibre-isolated points
with external private neighbors in both directions satisfies

```text
|T|≥[
 I_G+I_H-|D|
 -2Ω_G-2Ω_H-X_H-X_G
]_+.                                                        (38)
```

Every point counted by (38) carries the labelled mixed `(1,2)` or `(2,1)`
private-corner escape obligation. Equation (38) is exact on the
`C₅□C₅` 5-cycle and the `K₂□P₃` 2-cycle.

## Four-region and multiplicity identities

Let `C` be the product region with no horizontal open import and `D₀` the
region with no vertical open import. Put

```text
I=A∩C∩D₀,
W=(C∩D₀)\A,
J=(G□H)\(C∪D₀),
w(g,h)=q_gp_h,
K=w(A\I)+w(J).
```

Here `W` is exactly the missed-cell set and `J` is the double-open-import
region. Direct inclusion--exclusion gives

```text
M
=PQ+Z+E_H+E_G+α_H+α_G-K+w(W).                              (39)
```

Thus (39) repairs the false addition of the two repair energies by an exact
overlap tax.

There is a second exact decomposition. Let `m(z)` count all selected owners
of `z`, let `t(z)` retain only self-selection and existence of an owner in
each open direction, and define

```text
R=Σ_zw(z)[m(z)-t(z)],
Δ=Σ_{(g,h)∈A}{
 p_h[1-q(N_G[g])]
+q_g[1-p(N_H[h])]
}.
```

Then

```text
2(M-PQ-Z)
=E_H+E_G+α_H+α_G+R+Δ.                                     (40)
```

The two directional residuals are nonnegative and sum exactly to `R+Δ`.
Minimum dominators in `K₂□K₂` and `P₃□P₃` make the corrected maximum in
(34) sharp, so (39)--(40) are equality/stability diagnostics rather than a
new scalar constant.

## Complete obstruction to generic escape closure

At

`I_G=I_H=D` and `Ω_G=Ω_H=X_G=X_H=0`,

the dominator `D` is a perfect code: every product vertex has exactly one
owner. Its mixed escape-candidate relation is undirected.

More strongly, every finite bipartite graph `F` without isolates is
realizable as such a zero-defect escape graph. If `H` is the one-subdivision
of `F` with bipartition `S,T`, then

`D={(0,s):s∈S}∪{(1,t):t∈T}`

is a minimum perfect code in `K₂□H`, and its escape graph is exactly `F`.
Taking stars gives cyclic fraction `2/(k+1)→0`; taking paths gives
arbitrarily long in-trees. Hence generic cycle density, bounded return,
injective owner choice, and additive escape credit are all impossible even
at zero present defect.

## Actual calibration of Steiner's factor point

For every fixed `L`, a random graph `K∼G(n,1/2)` has, with positive
probability for large `n`,

```text
γ(K)>L,       ρ(K)=1,       ρ^{\{2\}}(K)=2.                 (41)
```

Indeed, union bounds show simultaneously that every pair and triple lies
in a closed neighborhood, while no set of at most `L` vertices dominates.
The first two properties force the two packing values in (41).

Write

```text
d=c=(5+√73)/24,
t=(47-5√73)/24,
s=(√73-7)/6.
```

These positive numbers sum to one. Take a disjoint mixture with domination
mass fractions `d,t,s` coming respectively from graphs in (41), isolated
vertices, and copies of `C₅`. Since the three limiting normalized packing
pairs are

`(0,0)`, `(1,1)`, and `(1/2,3/4)`,

the mixture satisfies

```text
ρ/γ→t+s/2=(11-√73)/8=a,
ρ²/(2γ)→t+3s/4=(13-√73)/12=b.                              (42)
```

Thus Steiner's formal optimizer is the limit of actual finite graphs.
No continuous universal relation involving only `γ,ρ,ρ²` can exclude it.

## Indexed provider reuse obstruction

For one row, let `I` index terminal demands `y_i∈π_i`, and join `i` to a
selected row coordinate `a` when `a∈N[y_i]\π_i`. The unavoidable provider
reuse is the exact Hall deficiency

```text
|I|-ν(P)
=max_{J⊆I}(|J|-|N_P(J)|).                                  (43)
```

Indexed `K₃` atomicity and exact row exchange do not control (43). For every
`m`, an explicit graph `H_m` with blue cells `{c_i,s_i,t_i}` and red cells
`{r_i,a_i,w_i}` admits an actual dominator

`D_m=(T×{a_0,...,a_{m-1}})∪(X×{c_i,w_i})⊂C₅□H_m`,

where `T={0,2,4}` and `X={1,3}`. Every blue fibre is the same exact terminal
triangle `T`, its canonical weighting is an optimal global 2-packing, and
each provider row performs a minimum size-preserving exchange. Nevertheless
the single point `(g,a_0)` is the unique provider for all `m` blue demands
`s_i`.

The four-region tax is zero for the natural indexed packings, so it cannot
detect reuse across different packing choices. The obstruction is paid
instead by the exact fibre defects:

```text
blue: (p_i,d_i,δ_i)=(1,1,0),
red:  (p_i,d_i,δ_i)=(3,0,3),
v=4m.                                                       (44)
```

Even ideal row-plus-column triangle additivity is quantitatively tiny:

```text
b²+2b(b-a)=(13-√73)/24≈0.18567<c.
```

Starting from `b²`, at least eighteen independent triangle charges are
required to cross `c`, since

`(c-b²)/(b(b-a))=(249+21√73)/24≈17.851`.                    (45)

Thus the next lemma must couple outgoing terminal indices to incoming
private-hole two-packings and charge Hall deficiency to the full defect
budget with substantial amplification.

## Adaptive provider matching and labelled cycles

There is a universal positive theorem once the point inside each source
cell may be chosen adaptively. For a row `g`, put

```text
I_g={i:g∈L_i},
A_g=P_H(D∩({g}×H)).
```

Join `i∈I_g` to `a∈A_g\π_i` when
`N_H[a]∩π_i≠∅`. The exact row-exchange identity

`γ_H(⋃_{i∈I_g}π_i)=|I_g|`

implies Hall's condition. Indeed, the neighbor set of `J⊆I_g`, together
with the retained centers for `I_g\J`, dominates the whole union. Hence
there is an injection

```text
μ_g:I_g→A_g,
μ_g(i)∉π_i,
N_H[μ_g(i)]∩π_i≠∅.                                        (46)
```

Globally, (46) injects the blue incidences `(g,i)`, `g∈L_i`, into `D`
and leaves exactly

`v=|D|-Σ_i|L_i|`

selected points unused. If `v=0` and `|D_i|=|L_i|` for every column, the
matches give a loopless Eulerian cell digraph, hence a decomposition into
directed cycles carrying actual domination labels.

Under the full atomic/additive external-private hypotheses, every matched
point transfers injectively to a singleton private-hole occurrence. With
`e_x=|A_x|-|I_x|`, this gives the local open-neighborhood cut

```text
Σ_{g∈U}|I_g|
≤ρ(H)|N_G^open(U)|
 +2Σ_{x∈N_G^open(U)}e_x.                                   (47)
```

The theorem is exactly compatible with the obstruction above: in
`C₅□H_m`, it matches blue cell `B_i` to the distinct provider `a_i` using
the adaptively chosen target `t_i`. The pre-prescribed targets `s_i` still
all require `a₀`. Thus (46) solves adaptive cell-level provider reuse, not
the demand-specific graph (43).

The triangle-only consequence of (47) is

`3k(R-2r)≤|V(G)|ρ(H)`,                                      (48)

which is weaker than the existing all-incidence inequality
`k(2R-3r)≤|V(G)|ρ(H)`. No new universal constant follows. The remaining
bridge is compatibility between the triangle-energy witness and the
adaptive matching, or a useful exploitation of the local weighted cuts.

## Componentwise equality calibration

Let `C` be a connected component of `G`, and write

`Γ_C=γ(C)`, `r_C=ρ(C)`, `R_C=ρ^{\{2\}}(C)`.

Under the full equality conditions
`v=p_i=d_i=δ_i=B_i=0`, the canonical ordinary and integral 2-packings on
every `L_i` saturate their optima separately in each component. If `z_C`
and `τ_C` are the numbers of terminal singleton and triangle atoms in
`L_i∩C`, then

```text
z_C=3r_C-R_C,          τ_C=R_C-2r_C,
|L_i∩C|=2R_C-3r_C,     γ_C(L_i∩C)=R_C-r_C.                 (49)
```

Projection and additivity equality also localize:

`|D_i∩(C×π_i)|=|X_i∩C|=Γ_C-R_C+r_C`.

Finally the pointwise row balance, summed only over `C`, gives

`3R_C=Γ_C+4r_C`.                                            (50)

Equivalently `Γ_C=2z_C+5τ_C`. Thus the only local numerical atoms are
the singleton primitive `(2,1,2)` and triangle primitive `(5,1,3)`.
This is stronger than the previous global calibration: disconnected
components cannot cancel their deviations from (50).

## A connected triangle primitive

There exists a finite connected graph `P` with anticomplete triples `L,X`
and common remainder `Z` such that

```text
(γ(P),ρ(P),ρ²(P))=(5,1,3),
γ_P(L)=γ_P(X)=2,
γ_P(V\L)=γ_P(V\X)=γ_P(Z)=3.                                (51)
```

Moreover, `L,X` are the only feasible unit triples for an integral
2-packing, and each dominates the complement of the other.

For the construction, take `N` copies of a vertex adjacent to each chosen
pair from `L` and each chosen pair from `X`, and `N` copies adjacent to each
specified pair `(ℓ_p,x_q)`. Put independent probability-`1/2` edges among
these `18N` auxiliary vertices. With positive probability:

- every triple except `L,X` lies in a closed neighborhood; and
- every set of at most four vertices not containing all of `L` or `X`
  misses an auxiliary vertex.

For a fixed triple the failure probability is at most `(7/8)^{N-3}`; for
a fixed four-set it is at most `(15/16)^{N-4}`. The union bound tends to
zero, and `N=1000` already makes the sum less than `5.4·10^-13`.
The two events imply all claims in (51), while the deterministic incidences
make the graph connected. This is a deductive existence proof, not
finite-search evidence.

## Support-avoidance coordinate tax

Let `U` lie in one component `C` and be disjoint from every `L_i`. Let
`R_U` be the rows of `U` containing a selected product point, and let

`v_C=Σ_{g∈C}(|A_g|-|I_g|)`.

Then `|R_U|≤v_C`, and every cell satisfies

`|D_i∩(C×π_i)|≥|π_i|(γ_C(U)-|R_U|)
              ≥|π_i|(γ_C(U)-v_C)`.                         (52)

Indeed, for each `h∈π_i`, the same-coordinate support
`{g∈C:(g,h)∈D}` must horizontally dominate `U\R_U`; adjoining `R_U`
dominates all of `U`. Summing this domination lower bound over the distinct
coordinates `h` proves (52).

At zero vertical slack, the primitive's only terminal triples are `L,X`, so
their common remainder `Z` is avoided by every `L_i`. Equations (51)--(52)
give

`3|π_i|≤|D_i∩(C×π_i)|=5-3+1=3`.

Every partition cell is therefore a singleton. This forces
`|V(H)|=γ(H)`, hence `H` is edgeless, in which case no nonempty cell is
vertically dominated from outside. This contradiction proves:

> No full-zero-defect Steiner product can contain this connected triangle
> primitive as a component.

For `z` copies of `C₄` and `τ` copies of the primitive, a cell of size two
forces projection defect at least

`p_i≥3τ-z`.                                                  (53)

At the formal Steiner ratios,

`(3τ-z)/Γ=8b-9a=(11√73-89)/24>0`.                           (54)

Thus the natural componentwise-calibrated mixture cannot lift either.
Equations (52)--(54) are the first exact incompatibility between a realized
triangle equality skeleton and the Cartesian coordinates. They do not
exclude other `(5,1,3)` components whose allowable terminal triples cover
all hard subsets.

There is also an exact near-equality audit. With
`x_{i,C}=Γ_C-γ_C(L_i)`, (52) implies

```text
Σ_i(p_{i,C}+d_{i,C})
≥[|V(H)|(γ_C(U)-v_C)-Σ_i x_{i,C}]_+.                       (55)
```

Optimizing the resulting contribution to the full Steiner slack over the
integer `v_C` gives only

`E≥ceil([γ_C(U)-(Σ_i x_{i,C})/|V(H)|]_+)`.                  (56)

For the calibrated mixture this is `ceil((3τ-z)/2)`, so its normalized
gain is only `(11√73-89)/(192γ(H))`. It vanishes as `γ(H)` grows. Thus
support avoidance alone is a universal-constant STOP: the missing theorem
must charge an occupied avoided row in linearly many cells.

The opposite coverage extreme has an exact benchmark. Partition a graph
into paired independent triples `B_p`; put no edges between partners and
join unequal coordinate labels between every pair of nonpartner blocks.
The terminal triples partition the vertex set, each partner is a separated
minimum complement dominator, and `ρ=1,R=3`. Nevertheless three vertices
with distinct labels dominate the graph. Thus every support pays exactly

`γ(V\B_p)+γ(B_p)-γ(G)=3+2-3=2`.                             (57)

Coverage and all packing/complement conditions can coexist; in this
symmetric model, a transversal dominator exposes the additivity defect.

## Dependency-region stability and remaining obstruction

If `X` dominates `T=V(G)\L`, put

```text
e=|X|-γ_G(T),
d=γ_G(T)+γ_G(L)-γ(G),
C_X(S)={v∈T: ∅≠N[v]∩X⊆S}.
```

Then

`|S|-γ_G(C_X(S))≤e+d`.                                      (58)

The proof replaces `S` inside `X` by a minimum dominator of its complete
dependency region and then adds a minimum dominator of `L`. In a Steiner
column, the right side is at most `p_i+d_i`. Common-crown graphs show that
(58) cannot be transferred to one arbitrarily chosen private target per
member of `S`: the omitted parts of the dependency regions carry the
required domination number.

The adaptive atom ledger is also exactly conservative. At `v=0`, Hall
matching assigns one base unit to every selected point. A local triangle
repair-energy unit is real, but charging its distinguished selected point as
an additional unit double-counts that point. An exact eleven-vertex balanced
row-exchange example further shows that the adaptive targets need not form a
two-packing even when the cell transitions are Eulerian.

The remaining universal target is therefore stronger than common support
avoidance: every `(5,1,3)` equality component must force hard coordinate
holes in linearly many cells, or pay a product-scale packing, additivity, or
projection defect.

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

Forty-one exact tests check named graph products, domination and `k`-function
definitions, Steiner's subset inequality, equation (3), the exact
`Q(√73)` threshold identities, the withdrawn algebra witness, and the
five-vertex `k=3` counterexample together with corrected inequality (5).
They also exhaustively verify the matching-cover and capacity-two
classifications through five vertices, check the all-level hierarchy gadget,
validate the split-graph fractional examples, and exercise the coordinate-hole
adversarial skeleton. They also check the atomic external-private example,
the necessity of additivity, the `C₅□C₅` corner cycle, and small `P₄`
blocker targets. New exhaustive fixtures verify (32), its exact isolation
slack, (34), the small typed relaxation values, and the exact surd gap after
the corrected cap denominator. Session-seven fixtures verify (39)--(40),
the recovered cardinality slack, the one-subdivision realization of
arbitrary bipartite escape graphs, and the indexed-provider reuse
obstruction together with its adaptive matching. These are hygiene and
adversarial checks, not a finite proof of the universal conjecture.
Session-eight fixtures exhaust the dependency-region defect lemma on named
small graphs, verify the balanced eleven-vertex adaptive-target obstruction
and the covering triangle block design, and check the exact cap-half and
triangle-surplus identities in `Q(√73)`.

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
standalone blocker lift are also closed. The factor-marginal
blocker/diffuseness hybrid and the stronger combined lift are now closed as
well. The typed profile and corrected fractional ledger clear the mandatory
Cayley obstruction, and (38) turns isolation into a density of labelled
escape obligations. The universal escape-realization theorem closes generic
path/cycle arguments, while (42) closes factor-invariant reoptimization.
Equation (46) resolves adaptive cell-level provider reuse and adds labelled
cycle and local-cut structure. Equations (50) and (52) now exclude a
realized componentwise equality family using actual coordinate labels.
Future work must make the resulting support-coverage alternative universal
and quantitative; scalar weighted expansion and cap-only averaging are
closed.

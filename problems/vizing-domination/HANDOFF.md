# Handoff — Vizing’s domination conjecture

Read these first:

- `angles/componentwise-calibration/README.md`
- `angles/neutral-core-coordinate-tax/README.md`
- `angles/adaptive-triangle-conservation/README.md`
- `angles/joint-dependency-stability/README.md`
- `angles/adaptive-provider-cycles/README.md`
- `angles/fibre-slack/README.md`
- `angles/incidence-balance/README.md`

The best universal constant remains

`c=(5+√73)/24≈0.5643`.

The withdrawn `0.5809` claim is not a theorem and was not used.

## Decisive session-eight results

### 1. Equality is componentwise

Under the full equality conditions
`v=p_i=d_i=δ_i=B_i=0`, every connected component `C` satisfies

```text
3R_C=Γ_C+4r_C,
Γ_C=2z_C+5τ_C,
```

where `z_C,τ_C` are the fixed numbers of singleton and triangle terminal
atoms in every `L_i∩C`. All packing, projection, and domination-additivity
equalities localize to `C`.

The numerical primitives are therefore exactly

```text
singleton: (Γ,r,R)=(2,1,2),
triangle:  (Γ,r,R)=(5,1,3).
```

Global factor-invariant mixtures do not satisfy this stronger equality
condition componentwise.

### 2. The triangle primitive exists

There is a finite connected graph `P` with anticomplete triples `L,X` and
remainder `Z` such that

```text
(γ,ρ,ρ²)=(5,1,3),
γ(L)=γ(X)=2,
γ(V\L)=γ(V\X)=γ(Z)=3,
```

and `L,X` are the only feasible unit triples for an integral 2-packing.
An explicit `N=1000` probabilistic construction has a union-bound failure
probability below `5.4·10^-13`. This is a deductive existence proof.

Thus a factor-only argument cannot eliminate the triangle primitive.

### 3. Product coordinates eliminate the symmetric primitive

If a set `U` in a component `C` is disjoint from every vertical fibre, then

```text
|D_i∩(C×π_i)|
≥|π_i|(γ_C(U)-|R_U|)
≥|π_i|(γ_C(U)-v_C),
```

where `R_U` is the set of occupied rows in `U` and `v_C` is the component
vertical slack.

At zero slack, the primitive's common core `Z` is avoided by every allowable
terminal triple and has domination number three, while
`|D_i∩(C×π_i)|=3`. Every partition cell would have to be singleton, making
`H` edgeless and vertical domination impossible. Hence no full-zero-defect
Steiner product can contain this primitive.

For `z` copies of `C₄` plus `τ` copies of `P`, a size-two cell pays

`p_i≥3τ-z`.

At the formal ratios,

`(3τ-z)/Γ=(11√73-89)/24>0`.

This is the first exact Cartesian incompatibility for a realized
componentwise equality skeleton. Its strongest near-equality aggregate gives
only

`c+(11√73-89)/(192γ(H))`,

which vanishes as `γ(H)` grows. One occupied core row pays one vertical
slack unit and can be reused in every cell. Common support avoidance without
a per-cell reuse charge is therefore a universal-constant STOP.

### 4. Two supporting lemmas and two hard stops

For a complement dominator `X`,

```text
C_X(S)={v∈V\L:∅≠N[v]∩X⊆S},
|S|-γ(C_X(S))≤p_i+d_i.
```

This controls the complete dependency region. Common crowns show it does not
control one chosen private target per member of `S`.

Adaptive Hall atom credits total exactly `|D|-v`. At `v=0`, every selected
point is saturated once. The local triangle repair energy cannot be added by
charging its selected witness a second time. A balanced eleven-vertex
exchange also shows adaptive targets need not form a two-packing.

Cap-half averaging and scalar row-weighted expansion are hard stops:
the former gives only `(4/3)b²≈0.18385`, and connected true-twin reservoirs
make the latter arbitrarily slack.

A paired-triple covering design is the mandatory positive-defect benchmark:
its terminal triangles cover every vertex, each has a separated minimum
complement dominator, and `ρ=1,ρ²=3`, but a transversal three-dominator
forces exactly `d=2` per support.

## Only live attack

Prove a **product-scale support/coordinate dichotomy** for connected
`(5,1,3)` equality components.

Let `𝒯` be the hypergraph of feasible terminal triples that can occur as
`L_i∩C`. Establish one of:

1. broad coverage by `𝒯` forces a uniform positive domination-additivity or
   packing defect, generalizing the exact paired-block witness; or
2. an avoided hard set leaves coordinate holes that charge each occupied
   repair row in linearly many distinct cells, preventing one-time reuse.

Then:

1. make this product-scale dichotomy quantitative with
   `v_C,p_i,d_i,δ_i`;
2. sum it over components and partition cells;
3. insert the resulting term into
   `4|D|-k(3Γ-R)=v+3Σ(p_i+d_i)+Σδ_i`; and
4. only after obtaining a new combinatorial coefficient, solve the exact
   minimax.

Any proposed dichotomy or stability proof requires a fresh GPT-5.6 Sol
xhigh audit.

## Mandatory adversarial checks

- the symmetric `(5,1,3)` primitive in
  `angles/neutral-core-coordinate-tax`;
- the balanced eleven-vertex adaptive-target obstruction;
- common-crown dependency regions;
- the paired-triple covering design with exact `d=2`;
- true-twin reservoirs for scalar weighted cuts; and
- the actual `C₅□H_m` positive-defect provider obstruction.

## Hard stops

- No numerical reoptimization of Steiner's existing six inequalities.
- No relation using only `γ,ρ,ρ²`, even componentwise without product
  support labels.
- No scalar weighted expansion or cap-only tensor.
- No inference that adaptive Hall targets form a packing.
- No extra triangle unit charged to an already Hall-saturated selected point.
- No common-avoidance claim without controlling reuse of occupied core rows
  across cells.
- No generic escape closure, additive packing hierarchy, anchored/blocker
  slice, or unrestricted square-clique LP.
- Finite verification remains hygiene and falsification only.

# Neutral-core coordinate tax

## Status

**New product-sensitive lemma proved; zero-defect corollary independently
accepted by GPT-5.6 Sol at xhigh effort.** A set of factor rows avoided by
every vertical fibre must be horizontally dominated separately at every
coordinate of every partition cell. This excludes a concrete connected
triangle primitive, and the calibrated mixture built from it, from any
full-zero-defect Steiner product.

This is a rigorous incompatibility theorem for a natural equality class. It
does not yet classify every `(5,1,3)` primitive or improve the universal
constant.

## Support-avoidance cell-size lemma

Retain Steiner's product notation. For a component `C` of `G`, write

```text
D_{i,C}=D∩(C×π_i),
A_g=P_H(D∩({g}×V(H))),
I_g={i:g∈L_i}.
```

Let `U⊆V(C)` be avoided by every vertical fibre:

`U∩L_i=∅` for every `i`.                                    (1)

Let

```text
R_U={u∈U:A_u≠∅},
v_C=Σ_{g∈C}(|A_g|-|I_g|).
```

The row inequalities make `v_C≥0`, `Σ_Cv_C=v`, and (1) gives
`|R_U|≤v_C`. For every cell `i`,

`|D_{i,C}|≥|π_i|(γ_C(U)-|R_U|)
          ≥|π_i|(γ_C(U)-v_C)`.                              (2)

In particular, at `v=0`,

`|D_{i,C}|≥|π_i|γ_C(U)`.                                    (3)

### Proof

Fix `h∈π_i` and put

`S^C_{i,h}={g∈C:(g,h)∈D}`.

If `u∈U\R_U`, row `u` contains no selected product point. Therefore
`(u,h)` cannot be dominated vertically. Product domination forces a point
`(g,h)∈D` with `g∈N_C[u]`, so `S^C_{i,h}` dominates `U\R_U`.
Consequently `S^C_{i,h}∪R_U` dominates `U`, and

`|S^C_{i,h}|≥γ_C(U)-|R_U|`.

Sum this inequality over the distinct coordinates `h∈π_i`. Their supports
partition `D_{i,C}`, proving (2). If `v=0`, every `v_C` and `R_U` vanish,
giving (3).

The proof uses the actual Cartesian-product label `h`; it is invisible to
all factor-invariant and averaged profile bounds.

### Exact near-equality aggregate

The robust form has an exact limitation. Define component defects

```text
p_{i,C}=|D_{i,C}|-γ_C(V(C)\L_i),
d_{i,C}=γ_C(V(C)\L_i)+γ_C(L_i)-Γ_C,
x_{i,C}=Γ_C-γ_C(L_i).
```

They are nonnegative and sum to the global column defects. Equation (2)
gives

```text
Σ_i(p_{i,C}+d_{i,C})
≥[|V(H)|(γ_C(U)-v_C)-Σ_i x_{i,C}]_+.                       (4)
```

Together with the exact Steiner slack `E`, optimizing over the integer
`v_C≥0` yields

`E≥ceil([γ_C(U)-(Σ_i x_{i,C})/|V(H)|]_+)`.                  (5)

If `γ_C(L_i)=ℓ_C` is fixed and every `L_i` is nonempty, then `H` has no
isolated vertices and `|V(H)|≥2γ(H)`. Hence

```text
Σ_i(p_{i,C}+d_{i,C})
 ≥γ(H)[2(γ_C(U)-v_C)-(Γ_C-ℓ_C)]_+,
E≥ceil([γ_C(U)-(Γ_C-ℓ_C)/2]_+).                            (6)
```

The integer optimization in (5) is sharp for this information: one occupied
row costs one unit of `v_C` but is then exempted in every cell. Thus the
robust lemma by itself forces only a component-scale, not product-scale,
defect.

## A symmetric triangle primitive exists

There is a finite connected graph `P` with disjoint triples

```text
L={ℓ₁,ℓ₂,ℓ₃},       X={x₁,x₂,x₃}
```

such that

```text
γ(P)=5,       ρ(P)=1,       ρ^{\{2\}}(P)=3,                 (7)
γ_P(L)=γ_P(X)=2,
γ_P(V\L)=γ_P(V\X)=γ_P(Z)=3,                                (8)
```

where `Z=V(P)\(L∪X)`. The sets `L,X` are anticomplete, each dominates
the complement of the other, and they are the only feasible unit triples
for an integral 2-packing. Thus both are exact terminal conflict `K₃`
supports with zero partition-additivity defect.

### Probabilistic construction

For every `P_L∈binom(L,2)` and `P_X∈binom(X,2)`, take `N` vertices of
type `W_{P_L,P_X}`, adjacent deterministically to exactly
`P_L∪P_X` among `L∪X`. For every `(p,q)∈[3]²`, take `N` vertices of
type `Y_{p,q}`, adjacent deterministically to `ℓ_p,x_q`. Put independent
probability-`1/2` edges among the resulting `18N` vertices `Z`, and add no
other edges.

With positive probability both events hold:

1. every triple other than `L` and `X` lies in a closed neighborhood;
2. every set of at most four vertices containing neither all of `L` nor all
   of `X` misses a vertex in some `Y_{p,q}` block.

For a fixed nonexceptional triple, choose a compatible `W` type. At least
`N-3` unused copies catch its `Z` coordinates independently with
probability at least `1/8`, so failure is at most `(7/8)^{N-3}`. For a
fixed set of at most four vertices, choose `p,q` absent from its `L,X`
coordinates. At least `N-4` unused `Y_{p,q}` vertices avoid its selected
`Z` coordinates independently with probability at least `1/16`, so failure
is at most `(15/16)^{N-4}`. A union bound over triples and four-sets tends
to zero. For example `N=1000`, with `n=18006`, makes

```text
binom(n,3)(7/8)^997 < 1.5·10^-46,
(Σ_{j=0}^4 binom(n,j))(15/16)^996 < 5.4·10^-13.
```

The first event makes every pair have a common-neighborhood witness and
makes `L,X` the only feasible unit triples. Hence `ρ=1` and `R=3`.
The second event rules out a four-vertex dominator; a set containing all of
one distinguished triple plus only one other vertex misses a vertex of the
opposite triple deterministically. Five vertices suffice, for example `L`,
one `W` vertex covering two members of `X`, and the remaining member of
`X`. The same `Y`-block argument rules out two-vertex dominators of the
targets in (8), while `L` or `X` supplies the upper bounds. The deterministic
incidences connect every core vertex through `Z`, so the graph is connected.

Thus some finite outcome has all the asserted exact properties. Random
sampling is only an existence proof, not a certificate or finite-verification
claim.

## Exact lift obstruction

Suppose a component `C` of a full-zero-defect Steiner product is isomorphic
to `P`. Componentwise calibration gives one triangle and no singleton atom
in `L_i∩C`. Since `L,X` are the only feasible unit triples, every such
terminal support is one of them. The common core `Z` is therefore avoided by
all `L_i`.

Now `γ_C(Z)=3` and projection equality gives

`|D_{i,C}|=Γ_C-R_C+r_C=5-3+1=3`.

Equation (3) forces `3|π_i|≤3`, so every cell is a singleton. Hence
`|V(H)|=γ(H)`, forcing `H` to be edgeless. But then no nonempty singleton
cell can be vertically dominated from another coordinate, contradicting the
triangle in every `L_i`.

Therefore **no full-zero-defect Steiner product can contain this primitive
as a connected component**.

More generally, take `z` copies of `C₄` and `τ` copies of `P`. Then

```text
Γ=2z+5τ,       r=z+τ,       R=2z+3τ,
γ_G(V\L_i)=z+3τ,       |D_i|=z+3τ+p_i.
```

The union of the `τ` common cores has domination number `3τ`, so a cell of
size at least two forces

`p_i≥3τ-z`.                                                  (9)

At Steiner's formal ratios,

```text
z/Γ=3a-2b,       τ/Γ=2(b-a),
(3τ-z)/Γ=8b-9a=(11√73-89)/24>0.                           (10)
```

Thus the natural componentwise-calibrated mixture cannot lift at zero
defect either.

For the same mixture, (6) gives only

```text
E≥ceil((3τ-z)/2),
E/(Γγ(H))≥(11√73-89)/(48γ(H))+o(1).                        (11)
```

The induced normalized improvement is
`(11√73-89)/(192γ(H))`, which vanishes when `γ(H)` grows.
Therefore support avoidance alone is a **universal-constant STOP** despite
its exact zero-defect exclusion. A constant improvement needs an additional
theorem charging an occupied avoided row in linearly many cells, via the
coordinate holes left by its row labels.

## Verdict and next bridge

The primitive shows that factor-level triangle structure is genuinely
realizable; the coordinate tax shows that its most symmetric role-switching
realization cannot occur in an equality product. The missing universal
step is now precise:

> Prove that every `(5,1,3)` equality component either forces a hard
> coordinate hole in linearly many cells, or pays a product-scale
> packing/additivity/projection defect.

Merely finding a common avoided set is no longer enough: (11) shows that its
one-time vertical repair can be reused. The missing lemma must prevent that
reuse at product scale.

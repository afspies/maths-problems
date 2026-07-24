# Four-region overlap tax

## Status

**Exact two-energy identity and multiplicity decomposition proved and
independently audited twice at GPT-5.6 Sol xhigh effort.** The row and
column fractional repair ledgers can be added, provided one subtracts an
explicit overlap tax supported on selected nonisolated cells and cells
receiving open-coordinate imports from both directions.

This locates the precise combinatorial obstruction behind the sharp
directional maximum in the earlier charging theorem. The audit also
recovers cardinality slacks that the earlier statement unnecessarily
discarded. It does not yet improve the universal constant: minimum
dominators of `K₂□K₂` and `P₃□P₃` make every scalar strengthening sharp.

## Four regions

Let `A⊆V(G)×V(H)` and put `M=|A|`. Use

```text
A_g={h:(g,h)∈A},                 B_h={g:(g,h)∈A},
C_g=H\⋃_{x∈N_G(g)}A_x,           D_h=G\⋃_{y∈N_H(h)}B_y.
```

The neighborhoods in these definitions are open. Thus `(g,h)` lies in
`C_g` exactly when it receives no horizontal import, and it lies in `D_h`
exactly when it receives no vertical import.

As subsets of the product, define

```text
C={(g,h):h∈C_g},          D₀={(g,h):g∈D_h},
I=A∩C∩D₀,
W=(C∩D₀)\A,
J=(G□H)\(C∪D₀).
```

Here:

- `I` consists of selected cells isolated in both fixed-coordinate fibres;
- `W` consists of genuinely missed cells;
- `J` consists of cells receiving both a horizontal and a vertical open
  import.

If `A` dominates the product, then `W=∅`.

## Exact identity

Let `q,p` be fractional packings on `G,H`, with totals `Q,P`, and write

`w(g,h)=q_gp_h`.

Retain the terms

```text
Z=Σ_{(g,h)∈A}(1-q_g)(1-p_h),
E_H=Σ_gq_g[γ_H(C_g)-p(C_g)],
E_G=Σ_hp_h[γ_G(D_h)-q(D_h)].
```

The two typed-feasibility slacks are

```text
α_H=Σ_gq_g[|A_g|-γ_H(C_g)],
α_G=Σ_hp_h[|B_h|-γ_G(D_h)].
```

Finally put

`K=w(A\I)+w(J)`.

Then the following is an identity for every `A`:

```text
M
=PQ+Z+E_H+E_G+α_H+α_G-K+w(W).                              (1)
```

For typed-feasible `A`, the strongest immediate directional consequence is

```text
M≥PQ+Z+max{E_H+α_H,E_G+α_G}.                                (2)
```

This corrects the earlier statement, which retained only
`max{E_H,E_G}`. For an actual product dominator equation (1) has `w(W)=0`.

### Proof

The row terms telescope as

```text
E_H+α_H
=Σ_gq_g[|A_g|-p(C_g)]
=Σ_{(g,h)∈A}q_g-w(C).
```

Symmetrically,

`E_G+α_G=Σ_{(g,h)∈A}p_h-w(D₀)`.

Also

`PQ=w(G□H)`

and

`Z=M-Σ_Aq_g-Σ_Ap_h+w(A)`.

Adding gives

```text
PQ+Z+E_H+E_G+α_H+α_G
=M+w(G□H)+w(A)-w(C)-w(D₀).
```

Since

```text
w(G□H)-w(C)-w(D₀)
=w(J)-w(C∩D₀)
```

and `C∩D₀=I⊔W`, while `A=I⊔(A\I)`, the right side is

`M+w(A\I)+w(J)-w(W)`.

Rearranging proves (1).

## Multiplicity identity

For a cell `z`, let `m(z)` be its total number of selected owners: self
selection plus all horizontal and vertical open owners. Let `t(z)` retain
only existence in each channel:

```text
t(z)=1_A(z)
     +1_{z has a horizontal owner}
     +1_{z has a vertical owner}.
```

Put

```text
R=Σ_z w(z)[m(z)-t(z)],
Δ=Σ_{(g,h)∈A}{
    p_h[1-q(N_G[g])]
   +q_g[1-p(N_H[h])]
  }.
```

Both terms are nonnegative. The first counts repeated same-direction
owners beyond the first; the second is the packing-load slack at selected
owners. Exact double counting gives

```text
2(M-PQ-Z)
=E_H+E_G+α_H+α_G+R+Δ.                                      (3)
```

Indeed, summing `w` over all owner incidences gives

```text
Σ_z w(z)m(z)
=Σ_{(g,h)∈A}[
 p_hq(N_G[g])+q_gp(N_H[h])-q_gp_h
]
=M-Z-Δ.
```

The one-axis identities refine (3) separately:

```text
M-PQ-Z=E_H+α_H+S_H
      =E_G+α_G+S_G,
S_H,S_G≥0,
S_H+S_G=R+Δ.                                                (4)
```

Equation (2) follows. Thus the averaged consequence of (3) is not stronger
than the corrected directional maximum; the new content is the exact
equality/stability decomposition.

For an actual dominator, `t(z)≥1` and

`K=Σ_z w(z)[t(z)-1]`.

Combining this with (1) and (3) yields

`E_H+E_G+α_H+α_G=2K+R+Δ`.                                  (5)

Thus the overlap tax, repeated-owner mass, and packing-load slack account
for the entire two-direction repair ledger.

## Coverage-redundancy interpretation

For an actual product dominator, let `r_G(z),r_H(z)` be the numbers of open
horizontal and vertical owners of a cell `z`, and let `a(z)=1_A(z)`. Its
total domination redundancy is

`R₀(A)=Σ_z[a(z)+r_G(z)+r_H(z)-1]`.

Pointwise case analysis gives the exact unweighted decomposition

```text
R₀(A)=Ω_G+Ω_H+|A\I|+|J|,                                   (6)
```

where

`Ω_G=Σ_z(r_G(z)-1)_+`

and symmetrically for `Ω_H`. Thus `K` is the rank-one-weighted core of the
coverage redundancy left after repeated same-direction imports have been
removed. If `q_g≤s` and `p_h≤t`, then

`K≤st[R₀(A)-Ω_G-Ω_H]`.                                      (7)

Equation (6) also explains why `K=0` for a perfect dominating code.

## Sharp minimum-dominator obstructions

### `K₂□K₂`

Take the antidiagonal, and put weight `1/2` on each factor vertex. Then

```text
PQ=1,  Z=1/2,
E_H=E_G=1/2,
α_H=α_G=0,
K=1/2.
```

The two selected cells lie in `I`; the two unselected diagonal cells form
`J`. Equation (1) gives `M=2`. Thus `K=min{E_H,E_G}`, while
`R=Δ=0`.

### `P₃□P₃`

Take the minimum dominator

`A={(0,0),(1,2),(2,1)}`

and the optimal factor packings `q=p=(0,0,1)`. Then

```text
PQ=1,  Z=1,
E_H=E_G=1,
α_H=α_G=0,
I=A,
J={(1,1),(2,2)},
K=1.
```

Again `K=min{E_H,E_G}`, and (1) gives `M=3`. Hence minimum product
domination, optimal factor duals, and exact typed cardinality
complementarity do not imply a strict bound

`K<(1-ε)min{E_H,E_G}`.

The concentrated witness

```text
A={(0,1),(1,0),(1,3),(2,3),(3,1)}⊂P₄□P₄,
q=p=(1,0,0,1)
```

has `E_H=E_G=K=1` as well, though this five-set is not minimum.

There is also a sharp warning that the `α` terms must be retained. In
`P₃□P₃`, take

```text
A={(0,1),(2,0),(2,2)},     q=p=(0,0,1).
```

This is a minimum dominator and

```text
PQ=1, Z=1, E_H=E_G=0, α_H=1, α_G=0.
```

The corrected bound (2) gives `M=3` exactly, whereas the earlier
`max{E_H,E_G}` statement gives only two.

## Surviving bridge

The identities repair the invalid sum-of-energies step exactly and sharpen
the directional inequality by restoring `α_H,α_G`. A universal improvement
requires structure absent from the sharp singleton-supported examples.
Session seven's provider construction shows that the changing indexed
`K₁/K₃` systems alone still do not suffice: one point can serve arbitrarily
many exact terminal triangles while every per-index overlap tax vanishes.

**GO** only for a defect-weighted triangle/index estimate using the full
balanced incidence geometry. **STOP** for a generic strict overlap bound
based only on minimum domination, typed feasibility, optimal factor
packings, or independent per-index taxes.

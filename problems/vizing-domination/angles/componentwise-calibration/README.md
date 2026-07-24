# Componentwise calibration of Steiner equality

## Status

**Proved and independently accepted by GPT-5.6 Sol at xhigh effort.**
The global equality skeleton cannot hide cancellations between connected
components. Every component lies on the exact line

`3ρ^{\{2\}}(C)=γ(C)+4ρ(C)`.

This reduces the formal obstruction to singleton primitives
`(γ,ρ,ρ²)=(2,1,2)` and triangle primitives `(5,1,3)`. It is a classification
of the equality mechanism, not a universal constant improvement.

## The theorem

Let `C` be a connected component of `G`, and abbreviate

```text
Γ_C=γ(C),   r_C=ρ(C),   R_C=ρ^{\{2\}}(C).
```

Assume the full equality conditions in the oriented Steiner argument:

- `v=0`;
- `p_i=d_i=δ_i=0` for every partition cell `i`; and
- the terminal burden `B_i=0`, so the canonical ordinary and integral
  2-packings supported on `L_i` are globally optimal and every terminal
  conflict component is `K₁` or `K₃`.

Then, for every cell `i`, there are integers `z_C,τ_C`, independent of `i`,
such that `L_i∩C` has `z_C` singleton and `τ_C` triangle atoms, with

```text
z_C=3r_C-R_C,             τ_C=R_C-2r_C,
|L_i∩C|=2R_C-3r_C,        γ_C(L_i∩C)=R_C-r_C,              (1)
|D_i∩(C×π_i)|=|X_i∩C|=Γ_C-R_C+r_C.                         (2)
```

Moreover,

`3R_C=Γ_C+4r_C`.                                             (3)

Equivalently,

```text
Γ_C=2z_C+5τ_C,   r_C=z_C+τ_C,   R_C=2z_C+3τ_C.             (4)
```

## Proof

Packing and domination parameters are additive over connected components.
The canonical packing on `L_i` has global values `r=Σ_Cr_C` and
`R=Σ_CR_C`. Its restriction to `C` is feasible and has value at most the
corresponding component optimum. Equality of the sums therefore forces
equality in every component. The `K₁/K₃` atom equations are

```text
z_C+τ_C=r_C,          2z_C+3τ_C=R_C,
```

which give (1).

The additivity defect `d_i` is a sum of nonnegative component defects.
Thus `d_i=0` gives

`γ_C(V(C)\L_i)+γ_C(L_i)=Γ_C`.                                (5)

For the projection statement, put

```text
D_{i,C}=D_i∩(C×π_i),       X_{i,C}=P_G(D_{i,C}).
```

In every component,

`γ_C(V(C)\L_i)≤|X_{i,C}|≤|D_{i,C}|`.

The global equality `p_i=0` makes the sums of the three quantities equal,
so equality holds componentwise. Combining with (1) and (5) proves (2).

Finally `v=0` makes Steiner's row inequality exact at every vertex `g`.
Projection injectivity from `p_i=0` identifies the occupied-cell count with
`#{i:g∈X_i}`. Hence

`#{i:g∈L_i}=#{i:g∈X_i}`.                                    (6)

Sum (6) over `g∈C` and use (1)--(2):

`k(2R_C-3r_C)=k(Γ_C-R_C+r_C)`.

This is (3), and solving the two atom equations gives (4).

## Consequences and limitation

A component with `τ_C=0` is built numerically from the singleton primitive
`(2,1,2)`. A component with one triangle and no singleton atoms has exactly
`(5,1,3)`. Thus the only genuinely new local object needed at equality is a
connected triangle primitive.

The familiar disconnected calibration by isolated vertices, `C₅`s, and
dense graphs does not satisfy (3) componentwise. It remains a valid
factor-invariant no-go away from full product equality, but it is not an
equality skeleton for the oriented product proof.

The theorem does **not** say that every `(5,1,3)` component has the same
terminal triples, nor that such components are impossible. The
product-coordinate obstruction for one exact primitive family is developed
in `angles/neutral-core-coordinate-tax`.

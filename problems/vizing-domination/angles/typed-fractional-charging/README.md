# Fractional charging of typed fibres

## Status

**Exact label-correlated inequality proved and independently audited by
GPT-5.6 Sol at xhigh effort, then sharpened in session seven by restoring
the typed cardinality slacks.** The energy terms measure the failure of row
and column repair sets to be packing-saturated exact-one covers. They are
the first fractional certificate in this campaign that survives the
asymmetric Cayley obstruction because they depend on the actual fibre
labels.

The scalar cap corollary is only the known rank-one product packing and is a
STOP. The live term is the quantized repair energy.

## Correlated charging theorem

Let `A⊆V(G)×V(H)` be typed-feasible and put `M=|A|`. Let `q,p` be
fractional packings on `G,H`, with totals `Q,P`. Write

```text
A_g={h:(g,h)∈A},            V_g=⋃_{x∈N_G(g)}A_x,
C_g=V(H)\V_g,
B_h={g:(g,h)∈A},            U_h=⋃_{y∈N_H(h)}B_y,
D_h=V(G)\U_h.
```

Define

```text
Z_A(p,q)=Σ_{(g,h)∈A}(1-q_g)(1-p_h),
E_H=Σ_g q_g[γ_H(C_g)-p(C_g)],
E_G=Σ_h p_h[γ_G(D_h)-q(D_h)].
α_H=Σ_g q_g[|A_g|-γ_H(C_g)],
α_G=Σ_h p_h[|B_h|-γ_G(D_h)].
```

Then

```text
M≥PQ+Z_A(p,q)+max{E_H+α_H,E_G+α_G}.                         (1)
```

All four correction terms are nonnegative for a typed-feasible set. The
earlier session-six statement discarded `α_H,α_G`; the corrected form is
strictly stronger.

### Exact proof identity

Put

```text
a_g=|A_g|,
r_x=p(A_x),
o_g=Σ_{x∈N_G(g)}r_x-p(V_g),
σ_q(x)=1-q(N_G[x]).
```

Weighted union subadditivity and fractional packing give `o_g,σ_q(x)≥0`.
Direct double counting gives

```text
L:=Σ_{(g,h)∈A}(q_g+p_h-q_gp_h)-PQ
 =Σ_g q_g[a_g-p(C_g)+o_g]+Σ_x r_xσ_q(x).                   (2)
```

Typed feasibility and weak packing duality give

`a_g≥γ_H(C_g)≥p(C_g)`.

Splitting

```text
a_g-p(C_g)
=[a_g-γ_H(C_g)]+[γ_H(C_g)-p(C_g)]
```

shows that (2) implies `L≥α_H+E_H`; the symmetric identity implies
`L≥α_G+E_G`. Finally, pointwise,

`1=(q_g+p_h-q_gp_h)+(1-q_g)(1-p_h)`,

so `M=PQ+L+Z_A`, proving (1).

The maximum in (1) is sharp. On the antidiagonal in `K₂□K₂`, with both
packings uniform one-half,

`L=E_H=E_G=1/2` and `α_H=α_G=0`.

Thus no sum of the two corrected directional ledgers is available without
another product-specific term. The exact overlap and multiplicity
decomposition is in `../overlap-tax/README.md`.

## Exact meaning of the repair energy

Let `p` be a fractional packing on a graph `K`, let `C⊆V(K)`, and let
`T` be a minimum dominator of `C`. Then

```text
γ_K(C)-p(C)
 =Σ_{t∈T}[1-p(C∩N[t])]
  +Σ_{v∈C}p_v(|T∩N[v]|-1).                                 (3)
```

Both sums are nonnegative. Hence equality holds precisely when

1. every repair owner is `p`-saturated on the remaining target set; and
2. every positive-`p` target is covered exactly once by the repair.

If `p=f/2` for an integral 2-packing `f`, the gap in (3) is
half-integral. Every failure therefore costs at least `1/2`.

Equality in the full row identity additionally forces:

- `a_g=γ_H(C_g)` on every `q`-positive row;
- zero positive-`p` overlap among neighboring imported fibres; and
- `q(N_G[x])=1` whenever `p(A_x)>0`.

The symmetric conditions hold in columns. These are exactly the
packing-saturated exact-one repairs that can be compared with the existing
`K₁/K₃` terminal atoms.

## Terminal triangle parity and provider charge

Let `S⊆V(H)` be a terminal equality set whose conflict graph has `z`
singleton atoms and `τ` triangle atoms. Use its canonical half-2-packing
`p`: weight one on a singleton target, one half on each triangle target,
and zero outside `S`.

For every `C⊆V(H)`,

```text
γ_H(C)-p(C)
 ≥γ_H(C∩S)-p(C∩S)
 =(1/2)·#{triangle atoms T: |C∩T| is odd}.                  (4)
```

The first inequality uses that `p` is supported on `S`. Domination is
additive across the conflict components. A triangle intersection of size
`0,1,2,3` has domination-minus-packing gap `0,1/2,0,1/2`.

For typed rows `C_g=H\V_g` and any fractional packing `q` on `G`,

`Z_A(p,q)+E_H≥τQ/2`.                                        (5)

Fix a triangle `T`. If `|C_g∩T|` is odd, charge `q_g/2` to (4).
Otherwise `|V_g∩T|` is odd and nonzero. The total `q`-mass of rows
importing a label of `T` is at most

```text
Σ_x 1[A_x∩T≠∅] q(N_G(x))
≤Σ_{(x,h)∈A,h∈T}(1-q_x)
=2Z_T.
```

Summing the parity alternatives over the `τ` triangles proves (5).

This exact charge is too small to close the formal obstruction. At the
formal values

```text
a=(11-√73)/8,
b=(13-√73)/12,
τ/γ(H)=2(b-a),
Q/γ(G)=b,
```

equations (1) and (5) give only

```text
M/[γ(G)γ(H)]
 ≥b²+b(b-a)
 =b(2b-a)
 =(10-√73)/9
 ≈0.16178.
```

The exact missing coefficient to Steiner is

`c-b(2b-a)=(11√73-65)/72≈0.40255`.

The row and column triangle charges cannot be added because they consume
the same slack `L`; the `K₂□K₂` and `P₃□P₃` fixtures make the maximum in
(1) sharp. Thus atom parity alone is a STOP. A successful strengthening
must stop the same selected provider from serving many fibre-indexed
triangle systems, or rule out the large `(q,p)=(0,0)` mass that remains in
the formal scalar ledger.

## Cap corollary and its limit

If `q_g≤s` and `p_h≤t`, then

`Z_A≥M(1-s)(1-t)`.

Consequently

```text
M≥[PQ+max{E_H+α_H,E_G+α_G}]/(s+t-st).                       (6)
```

Discarding the energy gives

`M≥PQ/(s+t-st)`.                                             (7)

The subtraction `st` corrects the earlier weaker `s+t` envelope, but (7)
is not a new universal route. It is exactly the rank-one product fractional
packing with local load

`p_hq(N_G[g])+q_gp(N_H[h])-q_gp_h`.

For uniform packings on closed-neighborhood-regular factors, it is the
`n_Gn_H/(R_G+R_H-1)` product term already present in `Ξ`, and the
asymmetric Cayley family sends its normalized value to zero. The new
content is the label-correlated repair energy and typed cardinality slack.

## Cover-resilience arm

Define the global domination resilience

`σ(K)=min_{0≤t<γ(K)} u_K(t)/(γ(K)-t)≥1`.                     (8)

For every `V⊆V(K)`,

`γ_K(K\V)≥γ(K)-|V|/σ(K)`.                                   (9)

Indeed, a minimum dominator of `K\V` leaves an undominated hole contained
in `V`, and (6) bounds that hole.

If `q` is a fractional packing on `G`, with total `Q` and cap
`s=max q_g`, then every typed-feasible `A` satisfies

`M≥σ(H)γ(H)Q/[1+(σ(H)-1)s]`,                               (10)

and symmetrically. To prove (8), (7) gives

`σ(H)a_g+|V_g|≥σ(H)γ(H)`.

Multiply by `q_g`, sum, use the open-neighborhood packing bound, and then
`Σ_gq_ga_g≤sM`.

This scalar arm is useful for resilient graph classes but is not the main
universal target: `σ(K)=1` whenever some minimum dominator has a
self-private vertex. The row-dependent energy in (1) remains meaningful
when the global minimum in (6) is spoiled by one exceptional dominator.

## Three-layer repair consequence

Choose row repairs `R_g` of `C_g` and column repairs `S_h` of `D_h`, with
total masses at most `M`, and set

`m=1_A+1_R+1_S`

as an integer multiset on `G□H`. Every cell `z` satisfies

`m(N[z])≥2+1_A(z)`.                                        (11)

The first unit comes from a row repair or a horizontal `A`-owner; the
second comes from a column repair or a vertical `A`-owner. If both come
from `A`, the two open coordinate directions are distinct. Other
coincidences remain distinct multiset occurrences.

Thus, for every fractional product packing `W`,

`3M≥2W(V(G□H))+W(A)`.                                      (12)

This is a useful exact equality diagnostic but a universal STOP by itself:
it only constructs a structured integer 2-dominating function.

## Sharp examples

The new inequality is exact on all mandatory tests, for different reasons.

1. On the `C₅□C₅` perfect code with uniform one-third packings,

   `PQ=25/9`, `Z=20/9`, and `E_H=E_G=0`, giving `M=5`.
2. On the typed but non-dominating diagonal in `C₄□C₄`, uniform
   one-third packings give

   `PQ=Z=16/9`, `E_H=E_G=L=4/9`, giving `M=4`.
3. On the strict `(K₂⊔K₁)^2` typed witness, the packing
   `(1/2,1/2,1)` in each factor gives

   `PQ=4`, `Z=E_H=E_G=0`.

The last example confirms that equality in (1) does not secretly recover
product domination.

## Verdict

**GO** for combining the half-integral quantization in (3) with the
simultaneous `K₁/K₃` terminal classification. Near equality forces
packing-saturated exact-one repairs in every relevant row and column, plus
disjoint imported packing support and saturated owner neighborhoods.

**STOP** for the cap denominator alone, the global one-number resilience
parameter alone, adding `E_H+E_G`, or the three-layer repair alone.

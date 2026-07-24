# Handoff — Vizing’s domination conjecture

Read these session-six notes first:

- `angles/typed-fibre-relaxation/README.md`
- `angles/typed-partial-cover/README.md`
- `angles/typed-fractional-charging/README.md`
- `angles/isolation-escape-charging/README.md`
- `angles/corner-dynamics/README.md`
- `angles/incidence-balance/README.md`

The best universal constant remains

`c=(5+√73)/24≈0.5643`.

The withdrawn `0.5809` claim is not a theorem and was not used.

## Decisive session-six theorems

### 1. Two-axis near-cover profile

For

`u_K(t)=min_{|C|≤t}|V(K)\N_K[C]|`,

every row-typed incidence set `A`, with row masses `a_g` and column masses
`b_h`, satisfies

`Σ_g u_H(a_g)+Σ_hu_G(b_h)≤|G||H|`.                          (1)

The exact defect identity is

```text
|G||H|-Σ_gu_H(a_g)-Σ_hu_G(b_h)
=Σ_g(|V_g|-u_H(a_g))
 +Σ_h[|G|-u_G(b_h)-|N_G[B_h]|]
 +Σ_h|B_h\N_G^open(B_h)|.
```

The final term is induced-fibre isolation. On the `C₅□C₅` perfect code,
all five units of slack are isolation.

For `d`-regular `G`,

`Θ(G,H)≥|G|(t+1)u_H(t)/[u_H(t)+d(t+1)]`.                    (2)

There is also a fractional-packing-weighted version in the angle note.

### 2. Robust Cayley benchmark cleared

A new robust adaptation of the Newman/Bollobás--Janson--Riordan random-set
argument gives connected Cayley graphs on `F₂^m`, with

```text
n=2^m,
k=floor(n/m²),
q=n/k,
ℓ=log k,
t*=floor(q(ℓ-10 log ℓ)),
L=floor(ℓ⁶),
u(t*)>L,
t*<γ≤q(ℓ+1).
```

Equation (2) proves

`Θ(G,H)/(γ(G)γ(H))→∞`

for every pair of growing graphs from this robust family, regardless of
relative scale. If one factor is fixed, the liminf is at least
`|G|/γ(G)≥1`.

Thus the asymmetric Cayley construction that drives `Ξ` to zero is a hard
PASS for `Θ`, not an obstruction.

Do not claim that the global minimum

`min_{t<γ}u(t)/(γ-t)`

is large. The construction leaves an `o(γ)` final window where a singleton
private set could make it one.

### 3. Correlated fractional repair energy

For factor fractional packings `q,p`, totals `Q,P`, define

```text
C_g=H\V_g,       D_h=G\U_h,
Z=Σ_{(g,h)∈A}(1-q_g)(1-p_h),
E_H=Σ_gq_g[γ_H(C_g)-p(C_g)],
E_G=Σ_hp_h[γ_G(D_h)-q(D_h)].
```

Then exactly

`|A|≥PQ+Z+max{E_H,E_G}`.                                    (3)

For a minimum dominator `T` of a target `C`,

```text
γ(C)-p(C)
=Σ_{t∈T}[1-p(C∩N[t])]
 +Σ_{v∈C}p_v(|T∩N[v]|-1).
```

Hence zero energy means packing-saturated repair owners and exact-one
coverage of every positive-packing target. For half of an integral
2-packing, every failure costs at least `1/2`.

The maximum in (3) is sharp; `E_H+E_G` is false. The cap-only consequence
has denominator `s+t-st`, but the formal-ratio counterfamily still bounds it
by

`(-247+37√73)/132≈0.523698<c`.

### 4. Terminal triangle provider charge

For a terminal `K₁/K₃` equality set with `τ` triangle atoms and its
canonical half-2-packing,

`Z+E_H≥τQ/2`.                                                (4)

Odd remaining-target intersection with a triangle charges `E_H`; even
intersection forces an odd imported provider and charges `Z`.

This is rigorous but far too weak. At the formal ratios (4) plus (3) gives
only

`b(2b-a)=(10-√73)/9≈0.16178`,

leaving `(11√73-65)/72≈0.40255` to Steiner. Row and column charges
cannot be added. **STOP** for local atom parity alone.

The missing provider theorem must use the fact that the terminal triangle
systems vary with the fibre index. A single selected label should not be
allowed to pay for arbitrarily many independent odd-import demands without
creating collision, separation, or private-target slack.

### 5. Isolation-to-escape density

For a product dominator, let `I_G` count selected points isolated in their
fixed-label `G`-fibres. Put

```text
r_{x,h}=|N_G(x)∩B_h|,
Ω_G=Σ_{x,h}(r_{x,h}-1)_+,
X_H=Σ_x|V_x∩N_H[A_x]|.
```

If `Bad_G⊆I_G` lacks horizontal external-private neighbors, then

`|Bad_G|≤2Ω_G+X_H`.                                         (5)

When both factors have no isolates, the number `T` of fibre-isolated points
with external private neighbors in both directions satisfies

```text
|T|≥[
 I_G+I_H-|D|
 -2Ω_G-2Ω_H-X_H-X_G
]_+.                                                        (6)
```

Every point of `T` carries the labelled `(1,2)` or `(2,1)` private-corner
escape obligation. Equation (6) is exact on the `C₅□C₅` 5-cycle and
`K₂□P₃` 2-cycle.

Escape density is not yet cycle density. Owners can leave `T`, and bounded
indegree permits arbitrarily long in-trees.

## Best next attacks

### A. Provider non-reuse across fibre indices

At formal equality, every Steiner fibre has fixed singleton/triangle atom
counts, but the supported optimal 2-packing changes with the fibre index.
Use the balanced red/blue cell matrices, column separation, and
private-target injection to show that one selected coordinate cannot provide
the odd-import alternative in (4) for too many indexed triangles.

A useful theorem must recover a product-scale term. Another local parity
count is a STOP.

### B. Escape closure or path length

Iterate the labelled red-diagonal/blue-cross-zero transition from every
point counted by (6). Prove one of:

1. a positive fraction of owners remain inside `T`;
2. every escape path returns to `T` after bounded length; or
3. each departure charges a fresh `Ω`, `X`, terminal, projection, or
   partition-additivity defect.

The third option aligns best with the exact Steiner slack identity.

### C. Profile-isolation coupling

Equation (1) alone permits a fictitious mass three on `C₄□C₄`, while
exact typed enumeration gives four. The missing information is precisely
the location of isolated fibres. Seek a Hall/matching statement coupling
row and column isolation before passing to scalar masses.

## Hard stops

- No numerical reoptimization of Steiner's six existing inequalities.
- No additive `k`-packing hierarchy.
- No saturation-defect or anchored-deficit campaign.
- No cap correction by itself; `s+t-st` is already accounted for.
- No full `Λ`, combined `Ξ`, or averaged factor-dominator lift.
- No global-resilience claim for the random Cayley family.
- No local `K₁/K₃` parity-only argument.
- No bare escape count, cycle existence, or bounded-indegree argument.
- Finite tests remain hygiene and falsification only.

Any proposed provider-reuse or escape-closure proof requires a fresh
independent GPT-5.6 Sol xhigh audit.

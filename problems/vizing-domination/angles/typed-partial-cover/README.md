# Typed partial-cover profiles

## Status

**Two exact labelled inequalities and a robust Cayley calibration proved;
independently audited by GPT-5.6 Sol at xhigh effort.** The partial-cover
profile retains how many vertices remain uncovered by a prescribed number of
closed neighborhoods. This is precisely the information lost by domination
number and by the zero-factor marginal lift `Ξ`.

The profile clears both the asymmetric and comparable-scale random Cayley
families behind the `Ξ` obstruction. It does not prove the universal
conjecture: a `C₄□C₄` scalar relaxation still admits mass three although the
exact typed relaxation has value four.

## Near-cover profile

For a graph `K`, define

`u_K(t)=min_{|C|≤t}|V(K)\N_K[C]|`,                            (1)

for integers `0≤t≤|V(K)|`. Thus `u_K(t)` is the smallest residual
hole after at most `t` closed neighborhoods.

The elementary domination bound

`u_K(t)≥max{γ(K)-t,0}`                                       (2)

follows because `C` together with its uncovered set dominates `K`.
Equality in (2), for `t<γ(K)`, has an exact interpretation: there is a
`t`-set `C` whose hole `Q=V(K)\N[C]` has size `γ(K)-t`, and
`C∪Q` is a minimum dominating set. In particular,

`u_K(γ(K)-1)=1`

if and only if `K` has a minimum dominating set with a self-private vertex.

## Two-axis profile theorem

Let `A⊆V(G)×V(H)` be row-typed feasible. Write

```text
A_g={h:(g,h)∈A},                 a_g=|A_g|,
B_h={g:(g,h)∈A},                 b_h=|B_h|,
V_g=⋃_{x∈N_G(g)}A_x,
```

where `N_G(g)` is open, and assume

`a_g≥γ_H(V(H)\V_g)`                                        (3)

for every row. Then

`Σ_g u_H(a_g)+Σ_h u_G(b_h)≤|G||H|`.                         (4)

This already uses both coordinate systems, although only (3) is assumed.
Indeed, (3) supplies an `a_g`-set whose uncovered set lies in `V_g`, so

`u_H(a_g)≤|V_g|`.

Counting imported labels by columns gives

```text
Σ_g|V_g|
 =Σ_h|N_G^open(B_h)|
 ≤Σ_h|N_G[B_h]|
 ≤Σ_h(|G|-u_G(b_h)),
```

which is (4). Every typed-feasible set, and hence every product dominating
set, satisfies it.

### Exact defect identity

Define

```text
r_g=|V_g|-u_H(a_g),
ι_G(B)=|B\N_G^open(B)|,
e_G(B)=|G|-u_G(|B|)-|N_G[B]|.
```

All three quantities are nonnegative, and the proof above is the exact
identity

```text
|G||H|-Σ_g u_H(a_g)-Σ_h u_G(b_h)
 =Σ_g r_g+Σ_h e_G(B_h)+Σ_h ι_G(B_h).                        (5)
```

There is a symmetric identity using the column typed conditions. Equality
therefore forces every import set to attain the near-cover profile, every
column fibre to be an optimal partial cover, and every nonempty induced
column fibre to have no isolate. Applying both orientations forces occupied
alternating walks.

The isolation term is essential. For the perfect code

`A={(g,2g):g∈Z₅}⊂C₅□C₅`,

`u_C₅(1)=2`; the left side of (5) is five, `r=e=0`, and all five
units are the isolated column fibres. They circulate around the known
mixed `(1,2)` escape 5-cycle.

## One-sided quantitative bound

Let `G` be `d`-regular on `n_G` vertices and let `A` be typed-feasible of
mass `M`. For every integer `t`,

`M≥n_G(t+1)u_H(t)/[u_H(t)+d(t+1)]`.                          (6)

Rows of mass at most `t` must import at least `u_H(t)` labels. At most
`M/(t+1)` rows are heavier, while

`Σ_g|V_g|≤dM`.

Thus

`u_H(t)(n_G-M/(t+1))≤dM`,

which rearranges to (6).

There is a weighted version. If `q` is a fractional packing on `G`, with
total `Q` and cap `s=max q_g`, then

```text
M≥u_H(t)Q /
  [1+s max{u_H(t)/(t+1)-1,0}].                              (7)
```

For closed-neighborhood-regular `G`, the uniform packing in (7) is exactly
(6).

## Robust random Cayley graphs

The following is a new robust adaptation of the random-translate argument
of Bollobás--Janson--Riordan, not a theorem stated verbatim in their paper.

Let

```text
Q_m=F₂^m,        n=2^m,
k=floor(n/m²),  q=n/k,
ε=m^{-1/2},
t=floor((1-ε)q log k),
L=floor(k^{ε/3}).
```

For all sufficiently large `m`, there is an affinely spanning `k`-set
`S⊆Q_m`, containing zero, such that the connected undirected Cayley graph

`H_m=Cay(Q_m,S\{0})`

satisfies

`u_{H_m}(t)>L`.                                              (8)

To prove existence, choose a Bernoulli `p=k/n` set `S₀`. For fixed
`|T|=t` and an exceptional set `|E|=L`, the event

`T+S₀⊇Q_m\E`

requires `S₀` to meet `n-L` translates of `T`, each of size `t`, with
point multiplicity at most `t`. Newman's hitting estimate, recorded in
Bollobás--Janson--Riordan Remark 4.3, bounds its probability by

`exp(-(n-L)(1-p)^t/t)`.

After union bounding over `T,E`, the negative exponent is

`k^{ε+o(1)}/log k`,

whereas the two entropy terms are `O((log k)^4)` and
`k^{ε/3+o(1)}`. Hence the failure probability tends to zero. Equivalently,
the lower-tail Janson calculation in their proof gives the same separation.

With positive probability `S₀` also has at least `k` points and affinely
spans `Q_m`. Retain an affine basis while deleting to exactly `k` points,
then translate a retained point to zero. Deletion preserves (8), affine
spanning gives connectivity, and exponent two makes the Cayley graph
undirected. Its closed neighborhoods are exactly the translates of `S`.

The greedy translate-cover bound and (8) give

```text
t<γ(H_m)≤q(log k+1),
t/γ(H_m)→1,
L/γ(H_m)→∞.                                                 (9)
```

### Calibration

For every fixed graph `G`, (6) and (9) imply

`Θ(G,H_m)=(1-o(1))|G|γ(H_m)`.                              (10)

The reverse inequality is the all-row construction using one minimum
dominator of `H_m`. Consequently

`Θ(G,H_m)/(γ(G)γ(H_m))→|G|/γ(G)≥1`.

The same profile also handles comparable robust factors. Taking
`G=H=H_m`, (6) gives

```text
Θ(H_m,H_m)
 ≥n(t+1)L/[L+(k-1)(t+1)]
 =(1+o(1))(n/k)L,
```

while `γ(H_m)^2=O((n/k)^2(log k)^2)`. Since

`L/[(n/k)(log k)^2]→∞`,

the profile bound is eventually much larger than
`γ(H_m)^2`.

There is a sharper polynomial version that handles every relative scale.
Write `ℓ=log k`, keep `q=n/k∼ℓ²`, and take

```text
t*=floor(q(ℓ-10 log ℓ)),
L*=floor(ℓ⁶).
```

The same Newman union bound now has negative exponent of order `ℓ⁹`,
while the center-set and exceptional-set entropy terms are respectively
`O(ℓ⁴)` and `O(ℓ⁷)`. Hence one may choose the Cayley set so that

```text
u(t*)>L*,
t*<γ≤q(ℓ+1),
t*/γ→1.                                                     (11)
```

For two growing members `G,H` of this robust family, put
`a=max{log k_G,log k_H}` and `b=min{log k_G,log k_H}`, and orient (6)
so the larger-log factor supplies the profile. The normalized lower bound
has the form

```text
C L*/[L*+d_G(t*+1)],
C=(|G|/γ(G))((t*+1)/γ(H))∼k_G/b.
```

If `L*≥d_G(t*+1)`, this is at least `(1-o(1))k_G/(2b)`.
Otherwise it is at least `(1-o(1))a³/(2b)≥(1-o(1))a²/2`.
Thus

`Θ(G,H)/(γ(G)γ(H))→∞`                                      (12)

for every pair of growing robust-family members, regardless of their
relative scales.

Finally, choose a high-cover-multiplicity Cayley graph `G_j` first and a
robust `H_j` sufficiently farther out. Then the exact transitive formula
from `../combined-blocker-packing/` gives

`Ξ(G_j,H_j)/(γ(G_j)γ(H_j))→0`,

whereas (10) gives

`liminf Θ(G_j,H_j)/(γ(G_j)γ(H_j))≥1`.

Thus the actual labels in `Θ` decisively defeat the mandatory asymmetric
Cayley obstruction.

The global resilience

`min_{t<γ(H_m)}u(t)/(γ(H_m)-t)`

is not controlled by this argument. Equation (11) forces a large ratio up
to `t*`, but a collapse can still occur in the final
`O((log k)²log log k)` centers. In particular, a singleton private set in
some minimum dominator would make the global resilience one. The
single-threshold profile theorem avoids this unproved final-window claim.

## Scalar limitation and next bridge

For `C₄`, `u=(4,1,0,0,0)`. Minimizing only the scalar inequality (4)
allows a hypothetical mass three on `C₄□C₄`, although exact typed
enumeration gives `Θ=4`. The missing term is not another scalar profile:
it is the location of the isolated fibres in (5).

**GO** for charging `ι_G(B_h)` and its row analogue to the labelled
mixed-distance escape owners. **STOP** for treating (4) alone as a universal
proof.

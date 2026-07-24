# Handoff — Vizing’s domination conjecture

Read these session-four notes first:

- `angles/external-private-holes/README.md`
- `angles/bidirectional-blocker/README.md`
- `angles/terminal-capacity/README.md`
- `angles/incidence-balance/README.md`

## What is now proved

1. At full atomic/additive column equality, every
   `x∈X_i=P_G(D_i)` has an external private target
   `y∈V(G)\(L_i∪X_i)`. If `x` were self-private only, optimality of the
   supported 2-packing would produce a saturated witness `w∈N[x]`; replacing
   `x` by `w` and extending `w` through its `K₁/K₃` atom would dominate `G`
   with `γ(G)-1` vertices.
2. If the supported atomic capacity is short of the ambient optimum by
   `Δ=ρ²(G)-τ₂(F_G(L_i))`, the self-private set `S` only satisfies
   `ρ_G(S)≤Δ`. Do not strengthen this to `|S|≤Δ`: opposite vertices in `C₄`
   show that self-private members need not form a two-packing.
3. Fix a product row `y`. If `J` indexes the columns choosing `y` as an
   external private target, `P={a_i:i∈J}` is the set of singleton holes, and
   `e_y=|A_y|-|I_y|` is row slack, then

   `|J|-γ_H(P)≤e_y` and `|J|≤ρ(H)+2e_y`.

   At zero slack, `P` is a two-packing. Summation gives
   `M≤|V(G)|ρ(H)+2v`, and at formal equality
   `|D|≤|V(G)|ρ(H)`. This is rigorous but order-dependent.
4. Symmetric external private targets do not force an undominated corner.
   The perfect dominating code `{(i,2i):i∈Z₅}` in `C₅□C₅` gives an exact
   cycling obstruction.
5. The nonseparable bidirectional blocker lift `Λ(G,H)` satisfies
   `γ(G□H)≥Λ(G,H)≤γ(G)γ(H)` and
   `Λ(G,P₄)=2γ(G)` for every `G`. For vertex-transitive `r,s`-regular
   factors,

   `Λ=max{|G|γ(H)/(r+1),|H|γ(G)/(s+1)}`.

   Hence `L(K_{2m+1})□L(K_{2m+1})` drives its normalized value to `1/2`.
   Pure higher-rank fractional packing is separately blocked by the
   split-graph `□P₄` family.
6. For an ordinary maximum two-packing in `G` and any fractional packing `q`
   on `H`, with total `Q`,

   `Λ(G,H)≥Qγ(G)+ρ(G)Δ_H(q)`,

   where `Δ_H(q)` is the minimum closed-neighborhood saturation deficit over
   a dominating set of `H`. At the formal point, the canonical half-2-packing
   beats Steiner exactly above `Δ_H(q)=(1-b)γ(H)`. `C₅`/split mixtures show
   this is not forced by packing ratios alone. The diffuse alternative
   `γ_f(G□H)≥PQ/(η_p+η_q)` survives those mixtures.

## Best next attacks

### A. Order-free hole coupling

The individual row hole sets are two-packings. Find a constraint on overlaps
between different `P_y` that uses their source columns and the fixed
`K₁/K₃` atoms, rather than summing the trivial per-row bound and introducing
`|V(G)|`. A useful result must charge positive density on the
`Θ(γ(G)γ(H))` scale.

### B. Self-private stability

Under near-tight rather than exact columns, prove a lower bound for
`ρ_G(S_self)` in terms of `|S_self|` using the full terminal packing and
balanced-incidence hypotheses. General minimal dominating sets are too
flexible; the extra `K₁/K₃` geometry must be used.

### C. Defect–diffuseness dichotomy

Prove that a near-formal factor either has an optimized blocker packing with
saturation deficit above the exact threshold, or has a sufficiently diffuse
packing for the fractional tensor bound. The dichotomy must simultaneously
survive:

- the connected split graph against `P₄`, which kills every pure fractional
  certificate; and
- `L(K_{2m+1})□L(K_{2m+1})`, which kills `Λ` alone.

## Hard stops

- No numerical reoptimization of Steiner's existing inequalities.
- No more additive integer packing levels.
- No pure higher-rank fractional packing claim.
- No standalone blocker-lift universal claim.
- No inference that self-private members form a two-packing.
- No symmetric rectangle-corner contradiction without defeating the
  `C₅□C₅` perfect code.
- Finite tests remain falsification and hygiene, never evidence for the
  universal conjecture.

Any proposed proof requires a fresh independent GPT-5.6 Sol xhigh review.

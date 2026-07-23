# The all-involutions subcase (S–M's remaining structured family)

Banked framing, 2026-07-22 session 2. Not yet attacked; recorded so the
next session starts from the right formulation.

## Setting

Faber–Keegan permutation system (their Thm 4 / Cors 5–6; our Lemma 2
before the group specialization): permutations ψ_ij of 56 symbols,
ψ_ji = ψ_ij^{-1}, with ψ_ij, ψ_jk ψ_ij, ψ_ki ψ_ij ψ_jk, and
ψ_lk ψ_ki ψ_ij ψ_jl all fixed-point-free. The perfectness theorem kills
the case "all ψ_ij lie in a common semiregular group". The
Hoffman–Singleton graph (k=7) is assembled from ψ's that are
involutions NOT forming a group (S–M Fig. 5) — so the natural next
structured family is: **all ψ_ij involutions** (ψ_ij = ψ_ji; each
matching is a symmetric pairing of the two blocks' shared label set,
i.e. a perfect matching on the 56 symbols).

## Observations banked (checked, small)

- Parity does NOT give a cheap kill: an FPF involution on 56 symbols is
  28 transpositions = EVEN; on 6 symbols (k=7) it is ODD. So at k=57
  everything lives in A₅₆ and no sign obstruction arises; at k=7 signs
  alternate but FPF-ness is sign-blind. Any obstruction must be finer.
- The perfectness proof machinery dies without associativity of a
  common carrier group: the z_i = x_i·y_i lists are compositions of
  involutions from DIFFERENT matchings; products of two FPF involutions
  are exactly the FPF-ness constraints (T with the reference block),
  i.e. permutations with no cycle of length 1 — the S_t/abelianization
  device has no analogue. Expect this case to be genuinely
  computational, or to need the "larger configuration" ideas at the
  level of the involution graph (which pairs {x, ψ_ij(x)} appear).
- Because HoS EXISTS at k=7 with this shape, any analytic exclusion at
  k=57 must use 56-specific arithmetic (cf. S–M's remark that
  counting arguments must allow k=7 while excluding k=57).
- Search formulation: variables = 1540 perfect matchings on 56 symbols
  (one per block pair), constraints = FPF of the 3- and 4-fold
  products. Symmetry group: S₅₆ relabeling + S₅₆ block permutations —
  enormous; a direct search is hopeless without an equivariant or
  algebraic reduction. Possible reductions: (a) prescribe an
  automorphism as in c19/c7-sat and make the ψ's equivariant;
  (b) restrict to involutions from a single conjugacy class of a
  candidate non-group structure (e.g. a conjugacy class of FPF
  involutions in a chosen subgroup of S₅₆, cf. how HoS's matchings sit
  inside its automorphism group's involutions).

## Next actions (when picked up)

- [ ] Extract from S–M Fig. 5 the exact 21 involutions building HoS
      (k=7): what structure DO they form (conjugacy class? coset?
      union?) — the right generalization target falls out of this.
- [ ] Small-case census at k=7: how many essentially-distinct
      all-involution solutions exist (all should give HoS)? What does
      the solution's symmetry look like under the 4-cycle conditions?
- [ ] Only then decide: analytic angle vs equivariant SAT at 57.

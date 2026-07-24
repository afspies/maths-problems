# Audit of withdrawn arXiv:2607.01109

Mohsen Aliabadi and Elliot Krop, *An improved constant for Vizing's
conjecture*, arXiv:2607.01109v1, claimed the constant 0.5809. Current arXiv
metadata points to v2 and carries the author comment **“Algebraic mistake”**;
the current PDF is unavailable. The archived v1 remains auditable.

The failure is at the transition to equation (2.2) in the proof of Theorem
2.1, before the minimax calculation.

The paper quotes the valid Chen–Piotrowski–Shreve bound

`γ(G□H) ≥ γ(G)ρ(H)+ρ(G)(γ(H)-ρ(H))`.

It sets

`A=γ(G)`, `B=γ(H)`, `x=A-ρ(G)`, `y=B-ρ(H)`.

Therefore `ρ(G)=A-x`, `ρ(H)=B-y`, and the quoted right-hand side is

```text
A(B-y) + (A-x)(B-(B-y))
= A(B-y) + (A-x)y
= AB - xy.
```

The proof instead imposes equation (2.2),

`f(x,y) ≥ 3AB-2Ay-2xB+xy`,

without a valid intervening inequality or identity. These expressions are
not equal. For the admissible values `A=B=10`, `x=y=7`, the correct
Chen–Piotrowski–Shreve expression is 51, while the claimed replacement is
69. The subsequent symmetric minimization is internally coherent for the
wrong objective, but it proves nothing about `γ(G□H)`.

There is also a domain omission: because `x=A-ρ(G)` and `y=B-ρ(H)`, one has
`0≤x≤A` and `0≤y≤B`, not merely `x,y≥0`. This does not repair the primary
failure—the alleged 0.5809 balancing point lies inside the omitted upper
bounds—but it confirms that the optimization was not translated exactly.

**Verdict:** withdrawn and unusable. No theorem or constant from this paper
is used in this campaign.


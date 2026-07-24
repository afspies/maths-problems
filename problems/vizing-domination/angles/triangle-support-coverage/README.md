# Covering terminal triples and additivity

## Status

**Exact covering model constructed and adversarially audited.** Terminal
`K₃` supports can cover every vertex while retaining separated minimum
complement dominators and the exact packing values `ρ=1,ρ²=3`. In the
natural symmetric block design, the price is precisely two units of
domination-additivity defect per support.

This supports a coverage-versus-additivity strategy but does not prove it
universally.

## Construction

Fix `s≥4`. Partition the vertices into `2s` independent triples

`B_p={(p,0),(p,1),(p,2)}`

and pair block labels by a fixed-point-free involution `p↔p*`. Put no edges
between paired blocks. Between any other two blocks put `K_{3,3}` minus the
identity matching:

`(p,i)∼(q,j)` iff `q∉{p,p*}` and `i≠j`.                     (1)

Then:

```text
γ(G)=3,       ρ(G)=1,       ρ^{\{2\}}(G)=3,                 (2)
γ_G(B_p)=2,   γ_G(V\B_p)=3.                                 (3)
```

Every `B_p` is a feasible terminal conflict triangle, the supports partition
`V(G)`, and the partner `B_{p*}` is an anticomplete minimum dominator of
`V(G)\B_p`.

## Proof

Every closed neighborhood meets a fixed block in at most two vertices.
Given a pair in `B_p`, choose a block avoiding `p,p*` and a coordinate
different from the pair's coordinates; its vertex catches the pair.
Thus `B_p` is a terminal conflict `K₃`, has domination number two, and its
unit weighting is a feasible integral 2-packing of total three.

The same avoidance argument catches every pair of graph vertices, proving
`ρ=1`. Among any four vertices, three use at most two of the three coordinate
labels. Since their blocks and partners exclude at most six of the `2s≥8`
blocks, choose another block and the missing coordinate; its closed
neighborhood contains that triple. Therefore an integral 2-packing cannot
have four unit vertices. A weight-two vertex cannot coexist with any other
positive vertex because every pair is caught. Hence `ρ²=3`.

The partner block dominates the complement of `B_p`: any vertex outside
`B_p∪B_{p*}` is adjacent to two partner coordinates, while the partner
vertices dominate themselves. No pair dominates the complement; choose a
fourth block avoiding the two selected blocks and partners, then choose a
coordinate missed by their adjacency. This proves (3).

Finally, vertices with labels `0,1,2` chosen from three distinct partner
pairs dominate the whole graph. No pair dominates, so `γ(G)=3`.

Thus the additivity defect of every support is exactly

`d=γ_G(V\B_p)+γ_G(B_p)-γ(G)=3+2-3=2`.                       (4)

## Verdict

Coverage, terminal atomicity, separated *minimum* complement dominators,
and the exact packing data are mutually compatible. The symmetric covering
mechanism creates a transversal three-dominator and pays additivity defect
two.

Sparse variants based on matchings between blocks avoid that transversal
but lose terminal pair conflict or `ρ=1`. This is an exact warning, not a
classification: a genuine covering `(5,1,3)` primitive, if it exists, must
use non-blockwise dependency regions rather than a pairwise balanced design.

The next theorem should quantify this observed alternative:

> extensive terminal-triple coverage forces domination-additivity defect,
> unless repeated coordinate holes create a product-scale tax.

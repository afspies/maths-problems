# Audit of Chen--Li--Xi--Xu v3

Source audited: Chen, Li, Xi, and Xu, *The Mahler Conjecture in Three
Dimensions*, arXiv:2605.09334v3 (17 June 2026). This is a fresh preprint, not a
peer-reviewed premise. The shadow-system input was checked against the
dimension-\(n\) statement in Meyer--Reisner and its restatement as Proposition
1 of Fradelizi--Meyer--Zvavitch.

## Reconstruction with the dimensional seams exposed

1. **Centering, polarity, and compactness (dimension-independent).** The
   Santaló polar reverses the face lattice. Mahler volume is affine invariant
   and continuous. After John normalization, the class \(C_N^{(n)}\) of
   \(n\)-polytopes with at most \(N\) vertices is compact enough for the volume
   product to attain its minimum.
2. **Shadow-system convexity and rigidity (dimension-independent external
   theorem).** For a nondegenerate shadow system \(L_t\subset\mathbb R^n\),
   \(t\mapsto |L_t^{s(L_t)}|^{-1}\) is convex. If \(|L_t|\) is affine and the
   volume product is constant, Meyer--Reisner rigidity makes all \(L_t\)
   affine images under
   \(x\mapsto x+t(w\mathbin\cdot x+\beta)\theta\).
3. **Admissible speeds (definition dimension-independent).** A speed is
   admissible when its restriction to each facet not parallel to \(\theta\)
   is affine. A parallel facet imposes no constraint.
4. **Short-time persistence (statement dimension-independent; printed proof
   is written in 3D).** The v3 proof explicitly follows edges as intersections
   of two facets and vertices as intersections of three facets. In dimension
   four those sentences cannot simply be copied. The complete replacement
   argument is given below.
5. **Volume affinity (dimension-independent).** Triangulate every
   \((n-1)\)-facet without new vertices and cone to an affine-moving interior
   point. In each \(n\times n\) determinant, every \(t\)-dependent column is a
   multiple of the same \(\theta\); all terms of degree at least two vanish.
6. **Minimizers are terminal on both sides (dimension-independent after
   steps 2, 4, and 5).** The exact four-dimensional verification is below.
7. **Terminal-body classification (specifically 3D).** Section 5 uses polygon
   facets, the equality of edge/facet degrees in a 3D vertex figure, and
   \(f_0-f_1+f_2=2\). This is the only bridge that does not transfer to 4D.
8. **Passage from polytopes to bodies (dimension-independent).** Once every
   \(C_N^{(4)}\)-minimizer is a simplex, arbitrary polytopes follow by varying
   \(N\), and arbitrary convex bodies follow by Hausdorff approximation.

## Exact minimizer-to-terminal statement in dimension four

Let \(C_N^{(4)}\) be the full-dimensional 4-polytopes with at most \(N\)
vertices, and let \(Q\) minimize the Mahler volume \(\mathcal P\) on this
class. Suppose the repaired four-dimensional persistence lemma above is used.
Then \(Q\) and \(L=Q^{s(Q)}\) have only globally affine admissible speeds in
every direction.

For a shadow flow \(Q_t\), persistence keeps at most \(N\) vertices, so
minimality makes \(t=0\) an interior minimum. Volume affinity, convexity, and
Meyer--Reisner rigidity force its speed to be globally affine.

For a shadow flow \(L_t\), persistence keeps
\[
 f_3(L_t)=f_3(L)=f_0(Q)\leq N.
\]
Polarity reverses faces, hence \(L_t^{s(L_t)}\in C_N^{(4)}\). Therefore
\[
 \mathcal P(Q)\leq\mathcal P(L_t^{s(L_t)})
 \leq\mathcal P(L_t).
\]
At \(t=0\), applying the same polar inequality to \(Q\), together with the
display, forces \(\mathcal P(L)=\mathcal P(Q)\). Thus \(t=0\) is again an
interior minimum and rigidity makes the speed globally affine.

No dimension-four analytic hypothesis is missing beyond the repaired
persistence lemma and the standard hypotheses already present in the
Meyer--Reisner theorem: a two-sided, nondegenerate shadow interval and affine
primal volume. The terminal-polytope classification remains completely open
outside the subclasses proved in this campaign.

## Dimension-free face-lattice persistence lemma

Let \(P=\operatorname{conv}\{x_1,\ldots,x_V\}\subset\mathbb R^d\), let
\(\alpha\in A_\theta(P)\), and put
\[
x_i(t)=x_i+t\alpha_i\theta,\qquad
P_t=\operatorname{conv}\{x_i(t)\}.
\]
Then, for all sufficiently small \(|t|\), \(P_t\) has the same labeled
vertex--facet incidences, hence the same face lattice, as \(P\).

**Proof.** For every old facet \(F_k\), admissibility and the normal
calculation in CLXX produce a continuously moving hyperplane
\(H_k(t)=\{x:x\cdot v_k(t)=h_k(t)\}\) containing exactly the moved vertices
formerly on \(F_k\). Every other moved vertex remains strictly inside its
halfspace for small \(|t|\). Thus each old facet remains supporting.

At every old vertex choose \(d\) incident facet normals that are linearly
independent at \(t=0\). They remain independent and their moved hyperplanes
meet at the moved vertex, so every \(x_i(t)\) remains a vertex.

Let \(Q_t\) be the intersection of all moved old facet halfspaces. The family
\(Q_t\) is uniformly bounded for small \(|t|\): otherwise normalized
unbounded points would limit to a recession direction of the bounded
polytope \(Q_0=P\). We already have \(P_t\subseteq Q_t\).

Suppose, toward a contradiction, that there are \(t_j\to0\) and vertices
\(y_j\) of \(Q_{t_j}\) not among the \(x_i(t_j)\). Choose \(d\) active facets
at \(y_j\) with independent normals. There are finitely many choices, so pass
to a subsequence on which the labels \(k_1,\ldots,k_d\) are fixed. Uniform
boundedness gives a further subsequence \(y_j\to y\in P\). The old facets
\(F_{k_1},\ldots,F_{k_d}\) have a nonempty common face
\[
G=F_{k_1}\cap\cdots\cap F_{k_d}
\]
containing \(y\).

If \(\dim G=r>0\), choose \(r+1\) affinely independent vertices of \(G\).
Their moved copies remain affinely independent and lie in all \(d\) selected
hyperplanes. Hence the intersection of those hyperplanes has dimension at
least \(r\), contradicting independence of their normals at \(t_j\).
Therefore \(G\) is an old vertex, say \(x_i\). All selected moved hyperplanes
contain \(x_i(t_j)\); because their normals are independent, their unique
intersection is \(x_i(t_j)\). Thus \(y_j=x_i(t_j)\), the final contradiction.

So \(Q_t\) has no vertices beyond the vertices of \(P_t\), and
\(Q_t=P_t\). The strict nonincidences and preserved incidences show that the
labeled vertex--facet incidence matrix is unchanged. Since this matrix
determines the face lattice of a polytope, the face lattice persists. \(\square\)

## Source-level cautions

- The preprint itself says that most shadow-flow results extend to
  \(\mathbb R^n\), but this audit does not use that sentence as proof.
- Its persistence proof is not literally dimension-free; the replacement
  argument above is required.
- Vertex--facet incidence determines where admissibility equations live, but
  not their coefficients. Those depend on affine relations in the chosen
  realization.

## 2026-07-24 correction: terminality is not the 4D bridge

The reduction above remains valid, but the final sentence of the
minimizer-to-terminal section must not be read as evidence that a terminal
classification exists in dimension four. The exact certificate in
`../results/terminal-bridge-counterexample.md` constructs a rational
non-simplex 24-cell \(Q\) for which both \(Q\) and its genuine Santaló polar
are terminal.

The correct necessary-condition stack for a local minimizer is stronger:
after Santaló centering it is pair-terminal, it satisfies
\(c(K)=c(K^\circ)=0\), and its projective covariance Hessian is positive
semidefinite [klartag-2018; balacheff-solanes-tzanev-2023]. The last two
conditions are independent variational inputs, not consequences of shadow
terminality.

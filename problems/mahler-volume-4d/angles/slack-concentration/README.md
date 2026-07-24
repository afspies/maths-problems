# Slack concentration and a terminal trace gap

## The theorem-shaped target

Let \(P\subset\mathbb R^4\) be bi-centered and pair-terminal. If its
facet-circuit support graph is connected, conjecturally

\[
\boxed{
\operatorname{tr}\!\left(
\operatorname{cov}(P)\operatorname{cov}(P^\circ)
\right)<\frac19.
}
\]

This would finish the connected non-join branch. A local Mahler minimum must
satisfy

\[
\operatorname{cov}(P^\circ)
\succeq\frac1{36}\operatorname{cov}(P)^{-1},
\]

which implies the opposite trace inequality.

The simplex has trace \(1/9\), but its facet-circuit graph is disconnected.
Ellipsoids also attain equality, but are nonpolyhedral. The regular 24-cell
has trace \(169/1800<1/9\). Projectively critical pentagons do not falsify
the target: polygon edges have no affine circuit equations, so nontriangles
are not terminal.

## Probabilistic identity

Let \(X\) and \(Y\) be independent uniform points of \(P\) and \(P^\circ\),
respectively, and put

\[
Z=1-\langle X,Y\rangle.
\]

Polarity gives \(Z\ge0\). Bi-centering gives

\[
\mathbb E Z=1,
\]

and independence gives the exact identity

\[
\operatorname{Var}(Z)
=\mathbb E\langle X,Y\rangle^2
=\operatorname{tr}\!\left(
\operatorname{cov}(P)\operatorname{cov}(P^\circ)
\right).
\]

Thus the target is a sharp slack-concentration inequality
\(\operatorname{Var}(Z)<1/9\) on the connected terminal branch.

## Finite weighted slack energy

Choose vertex triangulations of \(P\) and \(P^\circ\). For a pair of
4-simplices \(S=\operatorname{conv}(x_0,\ldots,x_4)\) and
\(T=\operatorname{conv}(y_0,\ldots,y_4)\), put

\[
L_{ij}=1-x_i\cdot y_j\ge0.
\]

Write \(L_{i+}\), \(L_{+j}\), and \(L_{++}\) for row, column, and total
sums. The pair's contribution to
\(900\operatorname{tr}(\operatorname{cov}P\operatorname{cov}P^\circ)\)
is

\[
\begin{aligned}
E(S,T)={}&(25-L_{++})^2
+\sum_i(5-L_{i+})^2\\
&+\sum_j(5-L_{+j})^2
+\sum_{i,j}(1-L_{ij})^2.
\end{aligned}
\]

This follows directly from the second moment of a uniform 4-simplex:

\[
\mathbb E_S[XX^\mathsf T]
=\frac{
(\sum_i x_i)(\sum_i x_i)^\mathsf T+\sum_i x_ix_i^\mathsf T
}{30}.
\]

The desired trace ceiling is exactly that the primal/polar
volume-weighted average of \(E(S,T)\) is at most \(100\), with strictness in
the connected non-simplex case. A simplex has diagonal normalized slack
entries five and attains \(100\).

## Why terminality must enter quantitatively

Arbitrary nonincidence slacks can be large, so positivity and incidence
counts alone cannot prove this energy bound. The plausible missing input is
a volume-weighted Poincare or Hodge inequality on the facet-circuit support
complex:

- facet circuits supply local cancellation relations among slack rows;
- connected support removes the affine-join zero mode;
- pair-terminality supplies the same control after deleting any
  direction-parallel normal flat.

The route is **GO** only if those qualitative spanning statements can be
upgraded to a quantitative energy inequality. It should be abandoned upon
finding an exact bi-centered connected pair-terminal example with trace
above \(1/9\).

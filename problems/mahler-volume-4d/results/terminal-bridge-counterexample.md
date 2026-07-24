# Exact counterexample to the terminal-pair bridge

## Statement

There is a rational realization \(Q\) of the 24-cell such that \(s(Q)=0\)
and both \(Q\) and \(Q^\circ\) admit only globally affine admissible shadow
speeds in every direction. In particular,

\[
  \bigl(Q,Q^{s(Q)}\text{ pair-terminal}\bigr)
  \;\not\Longrightarrow\; Q\text{ is a simplex}.
\]

This falsifies the proposed four-dimensional classification bridge. It does
not falsify the Mahler conjecture: the constructed \(Q\) is not centered at
its centroid and therefore cannot be a local Mahler minimizer.

## Construction

Start with Paffenholz's four-parameter 24-cell realization
[rastanawi-sinn-ziegler-2020]. For

\[
  a=(1/5,2/5,3/5,4/5),
\]

take the 16 cube vertices \(\{\pm1\}^4\), together with the eight reflections
of \(a\) across the cube facets. Let \(P_0\) be their convex hull and let
\(g=c(P_0^\circ)\). Define

\[
  Q=\left\{\frac{x}{1-g\cdot x}:x\in P_0\right\}.
\]

Since \(g\) lies in the interior of \(P_0^\circ\), all denominators are
positive. Directly from the definition of polarity,

\[
  Q^\circ=P_0^\circ-g.
\]

Thus \(c(Q^\circ)=0\), so the origin is exactly \(s(Q)\).

## Exhaustive exact check

For a shadow direction \(\theta\), a facet is waived exactly when its normal
lies in \(\theta^\perp\). The waived normals therefore span a subspace of
rank at most three. Every possible waived set is the closure of a set of at
most three facet normals, so enumerating those closures exhausts all
directions; it is not direction sampling.

The verifier obtains:

```text
labelled-24-cell-incidence True
santalo-polar-centroid-zero True
primal-centroid-zero False
primal-direction-flats 1941
polar-direction-flats 580
all-speed-dimensions 5
terminal-pair-implies-simplex False
```

All ranks and centroids are rational. The pulling-triangulation centroid is
independently checked by triangulating every octahedral facet along its
triangular ridges and coning the boundary tetrahedra to the origin. The
labelled facet incidence is checked against the regular member \(a=0\) of
the same realization family.

Reproduce with:

```text
PYTHONPATH=problems/mahler-volume-4d/harness \
python3 -B problems/mahler-volume-4d/harness/verify_bridge_counterexample.py
```

## Consequence

The shadow-flow reduction to pair-terminality remains valid, but
pair-terminality is not a classification invariant strong enough to finish
dimension four. Any viable replacement must include further variational
conditions satisfied by an actual minimizer.

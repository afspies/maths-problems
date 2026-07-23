# Exact terminal-polytope harness

`polytope.py` implements dependency-free rational arithmetic for small realized
polytopes. It enumerates supporting facets and incidences, constructs the
origin polar, builds admissible-speed matrices, and computes rational ranks and
simplex volumes.

For each constrained facet `F`, a matrix row is an affine dependence `lambda`
of its vertices, and the verified speed equation is
`sum(lambda[v] * alpha[v]) == 0`. The block locations come from vertex--facet
incidence, while coefficients record realized affine dependences. Incidence
alone does not determine those coefficients.

Run:

```bash
python3 -m unittest discover -s problems/mahler-volume-4d/harness -v
```

The positive object is the centered 4-simplex: its polar, incidences,
five-dimensional speed space, and exact Mahler product `3125/576` are checked.
Negative controls are the 4-cross-polytope, the 4-cube in a facet-parallel
direction, and a pyramid over the 3-cube; each has certified non-globally
affine admissible speeds.

This is a discovery/falsification harness, not a verifier of the full Mahler
conjecture. A classification proof cannot be replaced by checking finitely
many face lattices.

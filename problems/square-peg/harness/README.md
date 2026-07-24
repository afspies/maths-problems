# Exact conjecture-hygiene harness

This harness checks only finite polygonal data.  It does **not** constitute
progress on the universal Square Peg conjecture.

`geometry.py` uses `fractions.Fraction` throughout and provides:

- exact simplicity checks for closed rational polygons;
- exact Liouville primitives
  \(\int y\,dx\) at polygon vertices, together with rational subdivision;
- exact verification that four rational boundary points form a nondegenerate
  square.

Run the known-object tests from the repository root:

```bash
python3 -m unittest discover -s problems/square-peg/harness -p 'test_*.py' -v
```

The Liouville convention is \(\lambda=y\,dx\) under
\(T^*\mathbb R\cong\mathbb R^2_{x,y}\).  Replacing it by \(-y\,dx\), as some
contact-sign conventions do, changes every primitive by a sign and changes
none of the convergence arguments.

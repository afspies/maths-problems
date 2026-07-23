# Journal — Four-dimensional Mahler volume conjecture

Append-only. One dated section per session: what was tried (exact commands,
encodings, parameters), outcomes, compute spent and where it ran. Newest at the
bottom. Do not rewrite history — corrections get their own dated entry.

## 2026-07-23 — scaffolded

Problem folder created from template. No work yet.

## 2026-07-23 — shadow-flow audit and terminal subclasses

### Scope and source audit

Worked on branch
`problem/mahler-volume-4d/2026-07-23-terminal-polytopes`, touching only this
problem folder and the generated root board. No `AGENTS.local.md` was present.

Audited Chen--Li--Xi--Xu, *The Mahler Conjecture in Three Dimensions*,
arXiv:2605.09334v3, against Meyer--Reisner's dimension-\(n\) shadow-system
theorem and the Fradelizi--Meyer--Zvavitch restatement. The step map is in
`literature/shadow-flow-audit.md`.

The minimizer-to-terminal reduction is valid in dimension four, but not merely
by copying the preprint. Its printed persistence proof uses a specifically 3D
intersection argument. Replacing it with an independent-active-facets
subsequence argument gives short-time face-lattice persistence in every
dimension. Facet triangulation and the one-direction determinant argument make
volume affine in every dimension. The bounded-vertex minimization and polar
chain then prove terminality of both a minimizer and its Santaló polar.

### Exact harness

Built `harness/polytope.py` before any computational search. It uses exact
`Fraction` arithmetic for rational rank/nullspaces, supporting facets, polar
vertices, incidence summaries, admissible-speed matrices, and simplex volume.
The speed equations are affine dependencies indexed by vertex--facet
incidence; the audit explicitly records that incidence alone does not
determine realization-dependent coefficients.

Commands:

```text
python3 -m unittest discover -s problems/mahler-volume-4d/harness -v
python3 -m py_compile problems/mahler-volume-4d/harness/polytope.py problems/mahler-volume-4d/harness/test_polytope.py
```

Final outcome: 6 tests passed in 0.494 seconds; byte-compilation passed. The
centered 4-simplex has exact product \(3125/576\) and speed dimension five.
The cross-polytope, cube in a facet-parallel direction, and pyramid over a
cube certify nontrivial speeds. No floats, seeds, solver search, or bulk
face-lattice enumeration were used.

### Incidence inequalities and subclass proofs

For \(V=f_0\), \(F=f_3\), \(I=f_{03}\), maximum facet size \(\Delta\), and
maximum vertex--facet degree \(\delta\), exact rank subadditivity gives
\[
\dim A_\theta(P)\ge V-I+4F+\Delta-4
\]
when \(\theta\) is parallel to a largest facet. Pair-terminality therefore
implies
\[
\Delta\le I-V-4F+9,\quad
\delta\le I-F-4V+9,\quad
2I\ge5(V+F)-10.
\]

Summing Euler over all 3-facets and using polygonal 2-faces and edge links
gave the flag/Dehn--Sommerville identities
\[
f_{03}-f_{02}+2f_2=2f_3,\qquad
f_{03}=f_{02}-2f_1+2f_0.
\]

Every simplicial 4-polytope has unconstrained speed space
\(\mathbb R^{f_0}\), so terminality forces \(f_0=5\). Duality handles the
simple pair-terminal class.

For \(P=\operatorname{pyr}(Q)\) and tangent direction \((u,0)\), proved
\[
A_{(u,0)}(P)\cong A_u(Q)\oplus\mathbb R,\qquad
T(P)\cong T(Q)\oplus\mathbb R.
\]
The polar is again a pyramid over a face-lattice dual of \(Q\). The 3D
dual-pair counting lemma then forces a pair-terminal 4-pyramid to be a
simplex.

Finally derived directly from polar cross-sections and the
centroid--Santaló characterization:
\[
\mathcal P(\operatorname{pyr}_d K)
=\frac{(d+1)^{d+1}}{d^{d+2}}\mathcal P(K).
\]
The audited three-dimensional theorem therefore proves
\(\mathcal P(P)\ge3125/576\) for every 4-pyramid, with equality only for a
4-simplex. This is the strongest first-session result and passes the
two-session continuation gate.

### Mandatory independent review

Consulted GPT-5.6 Sol at xhigh effort once the incidence/pyramid route was
selected. Its adversarial verdict:

- all rank, duality, and flag identities were correct;
- the simple/simplicial and pyramid terminality reductions were sound;
- the printed 3D persistence paragraph was a real citation gap, and the
  independent-active-facets repair closes it;
- the full terminal classification does **not** follow from the current
  inequalities; and
- the pyramid volume-product factorization supplies the stronger direct
  infinite-family theorem.

The reviewer required no correction to the stated partial theorems. Its
warning against presenting the flag inequality as a global classification is
reflected throughout the write-up.

### Compute and verdict

Local exact tests used under one CPU-second in the final run. External work
was one xhigh independent-review turn and source retrieval; there was no
search compute. Verdict: **continue**. The gate is met by both a new
incidence/dimension inequality and nontrivial infinite-family theorems.

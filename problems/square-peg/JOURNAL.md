# Journal — Square Peg conjecture

Append-only. One dated section per session: what was tried (exact commands,
encodings, parameters), outcomes, compute spent and where it ran. Newest at the
bottom. Do not rewrite history — corrections get their own dated entry.

## 2026-07-24 — scaffolded

Problem folder created from template. No work yet.

## 2026-07-24 — finite-variation / Young bridge

### Scope and source audit

Worked only in `problems/square-peg/` plus the generated root `README.md`.
Audited primary sources through 2026-07-24:

- Asano--Ike, arXiv:2412.21057v3, especially Theorems 1.1 and 4.1,
  Proposition 5.8/Corollary 5.9, and Remark 5.6;
- Greene--Lobb, arXiv:2404.05179v2, for Jordan Floer action, shrink-out, and
  the rectifiable area/radius result;
- Greene--Lobb, arXiv:2407.07798 / CMH DOI 10.4171/CMH/619, for the graph
  perturbation theorem;
- Boedihardjo--Geng, arXiv:1309.1576v2 / Constructive Approximation 42, for
  parameter-respecting embedded polygonal interpolation, \(q\)-variation
  convergence, Young--Loeve estimates, and the finite-\(p\) Green theorem;
- Young, Acta Mathematica 67 (1936), for the critical Dini condition.

The audit is in `literature/NOTES.md`.  It explicitly records that
Asano--Ike already prove every prescribed rectangle for every rectifiable and
every locally monotone Jordan curve.  It also records the official date
discrepancy: arXiv v3 was submitted 2026-01-05 and its PDF is dated
2026-01-06; a secondary experimental rendering showed the prompt's
2026-03-22 date.

Asano--Ike's condition is parametrized: smooth Jordan maps \(c_n:S^1\to
\mathbb R^2\) converge uniformly to the fixed map \(c\), and primitives of
\((c_n\circ e)^*\lambda\), normalized here by \(F_n(0)=0\), converge locally
uniformly on the universal cover.  Their proof, rather than the statement,
rescales areas to \(\pi\).  Rectifiability enters their Corollary 5.9 through
Riesz--Privalov length convergence for inner Riemann-map level curves and the
rectifiable Green theorem.

### Theorem proved

Proved in `angles/p-variation/README.md`:

> If a Jordan parametrization has finite \(p\)-variation for some \(p<2\),
> it satisfies Asano--Ike Theorem 1.1 and hence inscribes every prescribed
> rectangle.

The proof selects \(p<q<2\), uses Boedihardjo--Geng Theorem 2.2 for Jordan
polygonal interpolants and their Lemma 3.1 separately for \(q\)-variation
convergence, then rounds every polygon on its original cyclic parameter
intervals.  The corner-rounding lemma retains collinear speed breakpoints and
makes the smooth Jordan map arbitrarily close in uniform plus
\(1\)-variation norms.  Young--Loeve continuity with
\(C_q=2\zeta(2/q)\) gives uniform primitive convergence on one period;
quasiperiodicity gives local-uniform convergence on \(\mathbb R\).

Proved a sharper critical result in `angles/critical-p2/README.md`:

> If the periodic coordinate moduli obey
> \(\int_0^T\omega_x(r)\omega_y(r)r^{-2}\,dr<\infty\), the same peg
> conclusion holds.

The final proof uses an additive Dini sewing estimate
\(|I_{s,t}-y_sx_{s,t}|\le C(t-s)J(t-s)\), controls arbitrary tagged sums and
polygonal trapezoid corrections, and makes each finite polygonal smoothing
diagonally primitive-close by a BV estimate.  The repeated shrinking circle
\(z_n(t)=n^{-1/2}(e^{2\pi int}-1)\) isolates the \(p=2\) area anomaly but is
explicitly not claimed to be a Jordan counterexample.

### Strict nonrectifiable witness

`results/spiral-family.md` proves that the curve made from the two rotated
spirals \(\theta^{-1/d}e^{i\theta}\), \(1<d<2\), and an outer circular arc is:

- Jordan, by monotone radius and disjoint rotation;
- nonrectifiable, since its length dominates \(\sum n^{-1/d}\);
- finite \(p\)-variation for every \(p>d\), by a complete within-block /
  crossing-increment decomposition; and
- not locally monotone, since every projection changes sign infinitely often
  at the origin.

It is therefore outside both named Asano--Ike corollaries and now gets every
prescribed rectangle from the new bridge.

### Independent GPT-5.6 Sol reviews (xhigh)

Consulted GPT-5.6 Sol at xhigh at bridge selection and repeatedly on the
written proof, as required.

1. Initial verdict: **GO**.  The finite-\(p\) bridge was sound, the Dini--Young
   statement was recommended as the sharper headline, and novelty should be
   presented as a short synthesis rather than deep new machinery.
2. Written-proof verdict: **HOLD** pending explicit repairs to cyclic
   fixed-parameter smoothing, arbitrary-partition Dini sewing, and the
   polygon-to-smooth primitive estimate.
3. After those repairs, one final Dini additivity/tag-control issue was found
   and fixed.
4. Final focused verdict: **MERGE — all blocking proof issues are resolved.**

### Exact harness and commands

Built `harness/geometry.py` first.  It uses `fractions.Fraction` for rational
polygon simplicity, \(\int y\,dx\), shoelace area, rational subdivision, and
candidate-square verification.

Commands run:

```text
python3 -m unittest discover -s problems/square-peg/harness -p 'test_*.py' -v
python3 -m py_compile problems/square-peg/harness/geometry.py problems/square-peg/harness/test_geometry.py
xmllint --html --noout problems/square-peg/writeup/report.html problems/square-peg/writeup/artifact-template.html
python3 tools/board.py
```

The unit test command passed 5/5 tests in 0.001 seconds.  Python compilation
and both HTML checks emitted no errors.  The board regenerated with 18
problems.  Computation was negligible and ran locally; no private
infrastructure was used.

### Artifacts and status

Wrote the canonical report at `writeup/report.md` and a self-contained
presentation at `writeup/report.html`.  Status is `partial-results`: the
finite-\(p\) and Dini classes are proved subject to the cited published
inputs, but the unrestricted Square Peg conjecture remains open.  Targeted
search found no prior explicit peg theorem with these hypotheses; this is not
proof of priority, so expert confirmation remains the next gate before a DOI
or formal novelty claim.

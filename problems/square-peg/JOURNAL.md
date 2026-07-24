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

## 2026-07-24 — proof hardening and the finite-\(2\)-variation frontier

### Parallel hardening tracks

Launched three independent agents on nonoverlapping files while the main
thread attacked \(p=2\):

1. **Proof audit.** Checked Asano--Ike v3 Theorem 1.1/Remark 5.6 and
   Boedihardjo--Geng Theorem 2.2/Lemma 3.1 from the primary PDFs. Verdict:
   **MERGE** after replacing the unnecessarily strong and under-justified
   relative \(C^\infty\) rounding claim by a regular \(C^1\) fillet
   construction. Asano--Ike Remark 5.6 explicitly permits this regularity.
   Artifact: `results/p-variation-proof-audit.md`.
2. **Priority audit.** Checked the peg, Young/rough-path, and 2026 citation
   trails, including Greene--Lobb arXiv:2604.17116 and Barber
   arXiv:2604.27717. No explicit finite-\(p<2\) prescribed-rectangle theorem
   was found. Verdict: the result is best described as an “apparently
   unstated immediate corollary/synthesis,” not a new rough-integration
   theorem. Artifact: `literature/PRIORITY_AUDIT.md`.
3. **Paper package.** Produced `writeup/p-variation-note.md`; the main thread
   reconciled it with the proof audit's \(C^1\) repair.

No author was contacted and no external priority claim was made. A draft
inquiry is preserved in the priority audit for human review.

### Critical theorem and counterexample

Proved in `angles/critical-p2/osgood-area-anomaly.md`:

> For every parametrized Jordan curve \(c\) with trace
> \(C=\partial\Omega\), there are parameter-aligned inner and outer smooth
> Jordan approximation sequences whose Liouville periods tend to
> \(-|\Omega|\) and \(-|\Omega|-|C|\), respectively.

The construction uses interior and exterior Riemann maps, Carathéodory
boundary extensions, smooth approximations to the two boundary phase
homeomorphisms, and continuity of planar measure from below/above.
Interleaving the sequences for \(|C|>0\) gives uniform, parameter-aligned,
embedded smooth approximation with nonconvergent normalized primitives.
This refutes automatic primitive stability for a supplied approximation
sequence; it does not refute Asano--Ike's existential criterion.

To place the anomaly at the critical regularity, constructed a
positive-area \(1/2\)-Hölder Jordan curve by a four-corner Hilbert--Osgood
routing. At level \(n\), child squares have side
\[
 \ell_n={(1-\varepsilon_n)\ell_{n-1}\over2},
 \qquad \varepsilon_n=2^{-n-4}.
\]
The limiting four-corner set has area
\(\prod_n(1-\varepsilon_n)^2>0\). Explicit adjacent corner gates and straight
connectors prove embeddedness. Giving a level-\(n\) square interval length
\(\ell_n^2\) and splitting the remaining parameter time among connectors
gives a uniform \(1/2\)-Hölder estimate. Hence the closed curve has finite
\(2\)-variation.

Also proved the complementary global fact: if the limiting Jordan trace has
zero planar area, winding-number invariance traps the symmetric difference of
the approximating interiors in shrinking neighborhoods of the trace, so
their total periods converge. The unresolved obstruction is now local
primitive convergence on subarcs of zero-area traces.

### New literature input

Audited Antonelli--Young, arXiv:2605.15987v1 (15 May 2026), which develops
geometric beta-number criteria for signed area of \(1/2\)-Hölder curves.
This is the closest published input for the remaining zero-area local-lift
problem. It does not remove the positive-area inner/outer period anomaly.

### Required GPT-5.6 Sol xhigh review

Submitted the full \(p=2\) theorem to GPT-5.6 Sol at xhigh.

1. First verdict: **HOLD**. The conformal approximation, measure limits,
   Liouville sign, null-trace proposition, and claim boundary passed, but the
   Hilbert routing needed an explicit gate invariant, connector-length
   control, a missing child--connector--child Hölder case, and a seam-safe
   exterior closure.
2. Added the explicit southwest/northwest/northeast/southeast gate table,
   proved ancestor/descendant connector disjointness, used straight
   connectors of exact length \(\varepsilon_n\ell_{n-1}\), supplied a
   one-sided gate estimate and exhaustive least-common-parent split, and
   fixed the closing arc.
3. Second verdict: **HOLD** on one ambiguity in the gate endpoint estimate.
   Replaced it by the direct endpoint-adjacent descendant-interval argument.
4. Final verdict: **MERGE**. The reviewer confirmed the routing, injectivity,
   \(H=9\) Hölder constant, closure, conformal approximants, measure limits,
   and conservative Asano--Ike boundary.

### Compute and verification

All mathematical work and lightweight validation ran locally in the
repository worktree. No private compute infrastructure was used. The exact
verification commands were:

```text
python3 tools/board.py
python3 -m unittest discover -s problems/square-peg/harness -p 'test_*.py' -v
python3 -m py_compile problems/square-peg/harness/geometry.py problems/square-peg/harness/test_geometry.py
xmllint --html --noout problems/square-peg/writeup/report.html problems/square-peg/writeup/artifact-template.html
python3 -c 'import tomllib; tomllib.load(open("problems/square-peg/STATUS.toml","rb")); print("STATUS.toml OK")'
git diff --check
```

The board regenerated with 18 problems. The exact harness passed 5/5 tests
in 0.001 seconds. Python compilation, both HTML parses, TOML parsing, and
`git diff --check` completed without error.

## 2026-07-24 — critical Antonelli--Young local lift

### The breakthrough

Reconstructed Antonelli--Young, arXiv:2605.15987v1, Theorem 1.2 and Appendix
B directly from the primary PDF. Their planar hypothesis is not a beta-number
condition: for a \(1/2\)-Hölder path it is the finite dyadic
quadratic-diameter sum
\[
\sigma(c)=\sum_{i\geq0}\sum_{j<2^i}
\operatorname {diam}\{c(j2^{-i}),c((2j+1)2^{-i-1}),
c((j+1)2^{-i})\}^2.
\]
Their conclusion is convergence of polygonal signed areas over **all** fine
partitions, not just the dyadic sequence.

Proved in `angles/critical-p2/antonelli-young-bridge.md`:

> Every \(1/2\)-Hölder Jordan parametrization with
> \(\sigma(c)<\infty\) satisfies Asano--Ike Theorem 1.1 and hence inscribes
> every prescribed rectangle.

The key uniform-prefix lemma extends any two fine partitions of \([0,t]\)
by the same fine partition of \([t,1]\). The common tail cancels, so
Antonelli--Young's full-partition Cauchy modulus is uniform in \(t\).
Continuous polygonal prefix functions give continuity of the limiting
primitive. Boedihardjo--Geng then supplies arbitrarily fine
parameter-aligned Jordan polygons, and the existing diagonal regular-\(C^1\)
rounding makes their primitive error tend to zero. This proves exactly the
local-uniform primitive convergence Asano--Ike require.

### Strict critical witness

Constructed `results/critical-spiral-comb.md`. At scale \(n\), a simple
annular detour has radius
\(a_n=2^{-n-20}\), turn count
\(N_n=\lceil4^n/n^2\rceil\), and parameter time
\(w_n=N_na_n^2\). The detours replace diameters in pairwise disjoint disks
accumulating at one point of an otherwise polygonal Jordan curve.

The global background parametrization is explicitly Lipschitz. Constant-speed
detours give supported bumps with
\[
\|f_n\|_\infty\lesssim a_n,\qquad
\operatorname {Lip}(f_n)\lesssim a_n^{-1}.
\]
This proves a uniform \(1/2\)-Hölder bound, including cross-support cases.
At each dyadic scale,
\[
\sigma(f_n)\lesssim
w_n+a_n^2\log(e/a_n^2),
\]
so \(\sigma(c)<\infty\). Conversely, half-turn chords give
\(\sum_nN_na_n^p=\infty\) for every \(p<2\). Thus the curve has finite
\(2\)-variation but infinite \(p\)-variation for all \(p<2\), infinite
length, and is not locally monotone.

### Novelty and source boundary

Targeted searches through 2026-07-24 found no explicit use of
Antonelli--Young's theorem in the square/rectangular-peg literature. The
paper is only two months old and indexing is incomplete. The result is
therefore described conservatively as an “apparently unstated critical
corollary/synthesis,” not an independent critical-integration theorem.
Details are in `literature/CRITICAL_PRIORITY_AUDIT.md`.

Corrected the previous live documentation: beta numbers in
Antonelli--Young belong to their ambient Heisenberg-map/fibre analysis. The
directly used planar theorem has the dyadic diameter-square hypothesis.
The earlier journal entry is left unchanged under the append-only rule; this
paragraph records the correction.

### Required GPT-5.6 Sol xhigh review

Consulted GPT-5.6 Sol at xhigh at theorem selection and twice on the complete
proof.

1. Selection verdict: **PIVOT/GO** to the Antonelli--Young
   quadratic-diameter class; **HOLD** the speculative zero-area anomaly.
2. First written-proof verdict: **HOLD** for three local repairs: construct
   the limiting primitive as a uniform limit of continuous prefix functions;
   correct a false sentence about spiral/diameter intersections; and write
   the global Lipschitz background parametrization with explicit slope
   bounds.
3. After those repairs, final verdict: **MERGE both files.** No logical
   blockers remained in the uniform-prefix, embedded-rounding, Jordan,
   Hölder, \(\sigma\), variation, or local-monotonicity arguments.

### Compute and verification

All work ran locally in the repository worktree; no private compute
infrastructure was used. The rational harness remains conjecture hygiene and
does not count as evidence for the analytic theorem. Commands run:

```text
python3 -m unittest discover -s problems/square-peg/harness -p 'test_*.py' -v
python3 -m py_compile problems/square-peg/harness/geometry.py problems/square-peg/harness/test_geometry.py
xmllint --html --noout problems/square-peg/writeup/report.html problems/square-peg/writeup/artifact-template.html
python3 -c 'import tomllib; tomllib.load(open("problems/square-peg/STATUS.toml","rb")); print("STATUS.toml OK")'
python3 tools/board.py
git diff --check
```

The exact harness passed 5/5 tests in 0.001 seconds. Python compilation, both
HTML parses, TOML parsing, and `git diff --check` emitted no errors. The board
regenerated with 18 problems.

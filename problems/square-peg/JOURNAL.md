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

## 2026-07-24 — unrestricted zero-trace obstruction

### Literature reduction

Audited Asano--Ike v3 through Remarks 4.2 and 5.5--5.7 and Greene--Lobb's
2026 positive-measure-angle paper.  A fact missing from the earlier live
summary materially sharpens the frontier: Asano--Ike Remark 5.5 already
proves every positive-planar-measure Jordan trace inscribes every prescribed
rectangle by Lebesgue density.  The unrestricted problem therefore reduces
to null traces.

For a null trace, Schoenflies plus relative Oxtoby--Ulam gives a compactly
supported area-preserving/Hamiltonian homeomorphism taking the circle to the
curve.  This defines the canonical sheaf quantization \(F_C\), but does not
prove Remark 4.2's diagonal \(\mu hom\)-cohomology vanishing.  Remark 5.7
explicitly identifies that vanishing as the remaining universal step.

### Two false universal shortcuts

The action of a conservative smoothing is not \(C^0\)-continuous.  For
\[
\phi_n(r,\theta)=(r,\theta+\alpha_n(r))
\]
supported in a disk of radius \(\rho_n\), with \(N_n\) turns,
\[
\|\phi_n-\mathrm{id}\|_{C^0}\leq2\rho_n,\qquad
dS_n=\phi_n^*\lambda-\lambda
=\tfrac12r^2\alpha_n'(r)\,dr.
\]
Taking \(N_n\asymp\rho_n^{-2}\) keeps
\(\operatorname{osc}S_n\) bounded below.  Thus Oxtoby--Ulam plus conservative
smoothing supplies no boundary action estimate.

The square-angle Floer symmetry also does not pin the critical action.
Greene--Lobb's triangle inequality applies to the top invariant only and
gives \(\ell_2(\pi/2)\geq A/2\).  Duality gives
\(\ell_1(\pi/2)=A-\ell_2(\pi/2)\), but swaps the two degrees rather than
identifying them.  The stated axioms permit
\(\ell_2(\pi/2)\to A\) and \(\ell_1(\pi/2)\to0\), precisely the two shrink-out
endpoints.  Null support measure does not repair their no-shrinkout capping
estimate because the projected loops may have unbounded winding
multiplicity.

### The sharp obstruction

Proved `results/null-spiral-no-primitive.md`.  Put
\[
a(\theta)=\theta^{-1/2},\qquad
b(\theta)=\frac{a(\theta)+a(\theta+2\pi)}2.
\]
Traverse \(a(\theta)e^{i\theta}\) inward, the interleaved
\(b(\theta)e^{i\theta}\) arm outward, and close across the outer radial gap.
The order
\[
a(\theta)>b(\theta)>a(\theta+2\pi)
\]
proves embeddedness.  The trace is a countable union of finite rectifiable
arcs and hence is planar-null.  The full enclosed area is finite since
\[
a(\theta)^2-b(\theta)^2=O(\theta^{-2}).
\]
But for \(\alpha=(x\,dy-y\,dx)/2\), the inward-arm action is
\[
\int_{\theta_0}^{\Theta}\alpha
=\frac12\log(\Theta/\theta_0).
\]

The decisive local action-rigidity lemma is proved in
`angles/unrestricted-zero-trace/README.md`: if parameter-aligned regular
\(C^1\) Jordan curves and their normalized primitives converge uniformly,
then the limiting primitive agrees with the classical line integral on every
regular smooth subarc.  The proof extracts moving endpoints which form a
proper crosscut of a shrinking tubular rectangle, closes it along a parallel
side, and applies Green's theorem.  Uniform convergence of the primitives
removes the moving-endpoint errors.  Applied to the inward spiral, the lemma
would force a continuous primitive at the origin parameter to diverge.

Therefore this null curve admits no Asano--Ike Theorem 1.1 approximation
sequence at all.  Natural finite-spiral truncations make the distinction
visible: their total periods converge, while a central prefix primitive
diverges like \(-\tfrac12\log N\).  Embedded corner rounding preserves both
facts.

This is not a counterexample to Square Peg.  It proves instead that the
continuous-primitive route cannot solve the unrestricted problem.  The next
target is the weaker diagonal cohomology vanishing at \(\theta=\pi/2\).

### Novelty and independent review

Targeted searches through 2026-07-24 found no explicit local action-rigidity
lemma or null double-spiral obstruction in the peg, Young/rough-integration,
or conservative-smoothing literature.  Indexing is incomplete, so the result
is described as an explicit campaign counterexample to universality of the
primitive criterion, with no priority claim.

GPT-5.6 Sol at xhigh was consulted at route selection and on the final proof.
It returned **HOLD/PIVOT** on action-controlled conservative smoothing,
exhibited the shrinking radial-twist obstruction, and independently returned
**MERGE** on the local-rigidity lemma and double spiral.  The audit checked
the polar ordering, compact parametrization, planar-null trace, action signs,
moving-crosscut extraction, absence of derivative control, conversion
between \(\alpha\) and \(\lambda=y\,dx\), and the existential quantifier in
Asano--Ike.

### Compute and verification

All work ran locally in the repository worktree; no private compute
infrastructure was used.  The rational harness remains conjecture hygiene and
does not count as evidence for the theorem.  Commands run:

```text
python3 -m unittest discover -s problems/square-peg/harness -p 'test_*.py' -v
python3 -m py_compile problems/square-peg/harness/geometry.py problems/square-peg/harness/test_geometry.py
xmllint --html --noout problems/square-peg/writeup/report.html problems/square-peg/writeup/artifact-template.html
python3 -c 'import tomllib; tomllib.load(open("problems/square-peg/STATUS.toml","rb")); print("STATUS.toml OK")'
python3 tools/board.py
git diff --check
```

The exact harness passed 5/5 tests in 0.001 seconds.  Python compilation,
both HTML parses, TOML parsing, board regeneration (18 problems), and
`git diff --check` completed without error.

## 2026-07-24 — persistent diagonal locality and conformal concentration

### Wide-net attacks

Ran three independent proof attacks: direct diagonal \(\mu hom\), cyclic
configuration topology, and conformal/GMT/rough compactness.  Audited
Asano--Ike v3, Greene--Lobb's action construction, Matschke's special
trapezoids, and the Vrećica--Živaljević compactification argument against
their primary texts.

The exact unrestricted target is derived global diagonal cohomology:
\[
R\Gamma\!\left(\rho^{-1}\Delta_C;
\mu hom(F_C,T_{-a(\theta,C)}R_\theta F_C)
|_{\rho^{-1}\Delta_C}\right)\simeq0,
\qquad0<a(\theta,C)<\pi.
\]
After conjugating a null curve to the standard circle, this becomes the
persistent diagonal-locality statement in
`angles/diagonal-microlocal/README.md`.

### Universal conformal \(L^2\)-primitive theorem

Let \(f(z)=\sum a_nz^n\) map the disk conformally onto a bounded Jordan
domain, and put \(c_r(t)=f(re^{it})\).  For
\(\alpha=(x\,dy-y\,dx)/2\), the positive Fourier coefficients of the
mean-zero periodic part \(P_r\) of the primitive are
\[
\widehat P_r(k)
=\frac{C_{r,k}}{4i}+\frac{D_{r,k}}{2ik},
\]
\[
C_{r,k}=\sum_{m\geq0}\bar a_ma_{m+k}r^{2m+k},\qquad
D_{r,k}=\sum_{m\geq0}m\bar a_ma_{m+k}r^{2m+k}.
\]
Carathéodory gives \(|f_r|^2\to|f|^2\) uniformly and hence
\(C_r\to C\) in \(\ell^2\).  The area identity
\[
\sum_{m\geq1}m|a_m|^2=|\Omega|/\pi=:E
\]
gives \(|D_{r,k}|\leq E\), so dominated convergence after division by
\(k\) gives \(D_r/k\to D/k\) in \(\ell^2\).  Parseval proves strong
\(L^2\) convergence of the centered primitives.  The exact relation
\(y\,dx=\tfrac12d(xy)-\alpha\) transfers the result to Asano--Ike's
convention.

This yields an exhaustive dichotomy.  If the primitives are asymptotically
equicontinuous, Arzelà--Ascoli upgrades \(L^2\) to uniform convergence and
Asano--Ike gives every rectangle.  Otherwise, order-one action lies on
parameter intervals shrinking to one prime end.  Closing those arcs by
chords and using the area--winding identity gives
\[
\|\operatorname{Wind}\|_\infty\gtrsim\rho^{-2},\qquad
\operatorname{length}\gtrsim\rho^{-1}.
\]
Thus every remaining counterexample route is an action-concentration
problem.

### Two exact negative results

Square symmetry does not cancel collapsing actions.  Starting with a smooth
curve carrying a shrinking exact square, apply four disjoint radial
Hamiltonian twists centered at its vertices.  The maps and inverses converge
uniformly to the identity and fix the vertices, while the square action
changes by an arbitrary four-point second difference of the action
potential.  Hence an exact shrinking square can carry any prescribed
limiting action.

The same obstruction has a geometric two-fjord realization.  Two disjoint
\(N\)-turn spiral fjords at opposite square vertices, with
\(N\asymp\rho^{-2}\), make the sum of the two projected capping windings
have order-one integral on support of area \(O(\rho^2)\).  The complementary
fjord sides cancel only in the total Jordan area.

Matschke's Theorem 2.8 gives a separate exact reduction: if a Jordan curve
has no square, it has a special trapezoid at every parameter scale.  Direct
coordinates classify its normal, crossed, pair-coalescent, genuine
trapezoid, and equilateral collision screens.  The tangent-free secant map
has degree one, but no screen is excluded.  The ordinary
Fulton--MacPherson extension needs \(C^1\) tangent data and cannot be
transferred unchanged to arbitrary Jordan curves.

### Required GPT-5.6 Sol xhigh review

GPT-5.6 Sol at xhigh audited the direct microlocal route and returned
**HOLD** on an unrestricted proof.  It confirmed the exact formulation of
Remark 4.2, the conjugated diagonal geometry, and the conformal Fourier
theorem.  It rejected the inference from small local Hamiltonian oscillation
to equality of microlocal germs: the neighborhoods shrink with the error,
individual actions remain arbitrary, and \(\mu hom\) does not commute with
metric limits.

The review identified the sharp missing lemma: arbitrary interior-action
generators collapsing to the diagonal must pair into persistence bars whose
lengths tend to zero.  Chord-level action bounds are false; only a bar-level
\(C^0\) clean-intersection theorem can close the route.

### Sharp realization of conformal concentration

The null double spiral realizes the bad branch at sharp scales.  Its
logarithmic strip has width
\[
h(v)=\frac{\pi}{2v}-\frac{5\pi^2}{8v^2}+O(v^{-3}),
\]
so the longitudinal modulus of \(V<v<cV\) is
\[
M(V,cV)=\frac{(c^2-1)V^2}{\pi}+O(V).
\]
For \(c=e^{2\varepsilon}\), the inward arm has action exactly
\(\varepsilon\), while the cell has area \(O(V^{-1})\), condenser and
critical trace capacity \(O(V^{-2})\), and harmonic measure
\(\exp(-\Theta(V^2))\).  A diagonal choice of conformal radii proves
\(\eta>0\) for the analytic level curves.  Thus the classical conformal
compactness routes are sharp and insufficient.

### Exact microlocal eye

Every finite smooth spiral truncation has clean diagonal Floer cohomology
\(H^*(S^1;\mathbb F_2)\) at action \(0\pmod\pi\).  In the wild limit the
diagonal phase is
\[
t_{AA}(\theta)=s^2\left(\log(\theta/\theta_0)
-\frac{\sin2\theta}{2\theta}\right)+t_0\pmod\pi,
\]
so the reduced microsupport contains the entire action circle over the
collapsed point.  The two sheets have exact asymptotic separation
\[
\delta(\theta)=\frac12\int_\theta^\infty(a^2-b^2)
=\frac{\pi}{2\theta}+O(\theta^{-2}).
\]
A helical-eye toy model shows that \(j_!\) and \(Rj_*\) extensions agree on
every punctured finite stage but differ in point-supported translated
morphisms.  The missing theorem is therefore categorical: identify the
boundary extension chosen by metric-limit quantization.

GPT-5.6 Sol at xhigh performed this second microlocal audit.  Its verdict
remains **HOLD** on the unrestricted conjecture: the phase and eye-width
calculations are exact, but finite Floer complexes, projected microsupport,
and global \(C^0\) barcode continuity do not determine the limiting derived
extension.

### Configuration continuation

A relative-transversality refinement of Matschke's odd fiber intersection
produces a compact connected, fixed-type continuum of exact special
trapezoids spanning every compact positive scale interval.  Hausdorff
limits extend it to total collision.  Disjoint local insertions show that
all three non-square screens can nevertheless occur at one one-sided prime
end, so only a global invariant of the continuum can help.

### Novelty and claim boundary

Targeted searches through 2026-07-24 found no statement of the universal
conformal \(L^2\)-primitive theorem or its prime-end concentration dichotomy
in the peg literature.  The Fourier lemma is elementary, so it is described
only as apparently unstated in this context.  The unrestricted Square Peg
conjecture remains open.

### Compute and verification

All work ran locally in the repository worktree; no private compute
infrastructure was used.  The rational harness remains conjecture hygiene.
Commands run at session end:

```text
python3 -m unittest discover -s problems/square-peg/harness -p 'test_*.py' -v
python3 -m py_compile problems/square-peg/harness/geometry.py problems/square-peg/harness/test_geometry.py
xmllint --html --noout problems/square-peg/writeup/report.html problems/square-peg/writeup/artifact-template.html
python3 -c 'import tomllib; tomllib.load(open("problems/square-peg/STATUS.toml","rb")); print("STATUS.toml OK")'
python3 tools/board.py
git diff --check
```

The exact harness passed 5/5 tests in 0.001 seconds.  Python compilation,
both HTML parses, TOML parsing, board regeneration (19 problems), and
`git diff --check` completed without error.

## 2026-07-24 — action-retaining eye and square-envelope area

### Primary-source reconstruction

Re-read Asano--Ike v3, especially Proposition 2.4, Lemma 3.3, Remark 4.2,
Proposition 5.1, and the twisted action-period identification.  Also audited
their completeness paper, arXiv:2201.02598, Theorem 4.3 and Corollary 4.5.
After a summable subsequence the metric completion is explicitly
\[
 F_\infty\simeq\operatorname*{hocolim}_n
 T_{-\varepsilon_{\ge n}}F_n.
\]
It is a telescope of chosen interleaving morphisms, not an ordinary
\(!\), \(*\), or middle extension.  The source proves convergence and a
microsupport limsup estimate, but does not compute the telescope at a
collapsed prime end.

Audited Hugelmeyer, arXiv:2301.01340, Definition 1 and Theorem 1.  A
square-free Jordan curve has a continuous square envelope with its two
outer vertices in the exterior, its two rotated vertices in the interior,
side length tending to zero at both ends, and outer winding one on the
Jordan domain.  The theorem does not assert finite variation, simple
ribbons, one-sided winding, or endpoint convergence.

### Correction of the helical-eye model

The previous toy model incorrectly collapsed
\(\{r=0\}\times S^1_t\) to one point.  The actual set
\(\rho^{-1}\Delta\) retains the complete action circle.  It also compared
\(j_!\mathbb k_U\) and \(Rj_*\mathbb k_U\), which already differ on the
punctured side boundary, and inferred a sheaf morphism from a common stalk.
Naturality makes that alleged translated morphism zero.

For one fixed punctured eye sheaf \(F\), recollement gives
\[
 k_!F\to Rk_*F\to i_*Q\to+1.
\]
In the monotone helical model,
\[
 Q_t\simeq(\prod_{n\ge0}\mathbb k)/(\bigoplus_{n\ge0}\mathbb k)
\]
with shift monodromy.  It is locally constant in \(t\), hence its
microsupport has \(\tau_t=0\).  Thus the \(!\)-versus-\(*\) distinction
vanishes after Tamarkin localization.  A half-open eye of width \(w\) is
\(w\)-torsion; the null spiral's deep eye, of width
\(\pi/\theta+O(\theta^{-2})\), is arbitrarily torsion.

The remaining local datum is the Milnor boundary term of the continuation
telescope.  One must show that restriction to the diagonal commutes with
the relevant inverse limit and that the cross-stage tower is pro-zero away
from \(\pi\mathbb Z\).

### Exact failure of the zero-Hofer germ proof

The conjugated Hamiltonian
\[
 H^\phi(z,w)=|\phi(z)-\phi(w)|^2/4
\]
can be cut off in an invariant diagonal tube, after a compact midpoint
cut-off, without changing its shrinking germ and with Hofer oscillation
\(O(\varepsilon)\).  This geometric step is sound.

The categorical inference is false.  The constructible objects
\[
 V_\varepsilon
 =V_{\rm std}\oplus\mathbb k_{[a_0,a_0+\varepsilon)}
\]
converge to \(V_{\rm std}\) while their microstalk at the fixed endpoint
\(a_0\) retains an extra \(\mathbb k\).  More sharply, an action
skyscraper has zero one-sided interleaving distance from zero but non-zero
ordinary global cohomology.  Restricted diagonal \(\mu hom\) is not known
to be a limit-constructible Tamarkin object, so zero-distance rigidity does
not apply.  This exactly models the zero-lifetime critical class that
Remark 4.2 must eliminate.

A GPT-5.6 Sol xhigh audit and an independent categorical audit both returned
**HOLD**.  They confirmed the cut-off geometry and rejected both the
unsupported passage of smooth GKS locality through metric completion and the
zero-distance-to-isomorphism step for ordinary restricted \(\mu hom\).

### Square-envelope area conservation

For outer paths \(a,b\), write \(v=b-a\) and take the opposite square paths
\(c=a+Jv,d=b+Jv\).  Direct Young calculus, equivalently an exact synchronized
polygon calculation, gives
\[
 \mathcal A(\Gamma_{\rm in})-\mathcal A(\Gamma_{\rm out})
 =\frac{|v(s)|^2-|v(t)|^2}{2}.
\]
The long-side integrands cancel identically; only the straight connectors
remain.  A compactified finite-\(p<2\) square envelope with simple nested
ribbons is therefore impossible.

The existing envelope theorem does not supply the needed one-sided winding.
An exterior loop can wind once on the Jordan domain while adding a clockwise
exterior lobe; an inner loop can repeat many times.  Equal signed areas are
therefore compatible with the stated inside/outside conditions.

A second exact polygonal obstruction defeats the obvious paired closure.
For a \(\Pi\)-shaped domain and vertical translation \(v\), the set
\[
 \operatorname{Ext}(\gamma)\cap(\operatorname{Int}(\gamma)-v)
\]
has distinct components containing the two admissible outer vertices.
There is no outer connector whose translate remains inside.  Scaled notches
reproduce the failure at arbitrarily small square sizes.

The required final GPT-5.6 Sol xhigh audit first returned **HOLD** on the
phrase “one-sided winding”: a sixteen-fold positive inner loop is already a
counterexample.  After replacing it by the exact sufficient bounds
\[
 n_{\rm out}\geq\mathbf1_\Omega,\qquad
 0\leq n_{\rm in}\leq\mathbf1_\Omega,\qquad
 \int_\Omega(1-n_{\rm in})>0
\]
(or \(n_{\rm in}\leq0\)), the verdict was **MERGE**.  The audit independently
checked the sign in the ribbon identity and the components of the
\(\Pi\)-notch translation set.

### Claim boundary and compute

The unrestricted Square Peg conjecture remains open.  This session made two
proof-grade corrections/reductions and one exact conditional invariant; it
did not prove an unrestricted square.  The rational harness remains
conjecture hygiene only.

All work ran locally in the repository worktree; no private compute
infrastructure was used.  Commands included:

```text
python3 -m unittest problems.square-peg.harness.test_geometry
# failed during collection: ModuleNotFoundError: No module named 'geometry'
# (the harness uses its documented discovery-mode import path)
python3 -m unittest discover -s problems/square-peg/harness -p 'test_*.py'
python3 -m py_compile problems/square-peg/harness/geometry.py problems/square-peg/harness/test_geometry.py
xmllint --html --noout problems/square-peg/writeup/report.html problems/square-peg/writeup/artifact-template.html
python3 -c 'import tomllib; tomllib.load(open("problems/square-peg/STATUS.toml","rb"))'
python3 tools/board.py
git diff --check
```

## 2026-07-24 — unrestricted synthesis: three boundary no-go theorems

### Fresh parallel attacks

Ran three independent proof-first attacks rather than extending one formal
heuristic:

1. a GPT-5.6 Sol xhigh audit of square duality, Verdier duality,
   multiplicativity, and ordinary local Floer localization;
2. a full cross-time audit of Hugelmeyer's square-envelope construction; and
3. a tangent-free configuration-degree compactification with an explicit
   wild collision model.

The unrestricted Square Peg conjecture was **not** solved.  Each attack
returned a proof-grade obstruction delimiting what a successful theorem must
add.

### Oh localization and the distinguished-class mismatch

Audited Oh, arXiv:1111.5996v4, directly from the official source.  For an
engulfable Hamiltonian path with \(C^0\)-small time-one map, the
maximum-principle thick--thin decomposition defines local Floer homology and,
along a full engulfable homotopy, identifies it with ordinary Lagrangian
homology.  The source explicitly states that thin strips may have large area,
the decomposition does not respect action filtration, and local continuation
has no uniform filtration bound.

Oh's local/global spectral comparison controls the ordinary fundamental
class.  Asano--Ike's critical class is different: their microlocalization
formula sends
\[
v\longmapsto v\otimes1+1\otimes v,
\]
which restricts to \(v+v=0\) on the clean diagonal over \(\mathbb F_2\).
Their twisted \(F_0\) also has
\(\operatorname{End}(F_0)\simeq H^*(S^1)\), rather than the ordinary
\(H^*(T^2)\) of the torus zero section.

A two-parameter \(H=\mathbb k[v]/(v^2)\)-module with
\[
M_r=Hu\ (r<B),\qquad M_r=H/(v)u\ (B\le r<A),\qquad
M_r=0\ (r\ge A)
\]
shows that zero \(v\)-action on the action-\(A\) endpoint is compatible with
nonzero continuation of \(wv\) in the independent angle direction and with
\(A\leftrightarrow\pi-A\) duality. This is a formal germ model, not a
realization of the full \(R_\pi\) barcode or GKS geometry. The first
attempted one-parameter toy,
in which \(uv\) outlived \(u\), was rejected because its transition was not
\(H\)-linear and was not recorded as a result.

### Fixed-input microlocal Hom still creates a boundary class

Audited Asano--Ike's completeness paper, arXiv:2201.02598, Theorem 4.3 and
Corollary 4.5.  After a summable subsequence the limit is an actual translated
homotopy colimit.  Fixing the first input does not make \(\mu hom\)
cocontinuous.

The exact bounded counterexample is
\[
F=\mathbb k_{(0,1)},\qquad G_n=\mathbb k_{(1/n,1)}.
\]
Filtered colimits are exact, so \(\operatorname{hocolim}G_n=F\).  Every
\(G_n\) vanishes near \(0\), hence every finite
\(\mu hom(F,G_n)|_{T^*_0\mathbb R}\) is zero.  But \(F\) is simple on the
negative conormal at \(0\), so \(\mu hom(F,F)\) has a rank-one microstalk
there. The composite is not cocontinuous: the fixed singular sheaf remains a
contravariant internal-Hom test object, and microlocal specialization also
contains an open-embedding \(Rj_*\). External product with a
positive-\(\tau\) factor gives the Tamarkin analogue at any action.

This eliminates the strongest formal colimit shortcut.  A valid
no-ephemeral theorem must use a property special to GKS continuation maps
which excludes this translated-left-front telescope with fixed right cutoff.

### Cross-time envelope countermodel

For
\[
z(t)=\exp\!\left(-t+\frac{i}{20}\sin\frac{\pi t}{\log2}\right)
\]
the moving square with outer vertices \(z,2z\) and inner vertices
\((1+i)z,(2+i)z\) has no outer--inner collision at any two times: the
angular oscillation is at most \(0.1\), while every required constant ratio
has argument at least \(\arctan(1/2)>0.4\).

The triangle
\[
\operatorname{conv}\{0,10e^{i/5},10e^{6i/5}\}
\]
strictly separates the outer and inner vertices.  Nevertheless
\(a(n\log2)=b((n+1)\log2)\), and consecutive outer strands form simple
lenses in disjoint annuli with alternating winding signs.  Thus full
cross-time avoidance and a common endpoint limit do not imply one-sided
envelope winding.

An independent regular-level model
\[
r_N(x,\delta)=e^{2\pi i(x-N\delta)}
\]
has degree one and a single proper level component whose coordinate strands
wind \(N\) and \(N+1\) times.  The regular-level mechanism itself supplies
no coordinate monotonicity.

### Wild collision absorbs odd local square degree

For the square test map
\[
\Psi=(z_1+z_3-z_2-z_4,\,
|z_2-z_1|^2-|z_3-z_2|^2,\,
(z_2-z_1)\cdot(z_3-z_2)),
\]
the explicit square and four prescribed curve tangents in
`angles/wild-configuration-degree/README.md` give
\[
D\Psi=
\begin{pmatrix}
1&-1&-1&1\\
0&-1&1&0\\
-2&4&-2&0\\
0&0&-1&0
\end{pmatrix},
\qquad\det D\Psi=-2.
\]
The determinant was independently recomputed exactly with Python.

Similarity copies of the corresponding embedded bump collapse into the
straight side of a \(1/4\)-Lipschitz Jordan graph with no tangent at the
accumulation point.  The limit germ has no square because any two chord
slopes have absolute value at most \(1/4\) and hence cannot be
perpendicular.  The approximant's local square orbit has mod-two degree one,
while its normalized screen remains the same exact square on one fixed
prime-end side.

For exact squares, failure to converge to a nondegenerate limiting square
forces all four parameters to one parameter of the injective limit.  In
cyclic gap coordinates, three gaps tend to zero and the complementary gap
to one.  The four such vertices are one orbit under cyclic relabelling.
Therefore this unique total-collision orbit really can absorb odd **local**
degree.  No claim is made about the global number of squares on the
approximants.

### Claim boundary, compute, and verification

The three results are no-go theorems, not a proof of Square Peg.  The live
alternatives are now a GKS-specific boundary-exclusion theorem, a genuinely
global two-ended envelope invariant, or a configuration degree with a
nonlocal boundary correction.

GPT-5.6 Sol at xhigh performed the required final adversarial audit. It
corrected the internal-Hom attribution, required the formal two-parameter
module to be fully specified and explicitly non-geometric, fixed the
collision-screen normalization, and tightened three envelope qualifiers.
After those corrections its final verdict was **MERGE**.

All substantive work ran locally in the repository worktree; no private
compute infrastructure was used.  Source downloads were limited to the
official arXiv records for the cited papers.  Commands included:

```text
python3 -m unittest discover -s problems/square-peg/harness -p 'test_*.py' -v
python3 -m py_compile problems/square-peg/harness/geometry.py problems/square-peg/harness/test_geometry.py
xmllint --html --noout problems/square-peg/writeup/report.html problems/square-peg/writeup/artifact-template.html
python3 -c 'import tomllib; tomllib.load(open("problems/square-peg/STATUS.toml","rb")); print("STATUS.toml OK")'
python3 -c 'import sympy as s; ...'
# failed: ModuleNotFoundError: No module named 'sympy'
python3 -c 'import itertools; ...'
# exact determinant output: -2
python3 tools/board.py
git diff --check
```

The rational harness passed 5/5 tests in 0.001 seconds.  Python compilation,
both HTML parses, TOML parsing, board regeneration (19 problems), and
`git diff --check` completed without error.

## 2026-07-24 — unrestricted boundary invariants and conormal forcing

### Wide-net parallel attacks

Ran four independent proof-first tracks, including GPT-5.6 Sol at xhigh:

1. strengthen the missing microlocal telescope theorem using positive GKS
   continuation;
2. extract a two-ended linking invariant from Hugelmeyer's square envelope;
3. resolve total collision and compute the strongest integral equivariant
   square degree; and
4. audit a newly circulated conormal proof of Tao's Conjecture 5.6, then try
   to turn it into an unrestricted planar bridge.

The unrestricted Square Peg conjecture remains open. The session produced
three exact no-go theorems, an independently audited auxiliary proof after a
mandatory sign repair, and a sharply conditional rank-two splice reduction.

### Smooth positive GKS telescope

The generic no-ephemeral theorem is false even after adding the strongest
natural GKS hypotheses. Choose a smooth nonnegative compactly supported
\(g\) with \(g'(0)=1\), put
\[
 f_n(x)=2^{-n}g(2^nx),\qquad
 a_n=\|f_{n+1}-f_n\|_\infty,\qquad
 b_n=\sum_{j\geq n}a_j,
\]
and \(\widetilde f_n=f_n-b_n\). Then
\(\widetilde f_n\uparrow0\), so the canonical positive epigraph maps have
\[
 \operatorname{hocolim}\mathbb k_{\{t\geq\widetilde f_n(x)\}}
 =\mathbb k_{\{t\geq0\}}.
\]
Every finite front has reduced covector \(-1\) at \(x=0\), while the limit
has reduced covector \(0\). Hence every finite fixed-locus microlocal Hom
restriction is zero and the limit restriction has rank one.

Each stage is an invertible compactly supported GKS image generated near the
zero section by \(H_n=f_n\chi(p)\geq0\), with summable Hofer amplitudes.
Thus positivity, invertibility, and summability do not imply cocontinuity.
The only live sheaf theorem is specific to the conjugated quarter-rotation
and requires an explicit calculation of its four-sheet cap continuation
map. Artifact: `angles/gks-positive-telescope/README.md`.

### Exact envelope and collision boundary calculations

For the two exterior envelope strands \(a,b\) and an interior point \(p\),
continuous argument lifts \(A,B\) satisfy
\[
 (B-A)/(2\pi)\longrightarrow n_\pm\in\mathbb Z,
 \qquad n_- - n_+=1.
\]
Thus total outer winding one is exactly an end-order reversal in
\(\operatorname{Conf}_2(S^1)\). The two disjoint proper cylinder arcs
\[
 (0,t),\qquad ((1+e^t)^{-1},t)
\]
realize the same reversal without collision. Ordinary linking, Maslov,
ruled-ribbon intersection, and the normalized cross-ratio therefore do not
close the envelope argument. The missing theorem is end-order rigidity for
compatible boundary-crossing carriers in the full admissible-square space.
Artifact: `angles/envelope-global-linking/README.md`.

For the cyclic equivariant square test, cyclic relabelling reverses the
orientation of the four-parameter domain but acts by \(-I_4\) on the target,
whose determinant is \(+1\). Therefore
\[
 H_0(Q;\mathcal O)\cong\mathbb Z/2.
\]
The resolved total-collision boundary is one circle with trivial restricted
orientation system and hence carries \(\mathbb Z\), but its inclusion is
\(n\mapsto n\bmod2\). The explicit wild motif has exact equivariant
Jacobian determinant \(-8\) and realizes one boundary unit. Pairs change the
resolved integer by two while preserving the global parity, killing
ordinary integral, mod-four, collision-location, finite-screen, and
unfiltered-persistence repairs. Artifact:
`angles/global-collision-charge/README.md`.

### Audit of the July 2026 Tao 5.6 claim

A six-page unrefereed manuscript circulated publicly on 2026-07-15 under the
title *A Conormal Proof of Tao's Alternating-Area Conjecture for Jointly
Inscribed Squares*. It is false as written. It defines
\[
 {\cal A}(\sigma)=-\int_\sigma y\,dx
\]
but its Liouville period, vertical normalization, affine-diagonal
translation, and polygonal correction all use the opposite convention.
For example, its displayed choice \(c_i=-A_i/L\) leaves period
\(-2\epsilon_iA_i\), not zero.

The one-character repair
\[
 {\cal A}(\sigma)=+\int_\sigma y\,dx
\]
matches Tao and makes all subsequent formulas consistent. After that repair,
the matrix identity
\[
 Kp=(b-a,b,0,-a),\qquad \sum p_i=0,
\]
the global exact shear \(\Psi(q,p)=(q-Kp,p)\), the exact essential-circle
Hamiltonian lemma, the product compact-support cutoff, proper conjugation,
the zero-section/conormal PSS theorem, and the embedded polygonal rounding
all passed the audit. GPT-5.6 Sol at xhigh independently returned
**MERGE after the same mandatory sign repair** and found no deeper fatal
gap. This is recorded conservatively as an apparently sound repaired
argument, not established or reviewed literature. Primary comparisons were
Tao's published 2017 paper, Djuretić arXiv:1411.0852v2,
Abbondandolo--Portaluri--Schwarz arXiv:0810.1977, and Hugelmeyer's periodic
theorem arXiv:2407.20412. Artifact:
`literature/TAO56_CLAIM_AUDIT.md`.

### Why the conormal theorem still does not give Square Peg

Horizontal essential circles at heights
\[
 (h_1,h_2,h_3,h_4)=(0,s,3s,2s)
\]
have zero alternating action and the clean family of ordered squares
\[
 (x,0),\ (x+2s,s),\ (x+s,3s),\ (x-s,2s).
\]
Exactness normalization makes the product the zero section against
\(N^*\Delta_v\), so the clean family already carries the complete
\(HF\cong H_*(S^1)\). A small Morse perturbation gives exactly its two
generators. Both exact primitives vanish: normalized Floer action is zero
for every \(s\), while Tao-cylinder (universal-cover) side length is
\(\sqrt5\,s\). Hence both
generators may collide as \(s\to0\) or escape as \(s\to\infty\) with the
same action.

This exact family kills rank two, ordinary action, balanced four-copy
perturbations, affine square-preserving decoders, and finite cyclic covers
as unrestricted bridges. An independent Sol xhigh verdict was **KILL**.
Artifact: `angles/tao-conormal-bridge/README.md`.

A sharper conditional splice reduction survives. Retain four compact arcs
\(\alpha_i\subset C\) with empty common intersection, splice them to four
essential cylinder circles, balance action only in artificial chambers, and
make the product transverse. Put the retained pieces in one lifted disk
whose horizontal plus vertical diameter is smaller than the cylinder
period, excluding wrapped retained squares. If exactly one ordered joint
square uses any artificial piece, rank \(HF=2\) forces a second
all-retained square. Its compact limit is a Euclidean square on \(C\), and
the empty common intersection excludes total collision.

The swallowed-zero graph model gives exactly two transverse artificial
generators before splicing: keep three horizontal graphs and perturb the
fourth by \(\varepsilon g(q)\), where \(g\) has zero mean and two simple
zeros. After choosing the offsets generically, four small windows can be
placed around one zero's base positions while the other remains uniformly
isolated. The unresolved **odd artificial splice lemma** must
construct translation-separated connector corridors and an action-correction
ear with no additional mixed square. In the elementary cylinder square
congruences this is a finite exclusion problem over the fifteen nonempty
tail/core incidence patterns. No genericity claim substitutes for that
certificate. Artifact: `angles/conormal-tail-splicing/README.md`.

The final GPT-5.6 Sol xhigh audit returned **HOLD** on the first draft because
the quotient-injective retained disk did not by itself exclude a wrapped
cylinder square. Adding the explicit horizontal-plus-vertical diameter
bound above repairs the proof: each cylinder congruence is a multiple of
\(L\) with absolute value strictly below \(L\), hence an equality. The audit
also required Hausdorff convergence of the lifted retained pieces, generic
offsets separating the two zeros' base sets, and the
“Tao-cylinder/universal-cover side” wording. After these repairs its verdict
was **MERGE for the conditional reduction and no-go statements**, with the
odd artificial splice lemma still unproved.

### Exact checks, compute, and claim boundary

The harness was run before the attacks and remained conjecture hygiene only.
All substantive work and exact arithmetic ran locally in the repository
worktree; no private compute infrastructure was used. The source audit used
public official papers plus the public images of the unrefereed manuscript.
No author was contacted and no external priority claim was made.

Commands included:

```text
python3 -m unittest discover -s problems/square-peg/harness -p 'test_*.py' -v
python3 -m py_compile problems/square-peg/harness/geometry.py problems/square-peg/harness/test_geometry.py
python3 -c 'from fractions import Fraction; ...'
# Kp = (b-a,b,0,-a); sum p = 0
# equivariant determinant = -8
# corrected normalized periods = (0,0,0,0)
xmllint --html --noout problems/square-peg/writeup/report.html problems/square-peg/writeup/artifact-template.html
python3 -c 'import tomllib; tomllib.load(open("problems/square-peg/STATUS.toml","rb")); print("STATUS.toml OK")'
python3 tools/board.py
git diff --check
```

The unrestricted theorem was not proved. The live ambitious targets are now
either the finite odd-artificial-splice exclusion, a conormal class relative
to a fixed diagonal neighborhood, the square-specific four-sheet GKS cap
map, or end-order rigidity in the full admissible-square space.

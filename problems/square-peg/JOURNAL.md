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

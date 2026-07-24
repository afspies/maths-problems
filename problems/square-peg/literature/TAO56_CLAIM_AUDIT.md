# Audit of the July 2026 claimed proof of Tao's Conjecture 5.6

**Audit date:** 2026-07-24
**Material audited:** the six-page, unrefereed manuscript circulated on
2026-07-15 under the title *A Conormal Proof of Tao's Alternating-Area
Conjecture for Jointly Inscribed Squares* (the manuscript itself says it was
generated on 2026-07-14).
**Status of that manuscript:** an unreviewed claim, not established
literature.

## Verdict: MERGE after mandatory sign repair

The manuscript is **false as written**, because its definition
\[
\mathcal A(\sigma)=-\int_\sigma y\,dx
\tag{1}
\]
is incompatible with its Liouville-period formula (12), normalization (14),
and polygonal correction (24). In particular, the four translated cotangent
circles generally do **not** have zero Liouville period, so the invocation of
the exact-circle lemma and hence the Floer argument do not follow from the
displayed formulas.

This is not a fatal defect in the proposed theorem. The entire sign problem is
repaired by deleting the minus sign in (1), i.e.
\[
\mathcal A(\sigma):=\int_\sigma y\,dx.
\tag{1'}
\]
That change leaves the theorem logically unchanged: replacing every
\(\mathcal A(\sigma_i)\) by its negative does not change whether
\(\mathcal A(\sigma_1)-\mathcal A(\sigma_2)+\mathcal A(\sigma_3)-
\mathcal A(\sigma_4)\) vanishes. With (1') in place, all of the manuscript's
later signs are consistent.

After making that single global repair, the algebraic, exact-symplectic,
Hamiltonian-isotopy, compact-support, conormal-Floer, and smoothing steps all
pass this audit. The core corrected proof is sound at the level checked here,
but the current public version should not be promoted externally to an
established theorem until:

1. a corrected manuscript is issued;
2. the exact-circle isotopy-extension and conormal-Floer statements are cited
   in theorem-level form with their hypotheses and conventions aligned; and
3. an independent expert in cotangent-bundle Floer theory checks the corrected
   version.

Thus the appropriate repository verdict is **MERGE after applying (1')**, not
MERGE-as-written and not KILL. The correction and all dependencies needed for
the corrected proof are explicit in this audit. "MERGE" here is a repository
soundness verdict; it does **not** turn the circulated, unrefereed claim into
established literature.

## 1. Target statement and conventions

Tao's published Conjecture 5.6 says that, for four simple closed polygonal
paths \(\sigma_i\) homologous to the core circle in
\(\operatorname{Cyl}_L=(\mathbb R/L\mathbb Z)\times\mathbb R\), absence of a
jointly inscribed square implies
\[
\int_{\sigma_1}y\,dx-\int_{\sigma_2}y\,dx+
\int_{\sigma_3}y\,dx-\int_{\sigma_4}y\,dx\ne0.
\]
The square locus includes the degenerate case \(a=b=0\). This is exactly the
statement reconstructed in the manuscript, apart from its global choice of a
minus sign in the notation \(\mathcal A\). See Tao, Definition 5.1 and
Conjecture 5.6 in the [published paper][Tao].

Let
\[
Q=(\mathbb R/L\mathbb Z)^4,\qquad
\lambda=\sum_{j=1}^4p_j\,dq_j,\qquad e=(1,1,1,1),
\]
and identify a four-tuple \(z_i=(q_i,y_i)\) with
\[
p=(y_1,-y_2,y_3,-y_4).
\tag{2}
\]
The alternating signs in (2) are essential: the restriction of \(\lambda\)
to the product of the four cylinder curves is the alternating sum of their
\(y\,dx\) forms.

## 2. The sign inconsistency and its exact repair

### 2.1 What is wrong as written

Write \(\epsilon=(1,-1,1,-1)\) and
\[
L_i=\{(q_i,p_i)=(x,\epsilon_i y):(x,y)\in\sigma_i\}\subset T^*S^1.
\]
Under the manuscript's displayed definition (1),
\[
\int_{L_i}p_i\,dq_i
=\epsilon_i\int_{\sigma_i}y\,dx
=-\epsilon_i\mathcal A(\sigma_i),
\tag{3}
\]
not \(+\epsilon_i\mathcal A(\sigma_i)\) as claimed in (12).

The manuscript then translates the original curve vertically by
\[
c_i=-\frac{\mathcal A(\sigma_i)}L.
\]
This shifts \(p_i\) by \(\epsilon_i c_i\), so its new Liouville period is
\[
-\epsilon_i\mathcal A(\sigma_i)+\epsilon_i c_iL
=-2\epsilon_i\mathcal A(\sigma_i),
\]
not zero. Therefore the sentence immediately after (14), asserting that each
translated factor is exact, is false under (1).

The same mismatch appears in Section 6. Under (1), upward translation by
\(h\) gives
\[
\mathcal A(\sigma+(0,h))
=-\int_\sigma(y+h)\,dx
=\mathcal A(\sigma)-hL,
\tag{4}
\]
whereas the manuscript uses \(+\;hL\).

### 2.2 The one-character repair

With (1') instead,
\[
\int_{L_i}p_i\,dq_i=\epsilon_i\mathcal A(\sigma_i).
\]
Translation by \(c_i=-\mathcal A(\sigma_i)/L\) shifts the period by
\(-\epsilon_i\mathcal A(\sigma_i)\), making it zero. The combined momentum
shift is exactly the manuscript's
\[
v=\frac1L(-A_1,A_2,-A_3,A_4),
\tag{5}
\]
and the zero alternating-area hypothesis gives
\[
\langle v,e\rangle
=\frac{-A_1+A_2-A_3+A_4}{L}=0.
\]
Upward translation changes the corrected action by \(+hL\), so the Section 6
choice \(h_n=\delta_n/L\) and the identity \(\delta_n-h_nL=0\) also become
correct.

Equivalently, one may retain (1), but then (12), (14), (15), and (24) must all
be sign-reversed:
\[
c_i=+\frac{A_i}{L},\qquad
v=\frac1L(A_1,-A_2,A_3,-A_4),\qquad
h_n=-\frac{\delta_n}{L}.
\]
Both repairs prove precisely the same zero/nonzero theorem. The first is
cleaner because it matches Tao's convention.

## 3. Exact audit of the square-conormal dictionary

The matrix
\[
K=
\begin{pmatrix}
0&-1&0&1\\
-1&-1&0&0\\
0&0&0&0\\
1&0&0&1
\end{pmatrix}
\]
is symmetric. Define
\[
\Psi(q,p)=(q-Kp,p).
\]
This is globally well-defined on \(T^*Q\): the base coordinate is reduced
modulo \(L\), the fiber coordinate remains real, and the inverse is
\((q,p)\mapsto(q+Kp,p)\). No lift of \(q\) is being chosen.

For a square
\[
\begin{aligned}
z_1&=(x,y),&
z_2&=(x+a,y+b),\\
z_3&=(x+a-b,y+a+b),&
z_4&=(x-b,y+a),
\end{aligned}
\]
(2) gives
\[
p=(y,-y-b,y+a+b,-y-a).
\]
Direct multiplication gives
\[
Kp=(b-a,b,0,-a),\qquad
q-Kp=(x+a-b)e,\qquad
\langle p,e\rangle=0.
\tag{6}
\]
Thus \(\Psi(q,p)\in N^*\Delta\), where
\(\Delta=\{te:t\in\mathbb R/L\mathbb Z\}\).

Conversely, from \(\langle p,e\rangle=0\) and \(q-Kp=te\), set
\[
x=q_1,\quad y=p_1,\quad
b=-p_2-p_1,\quad a=-p_4-p_1.
\]
Then \(p_3=y+a+b\), while the four base equations give, modulo \(L\),
\[
q_2-q_1=a,\qquad q_3-q_2=-b,\qquad q_4-q_3=-a.
\]
These are exactly Tao's square equations on the cylinder. Consequently
\[
\operatorname{Squares}_L=\Psi^{-1}(N^*\Delta)
\tag{7}
\]
under (2), including the degenerate stratum. The fact that \(a,b\) are real
causes no global ambiguity: their values are recovered from the real fiber
coordinates, and the base equations are supposed to hold modulo \(L\).

**Verdict on Lemma 2.1:** correct.

## 4. Exact-symplectic shear

Because \(K=K^\mathsf T\),
\[
\Psi^*\lambda-\lambda
=-\langle p,K\,dp\rangle
=-d\!\left(\frac12\langle p,Kp\rangle\right).
\tag{8}
\]
Hence \(\Psi\) is an exact symplectomorphism and fixes the zero section.
It is also proper: it leaves \(p\) unchanged, and \(Q\) is compact. This last
point matters later, because conjugating a compactly supported Hamiltonian
diffeomorphism by \(\Psi\) still has compact support.

The argument needs neither invertibility of \(K\) nor compact support of
\(\Psi\) itself.

**Verdict on (6)--(8):** correct.

## 5. Exact essential circles in \(T^*S^1\)

The manuscript's Lemma 3.1 is the one-dimensional nearby-Lagrangian fact it
actually needs:

> A smooth embedded essential circle \(C\subset T^*S^1\) with
> \(\int_Cp\,dq=0\) is the image of the zero section under a compactly
> supported Hamiltonian isotopy.

The proposed proof is sound once its standard extension lemma is stated
precisely.

1. By classification/isotopy extension for the open annulus, \(C\) is joined
   to the core circle by a smooth isotopy \(C_t\) through embedded essential
   circles.
2. If \(a(t)=\int_{C_t}p\,dq\), vertical translation by \(-a(t)/L\) changes
   this period by \(-a(t)\), since every oriented essential circle has
   \(\int dq=L\). The endpoints stay fixed because \(a(0)=a(1)=0\).
3. For a parametrization \(i_t:S^1\to T^*S^1\) of the corrected family and
   variational vector field \(X_t\), Cartan's formula gives
   \[
   \frac d{dt}i_t^*\lambda
   =d(i_t^*\lambda(X_t))+i_t^*(\iota_{X_t}d\lambda).
   \]
   Since \([i_t^*\lambda]=0\) for every \(t\), the closed one-form
   \(i_t^*(\iota_{X_t}d\lambda)\) is exact. This is exactly zero Lagrangian
   flux.
4. The Lagrangian-isotopy extension theorem therefore produces an ambient
   Hamiltonian isotopy agreeing with the prescribed motion on \(C_t\).
   The trace is compact. Multiplying the extension Hamiltonian by a cutoff
   identically one on a neighborhood of the trace preserves its vector field
   along the trace and makes the Hamiltonian compactly supported.

The manuscript should replace its bare section citation by a precise
isotopy-extension citation or include the four-line flux argument above.
That is a presentation requirement, not a detected mathematical gap.

**Verdict on Lemma 3.1:** correct after citation-level tightening.

## 6. Translation to the affine conormal

Use the corrected action convention (1'). Let \(p\) be the alternating
momentum before normalization and \(p'=p+v\) after it, with \(v\) as in (5).
The alternating-area hypothesis gives \(\langle v,e\rangle=0\), so
\[
\langle p,e\rangle=0\quad\Longleftrightarrow\quad
\langle p',e\rangle=0.
\tag{9}
\]
Moreover
\[
q-Kp\in\Delta
\quad\Longleftrightarrow\quad
q-Kp'=q-Kp-Kv\in\Delta-Kv=:\Delta_v.
\tag{10}
\]
Since translation does not change tangent spaces,
\[
N^*\Delta_v
=\{(te-Kv,p):\langle p,e\rangle=0\}.
\]
Equations (9)--(10), together with (7), prove the claimed exact
correspondence
\[
\{\text{squares on the original curves}\}
\longleftrightarrow
\widetilde L\cap\Psi^{-1}(N^*\Delta_v).
\tag{11}
\]

**Verdict on Lemma 4.1:** correct after repairing the global action sign.

## 7. Product Hamiltonian and compact support

For each exact factor \(\widetilde L_i\), Lemma 3.1 gives a compactly
supported Hamiltonian isotopy \(\phi_{i,t}\) from the zero section to
\(\widetilde L_i\). Their product \(\Phi_t=\prod_i\phi_{i,t}\) carries the
zero section \(O_Q\) to \(\widetilde L=\prod_i\widetilde L_i\).

The sum of the four factor Hamiltonians is generally not compactly supported
on the full product, because a term depending on one factor is constant in
the other three fiber directions. The manuscript notices this and its repair
is valid. The trace
\[
\mathcal K=\bigcup_{t\in[0,1]}\Phi_t(O_Q)
\]
is compact, since \(O_Q\times[0,1]\) is compact. Choose a smooth compactly
supported \(\chi\) equal to one on an open neighborhood of \(\mathcal K\).
Then \(d\chi=0\) near the trace, so the Hamiltonian vector fields of \(H_t\)
and \(\chi H_t\) agree there. Uniqueness of ODE solutions shows that the
cutoff flow has the same restriction to \(O_Q\).

Conjugation is also safe. Since \(\Psi\) is a proper symplectomorphism fixing
\(O_Q\),
\[
\Psi(\widetilde L)
=(\Psi\phi\Psi^{-1})(O_Q),
\]
and the conjugate is Hamiltonian with compact support
\(\Psi(\operatorname{supp}\phi)\).

**Verdict on (19)--(20) and the compact-support discussion:** correct.

## 8. Zero-section/conormal Floer step

The required theorem is standard but should be stated with conventions
matching the application. For a closed manifold \(M\), a closed submanifold
\(N\subset M\), and a compactly supported Hamiltonian \(H\) for which the
relevant intersection is transverse, conormal PSS gives, over
\(\mathbb Z/2\),
\[
HF_*(\phi_H^1(O_M),N^*N)\cong H_*(N;\mathbb Z/2)
\tag{12}
\]
up to the grading convention. Equivalently, one may use Hamiltonian chords
starting on \(O_M\) and ending on \(N^*N\). This is the local-boundary
specialization of conormal Floer theory; the associated path space is
homotopy equivalent to \(N\). See [Djuretić][Dju] and
[Abbondandolo--Portaluri--Schwarz][APS].

Here \(M=Q\) is closed and \(N=\Delta_v\cong S^1\) is closed. Thus the
right-hand side is nonzero. If the unperturbed compact Lagrangian
\(\Psi(\widetilde L)\) were disjoint from the closed conormal
\(N^*\Delta_v\), the positive distance between them would keep all
sufficiently small compactly supported perturbations disjoint, contradicting
(12). Exactness rules out disc bubbling, and the conical behavior of the
conormal together with compactness of the other Lagrangian gives the standard
Floer compactness at infinity.

The 2008 paper is much more general than needed and its path-space statement
should not be quoted as though it literally prints (12) in the manuscript's
notation. Djuretić is the more direct citation for the zero-section/conormal
PSS formulation. This is a citation-precision issue; the non-displacement
consequence used here is valid.

Combining the forced intersection with (11) proves the corrected smooth
statement.

**Verdict on (21)--(22):** correct, with a request for a precise theorem
citation and convention check in the revised manuscript.

## 9. Smoothing and limiting argument

The polygonal passage is valid after the action-sign repair.

- A simple polygonal essential circle has only finitely many corners.
  After deleting redundant collinear vertices, choose disjoint sufficiently
  small neighborhoods of its vertices, smaller than the positive separation
  from all nonincident edges, and round within those neighborhoods. This
  produces smooth embedded essential circles; embeddedness is not being
  assumed after arbitrary mollification.
- The rounded curves converge in Hausdorff distance and stay in one compact
  vertical strip. Their actions converge because each replacement arc has
  coordinate diameter tending to zero and there are finitely many arcs.
- With
  \[
  \delta_n=A_{1,n}-A_{2,n}+A_{3,n}-A_{4,n},\qquad
  h_n=\delta_n/L,
  \]
  translating only the fourth curve upward by \(h_n\) changes its corrected
  action by \(h_nL\), so the new alternating action is
  \(\delta_n-h_nL=0\). Also \(h_n\to0\), and vertical translation preserves
  embeddedness and essentiality.
- The four selected vertices lie in a common compact subset of the cylinder.
  A subsequence converges to points on the original polygonal images.
  Tao's closed square locus is genuinely closed: from its four vertical
  coordinates one recovers \(a=y_4-y_1\) and \(b=y_2-y_1\), so \(a,b\) cannot
  escape while the vertices remain in a compact strip. Degenerate limiting
  squares are allowed by Definition 5.1.

**Verdict on Section 6:** correct after repairing the global action sign.

## 10. Relation to Hugelmeyer's periodic theorem

Hugelmeyer proves the periodic square-peg theorem for two disjoint periodic
Jordan strands, first smoothly on a symplectic four-torus and then for
continuous embeddings. His geometric Lagrangians are built from the two
curves and a square rotation map. See [Hugelmeyer, Theorems 1--2][Hugel].

The present claim is not merely a restatement of that theorem:

- it treats four arbitrary essential cylinder curves, which may overlap;
- its hypothesis is a single alternating action identity;
- it identifies the full four-curve square locus with a sheared conormal in
  \(T^*((S^1)^4)\); and
- its non-displacement input is zero-section versus conormal, rather than the
  pair of tori used in Hugelmeyer's periodic proof.

Conversely, the strongest already-established consequence is not new:
specializing Tao's four curves to
\((\sigma_1,\sigma_1,\sigma_2,\sigma_2)\) makes the alternating action vanish
identically and recovers the quadripartite/periodic problem. Hugelmeyer already
proved that periodic theorem, including the continuous disjoint-strand case.

Targeted searches through 2026-07-24 found no reviewed source proving Tao's
full four-curve Conjecture 5.6 and no indexed prior use of this exact shear
and affine-conormal reduction. Search coverage is not a priority proof.
Accordingly, the safe novelty description is:

> an unreviewed, apparently new conormal-Floer proof strategy for Tao's
> four-curve area-inequality conjecture, correct-looking after a global sign
> repair.

It must not be described as established or as having priority over any
unindexed work.

## 11. Does it advance unrestricted Square Peg?

Not by itself. Tao explicitly records that Conjecture 5.6 implies his other
auxiliary conjectures but not the unrestricted Toeplitz conjecture. The
manuscript proves, at most, the auxiliary cylinder statement. It supplies no
construction that takes an arbitrary planar Jordan curve to four essential
cylinder curves satisfying the alternating action identity, and it supplies
no argument excluding the degenerate intersection allowed in Tao's closed
square locus.

The potentially useful new module is narrower:

> whenever an unrestricted strategy can produce four essential cylinder
> strands with exactly balanced alternating Liouville periods, the corrected
> conormal argument forces an intersection without requiring transversality of
> the original curves.

To affect unrestricted Square Peg, one still needs a bridge producing those
strands with exact action balance and showing that the forced intersection
pulls back to a nondegenerate planar square. Neither Hugelmeyer's square
envelope nor the current Greene--Lobb/Asano--Ike approximation machinery
automatically provides that bridge. The claim therefore does not close any of
the repository's current total-collision, shrink-out, or null-trace
obstructions.

In microlocal language, the mechanism is static and points in the opposite
direction from the unrestricted diagonal-vanishing target: the shear turns the
square relation into \(N^*\Delta_v\), and the nonzero class
\(H_*(\Delta_v)\) forces some intersection. It neither removes the degenerate
diagonal class nor controls a continuation telescope as the four vertices
collide. The forced Floer generator may therefore be supported entirely on
the degenerate stratum in an unrestricted limiting construction.

## 12. Independent adversarial second opinion

As required by `AGENTS.md`, GPT-5.6 Sol at xhigh effort independently checked
the sign repair, the matrix/shear calculation, the exact-circle lemma, the
product cutoff, compact support after conjugation, Djuretić's conormal PSS
theorem, the nontransverse perturbation, smoothing, and the Hugelmeyer
comparison. Its verdict was:

> **MERGE after one global sign repair; no deeper fatal gap found.**

It independently selected the same repair (1') and emphasized the same
unrestricted obstruction: the conormal class forces an intersection but does
not exclude its lying on Tao's allowed degenerate diagonal.

## 13. Audit disposition

| Item | Result |
|---|---|
| Statement matches Tao 5.6 | Yes, modulo the global action sign |
| Square/conormal algebra | Pass |
| Global torus definition of the shear | Pass |
| Exact symplectic calculation | Pass |
| Exact essential-circle lemma | Pass, citation should be sharpened |
| Vertical normalization | **Fail as written; repaired by (1')** |
| Translation to affine conormal | Pass after sign repair |
| Product compact-support cutoff | Pass |
| Compact support after conjugation | Pass |
| Zero-section/conormal Floer non-displacement | Pass, theorem citation should be sharpened |
| Polygonal embedded smoothing | Pass |
| Action correction and closed-locus limit | Pass after sign repair |
| Subsumed by Hugelmeyer | No; stronger four-curve auxiliary statement |
| Solves unrestricted Square Peg | No |
| Final verdict | **MERGE after mandatory repair (1'); not correct as circulated** |

## Primary sources

- [T. Tao, *An integration approach to the Toeplitz square peg problem*,
  Forum Math. Sigma 5 (2017), e30][Tao].
- [J. Djuretić, *Piunikhin--Salamon--Schwarz isomorphisms and spectral
  invariants for conormal bundle*, arXiv:1411.0852v2][Dju].
- [A. Abbondandolo, A. Portaluri, and M. Schwarz, *The homology of path
  spaces and Floer homology with conormal boundary conditions*,
  arXiv:0810.1977][APS].
- [C. Hugelmeyer, *A Solution to the Periodic Square Peg Problem*,
  arXiv:2407.20412][Hugel].

[Tao]: https://doi.org/10.1017/fms.2017.23
[Dju]: https://arxiv.org/abs/1411.0852
[APS]: https://arxiv.org/abs/0810.1977
[Hugel]: https://arxiv.org/abs/2407.20412

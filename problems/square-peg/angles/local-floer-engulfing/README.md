# Local Floer engulfing at the diagonal

## Proposed shortcut

Let
\[
 L=C_0\times C_0,\qquad
 Q=(\phi\times\phi)^{-1}R_{\pi/2}(\phi\times\phi),
\]
where \(\phi\) is a compactly supported area-preserving homeomorphism
taking the standard circle to a planar-null Jordan curve.  The Hamiltonian
\[
 H^\phi(z,w)=|\phi(z)-\phi(w)|^2/4
\]
vanishes on the diagonal.  Cutting it off in a thin invariant diagonal
tube produces a topological Hamiltonian with arbitrarily small oscillation
and the same shrinking diagonal dynamics.

Oh's localization theorem for engulfable Hamiltonian paths
\cite{OhLocalization} is therefore a natural candidate for replacing the
uncontrolled global limit by local Floer homology in a fixed Darboux
neighborhood.

## What Oh's theorem actually controls

For a compact Lagrangian \(K\), a \(V\)-engulfable isotopy keeps the entire
path \(\phi_H^t(K)\) in a fixed Darboux neighborhood \(V\) of \(K\).  If the
time-one map is sufficiently \(C^0\)-small, a maximum principle separates
Floer strips contained in \(V\) from strips leaving \(V\).  The resulting
local Floer homology is continuation invariant and, along a full
engulfable homotopy from the identity, is isomorphic to \(H_*(K)\).

The source explicitly emphasizes the limitation relevant here:

- a thin strip may have large symplectic area;
- the maximum-principle thick--thin decomposition does not respect the
  action-filtration decomposition;
- even as the time-one maps tend uniformly to the identity there is no
  uniform filtration gap, no uniform action bound for local chords, and no
  control of the filtration change of the local continuation map.

Oh also proves equality of a local and global Lagrangian spectral invariant
for the **fundamental class** of a cotangent zero section, provided the
Hamiltonian is joined to zero through a full engulfable family. Under those
cotangent and engulfability hypotheses the proof identifies the relevant
local and global complexes. It does not identify Asano--Ike's twisted
\(v\)-complex or compare it across the non-engulfable change from the
original relative rotation to the small cutoff.

## Why the fundamental-class refinement does not apply

Asano--Ike's critical value does filter a distinguished class, but it is
not Oh's clean-diagonal fundamental class.  Their microlocalization map is
\[
 H^*(S^1)\simeq\operatorname{End}(F_0)
 \longrightarrow H^*(C_0\times C_0),
 \qquad
 v\longmapsto v\otimes1+1\otimes v.
\]
On the diagonal circle this class restricts to
\[
 v+v=0
\]
over \(\mathbb F_2\).  Thus the degree-one class defining
\(a(\theta,C)\) has zero ordinary clean-diagonal localization.  In
contrast, Oh's theorem controls the top class of the whole Lagrangian zero
section.  For the ordinary torus \(L=C_0\times C_0\), that theory has
\(H^*(T^2)\), whereas the twisted/bounding-cochain quantization \(F_0\)
used by Asano--Ike has
\(\operatorname{End}(F_0)\simeq H^*(S^1)\).

There are two further geometric mismatches.

1. A cutoff which becomes the identity away from the diagonal creates a
   large clean intersection outside the desired component.  The diagonal
   circle is an isolated clean component of the original pair, not the
   whole Lagrangian zero section to which Oh's fundamental-class
   comparison applies.
2. The cutoff path is engulfable, but a homotopy from the original relative
   rotation to that cutoff need not be engulfable.  Local continuation
   invariance cannot be invoked across precisely the transition whose
   action is uncontrolled.

## Exact two-parameter module countermodel

The distinction between a controlled fundamental class and an uncontrolled
critical endpoint is already visible algebraically, but the action and angle
directions must not be conflated.  Let
\[
 H=\mathbb k[v]/(v^2),\qquad |v|=1,
\]
and choose \(0<B<A<\pi\).  At the square angle define the action-depth
persistence module
\[
 M_r=
 \begin{cases}
 H u,&r<B,\\
 H/(v)\,u,&B\leq r<A,\\
 0,&r\geq A.
 \end{cases}
\]
The map at \(B\) is the \(H\)-linear quotient and the map at \(A\) is zero.
Consequently:

- the distinguished class \(u\) has its critical endpoint at the arbitrary
  interior action \(A\);
- the associated-graded endpoint is \(\mathbb k u\) and \(v\) acts by zero
  there;
- for an infinitesimal depth \(r<B\), a lift \(w=u\) still satisfies
  \(wv=uv\neq0\).

Make this a two-parameter module by setting
\[
 N_{r,\theta}=M_r\qquad
 (\pi/2\leq\theta\leq\pi)
\]
and taking every angle-continuation map to be the identity.  Then
\[
 c(w)v=c(wv)\neq0
\]
after continuation to \(\pi\). There is no requirement that \(wv\) survive
beyond \(A\) in the action-depth direction.  Finally take
\(N\oplus RD N\), where \(R(r)=\pi-r\), to add the complementary endpoint
\(\pi-A\).

Thus zero \(v\)-action on the critical diagonal graded piece, square-angle
duality, and nonzero continuation of \(wv\) to angle \(\pi\) are mutually
compatible at the level of the formal persistence germs used by the proposed
argument. This model does not claim to realize the full standard
\(R_\pi\) barcode or GKS geometry. It proves only that the cited formal
module, product, and duality constraints do not force the desired
vanishing. Controlling one clean/fundamental spectral class does not exclude
the required exact-action defect.

## Fixed-first-input homotopy colimits still fail

The completeness theorem represents a Cauchy limit, after passing to a
summable subsequence, by an actual translated homotopy colimit.  Conjugation
also fixes the first input:
\[
 \mu hom(F_0,R_\theta^{\phi_n}F_0)
 \longrightarrow
 \mu hom(F_0,R_\theta^\phi F_0).
\]
It is therefore tempting to hope that the bounded constructibility of
\(F_0\) makes \(\mu hom(F_0,-)\) commute with this homotopy colimit.  Even
that one-variable statement is false.

On \(X=\mathbb R\), take the bounded constructible sheaves
\[
 F=\mathbb k_{(0,1)},\qquad
 G_n=\mathbb k_{(1/n,1)}
\]
with the natural extension maps \(G_n\to G_{n+1}\).  Filtered colimits are
exact for sheaves of vector spaces, hence
\[
 \operatorname*{hocolim}_n G_n\simeq
 \mathbb k_{(0,1)}=F.
\]
Every \(G_n\) vanishes on a neighborhood of \(0\), so
\[
 \mu hom(F,G_n)|_{T^*_0X}=0.                             \tag{1}
\]
In the limit, \(F\) is simple along the negative conormal ray at \(0\), and
the standard simplicity calculation gives
\[
 \mu hom(F,F)_{(0;\xi)}\simeq\mathbb k
 \quad(\xi<0)                                             \tag{2}
\]
up to the universal grading convention.

Thus a new boundary microlocal class can appear in a homotopy colimit even
when the first input is fixed, bounded, constructible, and finite-stalk. In
the formula
\[
 \mu hom(F,G)=\mu_\Delta
 R\mathcal Hom(q_2^{-1}F,q_1^!G),
\]
there is no generic cocontinuity theorem: the fixed sheaf is still a
contravariant test object for internal Hom, and microlocal specialization
itself contains an open-embedding \(Rj_*\). Indeed, the finite internal-Hom
germs at \(0\) vanish while the limiting self-Hom germ contains the identity.
The left fronts of the \(G_n\) are translates, with a fixed right cutoff.
External products and action translations place the same defect
over a compact diagonal and at any chosen action.  This is the elementary
sheaf model of the class created when supports concentrate at a wild prime
end.  A valid preservation theorem therefore needs a uniform microlocal
neighborhood gap, which the null spiral does not have.

## Verdict

**Dead as a direct proof; useful localization no-go.** Oh's theorem supplies
a local complex and a fundamental-class comparison under its full
engulfability hypotheses, but it neither controls Asano--Ike's twisted
\(v\)-class nor compares the original rotation with the cutoff. The
remaining theorem is still telescope-specific:
the cross-stage continuation system of interior-action groups concentrating
at the diagonal must be pro-zero (or have vanishing Milnor term).

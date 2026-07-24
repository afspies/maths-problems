# Exact reductions for the connected terminal branch

The full connected non-pyramidal Mahler problem remains open. This note
records two exact reductions and one obstruction which sharply delimit the
remaining proof.

## 1. The polarity pairing is circuit-harmonic

Let

\[
U=(1,x_v)_{v\in V(P)},\qquad
V=(1,y_F)_{F\in\mathcal F(P)}
\]

and let \(D_P\) stack all facet-supported affine circuit rows. Every row
\(\alpha\) satisfies

\[
\alpha^\mathsf T\mathbf1=0,\qquad
\alpha^\mathsf TX=0.
\]

For a terminal polytope, the unwaived circuit equations have rank
\(f_0-5\), so

\[
\ker D_P=\operatorname{col}U.
\]

Put \(N_{vF}=x_v\cdot y_F\) and
\(L=\mathbf1\mathbf1^\mathsf T-N\). Then, identically,

\[
\boxed{
D_PN=D_PL=0,\qquad
ND_{P^\circ}^\mathsf T=LD_{P^\circ}^\mathsf T=0.
}
\]

Thus the polarity and slack matrices lie entirely in the affine harmonic
spaces. A circuit Poincare inequality of the form

\[
\|N\|^2\le C\bigl(
\|D_PN\|^2+\|ND_{P^\circ}^\mathsf T\|^2
\bigr)
\]

has zero right-hand side and cannot control \(N\). Connected circuit
support removes nontrivial labeled projective stabilizers, but supplies no
spectral control of these affine zero modes.

## 2. The corrected volume-mass and determinant targets

For a vertex triangulation, let \(R_S\) select a 4-simplex and put
\(G=I_5+\mathbf1\mathbf1^\mathsf T\). Define

\[
\mathsf M_P
=
\sum_S\frac{|S|}{|P|}R_SGR_S^\mathsf T.
\]

The barycentric second-moment formula gives, for every bi-centered polar
pair,

\[
\boxed{
900\operatorname{tr}\bigl(
\operatorname{cov}P\operatorname{cov}P^\circ
\bigr)
=
\operatorname{tr}\bigl(
\mathsf M_PN\mathsf M_{P^\circ}N^\mathsf T
\bigr).
}
\]

The connected trace-gap conjecture is therefore a comparison of the two
volume-derived mass forms on the four-dimensional nonconstant affine
harmonic spaces.

For simplex cells \(S=(x_0,\ldots,x_4)\) and
\(T=(y_0,\ldots,y_4)\), write

\[
L_{ST}=(1-x_i\cdot y_j)_{i,j=0}^4.
\]

If \(U_S\) and \(V_T\) are their homogeneous vertex matrices, then

\[
L_{ST}=U_S\operatorname{diag}(1,-I_4)V_T^\mathsf T.
\]

Consequently

\[
\boxed{
|\det L_{ST}|=(4!)^2|S||T|
}
\]

and the trace target is exactly

\[
\boxed{
\sum_{S,T}|\det L_{ST}|
\bigl(E(S,T)-100\bigr)<0.
}
\]

This is a genuinely global statement. For the canonical pulling
triangulations of the regular 24-cell, exact arithmetic gives

```text
simplex pairs                         5184
pairs with E > 100                    1784
maximum E                              344
determinant-weighted average E       169/2
```

Thus cellwise control is false even for a connected terminal example.

There is a sharper facet-level integration-by-parts form. Let \(r_F\) be
the cone-volume probability of a primal facet \(F\), let \(s_v\) be the
corresponding probability of the polar facet dual to \(v\), and let
\(c_F,d_v\) and \(H_F,H_v^\circ\) be their centroids and uncentered second
moments. The divergence theorem gives the dual-frame identities

\[
4\sum_F r_Fc_Fy_F^\mathsf T=I,\qquad
4\sum_v s_vd_vx_v^\mathsf T=I.
\]

Therefore

\[
\boxed{
\frac14-\frac94\operatorname{tr}\bigl(
\operatorname{cov}P\operatorname{cov}P^\circ
\bigr)
=
\sum_{F,v}r_Fs_v
\left[
(x_v\cdot y_F)(c_F\cdot d_v)
-\operatorname{tr}(H_FH_v^\circ)
\right].
}
\]

This is exactly the trace defect for the two cone measures on the
boundaries. At the regular 24-cell, the 576 unweighted brackets split into
288 values \(-11/100\) and 288 values \(3/16\); all 144 incidences are
positive, but the total is only \(31/800\). Hence even facet-pair positivity
is false. The unresolved target is a global transport inequality making the
connected circuit network's positive incidence contribution dominate its
negative nonincidences.

## 3. Exact constrained Santaló Hessian

In paired incidence coordinates let

\[
F_{vF}(x,y)=x_v\cdot y_F-1,\qquad
J=DF,\qquad T=\ker J.
\]

For \(u=(a_v,b_F)\in T\), define

\[
c(u,u)_{vF}=a_v\cdot b_F,\qquad
q_\omega(u)=\omega\cdot c(u,u)
\quad(\omega\in\ker J^\mathsf T).
\]

Suppose a bi-centered realization is constrained-critical and choose a KKT
multiplier with the sign convention

\[
g=\nabla(\log|P|+\log|P^\circ|)=J^\mathsf T\lambda.
\]

If \(H_0\) denotes the straight ambient Hessian after eliminating the
moving Santaló point, then every second-liftable incidence tangent satisfies

\[
\boxed{
Q_\lambda(u)=H_0(u)-2q_\lambda(u).
}
\]

Indeed, an actual acceleration \(h=z''(0)\) obeys

\[
Jh=-2c(u,u),
\]

and hence \(g\cdot h=-2q_\lambda(u)\). If \(\lambda\) is changed by a
self-stress, the displayed value is unchanged on the stress cone
\(q_\omega(u)=0\).

The KKT equations are the bipartite equilibrium system

\[
\nabla_{x_v}\log|P|
=\sum_{F\ni v}\lambda_{vF}y_F,\qquad
\nabla_{y_F}\log|P^\circ|
=\sum_{v\in F}\lambda_{vF}x_v.
\]

Euler homogeneity gives the exact global check

\[
\sum_{(v,F)}\lambda_{vF}=4.
\]

## 4. Projective-radical stress lemma

For every self-stress \(\omega\in\ker J^\mathsf T\), the polarization
\(B_\omega\) of \(q_\omega\) satisfies

\[
\boxed{
B_\omega(p,u)=0
\quad
(p\in T_{\rm PGL},\ u\in T).
}
\]

To prove this, use the self-stress equilibrium equations

\[
\sum_{F\ni v}\omega_{vF}y_F=0,\qquad
\sum_{v\in F}\omega_{vF}x_v=0.
\]

Substitution of the three projective generator types

\[
(Ax,-A^\mathsf Ty),\qquad
(t,-(t\cdot y)y),\qquad
(-(r\cdot x)x,r)
\]

reduces every term to these equations and the tangent incidences
\(y_F\cdot a_v+x_v\cdot b_F=0\).

Therefore the stress cone and q-regularity descend to \(T/T_{\rm PGL}\),
even though Mahler volume is invariant only under the 20-dimensional
affine subgroup.

## 5. Second-fundamental spanning lemma

Let \(q:V\to W\) be homogeneous quadratic, let \(q(u)=0\), and suppose
\(Dq_u\) is onto. Put \(L=\ker Dq_u\). If

\[
\boxed{
\operatorname{span}\{q(v):v\in L\}=W,
}
\]

then every sufficiently small neighborhood of \(u\) in the regular zero
locus of \(q\) linearly spans \(V\).

Indeed, a tangent \(v\in L\) has a curve

\[
\gamma_v(t)=u+tv+\frac{t^2}{2}h_v+O(t^3)
\]

in the regular zero locus. Twice differentiating gives

\[
Dq_u h_v=-2q(v).
\]

The local germ's linear span contains \(L\) and all \(h_v\). Since
\(Dq_u:V/L\to W\) is an isomorphism, the displayed hypothesis supplies
every normal class.

For a singular incidence realization, this criterion closes the KKT gap.
Every nearby regular zero integrates to a two-sided analytic incidence arc.
If their germ spans \(T=\ker J\), first-order vanishing at a local minimum
forces the objective gradient into \(T^\perp=\operatorname{im}J^\mathsf T\),
so the incidence multiplier used above genuinely exists.

At the rational nonregular Paffenholz 24-cell, the exact q-regular witness
has

\[
\dim T=50,\qquad
\dim\Omega=2,\qquad
\dim\ker Dq_u=48.
\]

The exact quadratic outputs of that 48-dimensional kernel have rank two;
already the second and third deterministic basis vectors give rank two.
Consequently the local q-regular germ spans all 50 incidence-tangent
dimensions. Since the 24 PGL directions lie in \(\ker Dq_u\), the same
statement spans the full 26-dimensional realization-moduli quotient.

After quotienting affine gauges, split

\[
T/T_{\rm aff}=D\oplus R,
\]

where \(D\) contains the four denominator-projective directions. Then

\[
q(d+r)=q(r)
\]

and the constrained Hessian has blocks

\[
\begin{pmatrix}A&B\\B^\mathsf T&C\end{pmatrix}.
\]

When \(A\succ0\), the correct moduli form is the Schur complement

\[
C-B^\mathsf TA^{-1}B.
\]

The projective block is intrinsically

\[
A=
30\operatorname{cov}(P)
-\frac56\operatorname{cov}(P^\circ)^{-1}.
\]

Thus the trace gap supplies a negative direction already in \(D\), while a
candidate passing the covariance test must be attacked on the q-regular
moduli cone through the Schur complement.

## 6. Exact regular-24-cell certificate

At the regular 24-cell, the deterministic exact KKT multiplier has

```text
incidences                       144
nonzero multiplier entries      120
global multiplier sum             4
minimum                         -7/48
maximum                          7/48
```

For the four denominator-projective directions and the four Paffenholz
realization directions, exact polarization gives

\[
\boxed{
A=-\frac{31}{13}I_4,\qquad
B=-\frac{31}{78}I_4,\qquad
C=-\frac{61}{234}I_4.
}
\]

In particular \(B\ne0\): discarding all 24 projective directions would
change the realization Hessian. The harness also verifies the
projective-radical stress lemma on exact tangent and stress bases at both
the regular and the rational nonregular Paffenholz 24-cells.

Finally, the interval bi-centering certificate for the nonregular
Paffenholz class proves the unique root is connected and pair-terminal on
both sides, and

\[
0.0999343391445795
<
\operatorname{tr}(
\operatorname{cov}P\operatorname{cov}P^\circ)
<
0.0999343606091986
<
\frac19.
\]

Thus the exact connected pair-terminal root satisfies the strict trace gap.
It is still a projective saddle, not a Mahler minimizer, because its
covariance matrix inequality has a negative direction.

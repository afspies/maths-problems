# Unrestricted frontier: zero-trace diagonal action

## Verdict

The unrestricted Square Peg conjecture is still open.  The current
sheaf/approximation route has, however, been reduced and sharply delimited:

1. Asano--Ike Remark 5.5 already gives every prescribed rectangle when the
   Jordan trace has positive planar measure.
2. For a null trace, Schoenflies and relative Oxtoby--Ulam give an
   area-preserving, hence Hamiltonian, homeomorphism taking the circle to the
   curve.
3. What is not automatic is Asano--Ike Remark 4.2's diagonal
   \(\mu hom\)-cohomology vanishing.  Equivalently on the approximation side,
   conservative \(C^0\) smoothing does not control boundary action
   potentials.

The explicit double spiral in
`../../results/null-spiral-no-primitive.md` proves that this last gap is
genuine:

> There is a planar-null Jordan curve which admits no parameter-aligned
> regular \(C^1\) Jordan approximants with locally uniformly convergent
> Liouville primitives.

Thus Asano--Ike Theorem 1.1 cannot by itself be turned into the unrestricted
rectangular-peg theorem by choosing more careful smooth approximants.  A
universal proof must use their weaker diagonal cohomology condition directly,
or introduce a different no-shrinkout mechanism.

## 1. Exact reduction from the 2026 literature

Normalize the area enclosed by \(C\) to \(\pi\).  For a Hamiltonian
homeomorphism \(\varphi\) with \(C=\varphi(C_0)\), Asano--Ike define
\[
F_C=K(\varphi\times\varphi)F_{C_0}.
\]
Their Theorem 4.1 assumes
\[
T_aSS^\bullet(F_C)\cap SS^\bullet(F_C)=\varnothing
\qquad(a\notin\pi\mathbb Z)
\]
and then produces every prescribed rectangle.  Remark 4.2 records the
strictly weaker fixed-angle condition: it is enough that, at the critical
value \(a_0=-a(\theta,C)\in(-\pi,0)\),
\[
\Gamma\!\left(
 \rho^{-1}(\Delta_C);
 \mu hom(F_C,T_{a_0}R_\theta F_C)|_{\rho^{-1}(\Delta_C)}
\right)\simeq0.                                           \tag{1}
\]

Remark 5.5 handles positive-measure traces by a density argument.  When
\(|C|=0\), the relative Oxtoby--Ulam theorem supplies the Hamiltonian
homeomorphism needed to define \(F_C\).  Remark 5.7 then identifies (1) as
the missing universal step.

The square symmetry \(R_{\pi/2}^2=R_\pi\) does not formally prove (1).
Greene--Lobb duality exchanges the two Floer degrees and actions \(a\) and
\(\pi-a\); it does not fix either spectral class.  Their triangle inequality
applies to the top class only.  Consequently it gives
\[
\ell_2(C,\pi/2)\geq \frac{\operatorname{Area}(C)}2,
\qquad
\ell_1(C,\pi/2)
=\operatorname{Area}(C)-\ell_2(C,\pi/2)
\leq\frac{\operatorname{Area}(C)}2,
\]
but permits \(\ell_2\to\operatorname{Area}(C)\) and
\(\ell_1\to0\) along smooth approximants.  These are exactly the two
shrink-out endpoints.

## 2. Why conservative smoothing is insufficient

For \(\lambda=\tfrac12r^2\,d\theta\), consider a radial twist
\[
\phi_n(r,\theta)=(r,\theta+\alpha_n(r))
\]
supported in \(r<\rho_n\), where \(\alpha_n\) makes \(N_n\) full turns.
Then
\[
\|\phi_n-\mathrm{id}\|_{C^0}\leq2\rho_n,\qquad
\phi_n^*\lambda-\lambda=dS_n,\qquad
dS_n=\tfrac12r^2\alpha_n'(r)\,dr.
\]
Choosing \(N_n\asymp\rho_n^{-2}\) keeps
\(\operatorname{osc}S_n\) bounded below although
\(\phi_n\to\mathrm{id}\) uniformly.  Hence no estimate of the form
\[
\operatorname{osc}(S_F-S_G)
\lesssim\|F-G\|_{C^0}
\]
can hold.

The twist can be inserted into conservative smoothings.  Its image of a
radial segment is a simple many-turn spiral; comparison loops lie in a
shrinking disk but have unbounded winding multiplicity.  Tube area without
multiplicity control therefore does not bound action.

This example alone concerns the full disk action and can be made constant on
the outer boundary.  The double-spiral theorem below supplies the stronger
boundary obstruction.

## 3. Local action rigidity

Put
\[
\alpha=\frac12(x\,dy-y\,dx),\qquad
\lambda=y\,dx=\frac12d(xy)-\alpha,\qquad
d\alpha=dx\wedge dy.
\]

**Lemma (local action rigidity).**  Let \(c_n:S^1\to\mathbb R^2\) be regular
\(C^1\) Jordan embeddings converging uniformly to a Jordan parametrization
\(c\).  Suppose normalized primitives \(df_n=c_n^*\lambda\) converge
uniformly on one period to a continuous \(f\).  If \(c\) is a regular
\(C^2\) embedding on an open interval \(I\), then, for \(s<t\) in \(I\),
\[
f(t)-f(s)=\int_s^t c^*\lambda.                            \tag{2}
\]

**Proof.**  Set \(g_n=\tfrac12x_ny_n-f_n\), so
\(dg_n=c_n^*\alpha\), and \(g_n\to g=\tfrac12xy-f\)
uniformly.

Choose \(s_-<s<t<t_+\) in \(I\), and a tubular chart
\[
\Psi:[s_-,t_+]\times(-\rho,\rho)\longrightarrow U,
\qquad \Psi(u,0)=c(u).
\]
Write \(\Psi^{-1}c_n(u)=(q_n(u),r_n(u))\).  Uniform convergence gives
\(q_n\to u\) and \(r_n\to0\) uniformly.  Taking the last crossing of
\(\{q=s\}\) and the first subsequent crossing of \(\{q=t\}\) produces
\(\sigma_n\to s\), \(\tau_n\to t\), such that
\(c_n|_{[\sigma_n,\tau_n]}\) is a proper simple crosscut of a tubular
rectangle of width \(\varepsilon_n\to0\).

Close the crosscut using the two transverse sides and one parallel side of
the rectangle.  The resulting loop is Jordan and encloses area
\(O(\varepsilon_n)\).  Green's theorem shows
\[
\int_{\sigma_n}^{\tau_n}c_n^*\alpha
\int_{\beta_n}\alpha=O(\varepsilon_n).
\]
The closing path \(\beta_n\), with reverse orientation, converges in \(C^1\)
to \(c|_{[s,t]}\).  Thus
\[
\int_{\sigma_n}^{\tau_n}c_n^*\alpha
\longrightarrow\int_s^t c^*\alpha.
\]
The left side is \(g_n(\tau_n)-g_n(\sigma_n)\), which converges to
\(g(t)-g(s)\).  The identity relating \(\lambda\) and \(\alpha\) gives
(2). \(\square\)

Uniform primitive convergence is essential here: it makes the errors between
the fixed endpoints and the extracted crosscut endpoints vanish even if the
approximants carry tiny high-twist caps.

## 4. Consequence for the universal program

The null double spiral has a smooth arm on which
\[
\int^\Theta\alpha=\frac12\log\Theta+O(1).
\]
Local action rigidity would force any limiting primitive to agree with this
classical primitive on every compact subarc.  The arm accumulates at a
finite parameter value, so continuity of the limiting primitive is
impossible.  The full period nevertheless converges because the outward
interleaved arm cancels the logarithmic divergence up to an integrable
\(O(\theta^{-2})\) remainder.

This separates three statements which must not be conflated:

- null trace makes total enclosed areas stable under oriented uniform Jordan
  approximation;
- null trace permits an area-preserving Hamiltonian filling;
- null trace does **not** imply a continuous boundary action lift or
  Asano--Ike Theorem 1.1.

The best remaining unrestricted target is therefore exactly (1) for
\(\theta=\pi/2\).  It must be proved without reconstructing a single-valued
continuous primitive.

## 5. A valid positive substitute

There is still a useful sufficient condition.  If the comparison loops
between corresponding approximation prefixes satisfy
\[
\sup_{n,m,t,z}|\operatorname{Wind}(L_{n,m,t},z)|\leq M,
\]
then, when \(|C|=0\),
\[
\sup_t|F_n(t)-F_m(t)|
\leq
M\,|\mathcal N_{\varepsilon_{n,m}}(C)|+o(1)
\longrightarrow0.
\]
This gives Asano--Ike primitive convergence.  The radial-twist and
double-spiral examples show why bounded winding is new geometric input, not
a consequence of \(C^0\) closeness or area preservation.

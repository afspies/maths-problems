# A critical spiral-comb Jordan curve

**Purpose.**  This construction witnesses that the critical
Antonelli--Young bridge is strictly larger than the finite-\(p<2\) class and
the rectifiable and locally monotone classes.  It gives a
\(1/2\)-Hölder Jordan parametrization \(c\) such that
\[
 \sigma(c)<\infty,\qquad
 \operatorname {Var}_p(c)=\infty\quad\text{for every }p<2.              \tag{1}
\]

Only scale estimates matter, so harmless absolute constants below are
suppressed.

## 1. A many-turn simple detour

For \(N\geq1\) and \(a>0\), let
\[
 r(\theta)=a\left(1-\frac{\theta}{4\pi N}\right),
       \qquad 0\leq\theta\leq2\pi N.
\]
Thus \(a/2\leq r(\theta)\leq a\).  In the disk \(D(0,a)\), take the two
spiral arms
\[
 A(\theta)=r(\theta)e^{i\theta},\qquad
 B(\theta)=r(\theta)e^{i(\theta+\pi)}.                 \tag{2}
\]
Join their inner endpoints by the semicircle of radius \(a/2\), and traverse
one arm inward and the other outward.  The result, denoted
\(\Gamma_{N,a}\), is a simple arc from \(a\) to \(-a\), contained in
\(\overline D(0,a)\) and meeting its boundary only at its endpoints.

Indeed, radius is strictly decreasing on each arm.  Points on different
arms with the same radius have arguments differing by \(\pi\), so the arms
are disjoint.  The joining semicircle has radius \(a/2\) and meets the arms
only at their inner endpoints.  Moreover,
\[
             c_0Na\leq\operatorname {len}\Gamma_{N,a}\leq C_0Na.        \tag{3}
\]
On each arm, successive half-turn points are separated by at least \(a\).

## 2. Scales and placement

For all sufficiently large integers \(n\), set
\[
 a_n=2^{-n-20},\qquad
 N_n=\left\lceil\frac{4^n}{n^2}\right\rceil,\qquad
 w_n=N_na_n^2.                                          \tag{4}
\]
Then
\[
 \sum_n w_n<\infty,\qquad
 \sum_n a_n^2\log\frac{e}{a_n^2}<\infty,                \tag{5}
\]
whereas, for every \(p<2\),
\[
 \sum_nN_na_n^p=\infty.                                 \tag{6}
\]

Fix a sufficiently large \(n_0\).  Choose disjoint parameter intervals
\(I_n\), \(n\geq n_0\), of lengths \(w_n\), centered at \(t_n=1/n\).
The factor \(2^{-20}\) makes this possible because
\(t_n-t_{n+1}\asymp n^{-2}\) and \(w_n\asymp2^{-40}n^{-2}\).

In the plane choose disks
\[
 D_n=D(q_n,a_n),\qquad q_n=(1/n,0).
\]
After another finite discard these disks are pairwise disjoint, since their
radii decay exponentially while consecutive centers are separated by
\asymp n^{-2}\).

Here is the global parameter map explicitly.  Choose
\(T>1/n_0+w_{n_0}/2\), with \(T<1\).  Define a background path
\(b:[0,1]\to\mathbb R^2\) by \(b(0)=0\); on each \(I_n\), let \(b\)
traverse the axis diameter from \(q_n-a_n\) to \(q_n+a_n\) affinely; on
each complementary interval between \(I_{n+1}\) and \(I_n\), join the
corresponding gates affinely along the axis; after \(I_{n_0}\), continue
affinely along the axis to a fixed outer endpoint at time \(T\).  On
\([T,1]\), let \(b\) follow a fixed polygonal closing arc below the strip
containing the disks and return to \(b(0)\).

This \(b\) is globally Lipschitz.  On a diameter interval and a complementary
gap, respectively, its slopes satisfy
\[
 \frac{2a_n}{w_n}=\frac2{N_na_n}\leq C
\]
and
\[
 \frac{(1/n-a_n)-(1/(n+1)+a_{n+1})}
 {(1/n-w_n/2)-(1/(n+1)+w_{n+1}/2)}
 \leq C,                                                \tag{7}
\]
after increasing \(n_0\).  The first ratio tends to zero and the second to
one.  The finitely many outer and closing pieces have finite slopes.

Now replace \(b|_{I_n}\) by the translated detour
\(q_n+\Gamma_{N_n,a_n}\), in the direction matching its two gates, and
parametrize it at constant speed.  Call the resulting top arc together with
the closing arc \(c\).

The disks are disjoint.  Each detour is simple, lies in its disk, and meets
the boundary of its disk only at its two gates.  (The spiral arms do cross
the omitted diameter inside the disk, but that diameter is not part of
\(c\).)  The portion of the axis belonging to \(c\) lies outside the open
disks and hence meets a detour only at its gates.  The lower closing arc is
disjoint from the disks and from the remaining axis except at its endpoints.
The resulting closed curve is therefore Jordan.

## 3. Uniform \(1/2\)-Hölder estimate

Write
\[
                         c=b+\sum_nf_n,                 \tag{8}
\]
where \(b\) is the Lipschitz parametrization which traverses the omitted
diameters linearly, and \(f_n\) is the difference between the detour and
that diameter on \(I_n\), extended by zero off \(I_n\).  The supports are
disjoint.  From (3)--(4),
\[
 \|f_n\|_\infty\leq Ca_n,\qquad
 \operatorname {Lip}(f_n)\leq\frac C{a_n}.             \tag{9}
\]
The second bound uses
\(\operatorname {len}\Gamma_{N_n,a_n}/w_n\leq C/a_n\).
Consequently, for \(h=|s-t|\),
\[
 |f_n(s)-f_n(t)|
 \leq C\min\{a_n,h/a_n\}\leq C\sqrt h.                 \tag{10}
\]

The sum in (8) has the same bound.  If \(s,t\) lie in different supports,
the endpoint of each intervening support lies between them; applying (9) to
the distance from the relevant point to that endpoint gives
\[
 \left|\sum_nf_n(s)-\sum_nf_n(t)\right|\leq2C\sqrt h.  \tag{11}
\]
Adding the Lipschitz background \(b\) proves that \(c\) is
\(1/2\)-Hölder.

In particular \(c\) has finite \(2\)-variation, since for every partition
\[
 \sum_k|c(t_{k+1})-c(t_k)|^2\leq C^2\sum_k(t_{k+1}-t_k)=C^2.             \tag{12}
\]

## 4. The Antonelli--Young sum is finite

For a dyadic interval \(J\) of length \(h\), let
\(\delta_J(f)\) be the diameter of the values of \(f\) at the left endpoint,
midpoint, and right endpoint of \(J\).  At scale \(h\), at most
\(C(1+w_n/h)\) such triples meet \(I_n\).  By (9),
\[
 \delta_J(f_n)\leq C\min\{a_n,h/a_n\}.                 \tag{13}
\]
Summing first over all dyadic \(J\) at a fixed scale and then over the three
ranges \(h\geq w_n\), \(a_n^2\leq h<w_n\), and \(h<a_n^2\), gives
\[
\begin{aligned}
 \sigma(f_n)
 &\leq C\sum_{h\ {\rm dyadic}}
   (1+w_n/h)\min\{a_n^2,h^2/a_n^2\}\\
 &\leq C\left(w_n+a_n^2\log\frac e{a_n^2}\right).      \tag{14}
\end{aligned}
\]
The right side is summable by (5).

At the three sample times of any fixed dyadic interval, at most three of
the disjointly supported \(f_n\)'s are nonzero.  Applying
\((u+v+w)^2\leq3(u^2+v^2+w^2)\) to the pairwise differences of those three
values yields
\[
 \delta_J\left(\sum_nf_n\right)^2
       \leq C\sum_n\delta_J(f_n)^2.                    \tag{15}
\]
The Lipschitz background satisfies \(\sigma(b)<\infty\) (equivalently, sum
\(\delta_J(b)^2\leq2\operatorname {Lip}(b)^2\)).  Equations
(5), (14), and (15) prove
\[
                              \sigma(c)<\infty.         \tag{16}
\]

## 5. It is outside every finite-\(p<2\) class

On each detour, choose consecutive half-turn points on one spiral arm.
Their mutual distances are bounded below by \(a_n\), and there are
\(\asymp N_n\) of them.  Finite collections of all these sample points,
listed in parameter order, are legitimate partitions.  Hence
\[
 \operatorname {Var}_p(c)^p
       \geq c_p\sum_nN_na_n^p=\infty                  \tag{17}
\]
for every \(p<2\), by (6).  In particular the curve has infinite length.

## 6. It is not locally monotone

The disks accumulate at the origin.  Given any nonzero linear projection
\(\ell:\mathbb R^2\to\mathbb R\) and any one-sided parameter neighborhood
of the origin, some complete detour \(\Gamma_{N_n,a_n}\) lies inside that
neighborhood.  Along either spiral arm, the angular coordinate makes a full
turn while its radius remains positive, so \(\ell\) has both an increase
and a decrease.  Thus no linear projection is monotone on any such
neighborhood.  The curve is not locally monotone in Stromquist's sense.

## 7. Peg consequence

The curve is a \(1/2\)-Hölder Jordan parametrization satisfying (16), so the
critical Antonelli--Young bridge applies.  It inscribes every prescribed
rectangle, including a square, despite having infinite \(p\)-variation for
every \(p<2\) and being neither rectifiable nor locally monotone.

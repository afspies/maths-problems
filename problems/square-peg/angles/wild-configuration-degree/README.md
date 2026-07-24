# Wild collision absorbs the local square degree

## Verdict

The ordinary configuration-space parity does **not** survive total
collision for arbitrary Jordan embeddings merely by adjoining cyclic gap
data, a prime-end side, and a normalized finite secant screen.

More precisely, there is a Jordan curve \(C\), a point \(p\in C\) at which
\(C\) has no tangent, and a parameter-aligned family of Jordan curves
\(C_\varepsilon\to C\) such that:

1. a fixed neighbourhood of \(p\) contains no square with all four
   vertices on \(C\);
2. \(C_\varepsilon\) has one regular square zero in a specified local
   configuration box, so its local mod-two degree is one;
3. the four parameters and vertices of this square converge to \(p\);
4. after normalization, the collision screen is a fixed exact square,
   approached from one fixed side of the prime end.

The zero is asserted to be unique only in its small configuration box.
There may be other squares elsewhere on \(C_\varepsilon\).  The
construction is a no-go theorem for a *local* boundary-free degree, not a
counterexample to the Square Peg conjecture and not a computation of the
global square parity.

## The square test map and its local index

For four points \(z_1,z_2,z_3,z_4\in\mathbb R^2\), put
\[
\begin{aligned}
 P&=z_1+z_3-z_2-z_4\in\mathbb R^2,\\
 E&=|z_2-z_1|^2-|z_3-z_2|^2\in\mathbb R,\\
 O&=(z_2-z_1)\mathbin{\cdot}(z_3-z_2)\in\mathbb R
\end{aligned}
\]
and \(\Psi=(P_x,P_y,E,O)\).
For distinct consecutive points, \(\Psi=0\) exactly when they are the
perimeter-ordered vertices of a square: \(P=0\) gives a parallelogram,
while \(E=O=0\) makes two adjacent sides equal and perpendicular.

Take the unit square
\[
 q_1=(-1/2,1),\quad q_2=(1/2,1),\quad
 q_3=(1/2,2),\quad q_4=(-1/2,2)
\]
and prescribe oriented curve tangents
\[
 T_1=(1,0),\quad T_2=(1,1),\quad
 T_3=(-1,1),\quad T_4=(-1,0).
\]
The derivative of \(\Psi\) with respect to the four curve parameters,
whose \(i\)-th point has velocity \(T_i\), is
\[
 D\Psi=
 \begin{pmatrix}
  1&-1&-1& 1\\
  0&-1& 1& 0\\
 -2& 4&-2& 0\\
  0& 0&-1& 0
 \end{pmatrix},
 \qquad \det D\Psi=-2.                         \tag{1}
\]
Thus this square is a regular zero of integral local degree \(-1\), and
mod-two local degree one.  Orientation-preserving similarities and
positive reparametrizations multiply the determinant by a positive
factor, so the sign is unchanged.

There is an embedded \(C^1\) arc \(\Gamma\) in the upper half-plane, from
\(A=(-2,0)\) to \(B=(2,0)\), which passes through the \(q_i\) in order
with these tangents and otherwise misses the segment \(AB\).  Here is an
explicit construction near the four marked points.  For sufficiently
small \(\delta>0\), join each \(q_i\) to \(q_{i+1}\) by the cubic Bézier
arc with control points
\[
 q_i,\quad q_i+\delta T_i,\quad
 q_{i+1}-\delta T_{i+1},\quad q_{i+1}
 \qquad(i=1,2,3).
\]
The three control polygons lie in disjoint thin neighbourhoods of the
bottom, right, and top sides of the square, meeting only at their common
endpoints.  Their endpoint derivatives are \(3\delta T_i\), so their
union is an embedded \(C^1\) arc with the required marked jets.  Join
\(A\) to \(q_1\) below and to the left of the square, and leave \(q_4\)
in direction \(T_4\) before routing above and to the right of the square
to \(B\).  These two connectors can be chosen disjoint and smoothed
without changing the marked jets.  The resulting \(\Gamma\) can also be
chosen to have horizontal projection contained in \([-2,2]\).

By (1) and the inverse function theorem, the marked square is the unique
zero of \(\Psi\) in some product neighbourhood of its four parameters.

## A locally square-free wild limit

Define a function on a neighbourhood of \(0\) as follows.  Put \(f(x)=0\)
for \(x\geq0\).  For \(x<0\), set
\[
 f(x)=g(-x),\qquad
 g(u)=\int_0^u \sigma(v)\,dv,
\]
where
\[
 \sigma(v)=\frac{(-1)^n}{4}
 \quad\text{for}\quad
 2^{-(n+1)}<v<2^{-n}.
\]
Then \(f\) is \(1/4\)-Lipschitz.  Moreover
\[
 \frac{g(2^{-n})}{2^{-n}}=\frac{(-1)^n}{12},              \tag{2}
\]
whereas the right-hand difference quotient of \(f\) at zero is zero.
Consequently the graph has no tangent at \(p=(0,0)\).

No four points of this graph form a square.  Indeed, for any two distinct
graph points the chord has finite slope \(m\) with \(|m|\leq1/4\).
If two such chord vectors have slopes \(m_1,m_2\), their dot product is
\[
 \Delta x_1\Delta x_2(1+m_1m_2)\ne0,
\]
because \(1+m_1m_2\geq15/16\).  A square has two perpendicular side
chords, which is impossible.

Close a finite piece of this graph by an embedded polygonal arc far from
\(p\), obtaining a Jordan curve \(C\).  The closing arc may be chosen so
that a disk \(D\) about \(p\) meets \(C\) only in the graph.  Hence \(D\)
contains no square all of whose vertices lie on \(C\).

## The odd local zero escapes to total collision

For \(\varepsilon>0\), replace the straight graph segment
\[
 [\varepsilon,2\varepsilon]\times\{0\}
\]
by the similarity image
\[
 S_\varepsilon(\Gamma),\qquad
 S_\varepsilon(x,y)=
 \left(\frac{3\varepsilon}{2}+\frac{\varepsilon x}{4},
       \frac{\varepsilon y}{4}\right).
\]
Because \(\Gamma\) lies strictly above \(AB\), except at its endpoints,
and its horizontal projection is contained in that of \(AB\), this
replacement is embedded and meets the rest of \(C\) only at its two
endpoints.  Denote the resulting Jordan curve by \(C_\varepsilon\).
It can be parametrized to agree with a fixed parametrization of \(C\)
off a shrinking parameter interval, and then
\[
 \|c_\varepsilon-c\|_\infty=O(\varepsilon).
\]

The four points \(S_\varepsilon(q_i)\) are an exact square on
\(C_\varepsilon\).  Equation (1) says that, in a sufficiently small
product box about their parameters, this is the only square zero and its
local mod-two degree is one.  All four parameters converge to the
parameter of \(p\), and all four vertices converge to \(p\). Applying
\(S_\varepsilon^{-1}\)—equivalently, subtracting
\((3\varepsilon/2,0)\) and dividing by the square side
\(\varepsilon/4\)—recovers the same four points \(q_i\). Thus the limiting
screen is an exact square, not a
nonzero boundary value of the square test map.  Every bump lies on the
same side of the local graph, so recording the prime-end side does not
remove this boundary zero.

If finite-stage regularity is desired, truncate the alternating graph on
\([-2^{-N},0]\) by its endpoint chord, retain the bump with
\(\varepsilon=\varepsilon_N\to0\), and round the finitely many unmarked
corners.  This gives finite-piece \(C^1\) Jordan approximants converging
parameterwise to \(C\), without changing the four marked jets or their
local degree.  A polygonal version retaining the four marked square
vertices is obtained by replacing the Bézier pieces by sufficiently
close polygonal arcs; transversality is then recovered by smoothing only
near the marked points with the prescribed jets.

## Classification of square escape faces

The above example realizes the only possible collision face for exact
squares.  Let \(c_n\to c\) uniformly, with \(c\) a Jordan
parametrization, and suppose cyclic quadruples on \(c_n\) are exact
squares.

If their side lengths have a positive lower bound along a subsequence,
compactness of the parameter circle gives a nondegenerate limiting square
on \(c\).  Otherwise their side lengths tend to zero, so all four image
points have one common limit \(p\).  Uniform convergence gives
\(c(t_i)=p\) for every limiting parameter \(t_i\).  Injectivity of \(c\)
forces all \(t_i\) to be the same point of \(S^1\).

Write a cyclic quadruple by its four positive gaps
\[
 (g_1,g_2,g_3,g_4),\qquad \sum_i g_i=1.
\]
After choosing which point starts the lifted order, total collision means
that three consecutive gaps tend to zero and the remaining complementary
gap tends to one.  Hence exact square zeros do not escape through
single-pair or two-cluster faces: they escape only through the four
vertices of the closed gap simplex, which form one orbit under cyclic
relabelling.  In the cyclic quotient there is therefore one total-collision
face capable of absorbing an odd square orbit.  The construction above
shows that it actually does so locally.

## Exact scope of the no-go

This proves that the following strategy cannot by itself establish the
unrestricted Square Peg conjecture:

1. compactify cyclic quadruples only by their gap degeneration;
2. add a one-sided prime-end label and a normalized finite secant screen;
3. assert that the square test map is nonzero on the boundary; and
4. transport the smooth mod-two square count to an arbitrary Jordan curve.

The boundary already contains a square screen carrying a regular local
degree-one zero.  Equivalently, local square parity is not \(C^0\)-closed.

The argument does **not** rule out a compactification with a nontrivial
boundary correction, an invariant coupling all scales, or a global
Floer/sheaf/action obstruction.  Such extra structure would have to show
that the boundary charge cannot account for the *global* obstruction; the
finite screen and prime-end side alone do not do that.

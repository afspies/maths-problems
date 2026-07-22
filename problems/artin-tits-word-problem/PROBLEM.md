# Word problem for the minimal unknown Artin-Tits group

## Statement
Let G be the Artin–Tits group with generators a, b, c, d and relations
ad = da (commutation) and xyx = yxy (braid) for every other pair
{a,b}, {a,c}, {b,c}, {b,d}, {c,d}. **Is the word problem for G decidable?**

Per Timothy Gowers's Polymath proposal (blog post, 2026-03-20), this is the
simplest Artin–Tits group whose word-problem status is unknown. All
Artin–Tits groups are conjectured to have decidable word problems, so the
expected answer is YES — the prize is the algorithm and its proof, which
plausibly requires new Garside-type theory. Big-picture: the word problem for
general Artin–Tits groups is one of the main open problems in geometric group
theory; cracking the minimal unknown case is the natural wedge.

## Community context (IMPORTANT)
This is a live, public Polymath-style project. Norms apply: results get
written up for the blog thread (the repo owner posts them), with full credit
to Gowers and commenters. Key thread facts to verify and build on:
- Gowers has an algorithm ("A₂"): never increases word length, solves every
  puzzle he has tried, including one derived from Dehornoy's braid (see
  arXiv:math/0311326, p.4). His implementation is vibecoded and unaudited —
  treat his *written spec* as the object, reimplement independently.
- Comment (Leif Schaumann, 2026-06-06): claims the word bbdCbbcDBBdCBBcD
  (uppercase = inverses; no a's) equals the identity but cannot be reduced to
  it without first increasing length — with a claimed generalization family.
  If correct, this likely defeats A₂-style non-lengthening algorithms and
  answers a question Gowers explicitly asked. **Machine-checkable**: the set
  of words reachable by non-length-increasing moves from a length-16 word is
  finite. Verify exhaustively before anything else builds on it.
- Comment thread (Gowers, 2026-04-06): one ChatGPT-5.4-Pro conversation
  claimed arXiv:2305.11622 reduces the problem to a finite computation and
  claimed to do it; a second conversation denied this. Adjudicating what that
  preprint actually gives is an open, valuable task.
- Tim Riley's comments: van Kampen / Dehn-proof-system framing; Charney's
  biautomaticity gives braid groups linear filling length — whether G has
  linear (or any computable) filling length is a sharp, publishable
  subquestion: a computable filling-length bound would itself decide the
  word problem.

## Why this group escapes the known decidable classes (director's analysis —
VERIFY carefully, this is from memory and load-bearing)
Coxeter diagram: K₄ with edge {a,d} labeled 2, all other edges labeled 3.
- Not spherical/finite type (no Garside structure of classical type).
- Not FC type: the parabolic on {a,b,c} is all-braid (affine Ã₂ diagram),
  complete but not spherical.
- Not large type: the label-2 edge ad = da violates "all labels ≥ 3".
- Not 2-dimensional: the parabolic on {a,b,d} (a–b braid, b–d braid, a–d
  commute) is spherical of rank 3 (type A₃, i.e. the braid group B₄).
- Not euclidean/affine type as a whole (McCammond–Sulway doesn't apply
  directly).
So G straddles every major decidable class while all its proper standard
parabolics land in decidable ones: {a,b,c} and {b,c,d} are affine Ã₂
(decidable — euclidean case), {a,b,d} and {a,c,d} are spherical A₃
(Garside). The whole group is a union of decidable parabolics glued along
decidable intersections — the innovation target is exactly this gluing.

## Angle-of-attack menu (the "go big" tiers are the point of this campaign)
- **Relative/interval Garside structures**: McCammond–Sulway built
  crystallographic Garside groups to crack euclidean Artin groups by
  *enlarging* the group; look for an analogous supergroup/interval complex
  for G. This is the flagged "Garside-theoretic innovation" lane.
- **Amalgam/complex-of-groups route**: exploit the decidable-parabolic cover;
  Deligne complex geometry (is it CAT(0) for G? known criteria by
  Charney–Davis), systolic/Helly techniques (Huang–Osajda proved biautomatic
  for large-type — what breaks at the label-2 edge?).
- **Rewriting/normal forms**: Dehornoy subword reversing; completeness of a
  length-bounded rewriting system (Schaumann's word, if verified, calibrates
  exactly how much lengthening is needed — a *computable bound* on the
  detour suffices for decidability).
- **Filling length / isoperimetric route**: prove a computable filling-length
  or Dehn-function bound for G (biautomaticity would be the elegant version).
- **Empirical wedge**: reimplement Gowers's A₂; adversarial word-generation
  campaigns to map where it fails; every defeating word is thread-worthy and
  constrains the theory.

## Certificate + verifier discipline
- Word-level claims (identity words, irreducibility-without-lengthening up to
  a bound, A₂ success/failure) are exact finite computations — exhaustive
  BFS with canonical forms, logged reproducibly in results/.
- "Algorithm X decides the word problem" requires a proof (termination +
  correctness), adversarially reviewed; partial versions ("X is correct on
  the parabolic P", "X decides words of syllable structure S") are
  first-class results.
- Theory claims (class memberships above, what arXiv:2305.11622 proves) need
  citations into literature/ after genuine reading — not model memory.

## First steps
1. Fetch Gowers's post + thread, his video-spec of A₂, arXiv:2305.11622,
   arXiv:math/0311326; literature map of decidable Artin–Tits classes with
   citations (verify every claim in the director's analysis above).
2. Harness: exact word/move engine for G (relations + free reduction +
   rotation), independent A₂ implementation from the written spec, canonical
   forms + BFS for exhaustive small-word analysis.
3. Exhaustively verify/refute Schaumann's word and family; test A₂ on it.
4. Then the big swing, multi-angle, per the menu above.

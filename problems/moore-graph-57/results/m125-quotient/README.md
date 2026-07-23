# m=125 semiregular-quotient search — negative DATA (not an exclusion)

**Claim level: resistance data only.** No exclusion is claimed; CP-SAT
returned UNKNOWN in every completed run. Recorded because the compute is
substantial and steers the next attack.

## The question

Does a symmetric 26×26 integer matrix C ≥ 0 exist with row sums 57,
C² + C − 56·I = 125·J, even diagonal? (Any group of order 125 acting
semiregularly on the degree-57 Moore graph forces one; nonexistence of C
would exclude all such actions — the largest admissible semiregular
order, see `../../angles/semiregular-quotient/`.)

The trace identity tr C = 15a − 143 (a = multiplicity of eigenvalue 7 on
the quotient's 1-perp) splits the search by a; parity + the diagonal cap
force odd a ∈ {11, …, 23}, so seven subproblems exhaust the question.

## Runs (all UNKNOWN — no verdict either way)

| run | a | budget | outcome | evidence |
|---|---|---|---|---|
| laptop DFS (quotient_scan.py) | all | 2·10⁹ nodes (~35 min) | no solution, not exhausted | JOURNAL 2026-07-22 |
| laptop CP-SAT, 8 workers | all | 3h | UNKNOWN (467k conflicts) | JOURNAL 2026-07-22 |
| laptop CP-SAT, 8 workers | 11 | 1h | UNKNOWN (~33M conflicts) | JOURNAL 2026-07-22 |
| cluster CP-SAT, 4 workers | 19 | 12h | UNKNOWN — 275.8M conflicts, 375.3M branches | `moore125_a19.log` |
| cluster CP-SAT, 4 workers | 21 | 12h | UNKNOWN — det-time 94,466 | `moore125_a21.log` |

Cluster runs: 4-CPU containers, OR-Tools CP-SAT (pip `ortools`,
python:3.12-slim), command `cp_quotient.py 57 125 43200 <a> 4`. Five
sibling runs (a ∈ {11,13,15,17,23}) were lost to an infrastructure
deadline kill before completing (JOURNAL 2026-07-23) — those a values
currently have NO 12h-scale attempt.

## Reproduce

```bash
.venv/bin/python angles/semiregular-quotient/cp_quotient.py 57 125 43200 19 4
```

(deterministic modulo CP-SAT's internal parallel racing; conflict counts
will vary, verdicts should not).

## Steering conclusion

b=26 quadratic feasibility resists ~30h cumulative CP-SAT plus a 2·10⁹
node DFS with zero signal. Next tools, in order: analytic cyclotomic
integrality on abelian lifts (`../../angles/semiregular-quotient/character_notes.md`),
bit-blasted SAT + DRAT (proof-carrying if UNSAT), character-filtered
a ∈ {13,17} runs. More plain CP-SAT hours are the weakest option.

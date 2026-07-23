# Pure-SAT + DRAT semiregular-quotient pipeline

**Status: encoding and SAT-model checks validated; external DRAT gate blocked
by shell network policy.**  The encoder generates every required m=125
fixed-trace instance well below the explicit 200-million-clause / five-minute
STOP thresholds.  Kissat exactly decodes all three d=7 witnesses.  The
requested drat-trim clone could not be fetched because this execution
environment cannot resolve or connect to GitHub; therefore no UNSAT result is
accepted here and the overall m=125 question remains open.

## Mathematics re-derived by the encoder

Let `n=d*d+1`, require `m | n`, and set `b=n/m`.  Exact
`isqrt(4*d-3)` arithmetic gives

```
r = (-1 + sqrt(4*d-3))/2
s = -1-r
```

The projection argument in `../quotient_scan.py` gives, without floating
point,

```
diag_cap    = min(m, d, (r*b +   (d-r)) // b)
offdiag_cap = min(m, d, (r*b + 2*(d-r)) // b).
```

The test suite captures `quotient_scan.search_quotients`' live local cap
values and checks equality for `(57,125)` and all three d=7 cases.  For the
target these are `b=26`, `diag_cap=8`, `offdiag_cap=10`; the encoder contains
an explicit regression assertion in the test, not magic-number caps in the
implementation.

For every `a in range(b)`,

```
trace(a) = d + r*a + s*(b-1-a).
```

The valid window retains exactly traces between zero and the capped maximum,
and retains only even traces when `m` is odd.  At `(57,125)` this independently
returns all seven quotient cases
`a in {11,13,15,17,19,21,23}`.  The abelian-lift filter
`a = 1 (mod 4)` is deliberately *not* applied to this quotient problem.

## Variables and deterministic numbering

Coordinates are always canonical upper-triangle pairs `(min(i,j),max(i,j))`.
Variables are allocated from 1 upward in this order:

1. For `(i,j)` in lexicographic upper-triangle order, `X[i,j,v]` is an
   exact-one entry literal.  Diagonal values are
   `0..diag_cap` (even only when `m` is odd); off-diagonal values are
   `0..offdiag_cap`.
2. Immediately after each one-hot block, `B[i,j,k]` is bit `k` of the entry.
3. Row-sum adder sum/carry variables follow.
4. If `a` is fixed, trace-adder sum/carry variables follow.
5. For quotient equations `(i,j)` in upper-triangle order and `t=0..b-1`,
   `P[{(i,t),(j,t)},k]` is bit `k` of the product.  A product bus is cached by
   its unordered pair of entry coordinates, so the same entry square is not
   duplicated between two self equations.  Quotient-adder sum/carry variables
   are interleaved as each equation is emitted.
6. Symmetry clauses allocate no variables.
7. With `--mod5`, `S[constraint,layer,residue]` (five residues) and
   `R[i,j,t,k]` (three product-residue bits for cross equations) are allocated
   in row-sum then upper-triangle equation order.

The sidecar `FILE.cnf.map.json` records every primary `X` block, all derived
parameters, fixed `a`, exact variable/clause totals, generation time, and
per-group counts.  Auxiliary IDs remain deterministic from the scheme above.

Write

```
qD = number of allowed diagonal values
qO = offdiag_cap + 1
E  = binom(b,2)
wD = bit_length(max diagonal value)
wO = bit_length(offdiag_cap)
wDD = bit_length(diag_max^2)
wDO = bit_length(diag_max*offdiag_cap)
wOO = bit_length(offdiag_cap^2).
```

The structural group sizes are:

| group | variables | clauses |
|---|---:|---:|
| entry exact-one | `b*qD + E*qO` | `b*(1+binom(qD,2)) + E*(1+binom(qO,2))` |
| entry value tables | `b*wD + E*wO` | `b*qD*wD + E*qO*wO` |
| cached product buses | `b*wDD + E*wOO + 2E*wDO + b*binom(b-1,2)*wOO` | `b*qD*wDD + E*qO*wOO + 2E*qD*qO*wDO + b*binom(b-1,2)*qO^2*wOO` |
| max diagonal | 0 | `(b-1)*binom(qD,2)` |
| sorted row 0 | 0 | `(b-2)*binom(qO,2)` |

Every exact sum is a ripple network wide enough for the sum of operand
maxima, so arithmetic cannot wrap.  For `L` operands and width `W`, it uses
`W*(L-1)` sum and `W*(L-1)` carry variables.  A truth-table full adder at bit
`k` with `u` distinct nonconstant inputs emits `2^(u+1)` clauses; each
addition also emits one no-overflow unit and the final bus emits `W` target
units.  This formula, applied to `b` row sums, one trace, and
`b*(b+1)/2` quotient sums, exactly gives the recorded adder counts.

For `(57,125)` without mod 5 the measured variable groups are:

```
entry_onehot=3,705  entry_bits=1,404  product_bits=61,607
adder_sum=115,562  adder_carry=115,562
```

and the measured clause groups are:

```
entry_exact_one=18,486       entry_value_table=14,820
product_value_table=6,882,785
row_sum_adder=62,764         trace_adder=2,217
quadratic_sum_adder=1,312,038
symmetry_max_diagonal=250    symmetry_sorted_row0=1,320
```

## Clause semantics and soundness

### Exact entries, products, and integer sums

Each entry block has one at-least-one clause and all pairwise at-most-one
clauses.  For every allowed value and each output bit, the selected one-hot
literal implies that bit's correct polarity.  Because exactly one value is
selected, every `B` bus is fully determined.

This implementation deliberately deviates from one product-indicator per
`(p,q)` pair.  It instead makes a small binary product bus and, for every
allowed selected pair, emits a table clause forcing every output bit of
`p*q`.  For squares the clause is binary; for distinct blocks it is ternary:

```
X_left[p] & X_right[q] -> P[k] == bit_k(p*q).
```

This implication direction suffices *for the output bits* because the input
blocks select exactly one pair, and that active pair supplies a forcing clause
for both polarities of every bit.  No product bit can float or fill arithmetic
slack.  This is not the unsound proposal in which unselected positive
per-pair auxiliaries may spuriously become true.  Full per-pair IFF gates
would also be sound, but measured estimates put them near one million extra
variables; the deterministic bus table is smaller and equally exact.

Truth-table Tseitin full adders define both output bits for every possible
input triple.  Accumulators have width `bit_length(sum operand maxima)`,
overflow carry is false, and the final bus is unit-fixed to the exact integer
target.  Hence each row sum and each equation

```
sum_t C[i,t]*C[j,t] + C[i,j] = m + (d-1)*[i=j]
```

holds over integers, not modulo a machine word.

### Trace and symmetry

The trace adder fixes the exact spectral trace for the selected `a`.

Simultaneous row/column permutation is the full relabelling action used here.
Given any solution, first relabel an index with maximal diagonal entry as 0.
Then permute indices `1..b-1` in descending order of their row-0 entries.
The second permutation fixes index 0, so it preserves maximality.  Therefore
`C[i,i] <= C[0,0]` and
`C[0,1] >= ... >= C[0,b-1]` lose no solution-equivalence class.

### Row-0 cubes

For `h=C[0,0]`, the remaining sorted row has `b-1` values in
`[0,offdiag_cap]` satisfying both

```
sum x_j   = d-h
sum x_j^2 = m+d-1-h-h^2.
```

The recommended-design prose's statement that the *remaining* square sum is
`181-h` omits `h^2`; `181-h` is the total-row square sum.  The code uses the
corrected remaining target `181-h-h^2`.  Exact recursive DP enumerates every
non-increasing sequence meeting those two identities.  Every
symmetry-broken solution obeys them, so its row 0 appears in a cube.  For a
fixed trace, cubes violating the necessary bound `trace <= b*h` are discarded
because max-diagonal symmetry makes all diagonals at most `h`; this pruning
also cannot remove a solution.

`--cubes` emits a directory `BASE.cnf.cubes/`, one standalone
`cube-N.cnf` per retained row pattern, plus `_base.cnf` and `manifest.json`.
On APFS each standalone file is a copy-on-write clone with `b` added unit
clauses; the file format is ordinary DIMACS, not a solver-specific iCNF.
This satisfies independent per-cube DRAT checking without multiplying
physical storage by the cube count.  `run_and_check.py` accepts the directory
and drives every listed cube.

The exact target counts, using *both* row identities, are:

| `h` | recomputed | prior consult | result |
|---:|---:|---:|---|
| 0 | 218 | 218 | match |
| 2 | 241 | 241 | match |
| 4 | 169 | 169 | match |
| 6 | 70 | 70 | match |
| 8 | 8 | 8 | match |

### Optional mod-5 clauses

The option is accepted only if `m=0` and `d=2 (mod 5)`.  Reducing the exact
quotient identity gives

```
C^2 + C - I = 0 (mod 5).
```

For `N=C-2I`,

```
N^2 = C^2 - 4C + 4I = C^2 + C - I = 0 (mod 5),
N*1 = (d-2)*1 = 0 (mod 5).
```

Thus the clauses are consequences of the exact equations, not an empirical
filter, and enabling them cannot change SAT/UNSAT status.  Symmetry needs no
new clauses because upper-triangle sharing already makes `N` symmetric.
This is the theorem checked algebraically in
`../verify_mod5_and_filter.py`.

Each modular sum is a deterministic five-state automaton.  The initial state
is exactly residue 0.  Every next layer is at-most-one; the unique selected
event and the unique previous state force its correct successor, so induction
also supplies at-least-one without a redundant long clause.  The final
residue-0 state is a unit.

For self terms, one-hot values directly supply
`(C[i,t]-2[t=i])^2 mod 5`.  For cross terms, a three-bit bus is table-forced
to

```
(C[i,t]-2[t=i]) * (C[j,t]-2[t=j]) mod 5.
```

At `(57,125)`, mod 5 adds exactly:

```
variables:
  mod5_product_bits=25,350
  mod5_state=50,895
clauses:
  mod5_product_table=2,938,650
  mod5_transition=284,050
  mod5_state_amo=98,020
  mod5_state_boundary=2,262
```

## Actual generated instance sizes

Every row below was generated as a real file in `generated/`; the DIMACS
header was checked against `wc -l - 1`.  No size is an estimate.

| a | mod 5 | variables | clauses | generation seconds |
|---:|:---:|---:|---:|---:|
| 13 | no | 297,840 | 8,294,680 | 7.240 |
| 13 | yes | 374,085 | 11,617,662 | 10.688 |
| 17 | no | 297,840 | 8,294,680 | 7.746 |
| 17 | yes | 374,085 | 11,617,662 | 10.149 |
| 21 | no | 297,840 | 8,294,680 | 7.781 |
| 21 | yes | 374,085 | 11,617,662 | 10.222 |
| 23 | no | 297,840 | 8,294,680 | 7.858 |
| 23 | yes | 374,085 | 11,617,662 | 10.262 |

No explicit STOP condition was hit.

The permitted smoke run was only:

```
run_and_check.py generated/m125-a23.mod5.cnf --timeout 30
TIMEOUT ... wall=30.121s cap=30s
```

No solver run was launched for a=13,17,21, and the timeout is not evidence
for or against feasibility.

## Commands

Use the task's absolute interpreter:

```bash
PY=/Users/alex/Developer/maths-problems/problems/moore-graph-57/.venv/bin/python

$PY encode_quotient.py 57 125 13 -o generated/m125-a13.cnf
$PY encode_quotient.py 57 125 all --mod5 -o generated/m125.cnf
$PY encode_quotient.py 57 125 23 --mod5 --cubes -o generated/m125-a23.cnf

$PY run_and_check.py generated/m125-a23.mod5.cnf --timeout 30
$PY run_and_check.py generated/m125-a23.cnf.cubes --timeout 600

$PY test_encoder.py -v
```

Without `-o`, one fixed-a DIMACS instance is written to stdout and the
statistics line goes to stderr.  `a=all` requires `-o`, because concatenating
multiple DIMACS headers would not be a valid solver input.

`run_and_check.py` enforces `1 <= timeout <= 600`, also passes the internal
Kissat time bound, and kills a solver that overruns the external wall clock.
It is Python rather than shell so the solver driver and the exact NumPy
`int64` model audit share the same structured decode map without fragile
shell parsing.
SAT models are decoded through the primary map and verified by actual NumPy
`int64` matrix multiplication.  An UNSAT status is returned only after the
external checker exits 0 and prints `s VERIFIED`.

## Tooling blocker recorded exactly

The required clone was attempted twice.  The key output was:

```
Cloning into 'problems/moore-graph-57/angles/semiregular-quotient/sat/tools/drat-trim'...
fatal: unable to access 'https://github.com/marijnheule/drat-trim/': Could not resolve host: github.com
```

The in-app browser was unavailable and direct-IP HTTPS fallback was also
blocked.  Consequently `tools/drat-trim/` was not created, `make` could not
be run, and gates (b)/(c) correctly fail rather than silently treating Kissat
UNSAT as certified.  Once network access is available, the remaining commands
are:

```bash
git clone https://github.com/marijnheule/drat-trim tools/drat-trim
make -C tools/drat-trim
$PY test_encoder.py -v
```

The current failed test summary is:

```
Ran 5 tests in 0.277s
FAILED (failures=1, errors=1)
```

The failures are solely the absent checker binary: all cap, SAT/decode, and
DP-count assertions pass, and Kissat returns UNSAT for the deliberately
impossible tiny case and the trace-incompatible d=7 cube.

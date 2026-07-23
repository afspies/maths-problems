#!/usr/bin/env python3
"""Proof-carrying pure-SAT encoding of semiregular quotient feasibility.

For n=d^2+1 and b=n/m, the sought symmetric integer matrix C satisfies

    C 1 = d 1,       C^2 + C - (d-1) I = m J.

Only upper-triangle entries are represented.  Every entry has an exact-one
block over the PSD-capped domain derived in quotient_scan.py.  Small binary
buses are deterministic table images of those blocks.  A truth-table
Tseitin ripple-adder network then expresses every exact integer sum.  In
particular, for i <= j we encode the nonnegative equality

    sum_t C[i,t] C[j,t] + C[i,j] = m + (d-1) [i=j].

This is deliberately a hand-rolled bit-vector adder rather than PySAT's
``PBEnc(best)``: the specified venv need not contain pypblib, the generated
gate semantics are locally auditable, and the construction is linear in the
number of operand bits instead of risking a state-per-sum BDD blow-up.

The optional mod-5 layer is accepted exactly when m=0 and d=2 (mod 5).
Then N=C-2I obeys N^2=0 and N1=0 over F_5.  Five-state deterministic
automata encode those redundant congruences over the same entry blocks.

No floating-point arithmetic is used anywhere in derivation, encoding, cube
enumeration, model decoding, or verification.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, Sequence


CLAUSE_LIMIT = 200_000_000
GENERATION_LIMIT_SECONDS = 300.0
HEADER = "p cnf {vars:20d} {clauses:20d}\n"


class EncodingLimit(RuntimeError):
    """A required explicit STOP condition was reached."""


@dataclass(frozen=True)
class Parameters:
    d: int
    m: int
    b: int
    r: int
    s: int
    diag_cap: int
    offdiag_cap: int
    diag_values: tuple[int, ...]
    offdiag_values: tuple[int, ...]
    valid_a: tuple[int, ...]

    def trace_for_a(self, a_mult: int) -> int:
        return self.d + self.r * a_mult + self.s * (self.b - 1 - a_mult)


def derive_parameters(d: int, m: int) -> Parameters:
    """Re-derive all arithmetic used by quotient_scan.py, exactly.

    The caps are floors of r+(d-r)/b and r+2(d-r)/b, additionally bounded
    by the elementary caps m and d.  Valid multiplicities are enumerated
    from the trace identity, the capped diagonal range, and (for odd m)
    evenness of every diagonal entry.
    """
    if d <= 0 or m <= 0:
        raise ValueError("d and m must be positive")
    n = d * d + 1
    if n % m:
        raise ValueError(f"m={m} does not divide d^2+1={n}")
    b = n // m
    disc = 4 * d - 3
    sq = math.isqrt(disc)
    if sq * sq != disc or (sq - 1) % 2:
        raise ValueError(f"4*d-3={disc} is not the required odd square")
    r = (-1 + sq) // 2
    s = -1 - r
    diag_cap = min(m, d, (r * b + (d - r)) // b)
    offdiag_cap = min(m, d, (r * b + 2 * (d - r)) // b)
    diag_values = tuple(
        range(0, diag_cap + 1, 2 if m % 2 else 1)
    )
    offdiag_values = tuple(range(offdiag_cap + 1))
    max_diag_value = diag_values[-1]
    valid_a = []
    for a_mult in range(b):
        trace = d + r * a_mult + s * (b - 1 - a_mult)
        if not 0 <= trace <= b * max_diag_value:
            continue
        if m % 2 and trace % 2:
            continue
        valid_a.append(a_mult)
    return Parameters(
        d=d,
        m=m,
        b=b,
        r=r,
        s=s,
        diag_cap=diag_cap,
        offdiag_cap=offdiag_cap,
        diag_values=diag_values,
        offdiag_values=offdiag_values,
        valid_a=tuple(valid_a),
    )


@dataclass
class EntryBlock:
    coord: tuple[int, int]
    values: tuple[int, ...]
    onehot: tuple[int, ...]
    bits: tuple[int, ...]

    @property
    def value_to_lit(self) -> dict[int, int]:
        return dict(zip(self.values, self.onehot, strict=True))

    @property
    def maximum(self) -> int:
        return self.values[-1]


class DimacsWriter:
    """Streaming DIMACS sink with a fixed-width seek-back header."""

    def __init__(
        self,
        path: Path,
        clause_limit: int = CLAUSE_LIMIT,
        time_limit: float = GENERATION_LIMIT_SECONDS,
    ):
        self.path = path
        self.partial = path.with_name(path.name + ".partial")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.handle = self.partial.open("w+", encoding="ascii", buffering=1024 * 1024)
        self.handle.write(HEADER.format(vars=0, clauses=0))
        self.count = 0
        self.started = time.monotonic()
        self.clause_limit = clause_limit
        self.time_limit = time_limit
        self.closed = False

    def add(self, clause: Sequence[int]) -> None:
        self.count += 1
        if self.count > self.clause_limit:
            raise EncodingLimit(
                f"clause STOP: {self.count:,} exceeds {self.clause_limit:,}"
            )
        if self.count % 100_000 == 0:
            elapsed = time.monotonic() - self.started
            if elapsed > self.time_limit:
                raise EncodingLimit(
                    f"generation STOP: {elapsed:.1f}s exceeds "
                    f"{self.time_limit:.1f}s at {self.count:,} clauses"
                )
        self.handle.write(" ".join(map(str, clause)))
        if clause:
            self.handle.write(" ")
        self.handle.write("0\n")

    def finalize(self, variables: int) -> None:
        self.handle.flush()
        self.handle.seek(0)
        header = HEADER.format(vars=variables, clauses=self.count)
        if len(header) != len(HEADER.format(vars=0, clauses=0)):
            raise AssertionError("fixed-width DIMACS header changed size")
        self.handle.write(header)
        self.handle.close()
        self.closed = True
        os.replace(self.partial, self.path)

    def abort(self) -> None:
        if not self.closed:
            self.handle.close()
            self.closed = True


class MemoryWriter:
    """Small-instance DIMACS sink used only by semantic unit tests."""

    def __init__(self):
        self.clauses: list[tuple[int, ...]] = []
        self.count = 0

    def add(self, clause: Sequence[int]) -> None:
        self.clauses.append(tuple(clause))
        self.count += 1


class CNFBuilder:
    """Deterministic variable allocator plus clause-accounting façade."""

    def __init__(self, sink: DimacsWriter | MemoryWriter):
        self.sink = sink
        self.top = 0
        self.variable_groups: Counter[str] = Counter()
        self.clause_groups: Counter[str] = Counter()

    def new_var(self, group: str) -> int:
        self.top += 1
        self.variable_groups[group] += 1
        return self.top

    def new_vars(self, number: int, group: str) -> tuple[int, ...]:
        return tuple(self.new_var(group) for _ in range(number))

    def add_clause(self, clause: Iterable[int], group: str) -> None:
        values = tuple(clause)
        if len(set(values)) != len(values):
            raise AssertionError(f"duplicate literal in clause {values}")
        if any(-lit in values for lit in values):
            raise AssertionError(f"tautological clause {values}")
        self.sink.add(values)
        self.clause_groups[group] += 1

    def exactly_one(self, lits: Sequence[int], group: str) -> None:
        if not lits:
            self.add_clause((), group)
            return
        self.add_clause(lits, group)
        for x, y in itertools.combinations(lits, 2):
            self.add_clause((-x, -y), group)

    def at_most_one(self, lits: Sequence[int], group: str) -> None:
        for x, y in itertools.combinations(lits, 2):
            self.add_clause((-x, -y), group)


def _forced_literal(variable: int, value: int) -> int:
    return variable if value else -variable


def _condition_negation(assignments: Sequence[tuple[int, int]]) -> list[int]:
    return [-var if value else var for var, value in assignments]


def encode_full_adder(
    builder: CNFBuilder,
    a: int | None,
    b: int | None,
    carry_in: int | None,
    sum_out: int,
    carry_out: int,
    group: str,
) -> None:
    """Truth-table CNF for (sum_out, carry_out) = a+b+carry_in.

    ``None`` is the Boolean constant false.  Enumerating only distinct
    nonconstant inputs avoids duplicate literals in high zero-padded bits.
    """
    inputs = (a, b, carry_in)
    variables = tuple(dict.fromkeys(v for v in inputs if v is not None))
    for values in itertools.product((0, 1), repeat=len(variables)):
        assignment = dict(zip(variables, values, strict=True))
        in_values = [0 if v is None else assignment[v] for v in inputs]
        total = sum(in_values)
        antecedent = _condition_negation(
            [(v, assignment[v]) for v in variables]
        )
        builder.add_clause(
            antecedent + [_forced_literal(sum_out, total & 1)], group
        )
        builder.add_clause(
            antecedent + [_forced_literal(carry_out, total >> 1)], group
        )


def encode_exact_sum(
    builder: CNFBuilder,
    operands: Sequence[tuple[Sequence[int], int]],
    target: int,
    group: str,
) -> None:
    """Encode an exact sum of unsigned bit buses without overflow."""
    if target < 0:
        builder.add_clause((), group)
        return
    max_total = sum(maximum for _, maximum in operands)
    if target > max_total:
        builder.add_clause((), group)
        return
    width = max(1, max_total.bit_length())
    if not operands:
        if target:
            builder.add_clause((), group)
        return

    def padded(bits: Sequence[int]) -> list[int | None]:
        if len(bits) > width:
            raise AssertionError("operand wider than exact-sum accumulator")
        return list(bits) + [None] * (width - len(bits))

    accumulator = padded(operands[0][0])
    for operand_bits, _ in operands[1:]:
        other = padded(operand_bits)
        next_accumulator = list(builder.new_vars(width, "adder_sum"))
        carry: int | None = None
        for bit in range(width):
            carry_out = builder.new_var("adder_carry")
            encode_full_adder(
                builder,
                accumulator[bit],
                other[bit],
                carry,
                next_accumulator[bit],
                carry_out,
                group,
            )
            carry = carry_out
        builder.add_clause((-carry,), group)
        accumulator = next_accumulator
    for bit, variable in enumerate(accumulator):
        expected = (target >> bit) & 1
        if variable is None:
            if expected:
                builder.add_clause((), group)
        else:
            builder.add_clause((_forced_literal(variable, expected),), group)


def enumerate_row0_cubes(params: Parameters) -> list[tuple[int, ...]]:
    """Enumerate all symmetry-sorted row-0 patterns by exact DP.

    If h=C[0,0], the *remaining* b-1 entries satisfy

        sum x_j   = d-h,
        sum x_j^2 = m+d-1-h-h^2.

    The extra ``-h^2`` is essential: the recommended-design prose's
    ``181-h`` is the total-row target, not the target for the remaining 25
    entries.  The consult's headline counts nevertheless agree with this
    corrected formula.
    """
    cubes: list[tuple[int, ...]] = []
    cap = params.offdiag_cap

    def visit(
        left: int,
        high: int,
        remaining_sum: int,
        remaining_square: int,
        prefix: tuple[int, ...],
        diagonal: int,
    ) -> None:
        if left == 0:
            if remaining_sum == 0 and remaining_square == 0:
                cubes.append((diagonal,) + prefix)
            return
        if remaining_sum < 0 or remaining_square < 0:
            return
        if remaining_sum > left * high:
            return
        if remaining_sum * remaining_sum > left * remaining_square:
            return
        if remaining_square > high * remaining_sum:
            return
        upper = min(high, remaining_sum, math.isqrt(remaining_square))
        for value in range(upper, -1, -1):
            visit(
                left - 1,
                value,
                remaining_sum - value,
                remaining_square - value * value,
                prefix + (value,),
                diagonal,
            )

    for diagonal in params.diag_values:
        visit(
            params.b - 1,
            cap,
            params.d - diagonal,
            params.m + params.d - 1 - diagonal - diagonal * diagonal,
            (),
            diagonal,
        )
    return cubes


class QuotientEncoder:
    """Construct one fixed-a quotient CNF."""

    def __init__(
        self,
        params: Parameters,
        a_mult: int | None,
        sink: DimacsWriter | MemoryWriter,
        *,
        mod5: bool = False,
        fixed_entries: dict[tuple[int, int], int] | None = None,
    ):
        self.params = params
        self.a_mult = a_mult
        self.builder = CNFBuilder(sink)
        self.mod5 = mod5
        self.fixed_entries = fixed_entries or {}
        self.entries: dict[tuple[int, int], EntryBlock] = {}
        self.product_cache: dict[
            tuple[tuple[int, int], tuple[int, int]], tuple[int, ...]
        ] = {}
        if a_mult is not None and a_mult not in params.valid_a:
            raise ValueError(
                f"a={a_mult} is outside derived valid window {params.valid_a}"
            )
        if mod5 and not (params.m % 5 == 0 and params.d % 5 == 2):
            raise ValueError(
                "--mod5 requires m == 0 and d == 2 (mod 5), the hypotheses "
                "under which N=C-2I has N^2=N1=0"
            )

    @staticmethod
    def coord(i: int, j: int) -> tuple[int, int]:
        return (i, j) if i <= j else (j, i)

    def block(self, i: int, j: int) -> EntryBlock:
        return self.entries[self.coord(i, j)]

    def allocate_entries(self) -> None:
        p = self.params
        for i in range(p.b):
            for j in range(i, p.b):
                values = p.diag_values if i == j else p.offdiag_values
                onehot = self.builder.new_vars(len(values), "entry_onehot")
                self.builder.exactly_one(onehot, "entry_exact_one")
                width = max(1, values[-1].bit_length())
                bits = self.builder.new_vars(width, "entry_bits")
                for value, literal in zip(values, onehot, strict=True):
                    for bit, output in enumerate(bits):
                        expected = (value >> bit) & 1
                        self.builder.add_clause(
                            (-literal, _forced_literal(output, expected)),
                            "entry_value_table",
                        )
                self.entries[(i, j)] = EntryBlock(
                    coord=(i, j),
                    values=values,
                    onehot=onehot,
                    bits=bits,
                )
        for coord, value in self.fixed_entries.items():
            block = self.entries[self.coord(*coord)]
            try:
                literal = block.value_to_lit[value]
            except KeyError as exc:
                raise ValueError(
                    f"fixed C{coord}={value} outside {block.values}"
                ) from exc
            self.builder.add_clause((literal,), "fixed_entry")

    def product_bits(self, left: EntryBlock, right: EntryBlock) -> tuple[int, ...]:
        key = tuple(sorted((left.coord, right.coord)))
        cached = self.product_cache.get(key)
        if cached is not None:
            return cached
        maximum = left.maximum * right.maximum
        width = max(1, maximum.bit_length())
        outputs = self.builder.new_vars(width, "product_bits")
        if left.coord == right.coord:
            for value, literal in zip(
                left.values, left.onehot, strict=True
            ):
                product = value * value
                for bit, output in enumerate(outputs):
                    self.builder.add_clause(
                        (-literal, _forced_literal(output, (product >> bit) & 1)),
                        "product_value_table",
                    )
        else:
            for lv, llit in zip(left.values, left.onehot, strict=True):
                for rv, rlit in zip(right.values, right.onehot, strict=True):
                    product = lv * rv
                    for bit, output in enumerate(outputs):
                        self.builder.add_clause(
                            (
                                -llit,
                                -rlit,
                                _forced_literal(output, (product >> bit) & 1),
                            ),
                            "product_value_table",
                        )
        self.product_cache[key] = outputs
        return outputs

    def add_row_sums(self) -> None:
        p = self.params
        for i in range(p.b):
            operands = [
                (self.block(i, j).bits, self.block(i, j).maximum)
                for j in range(p.b)
            ]
            encode_exact_sum(
                self.builder, operands, p.d, "row_sum_adder"
            )

    def add_trace(self) -> None:
        if self.a_mult is None:
            return
        p = self.params
        target = p.trace_for_a(self.a_mult)
        operands = [
            (self.block(i, i).bits, self.block(i, i).maximum)
            for i in range(p.b)
        ]
        encode_exact_sum(
            self.builder, operands, target, "trace_adder"
        )

    def add_quotient_equations(self) -> None:
        p = self.params
        for i in range(p.b):
            for j in range(i, p.b):
                operands: list[tuple[Sequence[int], int]] = []
                for t in range(p.b):
                    left = self.block(i, t)
                    right = self.block(j, t)
                    operands.append(
                        (
                            self.product_bits(left, right),
                            left.maximum * right.maximum,
                        )
                    )
                entry = self.block(i, j)
                operands.append((entry.bits, entry.maximum))
                target = p.m + (p.d - 1 if i == j else 0)
                encode_exact_sum(
                    self.builder,
                    operands,
                    target,
                    "quadratic_sum_adder",
                )

    def add_symmetry_breaking(self) -> None:
        p = self.params
        first_diag = self.block(0, 0)
        for i in range(1, p.b):
            current = self.block(i, i)
            for first_value, first_lit in zip(
                first_diag.values, first_diag.onehot, strict=True
            ):
                for value, literal in zip(
                    current.values, current.onehot, strict=True
                ):
                    if value > first_value:
                        self.builder.add_clause(
                            (-first_lit, -literal), "symmetry_max_diagonal"
                        )
        for j in range(1, p.b - 1):
            previous = self.block(0, j)
            following = self.block(0, j + 1)
            for pv, plit in zip(
                previous.values, previous.onehot, strict=True
            ):
                for fv, flit in zip(
                    following.values, following.onehot, strict=True
                ):
                    if fv > pv:
                        self.builder.add_clause(
                            (-plit, -flit), "symmetry_sorted_row0"
                        )

    def _mod5_initial_state(self) -> tuple[int, ...]:
        state = self.builder.new_vars(5, "mod5_state")
        for residue, literal in enumerate(state):
            self.builder.add_clause(
                (_forced_literal(literal, int(residue == 0)),),
                "mod5_state_boundary",
            )
        return state

    def _mod5_next_state(self) -> tuple[int, ...]:
        state = self.builder.new_vars(5, "mod5_state")
        self.builder.at_most_one(state, "mod5_state_amo")
        return state

    def _mod5_finish(self, state: Sequence[int]) -> None:
        self.builder.add_clause((state[0],), "mod5_state_boundary")

    def _mod5_onehot_event(
        self,
        state: Sequence[int],
        choices: Sequence[tuple[int, int]],
    ) -> tuple[int, ...]:
        following = self._mod5_next_state()
        for residue, state_lit in enumerate(state):
            for event_lit, weight in choices:
                self.builder.add_clause(
                    (
                        -state_lit,
                        -event_lit,
                        following[(residue + weight) % 5],
                    ),
                    "mod5_transition",
                )
        return following

    def _mod5_bus_event(
        self, state: Sequence[int], bits: Sequence[int]
    ) -> tuple[int, ...]:
        if len(bits) != 3:
            raise AssertionError("mod-5 residue bus must have three bits")
        following = self._mod5_next_state()
        for residue, state_lit in enumerate(state):
            for value in range(5):
                exclude_value = [
                    -bit if (value >> index) & 1 else bit
                    for index, bit in enumerate(bits)
                ]
                self.builder.add_clause(
                    (
                        -state_lit,
                        *exclude_value,
                        following[(residue + value) % 5],
                    ),
                    "mod5_transition",
                )
        return following

    def _mod5_pair_product_bus(
        self,
        left: EntryBlock,
        right: EntryBlock,
        left_shift: int,
        right_shift: int,
    ) -> tuple[int, ...]:
        outputs = self.builder.new_vars(3, "mod5_product_bits")
        if left.coord == right.coord:
            raise AssertionError("cross-equation pair blocks must differ")
        for lv, llit in zip(left.values, left.onehot, strict=True):
            for rv, rlit in zip(right.values, right.onehot, strict=True):
                value = ((lv - left_shift) * (rv - right_shift)) % 5
                for bit, output in enumerate(outputs):
                    self.builder.add_clause(
                        (
                            -llit,
                            -rlit,
                            _forced_literal(output, (value >> bit) & 1),
                        ),
                        "mod5_product_table",
                    )
        return outputs

    def add_mod5(self) -> None:
        """Add the redundant N1=0 and N^2=0 congruence automata."""
        p = self.params
        # N 1 = 0: event weights are C[i,j]-2[i=j].
        for i in range(p.b):
            state = self._mod5_initial_state()
            for j in range(p.b):
                block = self.block(i, j)
                choices = [
                    (literal, (value - (2 if i == j else 0)) % 5)
                    for value, literal in zip(
                        block.values, block.onehot, strict=True
                    )
                ]
                state = self._mod5_onehot_event(state, choices)
            self._mod5_finish(state)

        # N^2 = 0.  Self terms are squares of one selected entry value;
        # cross terms use a fully determined 3-bit product-residue table.
        for i in range(p.b):
            for j in range(i, p.b):
                state = self._mod5_initial_state()
                for t in range(p.b):
                    left = self.block(i, t)
                    if i == j:
                        shift = 2 if t == i else 0
                        choices = [
                            (literal, ((value - shift) ** 2) % 5)
                            for value, literal in zip(
                                left.values, left.onehot, strict=True
                            )
                        ]
                        state = self._mod5_onehot_event(state, choices)
                    else:
                        right = self.block(j, t)
                        bits = self._mod5_pair_product_bus(
                            left,
                            right,
                            2 if t == i else 0,
                            2 if t == j else 0,
                        )
                        state = self._mod5_bus_event(state, bits)
                self._mod5_finish(state)

    def build(self) -> dict[str, object]:
        started = time.monotonic()
        self.allocate_entries()
        self.add_row_sums()
        self.add_trace()
        self.add_quotient_equations()
        self.add_symmetry_breaking()
        if self.mod5:
            self.add_mod5()
        elapsed = time.monotonic() - started
        return {
            "schema": 1,
            "d": self.params.d,
            "m": self.params.m,
            "b": self.params.b,
            "r": self.params.r,
            "s": self.params.s,
            "diag_cap": self.params.diag_cap,
            "offdiag_cap": self.params.offdiag_cap,
            "valid_a": list(self.params.valid_a),
            "a": self.a_mult,
            "trace": (
                None
                if self.a_mult is None
                else self.params.trace_for_a(self.a_mult)
            ),
            "mod5": self.mod5,
            "variables": self.builder.top,
            "clauses": self.builder.sink.count,
            "seconds": elapsed,
            "variable_groups": dict(sorted(self.builder.variable_groups.items())),
            "clause_groups": dict(sorted(self.builder.clause_groups.items())),
            "entries": [
                {
                    "i": i,
                    "j": j,
                    "values": list(block.values),
                    "onehot": list(block.onehot),
                }
                for (i, j), block in sorted(self.entries.items())
            ],
        }


def metadata_path(cnf_path: Path) -> Path:
    return cnf_path.with_name(cnf_path.name + ".map.json")


def write_metadata(path: Path, metadata: dict[str, object]) -> None:
    temporary = path.with_name(path.name + ".partial")
    with temporary.open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2, sort_keys=True)
        handle.write("\n")
    os.replace(temporary, path)


def encode_to_file(
    d: int,
    m: int,
    a_mult: int | None,
    output: Path,
    *,
    mod5: bool = False,
    fixed_entries: dict[tuple[int, int], int] | None = None,
) -> dict[str, object]:
    params = derive_parameters(d, m)
    writer = DimacsWriter(output)
    encoder = QuotientEncoder(
        params,
        a_mult,
        writer,
        mod5=mod5,
        fixed_entries=fixed_entries,
    )
    try:
        metadata = encoder.build()
        writer.finalize(encoder.builder.top)
    except Exception:
        writer.abort()
        raise
    write_metadata(metadata_path(output), metadata)
    return metadata


def _clone_file(source: Path, destination: Path) -> None:
    """Use APFS copy-on-write when available; fall back to a byte copy."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["cp", "-c", str(source), str(destination)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if result.returncode:
        shutil.copyfile(source, destination)


def clone_with_units(
    base_cnf: Path,
    destination: Path,
    units: Sequence[int],
    base_metadata: dict[str, object],
    cube: Sequence[int],
) -> None:
    """Materialize one real cube-restricted CNF from a base via COW clone."""
    _clone_file(base_cnf, destination)
    clauses = int(base_metadata["clauses"]) + len(units)
    variables = int(base_metadata["variables"])
    with destination.open("r+", encoding="ascii", buffering=1024 * 1024) as handle:
        handle.seek(0)
        handle.write(HEADER.format(vars=variables, clauses=clauses))
        handle.seek(0, os.SEEK_END)
        for literal in units:
            handle.write(f"{literal} 0\n")
    metadata = dict(base_metadata)
    metadata["clauses"] = clauses
    metadata["cube"] = list(cube)
    groups = dict(metadata["clause_groups"])
    groups["cube_units"] = len(units)
    metadata["clause_groups"] = groups
    write_metadata(metadata_path(destination), metadata)


def cube_units(
    metadata: dict[str, object], cube: Sequence[int]
) -> tuple[int, ...]:
    blocks = {
        (int(entry["i"]), int(entry["j"])): entry
        for entry in metadata["entries"]  # type: ignore[index]
    }
    units = []
    for j, value in enumerate(cube):
        block = blocks[(0, j)]
        mapping = dict(
            zip(block["values"], block["onehot"], strict=True)
        )
        units.append(int(mapping[value]))
    return tuple(units)


def filtered_cubes(
    params: Parameters, a_mult: int | None
) -> list[tuple[int, ...]]:
    cubes = enumerate_row0_cubes(params)
    if a_mult is None:
        return cubes
    trace = params.trace_for_a(a_mult)
    # Max-diagonal symmetry gives every diagonal <= cube[0].
    return [cube for cube in cubes if trace <= params.b * cube[0]]


def emit_cubes(
    d: int,
    m: int,
    a_mult: int | None,
    output: Path,
    *,
    mod5: bool,
) -> tuple[Path, list[Path], dict[str, object]]:
    """Emit one actual DIMACS file per exhaustive row-0 cube.

    A copy-on-write clone of a single encoded base makes the required
    many-CNF format practical on APFS without weakening the solver/checker
    interface: every cube file is standalone DIMACS and carries its own map.
    """
    params = derive_parameters(d, m)
    cube_list = filtered_cubes(params, a_mult)
    directory = output.with_suffix(output.suffix + ".cubes")
    directory.mkdir(parents=True, exist_ok=True)
    base = directory / "_base.cnf"
    metadata = encode_to_file(d, m, a_mult, base, mod5=mod5)
    emitted = []
    width = max(1, len(str(max(0, len(cube_list) - 1))))
    for index, cube in enumerate(cube_list):
        destination = directory / f"cube-{index:0{width}d}.cnf"
        clone_with_units(
            base,
            destination,
            cube_units(metadata, cube),
            metadata,
            cube,
        )
        emitted.append(destination)
    manifest = {
        "schema": 1,
        "base": str(base),
        "count": len(cube_list),
        "files": [str(path) for path in emitted],
        "cubes": [list(cube) for cube in cube_list],
    }
    write_metadata(directory / "manifest.json", manifest)
    return directory, emitted, metadata


def output_for_a(base: Path, a_mult: int, multiple: bool) -> Path:
    if not multiple:
        return base
    if base.suffix:
        return base.with_name(f"{base.stem}.a{a_mult}{base.suffix}")
    return base.with_name(f"{base.name}.a{a_mult}.cnf")


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("d", type=int)
    parser.add_argument("m", type=int)
    parser.add_argument("a", help="one derived multiplicity, or 'all'")
    parser.add_argument("--mod5", action="store_true")
    parser.add_argument("--cubes", action="store_true")
    parser.add_argument("-o", "--output", type=Path)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    params = derive_parameters(args.d, args.m)
    if args.a == "all":
        multiplicities = list(params.valid_a)
    else:
        multiplicities = [int(args.a)]
    if not multiplicities:
        raise SystemExit("derived valid-a window is empty")
    if args.output is None and len(multiplicities) != 1:
        raise SystemExit(
            "'all' cannot concatenate multiple DIMACS headers on one stdout; "
            "supply -o BASE.cnf"
        )
    for a_mult in multiplicities:
        if a_mult not in params.valid_a:
            raise SystemExit(
                f"a={a_mult} not in derived valid window {params.valid_a}"
            )
        output = (
            output_for_a(args.output, a_mult, len(multiplicities) > 1)
            if args.output is not None
            else Path("-")
        )
        try:
            if output == Path("-"):
                if args.cubes:
                    raise SystemExit("--cubes requires -o BASE.cnf")
                with tempfile.TemporaryDirectory(
                    prefix="quotient-stdout-"
                ) as raw:
                    temporary = Path(raw) / "instance.cnf"
                    metadata = encode_to_file(
                        args.d, args.m, a_mult, temporary, mod5=args.mod5
                    )
                    with temporary.open("rb") as source:
                        shutil.copyfileobj(source, sys.stdout.buffer)
                    print(
                        f"d={args.d} m={args.m} b={params.b} a={a_mult} "
                        f"mod5={args.mod5}: vars={metadata['variables']:,} "
                        f"clauses={metadata['clauses']:,} "
                        f"seconds={metadata['seconds']:.3f} output=stdout",
                        file=sys.stderr,
                        flush=True,
                    )
                continue
            if args.cubes:
                directory, files, metadata = emit_cubes(
                    args.d, args.m, a_mult, output, mod5=args.mod5
                )
                print(
                    f"d={args.d} m={args.m} b={params.b} a={a_mult} "
                    f"mod5={args.mod5}: {len(files)} cubes in {directory}; "
                    f"base vars={metadata['variables']:,} "
                    f"clauses={metadata['clauses']:,} "
                    f"seconds={metadata['seconds']:.3f}",
                    flush=True,
                )
            else:
                metadata = encode_to_file(
                    args.d, args.m, a_mult, output, mod5=args.mod5
                )
                print(
                    f"d={args.d} m={args.m} b={params.b} a={a_mult} "
                    f"mod5={args.mod5}: vars={metadata['variables']:,} "
                    f"clauses={metadata['clauses']:,} "
                    f"seconds={metadata['seconds']:.3f} output={output}",
                    flush=True,
                )
        except EncodingLimit as exc:
            print(f"STOP d={args.d} m={args.m} a={a_mult}: {exc}", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""End-to-end validation gates for the quotient SAT + DRAT pipeline."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import time
import unittest
from collections import Counter
from pathlib import Path

from encode_quotient import (
    clone_with_units,
    cube_units,
    derive_parameters,
    encode_to_file,
    enumerate_row0_cubes,
    filtered_cubes,
)
from run_and_check import run_one


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
QUOTIENT_SCAN = PARENT / "quotient_scan.py"
CONSULT_COUNTS = {0: 218, 2: 241, 4: 169, 6: 70, 8: 8}


def load_quotient_scan():
    spec = importlib.util.spec_from_file_location(
        "quotient_scan_reference", QUOTIENT_SCAN
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {QUOTIENT_SCAN}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def capture_reference_caps(module, d: int, m: int) -> tuple[int, int, int]:
    """Read quotient_scan.py's own live locals after its cap computation."""
    captured: dict[str, int] = {}
    target_code = module.search_quotients.__code__

    def tracer(frame, event, arg):
        if frame.f_code is target_code and event == "line":
            local = frame.f_locals
            if "diag_cap" in local and "offdiag_cap" in local:
                captured["b"] = int(local["b"])
                captured["diag_cap"] = int(local["diag_cap"])
                captured["offdiag_cap"] = int(local["offdiag_cap"])
        return tracer

    old_trace = sys.gettrace()
    sys.settrace(tracer)
    try:
        module.search_quotients(
            d, m, max_solutions=0, max_nodes=0, progress=False
        )
    finally:
        sys.settrace(old_trace)
    if set(captured) != {"b", "diag_cap", "offdiag_cap"}:
        raise AssertionError(
            f"failed to capture quotient_scan cap locals for d={d},m={m}: "
            f"{captured}"
        )
    return (
        captured["b"],
        captured["diag_cap"],
        captured["offdiag_cap"],
    )


class EncoderValidation(unittest.TestCase):
    maxDiff = None

    def test_00_cap_and_window_equivalence(self):
        reference = load_quotient_scan()
        expected = {
            (57, 125): (26, 8, 10, (11, 13, 15, 17, 19, 21, 23)),
            (7, 25): (2, 4, 7, (0,)),
            (7, 10): (5, 3, 4, (1, 2, 3, 4)),
            (7, 5): (10, 2, 3, (4, 6, 8)),
        }
        print("GATE (pre): live cap equivalence against quotient_scan.py")
        for (d, m), wanted in expected.items():
            params = derive_parameters(d, m)
            live = capture_reference_caps(reference, d, m)
            derived = (params.b, params.diag_cap, params.offdiag_cap)
            self.assertEqual(live, derived)
            self.assertEqual(
                (
                    params.b,
                    params.diag_cap,
                    params.offdiag_cap,
                    params.valid_a,
                ),
                wanted,
            )
            print(
                f"CAP CHECK d={d} m={m}: b={params.b} "
                f"diag_cap={params.diag_cap} "
                f"offdiag_cap={params.offdiag_cap} "
                f"valid_a={list(params.valid_a)} MATCH"
            )

    def test_01_gate_a_d7_sat_and_exact_decode(self):
        cases = ((25, 0), (10, 4), (5, 4))
        print("GATE (a): d=7 known-feasible analogues")
        with tempfile.TemporaryDirectory(prefix="quotient-gate-a-") as raw:
            directory = Path(raw)
            for m, a_mult in cases:
                output = directory / f"d7-m{m}-a{a_mult}.cnf"
                generation_started = time.monotonic()
                metadata = encode_to_file(7, m, a_mult, output)
                generation_seconds = time.monotonic() - generation_started
                print(
                    f"GATE (a) d=7 m={m} b={metadata['b']} a={a_mult}: "
                    f"generated vars={metadata['variables']} "
                    f"clauses={metadata['clauses']} "
                    f"in {generation_seconds:.3f}s"
                )
                result = run_one(output, timeout_seconds=30)
                self.assertEqual(result.status, "SAT")
                self.assertIsNotNone(result.matrix)

    def test_02_gate_b_real_unsat_drat_pipeline(self):
        print(
            "GATE (b): d=7,m=25,a=0 plus impossible C[0][0]=0 "
            "(genuine solution requires trace 4 and max-diagonal symmetry)"
        )
        with tempfile.TemporaryDirectory(prefix="quotient-gate-b-") as raw:
            output = Path(raw) / "d7-m25-a0-c00zero.cnf"
            metadata = encode_to_file(
                7, 25, 0, output, fixed_entries={(0, 0): 0}
            )
            print(
                f"GATE (b) generated vars={metadata['variables']} "
                f"clauses={metadata['clauses']}"
            )
            result = run_one(output, timeout_seconds=30)
            self.assertEqual(result.status, "UNSAT")
            self.assertTrue(result.proof_verified)
            self.assertEqual(result.checker_exit, 0)

    def test_03_gate_c_cube_split_union(self):
        # d=7,m=10 has two genuinely distinct sorted row-0 DP patterns.
        # Fixing a=4 makes the h=1 cube UNSAT by trace/max-diagonal and the
        # h=3 cube SAT, so this exercises both branches and proof checking.
        params = derive_parameters(7, 10)
        cubes = enumerate_row0_cubes(params)
        self.assertEqual(len(cubes), 2)
        print(
            f"GATE (c): d=7 m=10 a=4 enumerated {len(cubes)} row-0 cubes"
        )
        with tempfile.TemporaryDirectory(prefix="quotient-gate-c-") as raw:
            directory = Path(raw)
            base = directory / "base.cnf"
            metadata = encode_to_file(7, 10, 4, base)
            results = []
            checker_errors = []
            statuses = []
            for index, cube in enumerate(cubes):
                path = directory / f"cube-{index}.cnf"
                clone_with_units(
                    base,
                    path,
                    cube_units(metadata, cube),
                    metadata,
                    cube,
                )
                print(f"GATE (c) cube {index}: row0={cube}")
                try:
                    result = run_one(path, timeout_seconds=30)
                except FileNotFoundError as exc:
                    checker_errors.append(str(exc))
                    statuses.append("UNSAT-UNCHECKED")
                    print(
                        f"GATE (c) cube {index} result=UNSAT-UNCHECKED: {exc}"
                    )
                    continue
                results.append(result)
                statuses.append(result.status)
                print(
                    f"GATE (c) cube {index} result={result.status} "
                    f"wall={result.seconds:.3f}s"
                )
            self.assertIn("SAT", statuses)
            if checker_errors:
                self.fail(
                    "cube UNSAT proof(s) were not checked:\n"
                    + "\n".join(checker_errors)
                )
            self.assertEqual(statuses, ["UNSAT", "SAT"])
            self.assertTrue(results[0].proof_verified)
            print(
                "GATE (c) cube union: at least one SAT found overall; "
                "row-0 DP + symmetry breaking lost no solution in this case"
            )

    def test_04_gate_d_exact_row0_counts(self):
        params = derive_parameters(57, 125)
        self.assertEqual((params.b, params.diag_cap, params.offdiag_cap), (26, 8, 10))
        counts = Counter(cube[0] for cube in enumerate_row0_cubes(params))
        self.assertEqual(len(filtered_cubes(params, 23)), 8)
        print(
            "GATE (d): both constraints used for 25 sorted off-diagonal "
            "entries: linear sum=57-h AND square sum=181-h-h^2"
        )
        for diagonal in (0, 2, 4, 6, 8):
            actual = counts[diagonal]
            claimed = CONSULT_COUNTS[diagonal]
            comparison = "MATCH" if actual == claimed else "MISMATCH"
            print(
                f"GATE (d) C[0][0]={diagonal}: recomputed={actual} "
                f"consult={claimed} {comparison}"
            )
            self.assertEqual(actual, claimed)
        print(
            "GATE (d) fixed a=23 plus max-diagonal trace bound retains "
            "8 cube patterns"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

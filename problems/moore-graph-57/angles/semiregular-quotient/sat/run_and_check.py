#!/usr/bin/env python3
"""Run Kissat with a hard cap, check DRAT, or exactly decode a SAT model.

The companion ``.map.json`` is not trusted as a mathematical verdict.  It
only maps primary one-hot variables back to matrix entries.  Every SAT model
is independently checked with NumPy int64 matrix multiplication and Python
integer structural checks.  Every UNSAT result is accepted only when the
local drat-trim binary prints ``s VERIFIED`` and exits successfully.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import numpy as np

from encode_quotient import metadata_path


HERE = Path(__file__).resolve().parent
DEFAULT_DRAT_TRIM = HERE / "tools" / "drat-trim" / "drat-trim"
MAX_SOLVER_SECONDS = 600


@dataclass
class RunResult:
    status: str
    seconds: float
    solver_exit: int | None
    proof_verified: bool = False
    checker_exit: int | None = None
    matrix: np.ndarray | None = None
    solver_stdout: str = ""
    checker_stdout: str = ""


def load_metadata(cnf: Path) -> dict[str, object]:
    path = metadata_path(cnf)
    if not path.is_file():
        raise FileNotFoundError(f"missing decode map: {path}")
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def parse_model(output: str) -> set[int]:
    positive: set[int] = set()
    saw_model = False
    for line in output.splitlines():
        if not line.startswith("v"):
            continue
        saw_model = True
        for token in line[1:].split():
            literal = int(token)
            if literal > 0:
                positive.add(literal)
    if not saw_model:
        raise AssertionError("SAT solver returned SAT but printed no model lines")
    return positive


def decode_and_verify(
    metadata: dict[str, object], model: set[int]
) -> np.ndarray:
    d = int(metadata["d"])
    m = int(metadata["m"])
    b = int(metadata["b"])
    matrix = np.zeros((b, b), dtype=np.int64)
    for entry in metadata["entries"]:  # type: ignore[index]
        i = int(entry["i"])
        j = int(entry["j"])
        values = [int(value) for value in entry["values"]]
        variables = [int(variable) for variable in entry["onehot"]]
        selected = [
            value
            for value, variable in zip(values, variables, strict=True)
            if variable in model
        ]
        if len(selected) != 1:
            raise AssertionError(
                f"entry C[{i}][{j}] selected {selected}, expected exactly one; "
                f"onehot vars={variables}"
            )
        matrix[i, j] = matrix[j, i] = selected[0]

    if not np.array_equal(matrix, matrix.T):
        raise AssertionError(f"decoded matrix is not symmetric:\n{matrix}")
    if np.any(matrix < 0):
        raise AssertionError(f"decoded matrix has a negative entry:\n{matrix}")
    row_sums = matrix.sum(axis=1, dtype=np.int64)
    if not np.all(row_sums == d):
        raise AssertionError(
            f"row sums differ from d={d}: {row_sums.tolist()}\n{matrix}"
        )
    if m % 2 and np.any(np.diag(matrix) % 2):
        raise AssertionError(
            f"m={m} is odd but diagonal is not even: "
            f"{np.diag(matrix).tolist()}\n{matrix}"
        )
    identity = np.eye(b, dtype=np.int64)
    lhs = matrix @ matrix + matrix - np.int64(d - 1) * identity
    target = np.full((b, b), m, dtype=np.int64)
    if not np.array_equal(lhs, target):
        bad = np.argwhere(lhs != target)
        details = [
            (
                int(i),
                int(j),
                int(lhs[i, j]),
                int(target[i, j]),
                int(sum(int(matrix[i, t]) * int(matrix[t, j]) for t in range(b))),
            )
            for i, j in bad[:20]
        ]
        raise AssertionError(
            "quotient identity failed at (i,j,lhs,target,C2): "
            f"{details}\n{matrix}"
        )
    a_mult = metadata.get("a")
    if a_mult is not None:
        expected_trace = int(metadata["trace"])
        actual_trace = int(np.trace(matrix, dtype=np.int64))
        if actual_trace != expected_trace:
            raise AssertionError(
                f"trace {actual_trace} != fixed-a trace {expected_trace}"
            )
    return matrix


def _remove_old_proof(path: Path) -> None:
    if path.exists():
        path.unlink()


def run_one(
    cnf: Path,
    *,
    timeout_seconds: int = MAX_SOLVER_SECONDS,
    solver: str = "kissat",
    drat_trim: Path = DEFAULT_DRAT_TRIM,
    print_output: bool = True,
) -> RunResult:
    if not 1 <= timeout_seconds <= MAX_SOLVER_SECONDS:
        raise ValueError(
            f"timeout must be 1..{MAX_SOLVER_SECONDS}, got {timeout_seconds}"
        )
    metadata = load_metadata(cnf)
    proof = cnf.with_name(cnf.name + ".drat")
    _remove_old_proof(proof)
    command = [
        solver,
        "--quiet",
        "--no-binary",
        f"--time={timeout_seconds}",
        str(cnf),
        str(proof),
    ]
    started = time.monotonic()
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    try:
        stdout, _ = process.communicate(timeout=timeout_seconds)
    except subprocess.TimeoutExpired:
        process.kill()
        stdout, _ = process.communicate()
        elapsed = time.monotonic() - started
        if print_output:
            print(
                f"TIMEOUT cnf={cnf} wall={elapsed:.3f}s "
                f"cap={timeout_seconds}s",
                flush=True,
            )
        return RunResult(
            status="TIMEOUT",
            seconds=elapsed,
            solver_exit=None,
            solver_stdout=stdout,
        )
    elapsed = time.monotonic() - started
    exit_code = process.returncode
    if exit_code == 10 or "s SATISFIABLE" in stdout:
        try:
            matrix = decode_and_verify(metadata, parse_model(stdout))
        except Exception as exc:
            if print_output:
                print(
                    f"ENCODER BUG cnf={cnf} solver_exit={exit_code} "
                    f"wall={elapsed:.3f}s: {exc}",
                    flush=True,
                )
            raise
        if print_output:
            print(
                f"SAT cnf={cnf} solver_exit={exit_code} wall={elapsed:.3f}s",
                flush=True,
            )
            print("DECODE CHECK: VERIFIED exact int64 quotient identity", flush=True)
            print(matrix, flush=True)
        return RunResult(
            status="SAT",
            seconds=elapsed,
            solver_exit=exit_code,
            matrix=matrix,
            solver_stdout=stdout,
        )
    if exit_code == 20 or "s UNSATISFIABLE" in stdout:
        if print_output:
            print(
                f"UNSAT cnf={cnf} solver_exit={exit_code} wall={elapsed:.3f}s",
                flush=True,
            )
        if not drat_trim.is_file() or not os.access(drat_trim, os.X_OK):
            raise FileNotFoundError(
                f"UNSAT proof exists at {proof}, but drat-trim binary is "
                f"missing or not executable: {drat_trim}"
            )
        checker = subprocess.run(
            [str(drat_trim), str(cnf), str(proof)],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=MAX_SOLVER_SECONDS,
            check=False,
        )
        checker_output = checker.stdout
        if print_output:
            print("DRAT-TRIM OUTPUT BEGIN", flush=True)
            print(checker_output.rstrip(), flush=True)
            print("DRAT-TRIM OUTPUT END", flush=True)
            print(f"DRAT-TRIM EXIT: {checker.returncode}", flush=True)
        verified = checker.returncode == 0 and "s VERIFIED" in checker_output
        if not verified:
            raise AssertionError(
                f"drat-trim rejected proof: exit={checker.returncode}\n"
                f"{checker_output}"
            )
        return RunResult(
            status="UNSAT",
            seconds=elapsed,
            solver_exit=exit_code,
            proof_verified=True,
            checker_exit=checker.returncode,
            solver_stdout=stdout,
            checker_stdout=checker_output,
        )
    if exit_code == 0 and (
        "s UNKNOWN" in stdout or elapsed >= 0.95 * timeout_seconds
    ):
        if print_output:
            print(
                f"TIMEOUT cnf={cnf} solver_exit={exit_code} "
                f"wall={elapsed:.3f}s cap={timeout_seconds}s",
                flush=True,
            )
        return RunResult(
            status="TIMEOUT",
            seconds=elapsed,
            solver_exit=exit_code,
            solver_stdout=stdout,
        )
    if print_output:
        print(
            f"SOLVER ERROR cnf={cnf} exit={exit_code} wall={elapsed:.3f}s",
            flush=True,
        )
        print(stdout.rstrip(), flush=True)
    raise RuntimeError(
        f"solver returned neither SAT nor UNSAT: exit={exit_code}\n{stdout}"
    )


def run_cube_directory(
    directory: Path,
    *,
    timeout_seconds: int,
    solver: str,
    drat_trim: Path,
) -> list[RunResult]:
    manifest_path = directory / "manifest.json"
    with manifest_path.open(encoding="utf-8") as handle:
        manifest = json.load(handle)
    files = [Path(path) for path in manifest["files"]]
    print(f"CUBES count={len(files)} directory={directory}", flush=True)
    results = []
    for index, path in enumerate(files):
        print(f"CUBE {index}/{len(files)-1} file={path}", flush=True)
        result = run_one(
            path,
            timeout_seconds=timeout_seconds,
            solver=solver,
            drat_trim=drat_trim,
        )
        results.append(result)
    sat_count = sum(result.status == "SAT" for result in results)
    unsat_count = sum(result.status == "UNSAT" for result in results)
    timeout_count = sum(result.status == "TIMEOUT" for result in results)
    print(
        f"CUBE UNION: SAT={sat_count} UNSAT={unsat_count} "
        f"TIMEOUT={timeout_count} at_least_one_sat={sat_count > 0}",
        flush=True,
    )
    return results


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="CNF or emitted .cnf.cubes dir")
    parser.add_argument("--timeout", type=int, default=MAX_SOLVER_SECONDS)
    parser.add_argument("--solver", default="kissat")
    parser.add_argument("--drat-trim", type=Path, default=DEFAULT_DRAT_TRIM)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    if args.input.is_dir():
        results = run_cube_directory(
            args.input,
            timeout_seconds=args.timeout,
            solver=args.solver,
            drat_trim=args.drat_trim,
        )
        return 0 if all(result.status != "TIMEOUT" for result in results) else 124
    result = run_one(
        args.input,
        timeout_seconds=args.timeout,
        solver=args.solver,
        drat_trim=args.drat_trim,
    )
    return 124 if result.status == "TIMEOUT" else 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Exact-arithmetic checks for Kakeya exponent ledgers.

The convention is that a shaded union in R^n obeys

    |union Y(T)| >= delta^(volume_exponent + o(1)).

Since 0 < delta < 1, a smaller volume exponent is a stronger lower bound.
The corresponding Minkowski-dimension lower bound is n-volume_exponent.
When a proof splits into exhaustive branches, its unconditional volume
exponent is the maximum (weakest) branch exponent.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any


def q(value: str | int) -> Fraction:
    """Parse an integer or a slash-separated rational exactly."""
    if isinstance(value, int):
        return Fraction(value)
    return Fraction(value)


def quotient_delta_exponent(
    numerator_exponent: Fraction, denominator_exponent: Fraction
) -> Fraction:
    """If A>=delta^a and B<=delta^b, then A/B>=delta^(a-b)."""
    return numerator_exponent - denominator_exponent


@dataclass(frozen=True)
class Branch:
    name: str
    volume_exponent: Fraction
    dimension_bound: Fraction

    @classmethod
    def from_json(cls, record: dict[str, Any], ambient_dimension: int) -> "Branch":
        volume_exponent = q(record["volume_exponent"])
        dimension_bound = q(record["dimension_bound"])
        expected = Fraction(ambient_dimension) - volume_exponent
        if dimension_bound != expected:
            raise ValueError(
                f"{record['name']}: dimension_bound={dimension_bound}, "
                f"but n-volume_exponent={expected}"
            )
        return cls(record["name"], volume_exponent, dimension_bound)


def verify_ledger(data: dict[str, Any]) -> dict[str, str]:
    ambient_dimension = int(data["ambient_dimension"])
    branches = [
        Branch.from_json(record, ambient_dimension) for record in data["branches"]
    ]
    if not branches:
        raise ValueError("ledger must contain at least one branch")

    global_volume = max(branch.volume_exponent for branch in branches)
    global_dimension = min(branch.dimension_bound for branch in branches)
    claimed_volume = q(data["claimed_global"]["volume_exponent"])
    claimed_dimension = q(data["claimed_global"]["dimension_bound"])

    if claimed_volume != global_volume:
        raise ValueError(
            f"claimed global volume exponent {claimed_volume}; "
            f"branch maximum is {global_volume}"
        )
    if claimed_dimension != global_dimension:
        raise ValueError(
            f"claimed global dimension {claimed_dimension}; "
            f"branch minimum is {global_dimension}"
        )
    if global_dimension != Fraction(ambient_dimension) - global_volume:
        raise AssertionError("branch aggregation is inconsistent")

    bottlenecks = sorted(
        branch.name for branch in branches if branch.volume_exponent == global_volume
    )
    return {
        "ambient_dimension": str(ambient_dimension),
        "global_volume_exponent": str(global_volume),
        "global_dimension_bound": str(global_dimension),
        "bottleneck_branches": ",".join(bottlenecks),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("ledger", type=Path)
    args = parser.parse_args()
    with args.ledger.open(encoding="utf-8") as handle:
        data = json.load(handle)
    result = verify_ledger(data)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

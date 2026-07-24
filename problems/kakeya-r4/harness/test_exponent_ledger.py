import json
import unittest
from fractions import Fraction
from pathlib import Path

from exponent_ledger import q, quotient_delta_exponent, verify_ledger


HERE = Path(__file__).resolve().parent


class ExponentLedgerTests(unittest.TestCase):
    def test_fraction_parser_is_exact(self) -> None:
        self.assertEqual(q("13/4"), Fraction(13, 4))

    def test_extremal_multiplicity_sign(self) -> None:
        # mass >= delta^eta and volume <= delta^(sigma-eta)
        # imply multiplicity >= delta^(-sigma+2 eta).
        sigma = Fraction(3, 4)
        eta = Fraction(1, 100)
        self.assertEqual(
            quotient_delta_exponent(eta, sigma - eta), -sigma + 2 * eta
        )

    def test_prompt_benchmark(self) -> None:
        data = json.loads((HERE / "benchmark_ledger.json").read_text())
        self.assertEqual(
            verify_ledger(data),
            {
                "ambient_dimension": "4",
                "global_volume_exponent": "3/4",
                "global_dimension_bound": "13/4",
                "bottleneck_branches": "trilinear",
            },
        )

    def test_rejects_wrong_dimension_conversion(self) -> None:
        data = {
            "ambient_dimension": 4,
            "branches": [
                {
                    "name": "bad",
                    "volume_exponent": "3/4",
                    "dimension_bound": "10/3",
                }
            ],
            "claimed_global": {
                "volume_exponent": "3/4",
                "dimension_bound": "10/3",
            },
        }
        with self.assertRaisesRegex(ValueError, "n-volume_exponent"):
            verify_ledger(data)

    def test_rejects_wrong_branch_aggregation(self) -> None:
        data = {
            "ambient_dimension": 4,
            "branches": [
                {
                    "name": "a",
                    "volume_exponent": "3/4",
                    "dimension_bound": "13/4",
                },
                {
                    "name": "b",
                    "volume_exponent": "2/3",
                    "dimension_bound": "10/3",
                },
            ],
            "claimed_global": {
                "volume_exponent": "2/3",
                "dimension_bound": "10/3",
            },
        }
        with self.assertRaisesRegex(ValueError, "branch maximum"):
            verify_ledger(data)


if __name__ == "__main__":
    unittest.main()

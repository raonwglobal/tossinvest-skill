import sys
import unittest
from pathlib import Path

# Load the sibling src directory without relying on importable package names.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from strategy_rules import (
    needs_rebalance, portfolio_weights, target_amount, target_drift,
    validate_target_weights,
)


class StrategyRulesTests(unittest.TestCase):
    def test_weights(self):
        self.assertAlmostEqual(portfolio_weights({"A": 30, "B": 70})["A"], 0.3)

    def test_drift(self):
        self.assertAlmostEqual(target_drift(0.6, 0.5), 0.1)

    def test_rebalance_threshold(self):
        self.assertTrue(needs_rebalance(0.56, 0.5, 0.05))
        self.assertFalse(needs_rebalance(0.53, 0.5, 0.05))

    def test_target_amount(self):
        self.assertEqual(target_amount(100000, 0.25), 25000)

    def test_validate_targets(self):
        self.assertTrue(validate_target_weights([0.4, 0.3]))
        self.assertFalse(validate_target_weights([0.7, 0.4]))


if __name__ == "__main__":
    unittest.main()

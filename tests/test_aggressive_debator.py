import unittest
from tradingagents.agents.risk_mgmt.aggressive_debator import (
    evaluate_portfolio_diversification,
    evaluate_sharpe_ratio,
    evaluate_position_sizing,
)

class TestAggressiveDebator(unittest.TestCase):
    def test_portfolio_diversification(self):
        result = evaluate_portfolio_diversification(["StockA", "StockB"], 0.3)
        self.assertEqual(result, "Diversify")

    def test_sharpe_ratio(self):
        returns = [0.01, 0.02, -0.005, 0.015]
        result = evaluate_sharpe_ratio(returns)
        self.assertGreater(result, -10)  # basic sanity check

    def test_position_sizing(self):
        result = evaluate_position_sizing(100000)
        self.assertEqual(result, 2000.0)

if __name__ == '__main__':
    unittest.main()

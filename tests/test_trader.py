import unittest
from tradingagents.agents.trader.trader import (
    execute_momentum_trading,
    execute_mean_reversion,
    execute_trend_following,
)

class TestTrader(unittest.TestCase):
    def test_momentum_trading(self):
        historical_prices = [100, 102, 105, 107, 110]
        result = execute_momentum_trading(historical_prices)
        self.assertEqual(result, "Buy")

    def test_mean_reversion_buy(self):
        prices = [110, 108, 105, 102, 98]
        result = execute_mean_reversion(prices)
        self.assertEqual(result, "Buy")

    def test_trend_following_buy(self):
        prices = [95, 96, 97]
        result = execute_trend_following(prices)
        self.assertEqual(result, "Buy")

if __name__ == '__main__':
    unittest.main()

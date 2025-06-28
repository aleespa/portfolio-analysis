import unittest
from datetime import timedelta

from portfolio_analysis.common import get_latest_working_day
from portfolio_analysis.data import get_latest_data, get_daily_time_series


class TestData(unittest.TestCase):
    def test_get_latest_data(self):
        d = get_latest_data("USDMXN=X")
        print(d)
    def test_get_daily_time_series(self):
        d = get_latest_working_day()
        start = d - timedelta(10)
        end = d
        data = get_daily_time_series(
            tickers=["USDMXN=X", "GBPMXN=X"],
            start=start,
            end=end,
        )
        print(data.loc[:, 'Close'])

if __name__ == '__main__':
    unittest.main()

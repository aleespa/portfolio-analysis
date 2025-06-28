import unittest
from datetime import timedelta

from portfolio_analysis.common import get_latest_working_day
from portfolio_analysis.data import get_daily_time_series
from portfolio_analysis.figures import plot_timeseries


class TestFigures(unittest.TestCase):
    def test_time_series_plot(self):
        d = get_latest_working_day()
        start = d - timedelta(250)
        end = d
        data = get_daily_time_series(
            tickers=["TSLA"],
            start=start,
            end=end,
        )
        plot_timeseries(data.loc[:, ('Close', "TSLA")], "TSLA")


if __name__ == '__main__':
    unittest.main()

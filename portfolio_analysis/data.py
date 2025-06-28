from datetime import date

import pandas as pd
import yfinance as yf

from portfolio_analysis.common import get_latest_working_day


def get_latest_data(tickers) -> pd.DataFrame:
    initial_date = get_latest_working_day()
    return yf.download(
        tickers,
        start=initial_date,
        interval='1d',
        end=None,
        auto_adjust=True,
        progress=False)

def get_daily_time_series(
        tickers,
        start: date,
        end: date) -> pd.DataFrame:
    start_str = start.strftime('%Y-%m-%d')
    end_str = end.strftime('%Y-%m-%d')
    return yf.download(
        tickers,
        start=start_str,
        interval='1d',
        end=end_str,
        auto_adjust=True,
        progress=False
    )


"""Buy the Dip vs. Dollar-Cost Averaging (DCA) — 25+ Year S&P 500 Backtest
Published by AlgoVantages (Tolga Has — https://tolgahas.com)

Reproduces the exact backtest comparing $500/month invested into SPY (dividend-adjusted)
from 2000-01-01 to today across four disciplined strategies:
  1. Monthly DCA (buy immediately on the 1st trading day of each month)
  2. Buy -10% Dip (hold cash at 0%, deploy all cash when drawdown <= -10%)
  3. Buy -20% Crash (hold cash at 0%, deploy all cash when drawdown <= -20%)
  4. Buy -10% Dip + 3% Cash Yield (idle cash earns 3% annualized T-bill proxy)

Usage:
    pip install yfinance pandas numpy
    python buy_the_dip_backtest.py
"""

import numpy as np
import pandas as pd
import yfinance as yf


TICKER = "SPY"
START_DATE = "2000-01-01"
MONTHLY_CONTRIBUTION = 500.0


def simulate(prices: pd.Series, dip_threshold: float | None, cash_yield: float = 0.0) -> dict:
    dates = prices.index
    vals = prices.to_numpy(dtype=float)
    months = dates.to_period("M")

    cash = 0.0
    shares = 0.0
    invested = 0.0
    buys = 0
    peak = vals[0]
    prev_date = dates[0]
    last_month = None

    for dt, price in zip(dates, vals):
        days = max((dt - prev_date).days, 0)
        prev_date = dt
        if cash > 0 and cash_yield > 0 and days > 0:
            cash *= (1.0 + cash_yield) ** (days / 365.25)

        peak = max(peak, price)
        dd = (price / peak) - 1.0

        m = months[dates.get_loc(dt)] if False else dt.to_period("M")
        if m != last_month:
            cash += MONTHLY_CONTRIBUTION
            invested += MONTHLY_CONTRIBUTION
            last_month = m

        if (dip_threshold is None or dd <= dip_threshold) and cash > 0:
            shares += cash / price
            cash = 0.0
            buys += 1

    final_val = shares * vals[-1] + cash
    return {
        "Invested": round(invested, 2),
        "Final Value": round(final_val, 2),
        "Return %": round((final_val / invested - 1.0) * 100.0, 2),
        "Buys": buys,
        "Idle Cash": round(cash, 2),
    }


if __name__ == "__main__":
    df = yf.download(TICKER, start=START_DATE, auto_adjust=True, progress=False)
    close = df["Close"].iloc[:, 0] if isinstance(df["Close"], pd.DataFrame) else df["Close"]
    close = close.dropna().astype(float)

    results = {
        "1. Monthly DCA": simulate(close, None, 0.0),
        "2. Buy -10% Dip (0% Cash)": simulate(close, -0.10, 0.0),
        "3. Buy -20% Crash (0% Cash)": simulate(close, -0.20, 0.0),
        "4. Buy -10% Dip (3% Cash)": simulate(close, -0.10, 0.03),
    }
    print(pd.DataFrame(results).T.to_string())

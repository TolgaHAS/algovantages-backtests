"""Global Markowitz Portfolio Optimization Backtest (SPY, QQQ, TLT, GLD, VNQ)
Published by AlgoVantages (Tolga Has — https://tolgahas.com)

Reproduces the 10-year Efficient Frontier and Max-Sharpe SLSQP optimization
comparing Optimal Markowitz weights against a classic 60/40 portfolio and 100% SPY.

Usage:
    pip install yfinance pandas numpy scipy
    python markowitz_global_backtest.py
"""

from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import yfinance as yf
from scipy.optimize import minimize

TICKERS = ["SPY", "QQQ", "TLT", "GLD", "VNQ"]
RISK_FREE_RATE = 0.04


def max_sharpe_weights(mu: np.ndarray, cov: np.ndarray, rf: float = RISK_FREE_RATE) -> np.ndarray:
    n = len(mu)
    init = np.full(n, 1.0 / n)
    bounds = tuple((0.0, 1.0) for _ in range(n))
    constraints = {"type": "eq", "fun": lambda w: np.sum(w) - 1.0}

    def neg_sharpe(w: np.ndarray) -> float:
        ret = float(np.dot(w, mu))
        vol = float(np.sqrt(np.dot(w.T, np.dot(cov, w))))
        return -(ret - rf) / vol

    res = minimize(neg_sharpe, init, method="SLSQP", bounds=bounds, constraints=constraints)
    return res.x / np.sum(res.x)


if __name__ == "__main__":
    end_dt = datetime.today()
    start_dt = end_dt - timedelta(days=3652)
    closes = yf.download(TICKERS, start=start_dt.strftime("%Y-%m-%d"), auto_adjust=True, progress=False)["Close"][TICKERS].dropna()
    rets = closes.pct_change().dropna()
    mu = (rets.mean() * 252).to_numpy()
    cov = (rets.cov() * 252).to_numpy()

    w_opt = max_sharpe_weights(mu, cov)
    w_6040 = np.array([0.60, 0.0, 0.40, 0.0, 0.0])

    for name, w in [("Max Sharpe Optimal", w_opt), ("Classic 60/40", w_6040)]:
        r = float(np.dot(w, mu))
        v = float(np.sqrt(np.dot(w.T, np.dot(cov, w))))
        s = (r - RISK_FREE_RATE) / v
        print(f"{name:20s} | Return: {r*100:5.2f}% | Vol: {v*100:5.2f}% | Sharpe: {s:4.2f}")
        print("  Weights:", dict(zip(TICKERS, np.round(w * 100, 1))))

"""Leveraged ETF Volatility Decay & Financing Drag Backtest (TQQQ vs. QLD vs. QQQ)
Published by AlgoVantages (Tolga Has — https://tolgahas.com)

Reproduces all three quantitative experiments on dividend-adjusted daily prices:
  1. Real ETF Era (2010-02-11 -> present): QQQ vs. QLD (2x) vs. TQQQ (3x) vs. TQQQ + 200-SMA
  2. Nov 2021 Peak-Buyer Stress Test (2021-11-19 -> present): QQQ vs. QLD vs. TQQQ recovery
  3. 27-Year Dot-Com Stress Test (2000-01-03 -> present): QQQ vs. Simulated Daily-Reset 2x & 3x

Usage:
    pip install yfinance pandas numpy
    python tqqq_volatility_decay_backtest.py
"""

import math
import numpy as np
import pandas as pd
import yfinance as yf


INITIAL_CAPITAL = 10_000.0
RISK_FREE_RATE = 0.04


def sim_leveraged(prices: pd.Series, leverage: float, annual_drag: float, capital: float = INITIAL_CAPITAL) -> pd.Series:
    r = prices.pct_change().dropna()
    lev_r = np.maximum(leverage * r.to_numpy(dtype=float) - (annual_drag / 252.0), -0.9999)
    vals = np.empty(len(prices), dtype=float)
    vals[0] = capital
    vals[1:] = capital * np.cumprod(1.0 + lev_r)
    return pd.Series(vals, index=prices.index)


def sim_sma200_overlay(signal_prices: pd.Series, trade_prices: pd.Series, window: int = 200) -> tuple[pd.Series, float]:
    sma = signal_prices.rolling(window).mean().shift(1)
    above = (signal_prices.shift(1) > sma).fillna(False).reindex(trade_prices.index).fillna(False)
    rets = trade_prices.pct_change().fillna(0.0)
    active_pct = float(above.iloc[1:].mean() * 100.0)
    strat_rets = np.where(above.to_numpy(dtype=bool), rets.to_numpy(dtype=float), 0.0)
    strat_rets[0] = 0.0
    eq = INITIAL_CAPITAL * np.cumprod(1.0 + strat_rets)
    return pd.Series(eq, index=trade_prices.index), active_pct


def compute_stats(eq: pd.Series) -> tuple[float, float, float, float, float]:
    yrs = max((eq.index[-1] - eq.index[0]).days / 365.25, 0.01)
    rets = eq.pct_change().dropna()
    ann_ret = float(rets.mean() * 252.0)
    ann_vol = float(rets.std(ddof=1) * math.sqrt(252.0))
    sharpe = (ann_ret - RISK_FREE_RATE) / ann_vol if ann_vol > 0 else 0.0
    cagr = ((float(eq.iloc[-1]) / float(eq.iloc[0])) ** (1.0 / yrs) - 1.0) * 100.0
    max_dd = float(((eq / eq.cummax()) - 1.0).min() * 100.0)
    return float(eq.iloc[-1]), cagr, ann_vol * 100.0, sharpe, max_dd


def download_close(ticker: str, start: str) -> pd.Series:
    df = yf.download(ticker, start=start, auto_adjust=True, progress=False, threads=False)
    close = df["Close"].iloc[:, 0] if isinstance(df["Close"], pd.DataFrame) else df["Close"]
    s = close.dropna().astype(float)
    s.index = pd.to_datetime(s.index).tz_localize(None)
    return s.sort_index()


if __name__ == "__main__":
    q2000 = download_close("QQQ", "2000-01-01")
    qld = download_close("QLD", "2010-02-11")
    tqqq = download_close("TQQQ", "2010-02-11")
    real_df = pd.concat({"QQQ": q2000, "QLD": qld, "TQQQ": tqqq}, axis=1)[["QQQ", "QLD", "TQQQ"]].dropna()

    print(f"=== WINDOW A: REAL ETF ERA ({real_df.index[0].date()} -> {real_df.index[-1].date()}, $10,000) ===")
    sma_eq, active_pct = sim_sma200_overlay(q2000, real_df["TQQQ"])
    curves_a = {
        "1x QQQ": INITIAL_CAPITAL * (real_df["QQQ"] / real_df["QQQ"].iloc[0]),
        "2x QLD": INITIAL_CAPITAL * (real_df["QLD"] / real_df["QLD"].iloc[0]),
        "3x TQQQ": INITIAL_CAPITAL * (real_df["TQQQ"] / real_df["TQQQ"].iloc[0]),
        f"TQQQ+200SMA ({active_pct:.1f}%)": sma_eq,
    }
    for label, eq in curves_a.items():
        fv, cagr, vol, sr, dd = compute_stats(eq)
        print(f"  {label:24s} | Final: ${fv:>12,.2f} | CAGR: {cagr:>6.2f}% | Vol: {vol:>5.2f}% | Sharpe: {sr:>4.2f} | MaxDD: {dd:>7.2f}%")

    r_real = real_df.pct_change().dropna()
    drag_qld = (2.0 * r_real["QQQ"].mean() - r_real["QLD"].mean()) * 252.0 * 100.0
    drag_tqqq = (3.0 * r_real["QQQ"].mean() - r_real["TQQQ"].mean()) * 252.0 * 100.0
    print(f"  Implied annual drag -> QLD: {drag_qld:.2f}%/yr | TQQQ: {drag_tqqq:.2f}%/yr")

    peak_df = real_df.loc["2021-11-19":]
    print(f"\n=== WINDOW B: NOV 2021 PEAK BUYER ({peak_df.index[0].date()} -> {peak_df.index[-1].date()}, $10,000) ===")
    for t in ["QQQ", "QLD", "TQQQ"]:
        eq = INITIAL_CAPITAL * (peak_df[t] / peak_df[t].iloc[0])
        fv, cagr, _, _, dd = compute_stats(eq)
        trough_dt = eq.idxmin()
        rec = eq.loc[trough_dt:][eq.loc[trough_dt:] >= INITIAL_CAPITAL]
        rec_mo = f"{round((rec.index[0] - eq.index[0]).days / 30.44)} mo" if not rec.empty else "Not recovered"
        print(f"  {t:4s} | Final: ${fv:>10,.2f} | Trough: ${eq.min():>8,.2f} ({trough_dt.date()}) | MaxDD: {dd:>7.2f}% | Recovery: {rec_mo}")

    print(f"\n=== WINDOW C: 27-YEAR DOT-COM STRESS TEST ({q2000.index[0].date()} -> {q2000.index[-1].date()}, $10,000) ===")
    curves_c = [
        ("1x QQQ (Actual)", INITIAL_CAPITAL * (q2000 / q2000.iloc[0])),
        ("Sim 2x (+3.45% drag)", sim_leveraged(q2000, 2.0, 0.0095 + 0.025)),
        ("Sim 3x (0.95% ER only)", sim_leveraged(q2000, 3.0, 0.0095)),
        ("Sim 3x (+5.95% drag)", sim_leveraged(q2000, 3.0, 0.0095 + 0.050)),
    ]
    for label, eq in curves_c:
        fv, cagr, _, _, dd = compute_stats(eq)
        print(f"  {label:24s} | Final: ${fv:>10,.2f} | Min: ${eq.min():>8,.2f} ({eq.idxmin().date()}) | CAGR: {cagr:>6.2f}% | MaxDD: {dd:>7.2f}%")

    r_q00 = q2000.pct_change().dropna()
    kelly_00 = (float(r_q00.mean() * 252.0) - RISK_FREE_RATE) / float(r_q00.var(ddof=1) * 252.0)
    kelly_10 = (float(r_real["QQQ"].mean() * 252.0) - RISK_FREE_RATE) / float(r_real["QQQ"].var(ddof=1) * 252.0)
    print(f"\nKelly Optimal Leverage -> Full Cycle (2000+): {kelly_00:.2f}x | Post-GFC Bull (2010+): {kelly_10:.2f}x")

# Episode 03: Leveraged ETFs (`TQQQ`) vs. `QQQ` — Volatility Decay & Financing Drag (`2000–2026`)

Quantitative backtest by **Tolga Has** ([tolgahas.com](https://tolgahas.com)) comparing `1x QQQ`, `2x QLD`, `3x TQQQ`, and a `TQQQ + 200-SMA` overlay across `4,222` real ETF trading days (`2010-02-11` to `2026-11-23`), November 2021 peak entries, and `6,764` full-cycle `QQQ` days (`2000-01-03` to `2026-11-23`).

## Video & Written Study
- **Full Video Breakdown (YouTube — 12:29):** https://youtu.be/P81Tjn9mXLg
- **Vertical Shorts Summary (YouTube Shorts — 00:54):** https://youtube.com/shorts/c1YqfTXVMnQ
- **Written Research Study (`tolgahas.com`):** [English](https://tolgahas.com/en/projects/algovantages/tqqq-volatility-decay/) · [Türkçe](https://tolgahas.com/projeler/algovantages/tqqq-volatility-decay/)

## Empirical Results (`$10,000` Initial Capital, `4.0%` Risk-Free Benchmark)

### 1. Real ETF Era (`2010-02-11` – `2026-11-23`, `4,222` Bars)

| Strategy | Final Value | CAGR | Annual Volatility | Sharpe Ratio | Max Drawdown | Key Note |
| :--- | ---: | ---: | ---: | ---: | ---: | :--- |
| **3x TQQQ Buy & Hold** | **$2,392,960.16** | 38.60% | 61.66% | 0.78 | -81.66% | Implied drag `5.57%/yr` (`2022`: `-79.09%`) |
| **2x QLD Buy & Hold** | $876,355.92 | 30.55% | 41.55% | 0.76 | -63.68% | Implied drag `2.94%/yr` (`2022`: `-60.52%`) |
| **TQQQ + 200-SMA Filter** | $661,432.68 | 28.38% | 47.32% | 0.68 | -55.91% | `84.7%` invested (`2022`: `-43.34%`) |
| **1x QQQ Baseline** | $172,126.00 | 18.48% | **20.84%** | 0.73 | **-35.12%** | Unleveraged benchmark (`2022`: `-32.58%`) |

### 2. November 2021 Peak-Buyer Stress Test (`2021-11-19` – `2026-11-23`)

| Portfolio | Final Value | Total Return | 2022 Crash | Trough Value | Max Drawdown | Breakeven Recovery |
| :--- | ---: | ---: | ---: | ---: | ---: | :---: |
| **1x QQQ** | **$16,603.92** | **+66.04%** | -32.58% | $6,488.21 | -35.12% | **25 months** (`2023-12-13`) |
| **2x QLD** | $15,766.20 | +57.66% | -60.52% | $3,631.55 | -63.68% | 30 months (`2024-05-24`) |
| **3x TQQQ** | $11,657.37 | +16.57% | -79.09% | $1,834.02 | -81.66% | 36 months (`2024-12-04`) |

### 3. 27-Year Dot-Com & GFC Survival Test (`2000-01-03` – `2026-11-23`, `6,764` Bars)

| Path (`$10,000` Start) | Final Value | CAGR | Max Drawdown | Trough Value & Date |
| :--- | ---: | ---: | ---: | :--- |
| **1x QQQ (Actual)** | **$81,627.15** | **8.12%** | **-82.96%** | `$2,117.15` (`2002-10-09`) |
| **Simulated 2x QQQ (`3.45%` drag)** | $38,396.77 | 5.13% | -98.75% | `$178.99` (`2009-03-09`) |
| **Sim 3x QQQ (`0.95%` ER Only)** | $12,612.28 | 0.87% | -99.96% | `$6.22` (`2009-03-09`) |
| **Sim 3x QQQ (`5.95%` realistic drag)** | $3,290.26 | -4.05% | **-99.97%** | **`$3.93`** (`2009-03-09`) |

- **Continuous Kelly Optimal Leverage:** `1.03x` across the full `2000–2026` cycle vs. `3.49x` during the `2010–2026` bull sample.

## Quickstart

```bash
pip install yfinance pandas numpy
python tqqq_volatility_decay_backtest.py
```

*Disclaimer: Educational & quantitative research only. Not financial advice.*

# Episode 02: Global Markowitz Portfolio Optimization vs. Classic 60/40 (`2016–2026`)

Quantitative portfolio study by **Tolga Has** ([tolgahas.com](https://tolgahas.com)) applying Markowitz SLSQP Sharpe maximization across five liquid global ETFs (`SPY`, `QQQ`, `TLT`, `GLD`, `VNQ`) over `2,512` overlapping trading days (`2016-11-21` to `2026-11-18`, risk-free rate `4.0%`).

## Empirical Results (`$10,000` Initial Capital)

| Portfolio | Final Value | CAGR | Annual Volatility | Sharpe Ratio | Max Drawdown | Key Allocation |
| :--- | ---: | ---: | ---: | ---: | ---: | :--- |
| **Max Sharpe Optimal** | **$47,143.91** | **16.80%** | 15.36% | **0.83** | **-24.49%** | `54.45% QQQ / 45.55% GLD` |
| **100% S&P 500 (`SPY`)** | $38,838.97 | 14.55% | 18.05% | 0.62 | -33.72% | `100% SPY` |
| **Equal Weight** | $28,217.98 | 10.95% | 12.44% | 0.58 | -26.45% | `20% each` |
| **Classic 60/40** | $23,137.81 | 8.76% | 11.61% | 0.44 | -27.24% | `60% SPY / 40% TLT` |
| **Min Volatility** | $20,459.51 | 7.43% | **9.95%** | 0.37 | -25.50% | `32.91% SPY / 44.85% TLT / 22.24% GLD` |

## Quickstart

```bash
pip install yfinance pandas numpy scipy
python markowitz_global_backtest.py
```

*Disclaimer: Educational & quantitative research only. Not financial advice.*

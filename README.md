# AlgoVantages — Open-Source Quantitative Finance Backtests

> *"In a world full of financial noise, we are your signal."*

Official reproducible Python backtests powering the **[AlgoVantages YouTube Channel](https://www.youtube.com/@AlgoVantages)** and quantitative research published by **Tolga Has** ([tolgahas.com](https://tolgahas.com)).

---

## Episodes & Studies

| Episode | Topic | Universe & Window | Key Empirical Finding | Video & Study | Code |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **01** | **Buy the Dip vs. Monthly DCA** | `SPY` (`2000-01-03` – `2026-11-18`, `6,761` bars) | Monthly DCA (`$937,869.94`, `11.26%` XIRR) beat `-10%` Dip (`-$18,704.47`), `-20%` Crash (`-$37,112.07`), and `-10%` Dip + 3% Cash (`-$8,764.52`). | [Full Video](https://youtu.be/tNB4yXVWi1c) · [Shorts](https://youtube.com/shorts/2ENhf9OmnHE) · [Study (EN)](https://tolgahas.com/en/projects/algovantages/buy-the-dip-vs-dca/) · [Study (TR)](https://tolgahas.com/projeler/algovantages/buy-the-dip-vs-dca/) | [`ep01_buy_the_dip/`](./ep01_buy_the_dip) |
| **02** | **Global Markowitz Optimization vs. 60/40** | `SPY, QQQ, TLT, GLD, VNQ` (`2016-11-21` – `2026-11-18`, `2,512` bars) | Max Sharpe Optimal (`54.45% QQQ / 45.55% GLD`) turned `$10,000` into **`$47,143.91`** (`0.83` Sharpe) vs. Classic 60/40 at `$23,137.81` (`0.44` Sharpe). | [Full Video](https://youtu.be/yJAKpqx0kvg) · [Shorts](https://youtube.com/shorts/TQK7paMDOSw) · [Study (EN)](https://tolgahas.com/en/projects/algovantages/markowitz-portfolio-optimization/) · [Study (TR)](https://tolgahas.com/projeler/algovantages/markowitz-portfolio-optimization/) | [`ep02_markowitz_portfolio/`](./ep02_markowitz_portfolio) |
| **03** | **Leveraged ETFs (`TQQQ`) vs. `QQQ` Volatility Decay** | `QQQ, QLD, TQQQ` (`2000-01-03` – `2026-11-23`, `6,764` bars) | `3x TQQQ` hit `$2,392,960.16` post-2010 (`5.57%/yr` drag), trailed `1x QQQ` (`$16,603.92` vs. `$11,657.37`) from Nov 2021 peak, and crashed **`-99.97%`** (`$3.93` trough) across Dot-Com + GFC (`1.03x` full-cycle Kelly). | [Full Video](https://youtu.be/P81Tjn9mXLg) · [Shorts](https://youtube.com/shorts/c1YqfTXVMnQ) · [Study (EN)](https://tolgahas.com/en/projects/algovantages/tqqq-volatility-decay/) · [Study (TR)](https://tolgahas.com/projeler/algovantages/tqqq-volatility-decay/) | [`ep03_tqqq_volatility_decay/`](./ep03_tqqq_volatility_decay) |

---

## Quickstart

```bash
git clone https://github.com/TolgaHAS/algovantages-backtests.git
cd algovantages-backtests
pip install -r requirements.txt

# Run Episode 01
python ep01_buy_the_dip/buy_the_dip_backtest.py

# Run Episode 02
python ep02_markowitz_portfolio/markowitz_global_backtest.py

# Run Episode 03
python ep03_tqqq_volatility_decay/tqqq_volatility_decay_backtest.py
```

---

## Author & Links
- **Author:** Tolga Has (10+ Years Banking, Quantitative Finance & Python)
- **Website & Written Research Briefs:** [tolgahas.com](https://tolgahas.com) · [AlgoVantages Research Hub](https://tolgahas.com/en/projects/algovantages/)
- **YouTube Channel:** [@AlgoVantages](https://www.youtube.com/@AlgoVantages)

---

## Disclaimer
**Educational & Quantitative Research Only. Not Financial Advice.**  
All scripts and historical backtest results in this repository are provided strictly for educational and reproducible research purposes. Historical performance does not guarantee future results.

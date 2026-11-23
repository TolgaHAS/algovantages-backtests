# AlgoVantages Episode 01: Buy the Dip vs. Dollar-Cost Averaging (2000–2026)

Quantitative backtest by **Tolga Has** ([tolgahas.com](https://tolgahas.com)) comparing disciplined Monthly DCA against waiting for `-10%` and `-20%` market drawdowns on `SPY` (`2000-01-03` to `2026-11-18`).

## Video & Written Study
- **Full Video Breakdown (YouTube):** https://youtu.be/tNB4yXVWi1c
- **Vertical Shorts Summary (YouTube Shorts):** https://youtube.com/shorts/2ENhf9OmnHE
- **Written Research Study (`tolgahas.com`):** [English](https://tolgahas.com/en/projects/algovantages/buy-the-dip-vs-dca/) · [Türkçe](https://tolgahas.com/projeler/algovantages/buy-the-dip-vs-dca/)
- **Medium Articles:** [English](https://medium.com/@tolgahas583/i-backtested-buy-the-dip-vs-monthly-dca-over-27-years-of-real-s-p-500-data-5c43a3cde2c4) · [Türkçe](https://medium.com/@tolgahas583/d%C3%BC%C5%9F%C3%BC%C5%9Fte-al-buy-the-dip-stratejisi-ger%C3%A7ekten-kazand%C4%B1r%C4%B1yor-mu-27-y%C4%B1ll%C4%B1k-s-p-500-python-backtesti-bd938e484f31)

## Results Summary (`$500/month`, Total Invested `$161,500.00`)

| Strategy | Final Value | Annualized XIRR | Buys | Days Holding Cash | Gap vs. DCA |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Monthly DCA | $937,869.94 | 11.26% | 323 | 0.0% | $0.00 |
| Buy -10% Dip (+3% Cash) | $929,105.42 | 11.2% | 148 | 57.9% | -$8,764.52 |
| Buy -10% Dip (0% Cash) | $919,165.46 | 11.14% | 148 | 57.9% | -$18,704.47 |
| Buy -20% Crash (0% Cash) | $900,757.87 | 11.02% | 81 | 76.3% | -$37,112.07 |

## Quickstart

```bash
pip install yfinance pandas numpy
python buy_the_dip_backtest.py
```

*Disclaimer: Educational quantitative research only, not financial advice.*

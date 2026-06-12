---
{
  "title": "Sweep \u2014 AAPL Backtest Results (5-Year)",
  "date": "2026-06-13",
  "draft": false,
  "type": "backtests",
  "period": "2021-06-14 \u2192 2026-06-12",
  "metrics": [
    {
      "label": "Total Return",
      "value": "+51.5%"
    },
    {
      "label": "CAGR",
      "value": "8.7%"
    },
    {
      "label": "Sharpe Ratio",
      "value": "0.48"
    },
    {
      "label": "Max Drawdown",
      "value": "23.2%"
    },
    {
      "label": "Win Rate",
      "value": "38.7%"
    },
    {
      "label": "Profit Factor",
      "value": "1.42"
    },
    {
      "label": "Total Trades",
      "value": "93"
    },
    {
      "label": "Avg Trade",
      "value": "11 days"
    }
  ],
  "yearly": [
    {
      "year": "2021",
      "return_pct": "+36.5%",
      "trades": "14",
      "win_rate_pct": "38.7%"
    },
    {
      "year": "2022",
      "return_pct": "-28.2%",
      "trades": "17",
      "win_rate_pct": "38.7%"
    },
    {
      "year": "2023",
      "return_pct": "+54.8%",
      "trades": "18",
      "win_rate_pct": "38.7%"
    },
    {
      "year": "2024",
      "return_pct": "+35.6%",
      "trades": "20",
      "win_rate_pct": "38.7%"
    },
    {
      "year": "2025",
      "return_pct": "+12.0%",
      "trades": "19",
      "win_rate_pct": "38.7%"
    },
    {
      "year": "2026",
      "return_pct": "+7.2%",
      "trades": "5",
      "win_rate_pct": "38.7%"
    }
  ],
  "cta_headline": "Trade Stocks on Moomoo \u2014 Commission-Free",
  "cta_body": "Access US markets with zero commissions and professional-grade charting tools.",
  "cta_label": "Open Moomoo Account",
  "cta_url": "https://j.moomoo.com/0BpZwx",
  "equity_curve_url": "/backtests/liquidity-sweep-pro-aapl-equity.png",
  "crosslinks": [
    {
      "title": "nadaraya_watson_regression_liquidity_sweeps_algoalpha review: settings, strategy &amp; how to use it",
      "url": "/reviews/nadaraya-watson-regression-liquidity-sweeps-algoalpha/"
    },
    {
      "title": "liquidity_sweep_pro review: settings, strategy &amp; how to use it",
      "url": "/reviews/liquidity-sweep-pro/"
    },
    {
      "title": "liquidity_sweep_profiler_flux_charts review: settings, strategy &amp; how to use it",
      "url": "/reviews/liquidity-sweep-profiler-flux-charts/"
    }
  ]
}
---

![Liquidity Sweep Pro — AAPL Equity Curve](/backtests/liquidity-sweep-pro-aapl-equity.png)

## How the Liquidity Sweep Pro Works

The liquidity sweep pro is one of the most widely-used signals in trading. It's simple, mechanical, and removes emotional decision-making from your trading by generating clear entry and exit signals based on the Sweep indicator.

On AAPL, the Sweep acts as a trend filter. It won't catch every exact bottom, but it reliably captures the meat of major moves while keeping you out of chop.

## 5-Year Performance on AAPL

Over five years (2021-06-14 → 2026-06-12), the Liquidity Sweep Pro delivered a **+51.5% total return** on AAPL, compounding at **8.7% annually**. 

At **0.48**, the Sweep earned less than one units of return for every unit of risk taken. For context, anything above 1.0 is considered good; above 1.5 is excellent.

The catch? A **23.2% max drawdown**. At some point during this 5-year run, you'd have been down nearly 23% from peak equity. That's significant territory for most traders. If you can't handle that kind of drawdown, this isn't for you — or you need to size down.

## Risk Assessment

| Metric | Value | Verdict |
|--------|-------|---------|
| Sharpe Ratio | 0.48 | ❌ Weak |
| Max Drawdown | 23.2% | ⚠️ Moderate |
| Win Rate | 38.7% | ❌ Low — relies on outsized wins |
| Profit Factor | 1.42 | ⚠️ Marginal |
| Trades/Year | ~93 total | Active |

The **profit factor of 1.42** tells the real story: when the Sweep fires, the winning signals are larger than the losing ones. Combined with a 38.7% win rate, this requires careful position sizing to be profitable.

## Does the Liquidity Sweep Pro Work on AAPL?

The liquidity sweep pro shows moderate edge on AAPL — **0.48 Sharpe, 1.42 profit factor** over 93 trades. It's not a home run, but it's also not random.

The 38.7% win rate means you'll be wrong more than half the time. The profit factor above 1.0 means your wins are bigger than your losses, which is what keeps you profitable.

Our take: usable as a confirmation tool, but not as a standalone system on AAPL. Combine with trend filters or volume confirmation for better results.



<small>Data source: Yahoo Finance (yfinance). Backtest engine: backtrader. 95% position sizing. 0.1% commission per trade. Last refreshed: June 13, 2026. Not financial advice. Past performance does not guarantee future results.</small>

![Liquidity Sweep Pro — Trade Signals on AAPL](/backtests/liquidity-sweep-pro-aapl-trades.png)

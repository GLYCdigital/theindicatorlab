---
{
  "title": "Sweep \u2014 SPY Backtest Results (5-Year)",
  "date": "2026-06-13",
  "draft": false,
  "type": "backtests",
  "period": "2021-06-14 \u2192 2026-06-12",
  "metrics": [
    {
      "label": "Total Return",
      "value": "+4.9%"
    },
    {
      "label": "CAGR",
      "value": "1.0%"
    },
    {
      "label": "Sharpe Ratio",
      "value": "-0.08"
    },
    {
      "label": "Max Drawdown",
      "value": "23.2%"
    },
    {
      "label": "Win Rate",
      "value": "38.1%"
    },
    {
      "label": "Profit Factor",
      "value": "1.06"
    },
    {
      "label": "Total Trades",
      "value": "105"
    },
    {
      "label": "Avg Trade",
      "value": "11 days"
    }
  ],
  "yearly": [
    {
      "year": "2021",
      "return_pct": "+12.8%",
      "trades": "10",
      "win_rate_pct": "38.1%"
    },
    {
      "year": "2022",
      "return_pct": "-18.6%",
      "trades": "22",
      "win_rate_pct": "38.1%"
    },
    {
      "year": "2023",
      "return_pct": "+26.7%",
      "trades": "20",
      "win_rate_pct": "38.1%"
    },
    {
      "year": "2024",
      "return_pct": "+25.6%",
      "trades": "24",
      "win_rate_pct": "38.1%"
    },
    {
      "year": "2025",
      "return_pct": "+18.0%",
      "trades": "22",
      "win_rate_pct": "38.1%"
    },
    {
      "year": "2026",
      "return_pct": "+8.8%",
      "trades": "7",
      "win_rate_pct": "38.1%"
    }
  ],
  "cta_headline": "Trade Stocks on Moomoo \u2014 Commission-Free",
  "cta_body": "Access US markets with zero commissions and professional-grade charting tools.",
  "cta_label": "Open Moomoo Account",
  "cta_url": "https://j.moomoo.com/0BpZwx",
  "equity_curve_url": "/backtests/liquidity-sweep-pro-spy-equity.png",
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

![Liquidity Sweep Pro — SPY Equity Curve](/backtests/liquidity-sweep-pro-spy-equity.png)

## How the Liquidity Sweep Pro Works

The liquidity sweep pro is one of the most widely-used signals in trading. It's simple, mechanical, and removes emotional decision-making from your trading by generating clear entry and exit signals based on the Sweep indicator.

On SPY, the Sweep acts as a trend filter. It won't catch every exact bottom, but it reliably captures the meat of major moves while keeping you out of chop.

## 5-Year Performance on SPY

Over five years (2021-06-14 → 2026-06-12), the Liquidity Sweep Pro delivered a **+4.9% total return** on SPY, compounding at **1.0% annually**. 

At **-0.08**, the Sweep earned less than one units of return for every unit of risk taken. For context, anything above 1.0 is considered good; above 1.5 is excellent.

The catch? A **23.2% max drawdown**. At some point during this 5-year run, you'd have been down nearly 23% from peak equity. That's significant territory for most traders. If you can't handle that kind of drawdown, this isn't for you — or you need to size down.

## Risk Assessment

| Metric | Value | Verdict |
|--------|-------|---------|
| Sharpe Ratio | -0.08 | ❌ Weak |
| Max Drawdown | 23.2% | ⚠️ Moderate |
| Win Rate | 38.1% | ❌ Low — relies on outsized wins |
| Profit Factor | 1.06 | ⚠️ Marginal |
| Trades/Year | ~105 total | Active |

The **profit factor of 1.06** tells the real story: when the Sweep fires, the winning signals are larger than the losing ones. Combined with a 38.1% win rate, this requires careful position sizing to be profitable.

## Does the Liquidity Sweep Pro Work on SPY?

The liquidity sweep pro struggled to generate meaningful edge on SPY over this 5-year period. With a **-0.08 Sharpe ratio** and **1.06 profit factor**, the risk-adjusted returns are below what most systematic traders would consider acceptable.

This doesn't mean the Sweep is useless — it may work better on different assets, timeframes, or when combined with other filters. But on SPY with default parameters over 5 years, it didn't produce a compelling standalone edge.

Our take: skip it on SPY unless you're combining it with other confirmations or using it on different timeframes.



<small>Data source: Yahoo Finance (yfinance). Backtest engine: backtrader. 95% position sizing. 0.1% commission per trade. Last refreshed: June 13, 2026. Not financial advice. Past performance does not guarantee future results.</small>

![Liquidity Sweep Pro — Trade Signals on SPY](/backtests/liquidity-sweep-pro-spy-trades.png)

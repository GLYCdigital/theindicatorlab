---
{
  "title": "Sweep \u2014 QQQ Backtest Results (5-Year)",
  "date": "2026-07-04",
  "draft": false,
  "type": "backtests",
  "period": "2021-07-06 \u2192 2026-07-02",
  "metrics": [
    {
      "label": "Total Return",
      "value": "+2.7%"
    },
    {
      "label": "CAGR",
      "value": "0.5%"
    },
    {
      "label": "Sharpe Ratio",
      "value": "0.01"
    },
    {
      "label": "Max Drawdown",
      "value": "36.4%"
    },
    {
      "label": "Win Rate",
      "value": "38.5%"
    },
    {
      "label": "Profit Factor",
      "value": "1.05"
    },
    {
      "label": "Total Trades",
      "value": "104"
    },
    {
      "label": "Avg Trade",
      "value": "10 days"
    }
  ],
  "yearly": [
    {
      "year": "2021",
      "return_pct": "+10.7%",
      "trades": "12",
      "win_rate_pct": "38.5%"
    },
    {
      "year": "2022",
      "return_pct": "-33.2%",
      "trades": "21",
      "win_rate_pct": "38.5%"
    },
    {
      "year": "2023",
      "return_pct": "+55.9%",
      "trades": "18",
      "win_rate_pct": "38.5%"
    },
    {
      "year": "2024",
      "return_pct": "+27.7%",
      "trades": "23",
      "win_rate_pct": "38.5%"
    },
    {
      "year": "2025",
      "return_pct": "+21.0%",
      "trades": "19",
      "win_rate_pct": "38.5%"
    },
    {
      "year": "2026",
      "return_pct": "+16.5%",
      "trades": "11",
      "win_rate_pct": "38.5%"
    }
  ],
  "cta_headline": "Trade Stocks on Moomoo \u2014 Commission-Free",
  "cta_body": "Access US markets with zero commissions and professional-grade charting tools.",
  "cta_label": "Open Moomoo Account",
  "cta_url": "https://j.moomoo.com/0BpZwx",
  "equity_curve_url": "/backtests/liquidity-sweep-pro-qqq-equity.png",
  "crosslinks": [
    {
      "title": "liquidity_sweep_retracements review: settings, strategy &amp; how to use it",
      "url": "/reviews/liquidity-sweep-retracements/"
    },
    {
      "title": "nadaraya_watson_regression_liquidity_sweeps_algoalpha review: settings, strategy &amp; how to use it",
      "url": "/reviews/nadaraya-watson-regression-liquidity-sweeps-algoalpha/"
    },
    {
      "title": "liquidity_sweep_pro review: settings, strategy &amp; how to use it",
      "url": "/reviews/liquidity-sweep-pro/"
    }
  ]
}
---

![Liquidity Sweep Pro — QQQ Equity Curve](/backtests/liquidity-sweep-pro-qqq-equity.png)

## How the Liquidity Sweep Pro Works

The liquidity sweep pro is one of the most widely-used signals in trading. It's simple, mechanical, and removes emotional decision-making from your trading by generating clear entry and exit signals based on the Sweep indicator.

On QQQ, the Sweep acts as a trend filter. It won't catch every exact bottom, but it reliably captures the meat of major moves while keeping you out of chop.

## 5-Year Performance on QQQ

Over five years (2021-07-06 → 2026-07-02), the Liquidity Sweep Pro delivered a **+2.7% total return** on QQQ, compounding at **0.5% annually**. 

At **0.01**, the Sweep earned less than one units of return for every unit of risk taken. For context, anything above 1.0 is considered good; above 1.5 is excellent.

The catch? A **36.4% max drawdown**. At some point during this 5-year run, you'd have been down nearly 36% from peak equity. That's stomach-churning territory for most traders. If you can't handle that kind of drawdown, this isn't for you — or you need to size down.

## Risk Assessment

| Metric | Value | Verdict |
|--------|-------|---------|
| Sharpe Ratio | 0.01 | ❌ Weak |
| Max Drawdown | 36.4% | ⚠️ Significant |
| Win Rate | 38.5% | ❌ Low — relies on outsized wins |
| Profit Factor | 1.05 | ⚠️ Marginal |
| Trades/Year | ~104 total | Active |

The **profit factor of 1.05** tells the real story: when the Sweep fires, the winning signals are larger than the losing ones. Combined with a 38.5% win rate, this requires careful position sizing to be profitable.

## Does the Liquidity Sweep Pro Work on QQQ?

The liquidity sweep pro struggled to generate meaningful edge on QQQ over this 5-year period. With a **0.01 Sharpe ratio** and **1.05 profit factor**, the risk-adjusted returns are below what most systematic traders would consider acceptable.

This doesn't mean the Sweep is useless — it may work better on different assets, timeframes, or when combined with other filters. But on QQQ with default parameters over 5 years, it didn't produce a compelling standalone edge.

Our take: skip it on QQQ unless you're combining it with other confirmations or using it on different timeframes.



<small>Data source: Yahoo Finance (yfinance). Backtest engine: backtrader. 95% position sizing. 0.1% commission per trade. Last refreshed: July 04, 2026. Not financial advice. Past performance does not guarantee future results.</small>

![Liquidity Sweep Pro — Trade Signals on QQQ](/backtests/liquidity-sweep-pro-qqq-trades.png)

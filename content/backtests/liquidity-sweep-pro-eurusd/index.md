---
{
  "title": "Sweep \u2014 EURUSD Backtest Results (5-Year)",
  "date": "2026-06-13",
  "draft": false,
  "type": "backtests",
  "period": "2021-06-14 \u2192 2026-06-12",
  "metrics": [
    {
      "label": "Total Return",
      "value": "-24.6%"
    },
    {
      "label": "CAGR",
      "value": "-5.5%"
    },
    {
      "label": "Sharpe Ratio",
      "value": "-2.72"
    },
    {
      "label": "Max Drawdown",
      "value": "24.6%"
    },
    {
      "label": "Win Rate",
      "value": "30.6%"
    },
    {
      "label": "Profit Factor",
      "value": "0.47"
    },
    {
      "label": "Total Trades",
      "value": "108"
    },
    {
      "label": "Avg Trade",
      "value": "8 days"
    }
  ],
  "yearly": [
    {
      "year": "2021",
      "return_pct": "-6.5%",
      "trades": "13",
      "win_rate_pct": "30.6%"
    },
    {
      "year": "2022",
      "return_pct": "-6.3%",
      "trades": "25",
      "win_rate_pct": "30.6%"
    },
    {
      "year": "2023",
      "return_pct": "+3.3%",
      "trades": "22",
      "win_rate_pct": "30.6%"
    },
    {
      "year": "2024",
      "return_pct": "-5.9%",
      "trades": "18",
      "win_rate_pct": "30.6%"
    },
    {
      "year": "2025",
      "return_pct": "+13.5%",
      "trades": "22",
      "win_rate_pct": "30.6%"
    },
    {
      "year": "2026",
      "return_pct": "-1.5%",
      "trades": "8",
      "win_rate_pct": "30.6%"
    }
  ],
  "cta_headline": "Trade Forex with TradingView Pro",
  "cta_body": "Execute directly from charts with integrated broker connections and real-time data.",
  "cta_label": "Get TradingView Pro",
  "cta_url": "https://www.tradingview.com/?aff_id=166324",
  "equity_curve_url": "/backtests/liquidity-sweep-pro-eurusd-equity.png",
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

![Liquidity Sweep Pro — EURUSD=X Equity Curve](/backtests/liquidity-sweep-pro-eurusd-equity.png)

## How the Liquidity Sweep Pro Works

The liquidity sweep pro is one of the most widely-used signals in trading. It's simple, mechanical, and removes emotional decision-making from your trading by generating clear entry and exit signals based on the Sweep indicator.

On EURUSD, the Sweep acts as a trend filter. It won't catch every exact bottom, but it reliably captures the meat of major moves while keeping you out of chop.

## 5-Year Performance on EURUSD

Over five years (2021-06-14 → 2026-06-12), the Liquidity Sweep Pro delivered a **-24.6% total return** on EURUSD=X, compounding at **-5.5% annually**. 

At **-2.72**, the Sweep earned less than one units of return for every unit of risk taken. For context, anything above 1.0 is considered good; above 1.5 is excellent.

The catch? A **24.6% max drawdown**. At some point during this 5-year run, you'd have been down nearly 25% from peak equity. That's significant territory for most traders. If you can't handle that kind of drawdown, this isn't for you — or you need to size down.

## Risk Assessment

| Metric | Value | Verdict |
|--------|-------|---------|
| Sharpe Ratio | -2.72 | ❌ Weak |
| Max Drawdown | 24.6% | ⚠️ Moderate |
| Win Rate | 30.6% | ❌ Low — relies on outsized wins |
| Profit Factor | 0.47 | ❌ Unprofitable |
| Trades/Year | ~108 total | Active |

The **profit factor of 0.47** tells the real story: when the Sweep fires, the winning signals don't outweigh the losers. Combined with a 30.6% win rate, this requires careful position sizing to be profitable.

## Does the Liquidity Sweep Pro Work on EURUSD?

The liquidity sweep pro struggled to generate meaningful edge on EURUSD over this 5-year period. With a **-2.72 Sharpe ratio** and **0.47 profit factor**, the risk-adjusted returns are below what most systematic traders would consider acceptable.

This doesn't mean the Sweep is useless — it may work better on different assets, timeframes, or when combined with other filters. But on EURUSD with default parameters over 5 years, it didn't produce a compelling standalone edge.

Our take: skip it on EURUSD unless you're combining it with other confirmations or using it on different timeframes.



<small>Data source: Yahoo Finance (yfinance). Backtest engine: backtrader. 95% position sizing. 0.1% commission per trade. Last refreshed: June 13, 2026. Not financial advice. Past performance does not guarantee future results.</small>

![Liquidity Sweep Pro — Trade Signals on EURUSD=X](/backtests/liquidity-sweep-pro-eurusd-trades.png)

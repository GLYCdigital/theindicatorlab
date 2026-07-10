---
{
  "title": "Sweep \u2014 ETH Backtest Results (5-Year)",
  "date": "2026-07-11",
  "draft": false,
  "type": "backtests",
  "period": "2021-07-12 \u2192 2026-07-10",
  "metrics": [
    {
      "label": "Total Return",
      "value": "-32.7%"
    },
    {
      "label": "CAGR",
      "value": "-7.6%"
    },
    {
      "label": "Sharpe Ratio",
      "value": "-0.20"
    },
    {
      "label": "Max Drawdown",
      "value": "52.7%"
    },
    {
      "label": "Win Rate",
      "value": "21.0%"
    },
    {
      "label": "Profit Factor",
      "value": "0.89"
    },
    {
      "label": "Total Trades",
      "value": "167"
    },
    {
      "label": "Avg Trade",
      "value": "5 days"
    }
  ],
  "yearly": [
    {
      "year": "2021",
      "return_pct": "+80.8%",
      "trades": "16",
      "win_rate_pct": "21.0%"
    },
    {
      "year": "2022",
      "return_pct": "-68.3%",
      "trades": "28",
      "win_rate_pct": "21.0%"
    },
    {
      "year": "2023",
      "return_pct": "+90.0%",
      "trades": "38",
      "win_rate_pct": "21.0%"
    },
    {
      "year": "2024",
      "return_pct": "+41.7%",
      "trades": "29",
      "win_rate_pct": "21.0%"
    },
    {
      "year": "2025",
      "return_pct": "-11.5%",
      "trades": "40",
      "win_rate_pct": "21.0%"
    },
    {
      "year": "2026",
      "return_pct": "-40.4%",
      "trades": "16",
      "win_rate_pct": "21.0%"
    }
  ],
  "cta_headline": "Trade Crypto on OKX \u2014 0.08% Spot Fees",
  "cta_body": "Execute these signals with institutional-grade liquidity and the lowest fees in crypto.",
  "cta_label": "Start Trading on OKX",
  "cta_url": "https://my.okx.com/join/89285202",
  "equity_curve_url": "/backtests/liquidity-sweep-pro-eth-usd-equity.png",
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

![Liquidity Sweep Pro — ETH-USD Equity Curve](/backtests/liquidity-sweep-pro-eth-usd-equity.png)

## How the Liquidity Sweep Pro Works

The liquidity sweep pro is one of the most widely-used signals in trading. It's simple, mechanical, and removes emotional decision-making from your trading by generating clear entry and exit signals based on the Sweep indicator.

On ETH, the Sweep acts as a trend filter. It won't catch every exact bottom, but it reliably captures the meat of major moves while keeping you out of chop.

## 5-Year Performance on ETH

Over five years (2021-07-12 → 2026-07-10), the Liquidity Sweep Pro delivered a **-32.7% total return** on ETH-USD, compounding at **-7.6% annually**. 

At **-0.20**, the Sweep earned less than one units of return for every unit of risk taken. For context, anything above 1.0 is considered good; above 1.5 is excellent.

The catch? A **52.7% max drawdown**. At some point during this 5-year run, you'd have been down nearly 53% from peak equity. That's stomach-churning territory for most traders. If you can't handle that kind of drawdown, this isn't for you — or you need to size down.

## Risk Assessment

| Metric | Value | Verdict |
|--------|-------|---------|
| Sharpe Ratio | -0.20 | ❌ Weak |
| Max Drawdown | 52.7% | ⚠️ Significant |
| Win Rate | 21.0% | ❌ Low — relies on outsized wins |
| Profit Factor | 0.89 | ❌ Unprofitable |
| Trades/Year | ~167 total | Active |

The **profit factor of 0.89** tells the real story: when the Sweep fires, the winning signals don't outweigh the losers. Combined with a 21.0% win rate, this requires careful position sizing to be profitable.

## Does the Liquidity Sweep Pro Work on ETH?

The liquidity sweep pro struggled to generate meaningful edge on ETH over this 5-year period. With a **-0.20 Sharpe ratio** and **0.89 profit factor**, the risk-adjusted returns are below what most systematic traders would consider acceptable.

This doesn't mean the Sweep is useless — it may work better on different assets, timeframes, or when combined with other filters. But on ETH with default parameters over 5 years, it didn't produce a compelling standalone edge.

Our take: skip it on ETH unless you're combining it with other confirmations or using it on different timeframes.



<small>Data source: Yahoo Finance (yfinance). Backtest engine: backtrader. 95% position sizing. 0.1% commission per trade. Last refreshed: July 11, 2026. Not financial advice. Past performance does not guarantee future results.</small>

![Liquidity Sweep Pro — Trade Signals on ETH-USD](/backtests/liquidity-sweep-pro-eth-usd-trades.png)

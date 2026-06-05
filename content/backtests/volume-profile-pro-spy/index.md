---
{
  "title": "VWAP \u2014 SPY Backtest Results (5-Year)",
  "date": "2026-06-06",
  "draft": false,
  "type": "backtests",
  "period": "2021-06-07 \u2192 2026-06-05",
  "metrics": [
    {
      "label": "Total Return",
      "value": "+8.8%"
    },
    {
      "label": "CAGR",
      "value": "1.7%"
    },
    {
      "label": "Sharpe Ratio",
      "value": "0.01"
    },
    {
      "label": "Max Drawdown",
      "value": "28.1%"
    },
    {
      "label": "Win Rate",
      "value": "35.4%"
    },
    {
      "label": "Profit Factor",
      "value": "0.95"
    },
    {
      "label": "Total Trades",
      "value": "79"
    },
    {
      "label": "Avg Trade",
      "value": "14 days"
    }
  ],
  "yearly": [
    {
      "year": "2021",
      "return_pct": "+13.6%",
      "trades": "10",
      "win_rate_pct": "35.4%"
    },
    {
      "year": "2022",
      "return_pct": "-18.6%",
      "trades": "19",
      "win_rate_pct": "35.4%"
    },
    {
      "year": "2023",
      "return_pct": "+26.7%",
      "trades": "16",
      "win_rate_pct": "35.4%"
    },
    {
      "year": "2024",
      "return_pct": "+25.6%",
      "trades": "13",
      "win_rate_pct": "35.4%"
    },
    {
      "year": "2025",
      "return_pct": "+18.0%",
      "trades": "15",
      "win_rate_pct": "35.4%"
    },
    {
      "year": "2026",
      "return_pct": "+9.3%",
      "trades": "6",
      "win_rate_pct": "35.4%"
    }
  ],
  "cta_headline": "Trade Stocks on Moomoo \u2014 Commission-Free",
  "cta_body": "Access US markets with zero commissions and professional-grade charting tools.",
  "cta_label": "Open Moomoo Account",
  "cta_url": "https://j.moomoo.com/0BpZwx",
  "equity_curve_url": "/backtests/volume-profile-pro-spy-equity.png",
  "crosslinks": [
    {
      "title": "vwap_bands review: settings, strategy &amp; how to use it",
      "url": "/reviews/vwap-bands/"
    },
    {
      "title": "vwap_multi review: settings, strategy &amp; how to use it",
      "url": "/reviews/vwap-multi/"
    },
    {
      "title": "htf volume spike imbalance projection review: settings, strategy &amp; how to use it",
      "url": "/reviews/htf-volume-spike-imbalance-projection/"
    }
  ]
}
---

![Volume Profile Pro — SPY Equity Curve](/backtests/volume-profile-pro-spy-equity.png)

## How the Volume Profile Pro Works

The volume profile pro is one of the most widely-used signals in trading. It's simple, mechanical, and removes emotional decision-making from your trading by generating clear entry and exit signals based on the VWAP indicator.

On SPY, the VWAP acts as a trend filter. It won't catch every exact bottom, but it reliably captures the meat of major moves while keeping you out of chop.

## 5-Year Performance on SPY

Over five years (2021-06-07 → 2026-06-05), the Volume Profile Pro delivered a **+8.8% total return** on SPY, compounding at **1.7% annually**. 

At **0.01**, the VWAP earned less than one units of return for every unit of risk taken. For context, anything above 1.0 is considered good; above 1.5 is excellent.

The catch? A **28.1% max drawdown**. At some point during this 5-year run, you'd have been down nearly 28% from peak equity. That's stomach-churning territory for most traders. If you can't handle that kind of drawdown, this isn't for you — or you need to size down.

## Risk Assessment

| Metric | Value | Verdict |
|--------|-------|---------|
| Sharpe Ratio | 0.01 | ❌ Weak |
| Max Drawdown | 28.1% | ⚠️ Moderate |
| Win Rate | 35.4% | ❌ Low — relies on outsized wins |
| Profit Factor | 0.95 | ❌ Unprofitable |
| Trades/Year | ~79 total | Active |

The **profit factor of 0.95** tells the real story: when the VWAP fires, the winning signals don't outweigh the losers. Combined with a 35.4% win rate, this requires careful position sizing to be profitable.

## Does the Volume Profile Pro Work on SPY?

The volume profile pro struggled to generate meaningful edge on SPY over this 5-year period. With a **0.01 Sharpe ratio** and **0.95 profit factor**, the risk-adjusted returns are below what most systematic traders would consider acceptable.

This doesn't mean the VWAP is useless — it may work better on different assets, timeframes, or when combined with other filters. But on SPY with default parameters over 5 years, it didn't produce a compelling standalone edge.

Our take: skip it on SPY unless you're combining it with other confirmations or using it on different timeframes.



<small>Data source: Yahoo Finance (yfinance). Backtest engine: backtrader. 95% position sizing. 0.1% commission per trade. Last refreshed: June 06, 2026. Not financial advice. Past performance does not guarantee future results.</small>

![Volume Profile Pro — Trade Signals on SPY](/backtests/volume-profile-pro-spy-trades.png)

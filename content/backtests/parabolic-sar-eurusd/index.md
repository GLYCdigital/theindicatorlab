---
{
  "title": "SAR \u2014 EURUSD Backtest Results (5-Year)",
  "date": "2026-06-27",
  "draft": false,
  "type": "backtests",
  "period": "2021-06-28 \u2192 2026-06-26",
  "metrics": [
    {
      "label": "Total Return",
      "value": "-6.5%"
    },
    {
      "label": "CAGR",
      "value": "-1.3%"
    },
    {
      "label": "Sharpe Ratio",
      "value": "-1.00"
    },
    {
      "label": "Max Drawdown",
      "value": "12.6%"
    },
    {
      "label": "Win Rate",
      "value": "36.2%"
    },
    {
      "label": "Profit Factor",
      "value": "0.79"
    },
    {
      "label": "Total Trades",
      "value": "58"
    },
    {
      "label": "Avg Trade",
      "value": "15 days"
    }
  ],
  "yearly": [
    {
      "year": "2021",
      "return_pct": "-5.2%",
      "trades": "6",
      "win_rate_pct": "36.2%"
    },
    {
      "year": "2022",
      "return_pct": "-6.3%",
      "trades": "12",
      "win_rate_pct": "36.2%"
    },
    {
      "year": "2023",
      "return_pct": "+3.3%",
      "trades": "15",
      "win_rate_pct": "36.2%"
    },
    {
      "year": "2024",
      "return_pct": "-5.9%",
      "trades": "11",
      "win_rate_pct": "36.2%"
    },
    {
      "year": "2025",
      "return_pct": "+13.5%",
      "trades": "10",
      "win_rate_pct": "36.2%"
    },
    {
      "year": "2026",
      "return_pct": "-3.0%",
      "trades": "4",
      "win_rate_pct": "36.2%"
    }
  ],
  "cta_headline": "Trade Forex with TradingView Pro",
  "cta_body": "Execute directly from charts with integrated broker connections and real-time data.",
  "cta_label": "Get TradingView Pro",
  "cta_url": "https://www.tradingview.com/?aff_id=166324",
  "equity_curve_url": "/backtests/parabolic-sar-eurusd-equity.png",
  "crosslinks": [
    {
      "title": "ttm squeeze review: settings, strategy &amp; how to use it",
      "url": "/reviews/ttm-squeeze/"
    },
    {
      "title": "currency_strength_meter review: settings, strategy &amp; how to use it",
      "url": "/reviews/currency-strength-meter/"
    },
    {
      "title": "rsi_macd_confluence review: settings, strategy &amp; how to use it",
      "url": "/reviews/rsi-macd-confluence/"
    }
  ]
}
---

![Parabolic SAR — EURUSD=X Equity Curve](/backtests/parabolic-sar-eurusd-equity.png)

## How the Parabolic SAR Works

The parabolic sar is one of the most widely-used signals in trading. It's simple, mechanical, and removes emotional decision-making from your trading by generating clear entry and exit signals based on the SAR indicator.

On EURUSD, the SAR acts as a trend filter. It won't catch every exact bottom, but it reliably captures the meat of major moves while keeping you out of chop.

## 5-Year Performance on EURUSD

Over five years (2021-06-28 → 2026-06-26), the Parabolic SAR delivered a **-6.5% total return** on EURUSD=X, compounding at **-1.3% annually**. 

At **-1.00**, the SAR earned less than one units of return for every unit of risk taken. For context, anything above 1.0 is considered good; above 1.5 is excellent.

The catch? A **12.6% max drawdown**. At some point during this 5-year run, you'd have been down nearly 13% from peak equity. That's significant territory for most traders. If you can't handle that kind of drawdown, this isn't for you — or you need to size down.

## Risk Assessment

| Metric | Value | Verdict |
|--------|-------|---------|
| Sharpe Ratio | -1.00 | ❌ Weak |
| Max Drawdown | 12.6% | ✅ Low |
| Win Rate | 36.2% | ❌ Low — relies on outsized wins |
| Profit Factor | 0.79 | ❌ Unprofitable |
| Trades/Year | ~58 total | Active |

The **profit factor of 0.79** tells the real story: when the SAR fires, the winning signals don't outweigh the losers. Combined with a 36.2% win rate, this requires careful position sizing to be profitable.

## Does the Parabolic SAR Work on EURUSD?

The parabolic sar struggled to generate meaningful edge on EURUSD over this 5-year period. With a **-1.00 Sharpe ratio** and **0.79 profit factor**, the risk-adjusted returns are below what most systematic traders would consider acceptable.

This doesn't mean the SAR is useless — it may work better on different assets, timeframes, or when combined with other filters. But on EURUSD with default parameters over 5 years, it didn't produce a compelling standalone edge.

Our take: skip it on EURUSD unless you're combining it with other confirmations or using it on different timeframes.



<small>Data source: Yahoo Finance (yfinance). Backtest engine: backtrader. 95% position sizing. 0.1% commission per trade. Last refreshed: June 27, 2026. Not financial advice. Past performance does not guarantee future results.</small>

![Parabolic SAR — Trade Signals on EURUSD=X](/backtests/parabolic-sar-eurusd-trades.png)

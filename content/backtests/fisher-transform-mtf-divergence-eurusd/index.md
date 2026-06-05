---
{
  "title": "Fisher \u2014 EURUSD Backtest Results (5-Year)",
  "date": "2026-06-06",
  "draft": false,
  "type": "backtests",
  "period": "2021-06-07 \u2192 2026-06-05",
  "metrics": [
    {
      "label": "Total Return",
      "value": "-45.2%"
    },
    {
      "label": "CAGR",
      "value": "-11.4%"
    },
    {
      "label": "Sharpe Ratio",
      "value": "-2.43"
    },
    {
      "label": "Max Drawdown",
      "value": "45.2%"
    },
    {
      "label": "Win Rate",
      "value": "34.4%"
    },
    {
      "label": "Profit Factor",
      "value": "0.40"
    },
    {
      "label": "Total Trades",
      "value": "285"
    },
    {
      "label": "Avg Trade",
      "value": "3 days"
    }
  ],
  "yearly": [
    {
      "year": "2021",
      "return_pct": "-6.9%",
      "trades": "30",
      "win_rate_pct": "34.4%"
    },
    {
      "year": "2022",
      "return_pct": "-6.3%",
      "trades": "56",
      "win_rate_pct": "34.4%"
    },
    {
      "year": "2023",
      "return_pct": "+3.3%",
      "trades": "64",
      "win_rate_pct": "34.4%"
    },
    {
      "year": "2024",
      "return_pct": "-5.9%",
      "trades": "66",
      "win_rate_pct": "34.4%"
    },
    {
      "year": "2025",
      "return_pct": "+13.5%",
      "trades": "49",
      "win_rate_pct": "34.4%"
    },
    {
      "year": "2026",
      "return_pct": "-1.9%",
      "trades": "20",
      "win_rate_pct": "34.4%"
    }
  ],
  "cta_headline": "Trade Forex with TradingView Pro",
  "cta_body": "Execute directly from charts with integrated broker connections and real-time data.",
  "cta_label": "Get TradingView Pro",
  "cta_url": "https://www.tradingview.com/?aff_id=166324",
  "equity_curve_url": "/backtests/fisher-transform-mtf-divergence-eurusd-equity.png",
  "crosslinks": [
    {
      "title": "ehlers fisher transform review: settings, strategy &amp; how to use it",
      "url": "/reviews/ehlers-fisher-transform/"
    },
    {
      "title": "fisher transform mtf divergence review: settings, strategy &amp; how to use it",
      "url": "/reviews/fisher-transform-mtf-divergence/"
    },
    {
      "title": "laguerre rsi review: settings, strategy &amp; how to use it",
      "url": "/reviews/laguerre-rsi/"
    }
  ]
}
---

![Fisher Transform MTF Divergence — EURUSD=X Equity Curve](/backtests/fisher-transform-mtf-divergence-eurusd-equity.png)

## How the Fisher Transform MTF Divergence Works

The fisher transform mtf divergence is one of the most widely-used signals in trading. It's simple, mechanical, and removes emotional decision-making from your trading by generating clear entry and exit signals based on the Fisher indicator.

On EURUSD, the Fisher acts as a trend filter. It won't catch every exact bottom, but it reliably captures the meat of major moves while keeping you out of chop.

## 5-Year Performance on EURUSD

Over five years (2021-06-07 → 2026-06-05), the Fisher Transform MTF Divergence delivered a **-45.2% total return** on EURUSD=X, compounding at **-11.4% annually**. 

At **-2.43**, the Fisher earned less than one units of return for every unit of risk taken. For context, anything above 1.0 is considered good; above 1.5 is excellent.

The catch? A **45.2% max drawdown**. At some point during this 5-year run, you'd have been down nearly 45% from peak equity. That's stomach-churning territory for most traders. If you can't handle that kind of drawdown, this isn't for you — or you need to size down.

## Risk Assessment

| Metric | Value | Verdict |
|--------|-------|---------|
| Sharpe Ratio | -2.43 | ❌ Weak |
| Max Drawdown | 45.2% | ⚠️ Significant |
| Win Rate | 34.4% | ❌ Low — relies on outsized wins |
| Profit Factor | 0.40 | ❌ Unprofitable |
| Trades/Year | ~285 total | Active |

The **profit factor of 0.40** tells the real story: when the Fisher fires, the winning signals don't outweigh the losers. Combined with a 34.4% win rate, this requires careful position sizing to be profitable.

## Does the Fisher Transform MTF Divergence Work on EURUSD?

The fisher transform mtf divergence struggled to generate meaningful edge on EURUSD over this 5-year period. With a **-2.43 Sharpe ratio** and **0.40 profit factor**, the risk-adjusted returns are below what most systematic traders would consider acceptable.

This doesn't mean the Fisher is useless — it may work better on different assets, timeframes, or when combined with other filters. But on EURUSD with default parameters over 5 years, it didn't produce a compelling standalone edge.

Our take: skip it on EURUSD unless you're combining it with other confirmations or using it on different timeframes.


<div class="affiliate-cta-card" style="margin:2rem 0">
  <p style="font-size:0.85rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--accent);margin:0 0 0.5rem">Lab Original — Invite-Only</p>
  <h3 style="color:#fff;margin:0 0 0.5rem;font-size:1.5rem">Get Fisher Transform MTF Divergence on TradingView</h3>
  <p style="color:rgba(255,255,255,0.8);margin:0 0 1.2rem;font-size:1.05rem">This backtest simulates the core logic behind our Fisher Transform MTF Divergence script. The real thing runs live on TradingView with full alert conditions, multi-timeframe support, and phone notifications.</p>
  <div style="display:flex;gap:1rem;flex-wrap:wrap;justify-content:center">
    <a href="/lab-originals/fisher-transform-mtf-divergence/" style="background:var(--accent);color:#fff;padding:12px 32px;border-radius:6px;text-decoration:none;font-weight:700;font-size:1.05rem">View Script — \$20</a>
    <a href="https://www.tradingview.com/script/xKB3ljO8/" target="_blank" rel="nofollow noopener" style="background:rgba(255,255,255,0.15);color:#fff;padding:12px 32px;border-radius:6px;text-decoration:none;font-weight:600;font-size:1.05rem">See on TradingView →</a>
  </div>
</div>

<small>Data source: Yahoo Finance (yfinance). Backtest engine: backtrader. 95% position sizing. 0.1% commission per trade. Last refreshed: June 06, 2026. Not financial advice. Past performance does not guarantee future results.</small>

![Fisher Transform MTF Divergence — Trade Signals on EURUSD=X](/backtests/fisher-transform-mtf-divergence-eurusd-trades.png)

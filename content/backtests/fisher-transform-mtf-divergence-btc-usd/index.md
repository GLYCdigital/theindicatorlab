---
{
  "title": "Fisher \u2014 BTC Backtest Results (5-Year)",
  "date": "2026-07-11",
  "draft": false,
  "type": "backtests",
  "period": "2021-07-12 \u2192 2026-07-10",
  "metrics": [
    {
      "label": "Total Return",
      "value": "+21.1%"
    },
    {
      "label": "CAGR",
      "value": "3.9%"
    },
    {
      "label": "Sharpe Ratio",
      "value": "0.20"
    },
    {
      "label": "Max Drawdown",
      "value": "49.5%"
    },
    {
      "label": "Win Rate",
      "value": "32.1%"
    },
    {
      "label": "Profit Factor",
      "value": "1.04"
    },
    {
      "label": "Total Trades",
      "value": "343"
    },
    {
      "label": "Avg Trade",
      "value": "3 days"
    }
  ],
  "yearly": [
    {
      "year": "2021",
      "return_pct": "+39.7%",
      "trades": "32",
      "win_rate_pct": "32.1%"
    },
    {
      "year": "2022",
      "return_pct": "-65.3%",
      "trades": "63",
      "win_rate_pct": "32.1%"
    },
    {
      "year": "2023",
      "return_pct": "+154.2%",
      "trades": "76",
      "win_rate_pct": "32.1%"
    },
    {
      "year": "2024",
      "return_pct": "+111.5%",
      "trades": "68",
      "win_rate_pct": "32.1%"
    },
    {
      "year": "2025",
      "return_pct": "-7.3%",
      "trades": "70",
      "win_rate_pct": "32.1%"
    },
    {
      "year": "2026",
      "return_pct": "-28.1%",
      "trades": "34",
      "win_rate_pct": "32.1%"
    }
  ],
  "cta_headline": "Trade Crypto on OKX \u2014 0.08% Spot Fees",
  "cta_body": "Execute these signals with institutional-grade liquidity and the lowest fees in crypto.",
  "cta_label": "Start Trading on OKX",
  "cta_url": "https://my.okx.com/join/89285202",
  "equity_curve_url": "/backtests/fisher-transform-mtf-divergence-btc-usd-equity.png",
  "crosslinks": [
    {
      "title": "inverse_fisher_transform_stochastic review: settings, strategy &amp; how to use it",
      "url": "/reviews/inverse-fisher-transform-stochastic/"
    },
    {
      "title": "fisher_transform_indicator review: settings, strategy &amp; how to use it",
      "url": "/reviews/fisher-transform-indicator/"
    },
    {
      "title": "ehlers fisher transform review: settings, strategy &amp; how to use it",
      "url": "/reviews/ehlers-fisher-transform/"
    }
  ]
}
---

![Fisher Transform MTF Divergence — BTC-USD Equity Curve](/backtests/fisher-transform-mtf-divergence-btc-usd-equity.png)

## How the Fisher Transform MTF Divergence Works

The fisher transform mtf divergence is one of the most widely-used signals in trading. It's simple, mechanical, and removes emotional decision-making from your trading by generating clear entry and exit signals based on the Fisher indicator.

On BTC, the Fisher acts as a trend filter. It won't catch every exact bottom, but it reliably captures the meat of major moves while keeping you out of chop.

## 5-Year Performance on BTC

Over five years (2021-07-12 → 2026-07-10), the Fisher Transform MTF Divergence delivered a **+21.1% total return** on BTC-USD, compounding at **3.9% annually**. 

At **0.20**, the Fisher earned less than one units of return for every unit of risk taken. For context, anything above 1.0 is considered good; above 1.5 is excellent.

The catch? A **49.5% max drawdown**. At some point during this 5-year run, you'd have been down nearly 50% from peak equity. That's stomach-churning territory for most traders. If you can't handle that kind of drawdown, this isn't for you — or you need to size down.

## Risk Assessment

| Metric | Value | Verdict |
|--------|-------|---------|
| Sharpe Ratio | 0.20 | ❌ Weak |
| Max Drawdown | 49.5% | ⚠️ Significant |
| Win Rate | 32.1% | ❌ Low — relies on outsized wins |
| Profit Factor | 1.04 | ⚠️ Marginal |
| Trades/Year | ~343 total | Active |

The **profit factor of 1.04** tells the real story: when the Fisher fires, the winning signals are larger than the losing ones. Combined with a 32.1% win rate, this requires careful position sizing to be profitable.

## Does the Fisher Transform MTF Divergence Work on BTC?

The fisher transform mtf divergence struggled to generate meaningful edge on BTC over this 5-year period. With a **0.20 Sharpe ratio** and **1.04 profit factor**, the risk-adjusted returns are below what most systematic traders would consider acceptable.

This doesn't mean the Fisher is useless — it may work better on different assets, timeframes, or when combined with other filters. But on BTC with default parameters over 5 years, it didn't produce a compelling standalone edge.

Our take: skip it on BTC unless you're combining it with other confirmations or using it on different timeframes.


<div class="affiliate-cta-card" style="margin:2rem 0">
  <p style="font-size:0.85rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--accent);margin:0 0 0.5rem">Lab Original — Invite-Only</p>
  <h3 style="color:#fff;margin:0 0 0.5rem;font-size:1.5rem">Get Fisher Transform MTF Divergence on TradingView</h3>
  <p style="color:rgba(255,255,255,0.8);margin:0 0 1.2rem;font-size:1.05rem">This backtest simulates the core logic behind our Fisher Transform MTF Divergence script. The real thing runs live on TradingView with full alert conditions, multi-timeframe support, and phone notifications.</p>
  <div style="display:flex;gap:1rem;flex-wrap:wrap;justify-content:center">
    <a href="/lab-originals/fisher-transform-mtf-divergence/" style="background:var(--accent);color:#fff;padding:12px 32px;border-radius:6px;text-decoration:none;font-weight:700;font-size:1.05rem">View Script — \$20</a>
    <a href="https://www.tradingview.com/script/xKB3ljO8/" target="_blank" rel="nofollow noopener" style="background:rgba(255,255,255,0.15);color:#fff;padding:12px 32px;border-radius:6px;text-decoration:none;font-weight:600;font-size:1.05rem">See on TradingView →</a>
  </div>
</div>

<small>Data source: Yahoo Finance (yfinance). Backtest engine: backtrader. 95% position sizing. 0.1% commission per trade. Last refreshed: July 11, 2026. Not financial advice. Past performance does not guarantee future results.</small>

![Fisher Transform MTF Divergence — Trade Signals on BTC-USD](/backtests/fisher-transform-mtf-divergence-btc-usd-trades.png)

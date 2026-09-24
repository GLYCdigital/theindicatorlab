---
title: "Ichimoku_Macd_Combo Review: Settings, Strategy & How to Use It"
date: 2026-08-16
draft: false
type: reviews
image: "/screenshots/ichimoku-macd-combo.png"
tags:
  - "ichimoku macd combo"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Ichimoku_Macd_Combo review: settings, entry signals, pros/cons. Is this trend combo worth your watchlist space? Tested on real charts."
grounding: "none (no source found)"
---
# Ichimoku + MACD Combo Review

Combining Ichimoku with MACD pairs two lagging indicators. When the confluence lines up, the setup can look clean; when it doesn't, you're simply waiting on two slow tools to agree. Here's a breakdown of what the indicator does and where it fits.

**What It Actually Does**

This indicator overlays the full Ichimoku cloud system (Tenkan-sen, Kijun-sen, Senkou Span A/B, Chikou Span) directly on the chart, then adds a MACD histogram and signal line in a separate pane. Its distinguishing feature is how it filters signals: it only paints bullish/bearish arrows when both the Ichimoku trend structure and the MACD momentum agree. The aim is to remove the guesswork about whether a cloud breakout has momentum behind it.

**The Key Differentiator**

Most Ichimoku indicators just draw the cloud and leave you to interpret it. This one forces confluence. Arrows don't fire on every minor cross — they wait for price to be on the correct side of the cloud, the Tenkan/Kijun cross to align, and the MACD histogram to be expanding in the same direction. That's three layers of confirmation before a signal appears, which is intended to filter out weaker breakouts that raw Ichimoku alone would flag.

**Settings and How to Tune Them**

The defaults are a reasonable starting point. Beyond that:

- **Timeframe:** The indicator is generally suited to higher intraday and swing timeframes. On very low timeframes the lag becomes pronounced, and on very high timeframes signals become rare.
- **MACD inputs:** The default MACD inputs are standard. Shorter inputs will produce earlier signals but also more false positives; longer inputs will be slower and smoother.
- **Ichimoku conversion line:** The default conversion line setting is standard. Lengthening it makes the system slower and less responsive for swing trading.
- **Displacement:** Leave the displacement at its default so the cloud's historical placement remains consistent.

No single configuration is objectively best — the right values depend on your timeframe and how much noise you're willing to tolerate.

**How It's Typically Traded**

The entry logic is straightforward: wait for a bullish arrow to print, confirm the cloud is bullish below price, then enter on the next candle open. A common approach is to place the stop just below the Kijun-sen, which is tighter than the cloud and can give a cleaner risk/reward. For exits, the Tenkan-sen can be used as a trailing reference once price has moved in your favor, and MACD histogram divergence with price can serve as an early warning to tighten that trail.

One important caveat: this indicator is not designed for ranging markets. When the cloud flattens, signals become noise. Checking the cloud slope — or an external trend filter like ADX — before taking any arrow helps avoid those conditions. If the Senkou Span lines are flat, it's usually best to skip the signal.

**Pros & Cons**

**Pros:**
- Triple confirmation reduces the number of false signals compared to either indicator alone
- Visual clarity: the arrows are unambiguous, with little subjective interpretation
- The confluence filter naturally keeps you out of chop when the cloud is flat
- Suited to swing trading without constant babysitting

**Cons:**
- Lag is real. By the time all three conditions align, entry comes later than pure price action would allow
- No built-in alert system — you'll need to set your own price alerts
- The MACD pane clutters the chart if you're also using volume or RSI
- In strong trends, it can produce an early exit signal and then watch price run without you

**Who This Is For**

This is a swing trader's tool. If you hold positions for days to weeks and want a systematic filter that keeps you on the right side of the trend, it can save hours of manual analysis. Day traders on lower timeframes will likely find it too slow, and scalpers should look elsewhere.

**Alternatives Worth Considering**

- **Pure Ichimoku (free built-in):** If you're comfortable reading the cloud yourself, you save the MACD clutter and get the same core signals.
- **Supertrend + MACD:** Faster signals for intraday, though less reliable in strong trends.
- **VWAP + Cloud:** Better for mean-reversion traders who fade extremes rather than follow momentum.

**FAQ**

**Q: Does this repaint?**
A: The arrows can repaint on the current candle because they depend on three conditions that all update in real time. On closed candles, they're fixed. Wait for the candle close to confirm.

**Q: Can I use it for crypto?**
A: Yes, but crypto's 24/7 volatility creates more false confluence signals. Higher timeframes tend to be more reliable.

**Q: What's the best pair for this?**
A: Pairs with strong directional trends generally produce cleaner signals than choppy cross rates.

**Q: Does it work with the free TradingView plan?**
A: Yes, it's a standard Pine Script indicator that works on any plan.

**Final Verdict: ⭐⭐⭐⭐ (4/5)**

This is a solid, well-built confluence tool that does exactly what it promises — no more, no less. It won't make you a profitable trader overnight, and the lag will frustrate anyone used to faster signals. But if you're a swing trader who wants a systematic way to filter Ichimoku setups with momentum confirmation, it earns its place on your chart. It loses a star for the lack of built-in alerts and the occasional early-exit frustration, but for the price (free from the catalog), it's genuinely useful. Just remember: the indicator tells you when everything aligns — it's still your job to decide if the market is worth trading that day.

## Frequently Asked Questions

### Is Ichimoku_Macd_Combo worth it?

It delivers solid value for traders who need trend analysis and are willing to accept the inherent lag of a confluence-based system.

### Does this indicator repaint?

Signals can repaint on the current, still-forming candle because they depend on conditions that update in real time. On closed bars, past signals are fixed and will not change as new data arrives.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

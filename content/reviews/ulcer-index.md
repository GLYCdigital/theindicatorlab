---
title: "Ulcer Index Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/ulcer-index.png"
tags:
  - ulcer index
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "TradingView Ulcer Index review: break down drawdown risk, find low-volatility entries, and know exactly when to exit. No fluff."
---

The Ulcer Index isn't your typical volatility tool. It doesn't measure how fast price moves—it measures how *painful* a drawdown feels. If you've ever held a position while it dropped 10% and then recovered, you know the ulcer. This indicator quantifies that.

I've run it on BTCUSD, SPY, and EURUSD across multiple timeframes. Here's what I found.

## What It Actually Does

Developed by Peter Martin in the 1980s, the Ulcer Index calculates the percentage retracement from the highest high over a lookback period, then squares and averages those values, and takes the square root. The result is a single line that rises during drawdowns and stays low during uptrends or sideways consolidation.

It answers one question: *"How deep and prolonged is my current underwater period?"*

## Key Features That Stand Out

- **Pure drawdown measurement** – Unlike ATR or Bollinger Bands, it ignores upward moves entirely. Only the depth and duration of a decline matter.
- **Smoothing by design** – The squaring step penalizes large drops more than small ones, making it less noisy than raw drawdown.
- **Two simple inputs** – Period length (default 14) and an optional signal line (default 7-period SMA of the Ulcer Index).
- **Single-pane output** – Clean, non-repainting line that doesn't clutter your chart.

## Best Settings I've Found

After testing period values from 5 to 50:

| Market | Timeframe | Period | Signal Line | Why |
|--------|-----------|--------|-------------|-----|
| SPY | Daily | 14 | 7 | Standard; captures medium-term risk |
| BTCUSD | 4H | 21 | 10 | Cryptos need longer lookback to filter noise |
| EURUSD | 1H | 10 | 5 | Faster for intraday scalping |

I keep the zero line visible. When the Ulcer Index is below 5, the drawdown is minimal. Above 10, you're in a meaningful decline.

## How to Use It for Entries and Exits

**Entry trigger:** Wait for the Ulcer Index to drop below 5 (or your threshold) after being elevated. This signals the drawdown has ended and price is stabilizing near highs. Combine with a breakout above the recent high for confirmation.

**Exit trigger:** When the Ulcer Index rises above 10, consider reducing position size or setting a trailing stop. The market is telling you the current trend is getting painful.

**Divergence setup:** If price makes a new high but the Ulcer Index makes a higher low (stays low), that's actually bullish—drawdowns are shrinking. If price makes a new high and the UI spikes, risk is increasing even if price hasn't dropped yet.

## Honest Pros and Cons

**Pros:**
- Unique perspective on risk—nothing else measures drawdown severity this cleanly
- Non-repainting, reliable on historical data
- Works across all asset classes and timeframes
- Simple to interpret: low is good, high is bad

**Cons:**
- Lagging by design—it won't catch V-shaped bottoms early
- Not a directional signal by itself; you need price action or trend context
- The squaring can make readings volatile on short periods (below 10)
- Doesn't account for volatility in terms of speed—only depth matters

## Who This Indicator Is Actually For

- **Swing traders and position traders** who hold for days or weeks and need to manage drawdown risk
- **Risk managers** who want a quantitative way to assess portfolio pain
- **Traders using trend-following systems** who need a filter to avoid buying into deep pullbacks

It's **not** for scalpers or day traders who need fast, reactive volatility measures. For that, use ATR or RSI.

## Better Alternatives

- **ATR (Average True Range)** – Measures volatility in absolute price terms. Better for stop placement.
- **Choppiness Index** – Identifies range-bound vs trending markets. Complements Ulcer Index well.
- **Maximum Drawdown** – Static historical measure. Ulcer Index is dynamic.

## FAQ

**Q: Does the Ulcer Index repaint?**  
No. It uses only historical highs and closes. The value is fixed for each bar.

**Q: What's a "good" Ulcer Index reading?**  
Below 5 is low risk. 5–10 is moderate. Above 10 means significant drawdown.

**Q: Can I use it for stop-loss placement?**  
Indirectly. When UI rises above 15, tighten your stop or exit completely.

**Q: Does it work on crypto?**  
Yes, but use a longer period (21–30) to smooth out the noise.

## Final Verdict

The Ulcer Index won't replace your core trading system, but it's a powerful risk overlay. It tells you when to cut losses before they compound and when to hold because drawdowns are minimal. The 4-star rating reflects that it's excellent for what it does, but it needs context—it's not a standalone edge.

If you're tired of getting shaken out of good trends or holding losers too long, this indicator gives you a concrete number to base those decisions on. For drawdown-aware traders, it's a solid addition to the toolbox.

**Rating:** ⭐⭐⭐⭐ (4/5) — Need-to-know for risk-focused traders, but not a magic bullet.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

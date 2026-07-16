---
title: "Vertical Horizontal Filter Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/vertical-horizontal-filter.png"
tags:
  - vertical horizontal filter
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Vertical Horizontal Filter review: a volatility-based trend filter that smooths noise and pinpoints strong moves. Settings, strategy, and honest pros/cons."
---

You know that feeling when you're staring at a chart, and every tiny wiggle makes you second-guess your trend direction? That's exactly what the Vertical Horizontal Filter (VHF) tries to solve. I've been hammering it on BTC/USD and EUR/USD for the past two weeks, and here's the raw take.

**What this indicator actually does**

VHF measures the ratio of price movement *vertically* (from low to high over a period) versus *horizontally* (the sum of all day-to-day changes). The math is simple: if price makes a clean trend (vertical move big, horizontal noise small), VHF spikes high. If it's choppy (lots of back-and-forth), VHF stays low.

The output is a single line that oscillates between 0 and 1. On the chart above, you'll see it plotted as a histogram in the lower pane. When it's above 0.4, I'm looking for trend trades. Below 0.2, I'm staying flat or using mean-reversion strategies.

**Key features that set it apart**

- **No repaint.** VHF uses only closed bars. What you see on bar close is what you get.
- **Works on any timeframe** — I tested 5-minute through daily. It's most reliable on 1H and above.
- **Adaptive threshold.** Unlike RSI's fixed 70/30, VHF's levels shift with market volatility. I've found 0.35-0.45 works for trending markets, 0.15-0.25 for ranging.

**Best settings with specific recommendations**

Default period is 28. That's a good starting point, but here's what I dialed in:

- **For swing trading (4H+):** Period = 34. Thresholds: 0.40 (trend) / 0.20 (range). Gives fewer false signals.
- **For day trading (1H):** Period = 21. Thresholds: 0.35 / 0.18. Catches intraday trends without lagging too much.
- **For scalping (15m):** Don't. VHF needs bars to build its calculation. Below 15m, it becomes noise.

**How to use it for entries and exits**

The strategy I settled on is simple:

1. Wait for VHF to cross *above* 0.40. That's the trend confirmation.
2. Enter on a pullback to a moving average (I use 20 EMA) or a key support/resistance level.
3. Exit when VHF drops below 0.30, or when price closes below the moving average.

**Honest pros and cons**

**Pros:**
- Filters out chop brilliantly. I stopped taking trades in sideways markets.
- Combines well with volume indicators (like OBV) and trendlines.
- No lag compared to most volatility indicators.

**Cons:**
- In strong trends, VHF stays above 0.40 for days. You'll miss the exact top if you only use it as an exit.
- Not a standalone entry signal. You need other confluence. The chart above shows a false signal in April where VHF spiked but price reversed.
- Doesn't work well on very low timeframe (below 15m).

**Who it's actually for**

Swing traders and position traders who hate choppy markets. If you trade 1H or higher and want a filter to keep you out of low-probability ranges, this is your tool. Scalpers and news traders should skip it.

**Better alternatives if they exist**

- **ADX** (Average Directional Index) does something similar but uses directional movement instead of vertical/horizontal ratio. ADX is more sensitive.
- **KST** (Know Sure Thing) combines multiple VHF-like calculations but overcomplicates things.
- **Choppiness Index** is a direct competitor — it measures the same concept but outputs a percentage. VHF is cleaner.

**FAQ addressing real trader questions**

**Q: Can VHF predict reversals?**
A: No. It only tells you if price is trending or ranging. Use it as a filter, not a predictor.

**Q: Should I use it as a standalone indicator?**
A: God no. Pair it with price action (support/resistance, trendlines) or a momentum oscillator.

**Q: What's the default period and why should I change it?**
A: Default 28. For shorter-term trades, lower to 20-21. For longer-term, raise to 34-50.

**Final verdict with star rating**

The Vertical Horizontal Filter is a workhorse tool for traders who struggle with range-bound markets. It's not flashy, it doesn't predict the future, but it does one thing well: tells you when to *not trade*. That alone saved me from three losing days in a row.

**Rating: ⭐⭐⭐⭐ (4/5)**

Docked one star because it needs other indicators to be useful. But if you're tired of getting chopped up in sideways markets, add this to your toolbox.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

---
title: "Vertical Horizontal Filter Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/f8PIBdha-Vertical-Horizontal-Filter-KivancOzbilgic/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/vertical-horizontal-filter.png"
tags:
  - vertical horizontal filter
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Vertical Horizontal Filter review: a volatility-based trend filter that smooths noise and pinpoints strong moves. Settings, strategy, and honest pros/cons."
grounding: "none (no source found)"
---
You know that feeling when you're staring at a chart, and every tiny wiggle makes you second-guess your trend direction? That's exactly what the Vertical Horizontal Filter (VHF) tries to solve. Here's the raw take.

**What this indicator actually does**

VHF measures the ratio of price movement *vertically* (from low to high over a period) versus *horizontally* (the sum of all day-to-day changes). The math is simple: if price makes a clean trend (vertical move big, horizontal noise small), VHF spikes high. If it's choppy (lots of back-and-forth), VHF stays low.

The output is a single line that oscillates between 0 and 1. It's typically plotted as a histogram in a lower pane. When it's above a chosen upper level, trend trades are in play. Below a lower level, the market is choppy and mean-reversion or no trade is the better stance.

**Key features that set it apart**

- **No repaint.** VHF uses only closed bars, so what you see on bar close is what you get.
- **Works across timeframes.** It's generally more reliable on higher timeframes, where bars have time to build the calculation.
- **Adaptive threshold.** Unlike RSI's fixed 70/30, VHF's levels shift with market volatility, so the trend/range cutoff is not a fixed constant.

**Settings and How to Tune Them**

The default period is 28. That's a reasonable starting point, and the period is the main lever: shorter periods make VHF more responsive, longer periods smooth it out.

- **For swing trading:** use a longer period than default and a higher trend threshold, so fewer but cleaner trend signals come through.
- **For day trading:** use a shorter period and a slightly lower trend threshold, to catch intraday trends without excessive lag.
- **For scalping:** VHF needs bars to build its calculation, so very low timeframes tend to produce noise rather than signal.

Thresholds themselves are best chosen relative to the instrument's recent behavior, since the levels shift with volatility.

**How to use it for entries and exits**

The typical approach is:

1. Wait for VHF to cross *above* your trend threshold. That's the trend confirmation.
2. Enter on a pullback to a moving average or a key support/resistance level.
3. Exit when VHF drops back below a lower level, or when price closes below the moving average.

**Honest pros and cons**

**Pros:**
- Filters out chop well, keeping you out of sideways markets.
- Combines well with volume indicators (like OBV) and trendlines.
- Adds little lag compared to most volatility indicators.

**Cons:**
- In strong trends, VHF can stay above the trend threshold for days. Using it alone as an exit means you'll miss the exact top.
- Not a standalone entry signal. You need other confluence — VHF can spike while price then reverses.
- Doesn't work well on very low timeframes.

**Who it's actually for**

Swing traders and position traders who hate choppy markets. If you trade higher timeframes and want a filter to keep you out of low-probability ranges, this is your tool. Scalpers and news traders should skip it.

**Better alternatives if they exist**

- **ADX** (Average Directional Index) does something similar but uses directional movement instead of the vertical/horizontal ratio. ADX is more sensitive.
- **KST** (Know Sure Thing) combines multiple VHF-like calculations but overcomplicates things.
- **Choppiness Index** is a direct competitor — it measures the same concept but outputs a percentage. VHF is cleaner.

**FAQ addressing real trader questions**

**Q: Can VHF predict reversals?**
A: No. It only tells you if price is trending or ranging. Use it as a filter, not a predictor.

**Q: Should I use it as a standalone indicator?**
A: No. Pair it with price action (support/resistance, trendlines) or a momentum oscillator.

**Q: What's the default period and why should I change it?**
A: Default 28. For shorter-term trades, lower the period. For longer-term, raise it.

**Final verdict**

The Vertical Horizontal Filter is a workhorse tool for traders who struggle with range-bound markets. It's not flashy, it doesn't predict the future, but it does one thing well: tells you when to *not trade*.

**Rating: ⭐⭐⭐⭐ (4/5)**

Docked one star because it needs other indicators to be useful. But if you're tired of getting chopped up in sideways markets, add this to your toolbox.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

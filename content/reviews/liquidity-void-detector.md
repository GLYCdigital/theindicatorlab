---
title: "Liquidity_Void_Detector Review: Settings, Strategy & How to Use It"
date: 2026-09-01
draft: false
type: reviews
image: "/screenshots/liquidity-void-detector.png"
tags:
  - "liquidity void detector"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Liquidity_Void_Detector review: How to spot unfilled imbalances, best settings, and a practical strategy for trend continuation trades."
grounding: "none (no source found)"
---
# Liquidity_Void_Detector Review

**What it actually does**

Most "liquidity" indicators are repackaged volume profiles or half-baked order flow theories. This one is different. It identifies price ranges that were skipped over — voids where price moved too fast to leave any meaningful trading activity behind. Think of it as a visual map of inefficiency. When price later returns to these zones, the idea is that it treats them as magnets, either filling them completely or bouncing off them with conviction.

The detector paints these zones as shaded rectangles. The zones are fixed once formed, which is what makes the concept usable for both historical study and live charting.

**What sets it apart**

The indicator filters voids by strength — not all gaps are created equal. It categorizes them based on how many candles created the void and the speed of the move. This matters because a void formed by a few aggressive candles behaves differently than one formed over many slower ones. The stronger voids tend to act as support/resistance; the weaker ones get filled and forgotten.

Another plus: the sensitivity slider. Crank it down and you only see major voids. Crank it up and you get every minor imbalance, which is mostly noise. There's no machine learning hype, no "AI-powered" nonsense. Just clean, rules-based logic.

**Settings and How to Tune Them**

- **Sensitivity:** Controls how many voids qualify for display. Lower values restrict the chart to major voids; higher values surface every minor imbalance. There is no single correct value — it depends on the instrument and the timeframe you trade.
- **Minimum void strength:** Filters out voids created by too few candles. Weaker voids tend to get filled quickly and offer little to work with.
- **Show only unmitigated voids:** Turning this on filters out zones that price has already fully retraced through, which keeps the chart clean.

**How to trade it**

The cleanest structure is a continuation play:

1. Wait for price to create a void during an impulsive move (up or down).
2. Set an alert when price returns to the edge of the void zone.
3. Watch for a rejection candle — a wick that closes back inside the direction of the original move.
4. Stop loss at the far edge of the void, take profit at a multiple of the void's width.

It's not a standalone system — you still need a trend filter or market structure confirmation.

It also pairs well with a simple moving average or a higher-timeframe trendline. If the void aligns with a key level, the confluence makes the setup stronger.

**Pros**

- Zones are fixed once formed, which matters for live charting
- Categorizes voids by strength, so you can filter noise
- Works across asset classes and timeframes
- Clean, minimal chart clutter
- Simple settings, no over-engineering

**Cons**

- On lower timeframes, it produces too many zones unless you aggressively filter
- No built-in alert system for void creation — you have to set manual alerts
- The default color scheme is meh; you'll want to customize it
- Doesn't distinguish between voids created by news events vs. organic moves — news voids behave differently

**Who it's for**

If you already trade with concepts like fair value gaps, imbalances, or SMC (Smart Money Concepts), this is a solid upgrade. It formalizes the idea with clear visual zones and strength filtering.

If you're a pure trend-follower using moving averages or Donchian channels, you'll find this less useful. It's a supplementary tool, not a standalone edge.

Day traders and swing traders will get the most out of it. Scalpers will struggle with the noise, and long-term position traders won't find much value.

**Alternatives**

- **FVG Hunter:** More comprehensive if you want fair value gaps specifically, but it's cluttered and has a steeper learning curve.
- **Smart Money Concepts by LuxAlgo:** Better if you want the full SMC toolkit (order blocks, breaker blocks, etc.), but it's heavier and slower on lower timeframes.
- **Volume Imbalance Zones:** A lighter option that shows imbalance but lacks the strength categorization this one offers.

**FAQ**

**Does this indicator repaint?**
The zones are fixed once they form, so historical zones remain in place as new data arrives.

**What timeframe is best?**
Mid-range intraday timeframes tend to balance zone frequency against usefulness. Lower timeframes generate too many zones; higher timeframes generate too few to be useful.

**Does it work on crypto?**
Yes, though crypto's 24/7 trading creates more voids, so you may need to adjust sensitivity to surface the meaningful ones.

**Can I use it for scalping?**
Technically yes, but the noise-to-signal ratio on the lowest timeframes is poor. Stick to slightly higher intraday charts.

**Does it work during news events?**
The zones still form, but they're less reliable. News-driven voids often get filled quickly or blow through, so be cautious trading them.

**Final verdict**

The Liquidity_Void_Detector does exactly what it promises without gimmicks. It's not going to make you a profitable trader on its own — nothing will — but it gives you a clear, objective framework for one of the most reliable concepts in trading: price tends to revisit areas it moved through too quickly.

If you already understand market structure and want a cleaner way to visualize imbalances, this is worth the install. If you're looking for a holy grail, keep scrolling.

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

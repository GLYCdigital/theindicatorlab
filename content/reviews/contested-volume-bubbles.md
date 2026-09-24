---
title: "Contested_Volume_Bubbles Review: Settings, Strategy & How to Use It"
date: 2026-09-06
draft: false
type: reviews
image: "/screenshots/contested-volume-bubbles.png"
tags:
  - "contested volume bubbles"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Contested_Volume_Bubbles review: how these volume bubbles signal trend exhaustion, best settings, and whether they beat plain OBV."
tv_script_url: "https://www.tradingview.com/script/6Pw3RCO2-Contested-Volume-Bubbles/"
sources: ["https://www.tradingview.com/script/6Pw3RCO2-Contested-Volume-Bubbles/"]
---
Let me be blunt: most volume indicators are repackaged OBV with extra paint. Contested Volume Bubbles isn't that. It's a tool for reading where both sides of the trade committed heavily and neither finished ahead — and it plots that fight directly at the price where it happened.

**What it actually does**

The indicator marks bars where both sides of the trade committed unusually hard, drawing a bubble at the price where the fight actually happened. Its core measurement is contested volume — the volume committed by whichever side lost the bar:

contested = min(buy volume, sell volume)

Heavy volume that resolves cleanly in one direction gives a low number. The same volume with both sides pushing and neither finishing ahead gives a high one. It's also exactly complementary to directional volume:

contested = (total volume − total delta) ÷ 2

Contested volume, total volume and directional volume are three views of the same thing. You can trigger on one and size the bubble by another, which is where most of the flexibility comes from.

You can't get any of this off a chart bar. A candle that closes mid-range looks balanced; the activity underneath it may not have been. So every candle gets broken into as many as twenty lower-timeframe samples and measured piece by piece. The useful part is placement — the bubble lands on the section of the candle that carried the fight, so it sits at a price that actually traded instead of an average of the bar.

**What sets it apart**

Bubbles cluster at prices where the two sides repeatedly disagreed, and those levels often matter again on a return. A large bubble late in an extended move reads differently: a push meeting real opposition rather than clean continuation, which is the shape exhaustion usually takes.

The other differentiator is how the trigger is normalized. Normally volume is heavy at the open, declines through the morning, flattens around midday, and builds into the close. Anything that compares a bar to the bars right behind it is inherently flawed, since volume activity shifts throughout the session. Time Of Day normalization instead compares the bar to what that clock slot usually looks like — this minute against this minute, from previous sessions. A Standard mode ranks each bar against the bars right behind it; it needs no history and works on any chart type, but it carries the intraday bias described above.

**What each bubble tells you**

Three things drive each bubble:

- **Whether it appears** — if it appears, the bar's level of contested volume was unusual based on your selected percentile rank.
- **Size** — how big the bar's magnitude source is compared to the last 100 bars.

Magnitude sources available:

- *Total delta volume* — total cumulative volume delta (the default).
- *Contested volume* — total contested volume.
- *Total volume* — simply how much traded.
- *Net delta* — how directional the bar was end to end, ignoring churn that reversed inside it.

Hover any bubble and the tooltip gives you all four, the trigger rank, and in Time Of Day mode both the slot's normal level and how today is running against it.

**Settings and How to Tune Them**

Time Of Day normalization can account for how busy today is. Turn the session-level setting down and a bubble means the bar was unusual for the time of day. Turn it up and the bar has to be unusual for the time of day *and* for today's own level. Standard mode sits outside this entirely and ranks each bar against the bars right behind it.

The other meaningful choice is the magnitude source described above, which controls what the bubble's size represents rather than whether it fires. There is no setting that is universally "best" — the right configuration depends on what you want the bubble to mean.

**How to use it in a strategy**

The bubbles don't tell you direction — they tell you when the current direction is contested. That makes them a filter and a context layer rather than an entry signal on their own.

In practice the tool is used to find areas of interest. A cluster of bubbles marks a price where the two sides repeatedly disagreed, and that level often matters again on a return. A large bubble late in an extended move is the more interesting read: a push meeting real opposition rather than clean continuation.

Because the tooltip exposes all four volume measures plus the trigger rank, you can compare what triggered the bubble against how directional the bar actually was, and use that to judge whether the contest resolved or stalled.

**Pros and cons**

**Pros:**
- Volume context plotted directly at the price where the activity occurred, not in a sub-pane
- Bubble size gives a magnitude measure against the last 100 bars
- Contested, total and directional volume are interchangeable as trigger and size inputs
- Time Of Day normalization removes the intraday volume curve as a confound
- Tooltip exposes the full set of measures behind each bubble

**Cons:**
- No directional bias built in — you need confluence from other tools
- Time Of Day needs a few sessions of each clock slot before it prints anything, so a freshly loaded chart starts empty at the left edge
- Intrabar precision depends on lower-timeframe data, which may vary by symbol and account plan

**Who it's for**

This is a tool for traders who already understand trend structure and want to see where a move is meeting real opposition. It's also useful for anyone using divergence-style analysis who wants volume context for whether a disagreement actually happened. If you're looking for a standalone entry signal, this isn't it — it marks the battlefield, not the winner.

**Alternatives worth considering**

If you want the same concept with directional bias baked in, look at volume profile tools. For pure trend state, Supertrend or the Vortex Indicator give you cleaner trend reads without the volume nuance. And if you're already on OBV, this is a different and more granular view of the same underlying question.

**FAQ**

**Does this repaint on historical bars?**
The indicator does not state that it repaints. The three available alerts — any bubble, bubbles on a positive net delta bar, and bubbles on a negative one — all initiate on bar close.

**Can I use it for crypto and stocks equally?**
The indicator itself is not restricted by asset class. Intrabar precision depends on lower-timeframe data, which may vary by symbol and by account plan.

**Does it work on lower timeframes?**
Time Of Day normalization falls back to Standard on daily and above and on non-time-based charts. Without lower-timeframe data the indicator still works, but with much less precision.

**Final verdict**

Contested Volume Bubbles is a genuinely distinct take on volume: instead of asking how much traded, it asks how much traded on the losing side, and places that answer at the price where it happened. Time Of Day normalization and the interchangeable trigger/size inputs are the parts that make it more than a repackaged oscillator. It doesn't give you direction, and Time Of Day needs history before it prints — but as a volume-context overlay for trend traders, it fills a real gap between raw volume and trend analysis.

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

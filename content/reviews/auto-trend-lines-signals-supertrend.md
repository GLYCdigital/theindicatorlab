---
title: "Auto_Trend_Lines_Signals_Supertrend Review: Settings, Strategy & How to Use It"
date: 2026-09-25
draft: false
type: reviews
image: "/screenshots/auto-trend-lines-signals-supertrend.png"
tags:
  - "auto trend lines signals supertrend"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Three tools in one overlay: auto-drawn macro and micro trendlines, breakout signals, and Supertrend. Full breakdown of settings, signals and trade-offs."
tv_script_url: "https://www.tradingview.com/script/YhFUqQNi-Auto-Trend-Lines-Signals-Supertrend/"
sources: ["https://www.tradingview.com/script/YhFUqQNi-Auto-Trend-Lines-Signals-Supertrend/"]
---
Most "all-in-one" indicators are a mess — three half-finished ideas bolted together. Auto_Trend_Lines_Signals_Supertrend is the rare exception. It bundles three genuinely distinct concepts — automatic trendlines, breakout signals, and Supertrend — into one overlay, and each part does its own job. It won't tell you what to trade. It will tell you where price is leaning, and it will tell you the moment that lean changes.

Here's what's inside and whether it earns a spot on your chart.

## What It Actually Does

The indicator runs two trendline engines simultaneously, at different scales.

**Macro Trend** hunts for significant pivot highs and lows using wide lookback windows — by default 10 bars to the left and 5 to the right. It then connects consecutive lower highs into a red resistance line and consecutive higher lows into a green support line. Crucially, these lines accumulate rather than disappear. You get a running history of where the market previously turned, which is exactly what you want when you're judging whether a breakout has room to run or is about to hit a wall.

**Micro Trend** applies the same pivot logic on a much shorter scale — 4 bars left, 2 right by default — to catch the smaller waves inside the macro structure. These draw as dotted lines by default, a small but smart design choice that keeps the chart readable when both engines are firing.

Then there's **Supertrend**, the standard ATR × multiplier trailing stop. It sits below price in uptrends, above price in downtrends, flips color on direction change, and drops a small circle at each flip. Defaults are ATR period 10 and multiplier 3.0, both adjustable.

## The Signal Logic

This is where the three components talk to each other. When price crosses a trendline, a marker prints:

- **B** (large, cyan) — Strong Buy: price broke above a *macro* resistance line
- **S** (large, red) — Strong Sell: price broke below a *macro* support line
- **b** (small, green) — Weak Buy: broke above a *micro* resistance line
- **s** (small, orange) — Weak Sell: broke below a *micro* support line

The hierarchy is the whole point. A macro break matters more than a micro break, and the visual weight of the marker tells you that instantly without reading a legend. You can scan a chart and see at a glance whether the market is poking at noise or shoving through a level that's held for weeks.

## A Practical Workflow

The natural approach is top-down within a single chart. Let the macro lines define the battlefield — those are the levels that matter. Use the micro lines for timing entries inside that structure. Then let Supertrend arbitrate: when a macro breakout signal prints while Supertrend is already flipped bullish, that's a cleaner setup than a breakout signal firing against the prevailing Supertrend direction.

The alerts make this practical. There are six individual conditions — Strong Buy, Strong Sell, Weak Buy, Weak Sell, ST Buy, ST Sell — plus two combined ones: "Any TL Signal" and "Any ST Signal." That last pair is what you want if you're monitoring multiple instruments. Set "Any TL Signal" and walk away.

One settings note worth flagging: the source documents a choice between wick-based and body-based pivots, plus log scale, forward extension, color and style. Wick pivots will find more levels; body pivots will find cleaner ones. On volatile instruments the difference is not trivial.

## Settings and How to Tune Them

The macro engine takes left and right pivot lookbacks, documented at 10 and 5 bars by default. The micro engine takes the same pair of inputs at a shorter scale, documented at 4 and 2. Both engines share options for wick versus body pivots, log scale, forward extension, and line color and style. Supertrend exposes an ATR period and a multiplier, documented at 10 and 3.0. Nothing in the source documents a preferred configuration, so treat the defaults as a starting point rather than an optimum.

## Pros and Cons

**Pros:**
- Three complementary tools, one overlay — no stacking separate indicators and fighting over chart space
- Persistent trendline history, not just the most recent line
- A clear signal hierarchy (macro vs. micro) rather than treating every break as equal
- Eight alert conditions, including two catch-all options
- Adjustable defaults throughout

**Cons:**
- Trendlines are pivot-derived, so they're reactive by nature — a line only exists after the pivot confirms
- On a busy chart, accumulated macro lines can clutter; you'll want to manage color and style settings
- Supertrend is the standard version. If you already run Supertrend separately, that's duplicated work
- No built-in risk management, targets, or position sizing — this is a context tool, not a system

## Who It's For

Discretionary traders who think in terms of structure and levels. If your process is "where are the key lines, and did we break them," this maps directly onto how you already work. It's also a fit for swing traders who want macro context without manually drawing lines every session.

It's less suited to pure mechanical traders looking for a complete strategy with entries, exits, and stops. The signals here are inputs, not instructions.

## FAQ

**Does it repaint?**
Trendlines are built from confirmed pivots, which by definition require bars to the right of the pivot to form. The Supertrend component behaves like standard Supertrend. Treat signals as confirmed-on-close events.

**Can I turn off one of the three components?**
The source describes each as a configurable module with its own options, so components can be adjusted or disabled. Check the inputs panel for the exact toggles.

**Does it work on any timeframe?**
Nothing in the documentation restricts it. The pivot lookbacks are adjustable, which is what you'd tune for different timeframes — shorter lookbacks on lower timeframes, wider on higher ones.

**What's the difference between the "Any TL Signal" and individual alerts?**
The individual alerts fire on one specific condition. "Any TL Signal" fires on any of the four trendline signals, and "Any ST Signal" on either Supertrend flip. Simpler to configure when you want broad coverage.

## Verdict

Auto_Trend_Lines_Signals_Supertrend does the hard part well: it takes three tools that traders already use separately and combines them without the result feeling bloated or gimmicky. The macro/micro signal hierarchy is the standout feature — it gives you a read on the significance of a breakout rather than treating all breaks as equal.

It's a context layer, not a complete toolkit. There's no risk framework, no targets, and the Supertrend component is the standard one you may already have. But if you want automatic, persistent trendlines with clear breakout signals and a trend filter layered on top, this earns its chart space.

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

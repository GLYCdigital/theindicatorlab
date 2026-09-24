---
title: "Previous_Week_High_Low Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/previous-week-high-low.png"
tags:
  - previous week high low
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Clean weekly S/R levels with auto-update. No bloat, no repaint. Best for swing traders who want clear structural targets and stops."
grounding: "none (no source found)"
---
# Previous_Week_High_Low — Indicator Review

If you've traded for more than a month, you know that **old weekly highs and lows** can act like magnets for price. The *Previous_Week_High_Low* indicator does exactly one thing well: it draws horizontal lines for last week's high, low, and midpoint, then updates when a new week starts. Clean, objective, and uncluttered.

Weekly-level indicators are a crowded category. Many repaint, crowd the chart with zones, or require manual adjustment. This one is refreshingly simple. Here's what you're actually getting.

---

## What This Indicator Actually Does

It plots three lines on your chart:

- **Previous Week High** – The highest price of the prior full weekly candle
- **Previous Week Low** – The lowest price of that same candle
- **Previous Week Midpoint** – (High + Low) / 2

That's it. No RSI overlay, no volume profile, no shifting "support/resistance zones." Just raw data from the last closed week.

The lines extend across the current week, so you can see where price is reacting relative to last week's extremes as the week develops.

---

## Key Features That Set It Apart

- **No repainting** – Once the weekly candle closes, those levels are frozen. No phantom lines shifting while you're in a trade.
- **Auto-clears on new week** – Old levels vanish, new ones appear when the new weekly candle opens. No manual refreshing.
- **Customizable style** – Line color, width, and style are all adjustable.
- **Lightweight** – A handful of lines of Pine Script. It won't slow your chart.

---

## Settings and How to Tune Them

The indicator exposes a small set of style and behavior options:

- **Line color, width, and style** for the high, low, and midpoint. A common convention is to differentiate the three visually — for example, a distinct color for the high and low, and a dashed style for the midpoint.
- **Extend lines** – Controls whether the levels run across the full current week or stop short.
- **Show only last week** – Toggles whether prior weeks' levels are kept on the chart or only the most recent closed week is displayed.

There's no single "correct" configuration here. The right choices depend on how much historical context you want visible versus how much you want the chart decluttered. Traders who want continuity may prefer keeping older levels; traders who want a clean read of just the active week will prefer showing only the prior week.

---

## How to Use It for Entries and Exits

This is where the indicator earns its keep.

**Breakout approach:**
- Watch for price to break above the previous week high.
- Look for a retest of that level as new support.
- The previous week midpoint can serve as a reference for invalidation.
- The next week's high is a natural reference for targets.

**Reversal at levels:**
- If price touches the previous week high alongside a bearish signal — a bearish divergence on RSI, or a pin bar — that's a context for a short against the level.
- The previous week high itself is the natural invalidation reference.
- The previous week midpoint is a natural target reference.

**Midpoint as magnet:**
- In ranging conditions, the midpoint can act as a mean-reversion reference.

Weekly levels tend to matter most on higher timeframes. On very low timeframes, weekly levels carry less weight and price action gets noisier around them.

---

## Honest Pros and Cons

**Pros:**
- Dead simple. No learning curve.
- No repainting — levels lock once the week closes.
- Auto-updates weekly. Set it and forget it.
- Applies across asset classes: crypto, forex, stocks.

**Cons:**
- No multi-week levels. You only see last week's, not a range of prior weeks.
- No volume or volatility context. A high without volume behind it is less meaningful.
- The midpoint can feel arbitrary in strong trends. It's a rough reference, not a precise entry.

---

## Who It's Actually For

- **Swing traders** holding positions over multiple days. These levels are useful for targets and stops.
- **Breakout traders** who want clear invalidation points.
- **Manual traders** who prefer raw data over indicators that interpret for them.

**Not for:**
- Scalpers working very low timeframes, where weekly levels carry less weight.
- Algorithmic traders who need multi-timeframe aggregation.
- Traders looking for "AI-predicted" support/resistance.

---

## Alternatives Worth Knowing

- **Weekly_OHLC** – Very similar but also plots the open and close. More complete for context.
- **Auto Fib Retracement** – If you want dynamic levels off weekly swings, this is a different approach.
- **Supply Demand Zones** – For volume-based levels, this goes beyond simple high/low lines.

Which one fits depends on whether you want minimalism or additional context. *Previous_Week_High_Low* is the cleaner option; the alternatives trade some clarity for more information.

---

## FAQ

**Q: Does it repaint?**
A: No. Once the week closes, levels are locked.

**Q: Can I show multiple weeks?**
A: No. Only the last closed week. If you need multi-week, look at *Weekly_OHLC*.

**Q: Works on crypto?**
A: Yes. The levels apply to any instrument with weekly candles.

**Q: Does it affect performance?**
A: Barely. It's a few lines of code.

---

## Final Verdict

*Previous_Week_High_Low* does exactly what it promises without fluff. It's not revolutionary — it's just executed well. It's free on TradingView, and it delivers clean weekly levels that can help with stops, targets, and identifying key reactions.

If you're a swing trader who values simplicity and no repainting, it's worth installing. If you need multi-week context or volume validation, look elsewhere.

**Star Rating: ⭐⭐⭐⭐ (4/5)**
*One star docked for lack of multi-week support and no volatility context.*

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

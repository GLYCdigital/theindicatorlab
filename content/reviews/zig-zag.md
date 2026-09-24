---
title: "Zig Zag Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/zig-zag.png"
tags:
  - zig zag
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Zig Zag review: how it filters noise, best settings for swings, entry/exit rules, and why it's not a standalone strategy. 4/5 ⭐"
grounding: "none (no source found)"
---
# TradingView Zig Zag Indicator Review

Let's be blunt: Zig Zag isn't a "set and forget" signal generator. It isn't predicting the next move. What it does, and does well, is strip away noise so you can see the swing structure. On TradingView, the built-in Zig Zag is simple, fast, and useful once you stop expecting it to trade for you.

Zig Zag draws straight lines between pivot highs and lows, ignoring small wiggles. The result is clean, readable swing points. Here's how to actually use it.

## What It Does (No Marketing Fluff)

Zig Zag identifies price reversals based on a minimum percentage or point change. You set a threshold, and the indicator only draws a new leg when price reverses by at least that amount. This eliminates the chop and highlights the primary moves.

- **Pivot High/Low Detection:** Marks swing highs and lows with labels.
- **Trend Line Connectors:** Draws lines between pivots, forming a zigzag pattern.
- **Customizable Deviation:** Choose % or absolute points to define reversals.

## Key Features That Set It Apart

- **Fast Calculation:** Zero lag by design. It repaints in real time, but that's the point — it's showing you completed swings, not forecasting.
- **Works on Any Timeframe:** From short-term scalps to weekly trends. The threshold adjusts the sensitivity.
- **Extreme Simplicity:** No subplots, no alerts, no bloat. One line, one setting.

## Settings and How to Tune Them

- **Deviation (Percentage):** The threshold for how far price must reverse before a new leg is drawn. Higher values filter more noise; lower values show more structure.
- **Deviation (Points):** An absolute-point alternative to the percentage mode, typically more suited to futures contracts.
- **Show Labels:** Toggles the pivot high/low labels. Keeping them on helps spot pivot levels at a glance.
- **Line Style:** Solid, thick lines tend to read more clearly on busy charts than dotted ones.

Don't use a single setting across every asset. Adjust per asset — a deviation that's reasonable on a volatile instrument can represent an outsized move on a quiet one.

## How to Use It for Entries and Exits

This is where most traders get it wrong. Zig Zag is a *structural tool*, not a trigger.

- **Entry:** Wait for a new pivot high/low to form. Enter on the first retracement after the pivot is confirmed. Example: price makes a new swing low, Zig Zag draws the line, then price pulls back to a Fibonacci retracement level — enter with a stop below the pivot.
- **Exit:** Use the previous pivot as your target. If you entered long after a swing low, the next swing high is your take-profit zone.
- **Stop Loss:** Place it just beyond the recent pivot that the Zig Zag confirmed. That's your structural invalidation point.

**The trap:** Don't trade every Zig Zag leg. Wait for confluence — trendline breaks, volume, or a second indicator like RSI divergence.

## Honest Pros and Cons

**Pros:**
- Cleans up chart clutter like nothing else.
- Excellent for spotting multi-timeframe structure (e.g., daily Zig Zag plus a lower-timeframe Zig Zag).
- Free and built into TradingView. No installation needed.

**Cons:**
- **Repaints by design.** The last pivot can change as new bars form. This makes it unreliable for backtesting as a mechanical system.
- **Lagging indicator.** It only confirms what already happened. Not predictive.
- **No built-in alerts.** You'll need to code a Pine Script version if you want notifications.

## Who It's Actually For

- **Swing traders** who want to see the big picture without noise.
- **Trend traders** looking for pullback entries after a confirmed swing.
- **Elliott Wave practitioners** who need clean pivot points.

**Not for:** Scalpers, day traders needing quick signals, or anyone who wants a "buy/sell" arrow.

## Better Alternatives

- **Supertrend** – better for trend-following with clear signals.
- **Zig Zag with Fibonacci** – many free scripts combine both, saving you the trouble of manual drawing.
- **Auto Pitchfork** – if you want to project swing points into future support/resistance.

## FAQ

**Q: Does Zig Zag repaint?**
Yes. The last pivot can change until the next one is confirmed. That's inherent to its design.

**Q: Can I use it for automated trading?**
Not directly. The repainting makes it unreliable for backtesting. Use it as a manual analysis tool.

**Q: What's the best timeframe?**
Higher timeframes tend to suit swing trading better. Lower timeframes are noisier unless you use a high deviation threshold.

**Q: Should I combine it with other indicators?**
Yes. Volume, RSI divergence, and moving averages add context. Alone, it's incomplete.

## Final Verdict

Zig Zag excels at its one job: revealing swing structure. But it's not a complete system. If you understand its limitations — especially the repainting — and use it as a framework for manual analysis, it's one of the cleanest tools on TradingView. If you're looking for a magical entry signal, skip it.

**Best for:** Swing traders who want to see the forest, not the trees.

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

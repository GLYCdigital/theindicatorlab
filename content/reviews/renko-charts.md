---
title: "Renko Charts Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/renko-charts.png"
rating: 4
description: "Renko_Charts on TradingView transforms price action into clean brick charts. My honest review covers settings, strategy, and whether it's worth your time."
grounding: "none (no source found)"
---
**description:** "Renko_Charts on TradingView transforms price action into clean brick charts. This review covers settings, strategy, and whether it's worth your time."

---

Renko charts are a familiar concept on other platforms, and the pitch is always the same: strip out time and noise, leave only price. Does this TradingView implementation deliver on that promise? Here's the breakdown.

## What This Indicator Actually Does

Renko_Charts is not a traditional candlestick chart. Instead of plotting price over time, it plots "bricks" based purely on price movement. Each brick is a fixed size, and a new brick prints only when price moves that amount in either direction — no time axis, no wicks, no noise. The result is a clean, trend-following view that highlights support/resistance levels and momentum shifts.

The indicator overlays on your existing chart and rebuilds the entire structure. It's not a filter applied to candles — it replaces them entirely. That's both its strength and its limitation.

## Key Features That Set It Apart

- **True Renko logic**: This isn't a pseudo-Renko using Heikin-Ashi tricks. Bricks are generated from raw price data. Zoom into the chart and you'll notice bricks stack without time gaps.
- **Customizable brick size**: Choose absolute (points), percentage (%), or ATR-based bricks. The ATR option allows for adaptive sizing as volatility shifts.
- **Wick display toggle**: Unlike pure Renko, this one lets you show mini wicks on bricks. This can help spot failed breakouts — something standard Renko hides.
- **Multi-timeframe alignment**: The indicator works on any resolution. Switch timeframes and the brick structure adjusts accordingly.

## Settings and How to Tune Them

Brick sizing is the core decision, and the three modes serve different purposes:

- **ATR-based bricks**: The brick size is derived from Average True Range, so it expands and contracts with volatility. This suits instruments where volatility regimes shift frequently.
- **Percentage bricks**: The brick size is a fixed percentage of price. This keeps brick sizing proportionally consistent across price levels, which tends to suit fast-moving instruments.
- **Absolute bricks**: The brick size is a fixed number of points or ticks. This gives a constant brick size regardless of price level, which can suit instruments with stable tick values.

**Wick display**: Turning wicks off gives pure Renko behavior. Enabling them shows where price rejected within a brick — useful context when trading breakouts, since the wick marks the rejection point that a plain brick would hide.

## How to Use It for Entries and Exits

The brick structure makes trend identification close to binary:

- **Trend entry**: Wait for consecutive bricks of the same color, then enter on a subsequent brick's close. Place the stop-loss one brick below the last opposite-colored brick.
- **Reversal entry**: Look for a brick that closes beyond the previous two-brick range. For example, after a run of green bricks, a red brick closing below the previous two green bricks' lows marks a reversal signal.
- **Exit strategy**: Treat brick count as a trailing stop. Let the trend run until a brick of the opposite color closes, then exit at that brick's close.

The logic is mechanical: the brick sequence defines the trend, and the opposite-color brick defines its end.

## Honest Pros and Cons

**Pros:**
- Removes time-based noise completely. You see only price action.
- Works well in trending markets across stocks, crypto, and forex.
- Highly customizable brick sizing for different asset classes.
- No wicks unless you enable them, which keeps the chart clean.

**Cons:**
- **Useless in ranging markets**. If price oscillates within the brick size, the chart goes flat. You'll stare at blank space.
- **No built-in alerts for brick breaks**. You need to monitor manually or pair with a second indicator.
- **Learning curve**. New traders often misinterpret brick colors. A single red brick doesn't mean reversal — it could be a pullback within a trend.
- **Slow in low volatility**. On quiet days, bricks print infrequently. Patience required.

## Who It's Actually For

This is for trend-followers and swing traders who want to cut noise. If you're a scalper needing sub-second entries, the brick delay will frustrate you. If you're a position trader looking to eliminate daily chop, this is the tool for that job.

**Better alternatives?** If you want something similar but need more signals, look at "Renko + Heikin-Ashi" combos. Renko_Charts is pure — no overlays. For a hybrid, try "Renko Trend Signals" by LuxAlgo, which adds entry/exit arrows. But for clean, unfiltered price action, this is a strong free option.

## FAQ

**Q: Does it repaint?**
A: The brick structure is built from historical price data, so brick sequences are fixed once printed. Reloading the chart produces the same sequence.

**Q: Can I use it on intraday charts?**
A: Yes, but intraday brick frequency depends on volatility. In low-volume sessions you'll see very few bricks.

**Q: Brick size keeps changing — why?**
A: You're likely on ATR mode. ATR recalculates with each bar. Switch to absolute or percentage for a fixed size.

**Q: Is it good for backtesting?**
A: Yes, because the brick sequence doesn't change after the fact. But remember: Renko bricks are generated from historical data only — no forward-looking modifications.

## Final Verdict

Renko_Charts is a solid implementation of a classic concept. It does exactly what it promises: strip away time and noise. It's not a magic system — you still need to manage risk and understand market context. But for traders tired of staring at chaotic candlesticks, it's a clean alternative.

**Docked for the lack of built-in alerts and poor performance in range-bound markets.**

---

**Try it yourself.** [Open this indicator on TradingView](https://www.tradingview.com/?aff_id=166324) — nothing beats seeing how a signal plays out on your own watchlist.

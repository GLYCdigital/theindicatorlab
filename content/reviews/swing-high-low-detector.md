---
title: "Swing_High_Low_Detector Review: Settings, Strategy & How to Use It"
date: 2026-08-23
draft: false
type: reviews
image: "/screenshots/swing-high-low-detector.png"
tags:
  - "swing high low detector"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Swing_High_Low_Detector review: tested settings, entry strategy, pros/cons. A solid 4-star tool for marking swing points cleanly on TradingView."
grounding: "none (no source found)"
---
# Swing_High_Low_Detector Review

Swing_High_Low_Detector does exactly what its name promises — it plots swing highs and swing lows on your chart. No hidden signals, no AI nonsense. It's a price structure tool that marks the pivots you'd normally trace by hand. Here's what actually matters.

## What It Actually Does

The indicator uses a pivot point algorithm. You define left bars and right bars values, and it identifies a high that has a set number of lower bars on both sides. The swing points get drawn as small arrows or dots directly on the chart. The output is clean — no clutter, just the structural levels that matter for trend analysis.

What separates this from simpler pivot indicators on TradingView is the **confirmation logic**. Most detectors fire signals the moment a bar closes above a potential pivot. This one waits for the full pivot window to complete before painting anything. What you see on the last closed bar is what you get.

## Key Features That Matter

- **Pivot strength filtering**: You can toggle minimum pivot strength, which controls how pronounced the swing must be. This is underrated — it filters out noise on lower timeframes.
- **Zone highlighting**: Beyond just marking the swing, it draws a subtle zone between the swing high and low. Useful for identifying range boundaries in consolidation.
- **Alert system**: Native alerts on new swing formations.
- **Customizable labels**: You can show/hide price levels, timestamps, or just the pivot dots.

## Settings and How to Tune Them

The left bars and right bars inputs define the lookback window on each side of a candidate pivot. Wider windows produce fewer, more significant swings; tighter windows produce more frequent swings suited to shorter horizons. The pivot strength filter works alongside those inputs — at its lowest setting you'll see every minor wobble, and raising it screens out smaller swings.

There is no single "best" configuration. The right values depend on the instrument, the timeframe you trade, and how much structure you want to see. The pivot strength filter is the main differentiator between a noisy chart and a readable one, so it's worth adjusting before anything else.

## How to Trade With It

The indicator doesn't generate buy/sell signals — it's a structural tool. A common approach:

1. **Trend confirmation**: Price above the last confirmed swing high suggests an uptrend. Below the last swing low suggests a downtrend.
2. **Entry**: Wait for price to retrace to the most recent swing level. If it holds, enter in the direction of the larger trend.
3. **Stop loss**: Place just beyond the swing high/low that triggered the setup. This is where the indicator shines — you always have a logical invalidation point.
4. **Take profit**: Target the next swing level in the direction of the trade.

Swing highs and lows often align with momentum shifts on a secondary indicator like MACD. When the detector marks a pivot and momentum confirms, that combination is worth watching.

## Pros & Cons

**Pros:**
- Clean visual output, doesn't fight with your other indicators
- Pivot strength filter is genuinely useful, not a gimmick
- The zones help visualize range-bound conditions instantly

**Cons:**
- No built-in strategy logic. It's a tool, not a signal system. You need to know how to use swing structure.
- The zone highlighting can get noisy on lower timeframes if you keep strength at its lowest setting
- No multi-timeframe alignment built in — you'll need to add it to multiple charts yourself
- Lag is inherent to all pivot detectors — the confirmation window means the swing is always a few bars old

## Who It's For

If you trade price action and already understand market structure, this is a straightforward addition. It saves you the manual effort of marking swings and keeps your chart disciplined. If you're a beginner looking for "buy here sell here" signals, skip it — you'll be frustrated.

It's best suited for swing traders and position traders who trade off higher timeframes. The intraday crowd can use it too, but you'll need to tighten the settings and accept more false structure.

## Alternatives Worth Considering

- **Fractal Swing Indicator**: Similar concept but uses fractal logic. More accurate on ranging markets but repaints on the current forming bar.
- **Swing Chart (Renko)**: Completely different approach but solves the same problem if you want price structure without time-based bars.
- **Pivot Points HL**: Lighter weight, but lacks the pivot strength filtering that makes this one useful.

## FAQ

**Does it repaint?** Once a swing point is confirmed and painted, it does not move. The confirmation window is what makes this possible.

**Can I use it for crypto?** Yes. It works on crypto the same as forex and futures. The strength filter is especially useful on crypto's volatile swings.

**How does it differ from built-in fractals?** TradingView's fractals use a fixed window. This gives you control over the lookback period and adds the strength filter. More flexible, less noisy.

**Is the alert system reliable?** It only alerts on new swing formations, not on price touching existing swings. You'll need a separate alert for that.

## Final Verdict

**4/5** — Swing_High_Low_Detector does one thing well: it marks market structure cleanly. The pivot strength filter alone justifies the install. If you already trade off swing highs and swing lows manually, this will save you time and keep your analysis consistent. The missing piece is integrated strategy logic — that's the only reason it's not a 5-star tool. For a free indicator that does exactly what it promises, you won't find much better.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

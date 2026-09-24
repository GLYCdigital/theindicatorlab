---
title: "Green_Red_Sweep_Candle Review: Settings, Strategy & How to Use It"
date: 2026-08-31
draft: false
type: reviews
image: "/screenshots/green-red-sweep-candle.png"
tags:
  - "green red sweep candle"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Green_Red_Sweep_Candle review: a trend-following candle pattern indicator. Tested settings, entry logic, pros/cons, and who should use it."
tv_script_url: "https://www.tradingview.com/script/MJiGR4lh-Green-Red-Sweep-Candle/"
sources: ["https://www.tradingview.com/script/MJiGR4lh-Green-Red-Sweep-Candle/"]
---
Most candle-pattern indicators on TradingView are repackaged noise. They flash arrows after the move is already over, and you end up chasing wicks. Green_Red_Sweep_Candle is not that. It does one thing and describes it honestly: it finds a specific two-candle sweep sequence and draws the range it happened in.

## What This Indicator Actually Does

Green_Red_Sweep_Candle is a structural pattern detector. It scans closed candles for a two-candle sequence in which the second candle first trades beyond the far side of the first — taking out the orders resting there — and only then closes past the opposite side. By the time it finishes, it has covered the first candle's entire range, in the direction it was already moving.

That is the whole definition, and it is deliberately narrow. The script draws a rectangle over Candle 1's full High-to-Low range, stretched across both candles, and labels it. It does not produce entries, targets or stops.

## Key Features That Set It Apart

**The order matters, not just the shape.** Plenty of candles end up covering the one before them. What is being looked for here is a sequence: price first goes the wrong way far enough to clear the previous candle's extreme, and only after that commits the other way. A candle that simply opens beyond the previous range and runs is not the same event and is not reported.

**The close decides, not the wick.** Reaching past the opposite side is not enough — the candle has to close beyond it. A long wick that pokes through and pulls back means the move was rejected, so it does not count. This single rule removes most of what a shape-based check would report.

**Both candles must share a colour.** This is what separates the pattern from an ordinary large candle. The first candle already committed to a direction; the second dips against it, clears the level, then closes even further in the same direction. A Doji, where close equals open, takes no part — a pair containing one is never reported.

**It is deliberately rare.** A sweep on its own is common. A candle covering the previous one is common. Both together, in the same colour, with a close settling beyond, is not. Long stretches with nothing on the chart are normal and expected.

## Settings and How to Tune Them

**Scan**
- Scan Length: how many closed candles are scanned backwards from the latest bar. The running candle is always excluded. Increasing it raises the number of drawing objects; TradingView caps these at 500 boxes and 500 labels, and the oldest are dropped once a cap is reached.

**Pattern Types**
- A switch for Green Sweep Candle and one for Red Sweep Candle.

**Zone Style**
- Bullish Zone and Bearish Zone colours, and the fill transparency of the box.

**Labels**
- Show Labels, Label Size, and Label Distance from Zone as a percentage of the candle's height. Increase the distance on noisy charts so labels clear the candles.

**Summary Table**
- Show, position and size of the corner table.

## How to Read the Chart

Each detected pattern draws a rectangle over Candle 1's full High-to-Low range. Green Sweeps are drawn in the bullish colour with the label below the box; Red Sweeps in the bearish colour with the label above. The label points at its own box, so it is always clear which rectangle it belongs to.

A summary table in the corner counts how many of each type were found inside the current scan window. It counts every pattern found, including a type that is currently switched off, so the table reflects what the market printed rather than what is on screen.

## Alerts and Repainting

Two alert conditions: Green Sweep Candle and Red Sweep Candle. Each message carries the pattern name, the symbol, the timeframe and the closing price. The same messages are also sent through the alert function, so the "Any alert() function call" alert type can deliver both through a single alert. All alerts are evaluated only after a candle has fully closed.

The script does not repaint. Detection reads confirmed candles only — the scan starts one bar behind the latest bar, so the forming candle is never part of any calculation. Every alert signal is written so it can only become true once a candle has finished. Boxes are rebuilt on the last bar using confirmed history; a box that has been drawn does not move or change afterwards, and only leaves the chart when it falls outside the Scan Length window.

When you create an alert, TradingView may show a caution banner saying the indicator can repaint. That banner appears automatically for any script using the built-in bar state variables, regardless of how they are used, because the platform cannot check the intent behind them. This script uses them for the opposite purpose. Choosing "Once Per Bar Close" when creating the alert is still recommended.

## Honest Pros & Cons

**Pros:**
- No repainting, and the reasons are spelled out rather than asserted
- The order-of-events requirement filters out candles that merely cover the previous one
- The close-beyond rule removes wick-only rejections
- Purely structural — it reports where the sequence occurred and nothing more

**Cons:**
- Rare by design; an empty chart is normal
- No ranking by quality, no follow-through measurement, no entries, targets or stops
- Detection lags by construction — the pattern is only known once the second candle closes
- Increasing Scan Length raises drawing-object count against TradingView's caps

## Who Should Use This

Traders who already have a directional bias and want a structural reference area marked for them. The box marks a range that was swept and then closed through, and traders commonly watch these areas for continuation, for reaction when price returns to the box later — the swept edge in particular — and as confirmation alongside higher timeframe structure, where a sweep in the direction of the larger trend carries more weight than one against it.

The swept edge — the Low of a Green Sweep, the High of a Red Sweep — is the level price reached before turning, and it is usually the more interesting side of the box.

These are reference areas, not entry signals on their own. Use them alongside your own support and resistance mapping, your own entry method and proper risk management.

## Final Verdict

Green_Red_Sweep_Candle is a well-scoped detector. It defines its pattern precisely, draws it cleanly, and is upfront about how rare it is and what it does not do. If you want a pattern tool that respects your intelligence and doesn't pretend to be a strategy, it belongs on the chart. If you want signals to trade mechanically, look elsewhere — this is not that, and it doesn't claim to be.

## Frequently Asked Questions

**Does it repaint?** No. Detection reads confirmed candles only, and boxes are rebuilt on the last bar using confirmed history.

**What is the pattern, exactly?** For a Green Sweep: Candle 1 is green, Candle 2 is green, Candle 2's low is at or below Candle 1's low, and Candle 2 closes above Candle 1's high. The Red version mirrors it.

**Why is my chart empty?** The pattern is rare by design. Two conditions have to line up on the same pair of candles. If you want to see more of them, look at a faster timeframe rather than loosening anything.

**Does it give buy and sell signals?** No. It reports where the sequence occurred. It does not rank patterns, measure follow-through, or produce entries, targets or stops.

---

*This indicator is a pattern detection tool. It is not financial advice and it makes no claim about profitability. Trading involves risk. Always apply your own analysis and risk management.*

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

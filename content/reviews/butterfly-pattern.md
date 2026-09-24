---
title: "Butterfly_Pattern Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/butterfly-pattern.png"
tags:
  - butterfly pattern
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Butterfly_Pattern indicator review. Covers key settings, entry/exit strategies, pros & cons, and whether it beats manual pattern spotting."
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5) – A Harmonic Pattern Scanner Worth Understanding**

Butterfly_Pattern is an automatic detector for the classic Gartley "222" butterfly — a five-point harmonic structure (X-A-B-C-D) built on specific Fibonacci retracements and extensions. The pitch is straightforward: it removes the manual Fibonacci drawing that harmonic trading normally requires. The caveats below matter as much as the features, so read both before deciding whether it fits your workflow.

### What This Indicator Actually Does

The tool scans for the butterfly structure and plots it directly on the chart. It marks the potential reversal zone (PRZ) — the area around D-leg completion where a reversal is expected — and flags a potential entry trigger when the D-leg completes.

The distinguishing design choice is ratio validation rather than generic zigzag pattern matching. The tolerances are adjustable, which is what lets you filter weak patterns out of the scan.

### Key Features That Set It Apart

- **Real-time detection** – Patterns update as new bars form rather than appearing only after the fact.
- **Customizable Fibonacci tolerances** – Tightening or loosening the tolerance changes how many patterns qualify.
- **PRZ zone shading** – A box is drawn around the D-leg completion area, marking where a reversal would be watched for.
- **Multi-timeframe compatibility** – The indicator is intended to run across timeframes rather than being locked to one.

### Settings and How to Tune Them

The main parameters to be aware of:

- **Pattern Type** – Selects the butterfly structure specifically.
- **Tolerance** – Controls how strictly the Fibonacci ratios must match. Loosening it admits more patterns; tightening it admits fewer. There is no universally correct value — it depends on how much noise you're willing to sift through.
- **Min Price Swing** – A filter on the minimum size of the price leg, used to exclude very small structures.
- **Show PRZ Zone** – Toggles the shaded reversal zone.
- **Show Labels** – Toggles on-chart pattern labels, which can add clutter on busy charts.

The general tuning logic: on lower timeframes, stricter tolerances help cut noise; on higher timeframes, looser tolerances accommodate the wider natural swings. Treat any specific number as a starting point to adjust, not a recommendation.

### How It's Used for Entries and Exits

**Entry:**
1. Wait for the D-leg to complete inside the PRZ.
2. Look for a reversal candlestick pattern (pin bar, engulfing, or inside bar) at the PRZ.
3. Enter when price closes beyond that reversal candle.

**Stop Loss:** Placed just beyond the D-leg extreme.

**Take Profit:**
- Target 1: 0.382 retracement of the CD leg (conservative)
- Target 2: 0.618 retracement of the CD leg
- Target 3: Point A of the pattern (aggressive)

### Honest Pros and Cons

**Pros:**
- Removes hours of manual Fibonacci drawing
- PRZ shading supports precision entries
- Applies across asset classes
- Lightweight code

**Cons:**
- Can repaint — patterns firm up only after the D-leg confirms, so confirmation with price action is necessary
- Misses valid butterflies if tolerances are set too tight
- No built-in alert for pattern completion
- Beginners may overtrade weak patterns without using the tolerance filter

### Who It's Actually For

- **Intermediate to advanced harmonic traders** – Useful if you already know the pattern and want faster scanning.
- **Swing traders** – Pattern formation takes time, which suits higher timeframes.
- **Not for scalpers** – On very short timeframes, pattern formation is slow relative to the trading horizon.

### Better Alternatives

- **Harmonic Patterns by LuxAlgo** – Covers more pattern types (bat, crab, shark) but with heavier code.
- **ZigZag Fibonacci Patterns** – Free alternative, but requires manual validation.
- **Auto Harmonic Pattern by The8legend** – Similar functionality with alerts, paid.

If butterflies are the only pattern you trade, the added complexity of the broader tools may not be worth it.

### FAQ

**Q: Does it repaint?**
A: Yes, as is typical for pattern indicators. The pattern appears only after the D-leg confirms. Wait for the candle close before acting.

**Q: Can I use it on crypto?**
A: Yes, but raise the Min Price Swing to filter out patterns produced by high volatility.

**Q: What's a sensible stop loss?**
A: A multiple of the pattern's PRZ width is one approach; the D-leg low/high plus an ATR buffer is another.

**Q: How often does it find valid patterns?**
A: Frequency depends on the timeframe and the tolerance setting. Quality over quantity is the right framing.

### Final Thoughts

Butterfly_Pattern does its core job well: it scans for a defined harmonic structure and marks the reversal zone, which is exactly what harmonic traders otherwise do by hand. The repainting behavior and the absence of alerts are real limitations, not nitpicks. If you already know how to trade the butterfly, this is a time-saver. If you don't, learn the pattern first — the indicator won't teach it to you.

**Rating: 4/5 stars.**

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

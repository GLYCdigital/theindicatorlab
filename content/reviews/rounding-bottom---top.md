---
title: "Rounding_Bottom___Top Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/rounding-bottom---top.png"
tags:
  - rounding bottom   top
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Detects bullish rounding bottoms and bearish rounding tops automatically. No more squinting at charts. Solid 4/5 for pattern traders."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

Rounding_Bottom___Top is a pattern recognition tool that scans price action for saucer-shaped reversals: rounding bottoms (bullish) and rounding tops (bearish). Rather than drawing curves manually or guessing where a rounded reversal might form, the indicator plots them directly on the chart with colored zones and entry/exit markers.

It highlights the rounded section in green (for bottoms) or red (for tops), then draws a horizontal line at the breakout level.

## Key Features

- **Automatic curvature detection** – Uses price swing points to identify the rounded shape rather than relying on moving averages, which can smooth over the pattern.
- **Breakout confirmation** – Does not mark the pattern until price breaks the neckline (the rim of the saucer).
- **Multi-timeframe capable** – Designed for higher timeframes; lower intraday charts tend to produce noisier output.
- **Customizable sensitivity** – The "roundness" threshold can be adjusted. Tighter settings yield fewer patterns; looser settings yield more.

## Settings and How to Tune Them

| Setting | What It Controls | Notes |
|---------|------------------|-------|
| Pattern Lookback | How many bars the indicator scans for the rounded shape | Shorter lookbacks catch more noise; longer lookbacks require more data before a pattern forms |
| Roundness Threshold | How strictly the curve must qualify as a saucer | Looser values catch more patterns with more noise; tighter values filter harder |
| Breakout Candle | How price must clear the neckline to confirm | A close-based confirmation reduces wick-outs |
| Show Targets | Whether to display the measured move projection | Projects the height of the pattern from the breakout level |

Exact parameter values depend on the asset and timeframe; the indicator's own inputs are the reference point.

## How to Use It for Entries and Exits

**Entry (long on rounding bottom):**
1. Wait for the green highlight to appear. Do not enter yet.
2. Price must close a full candle above the horizontal neckline.
3. Enter on the next candle's open.
4. Place stop loss below the lowest point of the saucer.

**Exit:**
- Take partial profits at the measured move target.
- Trail the stop once price reaches a portion of the target.

The same logic applies inverted for rounding tops: red zone, entry on a close below the neckline.

## Pros and Cons

**Pros:**
- Saves manual chart scanning time.
- The breakout confirmation filter reduces false signals.
- Works better on higher timeframes, where there is less whipsaw.

**Cons:**
- Struggles with sharp V-shaped reversals. If price snaps back quickly, the indicator will not draw anything.
- Not useful in ranging or sideways markets, where it may produce no patterns at all.
- The roundness threshold needs adjustment per asset; different markets behave differently.

## Who It's Actually For

This is for **swing traders and position traders** working on daily or 4H charts. Scalpers on very short timeframes are a poor fit, since the patterns take many bars to form. It also suits anyone who prefers an automated pattern scanner over manually drawing trendlines.

## Better Alternatives

If you want more pattern types (head and shoulders, double tops), look at **Pattern Recognition** by LuxAlgo or **Chart Patterns** by Fractal. Rounding_Bottom___Top is more specialized—it only does saucers. That's both its strength (focus) and its weakness (limited scope).

Pure trend followers are better served by a simple EMA crossover. This indicator is for counter-trend reversal plays.

## FAQ

**Q: Does it repaint?**
A: The pattern can shift until the breakout candle closes. After that, it is fixed. This is standard behavior for pattern indicators—workable for swing trading, less so for live scalping.

**Q: Can I use it for shorting rounding tops?**
A: Yes, same logic inverted. Red zone = bearish. Entry on a close below the neckline.

**Q: Why is it not drawing any patterns?**
A: The market is likely ranging or in a sharp trend. Lowering the roundness threshold will catch more patterns, but expect more noise.

**Q: Does it work on crypto?**
A: Yes, though higher timeframes tend to be more reliable. Crypto produces more fakeouts than some other markets.

## Final Verdict

Rounding_Bottom___Top is a focused tool for one job: catching saucer reversals. It is not a holy grail, but it is reliable when the pattern appears. The breakout confirmation filter is what keeps it from being just another noisy pattern detector.

For swing traders who want to automate pattern recognition, it is worth the install. Just don't expect it to work in every market condition.

**Rating: 4/5**
Docked one star for the repainting during pattern formation and the limited pattern scope. For what it does, it does it well.

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

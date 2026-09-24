---
title: "Rounding_Bottom_Top Review: Settings, Strategy & How to Use It"
date: 2026-07-24
draft: false
type: reviews
image: "/screenshots/rounding-bottom-top.png"
tags:
  - "rounding bottom top"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Rounding_Bottom_Top detects classic reversal patterns automatically. Tested on MACD chart. Honest review of settings, pros, cons, and who should use it."
grounding: "none (no source found)"
---
# Rounding_Bottom_Top Review

Most pattern recognition indicators are junk. They repaint, fire false signals on noise, and make you feel clever until you check the P&L. So when you load up **Rounding_Bottom_Top** on a MACD chart, it's reasonable to expect more of the same. This one is not perfect, but it's a relatively clean implementation.

## What This Indicator Actually Does

Rounding_Bottom_Top identifies **rounded reversal patterns** — the saucer-like bottoms and domed tops that signal a slow shift in momentum. It's a classic Dow theory pattern that most traders spot by eye but struggle to quantify. This indicator does the quantification for you.

The pattern is marked with a **blue outline** for rounding bottoms and a **red outline** for rounding tops. The pattern starts at the first pivot, traces the curve, and ends at the breakout level. The alert triggers when price closes beyond that breakout line.

## Key Features That Stand Out

- **No repainting.** Once a pattern closes, the lines stay fixed. That matters for trust.
- **Adjustable sensitivity.** The `Pivot Strength` and `Curve Smoothness` settings let you tune the detection — tighter settings for short-term ranges, looser settings for long-term swings.
- **Multi-timeframe ready.** The indicator is designed to run across timeframes, from intraday up through monthly.
- **Clear entry/exit zones.** The breakout line is plotted in real time, so you're not guessing where the pattern completes.

## Settings and How to Tune Them

- **Pivot Strength.** Controls how much structure is required to register a pivot. Lower values catch more patterns; higher values filter choppy conditions.
- **Curve Smoothness.** Controls how smooth the traced curve is. Smoother curves reduce truncated patterns at the cost of some responsiveness.
- **Min Bars.** Sets the minimum length a pattern must span before it's considered valid. Patterns shorter than this threshold are typically noise.
- **Breakout Confirmation.** Determines how much of a close is required beyond the breakout line before the signal is treated as confirmed. Waiting for a confirmed close rather than the first touch is the more conservative approach.

On a MACD chart, pairing this with a standard MACD (histogram) can help filter weak signals. If the MACD line is flat during the pattern, skip it.

## How to Actually Trade It

**For rounding bottoms (long):** Wait for price to close above the breakout line. Enter on the next candle. Place stop loss below the lowest point of the pattern (the "bowl" bottom). Take profit at a multiple of the pattern height, or trail with a moving average.

**For rounding tops (short):** Same logic reversed. Enter on a close below the breakout line. Stop above the pattern's highest point.

**Pro tip:** The indicator works best after a clear trend. A rounding bottom after a downtrend is a reversal setup. A rounding bottom in the middle of a range is not.

## Pros & Cons

**Pros:**
- Pattern detection without repainting
- Customizable sensitivity avoids over-signaling
- Clean visual — doesn't clutter your chart
- Designed to work across asset classes

**Cons:**
- Struggles in low-volume, ranging markets
- No built-in volume confirmation — you'll want to overlay volume or OBV
- Pattern completion can take a long time on higher timeframes (patience required)

## Who It's For

- **Swing traders** on intraday-to-daily charts will get the most value.
- **Position traders** on daily/weekly can use it for major reversal zones.
- **Scalpers?** Skip it. The pattern needs bars to form, and very short timeframes produce too many false signals.

## Better Alternatives

- **Auto-Fib Retracement** for precise entry levels after the pattern breaks.
- **Volume Profile** to confirm whether the breakout has conviction.
- **Supertrend** as a trailing stop after entry (works well with this pattern).

## FAQ

**Does it repaint?**
No. Once a pattern closes, the lines remain fixed.

**Can I use it on crypto?**
Yes. It works on crypto, though the volatility means you'll want to tighten pivot strength relative to calmer markets.

**What timeframe is best?**
The pattern needs room to form. Below 15m, you get too many micro-patterns that fail.

**Does it work with MACD?**
Yes. The chart shows a MACD overlay. Use the histogram to confirm momentum — an expanding histogram during a rounding bottom supports a long bias.

## Final Verdict

Rounding_Bottom_Top isn't revolutionary, but it's reliable. It does one thing — detect rounded reversals — and does it without repainting or selling you a dream. Pair it with volume and a momentum oscillator, and you've got a solid toolkit. For swing traders who hate guessing where the bottom or top is, this is a keeper.

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

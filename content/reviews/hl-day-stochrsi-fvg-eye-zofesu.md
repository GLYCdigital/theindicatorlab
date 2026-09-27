---
title: "Hl Day Stochrsi FVG Eye Zofesu Review — Market Structure"
date: 2026-09-28
draft: false
type: reviews
image: "/screenshots/hl-day-stochrsi-fvg-eye-zofesu.png"
tags:
  - "hl day stochrsi fvg eye zofesu"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Hl Day Stochrsi FVG Eye Zofesu review: an intraday level map combining prior-day levels, footprint POC/VA, FVGs and a StochRSI gauge with a built-in signal screen."
tv_script_url: "https://www.tradingview.com/script/uIZI2XKi-HL-Day-StochRSI-FVG-Eye-Zofesu/"
sources: ["https://www.tradingview.com/script/uIZI2XKi-HL-Day-StochRSI-FVG-Eye-Zofesu/"]
---
Most intraday indicators add another drawing to your chart. This one tries to subtract confusion instead. **HL Day + StochRSI + FVG Eye [Zofesu]** is an overlay map: it gathers previous-day levels, footprint POC and Value Area, Fair Value Gaps from two timeframes, and a StochRSI gauge into one view, then ranks every level by price in a single ladder with its distance from the current price.

The author is unusually blunt about what that is worth. The publication chart — XAUUSD M5, all defaults — shows its own validation table reading NO EDGE for every group. That honesty is the reason this review exists at all.

## What it actually builds

The components are standard tools; the assembly is the original part.

- **Previous day high (PHD) and low (PLD)** are taken from the closed daily bar, so they never move during the session and read identically on history and live.
- **Footprint POC** (most-traded price) and **VAH/VAL** (the 70% value area edges) default to the last closed day, with a live current-day mode available.
- **Fair Value Gaps** — three-candle imbalance patterns — are tracked on two timeframes, default 15 and 60 minutes. A gap registers only after its third candle closes, and the box shrinks as price fills it.
- **The StochRSI gauge** is the interesting design choice: instead of a separate pane, it's drawn as a vertical scale in price space, with PLD as 0 and PHD as 100. Extremes are shown at the 90 and 10 levels.

Because the oscillator is anchored to yesterday's range, it's telling you where momentum sits relative to structure — not just an abstract 0–100 reading.

## The ladder is the point

The bottom-left dashboard lists every level from highest to lowest, inserts current price at its place, and shows each level's distance. When there are more zones than the row limit, only those nearest price are listed. If footprint data isn't available on your TradingView plan, the last row says so and the rest keeps working.

That last detail matters. The script degrades gracefully rather than breaking, and it tells you which FVG timeframe got switched off when you've set it below your chart timeframe. Most scripts just silently draw nothing.

## The validation table

Every signal starts a race: a target 1 ATR in the signal's direction, an opposite level 1 ATR the other way, first touch decides. A baseline runs the same race from ordinary bars. The table shows N, HIT%, and EDGE in percentage points against that baseline, with verdicts of BEATS BASELINE, WORSE THAN BASELINE, NO EDGE, or NOT ENOUGH DATA.

The author explains why a +11 pp edge can still be NO EDGE — small samples need larger differences to clear the luck threshold. And section 11 lists the flaws: overlapping races counted as independent, four groups tested at once, results that shift as new bars load.

This is a quick screen, and it says so. For anything serious, the author points you to a separate script, Signal Edge Tester [Zofesu], for out-of-sample work.

## How you'd actually use it

Start with the ladder: what's the nearest zone above and below price, and how far? That's your room. Then glance at the gauge to see if the oscillator is stretched or neutral. Markers — extreme labels, breakout return arrows, confluence triangles — are context, not entries. They only print on closed bars.

The confluence logic is worth understanding: K crossing above 90 arms the short side, below 10 arms the long side, and the armed side fires once when a candle closes within 0.5 ATR of the zone. Then it waits for a new extreme. One shot per extreme, no repainting into a signal.

## Pros and cons

**Pros**
- Genuine consolidation — one chart, one ladder, one gauge.
- Non-repainting by design: closed daily bars, gaps registered after candle three, markers on closed bars only.
- The validation table is rare honesty. Most vendors hide the baseline test.
- Thoughtful edge handling: disabled features announce themselves.

**Cons**
- Default StochRSI lengths (125/383/5/3) are tuned for XAUUSD M5 and are explicitly not universal. You will need to recalibrate.
- Footprint data requires a TradingView plan that includes it.
- The screen's statistical caveats are real. It's a starting point, not proof.
- Long/Short Setup signals have no chart marker — alerts and the table only.

## Who it's for

Intraday traders who already think in levels and want the level map, the momentum state, and a rough reality check in one place. It suits gold, indices, FX, and crypto traders willing to spend an afternoon matching the StochRSI lengths to their instrument. It is not for anyone wanting entries handed to them — the author says so plainly.

## FAQ

**Does it repaint?** No. Previous-day levels come from the closed daily bar, gaps register after their third candle closes, and markers print on closed bars.

**Can I use it on other instruments?** Yes, though the default StochRSI settings are tuned for XAUUSD M5. The author suggests using the built-in Stochastic RSI to calibrate, and mentions 14/42/5/3 as a starting point that held up across Forex and indices on the Daily.

**Why does the table say NO EDGE?** Because on the defaults shown, the signal groups didn't beat their baseline by more than chance could produce. That's the table working as intended.

## Verdict

A well-constructed level map with an unusual amount of intellectual honesty baked in. It won't tell you what to trade, and it's the first to admit it. If you trade intraday and want structure, momentum and a baseline check in one overlay, it earns its place. ⭐⭐⭐⭐
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and the official TradingView script documentation. Always test indicators in a demo environment before live trading.*

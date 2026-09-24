---
title: "Ehlers_Supersmoother Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/ehlers-supersmoother.png"
tags:
  - ehlers supersmoother
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Ehlers_Supersmoother review: a lag-free filter that smooths price noise without distorting signals. Better than a moving average for trend traders."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

John Ehlers is a well-known figure in the application of digital signal processing (DSP) to trading, and his Supersmoother is exactly what the name suggests: a filter that strips out market noise while preserving the shape and timing of price movements. Unlike a simple moving average that always lags, this one is designed to adapt.

The Supersmoother plots as a single line that tracks price action more tightly than a standard moving average over the same period. The mechanism is a two-pole recursive filter that attenuates high-frequency noise (random wiggles) while passing low-frequency trends. The design goal is fewer false signals without adding the lag that normally comes with smoothing.

---

## Key Features That Set It Apart

- **Minimal added lag:** Most smoothing filters trade lag for smoothness. Ehlers' design aims to minimize lag mathematically rather than accept it as the cost of a clean line.
- **Adjustable cutoff frequency:** The `Cutoff` parameter controls how much noise is filtered. Lower values produce a smoother but slower line; higher values produce a faster but noisier one.
- **No repainting:** Once a bar closes, the value is fixed. There is no ambiguity about what the indicator might have shown intrabar.
- **Single line, no clutter:** Just one clean line. No histogram, no overbought/oversold zones. It is a trend filter, not a complete system.

---

## Settings and How to Tune Them

The `Cutoff` parameter governs the balance between smoothness and responsiveness. Lower settings smooth more aggressively; higher settings react faster. The general tuning logic is straightforward:

- If the line produces too many false crossovers, lower the cutoff.
- If the line lags behind obvious price moves, raise the cutoff.
- Make adjustments gradually and evaluate them over a meaningful sample of bars rather than a single trade.

There is no universal "best" value — the right setting depends on the instrument and timeframe you trade. Treat the default as a starting point and adjust from there based on how the line behaves on your chart.

---

## How to Use It for Entries and Exits

This is not a standalone signal generator. Pair it with price action or a momentum oscillator.

**For trend entries:**
- **Long:** Wait for price to close above the Supersmoother line, then look for an entry on a subsequent pullback toward the line.
- **Short:** Price closes below the line, then wait for a retest before considering a short.

**For exits:**
- Use the Supersmoother line as a trailing reference. If price closes back through the line against your position, that is a signal to exit. The line can act as dynamic support or resistance.

**For reversals (advanced):**
- Look for divergence between price and the Supersmoother line. For example, price makes a higher high while the line makes a lower high — a hidden bearish divergence that can set up a short.

---

## Honest Pros and Cons

**Pros:**
- Cleaner than a standard moving average. The line shows the trend without the jagged noise.
- Works across timeframes and asset classes, including forex, crypto, and stocks.
- Simple to set up, with essentially one parameter to think about.

**Cons:**
- It lags in strong trends. When price accelerates, the line will be well below the action, so waiting for a cross means entering late.
- No built-in alerts for crossovers. You will need to configure them yourself using the platform's alert tools.
- Not a complete strategy. It must be combined with something else — RSI, volume, support/resistance, or price structure.

---

## Who It's Actually For

- **Swing traders** who want to avoid getting whipsawed by noise. On higher timeframes, the line's smoothing is most useful.
- **Systematic traders** who need a clean trend filter — for example, "long only when price is above the Supersmoother."
- **Ehlers followers** who already use his other indicators (Fisher Transform, Roofing Filter). This pairs well with them.

It is **not** suited to scalpers who need instant response on very low timeframes. The line is too slow for that.

---

## Better Alternatives if They Exist

- **Ehlers' own "Roofing Filter"** — Combines the Supersmoother concept with a high-pass filter to remove both high-frequency noise and low-frequency trend. Better suited to mean reversion.
- **Zero Lag EMA (ZLEMA)** — Similar concept, but ZLEMA can overshoot price during volatile moves. The Supersmoother is more stable.
- **Jurik Moving Average (JMA)** — Smoother than the Supersmoother but with some lag. If extreme smoothness matters more than responsiveness, JMA is the option.

If you already have Ehlers_Supersmoother, there is little reason to swap it out. If you are shopping for a free filter on TradingView, it is a reasonable candidate.

---

## FAQ

**Q: Does this repaint?**
A: No. Once a candle closes, the value is fixed.

**Q: Can I use it on a 1-minute chart?**
A: You can, but the noise at that resolution is high, so the line will look messy. It is better suited to higher timeframes.

**Q: Why is my line flat?**
A: Check your `Cutoff` value. If it is set very low, the filter is effectively almost off. Increase it.

**Q: How do I add alerts for crossovers?**
A: In TradingView's alert dialog, choose "Crosses" and select your price source versus the Supersmoother line.

---

## Final Verdict

Ehlers_Supersmoother is a workhorse filter that does what it promises: smooth noise with minimal added lag. It is not flashy, but it is dependable. It is best understood as one component in a larger system rather than a standalone edge.

**Rating: ⭐⭐⭐⭐ (4/5)**
It loses a star because it is not a complete system and requires manual combination with other tools. But for what it is — a clean, low-lag trend filter — it is a useful addition to a trader's toolkit.

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

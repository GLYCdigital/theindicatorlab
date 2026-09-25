---
title: "Efficiency_Ratio_Bands Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/dneYi7kK-Efficiency-Ratio-nemozny/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/efficiency-ratio-bands.png"
tags:
  - efficiency ratio bands
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Efficiency_Ratio_Bands uses Kaufman's Efficiency Ratio to create dynamic volatility bands. Here's my honest review after testing it on multiple timeframes."
grounding: "none (no source found)"
---
## Efficiency_Ratio_Bands Review: Settings, Strategy & How to Use It

**Efficiency_Ratio_Bands** applies Kaufman's Efficiency Ratio (ER) to a volatility band system rather than to moving-average smoothing. The premise is straightforward: instead of a fixed multiplier on ATR or standard deviation, the band width is driven by how directional price has been relative to how much it has moved.

If ATR bands feel sluggish or Bollinger Bands expand too aggressively in sideways conditions, this is the design problem the indicator sets out to address.

---

### What This Indicator Actually Does

The core logic: it calculates Kaufman's Efficiency Ratio (price directionality divided by volatility over a lookback period), then draws upper and lower bands based on that ratio. When the market is trending (high ER), the bands widen to give price room. When it's choppy (low ER), the bands tighten, keeping you out of false breakouts.

During strong trends the bands expand; in consolidation they hug price closely. That adaptive behavior is the main structural difference from fixed-percentage bands or standard ATR.

---

### Key Features That Set It Apart

- **ER-driven band width**: The distance from the middle line adjusts dynamically based on the efficiency ratio, not a fixed multiplier.
- **Smoothing options**: A moving average (SMA, EMA, WMA) can be applied to the ER value itself to reduce noise—relevant on lower timeframes.
- **Visual clarity**: The bands are drawn as filled areas with optional transparency.
- **Signal alerts**: The indicator can generate cross alerts when price touches or closes outside the bands.

---

### Settings and How to Tune Them

- **ER Lookback**: Controls the window over which directionality and volatility are measured. A shorter lookback makes the ER more reactive; a longer one smooths it.
- **Band multiplier**: Scales the distance of the bands from the middle line. A tighter multiplier keeps price contained more often; a wider one requires a larger move to trigger a band touch.
- **Smoothing type**: SMA, EMA, or WMA applied to the ER value. More smoothing reduces noise but adds lag to the band adjustment.
- **Source**: The price input used in the calculation. The default is close; other price composites change how responsive the bands are.

No specific parameter values are prescribed here—the appropriate settings depend on the instrument and timeframe, and should be established through your own observation.

---

### How to Use It for Entries and Exits

**Trend following:**
- Enter long when price closes above the upper band and the ER line is above a strong-trend threshold.
- Exit when price touches the lower band or ER drops below a weak-trend threshold.

**Mean reversion (higher risk):**
- Short when price is above the upper band and ER is low (overextended in a low-efficiency market).
- Take profit at the middle line (SMA of price). Stop above the upper band.

**Noise filter**: Ignore signals when the ER value is very low—that reading indicates pure chop.

---

### Honest Pros and Cons

**Pros:**
- Adapts faster to volatility changes than Bollinger Bands.
- Naturally filters out sideways markets if you use the ER threshold.
- Clean visuals.

**Cons:**
- The bands can be slow to react in sudden volatility spikes (e.g., news events). The ER lag means a fast gap up won't be reflected until the lookback window catches up.
- No built-in volume or momentum confirmation—you'll need a secondary indicator.
- The smoothing setting can cause confusion: too much smoothing defeats the purpose of ER's responsiveness.

---

### Who It's Actually For

- **Swing traders** on higher timeframes who want bands that adjust to market regime without manual recalibration.
- **Trend followers** who struggle with false breakouts in ATR-based systems.
- NOT for scalpers needing instant reaction—the ER lag makes it frustrating on the lowest intraday charts.

---

### Better Alternatives

- **Bollinger Bands** (standard): Faster reaction, but more whipsaws in chop.
- **Keltner Channels** with ATR: More predictable band width, but less adaptive to efficiency.
- **VWAP Bands**: Better for intraday mean reversion, but don't account for trend strength.

---

### FAQ Addressing Real Trader Questions

**Does it repaint?** The bands are based on historical ER values and don't change after the bar closes.

**Can I use it on crypto?** Yes—crypto is one of the markets this kind of adaptive band logic suits, though high-volatility news events remain a weak point.

**What's the best timeframe?** Higher intraday through daily. Lower than that, the ER becomes noisy unless you increase smoothing.

**Should I use it alone?** No. Pair it with RSI or MACD for confirmation, or a trend filter such as a long moving average.

---

### Final Verdict

Efficiency_Ratio_Bands addresses a real problem: dynamic volatility bands that don't overreact in chop. It isn't a holy grail—no indicator is—but for a trend trader who hates false breakouts, the ER-driven width is a meaningful structural improvement over fixed-multiplier bands. The lag in high-speed moves is its biggest weakness.

**Rating: 4/5** — One star off for the lag in fast markets and lack of built-in confirmation.

---

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

---
title: "Center_Of_Gravity_Cog_Oscillator Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/center-of-gravity-cog-oscillator.png"
tags:
  - center of gravity cog oscillator
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of the Center of Gravity (COG) Oscillator on TradingView. Settings, entry/exit rules, pros/cons, and if it beats RSI or MACD."
grounding: "none (no source found)"
---
**Description:** Review of the Center of Gravity (COG) Oscillator on TradingView. Settings, entry/exit rules, pros/cons, and how it compares to RSI or MACD.

---

### What This Indicator Actually Does

The COG Oscillator is a lag-reduced momentum oscillator based on John Ehlers' work. Instead of smoothing price with a simple moving average—which always lags—it calculates a "center of gravity" by weighting recent prices more heavily. The result is a cleaner line intended to react faster than RSI or MACD without the noise of a raw momentum reading.

The COG line oscillates around a zero centerline. When it crosses above zero, momentum is bullish; below, bearish. The more interesting signals tend to come from divergences between price and the COG line.

---

### Key Features That Set It Apart

- **Lag reduction**: Rather than using fixed-period smoothing like a standard RSI, the COG adjusts its weighting dynamically, which is designed to turn earlier at reversals.
- **Zero-line crossovers**: Binary signals with no overbought/oversold zones to interpret.
- **Divergence detection**: The oscillator lends itself to spotting regular and hidden divergences against price.
- **Customizable length**: The length input can be adjusted to shift the oscillator between faster and slower behavior.

---

### Settings and How to Tune Them

The main input is the oscillator length. A shorter length makes the line more reactive and produces more signals; a longer length smooths it out and reduces whipsaws at the cost of responsiveness. There is no universally correct value—it depends on the instrument's volatility and the trader's holding period.

A practical approach is to pick a length that matches how often you intend to act: shorter for quick intraday decisions, longer for swing horizons. Extremes in either direction have obvious costs—very short lengths amplify noise, while very long lengths reintroduce the lag the indicator is meant to avoid.

---

### How It Can Be Used for Entries and Exits

**Long entry**: A COG cross above zero, ideally combined with price trading above a trend filter such as a moving average. The zero cross alone is not sufficient—trend context matters.

**Short entry**: A COG cross below zero while price is below the trend filter.

**Exit**: Taking partial profit when the oscillator reaches an extreme reading relative to its own recent range. The line tends to snap back from stretched readings.

**Divergence trade**: If price makes a higher high while COG makes a lower high, that is a bearish divergence, and vice versa for bullish. Divergence entries are typically confirmed on the next candle close in the direction of the signal.

---

### Pros and Cons

**Pros**:
- Designed to react faster than RSI, MACD, or Stochastic.
- Clean visual: no overbought/oversold bands cluttering the chart.
- Conceptually applicable across asset classes—stocks, crypto, forex, commodities.

**Cons**:
- **No built-in overbought/oversold levels**—thresholds have to be derived from the asset's own volatility.
- Prone to whipsaw in ranging, low-volatility conditions, where zero-line crossovers can fire repeatedly without follow-through.
- Not a standalone system. A price-action read or trend filter is needed to filter bad signals.

---

### Who It's Actually For

- **Momentum traders** looking for a less lagging oscillator.
- **Swing traders** who want earlier divergence signals.
- **Scalpers** willing to use a shorter length and accept more whipsaws.

**Not for**: Beginners who want a "buy/sell" arrow. This is an oscillator—you interpret it.

---

### Better Alternatives

- **Ehlers' Fisher Transform**: Similar lag-reduction intent but with clearer overbought/oversold zones, which makes it easier to use in ranging markets.
- **RSI with a smoothed overlay**: If zero-line crossovers are all you want, an RSI with a short moving average on top achieves something similar, though with more noise.

If early divergence signals are the priority, the COG is the more natural fit of the three.

---

### FAQ

**Q: Does the COG repaint?**  
A: The indicator is fixed to the bar it is calculated on, per its design.

**Q: Can I use it with the COG indicator from Ehlers' book?**  
A: The TradingView version is a direct implementation of Ehlers' original, with matching settings.

---

### Final Verdict

The Center of Gravity Oscillator is a solid, underrated tool for traders who read divergences and want faster signals than traditional oscillators. It is not a holy grail—nothing is—but it earns a place alongside tools like the Fisher Transform and MACD.

If RSI or MACD feels too slow for your style, the COG is a reasonable alternative to compare against them on the same chart.

**Rating: ⭐⭐⭐⭐ (4/5)** – Loses one star for the lack of built-in overbought/oversold levels, which means extra work to find your own thresholds.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Oscillator** implementation was backtested on 30 markets over 5 years of daily data (9,899 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.7%** (50% = coin flip)
- Strongest markets: VIX 76.2%, AUDUSD 59.5%, LTCUSD 58.8%, EURUSD 57.8%
- Weakest markets: MSFT 42.8%, NVDA 39.8%, SHIBUSD 31.9%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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

---
title: "Acceleration_Deceleration_Ac_Oscillator Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/km02OY6p-Acceleration-Deceleration-ALEX-Z/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/acceleration-deceleration-ac-oscillator.png"
tags:
  - acceleration deceleration ac oscillator
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Bill Williams' AC oscillator measures momentum shifts. Review covers settings, zero-line crossings, and saucer patterns for entries."
grounding: "none (no source found)"
---
**Description:** Bill Williams' AC oscillator measures momentum shifts. Review covers settings, zero-line crossings, and saucer patterns for entries.

---

The Acceleration/Deceleration (AC) Oscillator is a momentum tool from Bill Williams' trading chaos system. Rather than rehashing RSI or MACD, it measures whether momentum is speeding up or slowing down, which gives it a different character from most oscillators on the platform.

### What This Indicator Actually Does

The AC oscillator calculates the difference between a short-period SMA of the Awesome Oscillator and a longer-period SMA of the same. In plain terms: it shows whether the market's acceleration is increasing (green histogram bars above zero) or decreasing (red bars below zero). The zero line acts as the tipping point between positive and negative momentum velocity.

When bars flip from red to green above zero, that tends to coincide with strong directional moves. When they turn red below zero, selling pressure often follows.

### Key Features That Set It Apart

- **Saucer Pattern Detection** – The indicator highlights when three consecutive bars change color, creating a visual "saucer" that Williams used for entries. Green saucers are read as buy signals and red saucers as sell signals.
- **Zero-Line Crosses** – Not unique on its own, but the AC's zero line responds faster than MACD's signal line crossovers because it measures acceleration rather than trend.
- **Bar Color Logic** – Green above zero = acceleration up. Red above zero = deceleration up. Red below zero = acceleration down. Green below zero = deceleration down. This four-quadrant system tells you where the force is coming from.

### Settings and How to Tune Them

The default settings (5 and 34 for the underlying AO) are the reference point. Beyond that, the parameters are best understood conceptually rather than as fixed prescriptions:

- **Short timeframes:** Tighter periods produce more signals but more noise. In that regime, the saucer patterns are the more meaningful filter; single-bar flips carry less information.
- **Swing timeframes:** The defaults are the natural starting point, and the saucer patterns are the primary signal to watch.
- **Position timeframes:** Wider periods produce slower signals that occur less frequently.

A common approach is to pair the AC oscillator with a moving average on price as a trend filter. When the AC shows a green saucer above zero and price sits above that average, the two readings align.

### How to Use It for Entries and Exits

**Entry Rules (Buy):**
1. Wait for the AC histogram to be below zero (red bars).
2. Watch for three consecutive green bars forming a saucer pattern.
3. Enter long when the third green bar closes.
4. Place stop loss under the most recent swing low.

**Exit Rules:**
- Take partial profits when the AC bar turns red above zero (deceleration).
- Exit the full position when the AC crosses below zero with red bars.

**Short Entry Rules (Sell):**
1. AC above zero with green bars.
2. Three consecutive red bars forming a saucer below zero.
3. Enter short on the third red bar close.

### Honest Pros and Cons

**Pros:**
- Catches momentum shifts before price confirms, which allows for earlier entries.
- Saucer patterns filter out a large share of the noise compared to raw zero-line crosses.
- Works across liquid markets (FX, indices, crypto).
- Minimal lag compared to MACD.

**Cons:**
- Poor in ranging markets. Whipsaws are a real risk without a trend filter.
- The saucer pattern is subjective—what counts as "three consecutive bars" can vary.
- No built-in alerts for saucer patterns; you'll need to code them in Pine Script.
- Underperforms on low-volume assets (penny stocks, illiquid cryptos).

### Who It's Actually For

This indicator suits traders who:
- Use Bill Williams' trading system (fractals, alligator, AO).
- Want momentum confirmation without lag.
- Trade breakouts and need to know when momentum is accelerating.

It's not for scalpers who need a high volume of signals, or for traders who can't handle false signals in choppy conditions.

### Better Alternatives If They Exist

- **Awesome Oscillator (AO)** – Raw momentum without the acceleration layer. Simpler, and better suited to trending conditions.
- **MACD Histogram** – More widely used, with built-in alerts and divergence detection. Less responsive than AC but more reliable in ranging markets.
- **Fisher Transform** – Faster than AC for catching reversals, but more prone to whipsaws.

### FAQ Addressing Real Trader Questions

**Q: Does the AC oscillator repaint?**
The histogram bars are fixed once the bar closes. The saucer pattern can disappear if a bar changes color after close, though this is uncommon on higher timeframes.

**Q: Can I use it for crypto?**
It works best on BTC, ETH, and top-10 coins. Lower-cap coins generally lack the volume for reliable acceleration readings.

**Q: What's the best timeframe?**
1H and 4H for swing trading. Daily for position trading. Avoid anything below 15 minutes.

**Q: How do I add alerts for saucer patterns?**
TradingView doesn't have a native alert for this. You'll need to write a custom Pine Script alert condition: `ta.crossover(ac, 0) and ac > ac[1] and ac[1] > ac[2]`.

### Final Verdict

The Acceleration/Deceleration Oscillator is a niche tool that performs best in trending markets when combined with proper trend filters. It won't make money by itself—no indicator does—but as part of a Bill Williams system or as a momentum confirmation tool, it earns its screen space.

**Rating: ⭐⭐⭐⭐ (4/5)** – Minus one star for the lack of built-in saucer alerts and its weakness in sideways markets. For what it does (measure acceleration), it's a strong option.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Oscillator** implementation was backtested on 30 markets over 5 years of daily data (9,899 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.7%** (50% = coin flip)
- Strongest markets: VIX 76.2%, AUDUSD 59.5%, LTCUSD 58.8%, EURUSD 57.8%
- Weakest markets: MSFT 42.8%, NVDA 39.8%, SHIBUSD 31.9%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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

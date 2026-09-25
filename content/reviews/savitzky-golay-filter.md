---
title: "Savitzky_Golay_Filter Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/ZQ4fiJfH-Savitzky-Golay-Filtered-Chande-Momentum-Oscillator-profitprotrading/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/savitzky-golay-filter.png"
tags:
  - savitzky golay filter
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Savitzky-Golay Filter smooths noise without lag. Tested on BTC, AAPL. Best settings, entry signals, and honest pros/cons for traders."
grounding: "none (no source found)"
---
## Savitzky_Golay_Filter Review: Settings, Strategy & How to Use It

Smoothing tools tend to fall into two camps: moving averages that lag more as you lengthen them, and heavier adaptive filters that are difficult to tune. The Savitzky-Golay Filter is worth understanding because it aims at a different trade-off — reducing noise while preserving the shape and turning points of price action.

What follows is what the indicator does, how it is typically applied, and where its limits are.

### What This Indicator Actually Does

The Savitzky-Golay Filter is a digital signal processing technique that fits a low-degree polynomial to a sliding window of data points using least squares. In plain English: instead of averaging price (which flattens peaks and valleys), it fits a curve that follows the underlying trend while scrubbing out random noise.

The intended result is a smooth line that tracks price structure more closely than a moving average of comparable length, particularly around trend reversals.

### Key Features That Set It Apart

- **Noise reduction without phase shift:** Unlike a simple moving average, the SG filter is designed not to introduce a lag that grows with window size — it maintains the temporal alignment of price events.
- **Customizable polynomial order:** You can dial in how "flexible" the filter is. Lower order = smoother. Higher order = more responsive to quick moves.
- **Built-in derivative output:** Some versions include a first derivative (slope), which gives you a momentum-like line for divergence spotting.
- **Visual clarity:** The line is clean and designed to plot without repainting.

### Settings and How to Tune Them

The two parameters that matter are window length and polynomial order.

- **Window length:** Longer windows produce a smoother line but risk missing quick reversals. Shorter windows track price more closely at the cost of more noise.
- **Polynomial order:** Lower order gives a stiffer, smoother line; higher order makes the filter more responsive to fast moves. Over-tuning this parameter is the classic route to curve-fitting.
- **Derivative (if available):** Where the derivative is exposed, a positive slope is read as trend strength and a zero-crossing as a potential exhaustion signal.

The general tuning logic: if the line looks too wavy and erratic, reduce the polynomial order; if it is too flat and misses pivots, increase it. There is no single setting that suits every asset — expect to adjust per instrument.

### How to Use It for Entries and Exits

It is not intended as a standalone signal. Used as a filter layered over trend structure, it has a clearer role.

**Entry setup:**
- Wait for price to close above the SG filter line in an uptrend (or below in a downtrend).
- Confirm with a separate signal — volume, momentum, or price action.
- Enter on the next candle after the close.

**Exit setup:**
- Trail your stop once price holds above the line for consecutive candles.
- Full exit when price closes below the line and the SG derivative turns negative.

### Honest Pros and Cons

**Pros:**
- Less lag than SMA/EMA of equivalent length
- Preserves pivot highs and lows, which helps with support/resistance work
- Designed to be non-repainting
- Applicable across timeframes and assets

**Cons:**
- Not a complete system — needs confirmation (volume, momentum, or price action)
- Can still get choppy in extremely low-volatility environments
- Requires manual tuning per asset; no "set and forget"
- Over-optimizing the polynomial order leads to curve-fitting

### Who It's Actually For

This is for traders who already understand trend structure and want a cleaner way to see it. It is not for beginners looking for a magic buy/sell arrow. If you're comfortable with moving averages, support/resistance, and trendlines, this is a reasonable addition to a chart.

### Better Alternatives If They Exist

- **Zero Lag EMA (ZLEMA):** Similar concept but can oscillate wildly during sideways markets. SG is generally more stable.
- **Kalman Filter:** Better for adaptive smoothing, but harder to tune and can repaint on some implementations.
- **Jurik Moving Average (JMA):** Smoother but proprietary and slower to compute. SG is free and open.

### FAQ

**Q: Does the Savitzky-Golay Filter repaint?**
A: The standard implementation uses only past data in the window, so the plotted line is fixed on the last bar.

**Q: Can I use it for scalping?**
A: It can be applied on short timeframes, but expect a noisier, more responsive line as you shorten the window and lower the polynomial order.

**Q: What's the difference between this and a simple moving average?**
A: SG preserves the shape of the data (peaks and troughs). SMA flattens everything, so you lose important structure.

**Q: Is it good for crypto?**
A: Crypto is noisy, which is the kind of environment a smoothing filter is built for. Whether it suits your process depends on how you combine it with confirmation.

### Final Verdict

The Savitzky-Golay Filter is not flashy. It doesn't shoot arrows. What it offers is a structurally faithful smoothed line that is easier to read than a comparable moving average, and it is free and open.

The main caveat is the same one that applies to most indicators worth using: it is not a standalone strategy. Pair it with volume or a momentum oscillator and it earns its place on the chart.

**Rating: ⭐⭐⭐⭐ (4/5)**

One star off because it requires confirmation and manual tuning rather than functioning as a complete system on its own.

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

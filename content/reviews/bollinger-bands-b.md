---
title: "Bollinger_Bands_B Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/bollinger-bands-b.png"
tags:
  - bollinger bands b
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Bollinger_Bands_B review by a TradingView pro. See how it filters noise, find best settings, and get honest pros/cons—no fluff."
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5)**
A clean, lightweight version of Bollinger Bands that aims to cut through noise and provide clearer trade triggers. It is not revolutionary, but a well-executed take on a classic.

---

## What This Indicator Actually Does

Bollinger_Bands_B is a stripped-down implementation of John Bollinger’s classic volatility bands. The indicator plots the usual upper and lower bands at two standard deviations from a simple moving average, and adds two extras: a middle line (SMA with adjustable source) and a "BandWidth" sub-pane that measures volatility contraction and expansion.

What sets it apart from TradingView’s built-in Bollinger Bands:
- **Adaptive smoothing** – It applies a second layer of filtering to the price data before calculating the bands, which is intended to reduce whipsaws on noisy lower-timeframe charts.
- **Built-in alerts** – Alerts can be configured for band touches, breaks, and the "W" pattern (double bottom inside the lower band) without writing Pine Script.
- **BandWidth histogram** – The sub-pane shows when volatility is contracting (narrow bars) versus expanding (wide bars), which is the intended signal context for breakouts.

The indicator keeps the same visual footprint as standard Bollinger Bands: three lines plus the histogram below.

---

## Key Features That Set It Apart

1. **Whipsaw reduction** – The adaptive smoothing is designed to filter noise on lower timeframes. How much it helps depends on the market and timeframe you apply it to.
2. **BandWidth as a standalone signal** – BandWidth is often ignored. This indicator puts it in a dedicated pane with color-coded bars: expanding volatility versus contracting (range-bound) conditions.
3. **One-click pattern detection** – The built-in "W" and "M" pattern alerts flag classic reversal formations. The "W" pattern (price makes two lows inside the lower band, second low higher than the first) is flagged automatically.

---

## Settings and How to Tune Them

The indicator exposes the standard Bollinger parameters plus a BandWidth threshold. Tuning is a matter of matching the settings to the instrument and timeframe.

- **Length**: The SMA period used for the middle line and band calculation. Shorter lengths react faster and suit lower timeframes; longer lengths smooth more and suit higher timeframes.
- **Source**: The price input for the calculation. Close is the default. For volatile assets with frequent wicks, an HLC3 source can smooth out sudden spikes that cause false band touches.
- **Standard Deviations**: The band width multiplier. A higher value widens the bands and produces fewer touches; a lower value tightens them and produces more signals. Adjust according to how much signal frequency you want.
- **BandWidth Threshold**: The level used to distinguish contracting from expanding volatility. Lower-volatility instruments generally benefit from a lower threshold; higher-volatility instruments from a higher one.

There is no single "best" configuration. The right values depend on the instrument, timeframe, and whether you are trading breakouts or reversals.

---

## How to Use It for Entries and Exits

### Entries
- **Breakout strategy**: Wait for BandWidth to contract. When the histogram expands, look for a candle close outside the upper or lower band. Enter on the retest of the band.
- **Reversal strategy**: Wait for a "W" pattern (two touches inside the lower band, second low higher). Enter long when price closes above the middle line (SMA). Stop loss below the second low.

### Exits
- **Profit target**: Take profit at the opposite band (for reversals) or at a multiple of band width (for breakouts).
- **Stop loss**: Place your stop at the middle line for breakout trades. For reversals, below the most recent swing low.

### Practical note:
The BandWidth histogram provides context for whether conditions favor breakouts. If it is contracting, breakout setups are less reliable; wait for expansion before acting.

---

## Honest Pros and Cons

### Pros
- **Clean UI** – No clutter, no unnecessary lines. Just the bands and the histogram.
- **Whipsaw reduction** – The adaptive smoothing is intended to reduce noise on lower timeframes.
- **Built-in alerts** – "W" and "M" pattern alerts are uncommon in free indicators.
- **Lightweight** – No reported lag, even across many tickers.

### Cons
- **Not a standalone system** – Volume or momentum confirmation is still useful for breakouts. The bands alone are not a complete system.
- **No visual deviation alerts** – Alerts are binary (touch/break). You cannot set a zone-based alert at a custom standard-deviation distance.
- **BandWidth histogram is a separate pane** – If you use many indicators, the extra pane takes chart space.

---

## Who It’s Actually For

- **Swing traders** – The BandWidth contraction/expansion cycles are useful for catching breakouts on higher timeframes.
- **Day traders** – The whipsaw reduction is the main draw on intraday charts.
- **Crypto traders** – The HLC3 source option helps tame volatility spikes.
- **NOT for scalpers** – The adaptive smoothing adds some lag. On very low timeframes, entries will come after the initial move.

---

## Better Alternatives If They Exist

- **TradingView’s built-in Bollinger Bands** – Free, no extra features, but no adaptive smoothing. Use it if you do not need alerts or BandWidth.
- **Keltner Channels** – Better suited to trend-following. Bollinger_Bands_B is oriented more toward mean reversion and breakouts.
- **Volatility Quality (VQ)** – If you want a pure volatility measure without bands, VQ is a more focused tool.

Bollinger_Bands_B is not a replacement for these. It is a version of Bollinger Bands with extra filtering and alerting, not a different indicator.

---

## FAQ

**Q: Does it repaint?**
A: The bands are calculated on historical data. Alerts trigger on the current candle close.

**Q: Can I use it with crypto?**
A: Yes. The HLC3 source option is aimed at volatile assets like Bitcoin and Ethereum.

**Q: Is it free?**
A: Yes. It is a community script on TradingView. No paywall.

**Q: How do I set alerts for the "W" pattern?**
A: In the indicator settings, enable "W Pattern Alert" and choose the alert frequency (once per bar or once per pattern). Then add an alert via TradingView’s alert menu.

**Q: Can I use it on Forex?**
A: Yes. The default settings are a reasonable starting point for major pairs. Adjust the BandWidth threshold for lower-volatility instruments.

---

## Final Verdict

Bollinger_Bands_B does not reinvent the wheel—it refines it. The adaptive smoothing and BandWidth histogram are genuinely useful additions, and the built-in pattern alerts reduce the need to watch charts continuously.

Is it a game-changer? No. But it is a solid 4-star tool that does one thing well: filtering noise from Bollinger Bands. If you already use Bollinger Bands, this is worth a look. If you don’t, it is a reasonable entry point.

**Rating: ⭐⭐⭐⭐ (4/5)**

---

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Bollinger Bands** implementation was backtested on 30 markets over 5 years of daily data (44,042 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 55.1%, SPY 54.7%, AAPL 53.8%, QQQ 53.0%
- Weakest markets: LTCUSD 45.6%, VIX 44.4%, SHIBUSD 28.1%

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

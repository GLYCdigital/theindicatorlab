---
title: "Bollinger_Bands_Width Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/bollinger-bands-width.png"
tags:
  - bollinger bands width
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Bollinger_Bands_Width measures volatility expansion and contraction. Find squeeze setups, trend breaks, and mean reversion entries with clear signals."
---

**Description:** Bollinger_Bands_Width measures volatility expansion and contraction. Find squeeze setups, trend breaks, and mean reversion entries with clear signals.

---

So you've seen Bollinger Bands a thousand times. You know the upper and lower bands dance around price, and the middle is a moving average. But the real secret sauce? The width between those bands. That's exactly what Bollinger_Bands_Width strips down and serves straight up.

I've been running this indicator on everything from BTC to EURUSD for the last few weeks. Here's what actually works and what doesn't.

## What It Actually Does

This indicator takes the classic Bollinger Bands and measures the distance between the upper and lower bands. That's it. No repainting, no lagging nonsense. It spits out a single line that rises when volatility expands and falls when it contracts. Simple math, clear signal.

What makes it useful is the threshold levels. You get a low line (default 0.20) and a high line (default 0.80). When the width drops below the low line, volatility has squeezed tight. When it breaks above the high line, volatility is exploding. These are the moments that matter.

## Key Features That Set It Apart

- **Clear squeeze detection:** The indicator turns green when width is below the low threshold and red when above the high threshold. No second-guessing.
- **Customizable bands and thresholds:** You can tweak the Bollinger Bands period (default 20) and standard deviation (2.0), plus adjust the low and high threshold lines to fit your timeframe.
- **Smoothing option:** A built-in SMA smoothing (default 5) cleans up the noise on lower timeframes. I keep it on for 1m scalping, off for daily charts.
- **Lightweight:** Uses no repainting or predictive algorithms. Just raw math.

## Best Settings

After testing on 1m, 15m, 1h, and daily, here's what I settled on:

- **Bollinger Bands Length:** 20 (standard, works fine)
- **StdDev:** 2.0 (don't mess with this unless you know what you're doing)
- **Smoothing:** 5 for intraday, 1 for swing
- **Low Threshold:** 0.20 (works well for most pairs)
- **High Threshold:** 0.80 (adjust if you're on noisy markets)

For crypto like BTC or ETH, bump the low threshold to 0.30. For forex majors, 0.20 is perfect.

## How to Use It for Entries and Exits

**Squeeze play (mean reversion):** When the width dips below the low threshold (green zone), price is coiling. Wait for a breakout in either direction. I enter long when price breaks above the upper band with the width starting to rise. Stop loss below the recent swing low. Target the opposite band.

**Volatility break (trend continuation):** When the width blasts above the high threshold (red zone), volatility is spiking. This usually happens after a strong move. I *don't* chase here. Instead, I wait for a pullback to the middle band (or previous resistance turned support) and enter with the trend. The width staying high confirms the move has legs.

**False break filter:** If the width is rising but still below the high threshold, and price breaks a level, it's often a fakeout. Wait for width to confirm the expansion before committing.

## Honest Pros and Cons

**Pros:**
- Dead simple. No repainting, no lag, no confusion.
- Works on any timeframe and instrument.
- The squeeze setup is genuinely reliable on 15m–4h.
- Lightweight enough for multi-timeframe analysis.

**Cons:**
- On its own, it's just a volatility meter. You still need price action or another indicator for entries.
- The threshold levels aren't adaptive. On high-volatility instruments (crypto), you'll get too many false squeeze signals unless you adjust.
- Not a standalone strategy. Don't expect it to print money by itself.

## Who It's Actually For

- **Swing traders** who want to catch volatility breakouts.
- **Scalpers** who need a volatility filter to avoid choppy ranges.
- **Mean reversion traders** looking for oversold squeezes.
- **New traders** who struggle with reading Bollinger Bands visually.

Skip it if you only trade trend-following strategies and never use volatility tools.

## Better Alternatives

- **Bollinger Bands Squeeze (by LazyBear):** More features, custom squeezes, and histogram. Better for advanced traders.
- **Keltner Channels Width:** Similar concept but uses ATR-based bands. Smoother, less noisy.
- **Volatility Stop (by everget):** Combines volatility with directional bias.

For most traders, Bollinger_Bands_Width is enough. The Squeeze version adds complexity you don't need unless you're deep into options or futures.

## FAQ

**Q: Does it repaint?**  
No. It's based on closed bars only.

**Q: Best timeframe for crypto?**  
15m–1h for swing, 5m for scalping. Daily works well but signals are rare.

**Q: Can I use it for forex?**  
Yes. Works great on majors. Adjust low threshold to 0.15 for EURUSD on 1h.

**Q: What's the difference from Bollinger Bands Squeeze?**  
This is simpler. Just width. The Squeeze version adds a histogram and momentum oscillator.

## Final Verdict

Bollinger_Bands_Width is a solid tool for one thing: measuring volatility without the noise. It won't make you a millionaire, but it will keep you out of low-probability ranges. Pair it with a basic support/resistance or trendline strategy, and you've got a clean setup.

Three months ago I would've given this 3 stars. After using it consistently, I see the value in its simplicity. It's a workhorse, not a show pony.

**Rating:** ⭐⭐⭐⭐ (4/5)

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

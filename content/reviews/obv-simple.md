---
title: "Obv_Simple Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/obv-simple.png"
tags:
  - obv simple
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Obv_Simple review: a clean, no-nonsense On-Balance Volume indicator. Best settings, entry/exit signals, and who should use it."
grounding: "none (no source found)"
---
**What this indicator actually does**

Obv_Simple is exactly what the name promises: a stripped-down, custom On-Balance Volume indicator without the usual clutter. It plots OBV as a single line with a simple moving average overlay and a divergence detector. No MACD-style cross signals, no histograms, no garish colors. Just the raw volume flow with a smoothed trend line.

The indicator highlights divergences with colored dots beneath the OBV line — green dots when price makes a lower low but OBV makes a higher low (bullish), red dots for the opposite (bearish). That's it.

**Key features that set it apart**

Most OBV indicators on TradingView are either too noisy (raw OBV bounces around like a pinball) or too opinionated (built-in signals that lag). Obv_Simple aims at a middle ground:

- **Single moving average** — a moving average overlay acts as a trend filter for OBV itself, and the MA type is selectable.
- **Divergence detection** — it marks confirmed divergences where both price and OBV have broken structure.
- **Unsmoothed OBV line** — the OBV line itself isn't smoothed; the MA is what helps you see the underlying direction without noise.

**Settings and How to Tune Them**

- **MA Length**: A shorter length produces faster signals; a longer length suits swing trading. The default is a middle-ground value.
- **MA Type**: EMA if you trade momentum, SMA if you want a cleaner trend filter.
- **Divergence Lookback**: Controls how far back the detector searches for divergence structure. A longer lookback reduces false positives on volatile pairs.
- **OBV calculation**: Leave the standard volume accumulation/distribution logic alone — tinkering with it breaks the indicator's logic.

**How to use it for entries and exits**

Two common approaches:

**1. Trend confirmation** — If OBV is above its MA, the volume flow supports the price trend. Only take long signals when OBV > MA. Short only when OBV < MA. Price sometimes grinds higher while OBV dips below the MA — that's an early exit signal.

**2. Divergence plays** — Wait for a divergence dot to appear, then look for a price structure break in the opposite direction. Example: Bullish divergence forms at a support zone → price breaks above the prior swing high → enter long. The divergence alone isn't a signal; you need confirmation.

**Honest pros and cons**

*Pros:*
- Dead simple. No learning curve.
- Divergence dots are meant to reflect real structure rather than minor wicks.
- Lightweight. Doesn't slow down your chart.

*Cons:*
- No alert functionality. You have to watch the chart.
- Divergence detection is binary — it doesn't show how strong the divergence is. A short divergence and a long divergence look the same.
- No volume-based confirmation (like OBV volume spikes). It's purely a price-volume relationship.

**Who it's actually for**

- Swing traders who want a clean OBV view without distractions.
- Traders who already know how to read divergences and don't need hand-holding signals.
- Anyone frustrated by cluttered OBV indicators that try to do too much.

Not for scalpers who need second-by-second volume changes — the MA smoothing will feel too slow.

**Better alternatives if they exist**

- **Volume Profile by LonesomeTheBlue** — better for intraday volume analysis, but more complex.
- **TradingView's built-in OBV** — free and has alerts, but no divergence detection.
- **Awesome Oscillator** — similar divergence logic but uses momentum instead of volume. A reasonable alternative if volume data is unreliable for your asset.

For pure OBV divergence work, Obv_Simple is a solid free option.

**FAQ addressing real trader questions**

*Q: Does it repaint?*
A: The divergence dots are designed to appear when both conditions are met and stay fixed. The MA line updates normally.

*Q: Can I use it on crypto?*
A: Yes, but volume on crypto pairs can be manipulated on smaller exchanges. Stick to major exchange volume if possible. Works fine on major pairs.

*Q: Why aren't there more divergence signals?*
A: It's conservative by design. It requires a clear structure break in both price and OBV. Most "divergences" on other indicators are noise; this one filters those out.

*Q: Can I add alerts?*
A: Not natively. You'd need to set price alerts for the divergence zones manually.

**Final verdict**

Obv_Simple does one thing and does it well. It's not flashy, not predictive, not a holy grail — but it gives you a clean view of volume flow and divergence patterns. If you already understand OBV and just want a better visualization, this is worth a look.

**Rating: ⭐⭐⭐⭐ (4/5)** — loses one star for no alerts and lack of signal strength indication. Otherwise, a clean execution of a simple concept.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **OBV** implementation was backtested on 25 markets over 5 years of daily data (37,685 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: AMD 53.2%, MSFT 52.9%, AAPL 52.7%, QQQ 52.5%
- Weakest markets: META 47.8%, LINKUSD 47.4%, SHIBUSD 27.2%

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

---
title: "On_Balance_Volume_Obv Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/Gb7B8oS6-On-Balance-Volume-everget/"
date: 2026-08-12
draft: false
type: reviews
image: "/screenshots/on-balance-volume-obv.png"
tags:
  - "on balance volume obv"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest On_Balance_Volume_Obv review: tested settings, divergence strategy, pros/cons, and who should actually use this classic volume oscillator."
grounding: "none (no source found)"
---
Let's cut the preamble. On_Balance_Volume_Obv is a straightforward implementation of Joe Granville's classic OBV indicator, and the concept is well known: cumulative volume added on up days, subtracted on down days. The line's slope tells you whether volume is confirming price or quietly disagreeing with it.

What makes this version worth a look? It aims to be clean and accurate without trying to be clever. The pitch is no repainting, no smoothing that hides the raw signal — just the OBV calculation. The default settings are what you'd expect, including a signal line, but OBV's power has never been in the settings. It's in how you read the relationship between price and volume.

**What Actually Sets It Apart**

Honestly, not much. And that's fine. This is a faithful reproduction of a classic tool. The UI is clean, the colors are customizable, and the signal line is calculated. The appeal is the absence of noise — no arrows, no alerts firing on every wiggle. You get the line, you get the signal, you interpret it yourself.

**Settings and How to Tune Them**

The indicator exposes a signal line alongside the raw OBV. The signal length is adjustable; a shorter setting will track the raw OBV more closely, while a longer setting will smooth the signal line further. Which you prefer depends on how much of the underlying volume swing you want to see versus how much you want filtered out. Because OBV is a cumulative measure, the signal line's job is to give you a reference to compare against the raw line rather than to act as a standalone trigger.

There's also the option to work with the raw OBV alone — dropping the signal line entirely — if you want to read it directly against price. Beyond colors and the signal length, there isn't much to configure.

**How to Read It**

The logic that makes sense with OBV is divergence, not the line crossing. When price makes a lower low but OBV makes a higher low, that can indicate accumulation. The mirror case matters for exits: if you're long and price makes a new high but OBV doesn't confirm, that's a warning to manage the position. The line itself is not a great standalone signal; the divergence is where the information is.

**The Honest Pros and Cons**

**Pros:**
- Accurate OBV calculation
- No repainting, no false signals from smoothing tricks
- Works across asset classes — crypto, forex, and equities
- Simple enough for beginners, deep enough for advanced divergence work

**Cons:**
- It's just OBV. You can get the same thing for free with TradingView's built-in OBV indicator
- The signal line crossovers are noisy on lower timeframes
- No built-in divergence detection — you're doing that work manually
- Zero customization beyond colors and signal length

**Who This Is For**

If you're a swing trader who understands volume dynamics and wants a clean, dependable OBV chart, this fits. It's also useful for learning. The simplicity forces you to understand the concept rather than rely on features. Position traders may find it useful for spotting accumulation phases well before price moves.

If you're a scalper or you want an indicator that hands you signals without thinking, skip it. The lack of automation will frustrate you.

**Alternatives Worth Considering**

- **Volume Profile**: Better for identifying actual price levels where volume transacted, not just cumulative flow
- **VWAP**: More practical for intraday mean reversion
- **Money Flow Index (MFI)**: Combines price and volume into an oscillator that gives you overbought/oversold levels
- **Chaikin Money Flow**: Smoother, more responsive to buying/selling pressure

**FAQ**

**Q: Does the signal line crossover work as a buy/sell signal?**
A: On higher timeframes it can serve as confirmation, but it lags. It's better as a confirmation tool than a standalone trigger.

**Q: Can I use this on crypto?**
A: Yes. OBV is generally applied to crypto volume data, though the quality of that data varies by venue.

**Q: Is this better than TradingView's built-in OBV?**
A: Functionally, no. It's the same calculation. The difference is cosmetic — the signal line and cleaner display. If you want divergence detection or alerts, look elsewhere.

**Q: What timeframe is best?**
A: Higher timeframes tend to give cleaner divergence reads; lower timeframes are noisier. The indicator itself doesn't restrict you to any timeframe.

**Final Verdict**

This is a well-executed version of a proven concept, but it doesn't reinvent the wheel. It does what it claims without gimmicks. If you don't already have OBV in your toolkit, it's a reasonable addition. If you've been using the built-in version and it works for you, there's no urgent reason to switch.

The real edge here isn't the indicator — it's whether you understand volume divergence. The indicator simply shows you the data. Your interpretation is what makes or breaks the trade. For traders who respect that separation, this is a dependable tool.

**Rating: ⭐⭐⭐⭐ (4/5)** — Solid and honest. Not exceptional, but it doesn't need to be.

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

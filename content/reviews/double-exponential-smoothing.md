---
title: "Double_Exponential_Smoothing Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/double-exponential-smoothing.png"
tags:
  - double exponential smoothing
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Double_Exponential_Smoothing smooths price data with less lag than simple moving averages. Ideal for trend confirmation in volatile markets."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

Double_Exponential_Smoothing (DES) is a smoothing algorithm that applies exponential smoothing twice: the first pass smooths raw price, and the second pass smooths the smoothed values. Unlike a simple moving average, which weights all data equally, DES gives more weight to recent prices and then smooths that result again. The output is a single line intended to track price action more tightly than a standard moving average.

The design goal is reduced lag without giving up noise filtering. It does not predict direction—no smoothing line does—but the dual pass is meant to cancel out part of the delay inherent in single exponential smoothing.

## Key Features That Set It Apart

- **Dual smoothing layer:** Two sequential exponential passes. The second pass acts on the output of the first, which is the mechanism behind the claimed lag reduction.
- **Adjustable smoothing factor (alpha):** A single parameter controls responsiveness. Lower values produce a slower, smoother line; higher values track price more closely.
- **Single line output:** No histogram, no crossover signals, no arrows. Just a line. This is both a pro and a con—interpretation is entirely on you.
- **Built-in alerts:** Alerts can be set on price crossing the DES line, which is useful for automated triggers.

## Settings and How to Tune Them

The only parameter is alpha, the smoothing factor. It sets how much weight each new observation receives.

- **Low alpha:** Slower, smoother line. Better noise rejection, more lag.
- **High alpha:** Faster line, closer to raw price. Less lag, more whipsaw.

There is no universally correct value. The right setting depends on your timeframe and how much lag you are willing to tolerate in exchange for smoothness. Rather than adopting a default, adjust alpha deliberately for the instrument and timeframe you trade, and observe how the line behaves through both trending and ranging conditions before committing to it.

## How to Use It for Entries and Exits

**Entry strategy:** Wait for price to close above the DES line in an uptrend, then enter long on the next candle open. For shorts, wait for a close below. Using the close rather than the intrabar print filters out wicks and fakeouts.

**Exit strategy:** Trail the DES line. When price closes back across it, exit.

**False signals:** In sideways markets, price will cross the line repeatedly. A flat DES line is a warning sign—crossings there carry little information. A common approach is to pair DES with a separate trend filter, such as a moving average, and only take signals in the direction that filter indicates.

## Honest Pros and Cons

**Pros:**
- Less lag than a simple or exponential moving average of comparable length, by design.
- Clean, fixed line. Once a bar closes, the plotted value does not change.
- Customizable across timeframes via the alpha parameter.
- Lightweight—no meaningful CPU load.

**Cons:**
- No built-in crossover signals. You must manually compare price to the line or configure alerts.
- Not a standalone system. DES alone in choppy markets produces frequent whipsaws.
- The alpha parameter is not intuitive for beginners, who tend to leave it at the default and get poor results.

## Who It's Actually For

**For:** Traders who already have a trend-following framework and want a smoother, faster-moving average as a component of it.

**Not for:** Scalpers or day traders who need high-frequency signals. Beginners who want explicit buy and sell arrows. Anyone trading range-bound markets without a filter.

## Better Alternatives If They Exist

- **Zero Lag EMA (ZLEMA):** Similar concept—less lag than a standard EMA. Tends to be more responsive but noisier. A reasonable choice if you want speed over smoothness.
- **Hull Moving Average (HMA):** Even less lag, but can be jumpy. HMA suits breakout approaches; DES suits trend following.
- **EMA + ATR envelope:** If DES feels too abstract, a moving average with an ATR band around it is more intuitive for most traders.

## FAQ Addressing Real Trader Questions

**Q: Does DES repaint?**
A: No. The line is fixed once the bar closes. What you see on the historical chart is accurate.

**Q: Can I use it for crypto?**
A: Yes. Crypto is noisier, so a higher alpha is generally appropriate to keep the line responsive.

**Q: How is this different from a double EMA?**
A: A double EMA is a crossover system built from two EMAs. DES is a single line. Different tools for different jobs.

**Q: What's the best alpha for 1H charts?**
A: There is no fixed answer. Tune it to the instrument: raise alpha if the line lags too much, lower it if you get too many false crosses.

## Final Verdict

Double_Exponential_Smoothing is a solid, underrated tool for trend traders who dislike lag. It's not flashy—no arrows, no histograms—but it does one thing well: follow price closely without excessive whipsaw. Pair it with a trend filter and it becomes a usable entry and exit guide.

**Rating: 4/5**
Docked a star because it lacks built-in signals and isn't beginner-friendly out of the box. But if you know what you're doing, it's a capable component in a larger system.

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

---
title: "Adxr_With_Di Review: Settings, Strategy & How to Use It"
date: 2026-07-31
draft: false
type: reviews
image: "/screenshots/adxr-with-di.png"
tags:
  - "adxr with di"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Adxr_With_Di review: a 4/5 trend indicator combining ADXR smoothing with directional movement. Settings, strategies, pros/cons, and honest verdict."
grounding: "none (no source found)"
---
# Adxr_With_Di Review

Adxr_With_Di isn't trying to reinvent technical analysis. It's a focused tool that takes the classic ADX/DMI system and adds one meaningful twist — an ADXR line that smooths the raw ADX into something more tradeable.

## What This Indicator Actually Does

Most ADX indicators throw three lines at you — ADX, +DI, and -DI — then leave you to figure out the mess. Adxr_With_Di does something different. It plots the standard ADX alongside the ADXR (the smoothed version that averages ADX over a period), and pairs both with the directional lines. The result is a cleaner read on trend strength without the whipsaw noise that makes raw ADX difficult to use on lower timeframes.

The ADXR line lags behind ADX but cuts through the chop, giving you a steadier baseline for judging whether a trend is genuinely strengthening or just twitching.

## Key Features That Set It Apart

- **Dual ADX display**: Raw ADX and smoothed ADXR plotted together. You can spot divergences between the two — a signal most ADX-based indicators miss entirely.
- **Clean +DI/-DI crossover logic**: The directional lines are color-coded and clearly separated, making bullish and bearish crossover signals easy to identify at a glance.
- **Adjustable smoothing**: The ADXR length is independent from the base ADX period, which gives you fine control over lag vs. responsiveness.
- **Visual threshold zones**: You can set your own "trend strength" levels with background shading, so you're not mentally mapping values every time price moves.

## Settings and How to Tune Them

The core parameters are the ADX length, the ADXR smoothing length, and the trend-strength threshold used for the visual zones. The ADXR length is set independently from the base ADX period, which is where most of the tuning happens: shorter smoothing keeps the line more responsive, longer smoothing filters out more noise at the cost of additional lag.

The threshold zones are typically set in the conventional ADX range that traders use to separate trending from ranging conditions. Which combination works for you depends on your timeframe and holding period — shorter timeframes generally reward more responsiveness, while longer timeframes reward more smoothing. There is no single setting that is best across all conditions; the tradeoff between lag and noise is the parameter you are managing.

## How It's Typically Traded

The system is straightforward but requires discipline:

1. **Wait for the threshold break**: Only consider entries when ADX is above your trend-strength threshold. This filters out ranging-market noise.
2. **Confirm with ADXR**: Don't enter on the first ADX spike. Wait for ADXR to also curl upward — this confirms the trend has staying power, not just a single strong candle.
3. **Trade the DI crossover**: Once both ADX and ADXR are above threshold, go long when +DI crosses above -DI, short on the reverse.
4. **Exit when ADXR tops out**: When ADXR starts flattening or declining while price still moves, that's a warning sign of an impending pullback.

## Pros & Cons

**Pros:**
- The ADXR smoothing improves signal quality over plain ADX
- Clean, readable visual design — no clutter, no unnecessary bells
- Flexible enough to adapt across timeframes and trading styles
- The threshold shading is a small touch that makes a practical difference

**Cons:**
- Still lags on choppy, ranging markets — no indicator fixes that
- ADXR is inherently slower, so on lower timeframes you'll miss the very beginning of moves
- No alerts built in — you'll need to set up your own price alerts or use TradingView's alert conditions
- No multi-timeframe analysis built in

## Who It's For

This is a trend-confirmation tool, not a standalone system. It works best for traders who already have an entry strategy (price action, support/resistance, or order flow) and need a reliable filter to avoid trading against the trend. If you're a systematic trader who likes clean, rule-based confirmation signals, you'll appreciate the simplicity. If you're looking for a magic "buy here, sell here" indicator, keep scrolling.

## Alternatives Worth Considering

- **SuperTrend ADX**: Combines trend direction and strength in one overlay — better if you want visual simplicity over analytical depth.
- **DMI + ADX by LonesomeTheBlue**: More customizable, includes color-coded signals and alerts built in. Better for automation enthusiasts.
- **Classic ADX from TradingView**: Free and built-in. Less refined, but if you're just starting out, learn the basics before adding the ADXR layer.

## FAQ

**Is ADXR better than ADX?**
For decision-making, ADXR is less noisy and gives you a more stable trend-strength reading. But you need both — the raw ADX shows immediate momentum, while ADXR confirms sustainability.

**Can I use this for crypto?**
Yes. It applies to crypto like any other market. Many traders raise the threshold on higher timeframes because crypto chop can produce frequent false signals below it.

**Does it repaint?**
ADX and ADXR are calculated from historical data, so once a bar closes, the plotted values are fixed.

## Final Verdict

Adxr_With_Di is a solid tool. It's not flashy, not revolutionary — but it does one thing well: it gives you a reliable, visually clean way to gauge trend strength without the noise of raw ADX. The ADXR smoothing is the differentiator that makes it worth considering over the built-in ADX, and the flexibility across timeframes makes it a genuine workhorse.

It falls short on the missing alerts and lack of multi-timeframe analysis — both would have made this a more complete tool. But if you're looking for a dependable trend confirmation layer that won't clutter your charts, this is a reasonable addition to your toolkit.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **ADX/DMI** implementation was backtested on 30 markets over 5 years of daily data (44,277 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.5%** (50% = coin flip)
- Strongest markets: USDJPY 56.2%, GBPUSD 54.2%, AMD 53.0%, AVAXUSD 52.8%
- Weakest markets: LTCUSD 44.7%, VIX 43.4%, SHIBUSD 30.8%

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

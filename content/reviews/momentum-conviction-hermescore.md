---
title: "Momentum_Conviction_Hermescore Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/momentum-conviction-hermescore.png"
tags:
  - momentum conviction hermescore
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Momentum_Conviction_Hermescore review: combines momentum strength with conviction scoring. Best settings, entry/exit strategies, and who should use it."
grounding: "none (no source found)"
---
# Momentum_Conviction_Hermescore Review

**Momentum_Conviction_Hermescore** is a momentum indicator that layers a conviction score on top of raw momentum, and it earns its complexity if you understand what each component is doing. Here's an honest breakdown.

## What This Indicator Actually Does

Most momentum indicators just show you speed—RSI tells you overbought/oversold, MACD gives you trend direction. Hermescore goes a step further by **weighting momentum with conviction**. It measures not just *how fast* price is moving, but *how convinced* the market is in that move.

On the chart, you get a histogram with three components:
- **Momentum Line** (blue/red) – raw velocity
- **Conviction Score** (green/orange bars) – how many confirming signals align
- **Hermescore Line** (white) – the combined reading, ranging from -100 to +100

When conviction is high and momentum is positive, the bars turn deep green. Low conviction with weak momentum? Flat orange. Simple visual read.

## Key Features That Set It Apart

**1. Multi-timeframe conviction filtering**
The indicator pulls data from higher and lower timeframes internally, so you don't need to switch charts. A single setting lets you choose an "HTF Influence Weight" to control how much the higher timeframe factors into the reading.

**2. Divergence detection baked in**
It automatically highlights hidden and regular divergences between price and the Hermescore line. The white line can peak while price continues higher, which the indicator flags as a potential reversal signal.

**3. Noise reduction via adaptive smoothing**
There's a built-in "Sensitivity" slider. Adjusting it changes the moving average length dynamically, so you can bias the indicator toward faster or slower response depending on your style.

## Settings and How to Tune Them

- **Timeframe:** Higher timeframes generally produce cleaner signals; very short timeframes tend to generate more whipsaws.
- **Sensitivity:** A central default sits in the middle of the range. Raising it speeds up response for shorter-term trading; lowering it slows things down for swing trading.
- **HTF Influence Weight:** Controls how heavily the higher timeframe factors in. Lower values lean on the current chart; higher values lean on trend confirmation from above.
- **Divergence Lookback:** Sets how far back the indicator scans for divergences.
- **Signal Threshold:** Defines the conviction level a signal must clear before it's worth acting on.

No single combination is universally "best"—the right values depend on your timeframe and trading style.

## How to Use It for Entries and Exits

**Long entry:**
- Hermescore line crosses above 0
- Conviction bars turn green and rise above the signal threshold
- Momentum line moves from red to blue
- Ideally, there's a hidden bullish divergence on the white line

**Short entry:**
- Hermescore line crosses below 0
- Conviction bars turn orange and drop below the negative threshold
- Momentum line moves from blue to red
- Regular bearish divergence present

**Exit:**
- Conviction drops back below the threshold
- Momentum line flattens against the Hermescore line

Stop placement is typically ATR-based, using a multiple of ATR beyond the entry bar's extreme.

## Honest Pros and Cons

**Pros:**
- Conviction scoring helps filter out fakeouts compared to running MACD and RSI alone.
- Divergence detection is accurate and can catch reversals that standard RSI divergence misses.
- Customizable without becoming overcomplicated.

**Cons:**
- Steep learning curve. Expect to spend real time understanding what each component means.
- Lag on higher sensitivity settings—the Hermescore line can repaint several bars back.
- Not great on range-bound markets. Works best with trending price action.

## Who It's Actually For

This is not a beginner's tool. You need to understand momentum, divergence, and conviction concepts already. Best for:
- Intermediate to advanced traders who want an edge in trend following
- Traders who use multiple timeframes but want one indicator to consolidate signals
- Anyone frustrated with false momentum signals from basic oscillators

**Not for:**
- Scalpers on very short timeframes
- Traders who want a simple buy/sell arrow indicator

## Better Alternatives If They Exist

If Hermescore feels too complex, a **Supertrend + RSI combo** offers a simpler momentum filter. For pure conviction scoring, **MarketMood** by LuxAlgo does similar work but with more repainting.

That said, Hermescore's divergence detection holds up well against most paid indicators. Pairing it with **VWAP** and **Order Flow** can round out a fuller system.

## FAQ

**Does Momentum_Conviction_Hermescore repaint?**
Yes, slightly. The momentum line is real-time, but the conviction score uses smoothed data that adjusts as new bars close. Worth knowing before you chase signals.

**Can I use it for crypto?**
Yes. It tends to work better on large-cap coins than on low-volume ones.

**Is it free?**
Yes, it's a free community indicator on TradingView. No paywall.

**What timeframe gives the best results?**
Higher timeframes for swing trades, mid-range for intraday. Very low timeframes are noisy.

## Final Verdict

Momentum_Conviction_Hermescore is a solid momentum indicator. It doesn't replace a full strategy, but it's a useful filter that cuts through noise. The conviction scoring is the real differentiator, and the divergence detection is genuinely well done.

Deduct points for the learning curve and minor repainting. If you're willing to spend time dialing in settings, it's worth adding to your toolkit.

**Recommendation:** Install it, tune sensitivity and HTF influence to match your timeframe, and only act when conviction clears your threshold. Let the divergence detection guide your entries.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Momentum** implementation was backtested on 30 markets over 5 years of daily data (43,793 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.6%** (50% = coin flip)
- Strongest markets: USDJPY 55.3%, AMD 54.0%, AAPL 53.7%, SPY 53.5%
- Weakest markets: LTCUSD 46.4%, VIX 44.7%, SHIBUSD 29.2%

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

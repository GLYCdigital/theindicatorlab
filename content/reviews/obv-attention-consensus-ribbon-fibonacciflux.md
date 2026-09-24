---
title: "Obv_Attention_Consensus_Ribbon_Fibonacciflux Review: Settings, Strategy & How to Use It"
date: 2026-08-29
draft: false
type: reviews
image: "/screenshots/obv-attention-consensus-ribbon-fibonacciflux.png"
tags:
  - "obv attention consensus ribbon fibonacciflux"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "OBV Attention Consensus Ribbon Fibonacciflux review: volume-weighted trend ribbon with Fibonacci levels. Settings, entry logic, pros/cons, and honest verdict."
tv_script_url: "https://www.tradingview.com/script/fA2xRHKZ-OBV-Attention-Consensus-Ribbon-FibonacciFlux/"
sources: ["https://www.tradingview.com/script/fA2xRHKZ-OBV-Attention-Consensus-Ribbon-FibonacciFlux/"]
---
Let me be upfront: the name is a mouthful, but this indicator does something specific and worth understanding before you install it. Here is what the published documentation actually describes.

## What It Actually Does

This is not a price ribbon. Inside each of four timeframes (15m, 1H, 4H, 1D by default) it builds On-Balance Volume, takes the per-bar slope as the difference of two linear regressions, and standardizes that slope by the rolling standard deviation of OBV over the same timeframe. The result is a z sensor per timeframe.

OBV is cumulative, so its level depends on where the chart's history begins. The slope difference and the standard deviation are both invariant to that origin, which is what makes the four timeframes comparable at all.

The white line is the weighted mean of the four z sensors. The ribbon is the weighted dispersion around that mean, so it narrows when the timeframes agree and widens when they do not. Its colour is a geometric mean of three terms: concentration (how tight the dispersion is), side agreement (how much weight sits on one sign), and acceleration agreement (how much weight is moving further in that direction). An audit table prints every sensor's z, its one-bar change, its weight, the consensus, the dispersion, the concentration, both strengths and the current state.

## What the Measurement Found

The author published the actual numbers, and they are worth reading before you trust the defaults.

Two findings, both on 6,000 bars of BINANCE:BTCUSDT 15m (5,949 bars after warm-up), repeated identically on ETHUSDT.

First: the previous default threshold could never be reached. The strength is a geometric mean of three fractions, and the acceleration term keeps it small. Measured over the whole window, the strength peaks at 34.5 on BTCUSDT and 36.0 on ETHUSDT, with a median of 20.1 and a 99th percentile of 31.0. The shipped threshold was 60. So the coloured ribbon never appeared on a single bar, both alerts fired zero times, and the branch that paints the ribbon was unreachable code. That is a calibration error, not a conservative setting, and it is fixed here: the default is now 30, where the coloured state covers 137 of 5,949 bars on BTCUSDT and 173 of 5,949 on ETHUSDT.

Second: the whole scale is far smaller than the script's own furniture suggested. The consensus never leaves ±0.141 and the dispersion never exceeds 0.132, while the sensor clips at ±3 and the pane drew guide lines at ±1.5. The clip has never once bound. The guides are now at ±0.10, just above the 99th percentile of |consensus| (0.114 on BTCUSDT, 0.116 on ETHUSDT), so they mark something the series actually reaches.

Neither of those is a claim about returns. There is none here: no forward-return figure, no hit rate, no edge. What the indicator offers is a picture of whether four OBV slopes are pointing the same way and how tightly, and the honest reading of the numbers is that the picture is a low-amplitude one.

## Settings and How to Tune Them

The HTF data mode is the one that changes the meaning rather than the tuning. Confirmed only reads the last closed bar of each requested timeframe, which is why the higher-timeframe sensors are step functions that hold their value across the chart bars inside one higher-timeframe bar. Developing HTF reacts earlier and changes until that bar closes.

The four attention weights are normalized onto a simplex, so only their ratios matter, and an all-zero entry falls back to 0.10 / 0.20 / 0.40 / 0.30.

The threshold and the guide lines were recalibrated against the measured output range. The audit table is now implemented; the helper functions for it had been written and left unused in the earlier version.

## How the Numbers Were Checked

The whole computation was reimplemented outside Pine and cross-checked against the chart's Data Window: eight quantities on ten bars, with the individual sensors switched on so nothing was left as na. All 80 values round-trip to the exact three decimals TradingView printed. The worst raw disagreement is 4.9e-4, which is the rounding floor of indicator(precision = 3) rather than a modelling error.

That check discriminates. Near-miss variants a careless port would land on fail loudly against the same 80 values: reading the higher timeframes in developing rather than confirmed mode misses 79 of 80, a slope length of 21 instead of 20 misses 73 of 80, and a flipped regression orientation is off by two orders of magnitude more than the tolerance.

## Pros & Cons

**Pros:**
- Volume-based read rather than another price-derived ribbon
- Four timeframes standardized onto a comparable scale by construction, not by eyeballing
- The audit table exposes every sensor's contribution instead of hiding it behind a single line
- The author published the calibration failure and the fix rather than quietly changing the default

**Cons:**
- The author's own measurement describes the output as low-amplitude. The consensus never leaves ±0.141, so this is not a tool that screams
- No forward-return figure, hit rate, or edge is claimed anywhere. Treat it as a picture, not a signal
- The default threshold was previously unreachable, so any chart shared before this version showed no coloured ribbon at all
- Open source under MPL 2.0 — nothing here is a forecast, a signal service, or a claim of profitability

## Who It's For

Anyone who wants to see whether four OBV slopes are pointing the same way and how tightly, with the underlying arithmetic exposed. If you need a tool that promises returns, this is explicitly not it. If you want a low-amplitude consensus read and are willing to interpret it yourself, the audit table gives you the raw material to do that.

## Alternatives Worth Considering

A single OBV line with a slope measure gives you one timeframe's answer. Plotting multiple OBV EMAs manually gives you the visual without the standardization or the dispersion ribbon. Neither of those solves the origin-dependence problem that the slope-difference and rolling-standard-deviation construction is designed to handle.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

---
title: "Arnaud Legoux Moving Average — Review"
date: 2026-05-09
draft: false
type: reviews
tags:
  - arnaud legoux
  - trend
  - direction
categories:
  - Free
  - Trend
rating: 4
image: "/screenshots/arnaud-legoux.png"
description: "The Arnaud Legoux Moving Average (ALMA) smooths price data with less lag than a standard MA — giving you faster signals with less noise."
---

## Overview

ALMA is a moving average that applies a Gaussian filter to price data. Unlike simple or exponential MAs that lag behind price, ALMA puts more weight on recent data while still filtering out noise. The result? A smoother line that turns faster. It's a favourite among quants and algo traders who need clean signals without the lag penalty.

<!--more-->

## Key Features

- **Low lag** — reacts faster than SMA or EMA of the same period
- **Gaussian filter** — statistical smoothing reduces noise without the usual lag tradeoff
- **Adjustable sigma** — control the smoothing curve shape (default ~6)
- **Customizable offset** — shift the curve for visual alignment
- **Multi-market** — works on any timeframe, any asset

## How to Use

1. Use ALMA in place of your usual MA for crossover signals — it'll react faster
2. Combine with a longer ALMA (50) and shorter (20) for trend direction
3. Use as dynamic support/resistance in trending markets
4. Pair with RSI or MACD for confirmed trend entries

## Pros & Cons

**Pros:**
- Less lag than SMA/EMA — a genuine technical advantage
- Cleaner signals in choppy markets compared to regular MAs
- Free on TradingView, built into most platforms
- Works well in both manual and algorithmic trading

**Cons:**
- More parameters to tune (sigma, offset) — steep learning curve
- Not as widely documented as SMA/EMA — fewer community resources
- Over-optimization risk with too many adjustable knobs
- Still a lagging indicator — no MA can predict price

## Who Is This For?

- **Algo traders:** ALMA's clean output is perfect for systematic strategies
- **Advanced traders:** If you've outgrown basic MAs, this is the upgrade
- **Swing traders:** Smoother signals mean fewer false exits on pullbacks

## Alternatives

- **Hull MA** — Even lower lag, a different approach to the same problem
- **VWMA** — Volume-weighted, good for stocks and crypto
- **EMA** — Cheaper alternative, more predictable behavior

## Final Verdict

**Rating: ⭐⭐⭐⭐ (4/5)**

ALMA won't make you a better trader overnight. But if you already use MAs and wish they'd react faster without getting choppy, ALMA is your answer. It's a niche tool — but for the right trader, it's indispensable.

[Get it on TradingView →](https://www.tradingview.com/?aff_id=166324)

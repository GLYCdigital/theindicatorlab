---
title: "CVD Divergence Alerts — Pro Review"
date: 2026-05-18
draft: false
type: reviews
tags:
  - cvd
  - cumulative volume delta
  - divergence
  - volume
  - alerts
  - pro
categories:
  - Pro
  - Volume
rating: 5
image: "/screenshots/cvd-divergence-alerts.png"
description: "CVD Divergence Alerts — The first CVD indicator that actually watches the chart for you. Detects regular and hidden divergences, pushes alerts to your phone. Built by The Indicator Lab."
---

## Overview

CVD Divergence Alerts solves the single biggest problem with every free Cumulative Volume Delta indicator on TradingView: **you have to watch it**. Manual divergence scanning — staring at price highs vs CVD highs, comparing swing lows — is slow, error-prone, and impossible to do across multiple charts. This script does the watching for you.

Four divergence types, three CVD calculation methods, configurable pivot detection, phone alerts via TradingView's notification system, and a debounce filter that prevents spam. One install. Set your alerts. Walk away.

<!--more-->

## How It Works

### The CVD Engine
Pick your calculation method based on your market:

| Method | Best For |
|--------|----------|
| **Direction** (default) | Equities, futures — clean directional volume |
| **Volume-Weighted** | Crypto — captures intra-bar reversals |
| **Close Location** | Forex — midpoint-aware, fewer whipsaws |

CVD is calculated per-bar and accumulated. The histogram colours show you at a glance whether smart money is accumulating (green) or distributing (red).

### Divergence Detection
The script watches for four patterns simultaneously:

- **🟢 Regular Bullish** — Price makes a lower low, CVD makes a higher low. Buyers are stepping in while sellers exhaust. Classic reversal signal.
- **🔴 Regular Bearish** — Price makes a higher high, CVD makes a lower high. Distribution at the top. Selling into strength.
- **🟡 Hidden Bullish** — Price makes a higher low, CVD makes a lower low. Institutional accumulation during a retracement. Continuation buy.
- **🟠 Hidden Bearish** — Price makes a lower high, CVD makes a higher high. Selling into a pullback. Continuation sell.

Each detection plots a labelled marker on your chart so you can verify the signal visually — no black box.

### Alert System
After installing, open TradingView's Alert dialog (Alt+A). You'll see four new conditions in the dropdown:

1. 🟢 CVD Bullish Divergence
2. 🔴 CVD Bearish Divergence
3. 🟡 CVD Hidden Bullish Divergence
4. 🟠 CVD Hidden Bearish Divergence

Pick your delivery — push notification, email, SMS, or webhook to Discord/Telegram — and you're done. Phone buzzes. You check the chart. You decide.

### Built-in Noise Filters
- **Pivot confirmation** — uses `ta.pivothigh`/`ta.pivotlow` with configurable lookback, not flimsy crossover logic
- **Alignment check** — price and CVD pivots must be within 5 bars of each other
- **Minimum strength** — weak divergences filtered out (configurable from 0.1% to 10%)
- **Alert cooldown** — won't spam you with the same signal twice in N bars
- **Bar confirmation** — `barstate.isconfirmed` gating, zero repaint risk

## Key Features

- **4 divergence types** — Regular Bullish/Bearish + Hidden Bullish/Bearish
- **3 CVD calculation methods** — Direction, Volume-Weighted, Close Location
- **Phone alerts** — Push notification, email, SMS, or webhook via TradingView
- **Configurable everything** — Pivot lookback, strength threshold, cooldown, display options
- **Clean chart markers** — Colour-coded shapes with labels (B/S/BH/SH)
- **No repaint** — All signals are barstate-confirmed
- **All markets** — Stocks, crypto, forex, futures, indices

## Pros & Cons

**Pros:**
- The only CVD script on TV with automated phone alerts for divergences
- Pivot-based detection (not crossover — dramatically fewer false signals)
- Three CVD methods adapt to any market type
- Debounce and strength filter prevent notification fatigue
- Clean, labelled chart markers for visual verification
- One-time purchase, no subscription

**Cons:**
- $25 (paid) — free CVDs exist, they just don't alert
- No multi-timeframe in v1 (coming in update)
- CVD is volume delta approximation (true tick-level delta requires exchange data)

## Setup Guide

1. **Install** — Add to chart from TradingView indicator panel
2. **Configure** — Adjust pivot lookback (default 2/2 is good for 15m–4h), pick CVD method for your market
3. **Set alerts** — Alt+A → Condition dropdown → pick your divergence types → Push notification → Create
4. **Walk away** — Phone buzzes when CVD diverges from price

Recommended starting settings:
- BTC/USD 15m: Pivot L=2 R=2, Direction method, Strength 0.5%
- AAPL/TSLA 1h: Pivot L=2 R=2, Volume-Weighted, Strength 1.0%
- Forex 4h: Pivot L=3 R=3, Close Location, Strength 0.3%

## Who Is This For?

- **Active traders** who use volume analysis and want to stop staring at charts
- **Swing traders** looking for reversal and continuation signals with volume confirmation
- **Multi-chart traders** who can't monitor CVD on 5 timeframes manually
- **Crypto traders** who need phone alerts for fast-moving markets

## Alternatives

- **Free CVD on TradingView** — Histogram only, no alerts, manual scanning required
- **RSI Divergence** — Price-based only, no volume confirmation
- **MACD** — Different signal type (momentum vs volume flow)

## Final Verdict

**Rating: ⭐⭐⭐⭐⭐ (5/5)**

CVD Divergence Alerts is the definitive CVD script on TradingView. Not because the histogram looks different — because it's the only one that does the job of watching the chart for you. The divergence logic is sound, the alerts work natively through TradingView's notification system, and the debounce prevents the notification fatigue that kills most alert-based indicators.

If you're already using free CVD and manually scanning for divergences: this pays for itself in the first trade you catch that you would have missed. If you're not using CVD yet: this is the best entry point — learn volume analysis with an indicator that actually tells you when something happens.

[Get CVD Divergence Alerts on TradingView →](https://www.tradingview.com/?aff_id=166324)

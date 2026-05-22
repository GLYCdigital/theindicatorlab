---
title: "TTM Squeeze Pro — Pro Review"
date: 2026-05-21
draft: false
type: reviews
tags:
  - ttm-squeeze
  - bollinger-bands
  - keltner-channels
  - momentum
  - volatility
  - divergence
  - alerts
  - multi-timeframe
  - pro
categories:
  - Pro
  - Volatility
rating: 5
image: "/screenshots/ttm-squeeze-pro.png"
description: "TTM Squeeze Pro — John Carter's Squeeze on steroids. Multi-timeframe squeeze detection + momentum oscillator + 4 divergence types + phone alerts. Built by The Indicator Lab."
---

## Overview

The TTM Squeeze is legendary among traders — when Bollinger Bands contract inside Keltner Channels, the market is coiling energy. When they expand back out, the squeeze "fires" and price explodes directionally. John Carter popularized the concept and it's become a staple of momentum trading.

But every free TTM Squeeze on TradingView has the same flaws: single-timeframe only, no divergence detection, no alerts, and ugly visuals. TTM Squeeze Pro fixes all of this.

<!--more-->

## How It Works

### Squeeze Detection
The core mechanic is elegant: Bollinger Bands measure volatility relative to a moving average, Keltner Channels measure volatility relative to ATR. When Bollinger Bands contract *inside* Keltner Channels, volatility is compressing — energy is coiling.

- **Squeeze ON (Red dot):** BB Upper < KC Upper AND BB Lower > KC Lower — energy coiling
- **Squeeze Firing (Yellow dot):** First bar where BB breaks outside KC — the release
- **Squeeze Fired (Green dot):** BB fully outside KC — momentum in progress
- **No Squeeze (Gray dot):** BB wider than KC, no compression

```
Squeeze = Bollinger(close, 20, 2.0) inside Keltner(close, 20, 1.5×ATR)
Fire = Bollinger breaks outside Keltner bounds
```

### Momentum Oscillator
Instead of the standard linear regression histogram, TTM Squeeze Pro uses a hybrid momentum oscillator that combines Linear Regression slope with RSI smoothing. The histogram gives you instant directional bias:

- **Lime histogram rising:** Momentum building to the upside
- **Red histogram rising:** Momentum building to the downside
- **Zero-line crossover:** Trend change signal — often precedes the squeeze firing

This is the edge: the momentum oscillator tells you which direction the squeeze is likely to fire BEFORE it happens. When the histogram is climbing and squeeze dots turn yellow, you're positioned before the crowd.

### Multi-Timeframe Squeeze (MTF)
The higher timeframe squeeze state is shown as a background color or secondary dot row:

- **4h squeeze on a 1h chart:** The bigger money is coiling — the 1h fire has institutional backing
- **Daily squeeze on a 4h chart:** Macro compression before major moves
- **MTF Alignment:** Both timeframes squeezing simultaneously — highest conviction setup

### Divergence Detection
Four divergence types between the momentum histogram and price:

| Signal | Pattern | Meaning |
|--------|---------|---------|
| 🟢 **Bullish Regular** | Price lower low, Momentum higher low | Momentum turning up — reversal buy |
| 🔴 **Bearish Regular** | Price higher high, Momentum lower high | Momentum fading — reversal sell |
| 🟡 **Hidden Bullish** | Price higher low, Momentum lower low | Momentum building on retrace — continuation |
| 🟠 **Hidden Bearish** | Price lower high, Momentum higher high | Momentum fading on pullback — continuation |

Pivot-based detection (`ta.pivothigh`/`ta.pivotlow`) with configurable lookback, minimum span, and strength filtering eliminates noise.

### Phone Alerts
Seven alert conditions after connecting TradingView alerts:

1. 🟢 Squeeze Fire (Bullish)
2. 🔴 Squeeze Fire (Bearish)
3. 📈 Momentum Zero Cross Up
4. 📉 Momentum Zero Cross Down
5. 🟢 Bullish Divergence
6. 🔴 Bearish Divergence
7. 🔷 MTF Squeeze Alignment

Each alert includes the squeeze state, momentum value, and HTF context.

## Key Features

- **Squeeze detection** — Bollinger Bands vs Keltner Channels with colour-coded dots
- **Momentum oscillator** — Linear Regression + RSI hybrid histogram for directional bias
- **Multi-timeframe squeeze** — Higher timeframe squeeze state on your trading chart
- **4 divergence types** — Regular + Hidden, Bullish + Bearish
- **7 alert conditions** — Squeeze fire, zero cross, divergence, MTF alignment
- **Configurable inputs** — BB length/multiplier, KC length/multiplier, momentum period, MTF resolution
- **Clean visuals** — Professional colour scheme (cyan/magenta/orange), separate pane
- **Zero repaint** — All signals confirmed on bar close
- **All markets** — stocks, crypto, forex, futures, indices

## Pros & Cons

**Pros:**
- Momentum oscillator gives directional bias BEFORE the squeeze fires — genuine edge
- MTF squeeze overlay adds institutional-grade context without switching charts
- Pivot-based divergence detection on the momentum histogram catches reversals
- Seven alert conditions cover every scenario — fire, cross, divergence, alignment
- Clean, uncluttered visuals — no kitchen-sink mess
- One-time purchase, no subscription

**Cons:**
- $25 (paid) — free TTM Squeezes exist, they just lack MTF, divergence, and alerts
- Squeeze dots can lag in choppy markets (fire → immediately re-squeeze)
- Learning curve — understanding squeeze mechanics takes practice
- Separate pane required (not an overlay)

## Setup Guide

1. **Install** — Add to chart from TradingView indicator panel (separate pane)
2. **Configure** — Set BB length (default 20), KC multiplier (default 1.5), momentum period (default 20)
3. **Enable MTF** — Set to 1 level above your chart timeframe for context
4. **Set alerts** — Alt+A → Condition dropdown → "Squeeze Fire (Bullish)" / "Momentum Zero Cross" → Push notification → Create

Recommended starting settings:
- BTC/USD 15m: BB 20×2.0, KC 20×1.5, Momentum 20, MTF 1h
- AAPL/NVDA 1h: BB 20×2.0, KC 20×1.5, Momentum 20, MTF 4h
- SPY Daily: BB 20×2.0, KC 20×1.5, Momentum 20, MTF Weekly

## Who Is This For?

- **Momentum traders** who want to catch explosive directional moves at inception
- **Squeeze traders** already using the TTM Squeeze who want MTF context and alerts
- **Multi-timeframe traders** who want higher timeframe squeeze state without switching charts
- **Crypto traders** who need phone alerts for fast-moving squeeze fires

## Alternatives

- **Standard TTM Squeeze** — Single timeframe, no divergence, no alerts, basic visuals
- **Bollinger Band Squeeze** — BB-only squeeze without Keltner confirmation, fewer signals
- **Keltner Channel Breakout** — KC-only approach, misses the compression phase entirely

## Final Verdict

**Rating: ⭐⭐⭐⭐⭐ (5/5)**

TTM Squeeze Pro transforms the classic squeeze concept into a professional-grade trading tool. The momentum oscillator alone is worth the price — it gives you directional bias while the squeeze is still coiling, which is when the best entries happen. Add MTF context, divergence scanning, and phone alerts, and you have the definitive squeeze indicator on TradingView.

If you're already using a free TTM Squeeze, upgrade immediately — the MTF overlay and alerts will pay for this in one caught move. If you've never used a squeeze indicator, start here. It's the complete package.

[Get TTM Squeeze Pro on TradingView →](https://www.tradingview.com/script/fM2r5hCG-TTM-Squeeze-Pro-Multi-Timeframe-Squeeze-Divergence-Alerts/)

{{< rawhtml >}}
<div style="margin-top:2rem;padding:1.5rem;background:var(--card-bg);border-radius:var(--radius-lg);text-align:center;font-size:1.15rem;color:var(--text-muted);">
  <strong>Want all Lab Originals?</strong> <a href="/the-lab-report/" style="color:var(--primary);">The Lab Report</a> gives you every script + consensus signals for one subscription.
</div>
{{< /rawhtml >}}

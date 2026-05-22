---
title: "Whale Liquidity / Absorption Profile — Pro Review"
date: 2026-05-21
draft: false
type: reviews
tags:
  - whale
  - liquidity
  - absorption
  - order-flow
  - volume
  - institutional
  - smart-money
  - pro
categories:
  - Pro
  - Volume
rating: 5
image: "/screenshots/whale-liquidity-absorption.png"
description: "Whale Liquidity / Absorption Profile — Detect when institutions are accumulating. Absorption signals + liquidity zones + Whale Activity Score. Phone alerts. Trade what whales trade. Built by The Indicator Lab."
---

## Overview

Volume indicators tell you how much traded. But they don't tell you WHO is trading or WHAT they're doing. When institutions accumulate, price stays flat while volume spikes — that's absorption. Most retail traders miss it because no free indicator detects it. By the time price moves, the whales are already positioned.

Whale Liquidity / Absorption Profile combines three order flow techniques into one indicator: absorption detection, liquidity zone mapping, and a Whale Activity Score. This is institutional-grade analysis on your TradingView chart — no footprint charts, no DOM, just the signals that matter.

<!--more-->

## How It Works

### Absorption Detection
Absorption is the fingerprint of institutional activity. When abnormal volume meets compressed price range, someone is absorbing the other side:

- **Volume threshold:** Current volume > VMA × multiplier (default 2.0x — configurable)
- **Range compression:** True Range < ATR × compression factor (default 0.5x)
- **Absorption signal:** Both conditions fire simultaneously
- **Bull/Bear bias:** Close vs open on the absorption candle determines direction

```
Absorption = (Volume > VMA × 2.0) AND (TrueRange < ATR × 0.5)
Bull Absorption = Absorption AND Close > Open
Bear Absorption = Absorption AND Close < Open
```

When you get **consecutive absorption bars** — multiple candles in a row meeting both criteria — the signal is significantly stronger. This is the whale loading up or distributing over time without moving price.

### Liquidity Zone Mapping
When absorption is detected, the indicator records the price zone (high-low of the absorption cluster) and draws a **persistent horizontal box**. These zones remain on your chart until price trades through them — showing you exactly where institutions built positions.

- **Zone strength** — Cumulative volume absorbed within the zone determines opacity and significance
- **Zone persistence** — Boxes stay until price breaks through (zone "absorbed back")
- **Support/resistance flip** — When price breaks a zone, it often flips from support to resistance (or vice versa)
- **Max zones** — Configurable (default 10) to keep charts clean

### Volume Footprint
Volume bars are colour-coded based on their abnormal-activity level:

| Colour | Threshold | Meaning |
|--------|-----------|---------|
| Gray | < 1.5× VMA | Normal volume |
| Yellow | 1.5× – 2.0× VMA | Elevated |
| Orange | 2.0× – 3.0× VMA | High — potential absorption |
| Red | > 3.0× VMA | Extreme — almost certainly institutional |

This gives you an instant visual read: red volume bars in a tight range = absorption happening right now.

### Whale Activity Score (WAS)
The WAS is a composite 0-100 score that quantifies institutional presence. It combines four factors:

| Component | Weight | What It Measures |
|-----------|--------|-----------------|
| Volume abnormality | 40% | How far current volume deviates from VMA |
| Range compression | 30% | How compressed price range is vs ATR |
| Absorption continuity | 20% | Consecutive absorption bars (cluster strength) |
| Zone cluster density | 10% | How many active liquidity zones overlap |

- **WAS > 60:** Elevated whale activity — pay attention
- **WAS > 80:** Extreme whale activity — high probability setup, alerts fire

The WAS line plots in a separate pane alongside volume bars, giving you a continuous institutional-presence gauge.

### Phone Alerts
Six alert conditions after connecting TradingView alerts:

1. 🟢 Bull Absorption Signal
2. 🔴 Bear Absorption Signal
3. 📈 WAS crosses above 60
4. 📈📈 WAS crosses above 80
5. 🚀 Zone Breakout (price breaks above a liquidity zone)
6. 💥 Zone Breakdown (price breaks below a liquidity zone)
7. 🔁 Absorption Cluster (3+ consecutive absorption bars)

## Key Features

- **Absorption detection** — Volume > VMA × multiplier AND True Range < ATR × compression factor
- **Liquidity zone mapping** — Persistent horizontal boxes at absorption clusters, fading over time
- **Whale Activity Score (WAS)** — Composite 0-100 institutional-presence gauge
- **Volume footprint** — Colour-coded bars (gray/yellow/orange/red) for instant volume-abnormality read
- **Consecutive absorption** — Stronger signal when multiple absorption bars cluster together
- **6 alert conditions** — Absorption, WAS thresholds, zone breaks, clusters
- **Zero repaint** — All signals confirmed on bar close
- **Institutional aesthetic** — Dark-theme compatible, clean, professional
- **All markets** — stocks, crypto, forex, futures, indices (works best on 1h–Daily)

## Pros & Cons

**Pros:**
- The only indicator on TV that combines absorption, liquidity zones, AND a composite activity score
- Liquidity zone persistence is genuinely useful — seeing where institutions built positions days ago
- WAS composite score removes subjectivity — a single number tells you if whales are active
- Volume footprint colour-coding makes abnormal volume instantly visible
- Consecutive absorption cluster detection catches methodical accumulation/distribution
- One-time purchase, no subscription

**Cons:**
- $35 (paid) — highest-priced Lab Original, but also the most sophisticated
- Requires understanding of order flow concepts (absorption, liquidity zones, volume footprint)
- Less effective on very low timeframes (sub-15m — noise dominates)
- WAS can stay elevated in prolonged high-volatility periods (earnings, FOMC)

## Setup Guide

1. **Install** — Add to chart from TradingView indicator panel (separate pane)
2. **Configure** — Set volume multiplier (2.0 is standard, lower to 1.5 for active stocks, raise to 3.0 for crypto)
3. **Set compression factor** — 0.5 is default; lower = stricter absorption, higher = more signals
4. **Set alerts** — Alt+A → Condition → "Bull Absorption Signal" / "WAS Crosses Above 60" → Push notification

Recommended starting settings:
- AAPL/NVDA 1h: Vol multiplier 2.0, Compression 0.5, VMA 20, ATR 14
- BTC/USD 4h: Vol multiplier 2.5, Compression 0.4, VMA 20, ATR 14
- SPY 1h: Vol multiplier 1.8, Compression 0.5, VMA 20, ATR 14
- Forex Daily: Vol multiplier 2.0, Compression 0.5, VMA 20, ATR 14

## Who Is This For?

- **Order flow traders** who understand absorption and want it on TradingView
- **Volume analysts** who want institutional-presence quantification beyond standard volume indicators
- **Swing traders** who want to position alongside whale accumulation before the move
- **Crypto traders** who need to spot exchange-level absorption in 4h-Daily timeframes

## Alternatives

- **Volume Profile** — Shows volume at price levels, but no absorption detection or WAS
- **CVD (Cumulative Volume Delta)** — Shows buying vs selling pressure, but no zone mapping or activity scoring
- **Market Facilitation Index** — Measures price movement per volume unit, but no cluster or zone tracking

## Final Verdict

**Rating: ⭐⭐⭐⭐⭐ (5/5)**

Whale Liquidity / Absorption Profile is the most sophisticated Lab Original. It solves a real problem that no other TradingView indicator addresses: quantifying institutional presence without a footprint chart or DOM. The WAS composite score alone is a tool you won't find anywhere else on the platform.

At $35, it's priced for serious traders who already understand order flow. If that's you, this indicator will change how you read volume. If you're new to absorption concepts, start with CVD Divergence Alerts ($25) first and graduate to this.

[Get Whale Liquidity / Absorption Profile on TradingView →](https://www.tradingview.com/script/ksAw7irF-Whale-Liquidity-Absorption-Profile-Institutional-Order-Flow/)

{{< rawhtml >}}
<div style="margin-top:2rem;padding:1.5rem;background:var(--card-bg);border-radius:var(--radius-lg);text-align:center;font-size:1.15rem;color:var(--text-muted);">
  <strong>Want all Lab Originals?</strong> <a href="/the-lab-report/" style="color:var(--primary);">The Lab Report</a> gives you every script + consensus signals for one subscription.
</div>
{{< /rawhtml >}}

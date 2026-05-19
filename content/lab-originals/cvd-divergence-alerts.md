---
title: "CVD Divergence Alerts"
date: 2026-05-18
draft: false
type: lab-originals
price: "$25"
status: "Available on TradingView"
image: "/screenshots/cvd-divergence-alerts.png"
description: "The only CVD indicator on TradingView that watches the chart for you. 4 divergence types, phone alerts, zero repaint."
---

{{< rawhtml >}}
<div style="background: #1a1b2e; border-radius: 12px; padding: 2rem; margin-bottom: 2rem; border: 1px solid rgba(255,255,255,0.1);">
  <div style="display: flex; gap: 1.5rem; flex-wrap: wrap; align-items: center;">
    <div>
      <h2 style="margin: 0 0 0.5rem; font-size: 1.5rem;">CVD Divergence Alerts</h2>
      <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 1rem;">
        <span style="background: #00bcd4; color: #000; padding: 2px 10px; border-radius: 4px; font-size: 0.85rem; font-weight: bold;">VOLUME</span>
        <span style="background: #4caf50; color: #fff; padding: 2px 10px; border-radius: 4px; font-size: 0.85rem;">$25 ONE-TIME</span>
        <span style="background: #ff9800; color: #000; padding: 2px 10px; border-radius: 4px; font-size: 0.85rem;">PHONE ALERTS</span>
      </div>
      <p style="margin: 0; color: #ccc; font-size: 0.95rem;">Cumulative Volume Delta + divergence detection + TradingView push notifications. The only CVD script that tells you when something happens instead of making you watch the histogram.</p>
    </div>
  </div>
</div>
{{< /rawhtml >}}

## What It Does

Every free CVD on TradingView is a coloured histogram. To find divergences between volume and price, you compare swing highs and lows manually — bar by bar, timeframe by timeframe. This script automates that entire process.

**Four divergence types, one install:**

| Signal | What It Means | Action |
|--------|--------------|--------|
| 🟢 Bullish Regular | Price lower low, CVD higher low | Buyers accumulating — reversal up |
| 🔴 Bearish Regular | Price higher high, CVD lower high | Distribution at highs — reversal down |
| 🟡 Hidden Bullish | Price higher low, CVD lower low | Accumulation during retrace — continuation |
| 🟠 Hidden Bearish | Price lower high, CVD higher high | Selling into pullback — continuation |

**Three CVD calculation methods:** Direction (equities/futures), Volume-Weighted (crypto), Close Location (forex).

## Key Features

- **4 divergence types** — regular + hidden, bullish + bearish
- **Phone alerts** — push notification via TradingView when a divergence fires
- **No repaint** — all signals confirmed on bar close
- **Pivot-based** — uses ta.pivothigh/pivotlow, not crossover logic (dramatically fewer false signals)
- **Alert debounce** — configurable cooldown prevents notification fatigue
- **3 CVD methods** — adapts to your market
- **Clean chart markers** — colour-coded B/S/BH/SH labels on every signal

## Technical Specs

| Detail | Value |
|--------|-------|
| Pine Script version | v6 |
| Price | $25 (one-time) |
| Timeframes | All (optimized for 15m–4h) |
| Markets | Stocks, crypto, forex, futures, indices |
| Alerts | Push, email, SMS, or webhook via TradingView |

## Who This Is For

- **Active traders** who use volume analysis and want to stop staring at charts
- **Swing traders** looking for reversal + continuation signals with volume confirmation
- **Multi-chart traders** who can't monitor CVD on 5 timeframes manually
- **Crypto traders** who need phone alerts for fast-moving markets

## Setup

1. Install from TradingView
2. Open Alert dialog (Alt+A) → "alert() function calls" → Push notification → Create
3. Walk away — phone buzzes when CVD diverges from price

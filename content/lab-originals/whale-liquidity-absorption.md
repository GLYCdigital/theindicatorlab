---
title: "Whale Liquidity / Absorption Profile"
date: 2026-05-22
draft: false
type: lab-originals
price: "$35"
status: "Available on TradingView"
categories: ["Volume"]
tags: ["whale", "liquidity", "absorption", "volume", "institutional", "order-flow"]
image: "/screenshots/whale-liquidity-absorption.png"
description: "Detect institutional accumulation before price moves.<br>Absorption signals, liquidity zones, Whale Activity Score, phone alerts."
---

{{< rawhtml >}}
<div style="background: var(--card-bg); border-radius: var(--radius-lg); padding: 2rem; margin-bottom: 2rem; border: 2px solid var(--accent);">
  <div style="display: flex; gap: 1.5rem; flex-wrap: wrap; align-items: center;">
    <div>
      <h2 style="margin: 0 0 0.5rem; font-size: 2.2rem; color: var(--text);">Whale Liquidity / Absorption Profile</h2>
      <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 1rem;">
        <span style="background: var(--accent); color: #fff; padding: 4px 14px; border-radius: 20px; font-size: 1.15rem; font-weight: 600;">VOLUME</span>
        <span style="background: var(--accent); color: #fff; padding: 4px 14px; border-radius: 20px; font-size: 1.15rem; font-weight: 600;">$35 ONE-TIME</span>
        <span style="background: var(--green); color: #fff; padding: 4px 14px; border-radius: 20px; font-size: 1.15rem; font-weight: 600;">PHONE ALERTS</span>
      </div>
      <p style="margin: 0; color: var(--text-secondary); font-size: 1.4rem; line-height: 1.6;">The only TradingView indicator that quantifies institutional presence without a footprint chart.<br>Absorption detection + liquidity zone mapping + Whale Activity Score — no DOM required.</p>
    </div>
  </div>
</div>
{{< /rawhtml >}}

{{< rawhtml >}}
<div style="margin: 2rem 0; border-radius: var(--radius-lg); overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.15);">
  <img src="/screenshots/whale-liquidity-absorption.png" alt="Whale Liquidity chart screenshot" style="width:100%;display:block;">
</div>
{{< /rawhtml >}}

## What It Does

Volume indicators tell you how much traded. They don't tell you *who* is trading or *what* they're doing. When institutions accumulate, price stays flat while volume spikes — that's absorption. Most traders miss it because no free indicator detects it. By the time price moves, the whales are already positioned.

This script combines three order flow techniques into one indicator — no footprint charts, no DOM, just the signals that matter.

**1. Absorption Detection**

When abnormal volume meets compressed price range, someone is absorbing the other side:

```
Absorption = (Volume > VMA × 2.0) AND (TrueRange < ATR × 0.5)
```

Consecutive absorption bars — multiple candles meeting both criteria — are the strongest signal. That's the whale loading up or distributing over time without moving price.

**2. Liquidity Zone Mapping**

When absorption fires, the indicator records the price zone and draws a persistent box. These zones stay on your chart until price breaks through — showing you exactly where institutions built positions. When price trades through a zone, it often flips from support to resistance.

**3. Whale Activity Score (WAS)**

A composite 0–100 gauge that quantifies institutional presence. Combines volume abnormality (40%), range compression (30%), absorption continuity (20%), and zone density (10%).

| WAS Level | Meaning |
|-----------|---------|
| 0–40 | Normal market — retail-driven |
| 40–60 | Elevated — pay attention |
| 60–80 | High whale activity — alerts fire |
| 80–100 | Extreme — institutions are active NOW |

**4. Volume Footprint**

Volume bars are color-coded by abnormality: Gray (normal), Yellow (1.5× VMA), Orange (2.0×), Red (3.0×+ — almost certainly institutional). Red bars in a tight range = absorption happening right now.

## Key Features

- **Absorption detection** — Volume > VMA × multiplier AND True Range < ATR × compression factor
- **Liquidity zone mapping** — Persistent boxes at absorption clusters until price breaks through
- **Whale Activity Score (WAS)** — Composite 0–100 institutional presence gauge
- **Volume footprint** — Color-coded bars (gray → yellow → orange → red)
- **Consecutive absorption** — Cluster detection for methodical accumulation/distribution
- **7 phone alerts** — Bull/bear absorption, WAS 60/80 cross, zone breakout/breakdown, absorption cluster
- **No repaint** — All signals confirmed on bar close
- **All markets** — Stocks, crypto, forex, futures, indices (best: 1h–Daily)

## Technical Specs

| Detail | Value |
|--------|-------|
| Pine Script version | v6 |
| Price | $35 (one-time) |
| Timeframes | All (optimized for 1h–Daily) |
| Markets | Stocks, crypto, forex, futures, indices |
| Alerts | Push, email, SMS, or webhook via TradingView |

## Who This Is For

- **Order flow traders** who understand absorption and want it on TradingView
- **Volume analysts** who want institutional presence quantification beyond standard indicators
- **Swing traders** who want to position alongside whale accumulation *before* the move
- **Crypto traders** who need to spot exchange-level absorption in 4h–Daily timeframes
- **Serious traders** who understand that reading volume is reading intent

## Setup

1. Install from TradingView (separate pane)
2. Configure: Volume Multiplier (2.0 standard), Compression Factor (0.5 standard)
3. Watch for red volume bars + WAS > 60 — that's whales active
4. Open Alert dialog (Alt+A) → "alert() function calls" → Push notification → Create
5. Phone buzzes when WAS crosses 60, 80, or absorption fires

{{< rawhtml >}}
<div style="text-align:center;padding:2rem 0 3rem;">
  <a href="https://buy.stripe.com/cNi28j0TA5lG5PocyZaAw05" class="lr-cta" style="background:var(--accent);color:#fff!important;font-weight:700;padding:18px 52px;border-radius:var(--radius);font-size:1.6rem;text-decoration:none!important;box-shadow:0 2px 8px rgba(232,119,34,.3);">Get Whale Liquidity / Absorption Profile — $35</a>
  <p style="margin-top:1rem;font-size:1.25rem;color:var(--text-muted);">Invite-only access · Lifetime · One-time purchase</p>
  <p style="margin-top:0.5rem;font-size:1.15rem;color:var(--text-muted);">After purchase, your TradingView username will be added to the script within 24 hours.</p>
</div>
{{< /rawhtml >}}

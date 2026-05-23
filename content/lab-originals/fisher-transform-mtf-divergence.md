---
title: "Fisher Transform MTF Divergence"
date: 2026-05-20
draft: false
type: lab-originals
price: "$20"
status: "Available on TradingView"
categories: ["Momentum"]
tags: ["fisher", "transform", "divergence", "momentum", "mtf", "reversal"]
image: "/screenshots/fisher-transform-mtf-divergence.png"
description: "Multi-timeframe Fisher Transform + automated divergence scanning.<br>The Fisher that actually finds reversals for you."
---

{{< rawhtml >}}
<div style="background: var(--card-bg); border-radius: var(--radius-lg); padding: 2rem; margin-bottom: 2rem; border: 2px solid var(--primary);">
  <div style="display: flex; gap: 1.5rem; flex-wrap: wrap; align-items: center;">
    <div>
      <h2 style="margin: 0 0 0.5rem; font-size: 2.2rem; color: var(--text);">Fisher Transform MTF Divergence</h2>
      <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 1rem;">
        <span style="background: var(--primary); color: #fff; padding: 4px 14px; border-radius: 20px; font-size: 1.15rem; font-weight: 600;">MOMENTUM</span>
        <span style="background: var(--accent); color: #fff; padding: 4px 14px; border-radius: 20px; font-size: 1.15rem; font-weight: 600;">$20 ONE-TIME</span>
        <span style="background: var(--green); color: #fff; padding: 4px 14px; border-radius: 20px; font-size: 1.15rem; font-weight: 600;">MULTI-TIMEFRAME</span>
      </div>
      <p style="margin: 0; color: var(--text-secondary); font-size: 1.4rem; line-height: 1.6;">Fisher Transform with higher-timeframe overlay + 4 divergence types + phone alerts.<br>The definitive Fisher — MTF context, divergence scanning, auto-alerts.</p>
    </div>
  </div>
</div>
{{< /rawhtml >}}

{{< rawhtml >}}
<div style="margin: 2rem 0; border-radius: var(--radius-lg); overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.15);">
  <img src="/screenshots/fisher-transform-mtf-divergence.png" alt="Fisher Transform MTF Divergence chart screenshot" style="width:100%;display:block;">
</div>
{{< /rawhtml >}}

## What It Does

The standard Fisher Transform on TradingView is single-timeframe with no divergence detection. You have to watch it. You have to scan for divergences manually. You have to switch timeframes for context.

This script fixes all three:
1. **Multi-timeframe Fisher** — a higher-timeframe Fisher line overlays your main chart (e.g. 4h Fisher on a 1h chart)
2. **Automated divergence scanning** — 4 divergence types detected via pivot-based logic
3. **Phone alerts** — push notification when Fisher crosses, diverges, or breaks OB/OS zones

## Key Features

- **MTF Fisher overlay** — HTF Fisher line on your trading chart (configurable: 5m to Weekly)
- **4 divergence types** — Regular Bullish/Bearish + Hidden Bullish/Bearish
- **Pivot-based detection** — `ta.pivothigh`/`ta.pivotlow`, not crossover noise
- **Trigger line crossovers** — Fisher crosses signal line for faster entries
- **OB/OS zones** — Configurable overbought/oversold with fill zones
- **Phone alerts** — push notification for crossovers, divergences, zone breaks (8 alert conditions)
- **Colour-coded histogram** — Fisher direction and momentum intensity at a glance
- **Zero repaint** — all signals barstate-confirmed
- **All markets** — stocks, crypto, forex, futures

## Technical Specs

| Detail | Value |
|--------|-------|
| Pine Script version | v6 |
| Price | $20 (one-time) |
| Timeframes | All (optimized for 15m–4h) |
| Markets | Stocks, crypto, forex, futures, indices |
| Alerts | Push, email, SMS, or webhook (8 alert conditions) |

## Who This Is For

- **Reversal traders** who want the sharpest turning-point detection available
- **Momentum traders** who want HTF context without switching charts
- **Divergence traders** who want automated scanning instead of manual comparison
- **Crypto traders** who need fast reversal signals in volatile markets

## Setup

1. Install from TradingView (separate pane)
2. Set Fisher length (default 10), enable MTF at 1 level above your chart TF
3. Adjust OB/OS levels (±2.0 for crypto, ±1.5 for stocks/forex)
4. Open Alert dialog (Alt+A) → "Fisher Bullish Crossover" / "Bullish Divergence" → Push notification → Create
5. When both Fishers agree on direction + you get a divergence alert → high-conviction setup

{{< rawhtml >}}
<div style="text-align:center;padding:2rem 0 3rem;">
  <a href="https://buy.stripe.com/9B6bIT7hYeWgelU2YpaAw01" class="lr-cta" style="background:var(--accent);color:#fff!important;font-weight:700;padding:18px 52px;border-radius:var(--radius);font-size:1.6rem;text-decoration:none!important;box-shadow:0 2px 8px rgba(232,119,34,.3);">Get Fisher Transform MTF — $20</a>
  <p style="margin-top:1rem;font-size:1.25rem;color:var(--text-muted);">Invite-only access · Lifetime · One-time purchase</p>
  <p style="margin-top:0.5rem;font-size:1.15rem;color:var(--text-muted);">After purchase, your TradingView username will be added to the script within 24 hours.</p>
</div>
{{< /rawhtml >}}

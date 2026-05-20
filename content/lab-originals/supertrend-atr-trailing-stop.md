---
title: "SuperTrend + ATR Trailing Stop"
date: 2026-05-20
draft: false
type: lab-originals
price: "$15"
status: "Available on TradingView"
image: "/screenshots/supertrend-atr-trailing-stop.png"
description: "SuperTrend entries plus independent ATR trailing stop.<br>Entry AND exit in one view. No more guessing stop placement."
---

{{< rawhtml >}}
<div style="background: var(--card-bg); border-radius: var(--radius-lg); padding: 2rem; margin-bottom: 2rem; border: 2px solid var(--primary);">
  <div style="display: flex; gap: 1.5rem; flex-wrap: wrap; align-items: center;">
    <div>
      <h2 style="margin: 0 0 0.5rem; font-size: 2.2rem; color: var(--text);">SuperTrend + ATR Trailing Stop</h2>
      <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 1rem;">
        <span style="background: var(--primary); color: #fff; padding: 4px 14px; border-radius: 20px; font-size: 1.15rem; font-weight: 600;">TREND</span>
        <span style="background: var(--accent); color: #fff; padding: 4px 14px; border-radius: 20px; font-size: 1.15rem; font-weight: 600;">$15 ONE-TIME</span>
        <span style="background: var(--green); color: #fff; padding: 4px 14px; border-radius: 20px; font-size: 1.15rem; font-weight: 600;">AUTO STOP-LOSS</span>
      </div>
      <p style="margin: 0; color: var(--text-secondary); font-size: 1.4rem; line-height: 1.6;">SuperTrend entries + independent ATR trailing stop.<br>The SuperTrend that doesn't abandon you after the entry signal.</p>
    </div>
  </div>
</div>
{{< /rawhtml >}}

## What It Does

Standard SuperTrend gives you entries. Then it goes silent. You're left staring at the chart wondering where to place your stop, whether to trail manually, and when to exit.

This script adds an independent ATR-based trailing stop that ratchets with price movement. Entry AND exit. Mechanical. No guesswork.

**Two lines, one view:**

| Line | What It Does | Default |
|------|-------------|---------|
| SuperTrend | Entry signals — flips when trend changes | ATR 10 × 3.0 |
| ATR Trailing Stop | Exit level — ratchets up in uptrends, never drops | ATR 14 × 2.0 |

Independent ATR periods mean you can keep entries responsive while giving stops room to breathe.

## Key Features

- **SuperTrend entries** — flip-based buy/sell signals with chart labels
- **ATR trailing stop** — independent line that ratchets with price, never widens against you
- **Stop-hit alerts** — phone notification when price pierces your trailing stop
- **Re-entry signals** — SuperTrend flips back after stop-out, you get a re-entry alert
- **Info table** — current ATR value, stop distance %, trend direction at a glance
- **Three display modes** — SuperTrend only, ATR Stop only, or Both
- **Zero repaint** — all signals confirmed on bar close
- **All markets** — stocks, crypto, forex, futures

## Technical Specs

| Detail | Value |
|--------|-------|
| Pine Script version | v6 |
| Price | $15 (one-time) |
| Timeframes | All (optimized for 15m–4h) |
| Markets | Stocks, crypto, forex, futures, indices |
| Alerts | Push, email, SMS, or webhook (4 alert conditions) |

## Who This Is For

- **Swing traders** who want mechanical entries with pre-defined stop levels
- **Crypto traders** who need wider stops for volatile markets
- **Trend followers** who want to stay in trades with a trailing stop mechanism
- **Beginners** who struggle with "where do I place my stop?" indecision

## Setup

1. Install from TradingView (overlay mode)
2. Set SuperTrend ATR (10 for active, 20 for swing) and multiplier (2.5–3.0)
3. Set Trailing Stop ATR (14–20) and multiplier (1.5–2.0)
4. Open Alert dialog (Alt+A) → "ST Bullish Entry" / "Stop Hit" → Push notification → Create
5. Enter on flips, exit on stop hits, re-enter on re-entry signals

{{< rawhtml >}}
<div style="text-align:center;padding:2rem 0 3rem;">
  <a href="https://www.tradingview.com/script/dH3ujrk1-SuperTrend-ATR-Trailing-Stop-Entry-Exit-in-One-View/" class="lr-cta" style="background:var(--accent);color:#fff!important;font-weight:700;padding:18px 52px;border-radius:var(--radius);font-size:1.6rem;text-decoration:none!important;box-shadow:0 2px 8px rgba(232,119,34,.3);">Get SuperTrend + ATR on TradingView — $15</a>
  <p style="margin-top:1rem;font-size:1.25rem;color:var(--text-muted);">Invite-only access · Lifetime · One-time purchase</p>
</div>
{{< /rawhtml >}}

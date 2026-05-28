---
title: "TTM Squeeze Pro"
date: 2026-05-22
draft: false
type: lab-originals
price: "$25"
status: "Available on TradingView"
categories: ["Volatility"]
tags: ["ttm", "squeeze", "volatility", "momentum", "mtf", "bollinger", "keltner"]
image: "/screenshots/ttm-squeeze-pro.png"
description: "John Carter's Squeeze on steroids.<br>Multi-timeframe detection, momentum oscillator, 4 divergence types, 7 phone alerts."
---

{{< rawhtml >}}
<div style="background: var(--card-bg); border-radius: var(--radius-lg); padding: 2rem; margin-bottom: 2rem; border: 2px solid var(--accent);">
  <div style="display: flex; gap: 1.5rem; flex-wrap: wrap; align-items: center;">
    <div>
      <h2 style="margin: 0 0 0.5rem; font-size: 2.2rem; color: var(--text);">TTM Squeeze Pro</h2>
      <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 1rem;">
        <span style="background: var(--accent); color: #fff; padding: 4px 14px; border-radius: 20px; font-size: 1.15rem; font-weight: 600;">VOLATILITY</span>
        <span style="background: var(--accent); color: #fff; padding: 4px 14px; border-radius: 20px; font-size: 1.15rem; font-weight: 600;">$25 ONE-TIME</span>
        <span style="background: var(--green); color: #fff; padding: 4px 14px; border-radius: 20px; font-size: 1.15rem; font-weight: 600;">PHONE ALERTS</span>
      </div>
      <p style="margin: 0; color: var(--text-secondary); font-size: 1.4rem; line-height: 1.6;">Multi-timeframe squeeze detection + Linear Regression momentum oscillator + 4 divergence types.<br>See the squeeze fire on your chart AND your higher timeframe — with phone alerts for all 7 signal types.</p>
    </div>
  </div>
</div>
{{< /rawhtml >}}

{{< rawhtml >}}
<div style="margin: 2rem 0; border-radius: var(--radius-lg); overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.15);">
  <img src="/screenshots/ttm-squeeze-pro.png" alt="TTM Squeeze Pro chart screenshot" style="width:100%;display:block;">
</div>
{{< /rawhtml >}}

## What It Does

The TTM Squeeze tells you when volatility is coiling — Bollinger Bands contract inside Keltner Channels, energy builds, and price explodes when the squeeze "fires." Every free version stops there. Single timeframe, no alerts, no divergence.

TTM Squeeze Pro adds three layers most traders never see:

**1. Momentum Oscillator (Linear Regression slope)**

The histogram shows momentum direction while the squeeze is still active. Lime rising = bulls loading up. Red rising = bears positioning. You get directional bias *before* the squeeze fires — that's the edge.

**2. Multi-Timeframe Squeeze**

A second dot row (or background tint) shows the higher timeframe squeeze state on your chart. 4h squeeze firing on a 1h chart = institutional backing. When both timeframes align, it's the highest-conviction setup.

**3. Divergence Detection**

Four divergence types on the momentum histogram vs price: regular bullish/bearish (reversals) + hidden bullish/bearish (continuations). Pivot-based, no noise.

| Signal | Pattern | Meaning |
|--------|---------|---------|
| 🟢 Bullish Regular | Price LL, Momentum HL | Momentum turning — reversal buy |
| 🔴 Bearish Regular | Price HH, Momentum LH | Momentum fading — reversal sell |
| 🟡 Hidden Bullish | Price HL, Momentum LL | Building on retrace — continuation |
| 🟠 Hidden Bearish | Price LH, Momentum HH | Fading on pullback — continuation |

## Key Features

- **Squeeze detection** — Bollinger vs Keltner with red/green/gray dots
- **Momentum oscillator** — Linear Regression slope histogram with directional coloring
- **Multi-timeframe squeeze** — HTF squeeze state as background tint or secondary dots
- **4 divergence types** — Regular + Hidden on momentum vs price
- **7 phone alerts** — Squeeze fire (bull/bear), zero cross (up/down), divergence (bull/bear), MTF alignment
- **No repaint** — All signals confirmed on bar close
- **Clean visuals** — Separate pane, professional color scheme
- **All markets** — Stocks, crypto, forex, futures, indices

## Technical Specs

| Detail | Value |
|--------|-------|
| Pine Script version | v6 |
| Price | $25 (one-time) |
| Timeframes | All (best: 15m–4h) |
| Markets | Stocks, crypto, forex, futures, indices |
| Alerts | Push, email, SMS, or webhook via TradingView |

## Backtest Results

<p style="font-size:1.1rem;color:var(--text-secondary);margin-bottom:0.5rem">6 assets tested · 438 total trades · 5-year data · Refreshed weekly</p>

<article class="review-article">
  <div class="content">

<table>
<thead>
<tr>
  <th>Asset</th>
  <th>Return</th>
  <th>Sharpe</th>
  <th>Max DD</th>
  <th>Win Rate</th>
  <th>PF</th>
  <th>Trades</th>
</tr>
</thead>
<tbody>
<tr><td>🟢 <a href="/backtests/ttm-squeeze-pro-tsla/" style="color:var(--accent);text-decoration:none;font-weight:600">TSLA</a></td><td>+131.5%</td><td>0.53</td><td>39.9%</td><td>29.2%</td><td>1.37</td><td>65</td></tr>
<tr><td>🟡 <a href="/backtests/ttm-squeeze-pro-qqq/" style="color:var(--accent);text-decoration:none;font-weight:600">QQQ</a></td><td>+56.7%</td><td>0.45</td><td>20.1%</td><td>32.3%</td><td>1.34</td><td>65</td></tr>
<tr><td>🟡 <a href="/backtests/ttm-squeeze-pro-aapl/" style="color:var(--accent);text-decoration:none;font-weight:600">AAPL</a></td><td>+56.7%</td><td>0.41</td><td>26.4%</td><td>40.4%</td><td>1.32</td><td>52</td></tr>
<tr><td>🟡 <a href="/backtests/ttm-squeeze-pro-btc-usd/" style="color:var(--accent);text-decoration:none;font-weight:600">BTC</a></td><td>+51.5%</td><td>0.32</td><td>53.8%</td><td>23.8%</td><td>1.18</td><td>101</td></tr>
<tr><td>🟡 <a href="/backtests/ttm-squeeze-pro-eth-usd/" style="color:var(--accent);text-decoration:none;font-weight:600">ETH</a></td><td>+30.3%</td><td>0.22</td><td>44.0%</td><td>21.7%</td><td>1.08</td><td>92</td></tr>
<tr><td>🟡 <a href="/backtests/ttm-squeeze-pro-spy/" style="color:var(--accent);text-decoration:none;font-weight:600">SPY</a></td><td>+19.4%</td><td>0.15</td><td>21.8%</td><td>39.7%</td><td>1.09</td><td>63</td></tr>
</tbody>
</table>

<p style="margin-top:1rem;font-size:1.1rem;color:var(--text-secondary)">🟢 Sharpe > 0.5 · 🟡 0–0.5 · 🔴 Negative</p>

<p style="margin-top:1rem"><a href="/backtests/ttm-squeeze-pro/" style="color:var(--accent);font-weight:600">→ Full backtest details and charts</a></p>

  </div>
</article>


## Who This Is For

- **Squeeze traders** who already use TTM Squeeze and want MTF context + alerts
- **Momentum traders** who want to catch explosive moves at inception
- **Multi-timeframe traders** who want HTF squeeze without switching charts
- **Crypto traders** who need phone alerts for fast squeeze fires

## Setup

1. Install from TradingView (separate pane below price)
2. Set MTF resolution to 1 level above your chart (e.g., 4h on a 1h chart)
3. Open Alert dialog (Alt+A) → "alert() function calls" → Push notification → Create
4. Walk away — phone buzzes when the squeeze fires or momentum crosses zero

{{< rawhtml >}}
<div style="text-align:center;padding:2rem 0 3rem;">
  <a href="https://buy.stripe.com/4gM4grfOu7tOb9I42taAw04" class="lr-cta" style="background:var(--accent);color:#fff!important;font-weight:700;padding:18px 52px;border-radius:var(--radius);font-size:1.6rem;text-decoration:none!important;box-shadow:0 2px 8px rgba(232,119,34,.3);">Get TTM Squeeze Pro — $25</a>
  <p style="margin-top:1rem;font-size:1.25rem;color:var(--text-muted);">Invite-only access · Lifetime · One-time purchase</p>
  <p style="margin-top:0.5rem;font-size:1.15rem;color:var(--text-muted);">After purchase, your TradingView username will be added to the script by the next business day.</p>
</div>
{{< /rawhtml >}}

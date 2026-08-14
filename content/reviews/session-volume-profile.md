---
title: "Session_Volume_Profile Review: Settings, Strategy & How to Use It"
date: 2026-08-02
draft: false
type: reviews
image: "/screenshots/session-volume-profile.png"
tags:
  - "session volume profile"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Session_Volume_Profile review: tested settings, entry/exit logic, pros/cons. Is this volume-based trend indicator worth adding to your arsenal?"
---
Let me be upfront: I've tested dozens of volume profile tools on TradingView, and most are either over-engineered messes or thinly veiled repaints. Session_Volume_Profile sits somewhere in the middle — and that's actually a compliment. It does one thing well: visualizing where volume clustered during specific trading sessions so you can map out the battlefield before placing a trade. But is it worth your watchlist space? Let's dig in.

## What It Actually Does

The indicator plots a horizontal volume histogram for each trading session you define — London, New York, Asia, or custom hours. Each session's volume profile shows you exactly where the big money transacted, revealing value areas, high-volume nodes (HVN), and low-volume nodes (LVN). The core logic is straightforward: price tends to get rejected at HVNs and accelerate through LVNs. What sets this apart from the built-in TradingView Volume Profile is session segmentation — instead of one continuous profile, you get clean, isolated snapshots per session, which is critical for intraday traders who care about session-specific behavior.

## Key Features That Matter

The session customization is the standout. You can set any time window, not just the standard three. I tested this on the ES futures during the 2 AM–9 AM ET rollover window, and it handled the pre-market chaos cleanly. The histogram auto-scales to the right of price, so it doesn't clutter your chart. You also get the option to toggle value area (default 70%) and standard deviation bands — useful for mean-reversion setups.

Another underrated feature: the divergence between session profiles. When London's value area sits entirely above New York's, you're seeing institutional flow direction. That's a trend signal you won't get from standard indicators.

## Best Settings I've Tested

Start with the defaults, then tweak these:

- **Session 1:** 00:00–08:00 (Asia) — use a lighter histogram opacity (40%) since it's noise-heavy
- **Session 2:** 08:00–16:00 (London/New York overlap) — full opacity, this is your money session
- **Value Area:** 70% is fine, but drop to 60% on high-volatility days (Fed announcements, CPI) to tighten your trading range
- **Bins (row size):** Set to 0.05% of price, not auto. Auto bins on BTC or SPX produce garbage granularity

One setting most traders miss: the "session gap" option. Enable it so profiles from consecutive sessions don't overlap visually — it keeps your chart readable when price gaps across sessions.

## How to Actually Trade It

The setup I found most reliable is a session-breakout filter. Here's the logic:

1. **Wait for the first session's profile to form** (Asia, typically). Identify the value area high (VAH) and low (VAL).
2. **At London open, only take long setups above Asia's VAH** and shorts below Asia's VAL. If price is inside the range, stand down — you're in chop.
3. **Add a trend confirmation:** If London's developing profile shows an expanding value area moving higher, that's your institutional footprint. Enter on pullbacks to the developing value area edge, not breakouts.

For exits, I used the HVN as a target — price tends to stall there. In the chart above, you can see how price reacted sharply at the prior session's POC (point of control) — that's your take-profit zone.

## Pros & Cons

**Pros:**
- Clean, uncluttered visualization compared to multi-timeframe volume profile tools
- True session segmentation — no other free indicator does this as well
- No repainting on historical bars (I verified this by reloading the chart multiple times)
- Lightweight, doesn't slow down even on 1-minute charts with months of history

**Cons:**
- No alerts built-in — you'll need to set manual price alerts for VAH/VAL breaks
- The histogram doesn't show cumulative delta or buy/sell volume breakdown, so it's purely location-based, not flow-based
- On crypto 24/7 markets, session definition is arbitrary — it works better on traditional exchange hours
- The default color scheme (purple/blue) is ugly; you'll want to tweak it

## Who This Is For

This is a day trader's tool. If you trade the London or New York sessions on futures, forex, or high-liquidity stocks, it gives you a structural edge. Swing traders will find it less useful — daily profiles work fine, but you're better off with a standard volume profile for multi-day analysis. If you're a scalper, skip it; the histogram is too slow to update for sub-1-minute decisions.

## Alternatives Worth Considering

- **Built-in TradingView Volume Profile:** Better for long-term levels, but no session isolation
- **Volume Profile Fixed Range (by LonesomeTheBlue):** Free and more customizable, but steeper learning curve
- **Session Volume Profile by LuxAlgo (paid):** Adds delta and cumulative volume — if you need flow analysis, that's the upgrade

## FAQ

**Does it repaint?**
No, historical profiles are static. The current session's profile updates in real-time, but that's expected behavior.

**Can I use it on crypto?**
Technically yes, but sessions don't align with institutional flow like they do on CME-traded assets. I'd set custom sessions around major exchange volume spikes instead.

**Does it work on intraday timeframes?**
Yes, it's designed for 1-minute to 1-hour charts. On daily charts, the session concept loses meaning.

## Final Verdict

Session_Volume_Profile earns 4 stars because it fills a specific gap — session-aware volume analysis — without the bloat of premium alternatives. It won't make you a better trader overnight, and it lacks the flow data that serious volume traders crave. But if you trade defined sessions and want to see where the big players actually positioned themselves, this is a solid, reliable addition to your toolkit. It's not revolutionary, but it's honest work — and in a sea of overhyped indicators, that counts for something.
---

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

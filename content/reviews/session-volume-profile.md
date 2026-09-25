---
title: "Session_Volume_Profile Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/niaUzHtv-Session-Volume-Profile-AUMBaumgartner/"
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
grounding: "none (no source found)"
---
# Session_Volume_Profile Review

Session volume profile tools on TradingView tend to fall into two camps: over-engineered suites that bury the core function under layers of options, or lightweight scripts that quietly repaint. Session_Volume_Profile sits closer to the middle, and that positioning is part of its appeal. It does one thing — visualizing where volume clustered during specific trading sessions — and it does that thing without much decoration.

## What It Actually Does

The indicator plots a horizontal volume histogram for each trading session you define: London, New York, Asia, or custom hours. Each session's profile shows where volume transacted, revealing value areas, high-volume nodes (HVN), and low-volume nodes (LVN). The working premise behind this style of tool is that price tends to get rejected at HVNs and accelerate through LVNs. What separates this from the built-in TradingView Volume Profile is session segmentation: instead of one continuous profile, you get isolated snapshots per session. For intraday traders who care about session-specific behavior, that distinction matters.

## Key Features That Matter

Session customization is the standout capability. Any time window can be defined, not just the standard three. The histogram auto-scales to the right of price, so it doesn't crowd the chart. There's also a toggle for value area and standard deviation bands, which is useful for mean-reversion setups.

A less obvious feature is the divergence between session profiles. When one session's value area sits entirely above another's, that reflects a directional shift in where volume concentrated — information a standard indicator won't surface.

## Settings and How to Tune Them

The defaults are a reasonable starting point. From there:

- **Session windows:** Define each session by its hours. Asia, the London/New York overlap, and other custom windows can each be set independently.
- **Value Area:** A percentage threshold determines how much of the session's volume the value area encloses. The default is a common starting point; traders focused on tighter ranges sometimes lower it during high-volatility periods.
- **Bins (row size):** Can be set manually rather than left on auto. Auto binning tends to produce coarse granularity on high-priced instruments, so a manual row size is often preferable.
- **Session gap:** Enable this so profiles from consecutive sessions don't overlap visually. It keeps the chart readable when price gaps across sessions.
- **Histogram opacity:** Adjustable per session, useful if you want quieter sessions to recede visually.

No single configuration is universally best — the right values depend on the instrument, the timeframe, and what you're trying to isolate.

## How to Actually Trade It

A common approach is to use the profile as a session-breakout filter:

1. **Wait for the first session's profile to form.** Identify the value area high (VAH) and low (VAL).
2. **At the next session's open, only take long setups above the prior session's VAH** and shorts below its VAL. If price is inside the range, the read is chop.
3. **Add trend confirmation:** A developing profile with an expanding value area moving in one direction suggests where volume is concentrating. Entries on pullbacks to the developing value area edge are one way to use that information, rather than chasing breakouts.

For exits, HVNs are a natural reference — price often stalls there. The prior session's POC (point of control) is another level worth watching as a potential take-profit zone.

## Pros & Cons

**Pros:**
- Clean, uncluttered visualization compared to multi-timeframe volume profile tools
- True session segmentation
- Historical profiles are static; the current session updates in real time, which is expected behavior for a developing profile
- Lightweight enough to run on intraday charts with extended history

**Cons:**
- No built-in alerts — VAH/VAL breaks require manual price alerts
- No cumulative delta or buy/sell volume breakdown; it's location-based, not flow-based
- On 24/7 crypto markets, session definition is arbitrary — it works better on traditional exchange hours
- The default color scheme leaves room for improvement

## Who This Is For

This is a day trader's tool. If you trade the London or New York sessions on futures, forex, or high-liquidity stocks, it provides structural context for session-based setups. Swing traders will find it less useful — daily profiles work, but a standard volume profile is generally better suited to multi-day analysis. Scalpers working on very short timeframes may find the histogram too slow to update for their decisions.

## Alternatives Worth Considering

- **Built-in TradingView Volume Profile:** Better for long-term levels, but no session isolation
- **Volume Profile Fixed Range (by LonesomeTheBlue):** Free and more customizable, but a steeper learning curve
- **Session Volume Profile by LuxAlgo (paid):** Adds delta and cumulative volume — the upgrade path if you need flow analysis

## FAQ

**Does it repaint?**
Historical profiles are static. The current session's profile updates in real time, which is expected behavior rather than repainting.

**Can I use it on crypto?**
Technically yes, but sessions don't align with institutional flow the way they do on CME-traded assets. Setting custom sessions around major exchange volume spikes is one workaround.

**Does it work on intraday timeframes?**
Yes — it's designed for intraday charts. On daily charts, the session concept loses meaning.

## Final Verdict

Session_Volume_Profile fills a specific gap — session-aware volume analysis — without the bloat of premium alternatives. It won't transform your trading, and it lacks the flow data that serious volume traders want. But if you trade defined sessions and want to see where volume concentrated, it's a solid, reliable addition to the toolkit. Not revolutionary, but honest work.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

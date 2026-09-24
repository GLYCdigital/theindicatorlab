---
title: "Session_Vp Review: Settings, Strategy & How to Use It"
date: 2026-08-09
draft: false
type: reviews
image: "/screenshots/session-vp.png"
tags:
  - "session vp"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Session_Vp review: a session-based volume profile for TradingView. Tested settings, pros/cons, and how to trade trend continuations with it."
grounding: "none (no source found)"
---
# Session_Vp Review

Session_Vp is a session-specific volume profile. Rather than a single cumulative profile spanning weeks, it builds a separate profile for each trading session (Asian, London, New York, etc.) and displays the price levels where the most volume traded in each. The distinction matters: liquidity pools shift depending on which session is active, and a per-session view reflects that in a way a single aggregate profile does not.

## Key Features That Matter

The standout feature is the value area calculation. Session_Vp doesn't just render a histogram — it computes the value area and highlights it with a clear box, giving an immediate visual read on where the market considers "fair price" for that session. The value area ends up wide enough to be meaningful without being so wide it stops being actionable.

Session boundaries are fully configurable. Custom start and end times can be set for each session, which matters for instruments like crypto where sessions bleed into each other, or when overlaying your own defined sessions. Many volume profile tools force fixed exchange hours; this one does not.

The dashboard is a small panel showing the current session's POC (Point of Control), value area high, and value area low. No clutter — just the reference levels at a glance.

## Settings and How to Tune Them

- **Value area percentage**: Controls how much of the session's volume the highlighted area captures. Too tight and the area loses meaning; too wide and it stops being useful for entries. The default sits in a reasonable middle ground.
- **Session boundaries**: Set custom start and end times per session. For forex, classic Tokyo/London/New York splits are the natural choice; for crypto, align the windows to the instrument's actual liquidity curve rather than exchange hours.
- **Lookback / sessions displayed**: The indicator can show only recent sessions. Displaying every historical session adds noise to the chart without adding actionable information, so limiting the count is usually the cleaner read.

## How It Can Be Traded

A session-breakout approach is the most natural fit for what the tool shows:

1. Let the opening portion of a session establish its value area.
2. Mark the value area high and low.
3. If price breaks above the value area high on volume, look for a long entry on the first pullback that holds above the breakout level. Invert for shorts.
4. Stops can be referenced to the session's POC; targets to the next session's value area extreme.

This is mechanical and repeatable because the reference levels — POC, value area high, value area low — are objective and drawn from the session's own volume distribution.

## Pros & Cons

**Pros:**
- Session-specific focus is genuinely useful for intraday and swing traders
- Customizable session times work across asset classes
- Clean visual hierarchy — value area, POC, and extremes are all distinct
- Lightweight; no lag on the chart even with multiple sessions loaded

**Cons:**
- No automatic session detection. Times must be input manually, which takes a few minutes to set up correctly.
- No built-in alerts. Getting pinged when price exits the value area requires manually configured price alerts.
- The dashboard panel is static — it doesn't highlight which session is currently active unless you're looking at the chart. Minor, but worth noting.

## Who Should Use This

This is for traders who treat volume as a map of where large participants left their footprints, not just a histogram at the bottom of the chart. Day traders focused on specific sessions (London open, New York open) will find it sharpens entries. Swing traders can use it to identify where the next session's liquidity pools sit.

Scalpers on very fast timeframes will likely find a session profile too slow — they need faster feedback than a session-level view provides.

## Alternatives Worth Considering

**Volume Profile Fixed Range** by TradingView is the built-in standard — solid, but it doesn't segment by session. **VPVR** by LuxAlgo adds multi-timeframe volume profiles at the cost of more visual clutter. Session_Vp sits in a middle ground: more focused than the built-in, less overwhelming than the LuxAlgo option.

## FAQ

**Does Session_Vp repaint?**
The volume data is historical and fixed. Once a session closes, its profile does not change.

**Can it be used on crypto?**
Yes — and it suits crypto specifically because session times are customizable to a 24/7 trading cycle rather than fixed exchange hours.

**Does it work on lower timeframes?**
It can be applied there, but volume data becomes sparse and less reliable on very low timeframes.

## Final Verdict

Session_Vp is not a revolutionary indicator — it's a well-executed take on a proven concept. The session-specific approach fills a real gap for traders who think in terms of liquidity and session dynamics rather than trend lines alone. The lack of built-in alerts and the manual session setup hold it back from being a complete package, but for a few minutes of configuration you get a tool that adds a genuine dimension to market reads.

If you trade sessions, this deserves a spot on your chart. If you don't, it's worth evaluating — session-based volume analysis may change how you read the market.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

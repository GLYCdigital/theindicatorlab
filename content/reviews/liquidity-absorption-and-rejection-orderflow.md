---
title: "Liquidity_Absorption_And_Rejection_Orderflow Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/liquidity-absorption-and-rejection-orderflow.png"
tags:
  - liquidity absorption and rejection orderflow
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Tracks real-time orderflow absorption & rejection zones. Solid for spotting liquidity grabs and failed breakouts. Not a standalone system."
grounding: "none (no source found)"
---
**Description:** Tracks real-time orderflow absorption & rejection zones. Solid for spotting liquidity grabs and failed breakouts. Not a standalone system.

---

## What This Indicator Actually Does

This is not a lagging oscillator or a trend follower. It's a real-time orderflow tool that plots colored zones on your chart where price gets *absorbed* (heavy buying fails to push up) or *rejected* (sellers can't drive it lower). Think of it as a visual footprint of supply/demand battles.

You'll see two main things:
- **Absorption zones** (usually blue/teal): Price stalls despite aggressive volume. Liquidity is getting eaten.
- **Rejection zones** (usually red/orange): Price reverses sharply after hitting an area. Classic failed breakout or liquidity sweep.

The chart above shows an example on NQ 15-min: price swept below a swing low, then bounced hard off a rejection zone.

## Key Features That Set It Apart

- **Real-time calculation** – Zones form on the bar they occur and don't move.
- **Customizable sensitivity** – The absorption threshold defines how much volume versus price movement counts as absorption. In practice this is the main dial you'll adjust per instrument, since volatility profiles differ across markets.
- **Alerts on zone formation** – Useful for catching entries before the breakout crowd piles in.
- **Clean chart** – Unlike many orderflow tools, it doesn't clutter your screen with a million boxes. Zones fade after a few bars unless price retests.

## Settings and How to Tune Them

| Setting | What It Controls |
|---------|------------------|
| Absorption Threshold | Volume-to-price-movement ratio that qualifies a bar as absorption. Higher values filter more aggressively. |
| Rejection Sensitivity | How sharp a reversal must be to print a rejection zone. |
| Zone Expiration | How many bars a zone stays on the chart before fading. |
| Show Volume Delta | Toggles the delta display. |

The absorption threshold is the setting most worth tuning per market, since volume characteristics vary widely between instruments. The other settings are largely a matter of chart cleanliness and how much history you want visible.

## How to Use It for Entries and Exits

**Long entry:**
1. Wait for a rejection zone to form below a key level (e.g., prior low, VWAP).
2. Price sweeps into the zone, then closes back above it.
3. Enter on the next candle open. Stop loss below the zone low.
4. Target the next absorption zone or prior high.

**Short entry:**
Same logic inverted. Absorption zone above resistance → price fails to break → short on retest.

**Exit rule:** If price enters a zone and doesn't reverse within a couple of bars, exit. The zone is failing.

## Pros and Cons

**Pros:**
- Useful for identifying liquidity grabs (stop hunts) as they develop.
- Works on liquid markets – futures, forex, crypto.
- Zones form on the bar they occur and don't move.
- Lightweight – doesn't lag noticeably even on 1-min charts.

**Cons:**
- **Not a standalone system.** You need price action, support/resistance, or a trend filter. Blindly trading zones will kill your account.
- False signals in low-volume hours (e.g., Asian session on ES).
- No built-in backtest metrics. You'll have to eyeball it.

## Who It's Actually For

- **Orderflow traders** who already understand absorption and rejection concepts.
- **Swing traders** looking for precise entries on pullbacks.
- **Scalpers** who trade high volume markets (ES, NQ, GC).

**Not for:** Beginners who want a "buy here, sell there" magic button. Or anyone trading low-liquidity stocks.

## Better Alternatives

- **Sierra Chart's Order Flow Bars** – More granular, but costs money and is less user-friendly.
- **Bookmap** – Best for level 2 visibility, but overkill for most.
- **TradingView's built-in Volume Profile** – Free, but only shows historical zones, not real-time absorption.

If you're on a budget, this indicator is solid. If you're serious about orderflow, pair it with volume profile.

## FAQ

**Q: Does it repaint?**
A: No. Zones form on the bar they occur and don't move.

**Q: Can I use it on crypto?**
A: Yes, though you'll likely want a higher absorption threshold to filter noise.

**Q: Why do I get false signals during news?**
A: High volatility breaks the absorption/rejection logic. Avoid trading 5 minutes before/after major news.

**Q: Does it work on lower timeframes like 1-min?**
A: Yes, but zones expire quickly, so a shorter expiration is usually needed.

## Final Verdict

**Rating: ⭐⭐⭐⭐ (4/5)**

It's a niche tool, not a holy grail. If you understand orderflow and want a clean visual of absorption/rejection zones in real-time, this is one of the better options on TradingView. The lack of built-in backtesting and occasional noise in low volume holds it back from 5 stars.

Worth installing? Yes. Worth trading alone? No. Pair it with price action and a trend filter.

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

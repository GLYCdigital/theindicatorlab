---
title: "Session_Vwap_Profile_Candle_Delta Review: Settings, Strategy & How to Use It"
date: 2026-09-25
draft: false
type: reviews
image: "/screenshots/session-vwap-profile-candle-delta.png"
tags:
  - "session vwap profile candle delta"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Session VWAP Profile & Candle Delta review: anchored VWAP bands, auto session detection, volume profile POC and candle delta boxes in one Pine v6 overlay."
tv_script_url: "https://www.tradingview.com/script/36ik5Jpc-Session-VWAP-Profile-Candle-Delta-BigBeluga/"
sources: ["https://www.tradingview.com/script/36ik5Jpc-Session-VWAP-Profile-Candle-Delta-BigBeluga/"]
---
Most VWAP tools give you a line and call it a day. The **Session VWAP Profile & Candle Delta [BigBeluga]** tries to do considerably more: it anchors VWAP to a session, wraps it in standard deviation bands, builds a volume profile behind it, and then splits that profile's volume into bullish and bearish candle counts per price bin. That last part is what separates it from the pile of generic VWAP scripts on TradingView.

Here's what it actually does, and where it earns its keep.

## What This Indicator Is

At its core, this is a session-anchored VWAP overlay with three layered systems stacked on top of each other: a session engine, a volume profile engine, and a band-reversal signal system. The description frames it as a response to a specific gap — most VWAP and volume profile tools don't automate higher-timeframe session switching, and they rarely break volume down into bullish versus bearish candle counts per price bin.

That framing is fair. The candle delta distribution boxes are the genuinely distinctive feature here, not the VWAP itself.

## How the Session Engine Works

The indicator can target roughly 200 candles per session automatically via the *Use Auto Timeframe* setting, or you can fall back to a *Manual Timeframe*. Session boundaries are monitored through timeframe changes, which is what anchors the VWAP calculation and accumulates the underlying volume, price-volume, and squared price-volume sums.

Practically, this means you don't have to manually re-anchor VWAP each session or hand-pick a higher timeframe that happens to line up with your chart. The script adapts. For anyone who has spent time manually resetting anchored VWAP, that automation alone is worth noting.

## Volume Profile, Bins, and POC

The profile side uses dynamic bin resolution calculated from ATR volatility, or you can fix the bin count with the *Manual Bins Count* parameter. Within those bins, volume is distributed while the script tracks bullish and bearish candle counts, displayed as `[+Bullish | -Bearish]` distribution boxes.

The Point of Control — the highest-volume bin in the session — gets a dashed line drawn across the profile structure. Volume density is rendered as gradients, so higher-liquidity nodes stand out visually rather than requiring you to read numbers off a histogram.

This is the section of the tool that does the most work. Value area and POC identification is a well-worn concept, but seeing it rendered as a live, session-aware profile directly on the price chart — with the delta split visible — is a meaningful convenience.

## Band Reversals and Signals

Upper and lower standard deviation channels are computed around the central VWAP using a configurable *Band Multiplier (StdDev)*. The VWAP mid line is colored bull or bear based on session direction, which gives you an at-a-glance read on which side of the session's flow you're on.

The signal logic is straightforward: when price pierces an outer band and then closes back inside it, a triangle marker is plotted. There's spacing gap enforcement to prevent the chart from being carpeted in signals during choppy conditions.

Be clear on what this is: a mean-reversion trigger based on band rejection. It is not a trend-following system, and the description doesn't pretend otherwise.

## How to Use It

Three documented workflows:

1. **Value areas and POC** — watch the POC line and density bins for fair-value zones and high-liquidity nodes.
2. **Band rejections** — the triangle signals at the outer standard deviation channels are the intended entry trigger when price fails a breakout and closes back inside.
3. **Order flow balance** — read the candle count distribution boxes to judge whether buyers or sellers dominate specific price nodes within the session.

The natural pairing is POC plus band rejection: if price rejects an outer band and the delta boxes show one side dominating near that level, you have confluence rather than a lone signal.

## Pros and Cons

**Pros:**
- Automated session detection removes manual VWAP re-anchoring.
- Candle delta distribution per bin is genuinely uncommon and adds information a plain profile doesn't have.
- ATR-driven dynamic bins adapt to volatility instead of forcing a fixed resolution.
- Garbage-collected session tracking suggests the author cared about performance across long histories.

**Cons:**
- It's a dense overlay. VWAP bands, profiles, gradients, POC lines, and triangle markers on one chart can get busy, especially on lower timeframes.
- The signal logic is purely mean-reversion — no trend continuation component.
- The delta boxes require interpretation. They're informative, not a mechanical trigger.

## Who It's For

Intraday and swing traders who already think in terms of VWAP and value areas, and who want session automation plus a delta dimension without running two separate scripts. If you're a pure price-action trader who finds profiles noisy, this won't convert you. If you're already anchoring VWAP by hand, it likely will.

## FAQ

**Does it repaint?** The description doesn't address repainting, so treat real-time band touches with normal caution until a bar closes.

**Can I use a fixed timeframe?** Yes — the *Manual Timeframe* setting overrides the auto mode.

**What does the triangle signal mean?** Price pierced an outer standard deviation band and closed back inside it — a rejection.

**Is the bin count fixed?** No, unless you set it manually. By default it's ATR-driven.

## Final Verdict

The Session VWAP Profile & Candle Delta is a well-architected, genuinely differentiated take on session VWAP. The candle delta distribution is the standout feature and the automation is real. It loses a star for visual density and a signal system that's one-dimensional — mean-reversion only. If your style fits that mold, it's a strong addition.

**Rating: ⭐⭐⭐⭐ (4/5)**
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

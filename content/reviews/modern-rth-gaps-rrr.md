---
title: "Modern Rth Gaps Rrr Review — Trend Indicator"
date: 2026-10-04
draft: false
type: reviews
image: "/screenshots/modern-rth-gaps-rrr.png"
tags:
  - "modern rth gaps rrr"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Modern RTH Gaps maps true overnight index gaps from the 16:00 close to the 09:30 open, then shrinks them with live ETH fills. A clean, honest gap tool."
tv_script_url: "https://www.tradingview.com/script/cBvTG8zW-Modern-RTH-Gaps-RRR/"
sources: ["https://www.tradingview.com/script/cBvTG8zW-Modern-RTH-Gaps-RRR/"]
---
Most gap indicators on TradingView do the same lazy thing: they measure candle-to-candle and call it a gap. That's not how an index actually gaps. Modern RTH Gaps (Dynamic ETH Fills) takes the harder, more correct approach — and that's the entire reason it exists.

## What it actually does

The core idea is that a "true gap" isn't a candle pattern. It's the void between where regular trading hours stop and where they start again. On intraday charts, this script captures the 16:00 RTH close, freezes that price, and measures the gap against the 09:30 RTH open. That's the creation side — and it's RTH-only by design, which is the whole point.

The destruction side is where it gets interesting. Once a gap exists, price is price. The script uses dynamic box routing to continuously shrink and update the gap using all price action, including Extended Trading Hours wicks that dip into the zone. So a gap you marked at the open doesn't stay static while ETH quietly eats into it overnight — the box tightens as liquidity gets consumed.

As shown in the chart above, the gap zones render as boxes with supply/demand labels that move with the boundaries.

## The features that justify it

**Dynamic price labels.** As a gap shrinks, the Supply/Demand text updates in real time to reflect the narrower boundaries. This is the most practically useful feature here — if you're dialing in an options strike or a limit order, you want the *current* edge of the void, not where it was at 09:30.

**Hybrid timeframe engine.** This is the detail that separates it from strict session scripts, which tend to crash, error out, or vanish when you zoom to a Daily or Weekly chart — because those timeframes don't carry ETH data. Instead, this script runs a smart router: on higher timeframes it falls back to standard Open/Close calculations so your chart stays intact. That's a genuinely considerate piece of engineering, and it's the kind of thing you only appreciate after a session script has blown up your layout.

**Memory efficiency.** Built on Pine Script v6 arrays and types. Closed or expired gaps are purged from both the chart and the engine's memory stack, leaving no ghost objects behind. On a chart running multiple indicators, that discipline matters more than it sounds.

## How you'd actually use it

The workflow is straightforward. On an intraday chart, let the script mark the gap between the prior 16:00 close and the 09:30 open. From there, watch the box. If price wicks into it during ETH, the box shrinks and the labels update — that's your live map of remaining unfilled liquidity. The narrower the zone gets, the more precise any order you place around it needs to be. When the gap is fully consumed, it's gone from the chart entirely.

You're not getting buy/sell signals here. This is a mapping tool, not a strategy. It tells you *where* the void is; it doesn't tell you what to do about it.

## Pros and cons

**Pros:**
- The RTH-only creation logic is methodologically correct, not a cosmetic tweak on a standard gap script.
- Dynamic shrinking with ETH wick inclusion is the honest way to track gap fill.
- The hybrid timeframe fallback prevents the usual session-script breakage on Daily/Weekly.
- Live-updating labels make it usable for real order placement, not just chart decoration.
- Clean memory handling — no accumulating ghost boxes.

**Cons:**
- It's a visualization tool. No alerts, no entries, no exits, no confluence logic. You bring the decision-making.
- Its value is concentrated in index and equity instruments with a defined RTH session. Apply it to something without that structure and the premise falls apart.
- If you don't trade around gap fills or liquidity voids, this indicator has nothing to say to you.

## Who it's for

Index and equity traders who actively work gap fills — particularly those trading intraday options or placing limit orders near liquidity voids. The ICT and smart-money framing in the tags is a fair signal of the audience: traders who think in terms of unfilled liquidity rather than indicator crossovers. If you're a swing trader on Daily charts, the hybrid engine will keep the chart working, but the gap detail is largely lost at that resolution.

## FAQ

**Does it work on crypto or forex?**
The entire methodology depends on a Regular Trading Hours session with a defined close and open. The source is explicit that it's built for index and equity traders. Applying it elsewhere isn't what it was designed for.

**Will it break if I switch to a Weekly chart?**
No — that's the specific problem the hybrid timeframe engine solves. It falls back to standard Open/Close calculations when ETH data isn't available.

**Does it give signals?**
No. It maps and updates gap zones. Entries and exits are yours to determine.

## Verdict

This is a focused, well-engineered tool that solves one problem properly. The RTH-creation/ETH-destruction split is the correct model for how index gaps actually behave, and the dynamic labels plus the timeframe fallback show someone thought about real usage rather than just a screenshot. It loses a star only because it's purely a mapper — no alerts, no strategy layer — and its usefulness collapses outside RTH-based instruments. If gap fills are part of your playbook, it earns its chart space.

**Rating: ⭐⭐⭐⭐ (4/5)**
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and the official TradingView script documentation. Always test indicators in a demo environment before live trading.*

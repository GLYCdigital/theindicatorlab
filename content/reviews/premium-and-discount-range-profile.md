---
title: "Premium And Discount Range Profile Review — Volume Indicator"
date: 2026-10-03
draft: false
type: reviews
image: "/screenshots/premium-and-discount-range-profile.png"
tags:
  - "premium and discount range profile"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Premium And Discount Range Profile review: a live high-low range with a volume footprint that grades each edge as rejection, acceptance, or exhaustion."
tv_script_url: "https://www.tradingview.com/script/9BbXqai9-Premium-and-Discount-Range-Profile-MaxMaserati/"
sources: ["https://www.tradingview.com/script/9BbXqai9-Premium-and-Discount-Range-Profile-MaxMaserati/"]
---
Most range tools stop at drawing two lines and a midpoint. This one keeps going — it asks what actually happened at those edges. The Premium And Discount Range Profile builds a live range from the highest high and lowest low of the last N bars, splits it at the midline into premium and discount, then profiles the volume traded inside that range to grade each edge.

That last part is the interesting bit, and it's what separates this from the pile of generic premium/discount scripts.

## The core mechanic

The midline — labelled EQ — is simply (Highest High + Lowest Low) / 2. Price location is expressed as a percentage of the range: (Close − Lowest Low) / (Highest High − Lowest Low) × 100. Above 50% is premium, below is discount. The half holding price is drawn at full colour, so you can see at a glance which side of the auction you're standing in.

There's also a First Step signal: a green line prints on the first confirmed bar where the midline starts rising, a red line where it starts falling. Simple, but it gives the range a directional lean rather than leaving you with a static box.

## The footprint profile is the differentiator

The range is split into bins, and volume is distributed across them. If you have footprint data, each row's buy and sell volume drops into its bin. Without it, volume is spread across the bins each candle touches and split using the candle body and wicks. The largest bin becomes the POC. Bins above 70% of the POC are marked HVN; below 30% are LVN.

This is where the tool earns its keep. A high-low range tells you where price is expensive or cheap. A volume profile tells you where volume traded. Neither tells you whether traders are defending the edges. Combining them does, which is exactly the gap the author is targeting.

## Edge states: the auction verdict

Each edge gets classified. At the top: a top-bin HVN with sellers dominant reads as Strong Rejection. HVN with buyers dominant reads as Acceptance. An LVN reads as Exhaustion, and gets upgraded to Exhaustion → Rejection when a seller-dominant node sits in the top 33% of the range. The bottom edge mirrors all of this.

That's a genuinely useful vocabulary. Instead of eyeballing whether a wick "looks rejected", you get a stated condition with a defined input.

## How I'd actually use it

The documented workflow is clean. Read the Location row and the highlighted label first. Look for shorts in premium and longs in discount. Before taking a short, check the High Edge Status for Strong Rejection or Exhaustion → Rejection; before a long, check the Low Edge Status. A red First Step in premium supports shorts, a green First Step in discount supports longs.

The invalidation rule is the part most people will skip and shouldn't: the idea is dead when that edge shows Acceptance, or when a new high or low extends the range. That's an honest, mechanical stop to the thesis.

## Settings and practical notes

Settings are grouped sensibly — range lookback and box length, footprint toggle and row size, box and midline colours, zone labels, volume profile bins and width, POC/HVN/LVN, delta labels and edge states with a scan depth, optional high/low/mid line plots, table rows including Location, and First Step signal controls with history.

Two caveats worth stating plainly. Everything — range, profile, labels, edge states — includes the live candle and updates until it closes, so readings can shift intrabar. First Step lines print on confirmed bars only, which is the correct trade-off but means the signal lags the turn. And without footprint data, buy and sell volume are estimates, not measurements. If you're not on a footprint feed, treat the edge states as a heuristic.

The author states it's built for intraday futures such as ES1! and NQ1!. That's a narrow target, and the tool's design reflects it.

## Pros and cons

**Pros:** Combines three concepts that normally live in separate indicators; edge states give a concrete, testable verdict rather than a vibe; invalidation is defined; live updating keeps it relevant intrabar; works without footprint data, albeit approximately.

**Cons:** Intrabar repainting on the range and edge states is inherent to the design; volume estimates without footprint data weaken the core signal; the futures-intraday focus limits usefulness elsewhere; the number of settings and table rows can overwhelm on a first install.

## Who it's for

Intraday futures traders who already think in auction terms — value, acceptance, rejection — and want that framework automated on the chart. If you trade mean reversion from range extremes, this is aimed squarely at you. Swing traders on daily charts, or anyone without footprint data, will get less out of it.

## Verdict

This is a well-reasoned tool with a clear thesis: an edge only matters if you know how it was treated. It doesn't try to be everything, and the edge-state logic is the kind of thing you'd otherwise be doing by hand. The intrabar updating and estimate-based volume without footprint data keep it from being exceptional.

**Rating: ⭐⭐⭐⭐ (4/5)**

## Frequently Asked Questions

### Is Premium And Discount Range Profile worth it?

That depends on your workflow — the sections above cover what it does and where it fits. Check the official TradingView page for the current feature set and author notes before you decide.

### Does this indicator repaint?

Check the author's own description on TradingView — repainting behaviour is script-specific and we won't assert it for you here.
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

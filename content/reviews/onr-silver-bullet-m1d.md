---
title: "Onr Silver Bullet M1d Review — Trend Indicator"
date: 2026-09-29
draft: false
type: reviews
image: "/screenshots/onr-silver-bullet-m1d.png"
tags:
  - "onr silver bullet m1d"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Onr Silver Bullet M1D draws the three ICT Silver Bullet hours and the projected overnight range on one chart. A time-and-price framework tool, not a signal."
tv_script_url: "https://www.tradingview.com/script/FcAJ3joL-ONR-Silver-Bullet-M1D/"
sources: ["https://www.tradingview.com/script/FcAJ3joL-ONR-Silver-Bullet-M1D/"]
---
Most indicators try to tell you something. This one deliberately doesn't. **Onr Silver Bullet M1D** draws the *time* and *price* framework that ICT's Silver Bullet model is read inside, and then stops. No signals, no arrows, no grading of setups. If you're looking for a tool that decides for you, this isn't it — and the description is refreshingly upfront about that.

## What it actually draws

Two things, layered on one chart.

First, the **three ICT Silver Bullet hours** of the New York day: the London open, the New York morning, and the New York afternoon. Each hour is boxed from its own high to its own low, with a thin vertical line at its start and end running the full height of the chart, and the hour's name written large and faint inside the box.

Second, the **overnight range (ONR)** — the hours after the London Silver Bullet and before the New York session opens. It's boxed from its high to its low, with its equilibrium (the midpoint) drawn dotted, and then projected outward. The -1 standard deviation sits half a range beyond each edge; the -2 sits one full range beyond. Both distances are adjustable.

The point of the Silver Bullet model is that *time is part of the setup, not a filter on top of it*. A sweep, a shift or a fair value gap that prints outside the window isn't a Silver Bullet, however similar it looks. This script makes that rule visible at a glance, so you're not counting candles or marking boxes by hand.

## Key features worth noting

The **ONR table** (top right by default) is the detail that separates this from a plain session-box script. It shows the instrument, the chart timeframe, the size of the latest overnight range in points — marked live while it's still forming — its high and low, and the average size of the last ten finished overnight ranges on the chart, with today's range expressed as a share of that average. So a range that reads 125% of the average is a wider night than usual; 70% reads a quiet one. That single number gives you context for how far the New York morning might reasonably travel.

The **visual grammar** is thought through. Silver Bullet hours are soft lavender, the overnight range grey, so the two read apart instantly — and neither uses the purple or magenta that mean direction elsewhere in the M1D suite. Deviation lines are dashed at -1, solid at -2, each labelled at its left end on its price.

On **method**: every window is read from the New York clock by name, so it follows daylight saving on its own and doesn't depend on your chart's timezone. A box grows with its window while open and holds once closed. The ONR's equilibrium and deviations move with it until the range closes, then are fixed. The average is taken only over *finished* overnight ranges, and only from bars loaded on the chart — and the table tells you how many it used.

## How to use it

The script is drawn on 1-hour charts and below, but the model itself is read on the 1 to 5 minute charts. The workflow is the one ICT teaches: before the hour, mark resting liquidity on the 15-minute chart. Inside the hour, watch for a run on one side's liquidity followed by displacement the other way with a market structure shift, leaving a fair value gap that forms inside the window. Price is then allowed to trade back into that gap rather than chased.

This tool doesn't do any of that reading for you. It gives you the boxes, the projected deviations and the range context so you can do it faster and without hand-marking.

## Pros and cons

**Pros.** It does one job cleanly. The time windows are handled by New York clock name, so DST is a non-issue. The overnight range projections are a genuinely useful reference for framing how far a move out of the range may extend. Nearly everything is configurable: each hour on/off and its time, the ONR on/off and its time, equilibrium, deviations, their distances and labels, start/end lines, every fill and line colour, name and label colour and size, how many days stay on the chart, and the table's on/off state, position, size, average length and colours.

**Cons.** It fires **no alerts** — you'll be watching the chart, not your phone. It produces no entries, targets or stops by design, so it's only as good as the trader reading it. And the deviation projections are reference levels, not predictions; treating them as targets is a misuse of the tool.

## Who it's for

Discretionary intraday traders already working the ICT Silver Bullet model on index futures or FX, who want the windows and the overnight range drawn consistently instead of marked by hand every session. If you don't already understand sweeps, market structure shifts and fair value gaps, this indicator won't teach you — it assumes the model.

## FAQ

**Does it repaint?** No. A box grows while its window is open and holds once it closes. The ONR equilibrium and deviations move until the range closes, then are fixed.

**Does it work in my timezone?** Yes — every window is read from the New York clock by name, so it follows daylight saving automatically.

**Does it give buy/sell signals?** No. It's a charting tool that draws what the chart already contains.

## Verdict

A focused, well-executed framework tool that respects its own boundaries. It won't make decisions for you, and it makes no attempt to — which is exactly why it's useful in the right hands. Four stars: excellent at what it does, but the absence of alerts and the total reliance on the trader's own read keep it from being a five.

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

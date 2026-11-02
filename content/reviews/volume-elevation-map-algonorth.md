---
title: "Volume Elevation Map Algonorth Review — Volume Indicator"
date: 2026-11-03T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/volume-elevation-map-algonorth.png"
tags:
  - "volume elevation map algonorth"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Volume Elevation Map [AlgoNorth] turns 90 bars of volume into a 3D landscape of peaks, POC and value area. Honest 4-star review."
tv_script_url: "https://www.tradingview.com/script/yn9jlOax-Volume-Elevation-Map-AlgoNorth/"
sources: ["https://www.tradingview.com/script/yn9jlOax-Volume-Elevation-Map-AlgoNorth/"]
---
Most volume tools give you a histogram and call it a day. Volume Elevation Map [AlgoNorth] takes a different route: it renders the last 90 bars as a three-dimensional landscape where heavy volume rises into hills and thin volume lies flat. The busiest prices and moments become the peaks. It's a distinct way to read where the market actually fought — and the fact that it's honest about what it *can't* tell you is part of why it earns a solid rating.

## What it actually does

The map sits in the empty space to the right of price. Rows run from the low of the covered window at the front to the high at the back, and slices run from the oldest bar on the left to the current bar on the right. Each cell's hill height reflects the volume traded in that price-and-time slot, drawn on a softened scale so the smaller hills don't vanish.

Two ridges do the heavy lifting. A gold ridge traces the Volume POC — the price row that traded the most volume — with its price tagged. A white ridge marks the NOW row, the last close. Green hills are where buyers led; red hills where sellers led. A white dotted price path joins the hill summits in time order, so you can trace how price moved through the landscape.

## The parts that set it apart

Three things stand out from the documented behaviour.

First, the **volume dots**. They sit above the three highest-volume closed candles of the window, coloured by candle direction, with dashed threads connecting each dot to where that candle's volume lands on the map. Volume call-outs print under the candles. This ties the abstract landscape back to specific bars on the chart — a genuinely useful bridge.

Second, the **verdict strip**. Below the map, it reads which side traded more of the window's volume and that side's share, with a buy/sell split as a green/red edge underneath. It also tells you whether price sits above, in, or below the value area.

Third, the **value area logic**. It holds the price rows carrying up to 70% of the window's volume, built out from the POC row by adding whichever neighbouring row traded more — the same approach TradingView's volume profile uses. Familiar enough to trust.

## How you'd actually use it

The workflow is descriptive, not predictive, and the tool is upfront about that. You scroll the chart right (or raise the right margin in Chart settings) to bring the full map into view — at default settings it's roughly 85–90 bars wide with tags.

From there, you're reading structure. Tall hills mark where the most trading happened at a given price and time. The POC ridge shows the price row that absorbed the most volume. The verdict strip gives you a quick read on which side led and where price sits relative to value. The dots flag the heaviest candles and let you trace them onto the map.

One detail worth internalising: the same volume packed into a short burst stands taller than the same volume spread across the window. So the POC row doesn't necessarily carry the tallest hill. That's a feature of the smoothing, not a bug, but it will confuse anyone expecting a literal histogram.

## Pros and cons

**Pros**
- The 3D landscape is genuinely novel — it makes volume concentration legible in a way a flat profile doesn't.
- The dots-and-threads feature connects heavy candles to their map location, which is more than most volume tools bother with.
- The verdict strip and value-area read are stated plainly and can't contradict each other (the verdict follows the rounded split).
- It refuses to draw on Heikin Ashi, Renko and other synthetic charts rather than producing a distorted map — a good call.
- The documentation is unusually candid about limitations. More on that below.

**Cons**
- The buy/sell split is **estimated** from intrabar candle direction, not bid/ask data. The author says so explicitly. Row colours and the verdict are a read of volume, not order flow.
- Edge cells have fewer neighbours to blend with, so a burst at the map's boundary stands a little taller than the same burst mid-map. A minor distortion.
- On forex and CFD symbols you're looking at tick volume — activity, not contracts. That's a real constraint for anyone trading those markets.
- The map can only cover the bars TradingView allows the script to calculate. If that setting is below your chosen window, the map shrinks — and below 20 bars it just says NEEDS 20 BARS.
- Labels crowd when you're zoomed far out or when larger older swings are in view.

## Who it's for

Discretionary traders who already think in terms of value areas and POCs and want a more spatial view of where volume concentrated. If you're the type who reads a volume profile and asks "but *when* did that volume print?" — this tool answers that question visually. It's less suited to anyone wanting precise order-flow data or an automated signal, since it explicitly isn't either.

## FAQ

**Does it predict price?**
No. The documentation is blunt: it shows history, not a forecast. Everything comes from the covered window.

**Is the buy/sell split real order flow?**
No. It's an estimate from intrabar candle direction — buying if the bar closed up, selling if it closed down, with flat bars carrying the previous direction. Hill heights and the volume dots are real volume; the split is not.

**Why doesn't the POC row have the tallest hill?**
Because volume packed into a short burst stands taller than the same volume spread across the window. Hill height reflects volume per bar in that cell, blended with neighbours.

**Will it work on my Heikin Ashi chart?**
No. It stops with a message on synthetic chart types rather than drawing a distorted map.

**Why does the map show fewer bars than I set?**
TradingView's Calculated bars setting can limit it. If that's lower than your Bars covered setting, the map covers fewer bars.

## Verdict

Volume Elevation Map is a thoughtful, well-documented tool that does something most volume indicators don't: it gives volume a spatial dimension. It's honest about its limits — the estimated buy/sell split, the tick-volume caveat on forex, the edge-blending quirk — and that honesty is worth a lot. It won't replace your profile tool or your order-flow data, but as a complementary read on where the market actually traded, it earns its place on the chart.

**Rating: ⭐⭐⭐⭐ (4/5)** — genuinely distinctive, held back only by the inherent limits of estimated order flow and the constraints of what TradingView lets a script calculate.
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

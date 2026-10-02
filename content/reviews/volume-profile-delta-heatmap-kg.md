---
title: "Volume Profile Delta Heatmap Kg Review — Volume Indicator"
date: 2026-10-02
draft: false
type: reviews
image: "/screenshots/volume-profile-delta-heatmap-kg.png"
tags:
  - "volume profile delta heatmap kg"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Volume Profile Delta Heatmap Kg review: an all-in-one volume tool combining horizontal and rotated profiles, a delta heatmap, RSI signals and an info panel."
tv_script_url: "https://www.tradingview.com/script/WmHz18gf-Volume-Profile-Delta-Heatmap-KG/"
sources: ["https://www.tradingview.com/script/WmHz18gf-Volume-Profile-Delta-Heatmap-KG/"]
---
Most volume tools on TradingView do one thing. You want a profile, you add a profile. You want delta, you add a delta script. You want signals, you bolt on a third. Volume Profile Delta Heatmap [KG] takes the opposite approach: it bundles horizontal Volume Profile, a session Delta heatmap, a rotated (vertical) profile, RSI-filtered auto signals, and a live info panel into a single study. Whether that's a feature or a liability depends entirely on how much you trust one script to do five jobs.

## What it actually does

The core is a conventional horizontal Volume Profile. It builds from the last N bars (150 by default) across a user-defined number of price rows, distributing each candle's body and wick volume proportionally across price levels. From that it plots the POC — the price with the highest traded volume — plus VAH and VAL, the boundaries of the range containing a configurable share of total volume (70% by default). Bars inside the Value Area draw brighter; bars outside fade. That's standard, competent volume profile behaviour.

The Delta Heatmap is the more interesting piece. It splits recent sessions — Daily, Weekly, or Monthly — into price rows and colours each cell by net delta, defined here as buy volume minus sell volume. Green shades mean net buying, red shades net selling, and darker shades mean a stronger imbalance. Each session's total net delta prints above the heatmap. There's a damping option that softens delta when RSI is neutral, which is a sensible way to reduce noise during indecision.

Then there's the Rotated Volume Profile — a second, independently computed profile drawn vertically in the middle-right of the chart, with its own POC, VAH, VAL, arrows, brackets, and a volume axis. It's fully customisable in position, width, gap, histogram height, label frequency and axis ticks, and the frame, arrow and brackets can each be toggled.

## Signals and the RSI layer

Three signal engines are selectable: VA Breakout (close above VAH for a buy, below VAL for a sell), POC Bounce (price crossing POC with RSI agreement), or Both. Each can be filtered by RSI confirmation and by delta confirmation — net positive for buys, net negative for sells — with a minimum-bars-between-signals control and a total-signal cap to keep the chart from filling up with arrows.

RSI does double duty here: it filters signals and acts as a delta weighting factor. The info panel shows live RSI value and state alongside current POC, VAH and VAL prices. That's the workflow the author intends — read where volume sits, check who's in control, then let the signal engines flag the interaction.

## Honest trade-offs

The convenience is real. One script, one set of inputs, no cross-tool versioning headaches. The twelve grouped input sections cover nearly every colour, transparency, label size, offset and tick count, so you can shape it to your chart rather than the reverse.

The limitations are equally real, and the author is upfront about them. All drawing objects reset and redraw on the last bar, so historical bars carry no profile boxes — intentional, to stay within Pine's object limits, but it means you can't scroll back and study how the profile looked at a past decision point. The heatmap only uses roughly the last 500 bars. And delta is approximated from candle direction and volume (close versus open), not from true bid/ask data — so treat it as a directional proxy, not tick-accurate order flow. None of that is disqualifying, but it caps how far you can push the tool.

## Who it's for

Discretionary intraday and swing traders who already think in terms of value areas and want a single volume dashboard rather than a stack of scripts. If you're a purist order-flow trader who needs genuine footprint data, the approximated delta will frustrate you. If you're building a clean, readable chart and want POC/VAH/VAL plus a session imbalance view without three separate indicators, this is a coherent package.

## FAQ

**Does it repaint?** The drawing objects reset and redraw on the last bar by design, so historical bars don't retain profiles. Signals are built from close-based conditions, but you should confirm behaviour on your own setup before relying on them.

**Is the delta real order flow?** No. The source states delta is approximated from candle direction and volume. It's an interpretive reading, not exchange-level buy/sell data.

**How far back does the heatmap go?** Roughly the last 500 bars.

**Can I turn parts off?** Yes — the rotated profile's frame, POC arrow and VA brackets are individually toggleable, and inputs are grouped across twelve sections.

## Verdict

A genuinely well-organised all-in-one. It doesn't pretend to be footprint data, and it tells you exactly where its approximations lie. The last-bar redraw and ~500-bar heatmap window are the price of Pine's limits, not laziness. For traders who want volume context consolidated into one clean overlay, it earns its place. ⭐⭐⭐⭐

*Educational and informational only — not financial advice.*
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

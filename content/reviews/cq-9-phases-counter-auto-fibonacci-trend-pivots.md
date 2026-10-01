---
title: "Cq 9 Phases Counter Auto Fibonacci Trend Pivots Review"
date: 2026-10-01
draft: false
type: reviews
image: "/screenshots/cq-9-phases-counter-auto-fibonacci-trend-pivots.png"
tags:
  - "cq 9 phases counter auto fibonacci trend pivots"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "CQ 9 Phases Counter review: four structure tools in one overlay — zigzag metrics, auto Fibonacci, trend pivots and a 1-2-3-4-5 phase counter."
tv_script_url: "https://www.tradingview.com/script/HuOACUQB-CQ-9-Phases-Counter-Auto-Fibonacci-Trend-Pivots-v2/"
sources: ["https://www.tradingview.com/script/HuOACUQB-CQ-9-Phases-Counter-Auto-Fibonacci-Trend-Pivots-v2/", "https://mozilla.org/MPL/2.0/"]
---
Most multi-tool indicators are a bundle of unrelated scripts stapled into one pane. This one is different in a way that matters: its four sections share a common vocabulary of pivots, legs and retracement, so the pieces actually talk to each other instead of fighting for space.

## What it actually does

CQ_(9)_Phases Counter + Auto Fibonacci Retracement + Trend Pivots is a Pine Script v6 overlay by CQuevedo345 / UkutaLabs. It bundles four structure tools, each running on its own pivot engine:

1. **Zig Zag Trend Metrics** — a swing zigzag labelled HH / LH / HL / LL, with the size and duration of each move, optional range lines and a statistics table.
2. **Auto Fibonacci Retracement + Gauge** — a Fibonacci ladder drawn automatically on the last *settled* leg.
3. **Trend Pivots** — an independent pivot engine ported from "Trend Pivots [Anan]" under the MPL 2.0.
4. **Phase Counter + Adaptive Projection** — a third zigzag with permanent 1-2-3-4-5 numbering and a statistical projection.

The only intentional link between sections is that the Fibonacci ladder is fed by the Section 1 zigzag. Everything else can be tuned or switched off independently.

## The settled-leg idea is the smart part

Zigzag pivots based on a rolling highest/lowest window keep moving until direction flips. That's the classic complaint about auto-Fib tools — the levels you drew get invalidated while you're trading against them.

This script sidesteps it. The ladder is measured on the leg *before* the one still forming (P2 → P1). Both ends are frozen, so the levels never shift while the newest pivot keeps stretching. The current move away from P1 is the retracement being measured. It's a small design decision that removes a real annoyance.

The ladder itself covers 0 / 25 / 40 / 50 / 60 / 75 / 90 / 100 %, with extensions from -200 % through +200 %. Levels nearest price stay bright; distant ones fade, based on documented opacity tiers for the nearest, next-nearest and remaining levels. Entry and target tags sit at 40 %, 50 %, 60 %, 100 %, 125 %, 160 % and 200 %, each with hover tooltips that report zone range, distance from close, whether the level has been reached, and how much of the leg has retraced.

## Where the sections earn their keep

Section 1 gives you context before you touch a level: how big is a typical leg, how long does it usually take, and does the current move look normal or stretched. The stats table uses a geometric mean rather than a simple average, which is the right call when one outsized leg would otherwise dominate the number.

Section 3 is the trigger layer. Fractal-break arrows fire when a bar opens at or below the last pivot high and closes above it (or the inverse for lows), and there are three alert conditions for those breaks. That's what you'd use to time an entry *inside* a Fibonacci zone rather than guessing at the zone itself.

Section 4 is the most ambitious piece. You anchor a pivot you've verified — separately for 1H, 4H, 1D, 1W and 1M — and the counter numbers every other pivot in a repeating 1-2-3-4-5 cycle forward and backward. The Adaptive Projection then extends the current leg to the average length of past legs in the same direction, and reverses using the average length and slope of past opposite legs. The author is explicit that this is a statistical estimate, not a forecast. Take that seriously.

## Pros

- The settled-leg Fibonacci is a genuine fix, not a marketing angle.
- Four independent pivot engines means you can tune one section without breaking another.
- The gauge is unusually informative — range since P1, anchor-to-close move, extreme price with its percentage change, and a profit label.
- Alert conditions on fractal breaks make it usable for execution, not just analysis.
- Honest documentation, including a limitations section that flags object limits (500 labels, 500 lines, 500 boxes) and the profit label's price-unit offset.

## Cons

- That's a lot of on-chart furniture. Four sections plus labels, tags, gauges and projections can bury the candles if you enable everything.
- Price text uses a "$0,000" format, so it reads best on high-priced instruments like BTC. On low-priced or fractional symbols, displayed prices are rounded, and the profit label — offset 100 price units below the close — can sit far from price.
- Phase numbering only shows on 1h / 4h / 1D / 1W / 1M. On any other timeframe it stays hidden.
- The default anchors are largely placeholders. You have to verify and set your own, and if you change the section's Period, the anchor needs re-checking because different Periods produce different pivots.
- Section 3 confirms pivots a set number of bars late and draws them back on the pivot bar — standard, but it means the arrows aren't instant.

## Who it's for

Discretionary swing and position traders who already think in terms of legs and retracements and want the bookkeeping automated. It's less suited to scalpers, who will find the confirmation delays and the visual density working against them, and to anyone trading low-priced instruments, where the label formatting is a real friction point.

## FAQ

**Does it repaint?** The newest zigzag pivot in Sections 1 and 4 keeps updating until direction flips — that's why the Fibonacci ladder uses the settled leg instead. Section 3 pivots confirm after the pivot period elapses.

**Can I run just the Fibonacci part?** Yes. The Fibonacci section has its own master switch that controls levels, extensions, gauge and tags. The zigzag and last-leg highlight are unaffected.

**Does the phase counter work on any timeframe?** Numbering is tied to 1H, 4H, 1D, 1W and 1M anchors. Outside those, it stays hidden.

**Is the projection a price target?** No. It's an average-length estimate capped at 500 bars ahead.

## Verdict

This is a well-considered consolidation of four tools that belong together, with one genuinely useful design fix in the settled-leg Fibonacci. The cost is visual weight and some formatting quirks that narrow the audience. If you trade swings on higher-priced instruments and want structure, retracement, timing and cycle context in one overlay, it's a strong pick. If you need a clean chart or trade cheap symbols, look elsewhere.

⭐⭐⭐⭐
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

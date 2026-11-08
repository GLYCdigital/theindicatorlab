---
title: "Edo Range State Review — Trend Indicator"
date: 2026-11-09T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/edo-range-state.png"
tags:
  - "edo range state"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Edo Range State review: a free open-source TradingView tool that confirms ranges with compactness, efficiency and rotation tests, then tracks breakouts."
tv_script_url: "https://www.tradingview.com/script/iKBJt1S8-Edo-Range-State/"
sources: ["https://www.tradingview.com/script/iKBJt1S8-Edo-Range-State/"]
---
Most range indicators are lazy. They draw a box the moment price flattens out, then erase it the instant price ticks away. Nothing gets measured. Edo Range State takes the opposite approach: it treats a range as a phase with a beginning, a lifespan and a verdict at the end. Whether that makes it worth adding to your chart is what this review is about.

## What it actually does

Edo Range State is a free, open-source Pine Script study. It scans the latest window of closed bars — 20 by default — and only confirms a range when that window passes three tests simultaneously. The box it draws is fixed from the first bar of the window to the confirmation bar and never moves afterward. When price leaves, the range gets a colour-coded verdict: green for a break up, red for a break down.

The indicator is entirely self-contained. Everything is derived from the chart's price series — no volume, no higher timeframe, no external dependency. That's a deliberate design choice, and it keeps the tool predictable across instruments.

## The three tests, and why they matter

This is the part that separates Edo Range State from the usual band-drawing tools. A window qualifies as a range only if it is:

- **Compact** — the distance between the highest and lowest edge is at most 5 times the 50-bar ATR.
- **Directionless** — efficiency (net change of close divided by the sum of every close-to-close change) is at most 0.30. Near 0 means price went back and forth; near 1 means it moved in a straight line.
- **Rotating** — price visited the top zone and the bottom zone at least twice each, where each zone is the outer 20% of the height.

That third test is the one most range tools skip. As the developer notes, height and efficiency alone can't tell a genuine range from a quiet staircase or from two long candles in opposite directions. Rotation can. It's a small detail that meaningfully changes what gets confirmed.

The window is adjustable from 8 to 200 bars, and the height and efficiency limits scale with the square root of the window size — the way a random walk changes with length. The panel always shows the values in use, so you're never guessing what threshold is being applied.

## What you see on the chart

A confirmed range is drawn as a box with a dashed midline, tinted by its origin colour, with dots on candles that test the top or bottom. Edge labels on the right show the price of the top, midline and bottom, plus their distance to price in ATR. Finished ranges stay on the chart filled green or red, with a summary label like "Range · 48 bars · broke up · against its origin." Triangles mark the first close outside the box; orange crosses mark a failed breakout.

The panel is more informative than most. Full mode gives you up to seven rows covering state, range height in ATR, age, position of price, tests, origin bias, history, volatility and last event. Compact mode trims it to four. It also repositions itself so it doesn't cover the drawing, the latest candles or the TradingView legend.

## How breakouts are handled

This is where the logic gets genuinely useful. A breakout attempt begins when a candle closes beyond an edge by at least a 0.10 ATR buffer. It's confirmed with three consecutive closes outside, or a single close at 1 ATR or more beyond the edge. If price closes back inside before confirmation, the breakout is marked failed and the range continues with the same box.

That distinction matters for alerts. "Close above the range" fires earlier than "Range ended" — the first reports the attempt, the second the confirmed exit. If you trade range breaks, that separation is the difference between chasing noise and waiting for structure.

## Pros

- The three-test confirmation filter genuinely reduces false range identification compared to band-style tools.
- Fixed boxes that never stretch mean your reference levels stay honest.
- Origin bias and full history tracking turn the indicator into a running record of how ranges behaved on this instrument.
- Closed-bar-only logic means no repainting of state, counters or alerts.
- Fourteen predefined alerts, all evaluated at bar close.
- Free, open source, and the full Pine Script is publicly accessible.

## Cons

- The automatic panel corner doesn't account for summary labels of finished ranges, so on a crowded chart it can cover one — the developer acknowledges this and suggests switching corners or going Compact.
- With a very zoomed-out chart or a very short window, finished-range summary labels pile up.
- Below 50 bars of history the 50-bar ATR doesn't exist yet, so height isn't measurable and the panel tells you so.
- Labels and the panel corner follow the visible chart, so they shift when you zoom or scroll. The state, boxes, markers and alerts don't — but the moving text can be distracting.

## Who it's for

Discretionary traders who use range structure to frame entries and exits will get the most out of this. It's also a good fit for anyone building a rules-based range breakout system, since the confirmation logic and alert set are well-defined. If you want a tool that tells you when to buy, look elsewhere — by the developer's own framing, this is context, not a signal.

## FAQ

**Does it predict breakout direction?** No. It describes facts: the range was confirmed, price left, the range ended. It does not forecast which way the exit will go.

**Does it repaint?** No. Every decision is taken on closed bars. The only provisional element is the dashed box of a forming range, which disappears if the range isn't confirmed.

**Does the origin bias give an edge?** The documentation is refreshingly honest here — the share of ranges that break with their origin tends to sit close to half. It's a record of behaviour, not a forecast.

**What markets does it work on?** The defaults are calibrated for stocks, indices, forex, gold and crypto. The inputs most users touch are the window and the edge mode (wicks or bodies).

## Verdict

Edo Range State earns its four stars by doing something most range tools don't: it measures a range instead of just drawing one. The three-test filter, fixed boxes and clear breakout states make it a solid piece of analytical infrastructure. The panel overlap issue and label clutter on zoomed-out charts keep it from a perfect score, but those are cosmetic problems in an otherwise well-constructed, free, open-source tool. If range structure is part of how you read a chart, this belongs in your kit.

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

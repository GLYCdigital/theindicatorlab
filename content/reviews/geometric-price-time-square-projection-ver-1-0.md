---
title: "Geometric Price Time Square Projection Ver 1 0 Review"
date: 2026-11-14T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/geometric-price-time-square-projection-ver-1-0.png"
tags:
  - "geometric price time square projection ver 1 0"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "A Gann-style price/time squaring tool that projects a non-repainting master square, harmonic grid, and confluence signals. Honest 4-star review."
tv_script_url: "https://www.tradingview.com/script/Q1Qb5Q7Y-Geometric-Price-Time-Square-Projection-Ver-1-0/"
sources: ["https://www.tradingview.com/script/Q1Qb5Q7Y-Geometric-Price-Time-Square-Projection-Ver-1-0/"]
---
Gann geometry has a long, polarising history on TradingView. Most tools in that space either drown the chart in fan lines or hide the maths behind a black box. This one takes a narrower route: build a single square from one swing, then project it forward as a repeating grid. That's the entire premise, and it's a coherent one.

## What it actually does

The indicator takes a master swing and turns it into a square. Side A is the number of bars in that swing (time). Side B is the high-low range of the swing (price). The square is A bars wide and B points tall, and everything else — grid, diagonals, diamonds, quarter levels, time nodes — is derived from it.

The master square is built from closed bars and, per the author, does not repaint. On daily and above it uses a chosen Gann number (44, 88 or 176 bars); intraday it defaults to one trading session. That distinction matters: the square is a snapshot, not a rolling average, so you're analysing a fixed geometric frame rather than a moving one.

## Inside the geometry

Each cell of the projected grid carries the same internal structure. There are red diagonals representing the price/time angles, a blue inner square at 1/√2 of the side, teal diamonds showing the square rotated 45 degrees, and orange dashed COG lines marking the price centre and time middle. Diamond styles can be set to full diamonds, halves only, or a combination — a small detail with a real effect on chart clutter.

The master splits into four mid squares with quarter levels (¼, ½, ¾) and their own time nodes. Time nodes come in two weights: thick orange verticals for full squares (major cycle markers) and a ½ node for half the square width (minor). Labels show bars from the left edge and bars still to come, and past nodes mirror to the left of the master.

There's also an info label reporting bars, range, price per bar, and the nearest Pythagorean ratio — 3-4-5, 4-3-5 or 1-1-√2. That last piece is the most useful diagnostic in the tool: it tells you whether the swing actually resembles a clean ratio or is just noise.

## How the signals work

Every closed bar is scored across three components: a reversal candle on a time node (TIME), a rejection candle at a square level — base, top, COG or quarter line (PRICE), and a rejection candle on a diagonal (ANGLE). All three agree and you get a large triangle, the strongest tier. Two of three gives a small triangle (the default minimum). One of three gives a circle, hidden by default.

Direction is candle-based: a buy needs a close in the upper half of its range, a sell in the lower half. Green plots below the bar, red above.

## The honest caveats

The author is unusually upfront about one thing that most Gann scripts bury: the optional swing high/low triangles and signals back-filled inside the master window are **hindsight marks, not live signals**. They're drawn when a master is created. If you want strict real-time behaviour you must switch them off. That's a significant disclosure — leave them on and you'll be looking at a chart that flatters itself.

There's also a practical ceiling: TradingView allows 500 lines per script. The recommended settings default to 4 columns each side and 2 rows above and below, and the author notes that reducing the grid is how you get diamonds in every cell. So there's a trade-off between geometric completeness and visual density, and you'll be fiddling with it.

## Recommended starting points

The source lists presets rather than a single default: Gann 44 with Swing TF 3 on 3m–5m for scalping; Gann 88 with Swing TF 10 on 5m–15m for intraday; Gann 88 or 176 on daily for swing and positional work. For indices it suggests Gann 88, "Halves only" diamond style, and minimum confluence 2. Session length presets are given as 375 for NSE, 390 for US stocks, and 1440 for crypto and forex. The author explicitly frames these as starting points, which is the right framing.

## Pros and cons

**Pros**
- Non-repainting master square built from closed bars
- Structured, geometry-based framework instead of arbitrary levels
- Transparent confluence scoring across time, price and angle
- Clear disclosure of hindsight marks in the master window
- Useful swing-ratio diagnostic for judging signal quality

**Cons**
- Dense visual output; line limits force trade-offs on grid size
- The back-filled signals can easily mislead if left enabled
- Steep learning curve for anyone unfamiliar with Gann squaring
- No performance data provided — and none should be assumed

## Who it's for

Traders already comfortable with Gann or price/time geometry, who want a structured confluence map rather than an alert-driven system. It suits swing and positional traders on daily charts best, since the master square is more meaningful over larger swings. Scalpers can use it, but the intraday session-based master means you're rebuilding the frame every day.

## FAQ

**Does it repaint?** The master square and grid are built from closed bars and don't repaint. Live signals fire on bar close. The back-filled signals inside the master window are hindsight marks.

**Can I use it on any market?** The author states it works on any chart and market, with session-length presets for NSE, US stocks, crypto and forex.

**What's the difference between the triangle sizes?** Large means all three components agree; small means two of three; circles mean one of three and are hidden by default.

## Verdict

A well-constructed, honestly documented Gann squaring tool. It does one thing properly and tells you where its limitations are — including the one most scripts hide. The density and learning curve keep it off the top tier, but for traders who think in price/time terms it's a solid addition.

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

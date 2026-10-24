---
title: "Higher Timeframe Peak Session Volume Review — Volume"
date: 2026-10-25T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/higher-timeframe-peak-session-volume.png"
tags:
  - "higher timeframe peak session volume"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Higher Timeframe Peak Session Volume review: BigBeluga overlays up to five HTF volume profiles on price with POC lines and a combined total profile."
tv_script_url: "https://www.tradingview.com/script/dRQLmHat-Higher-Timeframe-Peak-Session-Volume-BigBeluga/"
sources: ["https://www.tradingview.com/script/dRQLmHat-Higher-Timeframe-Peak-Session-Volume-BigBeluga/"]
---
The friction this indicator targets is real and specific: reading higher-timeframe volume normally means leaving your chart. You finish your analysis on the 5-minute, then click over to the 1-hour or 4-hour to see where the session's volume actually sits, then click back and try to remember the levels. BigBeluga's Higher Timeframe Peak Session Volume collapses that loop by drawing completed HTF volume profiles directly into the right margin of your price chart.

## What it actually does

Each new higher-timeframe period — defined by the **Profile Timeframe** input — is detected, and volume is accumulated inside it as the period develops. The indicator tracks that period's start bar, end bar, high, and low, and then renders the finished period as a horizontal volume profile drawn off to the right of current price. It keeps up to **five** recent periods on screen at once, controlled by **Number of Profiles**.

Two details separate this from a generic volume profile tool. First, the bin height isn't fixed. Price rows are calculated as **ATR(100) divided by the ATR Divisor**, so the resolution self-adapts to the instrument's volatility — a quiet market and a violent one get appropriately scaled bins without you re-tuning anything. Second, there's optional **Gaussian smoothing** applied via the Profile Smoothing Radius, which softens the profile shape. Set it to 0 and the raw, spiky profile is what you see.

## The layered context

For every period, the indicator draws a **POC line** — the highest-volume bin — extending from that period's start bar all the way to the right margin, with a label at the origin showing the timeframe, the profile number, and the total period volume. Circle markers cap both ends of the line.

Then there's a piece I think earns the tool its keep: the **Total Polyline Profile**. It aggregates volume across every displayed period into one global profile and traces that combined shape along the right margin, scaled to the max volume bin. Color, line style, and width are all adjustable. So you get two readings at once — a per-session view and a blended view of where volume has genuinely concentrated across the whole window.

## How to use it

The most direct application is treating each period's POC line as volume-weighted support or resistance for that timeframe. Beyond that, overlaying multiple profiles lets you watch the POCs themselves: are they stacking at the same price, which suggests acceptance, or shifting period to period, which suggests rejection and migration? The total polyline gives you the composite picture underneath both.

Two practical knobs stand out. Raising the **ATR Divisor** gives finer bin detail; lowering it gives a smoother, higher-level read. And the visibility toggles let you strip out profiles, POC lines, labels, or borders when the chart gets crowded — which it will, because up to five profiles plus a polyline is a lot of ink. Assigning a distinct color to each of the five slots is almost mandatory for telling periods apart.

## Pros and cons

**Pros**
- Solves a genuine workflow problem — no timeframe switching to read session volume.
- ATR-based binning adapts resolution automatically, so it holds up across different instruments without constant fiddling.
- The combined total polyline plus per-period POCs is a layered read you don't often get in one overlay.
- Fully configurable: timeframe, profile count, colors, smoothing, and visibility all exposed.

**Cons**
- It's a price-chart overlay, not a separate pane, so on lower timeframes with five profiles active the right margin gets busy fast.
- The Gaussian smoothing is a visual/structural transform on the profile — worth understanding before you trust the shape, and it's optional for a reason.
- It's a context tool, not a signal generator. Nothing here tells you when to enter; you still have to do the interpretation.

## Who it's for

Discretionary traders who already use volume profile logic and want higher-timeframe context without leaving their execution chart. It suits intraday traders who care about where the session's value sits relative to price, and swing traders who want to see whether POCs across recent HTF periods are clustering or drifting. It's less useful for anyone looking for a mechanical entry trigger.

## FAQ

**Does it work on any timeframe?**
The Profile Timeframe input sets which higher timeframe is profiled, so you choose the relationship between your chart and the periods being tracked. The source doesn't prescribe specific pairings.

**How many profiles can I show?**
Up to five, set by Number of Profiles.

**Can I turn off the smoothing?**
Yes — set the Profile Smoothing Radius to 0 to disable it.

**Does it repaint?**
The source describes profiles of completed HTF periods; it doesn't make repainting claims either way. Treat the developing period as in-progress.

## Verdict

A focused, well-considered overlay that does one job properly: putting higher-timeframe volume structure on your working chart. The ATR-adaptive binning and the combined total polyline are the standout design choices, and the configurability means you can dial clutter down to taste. It won't hand you trades, and the right-margin density is a real trade-off — but as a context layer, it's a solid addition to a volume-aware workflow.

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

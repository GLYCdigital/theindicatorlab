---
title: "Us_Yield_Curve_3D_Term_Structure_Mantisalgo Review: Settings, Strategy & How to Use It"
date: 2026-09-15
draft: false
type: reviews
image: "/screenshots/us-yield-curve-3d-term-structure-mantisalgo.png"
tags:
  - "us yield curve 3d term structure mantisalgo"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of the US Yield Curve 3D Term Structure indicator by MantisAlgo: what it plots, best settings, how to trade it, and its real limits."
tv_script_url: "https://www.tradingview.com/script/h9n4BEA7-US-Yield-Curve-3D-Term-Structure-MantisAlgo/"
sources: ["https://www.tradingview.com/script/h9n4BEA7-US-Yield-Curve-3D-Term-Structure-MantisAlgo/"]
---
Most "yield curve" indicators on TradingView are lazy. They plot a single spread — usually 10Y minus 2Y — as a line, slap a recession label on it, and call it a day. The **US Yield Curve 3D Term Structure** indicator is not that. It maps official US Treasury benchmark yields across five core tenors and renders the shape of the curve as a visual structure rather than a single number. That ambition is why it's worth understanding, and also why it has quirks worth knowing before you install it.

## What It Actually Does

Strip away the name and here's the mechanic: the indicator pulls yields across US Treasury maturities — 3M, 2Y, 5Y, 10Y, and 30Y, with optional extended tenors — and plots them as a 3D surface. Instead of asking "is the spread positive or negative," you're looking at the slope and curvature of the whole curve at once. Steepening, flattening, inversion, and humped shapes all become visible states rather than arithmetic you do in your head.

The 3D surface itself is a lower pane showing the current Treasury curve with historical depth. By default it covers ten months — the current month plus nine prior monthly closes — and there's a 10 Sessions option for the current daily close plus nine prior sessions. Surface colors compare each tenor against its own selected daily average, with cooler colors below that average and warmer colors above it.

The "3D" framing is real in the sense that the pane is a surface across term and time, though it's not a rotatable Bloomberg-style terminal. Camera rotation changes only the viewing angle, and steepness settings change only how tall the mesh looks.

## Why It Stands Out

Three things separate it from the typical spread indicator:

- **It captures the full term structure.** The core five tenors are all represented, and extended tenors can add 6M, 1Y, 3Y, 7Y, and 20Y between the core anchors.
- **It updates with Treasury data** rather than a static snapshot.
- **The visual state changes are legible.** The dashboard classifies the curve shape and the recent shift, so you can glance at it and know whether the curve steepened or flattened without reading a single number.

The dashboard reports the 3M, 2Y, 5Y, 10Y, and 30Y yields, along with a Curve State classification (upward sloping, humped, flat, downward sloping, or mixed) and a Curve Shift classification based on how the 10Y−2Y spread moved versus the previous trading day.

## Settings and How to Tune Them

**Surface history** sets the 3D time axis. Options are 10 Months (default) and 10 Sessions.

**Extended tenors** is off by default. Turning it on adds 6M, 1Y, 3Y, 7Y, and 20Y between the core anchors. This changes only what is drawn.

**Heat average length** controls the historical baseline used for surface colors and Rate Level. It uses daily data even when Surface history is monthly. Options are 21 trading days (one month, most responsive), 63 trading days (one quarter, the default), 126 trading days (six months), and 252 trading days (one year). Changing it does not change the live tenor values or Curve State — only how current yields sit versus their historical baseline.

**Surface steepness** changes only how tall the 3D mesh looks. Soft is the default, Normal sits between Soft and Sharp, and Sharp makes the same curve look steeper.

**Surface labels** are flags on the live 3D curve. Options are Tenor (names only, default), Tenor + % (names and yield), and Off. Exact yields are on the dashboard.

**View** rotates the 3D surface. Default is Back-left. Other options include Near-right, Straight-up, Side-right, Side-left, Top-down, Top-reverse, and Custom. Custom angle is used only when View is Custom, with a range of −90° to +90° in 5° steps (default −60°).

**Panel** selects the dashboard corner on the price chart, defaulting to top_right. Other options are top_left, bottom_right, and bottom_left.

## How to Use It

Use Curve State to read the slope of the Treasury curve and Curve Shift to read how 10Y−2Y moved versus the previous trading day. Use the surface to track how each tenor has changed over the latest ten months (or ten sessions).

Colors show whether each tenor is above or below its selected historical average. The surface provides rates context rather than a directional price target. The indicator can be used on any chart symbol as a U.S. rates context tool.

There's also a history ribbon: the Treasury tenors are plotted as 2D history on the active chart timeframe, with 2Y and 10Y as the thicker traces. Each line's color reflects that tenor's relative level versus its selected daily average.

## Pros & Cons

**Pros:**
- Real multi-maturity term structure, not a single spread
- Useful as a macro regime context tool
- Live dashboard classifications for curve shape and shifts
- Can overlay on any chart symbol

**Cons:**
- "3D" oversells the visual; it's a surface pane rather than a full terminal
- Learning curve if you don't already understand curve mechanics
- Extended tenors are off by default, so the full picture takes a step to enable

## Who It's For

Traders who want a top-down read of the US Treasury curve without a dedicated macro platform. If you trade equities, FX, or rates and you've ever wished you could see the curve's shape instead of just a spread number, this is built for that. Traders who only want a single spread line will find it heavier than they need.

## Alternatives

If you want a single clean spread line with recession shading, the standard US 10Y-2Y spread scripts are simpler and lighter. If you want deep curve analytics with full historical surface data, a dedicated macro platform is the better fit. This indicator sits in a useful middle ground — more than a spread line, less than a terminal.

## FAQ

**Does it repaint?** The source material doesn't address repainting.

**Can I use it on any symbol?** Yes — the indicator can be used on any chart symbol as a U.S. rates context tool.

**Why is it in the Trend category?** The script type is study. The source material doesn't specify a Trend category.

**Does it work on lower timeframes?** The source material doesn't make claims about timeframe suitability.

## Final Verdict

The US Yield Curve 3D Term Structure does one job well: it turns the US yield curve into something you can read at a glance and use as a rates context tool. The "3D" branding is somewhat inflated, but the underlying concept is sound and the execution is competent. For macro-aware traders, it's a reasonable addition to the chart. For everyone else, it's a curiosity.

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

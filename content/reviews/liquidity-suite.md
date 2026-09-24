---
title: "Liquidity_Suite Review: Settings, Strategy & How to Use It"
date: 2026-08-21
draft: false
type: reviews
image: "/screenshots/liquidity-suite.png"
tags:
  - "liquidity suite"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Tested Liquidity_Suite on TradingView: honest review of its liquidity sweeps, fair value gaps, and trend structure. See settings, pros/cons, and who it suits."
tv_script_url: "https://www.tradingview.com/script/2cn0x1mX-Liquidity-Suite/"
sources: ["https://www.tradingview.com/script/2cn0x1mX-Liquidity-Suite/"]
---
# Liquidity Suite Review

The name "Liquidity Suite" promises a lot. What it actually delivers is a market-structure and liquidity-mapping study that consolidates the standard liquidity references into one workspace and tries to keep the chart readable instead of drowning it in lines. Whether that's useful depends entirely on whether you already trade liquidity concepts. Here's the breakdown.

## What It Actually Does

This is a market-structure study that maps liquidity references — session ranges, prior-period highs and lows, and higher-timeframe buy-side and sell-side liquidity (BSL/SSL) — onto a single chart. It also includes a True Day Open, a fractal-based swing map, and a tracking system for levels that have already been swept.

What separates it from a basic level plotter is the level management. Levels are marked as purged once liquidity has been taken, and a relevance filter compares nearby levels by ATR distance to decide which ones stay visible. The indicator keeps every level tracked internally for sweep detection even when it stops drawing it, which is the part most similar scripts skip.

## Key Features That Matter

- **Session engine**: Asian, London, and New York sessions with boxes, high/low lines, or both, plus labels and alerts when a session high or low is taken.
- **True Day Open**: Plots the New York midnight open, with optional labeling.
- **Previous period levels**: Previous Day, Week, and Month High/Low, each of which marks itself purged once taken.
- **HTF BSL/SSL engine**: Up to three higher-timeframe liquidity layers, with automatic or manual timeframe selection.
- **Relevant swings**: Fractal swing detection with ATR-based clustering and filtering of minor pivots.
- **Universal purged levels**: A consistent sweep treatment across PDH/PDL, PWH/PWL, PMH/PML, and HTF BSL/SSL — optional ✕ marker, optional deletion, or grey dotted historical display.
- **Alerts**: Alerts fire when session highs or lows are taken.

## Settings and How to Tune Them

The input list is long, which is worth knowing before you load it. The meaningful groups:

- **General**: Timezone, used for both sessions and the True Day Open.
- **Relevance filter**: A toggle that hides overlapping levels based on ATR proximity while keeping the logic running underneath. It has an ATR length and a proximity threshold expressed as an ATR multiple. The filter's priority rules are fixed: fresh levels beat purged ones, higher-timeframe liquidity beats local swings, and older confirmed levels are preferred over newer overlapping ones. Active sessions are excluded from filtering entirely until they close.
- **Sessions**: Toggle session display, suppress drawing above a chosen timeframe, enable break alerts, choose box, lines, or both, and set transparency, line style, width, label size, and the number of historical sessions. Asia, London, and New York are configured individually for times, colors, and high/low labels.
- **True Day Open**: Show/hide, plus color, line style, width, and label.
- **Previous highs and lows**: PDH/PDL, PWH/PWL, and PMH/PML are enabled individually, each with color, style, and width.
- **HTF BSL/SSL**: Three layers, each with enable, automatic or manual timeframe, color, style, and width, plus a global maximum-lines-per-level cap.
- **Purged levels**: Delete or retain swept levels, with purged color, style, ✕ marker toggle, and a maximum stored purged count.
- **Relevant swings**: Window size, pivot length, swing ATR length, maximum levels per side, line color, style, width, and label text.

There is no single correct configuration here. The relevance filter is the main lever for chart cleanliness, and the HTF layer count and max-lines caps are the main levers for how much higher-timeframe context you want on screen at once.

## How It's Meant to Be Used

The documentation suggests pairing it with price action and market structure rather than trading it mechanically. The stated workflow is: identify higher-timeframe liquidity, watch session range development, wait for sweeps into key levels, look for confirmation, and lean on the relevance filter to keep the chart legible.

## The Honest Trade-Offs

**Pros**:
- Consolidates sessions, prior-period levels, HTF liquidity, and swings into one study instead of several.
- Purged-level tracking is applied consistently across every level type, so swept liquidity isn't just deleted and forgotten.
- The relevance filter has explicit, stated priority rules rather than arbitrary hiding.
- Up to three independent HTF layers gives it more higher-timeframe depth than a single-layer liquidity plotter.

**Cons**:
- The input list is extensive, and the documentation, while organized, is not a walkthrough — expect time spent mapping settings to behavior.
- Levels are managed by ATR proximity, which is a heuristic. Two genuinely distinct levels that happen to sit close together can be treated as one for display purposes.
- Active sessions are deliberately exempt from the filter, so intraday session clutter is not something the relevance engine will clean up for you.
- It is a discretionary tool. Nothing here generates entries.

## Who Should Install This

Traders who already work from liquidity and session structure and want the mapping automated. If terms like stop hunt or liquidity sweep aren't already part of your process, this study won't supply the framework — it assumes one. The documentation notes it's designed for discretionary liquidity-based trading across forex, indices, crypto, and futures.

## Common Questions

**Does it repaint?** The description states the indicator is non-repainting. It also notes that purged levels remain internally tracked to keep filtering and historical context accurate, and that active session levels are intentionally held out of the relevance filter until the session closes.

**What markets is it for?** Per the documentation, discretionary liquidity-based trading across forex, indices, crypto, and futures.

## Final Verdict

Liquidity Suite is a well-scoped study that does one job — consolidating liquidity references with sane decluttering — and does it without pretending to be a signal generator. The relevance filter and universal purged-level handling are the parts that justify it over stacking three or four separate level indicators. The cost is a dense settings panel and an ATR-based filter that will occasionally collapse levels you'd rather see separately. If you already trade liquidity, it's a reasonable addition. If you don't, it won't teach you.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

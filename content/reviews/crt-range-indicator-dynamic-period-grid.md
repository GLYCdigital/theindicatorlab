---
title: "Crt_Range_Indicator_Dynamic_Period_Grid Review: Settings, Strategy & How to Use It"
date: 2026-08-16
draft: false
type: reviews
image: "/screenshots/crt-range-indicator-dynamic-period-grid.png"
tags:
  - "crt range indicator dynamic period grid"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Crt_Range_Indicator_Dynamic_Period_Grid tested: A dynamic support/resistance grid that adapts to volatility. Settings, pros/cons, and honest verdict inside."
tv_script_url: "https://www.tradingview.com/script/JVMlgA3j-CRT-Range-Indicator-Dynamic-Period-Grid/"
sources: ["https://www.tradingview.com/script/JVMlgA3j-CRT-Range-Indicator-Dynamic-Period-Grid/"]
---
I’ll be straight with you: most “range” indicators just redraw old highs and lows with fancy colors. This one is different in intent. The CRT Indicator [Dynamic Period Grid] is built around Candle Range Theory and liquidity concepts, and it frames a higher-timeframe range on your execution chart instead of leaving a mess of historical lines behind.

## What This Indicator Actually Does

The script looks at your chosen Higher Timeframe — say the 1-Hour chart — and establishes the High and Low of the most recently closed candle. That’s the Master Candle, and its range becomes the grid.

It then draws a clean bounding box around that range on your current lower timeframe — say the 15m chart. As long as subsequent HTF candles form inside the range, the box expands to the right, dropping a new vertical grid line to mark the passage of each new HTF period. The Master Range is only considered broken if a HTF candle closes outside the boundaries. On a true close, the old grid is wiped away and a brand new Master Range is established.

So the point isn’t a static level drawn months ago. It’s a live frame around the current HTF accumulation and manipulation phases, projected down onto the timeframe you actually execute on.

## Key Features That Stand Out

Three things define this tool:

1. **Liquidity Grab Detection (the Latch System)** — If price wicks past the range boundary but fails to close outside it, the indicator permanently latches a warning onto the chart. The breached horizontal line changes to your designated Breach Color, and the text label updates to explicitly call out a “(Liquidity Grab)”.
2. **Dynamic Grid Expansion** — The internal vertical lines keep your lower timeframe synced with the higher timeframe’s pacing, so you aren’t guessing where you are in the session.
3. **Unified, clean visuals** — The base grid stays a single solid color, defaulted to Yellow. Only levels that have been tested or swept change color, so your eye goes exactly where it needs to.

One more point worth flagging: the indicator is described as repaint-free multi-timeframe, built with secure historical data referencing so it plots accurately in real-time without looking into the future or repainting historical data.

## Settings and How to Tune Them

- **Master Timeframe** — Select the HTF you want to define your range (e.g., 60 for 1H, 240 for 4H). The text labels update automatically to reflect your choice.
- **Base Line/Text Color** — Customize the default color of the unbroken range grid.
- **Breach Colors** — Fully customize the visual alerts for when buy-side or sell-side liquidity is swept (e.g., Green for a high sweep, Red for a low sweep).
- **Line Styles & Widths** — Toggle between solid, dashed, or dotted lines to fit your chart aesthetic.

There is no sensitivity slider, no level-count parameter, and no calculation-window tuning here — the grid is defined by the HTF candle range, not by a volatility model you dial up or down.

## How to Use It (Entry/Exit Logic)

This isn’t a buy/sell signal indicator. It’s a structure tool. The documented approach is the sweep trade:

**Trading the sweep:** Wait for the boundary line to change color and display “(Liquidity Grab)”. Once the sweep is confirmed and price rejects back inside the grid, target the opposite side of the Master Range.

The distinction the tool is built to make is between a true structural breakout — a HTF candle closing outside the range — and a liquidity sweep, where price wicks past the boundary but closes back inside. That is the core read.

## Pros & Cons

**Pros:**
- Frames the active HTF range on your execution timeframe without endless historical lines
- Explicitly separates true closes outside the range from wick-only liquidity grabs
- The latch system keeps swept levels marked rather than letting them scroll away
- Base grid stays a single color, so only tested levels draw your attention

**Cons:**
- It is not a standalone strategy — the documented use requires waiting for a sweep and a rejection back inside
- The breakout reset depends entirely on HTF closes, so the grid only changes when a new HTF candle closes outside
- It is a structural framing tool, not a signal generator

## Who It’s For

This is for traders who already work with Candle Range Theory and liquidity concepts, and who execute on a lower timeframe while defining structure on a higher one. If you don’t already think in terms of HTF range, sweep, and close-back-inside, the grid won’t hand you a thesis — it will just frame one.

## FAQ

**Q: Does the indicator repaint?**
A: The script is described as repaint-free multi-timeframe, using secure historical data referencing so it plots accurately in real-time without looking into the future or repainting historical data.

**Q: Does it give buy/sell signals?**
A: No. It provides structure. The documented workflow is to wait for a confirmed sweep and rejection back inside the grid, then target the opposite side of the Master Range.

**Q: What defines a breakout versus a sweep?**
A: A breakout is a HTF candle closing outside the Master Range boundaries, which wipes the old grid and starts a new one. A sweep is a wick past the boundary with no close outside, which latches a “(Liquidity Grab)” label and recolors the breached line.

## Final Verdict

The CRT Indicator [Dynamic Period Grid] does one job: it tracks the active HTF Master Range, expands the grid forward as new HTF periods form inside it, and resets only on a true close outside. The latch system gives it a genuine edge over plain range boxes, because swept liquidity stays marked instead of vanishing.

It’s not a holy grail, and it isn’t pitched as one. It’s a structural framing tool for traders who already read liquidity. If your charts are cluttered with stale levels that no longer mean anything, this is a cleaner way to see the range that currently matters.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

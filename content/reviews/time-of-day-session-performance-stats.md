---
title: "Time_Of_Day_Session_Performance_Stats Review: Settings, Strategy & How to Use It"
date: 2026-08-19
draft: false
type: reviews
image: "/screenshots/time-of-day-session-performance-stats.png"
tags:
  - "time of day session performance stats"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Time_Of_Day_Session_Performance_Stats review: session stats, best settings, entry logic, pros/cons, and who should use it."
tv_script_url: "https://www.tradingview.com/script/Yr3kT0uI-Time-of-Day-Session-Performance-Stats-QuantAlgo/"
sources: ["https://www.tradingview.com/script/Yr3kT0uI-Time-of-Day-Session-Performance-Stats-QuantAlgo/"]
---
Most session indicators just paint a colored background and call it a day. The Time-of-Day/Session Performance Stats does something more substantive: it converts historical bars into ranked statistics by hour of day and by session, then overlays the result directly on the chart. It is a time-based analysis tool rather than an entry signal, and its value lies in telling you when markets have historically moved, not when to buy or sell.

Here's what it actually does: the indicator walks a configurable window of past bars in a selected timezone, assigns each usable bar to its hour of day and to any sessions it falls inside, and accumulates range, volume, directional closes, and drift in parallel. Range can be measured as a percent of close or in raw price units. Hours that fail a minimum bar-count threshold are dropped from every ranking so small samples can't distort the boards.

Five ranking boards are produced: Activity (average range), Volume (when the symbol reports it), Bias (percentage of directional bars that closed higher), Drift (mean close-minus-open percentage), and Aggregated (the mean percentile of range, volume, and directional edge). A separate Session Ranking panel orders the four major sessions by average range per bar. The Focus Hours panel translates the Aggregated ranking into four labeled allocation plans plus the single quietest hour to avoid.

**Settings and How to Tune Them:** Session windows for Sydney, Tokyo, London, and New York can each be enabled or disabled and given custom HHMM-HHMM values in the selected timezone. A weekdays-only filter removes weekend bars for forex, futures, and equities while leaving crypto intact. The Bars To Include setting restricts the study to all bars, any enabled session, or one named session. Range can be expressed as percent of close or raw price units. Overlays are driven independently by any of the rankings or by Focus Hours, with transparency controls to keep the shading obvious or subtle. Six color presets (Classic, Aqua, Cosmic, Cyber, Neon, Custom) apply a continuous gradient from the bullish color at rank 1 to bearish at the last rank; Custom mode exposes individual color pickers with automatic text contrast. There is no single "best" configuration — the appropriate choices depend on your instrument and schedule.

**How it's meant to be used:** This is a filter, not a standalone signal. The Aggregated ranking and Focus Hours panel are intended to show which windows historically carry the most range, volume, and directional edge, so activity can be concentrated where the data supports it. Divergences between the Bias and Drift boards are often the most interesting readings, since an hour can post a high bull rate yet still show negative drift if its losing bars are larger than its winning ones.

**Pros:**
- Turns vague "I trade better in the morning" impressions into ranked statistics
- Session boundaries are fully customizable, so windows can match any schedule rather than just the standard centers
- Overlays are computed from a trailing window, so background shading and bar coloring never repaint
- Built-in alerts cover entry into the peak activity hour, the quietest hour, the peak volume hour, the most bullish or bearish hour, the top Aggregated hour, session opens and closes, and the London-New York overlap

**Cons:**
- Rankings depend on sufficient bar counts per hour; hours below the minimum threshold are dropped entirely
- On chart intervals above 1 hour, most of the 24 hour buckets never receive a bar and the rankings are incomplete — the indicator displays a warning and recommends switching to 5m, 15m, 30m, or 1h
- The Volume board is hidden automatically on symbols that report no volume
- It is an analysis tool, not a trend-finding or entry system

**Who it's for:** Traders who already have a defined approach and want ranked insight into when markets actually move. It suits crypto traders running around the clock as well as equity and forex traders working a weekday session schedule. It is less suited to anyone looking for discrete trade signals.

**Alternatives worth considering:** Simpler session-shading tools give a cleaner visual of when volume and volatility hit without the ranking and statistics layer. Dedicated trade-analytics tools offer more granular per-trade reporting but lack the hour-of-day and session segmentation that makes this one distinctive.

**FAQ:**
- *Does it work with backtests?* The indicator analyzes historical bars for its statistics; it is not a strategy tester and does not produce backtest results.
- *Can I use it on crypto?* Yes. Sessions can be toggled and given custom windows in the selected timezone, and the weekdays-only filter leaves crypto fully intact.
- *Does it repaint?* No. Chart overlays read a trailing window of the same length rather than the final ranking, so background shading and bar coloring never repaint.

**Final verdict:** The Time-of-Day/Session Performance Stats won't make you a better trader by itself, but it replaces anecdote with ranked statistics. It exposes how much of your result depends on when you're active, and it does so with a non-repainting overlay and a clear set of ranking boards. The main caveats are the interval restriction above 1 hour, the reliance on adequate bar counts per bucket, and the fact that it analyzes rather than signals. For traders with an existing approach who want to optimize execution timing, it is a worthwhile addition to the toolkit. ⭐⭐⭐⭐

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

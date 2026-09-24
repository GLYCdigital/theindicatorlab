---
title: "Three_Session_Volume_Profile Review: Settings, Strategy & How to Use It"
date: 2026-09-17
draft: false
type: reviews
image: "/screenshots/three-session-volume-profile.png"
tags:
  - "three session volume profile"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Three_Session_Volume_Profile review: an honest look at this volume profile tool, its best settings, how to trade it, and where it falls short."
tv_script_url: "https://www.tradingview.com/script/CDfsfyDO-Three-Session-Volume-Profile/"
sources: ["https://www.tradingview.com/script/CDfsfyDO-Three-Session-Volume-Profile/"]
---
Most "volume profile" scripts on TradingView do the same thing: they draw a histogram on the side of your chart and call it a day. Three_Session_Volume_Profile takes a different angle. Instead of one profile, it builds three — typically covering distinct trading sessions (Asia, London, New York, or whatever split you configure) — and plots them so you can compare where volume actually accumulated across the day.

Here's what it does, where it earns its keep, and where it stumbles.

## What this indicator actually does

Strip away the naming and you get a session-segmented volume profile. The script divides the trading day into three windows, calculates a volume-at-price distribution for each, and renders a separate profile, Point of Control, Value Area, VWAP, and optional deviation bands for each period.

Each session is treated as its own auction. The value isn't in any single profile; it's in the comparison. If one session's POC sits well below another's, you're looking at a session that built value at a different level. How price behaves around a prior session's POC during the next session is one of the contextual observations the tool is built to support.

The default schedules use the America/New_York time zone: Asia 18:00–03:00, London 03:00–09:30, and New York 09:30–16:00. All schedules and the time zone are configurable, and the America/New_York setting automatically accounts for daylight-saving changes.

## Key features worth noting

- **Three independent profiles**, each resetting its calculations at the start of its own session. Sessions may overlap, and each continues to calculate independently when they do.
- **POC and Value Area per session.** The POC is the midpoint of the profile row containing the greatest allocated volume. VAH and VAL define the boundaries of the selected value area.
- **Value Area percentage is configurable.** The default contains 70% of session volume, but this percentage can be adjusted. Increasing it produces a wider area; reducing it produces a narrower one around the POC.
- **Session VWAP with optional deviation bands**, resetting independently at the beginning of each session. VWAP uses HLC3 as the representative bar price and weights it by volume. The standard deviation calculation is also volume-weighted, and the selected multiplier is applied above and below VWAP to produce the bands.
- **Developing and completed levels.** While a session is active, developing VAH, VAL, and POC can be displayed and update as new price and volume information enters. When the session ends, the final profile and levels are stored as completed values, and the number of completed profiles retained per session can be controlled from the settings.
- **Profile placement.** Each profile can be anchored left (to the session opening edge, extending right) or right (to the session closing or current edge, extending left). This refers to the boundaries of each session, not the edges of the visible chart. A separate Maximum width setting controls horizontal display width in chart bars and does not affect the underlying volume calculations.

The settings panel is crowded. If you want to open an indicator and go, budget time for setup.

## Settings and How to Tune Them

- **Time zone.** Select the time zone used to interpret all three schedules. America/New_York is suitable when session times should follow Eastern Time and adjust automatically for daylight saving. Use a fixed UTC offset only when daylight-saving adjustment is not desired.
- **Session times.** Set the opening and closing time for Asia, London, and New York. Overnight schedules, such as 18:00–03:00, are supported.
- **Rows.** Controls profile resolution and supports values from 12 to 200. More rows provide finer price segmentation but also increase calculation requirements. Lower values produce broader profile levels and require fewer calculations.
- **Value Area percentage.** The standard default is 70%. Increasing the percentage produces a wider Value Area, while reducing it produces a narrower area around the POC.
- **Completed vs. developing levels.** Developing levels can be used to observe how the current session's distribution changes; completed levels provide fixed references from prior sessions.
- **VWAP and deviation bands.** Optional, and can be enabled to visualize dispersion around the session-weighted reference price.

One behavior to understand: developing profiles and levels update during the active bar as its high, low, and volume change. This is normal real-time recalculation and should not be interpreted as a fixed signal. A new session high or low changes the profile range and can cause all rows to be redistributed. Completed levels remain fixed unless chart data, timeframe, symbol, session schedule, or indicator settings are changed.

## How to use it

The framework the indicator supports is cross-session context:

1. Mark the prior session's POC and value area boundaries.
2. Observe whether price accepts or rejects a previous session's Value Area.
3. Watch whether price rotates around a prior POC, moves from one session's value region toward another, or holds above or below a prior VAH or VAL.
4. Note whether price trades near or away from the active session VWAP, with deviation bands providing context for how far price is trading from the session's weighted mean.

These are contextual observations rather than predefined entry or exit signals. The indicator does not provide trade entries, exits, profit projections, or guarantees of future performance.

## Pros and cons

**Pros:**
- Genuinely useful cross-session comparison — most volume profile scripts don't separate sessions this way.
- Configurable sessions, value area, and time zone, so it adapts to different markets.
- The profile, VWAP, and deviation bands all use the same independently resetting session windows, so the components are internally consistent rather than merged from unrelated studies.
- No lookahead: the indicator does not request future data, and completed sessions are based only on bars belonging to those sessions.

**Cons:**
- Crowded settings panel with cosmetic inputs alongside the functional ones.
- Developing levels move during the active bar, which can look like flicker on lower timeframes with live data.
- The profile is an approximation built from chart-bar ranges and volume, not a tick-level bid/ask profile, footprint chart, or reconstruction of individual transactions.
- Changing the chart timeframe can change the resulting distribution.

## Who it's for

This is for intraday traders — futures, forex, or crypto — who already understand volume profile and want a session-comparison view. If you're a swing trader holding for days, the session granularity may be more than you need. If you're new to volume profile, a simpler single-profile script is a better starting point.

## Interpretation and limitations

A wide section of the profile represents a row receiving relatively more allocated volume; a narrow section represents relatively less. POC and Value Area levels identify areas of historical participation, but they do not guarantee future support or resistance. Their interpretation depends on market structure, volatility, liquidity, instrument type, and the trader's broader methodology.

On centralized futures markets, the script uses the exchange-reported volume available on the chart. On markets where only tick volume is available, the profile reflects that data instead of centralized transaction volume. Results can differ from volume-profile tools that use lower-timeframe or transaction-level data.

Because standard chart data does not provide the exact price of every transaction, each chart bar's volume is allocated across the profile rows intersected by that bar's high-low range, proportional to the amount of the bar's range overlapping each row. A bar with no measurable range has its volume assigned to the row containing its representative price.

## Final verdict

Three_Session_Volume_Profile does one thing well: it lets you compare value across three sessions at a glance, with POC, Value Area, VWAP, and deviation bands all derived from the same session windows. That's a coherent framework. The tradeoffs are the crowded settings panel, the developing-level recalculation during live bars, and the fact that it's an approximation from chart bars rather than transaction-level data. If cross-session volume comparison is what you're missing, this fills that gap.

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

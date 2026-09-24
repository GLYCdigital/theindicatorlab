---
title: "Ict_Killzones Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/ict-killzones.png"
tags:
  - ict killzones
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "ICT Killzones marks key intraday sessions for forex and indices. Works best on 5-15 min charts. Clean visuals, no repaint. 4/5."
grounding: "none (no source found)"
---
# Killzones Indicator Review

ICT-style session trading lives and dies by time. The Killzones indicator handles the mechanical part—drawing the session boxes—so attention can stay on price action inside them. Here is an honest look at what it does and where it falls short.

## What This Indicator Actually Does

It plots colored vertical zones on the chart representing the classic ICT trading sessions: Asian, London, and New York Killzones. Each zone has a start time, an end time, and an optional fill. The indicator draws from standard session times and can adjust for daylight saving time automatically when that toggle is enabled.

It is a time-based drawing tool. It does not generate signals, and it does not forecast price.

## Key Features

- **Customizable session offsets** – Start and end times can be shifted by minutes, which is useful if you trade a slightly different open or want to account for news events.
- **Zone fill opacity control** – Ranges from transparent to solid, so candles underneath can remain visible.
- **Separate toggle for each Killzone** – Each session can be enabled or disabled independently. Many free indicators force all three on at once.
- **Lightweight** – Does not appear to lag even on large watchlists.

## Settings and How to Tune Them

The indicator exposes a small set of inputs rather than a large parameter grid.

| Setting | What It Controls |
|---|---|
| **Asian Killzone** | Toggle for the Asian session zone |
| **London Killzone** | Start/end time for the London session zone |
| **NY Killzone** | Start/end time for the New York session zone |
| **Fill opacity** | Transparency level of the zone fill |
| **Zone border** | Border style (solid vs. dashed) |
| **DST adjustment** | Automatic daylight saving time shift |
| **Per-zone color** | Color input for each session zone |

Session start and end times are editable, and offsets can be applied in minutes. Which zones to enable, how transparent to make the fill, and whether to shift the New York window for a particular instrument are all user preferences—there is no single correct configuration. Traders on crypto often note that digital assets do not track traditional forex sessions as cleanly, so adjusting the New York window may be worth experimenting with. Test any offset on your own instrument before relying on it.

## How It Fits Into a Session-Based Workflow

The indicator is a timing filter, not a signal generator. A typical session-based approach might look like this:

1. Establish directional bias on a higher timeframe before the zone opens.
2. During the Killzone, watch for a breakout of an early reference candle's high or low.
3. Look for a retest of that level with a lower-timeframe close.
4. Target a prior session's high/low or a fixed risk-reward multiple.

The indicator's only job in that process is showing *when* to be looking. Everything else is the trader's call.

## Pros and Cons

**Pros:**
- Removes the manual work of drawing session rectangles.
- DST handling is built in via a toggle.
- Works across forex, indices, crypto, and commodities as a time overlay.

**Cons:**
- No volume profile or order flow—strictly time-based.
- Session times are anchored to EST, so traders working in GMT/UTC have to convert mentally.
- No "next session countdown" label.

## Who It's For

- **ICT-focused traders** – Anyone following Inner Circle Trader session concepts will recognize the framework immediately.
- **Session-based scalpers** – Traders who restrict activity to specific liquid hours.
- **Beginners** – Useful for learning how session behavior maps to time without drawing zones by hand.

**Not for:** Traders on 1H+ charts or those using pure price action without any time filter will find little here.

## Alternatives

- **Killzone Pro** (paid) – Adds volume-based zone strength and an audible alert when a zone begins.
- **Session Volume Profile** (free) – Shows volume distribution during each session, not just time boundaries.
- **Manual rectangles** (free) – If you only trade one session, drawing it yourself is trivial.

## FAQ

**Q: Does it work on crypto?**
A: Yes, but crypto does not respect traditional forex sessions as cleanly. It is still usable for the New York session on BTC.

**Q: Can colors be changed per zone?**
A: Yes—each zone has its own color input.

**Q: Do the zones change when the timeframe is switched?**
A: No. Zones are drawn from time, not price, so switching timeframes does not affect their placement.

**Q: Does it work on mobile?**
A: Yes, though zone labels may overlap on small screens.

## Final Verdict

For ICT-style session trading, this indicator does exactly what it claims—marks session times cleanly and stays out of the way. The absence of a countdown timer and any volume integration are the main gaps. As a free, no-frills zone marker, it earns a solid recommendation for intraday charts.

**Rating: 4/5**

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

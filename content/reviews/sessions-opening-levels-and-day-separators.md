---
title: "Sessions_Opening_Levels_And_Day_Separators Review: Settings, Strategy & How to Use It"
date: 2026-09-18
draft: false
type: reviews
image: "/screenshots/sessions-opening-levels-and-day-separators.png"
tags:
  - "sessions opening levels and day separators"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Sessions_Opening_Levels_And_Day_Separators review: honest look at session levels, day separators, best settings, pros, cons, and who should install it."
tv_script_url: "https://www.tradingview.com/script/KuFF1J1D-Sessions-Opening-Levels-and-Day-Separators/"
sources: ["https://www.tradingview.com/script/KuFF1J1D-Sessions-Opening-Levels-and-Day-Separators/"]
---
Most session indicators try to do too much. They stack highs, lows, midpoints, and VWAPs onto your chart until you can't see the candles anymore. This script does the opposite — it draws where trading days and weeks begin, shades the major sessions, marks previous period highs and lows, and draws reference opening levels. Then it gets out of the way.

## What This Indicator Actually Does

Strip away the name and here's the mechanic, as stated in the script's own documentation: it draws vertical lines where each trading day and week begins, shades four major sessions (Asia, London, New York AM, New York PM), marks the high and low of previous completed days, weeks and months, and draws horizontal lines at reference opening prices — the 00:00 open, the 10:00 open, today's open, this week's open, this month's open, this year's open, and the all-time high.

That's it. The author is explicit that it produces no buy or sell signals, that every level is a historical measurement of where price has already been, and that none of it is a probability, forecast, or expectation. It's a reference tool. If you came looking for buy/sell arrows, this is the wrong script.

The value proposition is context. The script bundles four modules that would otherwise occupy four separate indicator slots and four separate settings panels, and each module's calculation is open source.

## Key Features That Set It Apart

The day boundary is a real setting rather than an assumption. Five modes are available: Auto (the exchange's own session), Market open only, Midnight in exchange time, Midnight in New York, or a custom clock time in one of eleven timezones. Most session tools fix the separator to the exchange session or a single hardcoded hour.

The week line can follow the day line. If your day starts at midnight New York on a CME symbol, most tools still put the week line at the Sunday 18:00 exchange open, leaving it stranded between two day lines. The "Follow Day Start" mode learns which weekday opens the exchange's week and places the week line on the day boundary that lands on it.

There are twelve independent timeframe filters, one per element, each with its own "Apply Below" cutoff. Week lines can appear on the 4-hour, previous-day levels down to the 12-hour, session boxes only at 15 minutes and below, and the 00:00 level only at 45 minutes and below — all in one saved profile. Comparable tools use a single global cutoff that hides everything at once.

Day names are centred on the day. In Auto mode the position comes from the session's own midpoint, so it stays correct on a half day and on a holiday that TradingView folds into the neighbouring session. Other modes measure the previous day's width in bars.

The script also warns you when your chart is empty. With twelve filters, that's the most likely failure mode, so a note appears bottom-right naming the cause.

## Settings and How to Tune Them

**General.** Timezone applies to the session times and the 00:00 and 10:00 levels, and handles daylight saving automatically; day and week lines read their own timing from the market. Show Warning Messages controls the amber notes in the bottom-right corner.

**Day and Week Vertical Lines.** A master enable and an "Apply Below" cutoff govern the section. Day Line and Week Line each have on/off, style, thickness and colour; where a week line is drawn, that moment's day line is omitted. Day Starts At selects among the five boundary modes above, with Custom Time and Custom Zone fields used only in Custom time mode. Week Starts offers Follow Day Start, Exchange Week, or Specific Day plus a weekday. Day Names toggles Off / Short / Full with text colour and a manual horizontal nudge. Draw As switches between Lines and a Background tint of the whole bar.

**Sessions.** A master enable and its own "Apply Below" cutoff. Asia, London, NY AM and NY PM each have on/off, session times as HHMM-HHMM, box colour, and the letter written inside. Default times, in New York time, are Asia 20:00-02:00, London 02:00-08:30, NY AM 08:30-11:30, NY PM 13:30-16:00, and all four are fully editable. Label Size controls text size and the opacity of the letter.

**Previous Highs & Lows.** A master enable, Extend Lines Right with a bar count, and separate rows for Previous Day, Week and Month — each with on/off, colour, and a count of previous periods to show (the script caps these at 50 each). Apply Below is configured per period type, giving three independent filters here. Line Style applies across the section, and Fade Older Lines makes older levels fainter so the newest stands out.

**Opening Levels.** A master enable, then rows for 00:00 AM, 10:00 AM, Daily, Weekly, Monthly, Yearly and All-Time High — each with on/off, colour, its own chart text, and its own "apply below" timeframe. Line Style applies across the section; Text Colour sets colour and size of all labels; Line Length controls how far past the last bar the lines and labels sit.

## How to Read It

The script's documentation is careful to frame the following as common ways context tools of this kind are read, not as recommendations or strategies.

**Trend and continuation.** The previous day's high and low, and the week's opening price, are the levels most often referenced when describing whether a market is extending or retracing. A market trading and holding above the prior day's high is described differently from one that reached it and fell back. The suggested setup is previous day and week levels on, sessions off, day and week lines on, on the 1-hour or 4-hour.

**Range and mean reversion.** The session boxes give you a visible container. When the London box and the NY AM box overlap heavily in price, the market has not gone anywhere, and the box edges are boundaries other participants can see too. The 00:00 open and the daily open are frequently used as the "middle" a rangebound day oscillates around. Suggested setup: all four sessions on, 00:00 and daily open on, previous-day levels on, on the 15-minute.

**Scalping.** Use the session boxes as a filter on *when* rather than a signal on *what*. The boundary between one session box ending and the next beginning is where participation changes hands. The documentation suggests turning the day and week vertical lines off at 1 to 5 minutes, since they add clutter without adding information. Suggested setup: sessions on, previous day on, everything else off, on the 1-, 2- or 5-minute.

**Swing.** Switch to the weekly and monthly side. Previous week and previous month highs and lows, plus the monthly and yearly opens and the all-time high, give you the small set of levels a multi-week position is measured against. Suggested setup: previous week and month on, weekly, monthly and yearly opens on, sessions off, on the 4-hour or daily.

**Multi-timeframe workflow.** Because every element has its own "Apply Below" cutoff, you can set the script up once so that scrolling from a daily chart down to a 1-minute chart progressively reveals more detail without touching a setting.

## Pros & Cons

**Pros:**
- Four modules in one indicator slot, with open-source calculations
- Five day-boundary modes and three week-boundary modes, including one that follows the day boundary
- Twelve independent timeframe filters rather than one global cutoff
- Day names centred on the day rather than pinned to a clock
- An all-time high level tracked incrementally, without a backward scan
- A warning banner that names why the chart is empty

**Cons:**
- No session high and low levels. The box is the whole record and it stops at the session end.
- No alerts of any kind. The documentation calls this the most requested missing feature and the most likely addition to a future version.
- Only two fixed clock levels, 00:00 and 10:00. They cannot be moved and a third cannot be added.
- Only four sessions, with no fifth slot.
- No standard deviation or range projection levels, and no session midpoints.
- No statistics table and no hit rates — deliberate, per the author, because a hit rate on a chart reads as a probability and it is not one.
- Capped history: previous-level counts are limited to 50 each, day and week separators to 250 with the oldest dropped, and very deep history is trimmed to roughly 10,000 bars.

## Known Behaviours Worth Knowing

These are documented as expected, not bugs. "Market open only" matches Auto on most symbols, because futures, forex and crypto have no pre-market to skip; to see it differ, use a US stock with Extended Hours enabled. The 00:00 and 10:00 levels never appear on stocks, since every stock is closed at midnight, and they can also be skipped when a timeframe's bar grid steps over the exact minute, as on 45-minute and 3-hour charts. Previous-period lines run back across the period they summarise on historical bars — intentional, and the line was invisible while that period was forming. The current period has no line until it ends. Lookahead is used for period detection and for reading settled values; nothing visible is derived from unsettled future data. Saturday and Sunday names appear only on crypto symbols. The first day on the chart gets no name. A large gap can swallow a day boundary entirely, and no line is drawn for that day. Background mode forces a fixed transparency regardless of your swatch. Non-time-based charts (Renko, Range, Kagi, Point and Figure, Line Break) cannot use the "Apply Below" filters reliably, and a note says so.

## Alerts

There are none built in. The documentation frames this as a scope decision: everything the script draws is context, and context is not an event. The practical workaround today is a manual TradingView price alert — read the price off the level via the Data Window (DH, DL, WH, WL, MH or ML), open the alert dialog, choose the symbol rather than the indicator as the condition, set it to Crossing, enter the price, and set the trigger to Only Once. That alert sits on the price, not on the script, so it will not move when the level moves and must be re-created each session.

## Alternatives

The closest well-known free alternative is ICT Killzones + Pivots, which covers the same broad ground: session boxes, previous day/week/month levels, opening prices and separators. It stores each session's high and low as forward-extending horizontal lines, supports alerts on session and period levels, allows eight or more configurable opening times with custom labels, offers five or six configurable session slots, can plot standard deviation and range projection levels, and shows a statistics table with hit rates and sample sizes. It also offers an unlimited history mode. On all of those points this script has no equivalent.

TradingView also ships a built-in "Session breaks" option in Chart Settings that draws vertical session dividers for free, without using an indicator slot. If separators are all you want, that is the cheaper route — this script is only worth a slot if you want two or more of its four modules.

## Final Verdict

This is a context layer, and it is honest about being one. It does not forecast, it does not signal, and it deliberately withholds the statistics that would make it look like it does. The day-boundary and week-boundary modes, the twelve independent filters, and the empty-chart warning banner are the parts that go beyond the closest free alternative. The absence of alerts, session high/low levels,

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

---
title: "Overnight Gap Fill Tracker Review — Trend Indicator"
date: 2026-10-05
draft: false
type: reviews
image: "/screenshots/overnight-gap-fill-tracker.png"
tags:
  - "overnight gap fill tracker"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Overnight Gap Fill Tracker review: a statistics tool that logs how often opening gaps get retraced, broken down by depth, weekday and gap size."
tv_script_url: "https://www.tradingview.com/script/9RvNUe5J-Overnight-Gap-Fill-Tracker/"
sources: ["https://www.tradingview.com/script/9RvNUe5J-Overnight-Gap-Fill-Tracker/"]
---
Most gap indicators draw a box and leave the interpretation to you. This one keeps score. Overnight Gap Fill Tracker measures how often the opening gap on a stock or ETF is retraced during the same regular session, then breaks the results down by retracement depth, weekday and gap size. The chart plotting is familiar; the statistics layer is the point.

## What it actually does

At the first regular-session bar (09:30 New York time), the script measures the gap as today's open minus the previous session's close, taken from the prior daily bar. Gaps below a user-set minimum are ignored. It then draws the gap zone, the prior close, and the 25%, 50% and 75% retracement levels, measured from the open back toward the prior close.

During the session, each bar's high and low are compared against those levels. The script records which were reached — 25%, 50%, 75% and a full fill back to the prior close. The opening bar counts. Each finished session goes into a log, and the table is calculated from that log, either across every gap on the chart or only the most recent N sessions if a lookback is set.

## The setup trap worth knowing about

The defaults are scaled for SPX-level prices. On SPY, QQQ or a typical stock, those defaults filter out almost every gap, and the table looks empty until you fix it. That's not a bug, but it will confuse anyone who installs and moves on.

Two ways out. Set "Gap measurement unit" to Percent — the percent defaults work across symbols and price levels. Or stay in Dollar mode and enter your own min gap, small gap max and large gap min. The bounce distance setting is always in price units even in Percent mode. Changing any setting recalculates everything from the bars on your chart.

## Inside the table

The core output is fill rates at 25/50/75/100%, split into all gaps, gap-up only and gap-down only, each shown with counts (hits/total). Then fill rates by weekday, separated by direction, and fill rates by gap size using small/medium/large buckets you define.

Optional rows cover bounce and continuation. Bounce means: after the 50% level is touched, price moves back in the original gap direction by at least a set distance within a set number of bars. Continuation is the share of 50% touches that go on to a full fill. There's also a TODAY row showing the current gap, its 50% target, fill status, and how often gaps on this weekday in the same direction have reached 50% historically.

Sections can be toggled and the direction columns hidden to shrink the table. A colorblind-safe palette is included.

## Pros and cons

**Pros:**
- The weekday and gap-size breakdowns are the useful part. "Do gaps fill?" is a weak question; "do large gap-downs on a given weekday fill to 50%?" is a testable one.
- Counts are shown alongside every rate, which is the honest way to present small samples.
- Percent-based buckets stay consistent as price drifts over years, and travel across symbols.
- No lookahead. Levels are fixed at the session's first bar using the previous daily close with a one-bar offset, and once a level is touched it stays touched, so historical results don't change on reload.
- Open code, so you can audit how each statistic is counted.

**Cons:**
- The out-of-the-box experience is poor on anything except SPX-scale instruments. You must read the setup notes.
- Continuous futures aren't supported — session boundaries and rolls distort what counts as an overnight gap.
- Non-standard chart types (Heikin Ashi, Renko) won't work, since their open/close values aren't real prices.
- With extended hours enabled the script may not detect the session open.
- The current, unfinished session is included, so today's numbers move until the close. On a regular-hours chart, the table won't refresh for a new day until the market opens.

## How to use it

Run an intraday chart — 5 or 15 minutes is the natural fit — with standard candles or bars, set to regular trading hours, on a symbol with one regular session per day: US stocks, ETFs, indices like SPX. Complete the symbol-appropriate setup first, then read the table as context, not as a signal.

## Who it's for

Discretionary intraday traders who already watch the open and want base rates for gap behaviour rather than another arrow on the chart. Also useful for anyone building a gap-fade or gap-continuation ruleset who needs to know how often the setup actually resolves. Less useful for futures traders and anyone trading extended hours.

## FAQ

**Does it give buy or sell signals?** No. It's a statistics tool for study. The table describes past behaviour of the bars loaded on your chart.

**Why is my table empty?** Almost certainly the default gap thresholds. Switch to Percent mode or enter symbol-appropriate dollar values.

**Can I trust a 100% fill rate?** Check the count next to it. Single weekdays and large gaps can have small samples. The table header shows the date range and session count.

**Does it repaint?** No. Levels are set at the session's first bar, and touched flags persist.

## Verdict

A genuinely useful statistics layer wrapped around a common plot, held back only by defaults that don't travel and a narrow list of supported instruments. If you trade US equities or indices intraday and care about base rates, the weekday-conditional TODAY row alone justifies the install.

**Rating: ⭐⭐⭐⭐ (4/5)**
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

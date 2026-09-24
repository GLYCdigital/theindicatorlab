---
title: "Ibd_Style_Relative_Volume_Stockbee_Ep9M Review: Settings, Strategy & How to Use It"
date: 2026-08-18
draft: false
type: reviews
image: "/screenshots/ibd-style-relative-volume-stockbee-ep9m.png"
tags:
  - "ibd style relative volume stockbee ep9m"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Ibd_Style_Relative_Volume_Stockbee_Ep9M review: settings, volume trend strategy, pros/cons, and who should use this TradingView indicator."
tv_script_url: "https://www.tradingview.com/script/hbScFl8K-IBD-Style-Relative-Volume-Stockbee-EP9M/"
sources: ["https://www.tradingview.com/script/hbScFl8K-IBD-Style-Relative-Volume-Stockbee-EP9M/"]
---
Let's be clear about what this is: the **RVOL + EP9M** study is not a black box. It is a volume-pane tool that does two jobs — pace relative volume honestly intraday, and tag Stockbee's EP9M institutional-participation signal directly on qualifying bars. It is not a signal generator, and it does not replace price context.

## What This Indicator Actually Does

Two things on one volume pane.

First, relative volume that stays honest intraday. The problem it solves is specific: almost every RVOL tool estimates the day's finishing volume by taking what has traded so far and dividing by the fraction of the session elapsed. At 10:00, thirty minutes into a 390-minute session, that fraction is 30/390 = 0.077, so the tool multiplies volume so far by roughly thirteen. That is a straight line — it assumes volume arrives at a constant rate from open to close.

It does not. The intraday volume profile is a U: heavy on the opening drive, thinning midday, heavy again into the close. By 10:00 a normal stock has already done far more than 7.7% of its day. Multiplying by thirteen projects a finishing volume the stock was never going to reach.

The error is systematic, and it changes sign through the session. Straight-line RVOL runs inflated in the first hour, roughly honest in the early afternoon, and deflated in the final thirty minutes — on every symbol, every day.

This script replaces the straight line with a measured curve. Instead of assuming elapsed_time / 390, it asks: on this specific symbol, what fraction of a typical session's volume has actually been done by this time of day? That fraction, U(t), is measured from the symbol's own recent history, and the live bar is divided by it. Same arithmetic, honest divisor.

Second, EP9M markers — Pradeep Bonde's (Stockbee) 9M breakout screen — tagged directly on the bars that qualify.

## Key Features That Stand Out

- **Time-of-day volume curve.** Built by reading each recent complete session's own intraday sub-bars, bucketing by time of day, and normalizing each bucket by that day's own total. Normalizing per day makes the measurement scale-free — a 30M-share day and a 3M-share day contribute equally to the shape, which is the only thing being measured. Averaged across the lookback, this yields the cumulative curve U(t). Because it is measured rather than assumed, the curve is symbol-specific. A mega-cap and a thin small cap have genuinely different profiles; small caps in particular are far more open-weighted.

- **Two readings, one curve.** RVOL (Mean) is measured against the arithmetic mean of the lookback window and is comparable with conventional RVOL tools. RVOL (Median) is measured against the median of the same window. Share volume is heavily right-skewed — a single earnings day, index add, or halt-and-reopen drags the mean up for the whole lookback and suppresses every mean-based reading inside it. The median ignores the spike. Read together: close together means the baseline is clean; a wide gap means the mean is contaminated and the median row is the honest one. The median cell turns amber automatically when the mean runs at 1.25x the median or higher.

- **EP9M markers.** A session qualifies when the close is at least 4% above the prior close, volume exceeds the prior session's, and volume is at least 9,000,000 shares. The inverse (down EP9M) flips only the price leg: 4% or more below the prior close, same volume conditions. Markers offer nine shapes, five sizes, independent up and down colors, and a vertical gap so they sit clear of the volume columns.

- **Pre-market volume handling.** Optional, on by default. On daily and weekly charts each bar's own pre-market volume is summed from extended-session sub-bars and added to the plotted column, both baselines, and the projection, so all three are measured on the same basis. Only the regular-session portion is paced; the pre-market block is already complete when the session opens and is added back as a static term.

- **Diagnostics.** Show Diagnostic Rows exposes every term feeding the calculation: pacing mode, curve versus linear percentage, sessions accumulated, both baselines, the mean-to-median skew, and the full volume decomposition.

## Settings and How to Tune Them

- **Average Volume Length** — baseline window, default 50. Setting it to 20 lines up with conventional 20-day RVOL.
- **Use Time-of-Day Volume Curve** — turning it off reverts to straight-line pacing, which is the quickest way to see the size of the correction.
- **Curve Lookback** — how many complete sessions feed the curve.
- **Marker Shape / Size / Gap / Colors** — full control over EP9M tags. Triangle and Arrow invert on a down day; the remaining shapes signal direction by color alone.
- **Show Diagnostic Rows** — exposes the pacing mode, curve versus linear percentage, sessions accumulated, both baselines, the mean-to-median skew, and the volume decomposition. During a live session, comparing the `pct linear (v1)` row against the `pct curve` row shows the gap directly; it is widest in the first hour.

Every EP9M threshold is adjustable.

## How to Actually Read It

The two readings are the core workflow. When mean and median sit close together, the baseline is clean and the headline is trustworthy. When they diverge, the mean is contaminated — typically by a single outsized session inside the lookback — and the median row is the one to trust. The amber cell flags that condition automatically.

The diagnostic rows do the verification work. Toggling the curve off and watching the headline RVOL jump to the straight-line value shows the size of the correction on your own chart. The raw-volume row alongside separately summed pre-market and regular-session totals lets you confirm on your own data feed whether TradingView's volume already includes pre-market for a given symbol. That matters more for the EP9M 9,000,000-share floor — an absolute threshold — than for RVOL, where numerator and denominator move together and the ratio barely shifts.

This is a confirmation and context tool. It measures participation; it does not generate entries.

## Pros & Cons

**Pros:**
- Corrects a systematic, sign-flipping bias that straight-line RVOL carries all day
- The curve is measured from the symbol's own history, not a hard-coded template
- Mean versus median gives an immediate read on whether the baseline is contaminated
- EP9M tagging is built in, with full control over marker appearance and thresholds
- Diagnostics expose every term, so the calculation is auditable on your own data

**Cons:**
- The curve corrects bias, not variance. In the opening minutes the divisor is very small and a single block trade dominates the projection — early readings are directionally useful, not precise
- The curve needs several complete sessions before it engages; until then the script falls back to straight-line pacing and reports that in the diagnostics
- Intraday timeframes pace linearly within the bar — the time-of-day curve is a within-session shape, so it applies to daily and above
- Mid-week exchange holidays are counted as trading days in weekly and monthly pacing (daily pacing is unaffected)
- Markers are drawn as labels and capped at 500 per chart; beyond that the oldest are dropped silently
- TradingView volume is split-adjusted, so results on names with splits can differ from a raw-share-count implementation of the same screen

## Who This Is For

Traders who already know what relative volume is supposed to measure and want the intraday number to stop lying to them. It suits anyone watching for sustained institutional accumulation — the EP9M logic is an absolute participation filter, and names printing several qualifying sessions within a month are under sustained accumulation. If you trade off a volume pane on daily or weekly charts and have been mentally discounting the morning RVOL print, this removes the need.

## FAQ

**Q: Why does the headline RVOL change so much when I toggle the curve off?**
A: That gap is the straight-line error. The curve divisor reflects the symbol's actual time-of-day profile; the linear divisor assumes constant pacing. The difference is widest in the first hour.

**Q: Which reading should I trust — mean or median?**
A: Read them together. Close together means the baseline is clean. A wide gap means the mean is contaminated by an outsized session in the lookback, and the median row is the honest one. The amber cell flags when the mean runs at 1.25x the median or higher.

**Q: Does it handle pre-market volume?**
A: Yes, optionally and on by default on daily and weekly charts. Pre-market volume is summed from extended-session sub-bars and added as a static term to the plotted column, both baselines, and the projection. A diagnostic row lets you verify on your own feed whether TradingView already includes pre-market for a given symbol.

**Q: Can I use it intraday?**
A: The time-of-day curve is a within-session shape, so it applies to daily and above. Intraday timeframes pace linearly within the bar.

**Q: Why is the curve slow to start on a new symbol?**
A: It needs several complete sessions before it engages. Until then the script falls back to straight-line pacing and says so in the diagnostics.

## Final Verdict

RVOL + EP9M does one thing well and is honest about its edges. The time-of-day curve fixes a real, systematic bias that every straight-line RVOL tool carries, and the mean-versus-median pair gives a built-in check on whether the baseline can be trusted. The diagnostics make the whole calculation auditable rather than a black box.

The limitations are stated plainly and are worth taking at face value: early-session readings are directional, not precise; the curve needs history before it engages; the tool paces within-session shape on daily and above. This is a confirmation tool, not a signal generator. Used as one, it earns its place on the pane.

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

---
title: "Multi Timeframe Fvgs Ufo Review — Market Structure Indicator"
date: 2026-10-14
draft: false
type: reviews
image: "/screenshots/multi-timeframe-fvgs-ufo.png"
tags:
  - "multi timeframe fvgs ufo"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Multi Timeframe Fvgs Ufo review: tracks Fair Value Gaps from up to six timeframes with fill %, touches, invalidation and alerts. Honest 4-star verdict."
tv_script_url: "https://www.tradingview.com/script/F6oUQzkH-Multi-Timeframe-FVGs-ufo/"
sources: ["https://www.tradingview.com/script/F6oUQzkH-Multi-Timeframe-FVGs-ufo/"]
---
Most multi-timeframe FVG tools do one of two things badly: they either flood your chart with boxes you can't read, or they show you gaps and then forget they exist. Multi Timeframe Fvgs Ufo tries to solve both problems at once — it pulls Fair Value Gaps from up to six timeframes onto a single chart, then keeps tracking each gap after it forms. Whether it succeeds depends on how much you value post-formation data.

## What it actually does

An FVG, as the script defines it, is a three-candle pattern where the middle candle moves fast enough that the wicks of candle one and candle three don't overlap. That untouched range is the gap. This indicator surfaces those gaps across multiple timeframes — higher *and* lower than your chart — and then follows them.

The tracking layer is the interesting part. Once a gap exists, the script watches whether price taps it (a wick trades in), how deep price has travelled (fill %), how many separate entries occurred (touches), and whether price reached the midpoint — the EQ, or 50% level. You decide how much of that gets displayed.

## The detection logic matters

For timeframes equal to or higher than your chart, detection uses the last three *completed* candles of that timeframe. That means a confirmed FVG appears only after candle three closes, and confirmed gaps don't repaint. This is a meaningful distinction — plenty of FVG scripts draw the gap on candle two and then quietly move it.

Lower timeframes work differently. With "Show TFs Below Chart TF" enabled, the script reads the candles of that lower timeframe *inside* each chart candle, so a 15-minute FVG on a 1-hour chart is found on the real 15-minute candles — not approximated from the hourly bar. It also excludes price gaps where no trading occurred between two candles, like an opening gap.

## Keeping the chart readable

The clutter controls are where this script earns its keep. Each timeframe gets its own lookback — last X FVGs, X hours, X days, or the X nearest above and below price. You can hide nested FVGs (a gap sitting inside a same-direction gap from a higher timeframe), filter by minimum size in ticks or % ATR, restrict to a session window, or filter by direction.

Then there's display: extended FVGs are placed in a column per timeframe to the right of price, so timeframes don't stack on top of each other. You can switch between Box, Line, or Bracket. "Extend nearest" keeps only the closest gaps extended. The script stays under TradingView's 500-object limit, which sounds like a footnote until you've had a drawing vanish mid-session.

## Fill tracking and hover

Fill Display offers two modes: boxes shrink as price fills them, or the filled portion appears in a second colour. Labels can carry fill %, touch count, or both, plus the time the FVG formed. Hovering over a label reveals the full picture — formation time, levels, size, fill %, touches.

Invalidation is configurable: Wick fill, Body fill, Wick fill EQ, Body fill EQ, or None. Body rules use the bodies of the FVG's own timeframe, not your chart's. Invalidated gaps can be removed or kept in their own colours.

Alerts cover three events — New FVG, Tapped, and EQ tapped — each sent once per FVG, filterable by direction and timeframe. You create them with the condition "FVGs [ufo]" and "Any alert() function call".

## Limitations worth knowing

Touches are counted per chart candle for timeframes at or above your chart. Leave and re-enter an FVG within one candle and it registers as one touch. A lower chart timeframe counts more precisely.

Lower-timeframe FVGs start at the chart candle containing them, and TradingView caps how much lower-timeframe data a script can load — so 1-minute FVGs on a daily chart only reach back so far. Potential FVGs (dashed, marked with an asterisk) repaint by design: they update live and vanish if the gap closes before candle three finishes. They carry no alerts or tracking. Hours/Days lookback counts chart bars, capped at 5,000 bars back, and up to 200 FVGs are stored per timeframe.

## Pros and cons

**Pros:** genuine lower-timeframe detection from real candles; confirmed gaps don't repaint; deep fill and touch tracking; strong clutter controls including per-timeframe columns and nested filtering; hover details save you clicking through settings.

**Cons:** potential FVGs repaint with no tracking; touch counting is coarse on higher timeframes; lower-timeframe history is limited by platform data caps; it's an analysis tool with no signals — you still have to decide what a gap means.

## Who it's for

Discretionary traders who already use FVGs and want situational awareness across timeframes without six separate charts. If you trade intraday and care about whether a higher-timeframe gap has been respected or eaten, this is built for you. If you want buy/sell arrows, look elsewhere — the script states plainly it doesn't provide signals or predict reactions.

## Verdict

A well-considered FVG tracker with unusually good clutter management and honest documentation of its own limits. The repainting potential FVGs and coarse touch counting keep it from a perfect score, but for multi-timeframe gap analysis it's a solid, transparent tool.

**Rating: ⭐⭐⭐⭐ (4/5)**

## Frequently Asked Questions

### Is Multi Timeframe Fvgs Ufo worth it?

That depends on your workflow — the sections above cover what it does and where it fits. Check the official TradingView page for the current feature set and author notes before you decide.

### Does this indicator repaint?

Check the author's own description on TradingView — repainting behaviour is script-specific and we won't assert it for you here.
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

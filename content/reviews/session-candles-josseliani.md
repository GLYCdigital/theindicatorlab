---
title: "Session Candles Josseliani Review — Trend Indicator"
date: 2026-11-16T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/session-candles-josseliani.png"
tags:
  - "session candles josseliani"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Session Candles [josseliani] turns each trading session into a single candle on a mini-chart. Honest review of its features, signals and limits."
tv_script_url: "https://www.tradingview.com/script/fWsmAzYa-Session-Candles-josseliani/"
sources: ["https://www.tradingview.com/script/fWsmAzYa-Session-Candles-josseliani/"]
---
Most session tools just shade the background. Session Candles [josseliani] takes a different angle: it compresses each trading session into a single candle on a mini-chart that sits directly on your main chart. The idea is simple and useful — instead of squinting at intraday noise, you read the day the way you'd read a daily chart, with each session as one Open-High-Low-Close body.

The point isn't decoration. It's structure. Where did the range expand? Did a session take out the previous high or low and hold beyond it, or did it sweep and snap back? That's the kind of question this indicator is built to make visual.

## What it actually does

The core feature is that the session candles are built from **your chosen time windows**, not a fixed chart timeframe. The default schedule splits the day into three periods in New York time: Asia (18:00–02:00), London (02:00–08:00) and New York (08:00–18:00). You can swap in sequential sessions, equal eight-hour blocks, or custom intervals — and windows can overlap or leave gaps.

The mini-chart plots O/H/L/C on a shared price scale, with day separators, session labels and a live candle that updates as new data arrives. A short light line on each candle marks the 50% midpoint of its range, and grey guides beside the latest candle show the previous session's high, low and midpoint. A Weekly Open reference runs across the candles belonging to each trading week.

Two markers do the interpretive heavy lifting:

- **Blue — BREAK:** price traded beyond the previous session's high or low, and closed beyond it.
- **Yellow — SWEEP:** price traded beyond that level but closed back at it or inside the range.

Highs and lows are evaluated separately, and markers on the live candle are provisional until the session closes.

## The main-chart layer

Beyond the mini-chart, the indicator adds a session VWAP (with the completed session's final VWAP optionally frozen as a grey reference for 60 minutes), previous-session high and low labels, and Weekly Open plus optional Daily, H1 and H4 opens. There are confirmed pivot dots, Break of Structure levels, configurable Kill Zone boxes — including an optional third window — and session BUY/SELL signals.

The signal logic is worth understanding before you switch it on. A BUY needs a confirmed structure break with both the broken pivot and the closing price above VWAP; a SELL is the mirror. An optional EMA filter (default length 21) adds a condition. Signals are confirmed on the bar's close, with alerts for BUY, SELL or either.

There's a specific rule you should read carefully: once price moves **1 ATR** in favour of a signal, the search stops until the next session. Up to three attempts are allowed per session, and if an attempt doesn't follow through, the indicator permits another qualifying signal in the opposite direction. The author is explicit that this is an ATR distance, not a 1R profit target — the indicator does not calculate stop-loss risk. That's an honest caveat, and it matters.

## How to use it

Treat the mini-chart like a candlestick chart. Look for the documented pattern ideas — Power of Three relative to Weekly Open, fair value gaps between session candles, engulfing and reversal combinations, higher highs and lower lows. The author is clear that the indicator *doesn't* auto-identify these patterns; you read them yourself. The BREAK and SWEEP markers just tell you what happened at the prior session's extremes.

Then use the main-chart layer for context: VWAP for the session's direction, Kill Zone boxes to frame the hours you care about, and the structure signals if you want a rules-based prompt. Note that the boxes are visual references only — they don't filter signals.

## Pros and cons

**Pros**
- Genuinely novel framing — session-as-candle is a clean way to read multi-session structure.
- Flexible windows: presets, custom intervals, overlaps and gaps all supported.
- BREAK vs SWEEP distinction is precise and evaluated per side.
- Signals have documented, transparent logic rather than a black box.
- Mobile view option trims the mini-chart by 25% for smaller screens.

**Cons**
- Timeframe sensitivity is real. The ATR distance and structure confirmation both shift with the chart timeframe, so signal behaviour changes between, say, a one-minute and five-minute chart. The author documents this openly, but it means results aren't portable.
- Confirmed pivots need four bars to the right, so signal logic waits for confirmation.
- VWAP needs usable volume data, and daily/weekly opens follow the session calendar rather than standard candle opens — a subtlety that can confuse.
- Overlapping windows share price data, which muddies candle combinations.
- Intended for intraday charts of 60 minutes or less only.

## Who it's for

Intraday traders who already think in sessions — forex, index and gold traders especially — and anyone who wants to analyse the day's structure without leaving their execution chart. It's less suited to swing traders or anyone working above the 60-minute timeframe, where the tool's assumptions don't hold.

One more note: for recognised gold symbols, signals are blocked from 18:00 to 19:00 New York time.

## FAQ

**Does it draw the patterns for me?** No. It shows the candles and markers; reading patterns is your job.

**Can I change the session times?** Yes — presets, custom windows and a schedule timezone are all configurable.

**Do Kill Zone boxes filter signals?** No, they're visual references only.

**Is the 1 ATR move a profit target?** No. It's a distance that stops the search for new signals — not a risk calculation.

## Verdict

Session Candles [josseliani] earns its place because it solves a real problem — reading multi-session structure without leaving the main chart — and it does so with transparent rules and honest caveats. The timeframe sensitivity and pattern-reading burden keep it short of five stars, but for intraday traders who already work session-to-session, it's a thoughtful, well-documented tool.

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

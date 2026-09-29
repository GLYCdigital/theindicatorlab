---
title: "Primitive Charts Session Candles Review — Trend Indicator"
date: 2026-09-30
draft: false
type: reviews
image: "/screenshots/primitive-charts-session-candles.png"
tags:
  - "primitive charts session candles"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Primitive Charts Session Candles condenses each trading session into a single candle beside your chart. Honest review of features, limits and fit."
tv_script_url: "https://www.tradingview.com/script/NYvqvVk1-Primitive-Charts-Session-Candles/"
sources: ["https://www.tradingview.com/script/NYvqvVk1-Primitive-Charts-Session-Candles/"]
---
Most session tools give you boxes drawn over price. This one takes a different route: each trading window becomes its own candle, plotted to the right of your chart and priced on the instrument's own scale. You read a session the way you read a bar — open, high, low, close — without squinting at shaded ranges or counting bars.

## What it actually does

Primitive Charts Session Candles summarises selected time windows as individual candles. Each candle starts at its session's opening time, develops as price arrives, and freezes when the session ends. The body spans open to close; the wicks mark the session's extremes. While a session is still forming, the latest observed price stands in as its close. Default colours are white for up candles and black for down.

Six windows ship with it, all on New York time and following daylight-saving shifts regardless of your chart's timezone:

- Asian: 20:00–00:00
- London: 02:00–05:00
- Premarket: 05:00–09:30
- Opening Range: 09:30–10:00
- Initial Balance: 09:30–10:30
- New York: 09:30–16:00

Every session calculates independently, so overlapping windows — Opening Range, Initial Balance and New York all share a start — develop side by side rather than fighting for the same space. That's the core appeal: you can watch London's range and closing position, compare the Opening Range against the Initial Balance, and follow New York as its candle builds, all in one glance.

## Configuration worth knowing

Enable only the sessions you want. Each slot has an editable name and time window, including overnight windows, and you can paste a pcr-1 roster code to load session definitions before overriding names or times separately.

The display holds up to one candle per enabled session and follows the current trading day by default, with an 18:00 New York reset grouping the prior evening's Asian session with the following London and New York sessions. Completed candles clear at that reset; a custom session crossing 18:00 stays visible through its own window. "Show candles from the previous day" keeps each session's most recent candle until its next occurrence replaces it in the same slot.

"Trace Candle Open" draws a connection from a forming candle's open back to the chart bar containing its session start. When nothing visible is forming, the trace follows the most recently completed visible candle with complete data — a useful reference tying the summary back to the underlying chart.

Display controls cover minimum and maximum chart timeframes (1 minute and 4 hours by default), distance from the chart, spacing between sessions, candle width, and shared up/down colours for bodies, borders and wicks. Names, times and dates are optional labels with their own size, colour and position settings; names are on by default, times and dates off. Hovering a label reveals OHLC, session status and source timestamps.

## Practical constraints

Use standard time-based charts from 1 minute to 4 hours, with the required session hours included, and leave room to the right of the chart. Session prices are measured from one-minute data across that range.

History depends on your symbol, feed and TradingView plan. Missing session minutes or boundaries trigger an "Incomplete" label and the candle is withheld. Custom windows spanning a market closure can also be marked incomplete. Open traces are omitted when their starting bar is more than 4,999 chart bars back.

## Pros and Cons

**Pros**
- Session OHLC on the price scale is genuinely easier to read than shaded ranges.
- Six pre-built windows cover the sessions most intraday traders care about.
- Overlapping sessions calculate independently, so Opening Range, Initial Balance and New York coexist.
- Editable names and windows, plus pcr-1 roster import, make custom session sets practical.
- Timezone handling is fixed to New York with DST — one less thing to misconfigure.

**Cons**
- It's a summary layer, not a signal generator. No alerts, no entries, no trend logic despite the category label.
- The 18:00 reset and previous-day logic take a session or two to internalise.
- Incomplete sessions get withheld entirely, so thin data leaves gaps.
- Requires dedicated right-side space and a time-based chart within the timeframe bounds.

## Who it's for

Intraday traders who think in sessions — particularly index futures and forex traders watching London, the Opening Range and New York. If you already mark session ranges manually, this replaces that routine with something cleaner. If you want buy and sell signals, look elsewhere.

## FAQ

**Does it work on any timeframe?**
It's built for standard time-based charts from 1 minute to 4 hours, and the min/max timeframe settings control visibility.

**Can I use my own session times?**
Yes. Each slot's name and window are editable, and you can load definitions via a pcr-1 roster code.

**Why is a candle missing or labelled Incomplete?**
Missing session minutes or boundaries, or a custom window spanning a market closure, will mark the session incomplete and withhold the candle.

**Does it repaint?**
Forming candles update as price arrives by design; completed candles freeze at session close.

## Verdict

A focused, well-considered session visualiser. It doesn't pretend to predict anything — it organises the trading day into comparable candles and gets out of the way. The 18:00 reset logic and incomplete-data handling are honest rather than hidden, and the pcr-1 import shows this was built by someone who actually uses session frameworks. Loses a star for being purely descriptive and for the space and data requirements.

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

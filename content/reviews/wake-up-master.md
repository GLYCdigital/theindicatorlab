---
title: "Wake Up Master Review — Trend Indicator"
date: 2026-11-13T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/wake-up-master.png"
tags:
  - "wake up master"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Wake Up Master review: a liquidity map for TradingView that plots session levels, live sweeps, FVGs, order blocks and manipulation legs on one chart."
tv_script_url: "https://www.tradingview.com/script/aAwGMHEF-Wake-Up-Master/"
sources: ["https://www.tradingview.com/script/aAwGMHEF-Wake-Up-Master/"]
---
Wake Up Master is a liquidity-mapping tool, not a signal generator. Its own description is blunt about that: "Use it as a map, not a signal." What it does is take the pre-session checklist many intraday traders run by hand — where are the highs and lows that matter, which ones have already been taken, where are the gaps and order blocks sitting — and draw it on one chart, updated live.

That framing matters. If you're looking for a trend indicator that tells you when to go long, this isn't it, despite the catalog filing. It's a structural overlay.

## What it actually draws

The core of the tool is liquidity levels. It marks previous week, previous day, previous 4-hour and previous 1-hour highs and lows, plus unswept daily highs/lows (two per side) and unswept weekly highs/lows (one per side) that price hasn't traded through. On top of that it adds the Asian session high/low (00:00–07:00 UTC) and the current session's high/low.

The sensible detail here is the merging. Levels that sit within a small tolerance of each other collapse into a single ray with a combined label — the description gives the example "4 hr high / London high." Anyone who has stacked manual levels knows how fast a chart turns into spaghetti, so this is a real quality-of-life choice rather than a marketing bullet.

## Sweeps are the interesting part

A level counts as swept the moment a wick trades through it — no waiting for a higher-timeframe candle to close. The level turns dotted, gets tagged "SWEPT hh:mm" with the time, and is removed 60 candles later.

This is a deliberate trade-off. Live sweeps mean the label can appear mid-candle, which is exactly when you want to know a level has been raided. The cost is that a wick through a level registers as a sweep even if price immediately snaps back. The script is honest about the design: "Sweeps are live by design," while FVGs, order blocks and legs are confirmed on closed candles only.

One practical gotcha the description flags directly: sweep times use the "Time zone for sweep times" setting, and Pine can't read your chart's own time zone. You have to set it to match the zone shown at the bottom right of your chart, or the timestamps will be wrong.

## Gaps, order blocks and manipulation legs

Fair value gaps are tracked on two timeframes — 15m and 5m on most charts, 3m and 1m on a 1m or 3m chart, and the chart's own timeframe above 15m. A gap is removed once a candle closes through it. Inverse FVGs flip a gap into support or resistance when price closes through its far edge, and are removed when price closes back through.

Order blocks are the nearest fresh ones per side, built from closed candles only. Manipulation legs are the most specific construct: a move of up to four candles that sweeps the previous swing and then closes beyond the nearest opposite swing formed before the sweep, with swing strength defaulting to two candles each side. Each leg is boxed with projected extension zones at 1.9× the leg's range beyond it, and there's an optional filter to show only legs whose zones price actually reached before the next leg formed.

## How you'd actually use it

The documented workflow is straightforward: watch for price to sweep a level (the label flips to "SWEPT"), then look for a reaction at a nearby FVG, IFVG, order block or leg zone. It's a confluence process — sweep plus reaction area — rather than a single trigger.

The description says it was built for gold on 1m–15m charts, where session levels and sweeps matter most, but claims it works on any symbol and timeframe. Every element has its own on/off switch, colour and font size, so you can strip it down to just the levels you care about. That configurability is what keeps a tool this dense usable.

## Pros and cons

**Pros**
- Genuinely consolidated: session levels, unswept highs/lows, sweeps, FVGs, IFVGs, order blocks and legs in one place.
- Sweeps register on the wick, live, with a timestamp — useful for intraday execution.
- Level merging keeps the chart readable.
- Confirmed drawings don't repaint; the author is explicit about what is and isn't confirmed.
- Fully toggleable, so you can reduce clutter.

**Cons**
- It's a map, not a system. No entries, no exits, no bias — you supply the decision-making.
- The time zone setting is a manual step that will silently produce wrong timestamps if you ignore it.
- TradingView caps an indicator at 500 lines, labels and boxes, so only the nearest levels are retained. On a busy chart you may lose context.
- Live sweeps can flag a level that price immediately rejects — by design, but worth knowing.

## Who it's for

Intraday discretionary traders — particularly gold and index scalpers on lower timeframes — who already think in terms of liquidity sweeps, fair value gaps and order blocks and are tired of drawing levels by hand each session. If you trade daily or weekly swing setups, or you want a mechanical signal, this will frustrate you.

## FAQ

**Does it give buy or sell signals?** No. The description states plainly that it does not give signals and is not financial advice.

**Does it repaint?** Confirmed FVGs, order blocks and legs are closed-candle only and don't repaint once confirmed. Sweeps are live by design.

**Why are my sweep times wrong?** Pine can't read the chart's time zone. Set the "Time zone for sweep times" option to match the zone at the bottom right of your chart.

**Why did some levels disappear?** TradingView limits an indicator to 500 lines, labels and boxes, so only the nearest levels are kept.

## Verdict

Wake Up Master does one job well: it puts the liquidity picture on a single chart and keeps it current. The sweep logic and level merging show someone who actually uses this kind of tool, and the documentation is unusually candid about limitations. It loses a star because it's a component, not a complete approach — you still need your own read on entries and risk. ⭐⭐⭐⭐
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

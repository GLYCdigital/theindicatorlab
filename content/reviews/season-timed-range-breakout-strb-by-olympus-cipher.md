---
title: "Season Timed Range Breakout Strb By Olympus Cipher Review"
date: 2026-11-06T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/season-timed-range-breakout-strb-by-olympus-cipher.png"
tags:
  - "season timed range breakout strb by olympus cipher"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "STRB by Olympus Cipher is a session-timed range breakout tool with built-in breakout, failure and retest stats. Honest review of what it does."
tv_script_url: "https://www.tradingview.com/script/kmhbdWoO-Season-Timed-Range-Breakout-STRB-by-Olympus-Cipher/"
sources: ["https://www.tradingview.com/script/kmhbdWoO-Season-Timed-Range-Breakout-STRB-by-Olympus-Cipher/"]
---
Most opening-range indicators stop at drawing a box. This one keeps score. STRB — Season Timed Range Breakout, by Olympus Cipher — builds a range inside a time window you specify, projects levels from it, flags breakouts, and then tallies how those same breakouts behaved across the history loaded on your chart. Setup on one side, feedback on the other.

That combination is the whole pitch, and it's a good one. Whether it holds up depends on how much you want from a free, open-source script.

## What it actually does

You give the indicator a session window as a string — the description's example is `0930-0945`, with the end exclusive — or you tell it to use the first N candles of the trading session instead. A candle joins the range if its open time falls inside the window. The range itself is just the highest high and lowest low of those candles.

From there it projects up to three targets per side as multiples of the range size, plus a stop-loss reference for longs and shorts. The stop can be a multiple of the range or a percentage of the entry level. Levels can extend to the end of the trading session, stop at the breakout candle, or not extend at all.

The statistics table is the part worth paying attention to. It reports how breakouts have played out with your current settings, using only the history loaded on your chart.

## Multi-window mode

Turn it on and up to three independent windows run simultaneously — the defaults are New York, London and Asia. Each has its own range, trading session, levels, signals, tracked breakout and statistics. The table gains an "All" column that combines them.

This is the feature that separates STRB from the pile of single-session range scripts. If you trade more than one session, you don't need three copies of the indicator fighting for chart space.

## How breakouts, failures and retests are handled

Breakouts are evaluated on closed candles only, so the signals don't repaint. That's stated plainly in the description and it's the right design choice.

You choose whether the candle close or the wick must clear the range, and you can add a buffer in ticks. Signals can be limited to the first breakout of a session or allowed once per side. When a breakout fires, the box gets tinted and the opposite side's targets and stop are removed — only the relevant side stays on the chart. Small thing, but it keeps the chart readable.

Then there's the tracking layer. A **failure** is marked with an X when a later candle closes back beyond the entry level. A **retest** gets a diamond when a candle touches the broken level and closes back on the breakout side. Only the first retest after a breakout is marked, and no retest is counted after a failure. All of this has to be switched on in settings.

## The optional filters

Three filters are available, all off by default:

- **ATR filter** — compares range size against the previous completed daily ATR, so only ranges that are neither Narrow nor Wide (thresholds you set) are traded.
- **Relative volume filter** — the breakout candle's volume must exceed a multiple of its recent average.
- **VWAP filter** — longs must close above VWAP, shorts below it.

A breakout that fails a filter is ignored and doesn't consume the session's signal. That last detail matters more than it looks: it means a filtered-out breakout doesn't silently burn your one shot for the day.

## Pros and cons

**Pros**
- Breakout signals on closed candles only — no repainting.
- The built-in statistics table turns a drawing tool into something you can actually evaluate.
- Multi-window mode covers three sessions without stacking indicators.
- Filters are off by default and clearly documented, so you can start with the raw behaviour and layer conditions on one at a time.
- Open-source under MPL 2.0 — you can read the code.

**Cons**
- Intraday only.
- Statistics are limited to the history your TradingView plan loads, so the table's usefulness scales with your subscription.
- The stats track only the first breakout of each session, assume entry at the range level, and ignore commissions, slippage and position sizing. Treat them as a behavioural sketch, not a backtest.
- Targets and stop lines are visual references, not recommendations — the author is explicit about this.
- Default windows assume New York time, so anyone trading other markets has to reconfigure before the tool means anything.

## Who it's for

Discretionary intraday traders who already work with opening ranges or session breakouts and want a consistent way to draw them, plus a rough read on how the setup has behaved. It suits people who trade one or two sessions and want to compare them side by side. It is not for swing traders, and not for anyone looking for a signal service — the indicator shows you a structure, not an edge.

## FAQ

**Does it repaint?**
No. Breakouts are evaluated on closed candles only.

**Can I use it on a daily chart?**
No. It's intraday only.

**Are the statistics a backtest?**
No. They cover only the history loaded on your chart, assume entry at the range level, track only the first breakout per session, and ignore costs and sizing.

**Do the filters apply by default?**
No. All filters are off by default.

**How do I set up alerts?**
Choose one of the STRB alert conditions and set it to "Once Per Bar Close".

## Verdict

STRB does two jobs — drawing timed ranges and measuring how breakouts from them resolved — and does both without pretending the second is a backtest. The closed-candle evaluation, the multi-window mode and the sensible filter defaults show someone thought about how traders actually use these tools. The intraday-only limitation and the plan-dependent statistics keep it short of exceptional, but for a free open-source script it's a solid, honest piece of work.

⭐⭐⭐⭐
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

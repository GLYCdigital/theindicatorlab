---
title: "Turtle Soup Failed Breakout Review — Trend Indicator"
date: 2026-10-02
draft: false
type: reviews
image: "/screenshots/turtle-soup-failed-breakout.png"
tags:
  - "turtle soup failed breakout"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Turtle Soup Failed Breakout review: a rule-based failed-breakout indicator with ATR stops, R-multiple targets, filters and webhook alerts. 4 stars."
sources: ["https://www.tradingview.com/script/LME1uK6a-Turtle-Soup-Failed-Breakout-MarkitTick/"]
---
Most breakout tools assume the breakout is the trade. This one assumes the opposite — that the interesting moment is when the breakout fails. Turtle Soup Failed Breakout scans a rolling price channel for pushes beyond a prior extreme that can't hold, then draws a complete trade plan on the chart for each confirmed signal. It's a specific, opinionated tool, and it's worth understanding exactly what it does before you install it.

## What it actually detects

The engine is simple to describe. On every bar it takes the highest high and lowest low of the previous *Channel Len* bars (20 by default), excluding the current bar so the comparison is always against a range that was already complete. It then watches for price to pierce one of those edges and close back inside.

Two variants are available:

- **Turtle Soup** — the same-bar failure. Price trades below the channel low but closes back above it (for a long).
- **Turtle Soup +1** — the next-bar failure. The previous bar closed *outside* the channel, and the current bar closes back inside. This catches breakouts that looked accepted for one bar before being rejected.

The key filter is an age requirement. The prior extreme must be at least *Min Extreme Age* bars old (4 by default). A break of a high made two bars ago is noise; a break of a level that's been sitting there for a while is a genuine test of a level other traders are watching.

## The trade plan is the real feature

Plenty of indicators fire an arrow and leave the rest to you. This one draws the whole plan: entry at the confirmed close, a stop placed beyond the failed extreme by an ATR buffer (0.25 ATR over 14 bars by default), and three targets at 1R, 2R and 3R. Because the stop is volatility-scaled rather than a fixed distance, the invalidation point sits just past the price that actually kills the failed-breakout idea.

Tracking is conservative and clear. The stop is checked before targets each bar, so an ambiguous bar that touches both counts as a stop. The stop does not move after TP1 or TP2 — trailing or breakeven management is your call, not the script's. Labels flip to HIT with the percentage move when a level is reached, and the dashboard carries a ten-block progress bar for targets hit.

## Filters, alerts and what to watch for

Two optional filters are included. The higher-timeframe filter requires the last completed HTF close to be on the correct side of an EMA (50 periods on the 240-minute by default) — and it only reads closed HTF values, so it doesn't repaint. The ADX filter requires the previous bar's ADX to be at or above a threshold (20 by default). Both are context, not decoration: one asks whether the reversal agrees with the bigger trend, the other whether there's enough directional energy for a reversal to travel.

Webhook support is genuinely thought through. A confirmed signal sends structured JSON with action, ticker, timeframe, direction, entry, stop, three targets and the failed channel level. Each target fires its own message on touch, while entry alerts wait for the bar close. The action strings are configurable so they match your receiving system. One gap worth noting: there is no stop-loss alert.

On repainting — signals are final only at bar close, and a printed signal is not removed or moved. The dashboard and target tracking update live on the forming bar, which is normal real-time behaviour, not repainting.

## Pros and cons

**Pros:**
- Clear, mechanical rules — no eyeballing of range edges
- Two pattern variants in one tool, runnable separately or together
- Complete trade plan with volatility-scaled stops and R-multiple targets
- HTF and ADX filters that read only completed data
- Well-structured webhook JSON for automation
- Honest limitations section in the author's own documentation

**Cons:**
- Counter-trend by design: in strong trends, new extremes keep extending and this will produce a run of stops
- The stop-first rule and the fixed stop after TP1 are deliberate simplifications you may disagree with
- No stop-loss alert, which is an odd omission for a webhook-driven tool
- Results depend heavily on symbol, timeframe and settings — there is no "best market" here

## Who it's for

Discretionary traders who already watch range edges and want a rule-based trigger will get the most from this. It also suits systematic traders who want a ready-made failed-breakout signal with a defined trade plan and JSON output they can pipe into an execution system. It is not for trend followers, and it's not for anyone who wants the indicator to manage the trade after entry — it won't trail your stop.

## FAQ

**Does it repaint?** No. Signals are final at bar close, and the channel is built from completed bars only.

**Can I run both variants at once?** Yes — the Setup input offers Turtle Soup, Turtle Soup +1, or Both.

**What happens if a new signal appears while a trade is open?** The new signal replaces the current plan, open or not.

**Does the stop move after TP1?** No. It stays at its original price.

**Which timeframe works best?** The source material doesn't say, and neither will I.

## Verdict

This is a well-built, honestly documented implementation of a published concept — Connors and Raschke's Turtle Soup from *Street Smarts*, adapted to wait for a confirmed close rather than entering intrabar. The channel-plus-age logic is sound, the trade plan is complete, and the filters and alerts are implemented with care. What holds it back from five stars is the nature of the pattern itself: failed breakouts are one reading of price at a range edge, not a forecast, and the tool's own documentation is upfront that counter-trend setups can produce a series of stops in trending conditions. If you trade range edges and want the rules handled for you, this earns its place on your chart.

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

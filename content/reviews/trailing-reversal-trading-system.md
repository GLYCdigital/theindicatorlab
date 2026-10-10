---
title: "Trailing Reversal Trading System Review — Trend Indicator"
date: 2026-10-11
draft: false
type: reviews
image: "/screenshots/trailing-reversal-trading-system.png"
tags:
  - "trailing reversal trading system"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Trailing Reversal Trading System review: a Colby percentage-swing rule built into a full trade workflow with ATR stops, R-multiple targets and a live reversal level."
tv_script_url: "https://www.tradingview.com/script/qf0pCWVj-Trailing-Reversal-Trading-System-MarkitTick/"
sources: ["https://www.tradingview.com/script/qf0pCWVj-Trailing-Reversal-Trading-System-MarkitTick/"]
---
The Trailing Reversal Trading System takes a single sentence from Robert W. Colby's *Encyclopedia of Technical Market Indicators* and turns it into an actual trade workflow. The sentence is simple: go long when price rises a set percentage from a recent pivot low, go short when it falls the same percentage from a recent pivot high. Colby's version stops there. This script builds the rest — swing tracking, a live reversal level, volatility-based risk, three targets, and a dashboard that narrates the whole trade.

That gap between a rule and a tool is the real subject of this review.

## What it actually does

The engine tracks one swing at a time, bar by bar. In an up swing, every new higher high becomes the reference point; the swing survives until price falls the reversal percentage below that high. In a down swing, the mirror applies. When the swing flips, the pivot it reversed from gets stored, and that pivot becomes the anchor for the stop on the next trade.

What makes this more than a repackaged idea is the Reversal Level: a step line drawn in advance showing the exact price that would end the current swing. During an up swing it trails upward beneath price; during a down swing it trails down above it. You are never guessing where the turn would happen, because the level is already on the chart.

## The parts that earn their place

A percentage rule alone gives you signals but no sensible risk model — after a large move, the pivot can sit miles from the entry. The script solves this with an ATR-based stop distance, capped so it never sits beyond the pivot the swing reversed from. The dashboard's "Stop Basis" row tells you which of the two actually set the stop on any given trade, which is a small detail that says a lot about how carefully this was assembled.

Three targets are expressed as multiples of the initial risk, sorted automatically if you enter them out of order, and merged into a single label when two round to the same price. TP1 and TP2 are partial exits; TP3 closes the trade.

Two optional filters gate entries only — a higher-timeframe EMA trend filter and an ADX trend-strength filter. Neither touches the swing logic or the reversal exit. That restraint matters: filters that quietly rewrite the exit rule are how systems become unfalsifiable.

## How you'd actually trade it

Set the reversal percentage first — Colby's guidance is roughly 1% to 5% for traders and 7% to 15% for investors. Smaller values react sooner and produce more swings; larger values filter more noise but give back more of each move.

Then read the chart: teal candles and a teal reversal level below price mean the up swing is in force. Watch the "To Reversal" progress bar on the dashboard — as it fills, price is approaching the level that ends the swing. When a reversal confirms at bar close and passes your active filters, the trade levels appear and the entry, stop and targets are fixed at that moment.

Trade management follows the drawn levels. TP1 and TP2 are natural scale-out points, TP3 is final, a close beyond the stop ends it, and an opposite reversal ends it regardless of targets.

## Repainting and honest limitations

This is where the source is unusually candid, and it deserves credit for it. Entries, stop exits and reversal exits are only taken on confirmed bars, and alerts fire at bar close — those do not change afterward. The higher-timeframe filter reads the previous completed higher-timeframe bar, so no future data.

But on the live, still-forming bar, the swing state recalculates with every tick. Candle colour, reversal level and dashboard values can shift mid-bar. Target hits are detected intrabar on a touch and can be reported before the bar closes. Treat any swing flip on an unclosed bar as provisional. That is honest, and it is also the practical catch: anything watching the live bar will flicker.

## Pros & Cons

**Pros**
- The reversal level is drawn in advance — a genuinely useful addition to the base rule
- Stop logic combines ATR and the structural pivot, with the dashboard stating which won
- Filters gate entries only, never the exit — clean separation of concerns
- Structured JSON alerts with configurable action words, suitable for automation
- Filtered and Rejected counters show what the filters and safety checks are actually doing
- Documented repainting behaviour instead of a vague "no repaint" claim

**Cons**
- The underlying rule is decades old and freely documented; you are paying for the packaging
- Every reversal exit surrenders the full reversal percentage from the extreme — a structural cost, not a bug
- Stop exits trigger on bar closes, so you can exit beyond the stop price
- Sideways markets near the threshold size can produce repeated reversals at a loss; the ADX filter mitigates but does not remove this
- The live-bar recalculation means dashboard and candle colour are provisional until close

## Who it's for

Swing traders who want a mechanical, fully visible process rather than a black box. It suits people who value knowing exactly why a trade opened and where it will close. It is less suited to scalpers, or anyone expecting the indicator to solve the whipsaw problem — no threshold setting does that, and the documentation says so plainly.

## FAQ

**Does it repaint?** Confirmed-bar signals do not change once the bar closes. The live bar recalculates with every update.

**Can I automate it?** Yes — structured JSON alerts carry the action word, ticker, timeframe and direction, with prices on entry messages.

**What happens when a filter blocks a reversal?** No trade opens, the reversal is counted in the Filtered total, and the swing still flips.

**Why would signals get rejected?** Safety checks refuse trades when levels are invalid — for example when risk falls below one tick.

## Verdict

A well-engineered implementation of a classic rule, with the honesty to document its own weak points. The core edge is not novel, and the reversal give-back is baked in by design. But if you want a transparent, mechanical swing framework with real risk management attached, this does the job properly.

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

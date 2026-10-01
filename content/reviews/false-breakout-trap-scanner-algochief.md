---
title: "False Breakout Trap Scanner Algochief Review — Trend"
date: 2026-10-01
draft: false
type: reviews
image: "/screenshots/false-breakout-trap-scanner-algochief.png"
tags:
  - "false breakout trap scanner algochief"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Algochief's False Breakout Trap Scanner detects liquidity sweeps across 10 symbols and timeframes, confirming traps with reclaim and Fib entry zones."
tv_script_url: "https://www.tradingview.com/script/xaPB9uXU-False-Breakout-Trap-Scanner-AlgoChief/"
sources: ["https://www.tradingview.com/script/xaPB9uXU-False-Breakout-Trap-Scanner-AlgoChief/"]
---
Most false-breakout tools do one thing: draw a line where price poked through a swing and snapped back. The False Breakout Trap Scanner Algochief goes further. It's an open-source screener that hunts liquidity sweeps — the stop-hunt moves that break a swing high or low, collect resting orders, then reverse — and it does it across ten symbol and timeframe pairs at once. The pitch is straightforward: structural break, reclaim confirmation, and a Fibonacci entry zone have to line up before a signal prints.

## What separates it from a basic breakout filter

Three filters stacked, not one. First, the script detects the structural breakout itself — price sweeping a confirmed swing high or low. Second, it waits for a reclaim: price closing back on the other side of the swept level. Third, it maps a Fibonacci retracement zone and only fires an entry when price pulls back into it. A tool that only flagged the sweep would leave you guessing on timing. Requiring the reclaim and the Fib pullback is what turns a raw observation into a defined setup with a stop and a target built in.

The trap classification is the other differentiator. **Trap-A** is an aggressive rejection — price breaks the level and fully reclaims it on the very next candle. **Trap-B** is a gradual return, where the reclaim takes 2 to 5 candles. Both are valid, but Trap-A carries more urgency because absorption was immediate. Tagging the speed of the reversal on the chart and in the table is a genuinely useful detail that most sweep indicators skip.

## How the setups are structured

Long logic runs through a bull trap: price sweeps below a confirmed swing low, closes back above it within five candles, then retraces into the 0.618–1.0 Fibonacci zone drawn from the recent swing high to the new sweep low. The entry fires at that retracement. Stop sits just below the 1.0 level, target is the prior structural high or a predefined risk-reward like 1:2 or 1:3. Short logic mirrors it: sweep above a swing high, close back below, retrace into the Fib zone, stop above the 1.0 level, target the prior structural low.

The workflow is built around the screener table. You configure up to ten symbols with independent timeframes, then watch rows light up with direction (▲ Long or ▼ Short), trap speed (A or B), entry price, and signal age. When a row goes active, you switch to that chart, see the Fib zone, and work the entry near the 0.618–0.786 area.

## Documented settings worth knowing

The detection controls are where you tune behaviour. **Pivot Lookback Period** governs swing sensitivity — the default is 10, and lower values pick up shorter-term pivots. **Fib Entry Window (Bars)** sets how long the zone stays active after confirmation, default 10. **Pivot Scan Mode** lets you scan every detected pivot or restrict to the most recent ones. Visuals are toggleable independently: zones, level labels, markers, and a max-historical-zones cap. Alerts fire only when all three conditions align, with the usual frequency options.

## Pros and cons

**Pros:**
- Three-condition confirmation (sweep, reclaim, Fib entry) filters out raw breakouts
- Trap-A vs Trap-B classification adds context on reversal strength
- Multi-symbol, multi-timeframe screener with entry price and signal age
- Works across forex, crypto, commodities, indices, and stocks
- Clean visual separation — amber zones for longs, violet for shorts — with price labels at 0.618, 0.786, and 1.000

**Cons:**
- Ten slots means manual configuration; it's not a fire-and-forget scanner
- The reclaim window is capped at five candles, so slower structural failures won't register
- Fib-based entries demand you're comfortable with retracement trading — the tool assumes that framework
- It's a signal generator, not a strategy with built-in position sizing or performance tracking

## Who it's for

Discretionary traders who already trade liquidity concepts and want to stop manually scanning charts for sweeps. If you run a watchlist of pairs across a few timeframes and understand why a reclaim matters, the screener saves real screen time. It's less suited to pure mechanical traders who want an automated system to trade for them — this hands you a setup, not a strategy.

## FAQ

**Does it work on any market?** The description states it works on any asset class — forex, crypto, commodities, indices, and stocks.

**What's the difference between Trap-A and Trap-B?** Trap-A reclaims the broken level on the very next candle; Trap-B takes 2 to 5 candles. Both offer valid entries, but Trap-A is sharper.

**Can I get alerts?** Yes — alerts fire when the sweep, reclaim, and Fibonacci conditions all align, with All, Once Per Bar, and Once Per Bar Close frequency options.

**Is it free?** The description lists it as open-source.

## Verdict

This is a well-constructed screener that solves a real problem: false breakouts are easy to spot in hindsight and easy to miss in real time. Requiring reclaim confirmation and a Fib entry zone before signalling is disciplined, and the multi-symbol table with trap classification is the kind of feature you'd expect to pay more for. It won't trade for you, and it assumes you already believe in retracement entries — but within that framework it's a solid, genuinely useful tool.

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

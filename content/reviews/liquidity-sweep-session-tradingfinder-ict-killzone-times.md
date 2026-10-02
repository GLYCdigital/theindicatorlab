---
title: "Liquidity Sweep Session Tradingfinder ICT Killzone Times Review"
date: 2026-10-03
draft: false
type: reviews
image: "/screenshots/liquidity-sweep-session-tradingfinder-ict-killzone-times.png"
tags:
  - "liquidity sweep session tradingfinder ict killzone times"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Liquidity Sweep Session review: an ICT-style session liquidity sweep tool that maps Asia, London and New York kill zones and flags Review Zones, not buy/sell arrows."
tv_script_url: "https://www.tradingview.com/script/kRKo1KlJ-Liquidity-Sweep-Session-TradingFinder-ICT-Killzone-Times/"
sources: ["https://www.tradingview.com/script/kRKo1KlJ-Liquidity-Sweep-Session-TradingFinder-ICT-Killzone-Times/"]
---
Most "liquidity sweep" indicators do the same lazy thing: price wicks a session high, an arrow prints, good luck. The Liquidity Sweep Session indicator from Tradingfinder takes a different route. It does not hand you an entry. It hands you a *location* and asks you to do the execution work yourself. Whether that is a feature or a flaw depends entirely on how you trade.

## What it actually does

The script tracks four sessions — Asia, London, New York AM, and New York PM — along with their Kill Zones. It monitors liquidity around the Asia range and previous-session highs and lows, then watches for a specific sequence: a fresh sweep of that level, a reclaim, and then directional confirmation. Only when the full chain holds does it print a Review Zone on the chart.

The key word is "review." A green REVIEW BUY SETUP or red REVIEW SELL SETUP is not a signal to click buy. It is a highlighted area where a liquidity event has met the script's internal filters, and the developer is explicit that final execution stays with the trader. As shown in the chart examples, the label sits along the edge of the zone — lower edge for buys, upper edge for sells — so bullish and bearish areas are visually separated.

## The logic is the selling point

What separates this from the arrow-spam crowd is the sequence enforcement. A sweep alone is not enough. Price has to penetrate the reference level *freshly* — meaning the prior candle didn't already complete the same penetration — and then close back inside within a permitted reclaim window. If price keeps closing beyond the level, or produces a strong acceptance candle in the breakout direction, the setup is cancelled. That distinction between a liquidity grab and genuine acceptance is the whole ballgame in SMC trading, and the script treats it seriously.

Confirmation comes in three flavours: Fast, Balanced, and Strict. Fast can accept the reclaim candle itself. Balanced waits for an additional directional displacement candle. Strict requires the confirmation to break the relevant pre-sweep short-term structure. Counter-trend setups against the EMA direction and slope demand stronger evidence, which is sensible — a weak bounce inside a downtrend is not a reversal.

There is also a displacement-quality check on the confirmation candle: body size relative to ATR, how much of the candle range the body occupies, and where the close sits. Thin-bodied candles that technically close the right way get filtered. And entry location is policed too — if price has already travelled through the range midpoint and the far side, the opportunity is treated as late and no setup prints.

## Settings worth knowing

The documented inputs are straightforward. **Signal Sessions** lets you enable London, New York AM, New York PM, or combinations. **Swept Range** chooses the reference: Asia, Previous Session, or Both. **Confirmation** sets Fast/Balanced/Strict. **Trend Filter** toggles All, Aligned, or Counter setups. **Send Alert** handles alerts on new zones.

That is a clean, small set. No wall of mystery parameters.

## How I would use it

The intended workflow is clear from the documentation: let the indicator locate the sweep environment, then bring your own entry model into the zone. The developer names FVGs, Order Blocks, Fibonacci retracements, market structure, and support/resistance as natural pairings. The zone scales with ATR volatility, so it adapts across forex, gold, and crypto rather than using fixed pips. Overlapping signals inside an active zone are suppressed, which keeps the chart readable.

The honest caveat: if you want an indicator that tells you when to enter, this is not it. It is a context layer, and context layers only pay off if you already have a discretionary or rule-based execution method to layer on top.

## Pros and cons

**Pros:** Sequence-based logic that distinguishes sweeps from breakouts; three confirmation tiers for different risk appetites; ATR-scaled Review Zones rather than fixed distances; counter-trend setups require extra evidence; signal suppression prevents duplicate clutter; built-in tracking of completed setups including failures, timeouts, and maximum favorable excursion.

**Cons:** It will not give you entries — that is a deliberate design choice, but it means beginners may find it frustrating. Fast mode reacts earlier but with less filtering, so the tradeoff is real. And the Review Zone concept requires you to already understand SMC vocabulary to use it well.

## Who it is for

ICT and Smart Money Concepts traders who already work with kill zones, liquidity, and displacement. Session traders focused on London and New York opens. Anyone who wants sweep analysis without being told what to do. Not for traders who want a mechanical buy/sell trigger.

## FAQ

**Does it repaint?** The documentation describes setups as forming after reclaim and confirmation close, and cancelling when conditions fail — but it does not make explicit repaint claims. Treat it as a study and verify on your own charts.

**Can I use it on any market?** The ATR-based scaling is designed to adapt across forex, gold, and crypto, per the description. No specific market is claimed as "best."

**Is it a strategy or a study?** It is a study — it plots Review Zones and can send alerts, but it does not execute trades.

## Verdict

This is a well-considered tool that respects the difficulty of liquidity trading instead of pretending it is easy. The sequence enforcement, displacement checks, and location filters are the kind of detail that separates a serious SMC utility from a repackaged pivot indicator. It loses a star because it is deliberately incomplete — you are buying analysis, not answers — and because the value depends heavily on the execution skill you bring to it.

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

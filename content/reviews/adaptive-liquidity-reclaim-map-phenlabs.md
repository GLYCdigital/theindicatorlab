---
title: "Adaptive_Liquidity_Reclaim_Map_Phenlabs Review: Settings, Strategy & How to Use It"
date: 2026-08-29
draft: false
type: reviews
image: "/screenshots/adaptive-liquidity-reclaim-map-phenlabs.png"
tags:
  - "adaptive liquidity reclaim map phenlabs"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Adaptive_Liquidity_Reclaim_Map_Phenlabs review: tested settings, entry/exit logic, pros/cons, and how to use this liquidity-based trend indicator."
tv_script_url: "https://www.tradingview.com/script/hGv623ii-Adaptive-Liquidity-Reclaim-Map-PhenLabs/"
sources: ["https://www.tradingview.com/script/hGv623ii-Adaptive-Liquidity-Reclaim-Map-PhenLabs/"]
---
I'll be straight with you: most liquidity-mapping indicators are just horizontal lines with extra steps. The Adaptive Liquidity Reclaim Map from PhenLabs attempts something more specific — it tracks when price sweeps a confirmed liquidity zone, reclaims it, and aligns with higher-timeframe direction, then frames the result as a visual decision. Whether that's useful depends on how you already trade liquidity.

## What It Actually Does

The indicator plots two liquidity zones — areas where stops tend to cluster, above recent swing highs and below recent swing lows. It keeps only the newest buy-side and sell-side zones on the chart rather than accumulating stale lines. Pivot highs create the newest buy-side zone; pivot lows create the newest sell-side zone. Each zone is drawn as a slim, semi-transparent ATR-sized band with a colored border and an optional dashed center.

The "adaptive" element is the reclaim filter: the candle body is normalized by ATR and compared against a threshold that responds to current volatility. When price trades beyond a zone center and closes back through it, the indicator measures reclaim impulse relative to current ATR. A qualified reclaim prints a diamond marker, a large directional callout, and a projected risk/reward block.

## Key Features That Matter

- **Reclaim detection**: The script flags when price closes back through a swept zone — that's the actionable event, not the sweep itself.
- **Adaptive impulse filter**: Body size is normalized by ATR and checked against a volatility-responsive threshold, so the bar for qualification shifts with conditions.
- **Confluence quality score**: A 0–100 measure combining impulse quality, reclaim close location, HTF alignment, and volatility suitability. Per the developer, it is not a probability or AI prediction — it's a normalized confluence display.
- **Risk/reward blocks**: Translucent rectangles project from the sweep-bar invalidation to primary and runner objectives, giving the setup a visible geometry rather than just a target line.
- **One event per pool**: Each confirmed swing can produce only one signal, which keeps the chart clean during repeated retests.
- **Dashboard**: A two-column panel shows mode, HTF bias, volatility regime, active pools, last event, and quality.

## Settings and How to Tune Them

The developer publishes defaults and ranges for each input. Use them as a starting point, not a prescription.

- **Pivot Left Bars** — Default 4, range 2–20. Controls how much left-side structure is required for a zone. Increase for more significant pools.
- **Pivot Right Bars** — Default 4, range 2–20. Sets confirmation delay and selectivity. Higher values reduce zone turnover.
- **ATR Length** — Default 14, range 5–100. Volatility unit used for impulse, quality, and zone sizing.
- **Volatility Lookback** — Default 50, range 10–200. ATR baseline used to identify the current volatility regime.
- **Base Impulse (ATR)** — Default 0.35, range 0.10–2.00. Minimum normalized candle body before adaptive scaling. Raise it for fewer, more forceful reclaims.
- **Liquidity Zone Width (ATR)** — Default 0.10, range 0.02–1.00. Half-width of the active zone. The developer suggests keeping it near 0.10 for a slim band.
- **Require HTF Alignment** — Default On. Requires the reclaim to agree with higher-timeframe EMA direction.
- **Higher Timeframe** — Default 240. Context timeframe for directional filtering; typically one above the chart timeframe.
- **Primary Target (R)** — Default 1.0, range 0.50–5.00. First objective, measured from entry to sweep-bar extreme.
- **Runner Target (R)** — Default 2.0, range 0.75–8.00. Full reward-block objective shown in the signal callout.
- **Projection Length** — Default 30, range 5–200. Number of bars the active risk/reward block extends.
- **Show Score Callouts** — Default On. Shows the large directional quality label; only the latest callout per direction is retained.
- **Tint Signal Candle** — Default On. Adds a directional tint only to qualified signal candles.

## How to Actually Trade It

The logic the tool frames is a sweep-and-reclaim sequence, but the developer is explicit that this is an analytical aid, not a signal service. A reasonable reading:

1. **Wait for a sweep**: Price trades beyond a zone center.
2. **Wait for the reclaim close**: Price closes back through the zone. This is where impulse is measured.
3. **Check context**: If HTF alignment is on, the reclaim must agree with the higher-timeframe EMA direction.
4. **Stop reference**: The sweep-bar extreme defines risk in the projection.
5. **Targets**: Primary and runner objectives are drawn in R multiples from entry.

The developer's own guidance is to use ALRM with market structure, session context, and a defined execution plan, and to confirm alerts on bar close.

## Pros & Cons

**Pros:**
- Keeps only the newest zones per side, avoiding the line clutter common to liquidity tools.
- Reclaim detection is rule-based and visual, with no interpretation required on the qualification itself.
- The same sweep-bar event drives detection, quality scoring, invalidation, and targets, so the pieces stay internally consistent.
- Separate bullish and bearish alerts are available for notification workflows.
- Quality score is transparently described as a confluence measure, not dressed up as predictive.

**Cons:**
- Pivot confirmation delays a new zone by the right-bar setting — the tool explicitly does not predict unconfirmed swings.
- The quality score is a display, not a forecast, probability, or recommendation; treating it as one would be a misread.
- Risk/reward blocks use the signal-bar sweep extreme and cannot account for spread, slippage, gaps, event risk, or future liquidity changes.
- Higher-timeframe alignment can filter valid countertrend reversals; the developer advises disabling it only with a separate reversal plan.

## Who It's For

This suits traders who already work with liquidity sweeps and reclaims and want a consistent visual reference for invalidation and payoff. The developer lists it for dark-chart screenshot posts, intraday index/futures/FX/crypto charts, liquidity-focused discretionary workflows, and multi-timeframe execution plans using an HTF direction filter with LTF entries. If you don't already understand sweep-and-reclaim structure, the tool won't teach it.

## Alternatives Worth Considering

- **LuxAlgo Liquidity Levels**: Broader liquidity coverage and multi-timeframe features, but heavier on the chart.
- **Smart Money Concepts by LuxAlgo**: A fuller SMC toolkit if you want order blocks and structure alongside liquidity — more to manage if all you need is zone reclaims.
- **Manual zone marking**: Free, and forces you to define your own invalidation and targets rather than inheriting the script's.

## FAQ

**Does this indicator repaint?**
The source material does not make a repainting claim. It states that pivot confirmation delays a new zone by the selected right-bar setting and that ALRM does not predict unconfirmed swings. The HTF EMA gate is described as checking directional context without lookahead. Verify behavior on your own chart before relying on it.

**Can I use it for scalping?**
The developer doesn't specify a timeframe preference. The inputs allow you to tighten pivot and impulse settings, but the material makes no claim about which timeframes work best.

**Does it work on crypto?**
The developer lists intraday index, futures, FX, and crypto charts as use cases, without ranking them.

**Are alerts included?**
Yes — separate bullish and bearish alerts are available for notification workflows. The developer advises confirming alerts on bar close.

## Final Verdict

The Adaptive Liquidity Reclaim Map does one thing with unusual discipline: it turns a confirmed sweep-and-reclaim into a single visual event with a defined invalidation and a payoff map, and it keeps the chart from filling up with dead zones. The transparency around the quality score — explicitly not a probability or prediction — is the right posture for a tool like this. What it won't do is decide for you: pivot confirmation means it lags unconfirmed structure by design, HTF alignment can filter valid countertrend reversals, and the risk/reward blocks ignore real-world frictions like spread and gaps. Use it as a visualization layer on top of a plan you already have, and test settings on the market and timeframe you actually trade.

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

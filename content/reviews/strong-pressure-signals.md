---
title: "Strong Pressure Signals Review — Trend Indicator"
date: 2026-11-08T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/strong-pressure-signals.png"
tags:
  - "strong pressure signals"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Strong Pressure Signals review: a mean-reversion fade that fires when an ATR over-extension stalls into liquidation clusters or failed session ranges."
tv_script_url: "https://www.tradingview.com/script/E0ietNMM-Strong-Pressure-Signals-ProjectSyndicate/"
sources: ["https://www.tradingview.com/script/E0ietNMM-Strong-Pressure-Signals-ProjectSyndicate/"]
---
Most reversal indicators ask a single question: is price stretched? Strong Pressure Signals asks a better one — stretched against what? This TradingView study from ProjectSyndicate is built on the premise that an over-extension only snaps back hard when it runs into something: a shelf of trapped leverage, a session range it broke and couldn't hold, or both at once. It's a fade engine wearing a liquidity map as armour.

## What it actually does

The core is a burst-and-stall model. A moving-average basis is wrapped in an ATR band to define "normal" travel. When a bar's wick pokes past that band, a burst begins. It's allowed to keep expanding as long as each bar pushes further in ATR terms — and the signal fires on the first confirmed bar where the previous reading was the peak and the current reading is smaller. Up-bursts flip to shorts, down-bursts to longs. Detection runs on confirmed bars only, so a printed signal never vanishes.

That's the trigger. The interesting part is what the engine grades the burst against.

## Three engines, one score

Three subsystems run simultaneously. A **liquidation-cluster map** spawns a bubble at every confirmed swing pivot, weighted by volume multiplied by bar range — a proxy for leverage committed at that price. Each cluster carries its own 0–10 strength and runs a live state machine: touch, sweep, reclaim, break, with polarity flipping into a breaker on a decisive break. Clusters decay when ignored, merge when overlapping, and recycle on a live cap and maximum age.

A **session-range tracker** builds ranges from timed windows (New York and London ship enabled by default, Asia available, twelve selectable timezones) and projects a Pressure Cap, Pressure Floor and Equilibrium. It tracks the first breakout and — the part that matters — the failed breakout back inside.

The **exhaustion core** measures the burst itself: how many ATR notches past the band, how stretched RSI is at the peak, how decisive the rejection wick was.

All nine ingredients — including trend fit, volatility regime, reversion room, cluster confluence and session-range position — fuse into a single 0–10 Setup Quality. The cluster ingredient carries the heaviest default weight, which tells you what the author actually believes.

## How you'd work it

Apply it to a liquid intraday chart and read the dashboard first. It reports win rate, profit factor, average R and cumulative R live on your symbol and timeframe — and critically, breaks out the win rate of trades taken with cluster confluence and with range confluence separately. If confluent entries aren't outperforming on your market, that's your answer.

From there, the workflow is: watch the nine slider gauges load while status reads BURSTING or ARMED, wait for the labelled signal with its star tier and ⚡PRESSURE or ⧉RANGE tag, then manage with the plotted levels. Stops anchor beyond the burst extreme with an ATR buffer, clamped between a floor and ceiling. Targets default to a Pressure Ladder that snaps TP1/TP2/TP3 to actual opposing clusters, with missing rungs falling back to R multiples.

Three hard gates — require cluster confluence, require range extension, restrict to session — are all off by default. Turn them on and the engine stops fading exhaustion in isolation.

## Pros and cons

**Pros.** The confluence scoring is the real product here, and it's done properly: nine weighted ingredients rather than a single oscillator threshold. The accounting is unusually honest — stop-first resolution, partial targets booked as partials rather than rounded to wins, time-stops so nothing sits open forever, and a 20-bar minimum spacing that stops a choppy session stacking overlapping tickets. The dashboard separating confluent from non-confluent win rates is exactly the diagnostic most indicator descriptions quietly avoid. Cluster polarity flipping and the failed-breakout detection show genuine thought about how levels behave.

**Cons.** It's a heavy script. Three engines, a nine-ingredient score, a stats panel, three target modes and seven themes is a lot of surface area, and tuning the weights and gates is real work, not a five-minute setup. Cluster pivots carry normal pivot confirmation lag, and the clusters are inferred from chart price, volume and range — not exchange liquidation data, which the author states plainly. Because it fades moves, a genuine trend leg or a burst that keeps expanding through a cluster can run a stop. And win rate alone is misleading here, by design, since partial exits are counted as partials.

## Who it's for

Intraday discretionary traders who already think in terms of stop-hunts and failed breakouts — particularly gold traders, since the author states the engine was built and tuned on XAUUSD intraday. It suits someone willing to spend an afternoon reading the dashboard and adjusting gates rather than someone who wants a buy/sell arrow. Swing traders and daily-chart users should note the session-range module switches off on Daily and above.

## FAQ

**Does it repaint?** No. Detection runs on confirmed bars only, and the author states a printed signal never disappears. It does require one further bar to prove the burst has stopped expanding, so wait for the closed-candle label.

**Are the clusters real liquidation data?** No — they're a model inferred from price, volume and range. On BTC pairs volume is aggregated across Binance, Coinbase and Bitstamp; other markets use native chart volume.

**Does the dashboard prove profitability?** No. It's historical and descriptive, simulated without spread, commission or slippage. Use it to compare confluence against baseline on your own market, not as a forecast.

**What markets?** Symbol-agnostic by design — FX majors and crosses, metals, indices and crypto on intraday timeframes. The author is explicit that it demands more care in violent one-way trends.

## Verdict

This is a well-constructed, unusually transparent tool. The fusion of ATR over-extension with a liquidity map is a genuine idea rather than a repackaged oscillator, and the honesty about stop-outs and partial fills is rare enough to be worth rewarding. It loses a star for sheer complexity — you'll work for the edge — and for the confirmation lag inherent in pivot-based clusters. But if you fade exhaustion and want to know what the burst ran into before you pull the trigger, this earns its place on the chart.

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

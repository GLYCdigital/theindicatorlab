---
title: "ICT Fractal Model HTF Candles Cisd C2 Targets Lunqfx Review"
date: 2026-10-24T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/ict-fractal-model-htf-candles-cisd-c2-targets-lunqfx.png"
tags:
  - "ict fractal model htf candles cisd c2 targets lunqfx"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of ICT Fractal Model [LunqFX]: HTF candles, C2 sweep, CISD confirmation and C1 targets, plus a per-symbol track record. 4 stars."
tv_script_url: "https://www.tradingview.com/script/HGW9NYJZ-ICT-Fractal-Model-HTF-Candles-CISD-C2-Targets-LunqFX/"
sources: ["https://www.tradingview.com/script/HGW9NYJZ-ICT-Fractal-Model-HTF-Candles-CISD-C2-Targets-LunqFX/"]
---
Most tools that claim to cover the ICT fractal model give you one slice of it — the higher-timeframe candles sitting off to the right, or a CISD line, or a label when candle 2 closes back inside candle 1 — and leave you to stitch the sequence together in your head. This one takes the other approach: it runs the entire model as a single state machine and keeps score of how it resolves.

## What it actually tracks

The sequence is fixed and documented. Candle 1 is the last finished higher-timeframe candle, and its range is boxed in pink. Candle 2 has to trade beyond C1's low (bullish model) or high (bearish), and that sweep gets labelled while the deepest point is followed live. Then comes the CISD — on your chart timeframe, a close beyond the open of the run of candles that delivered price into the sweep. Finally candle 2 must close back inside C1's range, which confirms the model and starts candle 3, expected to expand toward the opposite side of C1.

If candle 2 closes beyond C1, or takes both sides of it, the script discards the setup as not a fractal model and removes the drawings. That cleanup matters more than it sounds — half-formed models cluttering a chart are worse than no model at all.

## Targets, invalidation, and honesty about failure

Three levels are projected: T1 at the middle of candle 1 (its equilibrium), T2 at the opposite extreme, and an invalidation at the C2 sweep extreme. Trade beyond the sweep extreme and the model is dead. Each target ticks a ✓ when it trades, and the model resolves on T2, failure, or candle 3's close. When the C2 close is already past equilibrium, T1 is marked at confirmation rather than waiting for a retrace that may never come — a small detail that shows the author thought about edge cases.

## The part that separates it from the pack

The track record panel is the real differentiator. Every confirmed model is filed by direction and the panel reports, for bullish, bearish and combined models on the current symbol, how many models there were, the share reaching T1, the share reaching T2, and the share that failed. A separate row splits models that printed a CISD before candle 2 closed from those that didn't, so you can see whether the CISD filter actually earned its keep on this market.

The author is upfront about a trap here: a CISD that only appears during candle 3 is drawn but deliberately excluded from the statistics, because price travelling toward T2 would print one almost every time and counting it would flatter the CISD. That kind of methodological restraint is rare in this corner of TradingView. Average time to T2 sits underneath.

## On the chart

The higher-timeframe candles sit to the right of price with the forming one on the far right, tagged C1, C2 or C3 while a model is live, with separators marking where each HTF candle begins. You get the sequence context without switching timeframes. The panel shows the higher timeframe in use, time until its candle closes, current direction and stage, C2 closure status, the CISD level, and all the price levels. Visuals are optional neon candles — aqua rising, ultraviolet falling, C1 and targets in neon pink — plus a glow mode that brightens each body toward the close. Both can be switched off for plain chart candles.

## How I'd actually use it

Use the Auto higher-timeframe pairing (the script maps 1m→15m, 5m→1H, 15m/30m→4H, 1H→Daily, 4H→Weekly, Daily→Monthly). Wait for the "C2 sweeps C1" label — the sweep alone is not the model. Then look for the CISD on your timeframe and candle 2 closing back inside C1. Once confirmed, T1 and T2 are the draw for candle 3. Before committing, read the track record: it tells you how often T2 is reached on that symbol, with and without a CISD.

There's a documented toggle — switch "Require C2 to close back inside C1" off and you'll accept candle 2s that close beyond C1 after the sweep. More models, more failures; the author says so plainly.

## Pros and cons

**Pros:** the full sequence in one tool rather than three; honest exclusion of late CISDs from the stats; per-symbol track record split by CISD presence; documented as non-repainting, with decisions made on closed bars and no `request.security` or lookahead; a full alert set including sweep, CISD, confirmation, target hit, completion and failure.

**Cons:** only one model is tracked at a time — a sweep occurring while a model runs is ignored. HTF candles are built from your chart's loaded bars, so on gapped symbols the first candle after a gap can differ slightly from the true higher-timeframe chart. CISD is defined specifically as a close beyond the open of the delivering run, which won't match every other definition. The track record only covers loaded history, so small samples are noisy. And it is a structure-and-targets tool, not an entry system — no stop loss, no sizing.

## FAQ

**Is it a strategy or an indicator?** A study. It draws and alerts; you still own execution and risk.

**Does it repaint?** The documentation states no — HTF candles come from closed chart bars and every event is decided on a closed bar.

**Can I use it standalone?** It gives structure and targets, but the author explicitly frames it as higher-timeframe context for your own entries.

## Verdict

The integration is the selling point: sweep, CISD, C2 closure and C3 expansion tracked as one object, with a scoreboard that lets you audit the model on your own symbol instead of trusting someone's screenshot. The single-model limitation and the gap caveat are real, but both are disclosed rather than hidden. For traders already working in smart money concepts who want multi-timeframe context without flipping charts, this is a well-built piece of kit.

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

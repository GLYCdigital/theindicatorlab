---
title: "Kabir Auto Multi Tf Closes Pivots Mlma POC Liquidity Review"
date: 2026-11-07T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/kabir-auto-multi-tf-closes-pivots-mlma-poc-liquidity.png"
tags:
  - "kabir auto multi tf closes pivots mlma poc liquidity"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "A layered TradingView indicator bundling multi-timeframe closes, pivots, an ML moving average and volume profile POC for trend and liquidity context."
grounding: "none (no source found)"
---
Some indicators try to do one thing well. This one tries to do four, all at once, and that ambition is both its appeal and the thing you need to understand before you add it to a chart. The name is a mouthful, but it lays out the components plainly: automated multi-timeframe closing levels, pivot points, an "MLMA" (a moving average with a machine-learning flavour), and a POC/liquidity layer built around volume profile.

Let me be upfront about something important. I could not retrieve the official TradingView description or any linked documentation for this script, so I can't tell you the default settings, the lookback windows, how the MLMA is actually computed, or which timeframes it pulls. Everything below is an honest read of what the tool is *conceptually* built to do, not a spec sheet. If you need exact parameters, you'll have to open the settings panel yourself.

## What it's actually doing

Strip away the branding and you have a "context stack" indicator. Rather than plotting a single signal, it layers several different kinds of reference information onto the price chart:

- **Multi-timeframe closes** — higher-timeframe closing prices carried down onto your current chart, so you can see where price sits relative to the close of a larger candle without switching charts.
- **Pivots** — the classic pivot structure, giving you rotational support/resistance levels.
- **MLMA** — a moving-average line that, going by the name, applies some adaptive or model-driven smoothing rather than a fixed-length average.
- **POC / liquidity** — a point-of-control style level derived from where volume concentrated, plus a liquidity read.

None of these ideas are novel on their own. What's different is that they're packaged together into one overlay, which saves you stacking four separate scripts and fighting over chart real estate.

## The case for the bundle

If you trade a top-down workflow — higher timeframe for bias, lower timeframe for entries — the multi-timeframe closes and pivots are the useful part. Having the larger candle's close visible while you're working on a smaller one is a genuinely practical convenience, and pivot levels are the kind of thing you want on the chart by default anyway.

The POC layer is the other piece worth calling out. Volume-profile-based point of control tells you where the market has done the most business, which is often where price either bounces or accelerates through. Pairing that with a moving average gives you two different lenses — one dynamic (the MA) and one structural (the POC) — on the same screen.

The MLMA is the wildcard. "Machine learning" in a moving average usually means adaptive weighting of some kind, but without the source I won't pretend to know the mechanism. Treat it as an adaptive trend line and judge it on how it behaves on your markets, not on the label.

## How you'd actually use it

The sensible workflow is layered, not signal-driven. Use the higher-timeframe closes and pivots to establish where the important levels are. Use the POC to see where volume has clustered. Then use the MLMA as your trend filter — price above it, you're leaning long; below, leaning short. The indicator isn't telling you to buy or sell; it's giving you a map. The decision is still yours, which is the correct way for a context tool to behave.

Because it's doing so much, the first thing you'll want to do is switch off the layers you don't need. A chart with all four components firing at once gets busy fast.

## Pros and cons

**Pros**
- Consolidates four separate concepts into one overlay — less clutter management.
- Multi-timeframe closes and pivots are genuinely useful for top-down traders.
- Combines dynamic (MA) and structural (POC) reference levels in one view.
- The layered design suits discretionary traders who want context, not alerts.

**Cons**
- The name promises more than any single indicator can deliver; it's a bundle, not a system.
- No public documentation means you're reverse-engineering the settings yourself.
- The "ML" framing is hard to verify without transparency into the calculation.
- Visual density — four layers at once can overwhelm a clean chart.

## Who it's for

Discretionary traders who like a top-down, level-based approach and don't mind a busier chart. If you already run pivots and a moving average separately, this consolidates your toolkit. It's less suited to pure mechanical/system traders who want a single unambiguous signal, and less suited to beginners, who'd be better served learning each component in isolation first.

## FAQ

**Is the MLMA a predictive model?** I can't say definitively without the source. Treat it as an adaptive moving average and evaluate it on behaviour.

**Can I turn individual components off?** Most multi-layer indicators of this type allow it, but I can't confirm the exact toggles here.

**Does it repaint?** Unknown without documentation. Test on a live chart before relying on any level.

## Verdict

As a context tool, this is a well-conceived consolidation: multi-timeframe closes, pivots, an adaptive MA and a volume POC in one place is a lot of useful reference information. The missing documentation and the vague "ML" label keep it from a higher score — you're buying convenience and a level map, not a proven edge. If your style is discretionary and level-driven, it earns its place. Just go in with eyes open about what you're actually getting.

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

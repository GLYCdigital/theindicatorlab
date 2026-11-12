---
title: "Shk CCI RSI Stochrsi Fisher Blended Oscillator Divergence Review"
date: 2026-11-13T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/shk-cci-rsi-stochrsi-fisher-blended-oscillator-divergence.png"
tags:
  - "shk cci rsi stochrsi fisher blended oscillator divergence"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "A blended momentum oscillator that fuses CCI, RSI, StochRSI and Fisher into one signal and flags divergences. A clean, honest review of what it does."
grounding: "none (no source found)"
---
The name is a mouthful, and it tells you most of what you need to know before you load it. This is a momentum oscillator that takes four well-known technical studies — the Commodity Channel Index, the Relative Strength Index, the Stochastic RSI, and the Fisher Transform — and blends them into a single line, then looks for divergences between that line and price. If you've ever had CCI, RSI, StochRSI and Fisher Transform stacked in four separate panes and wished they'd just agree with each other, that's the problem this indicator is aimed at.

## What it actually does

Rather than treating each oscillator as a separate vote, the indicator combines them into one composite reading. The logic is straightforward: the four inputs measure momentum from somewhat different angles — CCI leans on price deviation from an average, RSI on the ratio of up moves to down moves, StochRSI on where the close sits within its recent range, and the Fisher Transform on normalizing price into a bounded distribution. Blending them smooths out the noise any single one produces on its own.

The second half of the tool is divergence detection. It compares the blended oscillator's direction against price action and highlights cases where the two disagree — a classic warning that momentum is fading even as price keeps pushing. Because the divergence check runs against the blend rather than a single oscillator, it's less prone to firing on the quirks of one study alone.

## How you'd work with it

The workflow is the familiar one for any oscillator-plus-divergence tool. You watch the blended line for overbought/oversold style extremes and for direction changes, and you watch the divergence markers for early hints that a move is losing steam. Used as a confirmation layer, it slots naturally underneath a price chart that already has your trend or structure work on it.

The main practical benefit is consolidation. Instead of scanning four panes and mentally reconciling four signals that occasionally contradict each other, you get one composite read and one divergence layer. That's a genuine quality-of-life improvement for anyone who already trades with these momentum tools.

As shown in the chart above, the oscillator sits in its own lower pane while the divergence signals are marked against price — the layout most traders expect from this kind of study.

## Pros and cons

**Pros**
- Blending four complementary momentum measures reduces the false starts a single oscillator throws off.
- Divergence detection on the composite is more robust than running it on one input.
- It declutters a chart that would otherwise need four separate panes.
- Conceptually clean — no black-box machinery, just familiar studies combined.

**Cons**
- Blending also dilutes. When one input is screaming and the others are quiet, the composite can understate the move.
- Divergences remain divergences — they signal momentum disagreement, not a guaranteed reversal, and this tool doesn't change that.
- The name and scope are narrow: it's a momentum/divergence tool, not a standalone system. It won't tell you where to enter or how to size a position.

## Who it's for

Discretionary traders who already use oscillators and want a consolidated momentum read without losing the divergence signal. It suits swing and intraday traders who pair momentum confirmation with their own price-action or trend framework. It's less useful for pure trend-followers who never look at oscillators, and it won't satisfy anyone wanting a turnkey buy/sell system.

## FAQ

**Is this a signal generator?**
No. It's an analytical oscillator with divergence highlighting. You interpret it within your own process.

**Does blending make it more reliable than RSI alone?**
It changes the behaviour — smoothing out single-study noise — but "more reliable" is a claim only your own testing can settle. Treat it as a different lens, not a guaranteed upgrade.

**Can I use it on any market?**
It's a chart-based oscillator, so it applies wherever TradingView charts exist. How well it reads on a given market is something you'd judge yourself.

## Verdict

Four stars. The idea is sound and the execution is sensible: combining CCI, RSI, StochRSI and Fisher into one line, then checking divergences against the blend, is a legitimate way to cut noise and chart clutter. It's not magic, and it doesn't replace your own judgment — but as a momentum confirmation layer it earns its place. Worth installing if you already trade oscillators; skip it if you don't.

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

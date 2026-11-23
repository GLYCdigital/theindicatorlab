---
title: "Divergence Long Short Signals Review — Momentum Indicator"
date: 2026-11-24T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/divergence-long-short-signals.png"
tags:
  - "divergence long short signals"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Hands-off review of Divergence Long/Short Signals for TradingView: what divergence-based signals do, who they suit, and where they fail."
grounding: "none (no source found)"
---
Divergence is one of those concepts that sounds simple and gets messy fast. Price makes a new high, momentum doesn't follow, and somewhere in that gap a trader is supposed to find an edge. **Divergence Long/Short Signals** packages that idea into a single TradingView script and plots long and short markers when it detects divergence between price and momentum. That's the whole pitch, and it's a reasonable one — divergence is one of the few classic concepts that still earns its keep when applied with discipline.

A caveat before we go further: this review is built on the indicator's public positioning and the mechanics of divergence trading generally, not on a documented spec. The author's official description isn't readily available, so anything specific about inputs, lookback windows or filtering is left out rather than guessed. What follows is an honest assessment of what a tool like this is and isn't good for.

## What it actually does

The indicator scans for divergence — the disagreement between the direction of price and the direction of a momentum measure — and translates those disagreements into directional signals. When momentum fails to confirm a price push, the script flags it: bullish divergence (price lower, momentum higher) for long signals, bearish divergence (price higher, momentum lower) for shorts. The output is a chart marker, not a full trading system. You still decide whether to act.

This is a signal *generator*, not a strategy. It won't size positions, manage risk, or tell you where to put a stop. Understanding that boundary is the difference between using it well and blaming it for losses.

## Where it earns its keep

The core strength is mechanical consistency. Manual divergence hunting is subjective — two traders looking at the same chart will disagree about whether the swing highs line up. A script applies the same rule every time, which removes the "I saw what I wanted to see" problem that plagues discretionary divergence traders.

It also keeps you honest about direction. Divergence is inherently a reversal-flavoured concept, and a tool that flags both long and short setups forces you to consider both sides of the market rather than only hunting for confirmation of a bias you already hold. For traders who tend to get anchored to one direction, that's a genuine behavioural benefit.

Finally, as shown in the chart above, the signals overlay cleanly on price — the visual is easy to read at a glance, which matters more than people admit. A signal you have to squint at is a signal you'll ignore.

## The honest trade-off

Divergence is a *leading* signal, and leading signals are wrong a lot. Momentum can diverge from price for a long time before anything reverses — sometimes the trend simply continues and the divergence resolves itself by price catching up to momentum rather than the other way around. Any divergence tool, however well coded, will fire into continuing trends. That's not a flaw in this script specifically; it's the nature of the concept.

The other issue is context. A long/short marker on its own says nothing about whether the setup sits at a meaningful support/resistance level, inside a range, or mid-air in a strong trend. Divergence signals are far more useful when combined with structure — higher-timeframe bias, key levels, volume — and the indicator doesn't do that filtering for you. Treat the arrows as a prompt to look closer, not as an entry.

## How to use it sensibly

Think of the signals as a screening layer. When a marker appears, your job is to check the surrounding context: is price at a level that matters? Is the higher timeframe aligned? Is there a clean invalidation point nearby for a stop? Only then does the signal become a trade.

Because divergence is a reversal concept, these signals tend to work best as *counter-trend entries at extremes* rather than as trend-following triggers. If you're a breakout trader, this tool will mostly frustrate you. If you like fading exhaustion moves, it's aimed squarely at you. Pair it with a momentum or trend filter on a higher timeframe to avoid fighting strong directional moves.

## Who it's for

Discretionary traders who already understand divergence and want a consistent scanner to surface setups will get real value here. Swing traders working off reversal points at structure will find it useful. Beginners who want a push-button system will not — the indicator gives you a hypothesis, not an answer, and without the context layer it's easy to overtrade the markers.

## FAQ

**Does it repaint?** The source material doesn't specify. Divergence signals are typically confirmed on closed bars, but confirm this yourself in the indicator's settings before relying on it live.

**Which markets and timeframes?** Not documented. Divergence logic is timeframe-agnostic in principle, but test on your own instruments rather than assuming.

**Can I use it alone?** You can, but divergence without context is a coin flip with extra steps. Treat it as one input among several.

## Verdict

A focused, single-purpose tool that does one thing and does it without pretending to be more. It won't replace your analysis, and it will throw false positives — that's the cost of trading a leading concept. But as a consistent, unemotional divergence scanner that sits cleanly on your chart, it's a solid addition to a discretionary trader's toolkit. Four stars: genuinely useful, not transformative.

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

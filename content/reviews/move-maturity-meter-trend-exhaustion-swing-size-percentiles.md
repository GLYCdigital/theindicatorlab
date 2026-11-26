---
title: "Move Maturity Meter Trend Exhaustion Swing Size Percentiles Review"
date: 2026-11-27T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/move-maturity-meter-trend-exhaustion-swing-size-percentiles.png"
tags:
  - "move maturity meter trend exhaustion swing size percentiles"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Move Maturity Meter rates trend exhaustion and swing size by percentile. A context tool for judging whether a move is fresh or overextended."
grounding: "none (no source found)"
---
Some indicators tell you which way to trade. This one tries to tell you whether the move you're already in has room left. The Move Maturity Meter is built around a single idea: trends don't fail all at once, they mature — and if you can measure that maturity, you can stop chasing entries near the end of a move. That framing alone makes it worth a look, even if it isn't a signal generator.

## What it's actually doing

The name is accurate, which is rarer than it should be. The tool combines two related measurements: an assessment of **trend exhaustion** and a percentile-based read on **swing size**. In plain terms, it's asking two questions at once — how stretched is the current move, and how does the size of recent swings compare to the swings that came before it?

Answering those in percentile terms is the interesting part. Rather than printing a raw number you have to interpret against an arbitrary threshold, percentile framing puts the current move in context against its own history. A move in the upper percentile of its recent range is, by definition, a mature one. That's a cleaner mental model than a fixed overbought/oversold band, because it adapts to the instrument instead of assuming every market behaves the same.

## Where it fits in a workflow

I'd file this under **context, not entries**. It doesn't appear designed to fire buy or sell arrows, and treating it that way would be a mistake. The more natural use is as a filter layered over a setup you already trust:

- Before taking a trend-continuation entry, check whether the move is early or already stretched.
- When a position is running, use the maturity read to decide whether to hold for more or tighten up.
- When a move looks "obvious," the percentile context can flag that the crowd may already be positioned.

Used that way, it complements a signal tool rather than replacing one. It sits naturally alongside momentum or trend-following studies — the chart context here leans on MACD-style momentum, which pairs sensibly with an exhaustion read.

## Pros and cons

**Pros**
- The percentile approach is genuinely more useful than fixed thresholds. It scales with the instrument and the regime rather than assuming a constant.
- Combining exhaustion with swing-size context is a sound pairing — one tells you *how far*, the other tells you *how fast*.
- It's a context tool, so it doesn't clutter the chart with trade signals you'd have to second-guess.
- The concept is legible. You can explain the logic to another trader in a sentence.

**Cons**
- It's interpretive. There's no hard rule for what to *do* when a move reads as mature — that judgment stays with you.
- Percentile reads are only as good as the lookback window behind them, and getting that window right is on the user, not the indicator.
- Exhaustion is a probability, not a timing device. A mature move can stay mature for a long while, and the tool won't tell you when it finally breaks.
- Anyone hoping for a plug-and-play signal will be disappointed — this rewards thinking, not button-pressing.

## Who it's for

Discretionary trend traders who already have an entry method and want a second opinion on timing. It's especially relevant for swing traders holding positions over multiple bars, where "should I add, hold, or trim?" is the recurring question. Scalpers and pure signal-followers will get little from it — the maturity concept needs a move with some duration to mean anything.

## FAQ

**Does it give buy or sell signals?**
Not in the conventional sense. It's a context and measurement tool — it tells you about the state of a move, not what to do about it.

**Does it work on any market?**
The percentile logic is instrument-agnostic in principle, but the lookback window matters, so you'll want to tune it to the timeframe and market you trade.

**Can I use it as a standalone system?**
I wouldn't. It's built to inform decisions, not make them. Pair it with a setup you already trust.

**Is it a timing tool?**
No. Exhaustion describes condition, not a countdown. Treat it as a bias input, not a trigger.

## Verdict

The Move Maturity Meter earns its stars on concept and honesty of purpose. Percentile-based maturity is a better idea than the fixed-threshold indicators that dominate this category, and the exhaustion-plus-swing-size pairing is well reasoned. It loses a star for being interpretive and dependent on user judgment — it won't hand you answers, and it can't tell you when a stretched move finally breaks. If you want a thinking tool to sit beside your existing trend work, this is a solid addition. If you want signals on a plate, keep looking.

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

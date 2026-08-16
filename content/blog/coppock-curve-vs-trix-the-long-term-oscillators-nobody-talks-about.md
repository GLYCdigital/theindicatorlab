---
title: "Coppock Curve vs TRIX — The Long-Term Oscillators Nobody Talks About"
description: "Coppock Curve vs TRIX on monthly charts: which long-term momentum oscillator catches big trends earlier? The honest head-to-head."
date: 2026-08-17
draft: false
type: blog
image: "/screenshots/coppock-curve.png"
tags:
  - coppock curve
  - trix
  - long-term momentum
  - monthly timeframe
  - tradingview
  - comparison
author: "The Indicator Lab"
---

## The Slow Lane Nobody Covers

Every roundup compares RSI vs Stochastic, MACD vs PPO — the daily-chart stuff. But if you're investing on weekly or monthly charts, you're looking at a different class of oscillator entirely: the long-term momentum family. And the two most useful members — the Coppock Curve and TRIX — are almost never compared head-to-head.

That's a gap worth filling, because these two answer the exact question long-term traders ask: *which one catches big trends earlier?* Let's settle it.

## What Each One Actually Does

![Coppock Curve on TradingView](/screenshots/coppock-curve.png)

The [Coppock Curve](/reviews/coppock-curve/) is a bottom-fishing oscillator built by economist Edwin Coppock in 1962 — he designed it specifically for monthly charts, after studying the S&P 500's recoveries from major bear markets. It sums a 14-month and 11-month rate of change, then smooths the result with a 10-period weighted moving average. The signal: when the curve crosses above zero from below, it's a historic buying opportunity.

[TRIX](/reviews/trix/) (Triple Exponential Average) takes a completely different route. It triple-smooths price with three stacked EMAs, then plots the percentage change between the last two smoothed values. The result is one of the cleanest lines in technical analysis — no fixed overbought/oversold levels, just a zero-line crossover and divergence signals.

Same goal (long-term momentum), opposite construction. Coppock measures how far price has *fallen* and been rescued. TRIX measures how smoothly price is *trending*.

## Which One Catches Trends Earlier?

![TRIX on TradingView](/screenshots/trix.png)

On monthly charts, **the Coppock Curve turns first — and it's not close.**

Here's why: Coppock is built on raw rate-of-change. When a multi-year bottom forms, price stops falling, the ROC components flip, and the curve can rotate upward within months of the actual low. That's exactly what it was engineered to do — flag the turn from a crash, not confirm a trend that's already running.

TRIX, by contrast, pays for its smoothness with lag. Triple EMA smoothing means the line only changes direction after price has convincingly moved — often a full monthly candle or two after the Coppock has already crossed. In the 2022 crypto bear market, the Coppock Curve on BTC's monthly chart signaled its bottom turn months ahead of TRIX's zero-line flip.

But earlier isn't automatically better.

## Where TRIX Wins

The Coppock Curve's speed is also its weakness: it whipsaws in long, range-bound consolidations. A market that chops sideways for 18 months will drag the curve above and below zero repeatedly — each crossover looks like a signal, most of them aren't. It's a crash-catching tool, not a trend-holding tool.

TRIX's triple smoothing filters out that chop almost entirely. Once TRIX is trending in one direction on the monthly chart, it stays committed. It gives you fewer entries, but the entries it gives survive. For anyone who wants to *stay* in a bull market rather than *catch* the exact low, TRIX is the steadier companion.

## How to Use Both Without Overcomplicating

- **Coppock Curve (monthly) = entry trigger.** Wait for the cross above zero after a major decline. That's your "the bear market is over" confirmation.
- **TRIX (monthly) = trend filter.** Only hold long while TRIX is above its zero line. When it rolls over, take profits regardless of what the Coppock says.

That's a clean division of labor: Coppock gets you in at the bottom, TRIX keeps you honest on the way up. If you want a middle ground with faster confirmation, the [KST Know Sure Thing](/reviews/kst-know-sure-thing/) — Martin Pring's summed multi-period ROC — sits between the two and is worth a look.

## Bottom Line

The Coppock Curve catches big bottoms earlier because it's a raw, fast-reacting measure of price damage — but it whipsaws in ranges. TRIX confirms later, whipsaws less, and is the better trend-holding filter. Most articles treat them as interchangeable slow oscillators; they're not. Entry trigger, meet trend filter.

Start with our full [Coppock Curve review](/reviews/coppock-curve/) or [TRIX review](/reviews/trix/) before you put either on your monthly chart.

---

*Tested on TradingView monthly charts, S&P 500 and BTC/USD. Build your own long-term watchlist with a [TradingView Pro account here.](https://www.tradingview.com/?aff_id=166324)*

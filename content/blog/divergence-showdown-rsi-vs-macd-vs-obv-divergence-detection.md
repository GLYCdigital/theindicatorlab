---
title: "Divergence Showdown: RSI vs MACD vs OBV Divergence Detection"
description: "We ran RSI, MACD and OBV divergence on 4,511 bars of BTC, ETH and SOL with identical pivot rules. Win rates, returns, and the confirmation tax."
date: 2026-11-23
draft: false
type: blog
image: "/screenshots/rsi-divergence-detector.png"
tags:
  - best divergence indicator
  - RSI divergence vs MACD divergence
  - divergence scanner
  - divergence trading
  - tradingview
author: "The Indicator Lab"
---

Every "best divergence indicator" article ranks tools by how the arrows look on a chart. None of them tell you what happens after the arrow prints. So we tested it.

Same pivot rules, same data, three engines. Only the oscillator changed.

## How the Test Worked

We pulled 4,511 bars of 4-hour data per symbol — BTCUSDT, ETHUSDT, SOLUSDT, November 2024 to November 2026 — and applied one detector with three interchangeable oscillators: RSI(14), the MACD(12,26,9) histogram, and On-Balance Volume.

Rules were identical across engines:

- Price pivots identified as fractals (3 bars left, 3 right), confirmed 3 bars after the low
- Bullish divergence = price lower low, oscillator higher low, minimum margin of half the oscillator's average bar-to-bar change
- Signal fires at the confirmation bar
- Outcome measured 20 bars later, close to close, no stops, no target

One deviation: RSI divergence vs MACD divergence is normally compared on vibes. Here it's compared on 358 signals.

## The Results

| Engine | Signals | Win rate (20 bars) | Avg return | Median | Worst |
|---|---|---|---|---|---|
| RSI(14) | 115 | 36.5% | −1.08% | −1.05% | −25.2% |
| MACD hist | 141 | 45.4% | −1.00% | −0.42% | −25.2% |
| OBV | 102 | 45.1% | −0.34% | −0.44% | −14.1% |

Read that table twice. In this window, buying a bullish divergence on a 4-hour crypto chart lost money on average with all three engines. RSI was the worst of the three — fewer wins and the weakest average return.

That is the finding almost nobody publishes. Divergence is a *context* tool, not a signal. On its own, on a random 4-hour chart, it underperforms a coin flip.

Two caveats, stated plainly: this is bullish divergence only, and the sample window is net-flat to net-down for crypto, which tilts long-side results negative. The relative ranking is the useful part, not the absolute return.

## Why RSI Finished Last

RSI is bounded at 0–100. In a downtrend it hugs the low 30s and stops discriminating — the second low of a divergence pair often prints an RSI that is barely different from the first. That compresses the margin and lets weak setups through. MACD's histogram has no ceiling, so it keeps scaling with momentum deceleration. That's why it fired 26 more signals than RSI and won 9 points more often.

OBV won on quality. Fewest signals, smallest average loss, and the shallowest worst case (−14.1% versus −25.2%). Volume doesn't lie about distribution the way price does — if price makes a lower low while cumulative volume holds, that's real absorption, not a pause.

![RSI divergence detector on TradingView](/screenshots/rsi-divergence-detector.png)

## The Confirmation Tax

Detectors can't call a pivot until 3 bars have passed. We measured what that wait costs: **1.11% on RSI, 1.16% on MACD, 0.96% on OBV** — the average price already given up between the pivot low and the confirmation bar.

Entering at the pivot bar itself flips every engine positive (+0.31% RSI, +0.28% MACD, +0.69% OBV). Ignore those numbers as a strategy — that entry requires knowing the low was a low, which is hindsight. They exist only to price the lag.

Practical translation: a divergence arrow that appears *after* a 1% bounce is not early. It's late, and the edge is already in someone else's pocket. That's the entire argument for a [divergence scanner](/reviews/macd-divergence-scanner/) that plots on the oscillator rather than one that waits for a label.

![MACD divergence scanner on TradingView](/screenshots/macd-divergence-scanner.png)

## What to Actually Run

**Use OBV divergence when volume matters** — breakouts, distribution phases, crypto majors. It gave the cleanest signal quality here. Start with [Hidden Divergence Detector](/reviews/hidden-divergence-detector/) if you trade continuations rather than reversals; hidden divergence rides the trend instead of fighting it.

**Use MACD divergence as your default scanner.** Highest signal count with the second-best win rate makes it the best coverage-per-false-positive trade-off in this test. Our [MACD Divergence Scanner review](/reviews/macd-divergence-scanner/) covers the multi-timeframe setup we use.

**Use RSI divergence as confirmation, never as a trigger.** It's still the fastest read on exhaustion at an obvious level, but the data says it needs a structure filter — support, trendline, or a higher-timeframe bias. The [RSI Divergence Detector](/reviews/rsi-divergence-detector/) is fine as the second opinion.

Stack two engines and require agreement if you want fewer, better signals. OBV plus MACD agreeing on a lower low was the cleanest combination in our sample.

## Bottom Line

If you're choosing one divergence engine for a scanner, choose MACD for coverage or OBV for quality. RSI divergence is the popular answer and the weakest performer in this test — not because the math is wrong, but because a bounded oscillator loses resolution exactly where divergence matters most.

No divergence arrow is a trade. It's a question: is this move exhausting? Answer it with structure and volume, then size accordingly.

---

*All indicators tested on TradingView. Build your own comparison layout with a [TradingView Pro account here.](https://www.tradingview.com/?aff_id=166324)*

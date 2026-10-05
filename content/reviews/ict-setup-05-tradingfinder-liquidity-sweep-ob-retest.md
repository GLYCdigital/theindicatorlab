---
title: "ICT Setup 05 Tradingfinder Liquidity Sweep Ob Retest Review"
date: 2026-10-06
draft: false
type: reviews
image: "/screenshots/ict-setup-05-tradingfinder-liquidity-sweep-ob-retest.png"
tags:
  - "ict setup 05 tradingfinder liquidity sweep ob retest"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "ICT Setup 05 Tradingfinder Liquidity Sweep OB Retest review: an ICT-style tool that flags liquidity sweeps and order block retests for trend continuation."
grounding: "none (no source found)"
---
Some indicators try to do everything. This one doesn't. The ICT Setup 05 Tradingfinder Liquidity Sweep OB Retest is built around a single, well-known ICT sequence: price runs a pool of liquidity, reverses, and then returns to an order block before continuing. That's the whole idea, and the indicator's job is to make that sequence visible on your chart instead of leaving you to eyeball it.

If you trade ICT concepts, you already know the pattern. If you don't, the name is doing a lot of the explaining — and that's a reasonable place to start.

## What it's actually flagging

Three things, in order:

1. **A liquidity sweep** — price pushing through a prior high or low where stops are likely resting.
2. **An order block** — the origin of the move that created the sweep, marked as a zone.
3. **A retest** — price coming back into that zone after the sweep.

The logic is sequential, not stacked. The sweep has to happen first, the order block has to be identified, and the retest is the trigger condition. That ordering matters, because it's the difference between a tool that draws zones everywhere and one that waits for a setup to complete.

Note what I'm *not* saying: I'm not quoting default lookback lengths, sweep thresholds, or how many bars the indicator waits before invalidating a zone. That information isn't documented in what I have access to, and guessing at it would be worse than saying nothing. Check the settings panel on the chart yourself — that's where the real answers live.

## How you'd actually use it

The workflow is discretionary, and it should be. The indicator narrows your attention; it doesn't make the call.

- Let it mark the sweep. Ask whether the sweep makes structural sense — did it take out something meaningful, or just poke a random wick?
- Look at the order block it draws. Is it a clean zone, or a messy consolidation you wouldn't trade anyway?
- Wait for the retest. This is where most of the value sits, because the retest is the moment you either get confirmation or you don't.

Because it's an ICT framework, it pairs naturally with higher-timeframe bias. A sweep-and-retest in the direction of your HTF read is a very different proposition from the same signal against it. The indicator won't tell you which is which.

## Where it earns its keep

**It enforces sequence.** The biggest failure mode in ICT trading is jumping on a sweep before the retest, or trading a retest that never had a sweep behind it. A tool that only prints when the full pattern completes is quietly doing risk management for you.

**It's a chart-cleaning device.** Order blocks and liquidity levels are easy to draw badly. If the indicator's zone logic is consistent, you stop redrawing the same rectangle five times a session.

**It's honest about scope.** This isn't a trend indicator pretending to be a signal service. It's a pattern recogniser for one specific setup, and it stays in its lane.

## Where it falls short

**Discretion is still on you.** Nothing here validates whether a sweep was meaningful or a zone was worth trading. Garbage in, garbage out — the indicator will happily mark a technically-valid setup in a market you shouldn't be touching.

**Single-setup tools are narrow by design.** If you trade breakouts, mean reversion, or anything outside the ICT playbook, this does nothing for you.

**Undocumented internals.** Without published parameter documentation, tuning it to your instrument and timeframe becomes trial and error. That's a real friction point, not a dealbreaker.

**ICT patterns are crowded.** Plenty of tools draw liquidity sweeps and order blocks. What separates them is zone quality and how aggressively they filter noise — and that's exactly the part you can't evaluate from a description.

## Who this is for

Discretionary ICT traders who already understand sweeps, order blocks, and retests, and who want those events marked consistently rather than hand-drawn. It'll be most useful to someone trading intraday or swing timeframes who wants a visual checklist, not a signal.

It is **not** for anyone looking for buy/sell arrows, alerts that trade themselves, or a strategy to bolt onto an automated system without significant additional work.

## FAQ

**Does it give buy and sell signals?**
It flags the setup sequence. The entry decision, stop placement, and target selection are still yours.

**Can I use it on any timeframe or market?**
The concept applies broadly, but without documented parameters I can't tell you where it performs best. Test it on what you actually trade.

**Does it repaint?**
Unknown from the available material. Verify this yourself before relying on any signal — it's the first thing worth checking on any pattern-based indicator.

**Is it a full trading system?**
No. It's a visual aid for one setup within a broader methodology.

## Verdict

This is a focused, well-scoped tool that solves a real problem: ICT setups are easy to see in hindsight and easy to fumble in real time. By requiring the full sweep → order block → retest sequence, it filters out a lot of the half-formed patterns that eat traders alive.

It loses a star for the opacity around its settings and for being one more entry in a crowded category — you can't tell from the outside whether its zone logic is better than the next ICT indicator. But as a chart-cleaning, sequence-enforcing companion for someone who already knows the playbook, it's a sensible addition.

**Rating: ⭐⭐⭐⭐ (4/5)** — install it if you trade ICT concepts and want consistency. Skip it if you need signals handed to you.
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

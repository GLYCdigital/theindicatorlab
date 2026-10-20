---
title: "Liquidity Sweeps vs Stop Hunts — Reading Where the Market Hunts Your Stops"
description: "Not every wick below a low is a liquidity sweep. How to tell a stop hunt from a genuine break, and how to position instead of getting stopped out."
date: 2026-10-21
draft: false
type: blog
image: "/screenshots/liquidity-sweep.png"
tags:
  - liquidity sweep
  - stop hunt
  - smart money
  - market structure
  - price action
author: "The Indicator Lab"
---

Every trader learns the word "stop hunt" within six months. Almost nobody learns the difference between a stop hunt and a genuine break until they've been whipsawed a few dozen times.

Here's the uncomfortable truth: a wick below a swing low is not a liquidity sweep. It's just a wick. A liquidity sweep is a *sequence* — price reaching into a pool of resting orders, taking them, then failing to hold the level. Look at only the first half and you're trading noise with a story attached.

This post is about reading the whole sequence — and about where to put your stop so the hunt doesn't matter.

![Liquidity sweep marked on a TradingView chart](/screenshots/liquidity-sweep.png)

## Stop Hunt vs Sweep — the terminology trap

Most articles use "liquidity sweep" and "stop hunt" interchangeably. They're related but not identical, and the distinction changes how you trade it.

A **stop hunt** is the *motive*. Resting stop-losses above a high or below a low are fuel; somebody pushed price into them to fill size.

A **liquidity sweep** is the *event*. Price trades through the level, triggers the stops, then reverses — leaving the breakout crowd trapped on the wrong side.

A stop hunt tells you liquidity was taken. A sweep tells you it was taken *and rejected*. Only the second is a signal.

## The three things that separate a sweep from a break

Every indicator in this category is trying to answer one question: did price actually accept above/below the level, or did it just visit?

Three tells, in order of reliability:

**1. Close location, not wick size.** A real break closes beyond the level and builds from there. A sweep closes back on the origin side. Long wicks with a close back inside the prior range are the classic signature — but the close is the decision, not the wick.

**2. Time spent beyond the level.** Sweeps are fast. If price is still hanging around outside the level three or four candles later, you're not looking at a stop hunt. You're looking at a breakout that hasn't decided to run yet.

**3. What happens on the retest.** After a sweep, price reverses and often retests the swept level from the other side. If that level now *holds* against the trap direction, the sweep is confirmed. If price slices straight back through it, the original break was real.

Most "liquidity grab" indicators only score tell #1, and some only look at the wick. That's why they light up on every reversal candle in a ranging market.

## Why most sweep indicators give you false positives

The failure mode is structural. A tool that flags "price broke a recent low" will fire on every breakdown, whether or not anything reverses. Sensitivity settings trade one problem for another: tighten the lookback and you catch micro-sweeps with no follow-through; loosen it and you miss the ones that matter.

The [Liquidity Sweep Tracker review](/reviews/liquidity-sweep-tracker-smart-money-stop-hunts) covers this directly — the tracker is genuinely good at making an abstract concept visible, but it's a *flagging* tool, not a direction. If you take every marker as an entry, the ranging markets will eat you.

The more rigorous version adds structural confirmation: the sweep must be followed by a break of the opposing structure. That's what [Market Structure Pro](/reviews/market-structure-pro) labels after a liquidity grab — two events chained together are far more informative than either alone. [Liquidity Sweep](/reviews/liquidity-sweep) requires a reversal candle close and explicitly does not repaint confirmed labels. That matters: if a label can appear retroactively, you can't evaluate the tool's real hit rate.

## Where to actually put your stop

This is the practical payoff, and it's the part the "smart money" content skips.

You cannot hide a stop from a market that's hunting liquidity. It sits at a predictable distance below a predictable level. What you *can* do is stop placing it where the pool is.

- **Don't put stops directly under the obvious swing low.** That's the pool. Put them beyond the sweep's extreme — under the wick that swept you, not under the level that got swept.
- **Use the sweep as your entry, not your exit.** Wait for the reclaim close, enter on the retest, and stop out below the sweep low. You're now positioned *with* the hunt instead of in front of it.
- **Size down instead of tightening.** A wider stop with smaller size survives the hunt and keeps the same risk. A tight stop with full size is a donation.

Combine that with levels that already matter — [Liquidity Levels](/reviews/liquidity-levels) plots the pools themselves — and you have a workflow: identify the pool, wait for the sweep, confirm with structure, enter on the retest.

## Bottom line

A sweep is not a wick; it's a wick *plus* a rejected close *plus* follow-through. Trade the sequence, not the spike. If your stop sits exactly where every other trader's stop sits, no indicator will save you — moving it is the fix.

**Want the direction question answered for you?** The [Lab Report](/the-lab-report/) reads 123 indicators across 20 markets every 15 minutes and sends one consensus verdict to your phone, and [Lab Edge](/lab-edge/) adds weekly 166-market signal sets. 7-day free trial, cancel anytime.

---

*All indicators shown on live TradingView charts. Running sweep and structure tools side by side needs a plan that supports multiple indicators per chart — [compare TradingView plans here](https://www.tradingview.com/?aff_id=166324).*

---
title: "Supply and Demand Zones: The Complete Trading Framework"
description: "Supply and demand zones trading: how to draw them properly, why fresh zones beat tested zones, and the zone lifecycle that filters bad setups."
date: 2026-08-31
draft: false
type: blog
image: "/screenshots/supply-and-demand-zones.png"
tags:
  - supply and demand zones
  - support resistance zones
  - S&D strategy
  - trading strategy
  - tradingview
  - guide
author: "The Indicator Lab"
---

## Everyone Draws Supply and Demand Wrong

Here's the uncomfortable truth about supply and demand zones: most traders draw them wrong, trade them wrong, and then blame the concept when the zone fails. It wasn't the concept that failed — it was the zone.

A support line is a price level. A demand zone is an **area of institutional interest** — a place where buyers stepped in with enough force to reverse a move. The difference matters, because a zone has a lifecycle: it's born fresh, gets tested, and eventually breaks. Most articles stop at "draw a rectangle where price reversed." That's where the mistakes start. Here's the full framework.

## Part 1: How to Draw a Zone Properly

The rule is simple: **the zone starts at the origin bar — the first aggressive candle of the move — not at the reversal low.**

When price rallies hard off a low, the demand zone is the base of that move: the origin bar plus the last consolidation candle before the breakout. Not the wick, not the extreme low. The zone should be tight enough that it means something (a zone spanning 200 points on BTC is noise) but wide enough to survive minor wick-throughs.

Two types of bases:

- **Rally-Base-Rally (RBR)**: uptrend, pause, continuation up → demand zone.
- **Drop-Base-Rally (DBR)**: downtrend, pause, reversal up → demand zone.

The distinction matters because DBR zones — where price has already proven it can flip the script — are statistically stronger than simple continuation bases.

The [Supply And Demand Zones](/reviews/supply-and-demand-zones/) indicator automates this: it scans significant swings, draws zones on the swing bar, and fades them on a clean break. In my testing it drew zones tighter than most manual methods and, critically, it doesn't repaint.

![Supply and demand zones drawn on a TradingView chart](/screenshots/supply-and-demand-zones.png)

## Part 2: Fresh vs. Tested — Which Holds Better

This is the piece most articles miss, and it's the one that makes money: **fresh zones beat tested zones, and the first test is the trade.**

A fresh zone has never been touched. When price returns to it, everyone who missed the original move sees their entry — and the institutions that built the zone defend it. That first reaction is the highest-probability trade you'll get from a zone.

A tested zone has already produced a bounce. It's still tradable — but each touch weakens it. By the third touch, you're not trading supply and demand anymore, you're trading a well-worn support level that's statistically likely to break.

The rule I trade: **first test = full position. Second test = half position. Third test = watch, don't trade.**

This is why zone freshness matters more than zone size. A tight, fresh zone beats a massive, thrice-tested one every time.

## Part 3: Ranking and Filtering Zones

Not all zones are equal. When you have five zones on your chart, rank them:

1. **Time since creation** — the fresher, the better.
2. **Number of touches** — 0-1 touches = premium, 2+ = discount.
3. **Zone strength** — a demand zone born on high volume with a strong origin bar beats a weak-volume drift base.
4. **Location** — a zone at the edge of a range is worth more than one buried in the middle.

This is where [Market Structure Pro](/reviews/market-structure-pro/) earns its keep. It maps the HH/HL and LH/LL framework so you know whether you're buying at a higher low (strong) or into a lower high (weak). A demand zone that aligns with a higher low in an uptrend is the A+ setup. A zone fighting the trend is a C.

And if you want to understand *why* zones form, [Liquidity Levels](/reviews/liquidity-levels/) shows you where the resting orders are. Supply and demand zones are where price *reacted*; liquidity levels are where the fuel sits. When a fresh zone overlaps a liquidity pool, that's the confluence institutional traders actually trade.

## Part 4: The Zone Lifecycle and When to Ignore

Every zone follows the same path: **fresh → tested → broken → dead.**

The hard part isn't drawing the zone — it's accepting when it's dead. A zone is broken when price closes beyond it and doesn't return. At that point it flips: a broken demand zone becomes supply on retest. That flip is a legitimate trade, but it's a different setup — don't confuse it with "buy the zone."

Ignore zones when:

- Price has touched the zone 3+ times.
- The zone is fighting the daily trend.
- You can't see the origin bar clearly (choppy, overlapping candles = no base).

## Bottom Line

Supply and demand trading isn't about drawing rectangles — it's about trading the lifecycle: fresh zones, early tests, and quick exits when the story changes. Draw from the origin bar, rank by freshness, and let the zone tell you when it's done. For an automated version of the framework, start with the [Supply And Demand Zones](/reviews/supply-and-demand-zones/) review, then pair it with [Market Structure Pro](/reviews/market-structure-pro/) for context.

---

*All zones tested on TradingView daily and 4-hour charts. Want to run this framework with multiple indicators on one layout? [Get TradingView Pro.](https://www.tradingview.com/?aff_id=166324)*

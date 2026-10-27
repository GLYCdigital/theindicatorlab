---
title: "Funding Rate + Open Interest — The Crypto Positioning Edge"
description: "Funding rate tells you who is paying. Open interest tells you if they're adding. Combine both to spot crowded crypto trades before the squeeze."
date: 2026-10-28T03:30:00+08:00
draft: false
type: blog
image: "/screenshots/funding-rate.png"
tags:
  - funding rate indicator
  - open interest trading
  - crypto positioning
  - funding rate strategy
  - crypto futures
author: "The Indicator Lab"
---

Most crypto traders read funding rate as a sentiment gauge: positive means bullish, negative means bearish. Then they get stopped out when price grinds against a crowded book for three days. The problem isn't the indicator — it's reading one number in isolation. Funding shows *who is paying to hold a position*. Open interest shows *whether that position is new money or an exit*. Neither answers the question that matters: is this crowd growing or unwinding?

Read them together and that becomes answerable at a glance.

## What Each Series Actually Measures

![Funding rate indicator on a perpetual futures chart](/screenshots/funding-rate.png)

Funding is a periodic payment between longs and shorts on perpetual futures, a direct function of the perp-spot premium. When perps trade above spot, longs pay shorts — the market charges you for being long. Most major venues run a 0.01% per 8 hours baseline, roughly 11% annualized. Sustained funding above 0.03% per 8h is unusual; above 0.05% and you're looking at a leverage premium, not a trend signal.

Open interest is total contracts outstanding — a stock, not a flow. But its *change* is flow: rising OI means new positions opening, falling OI means positions closing. Neither series has direction on its own; they only become directional combined with each other and with price.

## The Four-Quadrant Read

This is the whole framework. Cross the sign of funding against the direction of OI change and you get four states, each with a distinct trade implication.

**OI up, funding positive.** New longs opening and paying. A crowded long. Trend-following works, but risk is asymmetric — the fuel for a long squeeze is being loaded. When funding prints an extreme while OI hits a local high, you're late, not early.

**OI up, funding negative.** New shorts opening and paying. Crowded short, the classic squeeze setup. Price grinding up against rising OI and negative funding is the most reliable squeeze pattern in crypto: the exit door is narrow and everyone faces the same way.

**OI down, funding positive.** Positions closing while longs still pay. Short covering, not new buying — no new money behind the rally. Most traders read it as strength and buy a dead-cat bounce.

**OI down, funding negative.** Longs capitulating. Selling is exit flow, not new short pressure. Downside continuation odds are lower than the price action suggests.

Two quadrants are continuation. Two are exhaustion. The chart looks similar in all four — which is why price alone can't separate them.

## Reading It on TradingView

Neither series belongs on the price axis — both get their own pane.

For funding, [the Funding Rate indicator](/reviews/funding-rate/) plots the per-8h rate as a histogram with a zero line. The zero line is the only level that matters. Watch for a sign shift while OI is still rising; that's a regime change, not noise.

For OI, [the Open Interest review](/reviews/open-interest/) covers plotting raw contract count. The useful transform is rate-of-change: OI up 5% over 24 hours alongside a 2% price move means the move is financed by new leverage. OI flat during a 2% move means spot or marked-up positions are driving it — much weaker.

Stack price, funding histogram, and OI line as three panes. Ninety seconds to set up, and it changes how you read every breakout.

## Where the Crowd Gets Trapped

![Open interest tracker showing contract count and trend](/screenshots/open-interest.png)

The highest-value signal in this pair is divergence, and almost nobody writes about it.

Price makes a higher high. OI makes a lower high. Funding flips negative. The rally is running on fewer positions while shorts begin to pay — a configuration that resolves violently, usually lower. You don't need to predict it, just not be the last long.

The mirror case: price makes a lower low, OI makes a lower low, funding goes deeply negative. Capitulation into a vacuum, and often the fastest move of the month — with most traders positioned against it.

Cross-reference [liquidation levels](/reviews/liquidation-levels/) for where forced exits cluster. Funding and OI tell you the crowd exists; liquidation heatmaps tell you where it dies. Extreme funding plus high OI plus a dense cluster 3% below spot isn't "short the top" — it's "expect a wick into that cluster, then reassess."

Add [CVD](/reviews/cvd/) as tiebreaker. Rising OI with flat CVD means positions opening without aggressive buying — passive accumulation or market maker hedging. Rising OI with rising CVD is real directional aggression.

## The Limits Worth Knowing

Open interest is reported per exchange and aggregated feeds lag by minutes; on illiquid alts the number is noisy enough to mislead. Funding rates are venue-specific, and both series are public — so the crowd watching them is large.

That last point matters most. These indicators don't give you an information edge. They give you a *positioning* edge: a mechanical way to tell whether a move has fresh leverage behind it or is just old positions changing hands. That's worth more than any entry trigger, because it tells you what happens *after* you're in.

---

**Want it automated?** [The Lab Report](https://theindicatorlab.com/the-lab-report/) runs 123 indicators across 20 markets, including crypto funding and OI positioning. [Lab Edge](https://theindicatorlab.com/lab-edge/) covers 166 markets with weekly signals.

---
title: "Liquidation Heatmaps — Trading the Cascade"
description: "Liquidation heatmaps show where leveraged positions die, not when. Read the cascade in three phases and time entries off exhaustion instead of the break."
date: 2026-10-30T03:30:00+08:00
draft: false
type: blog
image: "/screenshots/liquidation-levels.png"
tags:
  - liquidation heatmap
  - liquidation levels trading
  - crypto liquidation cascade
  - open interest
  - funding rate
author: "The Indicator Lab"
---

Almost every liquidation heatmap article explains the same thing: bright bands are where positions get liquidated, price gravitates toward liquidity, so trade toward the bright band. Then you buy the band, price slices through it without slowing, and you learn the hard way that a heatmap is a map of *fuel*, not of *direction*.

The gap in the standard coverage is timing. A dense cluster tells you where energy is stored. It says nothing about when it releases, or whether it releases at all. Get that part wrong and the heatmap becomes confirmation bias with pretty colors.

## What the Heatmap Actually Plots

![Liquidation levels indicator showing clustered forced-exit bands](/screenshots/liquidation-levels.png)

Liquidation heatmaps are not order book data. They're a model. The tool takes open interest, entry prices, and leverage tiers, then estimates at what price each cohort of positions gets forcibly closed — longs stacked below spot, shorts stacked above it. Bands get colored by side and weighted by estimated size.

The output is an *estimate of positioning*, refreshed as OI and price move — not a live feed of resting orders. It will be wrong in detail and roughly right in shape. Trade the shape.

Why clusters form where they do is mechanical. Liquidation price is a function of entry and leverage. Traders entering the same breakout at the same round number with similar leverage tiers produce numerically identical liquidation prices. Add exchange maintenance-margin steps — where a small move pushes a whole tier into liquidation — and you get dense bands rather than smooth gradients.

## The Cascade in Three Phases

This is the part most guides skip. A liquidation cascade isn't one event; it's a sequence, and each phase offers a different trade.

**1. The probe.** Price drifts into the edge of a band on declining volume. Retail reads this as a setup and adds in the direction of the move. Open interest climbs.

**2. Forced exits.** The first tier of liquidations triggers, market sells hit the book, price drops, which triggers the next tier. Open interest falls fast. This is the violent candle — the one that looks like a breakdown and is actually the most dangerous place on the chart to enter. You are buying or selling into a mechanical, price-insensitive flow.

**3. Exhaustion.** The cascade runs out of positions to liquidate. Open interest has collapsed, funding snaps toward neutral or flips, and price wicks and reclaims. This is where the edge lives.

The actionable rule: never trade phase two. Trade the transition into phase three.

## Timing Entries Off Exhaustion

![Open interest tracker confirming cascade exhaustion](/screenshots/open-interest.png)

The confirmation sequence I want before touching a cascade:

- **Open interest drops sharply** during the move into the cluster — the fuel is being consumed, not replenished.
- **Price wicks through the dense band and closes back above (or below) it.** The band failed to hold price. That failure is information: the positions that were supposed to defend that level are gone.
- **Funding normalizes.** Extreme funding collapsing toward baseline means the crowded side has been cleaned out.
- **The first retest holds.** Enter on the reclaim of the band, not on the wick.

The first move after a cascade is usually a violent snap back into the band; the second leg is the tradeable one. Size it as a *reaction*, not a trend — a cascade doesn't change the higher-timeframe regime, it resets positioning inside it.

Setups like this are visible in [Liquidation_Levels](/reviews/liquidation-levels/), which plots exchange-sourced clusters with thickness scaled to estimated size. For a lighter-weight estimate on BTC and ETH perps, the [Liquidation Level Estimator](/reviews/liquidation-level-estimator/) draws single long/short zones with adjustable aggression — faster to read, coarser, better suited to scalps than to swing entries.

## The Confirmation Pair

A heatmap alone can't tell you whether the crowd is still growing. [Open interest](/reviews/open-interest/) is the direct check: rising OI into a band means the fuel is being restocked and the cascade hasn't happened; falling OI means it already did.

[Funding rate](/reviews/funding-rate/) tells you how badly the crowded side is paying to stay in. Deeply negative funding plus a dense long-liquidation band below spot is a loaded spring — but it releases on its own schedule, not yours. Funding shows the pressure; the heatmap shows the release valve; OI tells you which one just fired.

## Where This Model Breaks

Heatmaps are venue-specific — Binance's clusters aren't Bybit's, and aggregators blur both. In a strong trend, dense bands get consumed without any reversal: price just eats through them. That's why the exhaustion filter matters more than the cluster. A band with no OI contraction behind it is a level, not an event.

Use the heatmap to answer "where will it get violent." Use OI and funding to answer "is it over." Only then does the entry exist.

---

**Want it automated?** [The Lab Report](https://theindicatorlab.com/the-lab-report/) runs 123 indicators across 20 markets, including crypto positioning and liquidation levels. [Lab Edge](https://theindicatorlab.com/lab-edge/) covers 166 markets with weekly signals.

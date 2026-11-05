---
title: "Monte Carlo Simulation for Traders — Stress-Testing Your Equity Curve"
description: "Monte Carlo trading done right: resample your trade sequence, not the price, and read drawdown probability instead of a single forecast number."
date: 2026-11-06
draft: false
type: blog
image: "/screenshots/monte-carlo-simulator.png"
tags:
  - monte carlo trading
  - equity curve simulation
  - drawdown probability
  - risk management
  - backtesting
  - guide
author: "The Indicator Lab"
---

Nearly every Monte Carlo indicator on TradingView does the same thing: it simulates price paths forward and draws a fan chart. Pretty, but it's answering the wrong question. You don't need to know where the asset might go. You need to know whether your account survives the trip.

Same math, better target: resample your trades instead of the price.

![Monte Carlo Simulator percentile fan chart on TradingView](/screenshots/monte-carlo-simulator.png)

## Price Paths vs. Trade Paths

A price simulation assumes returns are independent and roughly lognormal, then generates thousands of alternate futures. That's useful for one narrow job — setting a stop wider than the 90th-percentile noise band — and mostly useless beyond it, because markets trend, cluster, and gap. The [Monte Carlo Simulator review](/reviews/monte-carlo-simulator/) makes the same point: treat it as a volatility framework, not a crystal ball.

Your equity curve has a property price paths don't: its inputs are *already measured*. Every trade in your backtest has a real R-multiple. You don't need to model them — you need to reorder them.

## Resample the Sequence, Not the Asset

Take your list of trade results in R. Draw them back in random order, with replacement, until you've rebuilt a full-length run. Do that 10,000 times. You now have 10,000 equity curves built from the exact edge you measured, differing only in sequence.

This is a bootstrap, and it isolates the one variable a backtest can never show you: order. Expectancy is identical across all 10,000 paths. The experience of trading them is not. That gap is sequence risk, and it's the reason a profitable system still blows up traders who were sized for the average path instead of the bad one.

One refinement: use block bootstrap. Resampling trade-by-trade destroys streaks, and streaks are exactly what hurts. Sample in blocks of 5-10 consecutive trades to keep some of the clustering intact.

## The Three Numbers That Matter

I resampled a 45% win rate, 2R average winner, 300 trades, 10,000 paths — a good trend-following profile, not a fantasy one:

| Risk/trade | Median max DD | 95th pct max DD | P(DD ≥ 20%) | 5th pct terminal |
|---|---|---|---|---|
| 1% | 10.5% | 16.6% | 1.3% | 1.8× |
| 2% | 20.0% | 30.8% | 50.5% | 3.1× |
| 5% | 43.9% | 62.3% | 100% | 10.5× |

Same trades in every row. Only the sizing changed. Read the columns in this order:

**P(drawdown ≥ X)** — the probability question. At 2% risk there is a coin-flip chance of a 20% drawdown somewhere in 300 trades. That's not a tail event, that's the base case.

**95th percentile max drawdown** — what you must be able to sit through without modifying the system. If 30% is unlivable, 2% risk is too big, full stop. The [equity curve analyzer](/reviews/equity-curve-analyzer/) is the tool for measuring your real historical drawdown distribution before you simulate anything.

**5th percentile terminal equity** — the bad-but-not-catastrophic outcome. Not the median. The median flatters you, because half of all paths are better than it and you only get one path.

## The Trap in Terminal Wealth

Look at the 5% row and you'll see why this analysis gets ignored. The 5th-percentile terminal outcome is still 10× the account. On terminal wealth alone, aggressive sizing looks free.

But that 10× doesn't come with the median path — it comes with a 62% drawdown at the 95th percentile and a *guaranteed* 20% drawdown. Terminal wealth and path pain are drawn from the same distribution and you don't get to pick. If you'd cut size at the bottom of a 62% hole, your real terminal result is the one where you stopped, not the one the table shows. The [position size calculator](/reviews/position-size-calculator/) is how you convert an acceptable drawdown into an actual risk-per-trade number.

## Running It Without Fooling Yourself

Rules that keep the output honest:

1. **Simulate R-multiples, not currency.** Dollar P&L scales with account size and hides the edge.
2. **10,000 paths minimum** before quoting a 5th percentile. Below that, the tail is noise.
3. **Use the trades your backtest actually produced**, not your expected win rate. If the [backtesting dashboard](/reviews/backtesting-dashboard/) shows one symbol carrying the whole result, resample per symbol and find out how much of the edge is concentration.
4. **Run it after walk-forward, not instead of it.** Monte Carlo can't tell you whether the edge is real — it assumes it is. The [walk-forward guide](/blog/walk-forward-analysis-testing-a-strategy-without-fooling-yourself/) settles that question first.
5. **Report the distribution, never one number.** "Max drawdown is 12%" is meaningless. "Median 12%, 95th percentile 31%" is a decision.

The [Strategy Forecast Engine](/reviews/strategy-forecast-engine/) is the forward-looking counterpart — it estimates the environment; Monte Carlo estimates your survival inside that environment. Use both and you stop guessing which one you'll get.

The question was never where the market goes next. It was how deep the hole gets before you're right — and whether you're still holding when it does.

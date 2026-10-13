---
title: "Pine Script for Beginners: Writing Your First Indicator"
description: "A no-nonsense Pine Script tutorial: build your first moving average crossover indicator on TradingView, line by line, no coding background needed."
date: 2026-10-14T03:00:00+08:00
draft: false
type: blog
image: "/screenshots/moving-average-cross.png"
tags:
  - pine script tutorial
  - tradingview custom indicator
  - write pine script
  - pine script v5
  - indicator review
author: "The Indicator Lab"
---

Every "Pine Script tutorial" opens with a wall of code and assumes you already know what a variable is. This one doesn't. We're going to build a working moving average crossover indicator — the same logic behind the [Moving Average Cross](/reviews/moving-average-cross/) tool — in about fifteen lines, and understand every single one of them.

## What Pine Script Actually Is

Pine Script is TradingView's own language. It lives inside the platform, runs on their servers, and needs zero setup — no Python, no installs, no broker API. You write it in the Pine Editor (the bottom panel of any chart), press "Add to chart," and your script draws on the price chart immediately. That's the entire workflow. If you can read a chart, you can learn this.

## Step 1 — Open the Editor and Start a Script

Open any chart, click **Pine Editor** at the bottom, then **Open → New indicator**. Delete the placeholder code. The only line you must keep is the first one:

```
//@version=5
```

That tells TradingView which language version to use. Everything else is yours.

## Step 2 — Name the Indicator and Define Inputs

```pine
//@version=5
indicator("My First MA Cross", overlay=true)

fastLen = input.int(9,  "Fast MA Length")
slowLen = input.int(21, "Slow MA Length")
```

- `indicator()` is the title that shows in your chart legend.
- `overlay=true` means draw on top of price. Set it to `false` and you'd get a separate sub-panel.
- `input.int()` creates a settings box. Change the 9 and 21 later without touching code — from the gear icon on the chart.

This is the part beginners skip, and it's the part that makes a script reusable instead of a one-off.

## Step 3 — Calculate the Moving Averages

```pine
fastMA = ta.sma(close, fastLen)
slowMA = ta.sma(close, slowLen)

plot(fastMA, color=color.blue,   title="Fast MA")
plot(slowMA, color=color.orange, title="Slow MA")
```

`ta.sma(source, length)` is a built-in function — "simple moving average of this source over this many bars." `close` is a built-in variable holding the closing price of every bar. One line, two averages, done. Want an exponential average instead? Swap `ta.sma` for `ta.ema` — the same choice you're weighing in our [EMA Crossover review](/reviews/ema-crossover/).

![Fast and slow moving averages plus crossover markers plotted on a TradingView chart](/screenshots/moving-average-cross.png)

## Step 4 — Fire the Crossover Signal

```pine
bullCross = ta.crossover(fastMA, slowMA)
bearCross = ta.crossunder(fastMA, slowMA)

plotshape(bullCross, title="Buy",  style=shape.triangleup,   location=location.belowbar, color=color.green, size=size.small)
plotshape(bearCross, title="Sell", style=shape.triangledown, location=location.abovebar, color=color.red,   size=size.small)
```

Here's the concept that trips up almost everyone. You might be tempted to write `fastMA > slowMA` to mark bullish bars. That's true for the *entire trend*, so you'd paint signals on hundreds of candles. `ta.crossover()` is true for exactly one bar — the bar where the fast line crosses above the slow line. That's the event you actually trade.

## Step 5 — Add Alerts

```pine
alertcondition(bullCross, title="MA Bull Cross", message="Fast MA crossed above Slow MA")
alertcondition(bearCross, title="MA Bear Cross", message="Fast MA crossed below Slow MA")
```

Now right-click the chart → Add alert, pick your script, and you'll get pinged when the cross happens instead of staring at a screen. This is what turns an indicator into a workflow.

## From Indicator to Strategy

Note we used `indicator()` at the top. If you want TradingView to actually backtest the crosses, change that line to `strategy()` and add `strategy.entry` / `strategy.close` calls. The [Backtesting Dashboard](/reviews/backtesting-dashboard/) review shows what to measure once you have trades — because a pretty signal on a chart means nothing until you know its win rate and profit factor.

The one mistake to avoid: don't ship a script you don't understand. Copy-pasted indicators break the moment the market changes and you can't debug them.

## Practical Takeaway

Save this script, then change one thing at a time. Flip the lengths to 20/50 and watch how signals thin out. Swap `sma` for `ema` and see the crosses arrive earlier. Every change teaches you a rule of the language, and you'll build genuine intuition faster than reading any manual.

## Bottom Line

Your first Pine Script is a moving average crossover in fifteen lines: define inputs, calculate `ta.sma`, catch the cross with `ta.crossover`, and wire up an alert. Build it once by hand — then you can read any [Moving Average Cross](/reviews/moving-average-cross/), [EMA Crossover](/reviews/ema-crossover/) or [Backtesting Dashboard](/reviews/backtesting-dashboard/) script and know exactly what it's doing.

Related reads: [Moving Average Cross review](/reviews/moving-average-cross/) · [EMA Crossover review](/reviews/ema-crossover/) · [Backtesting Dashboard review](/reviews/backtesting-dashboard/) · [Adaptive Moving Average review](/reviews/adaptive-moving-average/)

---

**A custom script is only as good as the signals behind it.** The [Lab Report](/the-lab-report/) reads 123 indicators across 20 markets every 15 minutes and sends one call, and [Lab Edge](/lab-edge/) adds weekly 166-market signal sets. [Try the Lab Report →](https://theindicatorlab.com/the-lab-report/)

*All screenshots are from TradingView. Writing and testing custom Pine Script needs a plan that supports saving scripts and multiple indicators per chart: [compare TradingView plans here](https://www.tradingview.com/?aff_id=166324).*

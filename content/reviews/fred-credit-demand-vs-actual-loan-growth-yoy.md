---
title: "Fred Credit Demand Vs Actual Loan Growth Yoy Review — Trend"
date: 2026-10-03
draft: false
type: reviews
image: "/screenshots/fred-credit-demand-vs-actual-loan-growth-yoy.png"
tags:
  - "fred credit demand vs actual loan growth yoy"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Fred Credit Demand Vs Actual Loan Growth Yoy review: a macro indicator that pairs Fed loan demand with actual bank lending to flag cycle turns."
tv_script_url: "https://www.tradingview.com/script/dlYnr1Gz-FRED-Credit-Demand-vs-Actual-Loan-Growth-Fixed-YoY/"
sources: ["https://www.tradingview.com/script/dlYnr1Gz-FRED-Credit-Demand-vs-Actual-Loan-Growth-Fixed-YoY/"]
---
Most "trend" indicators on TradingView are variations on the same moving-average math. This one isn't. Fred Credit Demand Vs Actual Loan Growth Yoy is a macro charting tool built on Federal Reserve survey data, and it's trying to show you something the price chart cannot: the gap in time between when businesses *ask* for credit and when that credit actually hits the economy.

## What it actually plots

Two series, one story. The Blue Area tracks corporate credit demand — the point where a business applies for an expansion loan and a bank executive records it on the Fed's survey. The Orange Line tracks actual loan growth, the money that eventually shows up on bank balance sheets.

The script's own description lays out the sequence cleanly. Demand spikes first. Then comes the pipeline — collateral checks, legal covenants, credit facility approval — during which no money has moved. Only in the drawdown phase do businesses pull the cash to pay contractors, buy equipment, or build. That's when the Orange Line starts to rise.

The practical consequence: the Blue Area turns months before the Orange Line follows. That lag is the entire point of the indicator.

## The three setups it's built around

The description defines three conditions worth watching, and they're genuinely useful framing.

**Bullish divergence.** Blue breaks above zero and surges while Orange is still falling or stuck low. The read: businesses have regained their appetite for risk and are queuing up capital that will land over the coming quarters. This is the rebound trigger.

**Bearish divergence.** Blue plunges toward or below zero while Orange is still near highs and looks healthy. The read: CFOs have shut their balance sheets because they see trouble coming. The Orange Line's strength is borrowed from older projects finishing out. The description flags a growth slowdown as typically six months out — that's the script author's claim, not a measured statistic, so treat it as a heuristic rather than a backtested rule.

**Full credit expansion.** Both series rising together above zero. Intent has converted into real dollar creation, and new money is circulating through the banking system.

That's the whole framework. No signals, no alerts logic promised, no entry arrows — you're reading a macro relationship and drawing your own conclusions.

## How you'd actually use it

This is not a trigger tool. It's a context tool. The sensible workflow is to keep it on a separate pane or a dedicated macro chart and check it when you're forming a medium-term view — not when you're timing an entry.

The bullish divergence condition is the one with the clearest actionable shape: demand turning up while actual lending is still depressed tells you capital is in the pipeline. The bearish version is the one worth respecting most, because it's a warning that shows up while everything else looks fine. That's the scenario where a lagging indicator actively misleads you, and this tool exists to catch it.

Because both series are year-over-year, they're inherently slow. Nothing here will help you on a daily or intraday chart.

## Pros and cons

**Pros:**
- Genuinely differentiated. It's built on Fed survey data, not price transformations, so it adds information your chart doesn't already contain.
- The demand-versus-actual framing is conceptually sound and the description explains the mechanism rather than just asserting a signal.
- The three named conditions give you a repeatable way to read the two lines instead of eyeballing them.
- Good for macro regime awareness — knowing whether credit is expanding or contracting is useful context regardless of what you trade.

**Cons:**
- Lagging by design. Both lines are YoY, and one of them is structurally behind the other. This is not a timing tool.
- The "six months away" framing for recession warnings is a rule of thumb, not a measured outcome. Don't treat it as precise.
- It says nothing about which assets, sectors, or instruments respond — you have to make that mapping yourself.
- Macro data arrives on a slow release schedule, so the chart updates infrequently. If you want fast feedback, this isn't it.
- No documented inputs, thresholds, or alert conditions to tune. What you see is what you get.

## Who it's for

Macro-oriented swing and position traders, and anyone who trades rate-sensitive sectors — financials, industrials, real estate, small caps — where credit availability is a genuine driver. Also useful for anyone building a top-down thesis and wanting a credit-cycle input that isn't just another yield curve chart.

It is not for day traders, scalpers, or anyone who needs a signal to fire.

## FAQ

**Does it give buy or sell signals?**
No. It plots two macro series and describes how to interpret their relationship. Execution is on you.

**What timeframe should I use?**
The data is year-over-year, so it's a medium-to-long-horizon tool by construction. The script doesn't specify a recommended chart timeframe.

**Is the six-month recession warning reliable?**
The description presents it as a general pattern, not a measured hit rate. Treat it as directional guidance.

**Can I change the inputs?**
The source material doesn't document any configurable settings, so assume the defaults are the design.

## Verdict

This is a rare thing on TradingView: an indicator that isn't repackaging price. The demand-versus-actual-loan-growth relationship is a real macro mechanic, and the lag between the two lines is the kind of structural insight that's hard to get from a chart. It loses a star for being slow, untunable, and light on specifics — but if you trade macro or rate-sensitive names, it earns its pane.

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

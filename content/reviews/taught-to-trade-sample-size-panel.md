---
title: "Taught To Trade Sample Size Panel Review — Trend Indicator"
date: 2026-10-04
draft: false
type: reviews
image: "/screenshots/taught-to-trade-sample-size-panel.png"
tags:
  - "taught to trade sample size panel"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Taught To Trade Sample Size Panel review: a TradingView calculator that turns your trade count and win rate into a confidence interval — and tells you if your edge is real."
tv_script_url: "https://www.tradingview.com/script/qZkLfGBu-Taught-to-Trade-Sample-Size-Panel/"
sources: ["https://www.tradingview.com/script/qZkLfGBu-Taught-to-Trade-Sample-Size-Panel/"]
---
Most indicators on TradingView draw something. This one draws nothing. It sits in a panel, asks you for two numbers, and does arithmetic. That is either exactly what you need or completely useless to you, and the difference has nothing to do with the markets.

## What it actually does

The Taught To Trade Sample Size Panel takes your trade count and your observed win rate and returns the range the true rate plausibly sits in. It uses a Wilson score interval at 90, 95 or 99 percent confidence. Wilson is chosen over the textbook normal interval specifically because it behaves sensibly at small samples and at rates near 0 or 100 percent — which is where most retail track records live.

The framing question in the description is the whole point: you have 30 trades and 60 percent of them worked. Is that a real edge, or a coin flip that had a good month? The panel answers with a range, not a verdict.

## What the panel shows

Five outputs, each doing a different job:

- **True rate is between** — the Wilson interval around your observed rate at your chosen confidence level.
- **Interval width** — the gap between the two ends in percentage points, colour-coded green under 10, amber from 10 to 20, red above 20.
- **Tells apart from 50%?** — answers "Yes" only when the entire interval sits above or below 50 percent. This is the single most useful cell in the table.
- **Trades for ±10pp, ±5pp, ±2pp** — roughly how many trades it takes for the interval to shrink to that half-width at your observed rate.
- **This chart could give** — how many non-overlapping trades this chart's history could have produced at your holding period.

That last row is the one people skip and shouldn't. If the chart can only produce fewer trades than you need, no amount of backtesting on that chart will settle the question. You are not going to brute-force statistical significance out of a dataset that isn't long enough.

## The worked example is the argument

The defaults are 30 trades at 60 percent, 95 percent confidence. The true rate comes back somewhere between roughly 42 and 75 percent. That range contains 50. Narrowing it to plus or minus 5 points takes about 369 trades.

Read that again. Thirty trades at a 60 percent hit rate feels like something. It isn't evidence of anything yet, and the panel says so without hedging. That is a genuinely uncomfortable output and it is the reason this tool exists.

## How to use it

Pull the trade count and the rate from your own trade list or a strategy report. Type them in. Read the table before you read anything else about the result — before the equity curve, before the strategy description, before your own opinion of how it felt to trade. It has no alerts and draws nothing on the chart, because there is no market state to alert on. It is a calculator.

## Where it breaks down

The author is unusually candid about the failure modes, and they matter:

- It assumes every trade is an independent draw with the same underlying rate. Real trades cluster — regimes change, and trades taken close together share conditions. Both make real uncertainty **wider** than the panel shows.
- It is about a rate only. A 60 percent rate tells you nothing about win/loss size, costs, or drawdown. A strategy can be right most of the time and still lose money.
- The trades-needed rows use the normal approximation, which is rough at very small samples and near 0 or 100 percent.
- If you tried many parameter sets and kept the best, your entered rate is already inflated by selection. No interval corrects for that.
- "This chart could give" is a rough count: history length divided by holding period, ignoring gaps and time between trades.

That list is longer than most vendors would publish about their own tool, and it is the strongest signal that the maths here is not being oversold.

## Pros and cons

**Pros:** Honest, transparent statistics. Wilson instead of the naive normal interval. The selection-bias caveat is stated plainly rather than buried. The "can this chart even settle it" row prevents a whole category of wasted effort.

**Cons:** It is not a signal tool and will disappoint anyone who installed it hoping for entries. It cannot see trade clustering, so it understates real uncertainty. It says nothing about risk, sizing or expectancy. And the answer it usually gives — you need far more trades than you have — is not the answer most people are shopping for.

## Who it's for

Discretionary traders with a written trade log who want an honest read on whether their numbers mean anything. Strategy developers who want a sanity check before getting excited about a backtest. Anyone who has ever said "my system wins 60 percent" and should be asked how many trades that's based on.

It is not for anyone hunting entries, and it is not a substitute for expectancy, risk or drawdown analysis.

## FAQ

**Does it generate buy or sell signals?** No. It is an educational calculator with no alerts and no chart plotting.

**What confidence levels can I pick?** 90, 95 or 99 percent.

**Why Wilson and not the normal interval?** Because it behaves sensibly at small samples and at rates near 0 or 100 percent, where the normal approximation misbehaves.

**Can it tell me if my strategy is profitable?** No. It only addresses the rate. Win/loss size, costs and drawdown are outside its scope.

## Verdict

Four stars. It is narrow, it is unglamorous, and it will tell a lot of traders something they don't want to hear. But it does one job with real statistical rigour, states its own limitations in public, and costs you nothing but the honesty to type in your actual numbers. The star is withheld only because it is a single-purpose tool with no signal capability — if you want entries, look elsewhere.

⭐⭐⭐⭐
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

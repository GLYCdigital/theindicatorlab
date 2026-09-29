---
title: "Volume Divergence Bayesian Projection Review — Volume"
date: 2026-09-29
draft: false
type: reviews
image: "/screenshots/volume-divergence-bayesian-projection.png"
tags:
  - "volume divergence bayesian projection"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Volume Divergence Bayesian Projection review: a self-learning divergence tool that scores its own signals with Bayesian statistics and credible intervals."
tv_script_url: "https://www.tradingview.com/script/rPOx1NRY-Volume-Divergence-Bayesian-Projection/"
sources: ["https://www.tradingview.com/script/rPOx1NRY-Volume-Divergence-Bayesian-Projection/"]
---
Most divergence indicators hand you a line and a label and call it a day. You get "Bull" stamped on a swing low, and the rest is on you. Volume Divergence & Bayesian Projection takes a different route: it detects the divergence, then tracks what actually happened after each prior signal and reports the odds back to you in numbers.

That shift — from detection to feedback — is the whole point of this script.

## What it actually does

The indicator finds divergences by comparing pivots in price against pivots in a volume oscillator. When price and volume disagree, that disagreement gets classified, logged, and fed into a Bayesian engine that maintains a running posterior for each signal type.

The output is not a promise. It's a readout: a probability, a credible interval, an expected value, and an effective sample size. As shown in the chart above, the projection box on the last bar shows where past outcomes clustered (the Q25–Q75 range), with a median line marking the expected return.

## Two detection methods, four signal classes

What separates this from the usual divergence script is that it looks for disagreements in two directions:

- **Price-pivot method** — price makes a new high or low but volume fails to confirm. Classic exhaustion: the move is losing participation.
- **Oscillator-pivot method** — volume makes a new extreme but price fails to follow. Absorption: someone is quietly taking the other side.

These are genuinely different phenomena, and you can run them together or independently. Running them separately lets you compare which one behaves better on your instrument.

On top of that, four divergence classes are tracked: regular bullish and bearish (reversal signals), and hidden bullish and bearish (continuation signals). Each is learned from independently, so a weak hidden-bearish record doesn't contaminate the regular-bullish statistics.

## The Bayesian engine, in plain terms

For each signal type the script keeps two posteriors. A Beta-Bernoulli posterior answers "does this signal work?" — the probability that the expected directional move happens within N bars. A Normal posterior answers "how big is the move?" — the expected forward return, shrunk toward a prior mean so small samples don't produce absurd projections.

You can choose the prior: Uniform, Jeffreys, Skeptical, or Custom. Recency decay lets recent outcomes carry more weight than old ones. The credible interval comes from a configurable Z-score, and there's an edge filter that flags whether the interval excludes 50%.

The gate that matters most is the effective sample size (ñ = α + β). Projections don't render until the engine has accumulated enough evidence, so you won't see a confident-looking box built on two observations. That single design choice is why this tool earns a four rather than a three.

## How you'd actually use it

Add it to your instrument and timeframe, then let it run. The engine needs completed signals before it says anything useful — on a fresh chart, expect silence until the minimum sample threshold is met.

Watch the stats table across all four signal types. If one of them shows a meaningful posterior with a credible interval that excludes 50%, that's your edge on this market. If the intervals are wide or ñ is low, the honest answer is "insufficient evidence," and the indicator tells you that instead of pretending otherwise.

The projection only draws on the last bar, and its opacity scales with confidence — stronger edges are visually louder. Alerts cover the four signal types, and running two instances (one per detection method) gives you eight independent conditions.

## Pros and cons

**Pros:**
- Closes the loop between detection and outcome — rare in this category
- Explicit uncertainty: credible intervals and effective sample size, not just a probability
- Small-sample shrinkage prevents the overconfidence most "win rate" tools suffer from
- Two independent detection methods, independently toggleable
- Gating on minimum sample size is genuinely honest design

**Cons:**
- Signals are confirmed, not predictive — pivots need bars to form, so there's inherent lag
- Two methods share posteriors by default; method-specific stats require running two instances
- Requires history to be useful, which makes it a poor fit for quick discretionary scanning
- The statistical readout has a learning curve if you're not familiar with posterior language

## Who it's for

This suits systematic traders and analysts who want to know whether volume divergences carry any statistical weight on a specific instrument — and who are comfortable reading a credible interval. It's less useful for anyone wanting instant signals on a fresh chart, or for traders who want a clean visual without numbers attached.

## FAQ

**Does it predict the next move?**
No. It describes what happened after similar signals historically. The posterior is a summary of the past, not a forecast.

**Why don't I see a projection yet?**
The engine needs completed outcomes. On a fresh chart it stays gated until the minimum sample threshold is reached.

**Can I get separate stats for each detection method?**
Yes — add the indicator twice, one method per instance.

**Is the delayed signal a bug?**
No. Pivot-based detection requires bars to confirm the pivot. The delay is inherent to the method.

## Verdict

Volume Divergence & Bayesian Projection is a research tool dressed as an indicator, and that's a compliment. It refuses to give you a number until it has earned one, and it shows you the uncertainty alongside the estimate. The lag and the history requirement are real costs, but they're the price of doing divergence analysis honestly.

If you trade volume divergences and want to know whether they actually work on your market, this is one of the few tools that will tell you the truth.

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

---
title: "Monte Carlo Probability Forecaster Review — Trend Indicator"
date: 2026-11-14T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/monte-carlo-probability-forecaster.png"
tags:
  - "monte carlo probability forecaster"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Monte Carlo Probability Forecaster review: what this TradingView study actually does, who it suits, and where its honest limits lie."
tv_script_url: "https://www.tradingview.com/script/8TBCPxZp-Monte-Carlo-Probability-Forecaster/"
sources: ["https://www.tradingview.com/script/8TBCPxZp-Monte-Carlo-Probability-Forecaster/"]
---
Most TradingView indicators hand you a signal — a cross, a colour change, an arrow. This one hands you a distribution. The Monte Carlo Probability Forecaster is a study that estimates where price could plausibly sit after a chosen number of bars, by simulating thousands of possible future paths and tallying where they end up. It doesn't tell you what to do. It tells you what the recent behaviour of the instrument implies about the range of outcomes.

## What it actually does

The mechanics are straightforward, and the author documents them plainly. The script measures the logarithmic returns of the most recent bars (the Return Sample, default 200 bars). From that sample it generates future price paths bar by bar, using either a **Gaussian** model (returns drawn from a normal distribution using the recent average return and volatility) or a **Historical Resample** model (returns picked at random from the actual recent returns, which preserves fat tails, skew, and sudden large moves).

At the end of the forecast horizon, each path's final price is dropped into a price zone. The probability of a zone is simply the share of paths that finished inside it. Separately, every path is tracked throughout the forecast to see whether it touched the upside or downside target at any point — which yields "touch" probabilities alongside the "end" probabilities. That distinction is the most useful idea in the script.

## What lands on the chart

As shown above, the forecast reads as a cluster of visuals to the right of price:

- A **probability histogram** — one bar per price zone, sized by probability and labelled with its percentage and price range. The densest zone is marked "most likely."
- **Heat zones**, shading price bands across the forecast window, from red (low probability) through cyan (where paths cluster most heavily).
- A **percentile cone** built from the 5th, 25th, 50th, 75th and 95th percentiles of all paths, with the median as a solid line. It shows the plausible range widening with time — a visual reminder that uncertainty compounds.
- **Sample paths**, coloured green or red depending on whether each simulation ends above or below the start price.
- **Target lines** — dashed upside and downside targets, an optional custom level, and a dotted line at the start price.

## Settings worth understanding

The panel is dense but not confusing. **Number of Paths** goes up to 2,000, though the script automatically limits total calculation work to stay within TradingView's limits — if paths are reduced, the panel says "(reduced)," which is a welcome bit of honesty rather than a silent downgrade. **Forecast Horizon** runs from 5 to 300 bars. **Price Zones** ranges from 4 to 40, controlling how finely the final prices are bucketed.

Two toggles matter more than they look. **Keep Average Trend (Drift)** includes or removes the sample's average trend — switch it off for a neutral, volatility-only view when a strong recent run may be biasing the result. And **Update on Every Tick** is off by default, so the forecast is built from closed candles only and stays stable until the next candle closes. That's the right default for anyone using this to plan a trade rather than watch it flicker.

## How I'd actually use it

Set the horizon to your holding period first — the author's own example is 20 bars on a daily chart, roughly one trading month. Then read the histogram and the 50%/80% ranges to judge whether a target is statistically realistic inside that window. The genuinely practical step is comparing end versus touch probabilities: price often touches a level during the period without staying beyond it at the end. That's directly useful for placing take-profits and stops. Entering a specific price in the Custom Level field answers the question traders actually ask — "what are the odds we get there?"

## Pros and cons

**Pros**
- Two return models with a real conceptual difference: Gaussian for smooth assumptions, Historical Resample for instruments with frequent large or sudden moves.
- Touch probabilities, not just end probabilities — rare in retail tools and directly actionable for stops.
- Transparent about its own constraints, including the reduced-path notice and the closed-candle default.
- Open source, with a repeatable Random Seed so you can reproduce a forecast.

**Cons**
- It assumes future returns resemble the sample window. News, regime changes, and volatility shifts are invisible to it.
- Different seeds, sample lengths, and models produce different probabilities — the output is not one fixed number, and that can unsettle traders looking for certainty.
- It's calculated on the most recent bar only and is explicitly not a backtested signal, so it won't validate a strategy for you.
- The visual density may overwhelm newer users; four separate overlays plus a panel is a lot of screen.

## Who it's for

Discretionary traders who already have a thesis and want a statistical sanity check on targets and timing. Options and swing traders thinking in holding periods will get the most from the horizon setting. It is not for anyone wanting entry signals, and it is not a strategy backtester.

## FAQ

**Does it predict price?** No. The author is emphatic: the probabilities describe the model's range of outcomes, not a guarantee. It's statistics, not prophecy.

**Why did my probabilities change after reloading?** Likely a different Random Seed, a new closed candle, or a different model, sample length, or drift setting. Fix the seed for repeatable results.

**Which return model should I choose?** The source recommends Historical Resample for instruments with frequent large or sudden moves, because it preserves fat tails and skew.

## Verdict

This is a well-constructed, unusually honest statistical tool. It does one job — mapping the distribution of plausible outcomes from recent behaviour — and does it with more transparency than most scripts on the platform. The touch-versus-end distinction alone justifies a look. It loses a star because the output is inherently unstable across settings and seeds, and because it can't see the things that actually move markets. Use it to frame risk, not to outsource decisions.

**Rating: ⭐⭐⭐⭐**
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

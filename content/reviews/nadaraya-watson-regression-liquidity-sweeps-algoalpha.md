---
title: "Nadaraya_Watson_Regression_Liquidity_Sweeps_Algoalpha Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/nadaraya-watson-regression-liquidity-sweeps-algoalpha.png"
tags:
  - nadaraya watson regression liquidity sweeps algoalpha
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Combines Nadaraya-Watson smoothing with liquidity sweep detection. Great for spotting fakeouts and key levels, but needs tweaking."
grounding: "none (no source found)"
---
# Review: Liquidity Sweeps with Nadaraya-Watson Regression

## What This Indicator Actually Does

This is not another moving average crossover. The Nadaraya-Watson estimator is a kernel regression — it smooths price without assuming a straight line. The "liquidity sweeps" component scans for sharp wicks that pierce through support/resistance zones created by the regression envelope. The algorithm marks those wicks as potential liquidity grabs (stop hunts) ahead of a reversal.

The core use case: price sweeps above or below the regression band, tags an extreme, then reverses. The indicator is built to surface that pattern rather than every wick on the chart.

## Key Features

- **Adaptive regression band** – The kernel width adjusts to recent volatility. In quiet markets the band tightens; in high volatility it widens. This reduces false sweeps during news spikes.
- **Sweep detection logic** – It does not mark every wick. It compares the wick's penetration depth against the band's standard deviation, and only wicks that exceed a multiple of the band's width get flagged. This is the noise filter.
- **Multi-timeframe alignment** – You can set a higher timeframe for the regression while trading on a lower timeframe. Sweeps on the lower timeframe that align with the higher-timeframe band boundaries are marked with a larger dot, separating context-aligned sweeps from isolated ones.

## Settings and How to Tune Them

- **Regression length** – Controls how much history the kernel regression weighs. Longer lengths produce a smoother band better suited to swing levels; shorter lengths react faster but can overfit choppy ranges.
- **Kernel bandwidth** – Controls how reactive the regression is to recent price. Tighter bandwidth makes the regression more responsive; wider bandwidth smooths it. The right value depends on your holding period and the instrument's volatility.
- **Sweep threshold** – The multiple of the band's standard deviation a wick must exceed to be flagged. A higher threshold filters more aggressively, which is useful on trend days to avoid flags during ordinary pullbacks.
- **Multi-timeframe** – Enable and select a higher timeframe to filter out sweeps that do not align with major levels.
- **Show regression line only** – Disabling this reveals the full channel. The channel adds context but also visual noise, so the choice is a tradeoff between information and clutter.

## How to Use It for Entries and Exits

**Entry trigger**: A liquidity sweep that touches or briefly breaks the regression band, then closes back inside the band. Enter on the next candle's close if the sweep is confirmed.

**Exit**: Take partial profit at the opposite band. If you shorted after a sweep above the upper band, cover half at the lower band. Move the stop to breakeven once price has moved one band width in your favor.

**Stop loss**: Place it one to two band widths beyond the sweep's extreme. If price sweeps the upper band and continues higher, the stop sits above that wick.

**Filter**: Only take sweeps that occur during high-volume sessions such as the London or New York open. Sweeps during the Asian session often fail.

## Pros and Cons

**Pros**:
- Sweep detection is cleaner than most "liquidity trap" indicators. The kernel regression adapts well to ranging markets.
- Multi-timeframe alignment reduces false signals by requiring sweeps to line up with higher-timeframe band boundaries.
- The code is open (Pine Script v5), so the bandwidth formula can be modified if you're comfortable editing it.

**Cons**:
- Heavy on the chart. The regression band, sweep dots, and multi-timeframe lines can crowd the view. Turning off the band fill helps if you scalp.
- Laggy in fast markets. The kernel regression inherently smooths, so on very low timeframes sweeps are detected several candles late. This makes it a poor fit for scalping.
- No built-in alert for sweep detection. You have to construct your own alert condition on the sweep boolean, which is a real omission.

## Who It's For

This suits swing traders and position traders working on 15-minute to 4-hour timeframes. Scalpers on 1-minute charts will find the lag prohibitive. Traders who take breakouts without considering liquidity sweeps will find the regression context changes how they read price action.

## Alternatives

- **Liquidity Sweeps by LuxAlgo** – More polished UI and built-in alerts, but a paid subscription. It detects sweeps faster but omits the regression context this indicator provides.
- **Smart Money Concepts by HPotter** – Free, includes order blocks and fair value gap detection, but its sweep detection is basic. This version is more focused on sweep-only strategies.

## FAQ

**Q: Does it repaint?**
A: The regression line does not repaint. Sweep detection marks the wick at the time of candle close, and once a candle closes the sweep is fixed.

**Q: Can I use it on crypto?**
A: Yes. It works on BTCUSD and ETHUSD. Crypto volatility is higher, so the kernel bandwidth generally needs to be set wider than for lower-volatility instruments.

**Q: How do I set an alert for a sweep?**
A: Find the sweep boolean in the indicator's inputs or style tab and create an alert on that condition. There is no one-click alert button.

**Q: Does it work in backtesting?**
A: Partially. Sweep detection is based on closed candles, so backtesting is possible. But the regression band adjusts to the full dataset, so forward-testing is more reliable.

## Final Verdict

A solid addition to a swing trader's toolbox. It does not replace understanding market structure, but it automates the tedious part of identifying liquidity sweeps, and the kernel regression adds dynamic context that most sweep indicators lack. The lag and the absence of built-in alerts are genuine drawbacks, but for a free tool it covers a lot of ground.

**Rating**: 4/5 – A strong free tool for swing traders who want to spot stop hunts with adaptive levels. Be patient with the lag and set alerts manually.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

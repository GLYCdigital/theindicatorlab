---
title: "Composite_Valuation_Standard_Score Review: Settings, Strategy & How to Use It"
date: 2026-08-24
draft: false
type: reviews
image: "/screenshots/composite-valuation-standard-score.png"
tags:
  - "composite valuation standard score"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Composite_Valuation_Standard_Score review: honest take on this trend-scoring indicator. Best settings, strategy tips, pros/cons, and who should use it."
tv_script_url: "https://www.tradingview.com/script/bEc4OoWa-Composite-Valuation-Standard-Score/"
sources: ["https://www.tradingview.com/script/bEc4OoWa-Composite-Valuation-Standard-Score/"]
---
**Composite Valuation Standard Score (CVSS)** plots a single 0 to 100 line measuring how expensive the broad US equity market is against its own recorded history. It combines up to six valuation ratios through point-in-time statistics. The thesis: one valuation metric can mislead in isolation, but the average anchored z-score of several independent lenses — earnings, cyclically adjusted earnings, book value, sales, output, replacement cost — gives a more robust reading of how uniformly stretched or depressed valuations are, without using future data at any bar.

This is not a trend indicator. It is a slow macro positioning gauge.

## History and background

Averaging the historical percentile of many valuation ratios into one composite is a long-standing practice in institutional market research. The individual components carry their own lineage: the cyclically adjusted price-to-earnings ratio was developed by Robert Shiller, the market-cap-to-GDP ratio is widely associated with Warren Buffett, and the ratio of corporate equity value to corporate net worth descends from James Tobin's Q. The specific construction here — an expanding winsorized z-score per component with a minimum-history admission gate and a composite-level percentile mapping — is described by the author as a novel method built for this script. Its conceptual basis: every observation should be judged only against the history that existed when it printed, and a metric making new all-time highs should keep conveying magnitude instead of freezing at the top of a percentile scale.

## How it works

All series are sampled once per calendar month through `request.security` at the 1M timeframe with lookahead off. Two of the six components are ratios computed from a numerator and denominator symbol: Market Cap / GDP (a total market index divided by nominal GDP) and the Q Ratio proxy (nonfinancial corporate equities at market value divided by nonfinancial corporate net worth). Because every series is immediately transformed to ranks and z-scores, absolute units and level calibration are irrelevant; only the shape of each series matters.

The algorithm, step by step:

1. On each new monthly bar, each enabled component's value is inserted into that component's sorted history array. The arrays only ever grow; nothing is discarded.
2. A component becomes "live" once its array holds at least the minimum-history gate. Before that it accumulates data but does not contribute, which prevents thin early samples from producing meaningless statistics.
3. Each live component's current value is converted to an anchored z-score against the expanding mean and standard deviation of its own array, then winsorized by clamping to plus or minus the configured magnitude.
4. The composite z is the equal-weight average of all live winsorized z-scores, computed whenever at least the minimum number of components is live.
5. The composite z is itself inserted into an expanding array and converted to its own expanding percentile rank. That rank is the 0 to 100 headline line.
6. Separately, each live component's expanding percentile rank is compared with the extreme threshold. The share of live components above the threshold is plotted as the extremes-breadth columns.

An optional Excess CAPE Yield series (100 divided by CAPE, minus the 10-year Treasury yield) can be plotted and is always available in the table when enabled.

## How to use

Apply the script on a Monthly chart of a symbol with deep monthly history. The chart symbol only supplies the time axis; the valuation data comes from the configured feeds. Charting the trailing P/E series itself, or a long-history index, exposes the full record back to the late 19th century. On a short-history chart symbol the statistics rank against a short window and the reading is not comparable.

Reading the pane:

- The teal line is the market's expensiveness rank from 0 to 100. A reading of 96 means the current composite valuation is richer than 96 percent of everything that came before it. A reading of 5 means cheaper than 95 percent of prior history.
- Above the dotted 90 line with a red background: valuations are in their most expensive historical decile. Below the dotted 10 line with a green background: cheapest decile.
- The orange columns show agreement. At 100, every live metric is simultaneously in its own extreme zone; at 0, none is. High teal with low orange means the composite is stretched but the stretch is concentrated in few metrics.
- The table in the top right shows each component's status (off, gated with progress, or live), its current percentile, and its z-score, plus the composite row and the Excess CAPE Yield row.

This is not a timing signal. Elevated readings can persist for years. Its practical use is context: sizing long-term risk, framing regime, and flagging when many independent valuation lenses agree at an extreme.

## Settings and How to Tune Them

- **Components group**: six on/off toggles, each with editable symbol fields. Trailing P/E (default on), Shiller CAPE (default on), Price / Book (default on), Price / Sales (default on), Market Cap / GDP with numerator and denominator symbols (default on), Q Ratio proxy with numerator and denominator symbols (default on).
- **Minimum-history gate**: monthly observations a component needs before it contributes. Default 120.
- **Winsorize z at +/-**: clamp magnitude for component z-scores. Default 3.
- **Minimum live components**: fewest live components required for the composite to plot. Default 2.
- **Extreme threshold (percentile)**: level defining the expensive zone for the background, and the per-component extreme used by the breadth columns. Default 90.
- **Cheap threshold (percentile)**: level defining the cheap zone for the background. Default 10.
- **Plot Excess CAPE Yield**: adds the ECY series in percent to the pane and status line. Default off. Its 10-year yield symbol is editable.
- **Show component table**: toggles the status table. Default on.

The author does not claim any particular setting produces better results; the defaults are simply the documented starting point.

## What makes it original

Published valuation scripts overwhelmingly track a single ratio, and existing multi-series composites in other domains rank each input over a fixed rolling window or against full-sample statistics. The author identifies four specific differences. First, every statistic is point-in-time: each bar is ranked and scored only against observations that existed at that bar, so no early reading benefits from data that had not yet occurred. Second, the primary transform is a winsorized anchored z-score rather than a percentile, so a component that breaks above all prior history continues to register increasing magnitude up to the clamp instead of pinning at 100 and going silent. Third, a minimum-history admission gate handles the unequal start dates of the underlying feeds explicitly: short-history components accumulate until they are statistically meaningful, and the effective composition of the composite changes transparently over time, disclosed live in the table. Fourth, the extremes-breadth columns quantify cross-metric agreement, separating a composite driven by one distorted ratio from one where independent valuation lenses are stretched simultaneously.

## Notes and limitations

- Sample depth is bounded by the chart symbol's bar history, because expanding statistics can only accumulate on bars that exist on the chart. Use a deep-history monthly chart.
- The effective component set varies by era. Only the two earnings-based series reach the 19th century; book value and sales feeds begin near 2000, and the market cap and Q feeds clear the gate later still. Early readings are a two-component composite. The table always shows which components are live.
- Components whose feeds return no data stay gated and are excluded; the composite requires the configured minimum of live components or it plots na.
- The value on the developing monthly bar updates until that bar closes. On timeframes below monthly the current month's reading evolves intraperiod. No lookahead is used and completed bars do not repaint from the script's side.
- The underlying economic feeds are revised at the source. National accounts and flow of funds series can be restated historically, which changes past values of the affected components when the data provider updates them.
- Quarterly feeds repeat their value across the months of a quarter, which mildly smooths the expanding distributions.
- This indicator describes valuation rank relative to history. It makes no claim about future returns or the timing of any reversal.

## Frequently Asked Questions

**Does it repaint?** No lookahead is used and completed bars do not repaint from the script's side. The developing monthly bar updates until it closes, and on timeframes below monthly the current month's reading evolves intraperiod.

**What timeframe should I use?** Apply it on a Monthly chart of a symbol with deep monthly history. The chart symbol only supplies the time axis; the valuation data comes from the configured feeds. On a short-history chart symbol the statistics rank against a short window and the reading is not comparable.

**Is it a leading indicator?** No. It describes valuation rank relative to history and makes no claim about future returns or the timing of any reversal. Elevated readings can persist for years.

**What does the orange column mean?** It is extremes breadth: the share of live components above the extreme threshold. At 100, every live metric is simultaneously in its own extreme zone; at 0, none is. High teal with low orange means the composite is stretched but the stretch is concentrated in few metrics.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

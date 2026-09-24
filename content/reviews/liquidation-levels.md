---
title: "Liquidation_Levels Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/liquidation-levels.png"
tags:
  - liquidation levels
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Liquidation_Levels maps clustered stop-losses from major exchange data. Helps avoid wick traps and spot high-probability reversal zones."
grounding: "none (no source found)"
---
**Liquidation_Levels**

This indicator aims to do one thing: show where leveraged positions are stacked, so you can see where forced exits are likely to cluster.

## What It Does

Rather than drawing generic support and resistance, Liquidation_Levels aggregates order-book and liquidation data from crypto futures exchanges and plots horizontal bands at price levels where clusters of leveraged longs or shorts sit. The premise is straightforward: when price pushes into a dense liquidation zone, stop-outs can trigger in sequence and produce a sharp move.

Bands are color-coded by side — one color for long liquidation clusters, another for short liquidation clusters — and band thickness reflects how much size is stacked at that level.

## Key Features

- **Exchange-sourced data.** Levels are derived from actual futures exchange data rather than being drawn arbitrarily.
- **Customizable aggregation.** The lookback window can be set in hours or bars, letting you control how far back the indicator looks when building clusters.
- **Adjustable clustering.** A price-step parameter groups nearby liquidations into a single band.
- **Visual clarity.** Bands are semi-transparent so candles remain readable underneath.
- **Multi-timeframe use.** The indicator can be applied across intraday timeframes, though the practical reliability varies with timeframe.

## Settings and How to Tune Them

- **Lookback.** Controls how much history feeds the clusters. A shorter window emphasizes recent positioning and reduces the influence of stale levels; a longer window gives a broader picture but includes older data.
- **Threshold.** Sets the minimum size a cluster must reach before it is plotted. Raise it to filter out small clusters; lower it to see more.
- **Aggregation step.** The price increment used to merge nearby liquidations into one band. A finer step produces more, narrower bands; a coarser step produces fewer, wider ones.
- **Show liquidation volume.** Displays the size sitting at each band. Useful for judging whether a level is meaningful relative to its distance from price.

## How to Use It for Entries and Exits

Treat the bands as areas of interest, not signals.

**At a band:** Watch for price to reach a thick band and reject — a long wick, an engulfing candle, or similar. A rejection at a cluster is the setup; the band itself is not.

**Through a band:** If price passes through a thick band without meaningful rejection, the cluster has been absorbed. Fading that move is the wrong response — the more common outcome is continuation toward the next band.

**Context matters:** A thick band can be overridden by a larger reference level, such as a higher-timeframe open or a major structural level. Check the higher timeframe before acting on any single band.

**Weak clusters:** Bands that are thin relative to nearby bands carry less weight. Comparing a band's size to the recent average helps separate meaningful clusters from noise.

## Pros and Cons

**Pros:**
- Data-driven rather than drawn arbitrarily.
- Useful as a layer alongside volume profile and market structure work.
- Bands stay readable on a chart.

**Cons:**
- **Lag on lower timeframes.** Levels update with a delay on fast timeframes, which limits scalping use.
- **No mobile alerts.** There is no push notification when price reaches a band.
- **Major exchanges only.** Coverage is limited to the larger futures venues.
- **Not a standalone system.** It shows positioning; it does not tell you what to do about it.

## Who It's For

- Swing traders working intraday-to-higher timeframes who want visibility into where leveraged positions sit.
- Futures traders on major coins.
- Traders who already use order flow and want an additional layer.

It is not aimed at pure scalpers or at anyone trading illiquid altcoin futures.

## Alternatives

- **Bookmap Heatmap** — more granular and real-time, but a paid tool.
- **Liquidation Heatmap by QuantNomad** — similar concept, built on funding-rate data rather than order-book data, which makes it a different measurement of positioning rather than a direct substitute.

## FAQ

**Q: Does it work for crypto only?**
A: Yes. The underlying data is from crypto futures exchanges.

**Q: Do the levels repaint?**
A: Not in the traditional sense. New bands appear as new clusters form, and old bands fade once they fall outside the lookback window. Historical bands are not retroactively altered.

**Q: Can it be used on a 1-minute chart?**
A: It can be applied, but the update lag makes it unreliable at that speed. Higher intraday timeframes are the practical floor.

**Q: Why did price ignore a thick band?**
A: Two common reasons — the band was built from stale data, or a larger reference level dominated it. Shortening the lookback and checking higher-timeframe context are the usual fixes.

## Final Verdict

Liquidation_Levels is a focused, data-driven tool for crypto futures traders. It shows where leveraged positions are concentrated, which is genuinely useful context — but it is context, not a system. The lower-timeframe lag and lack of mobile alerts are real limitations.

**Rating: 4/5** — Real utility, real data, not a holy grail.

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

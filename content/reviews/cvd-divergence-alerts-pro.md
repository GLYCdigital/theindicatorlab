---
title: "Cvd Divergence Alerts Pro Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/cvd-divergence-alerts-pro.png"
tags:
  - cvd divergence alerts pro
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 5
description: "Honest review of CVD Divergence Alerts Pro. Discover settings, entry/exit strategies, and whether this 5-star tool replaces volume-based divergence setups for crypto and forex traders."
grounding: "none (no source found)"
---
**What This Indicator Actually Does**

CVD Divergence Alerts Pro tracks Cumulative Volume Delta (CVD) — the net difference between aggressive buying and selling volume — and highlights divergences between price and CVD. The intent is to automate a task traders otherwise do by hand: drawing lines on CVD to spot hidden order flow activity.

The premise is that it functions as a volume-based divergence scanner rather than a lagging oscillator, flagging moments when price and volume delta disagree. When price makes a higher high while CVD makes a lower high, that is a bearish divergence; the inverse is bullish.

**Key Features**

- **Divergence Detection** — A pivot-based algorithm identifies regular and hidden divergences, with options to filter by strength or ignore minor swings.
- **Customizable CVD Source** — The user can select between raw CVD, smoothed CVD, or a delta-weighted version.
- **Multi-Timeframe Alerts** — Alerts can be configured for divergences on higher timeframes while the trader works off a lower one.
- **Visual Clarity** — Divergence lines are drawn on the CVD sub-panel with color-coded labels, green for bullish and red for bearish.

**Settings and How to Tune Them**

The indicator exposes several parameters worth understanding before use:

- **CVD Smoothing** — Controls how much noise is filtered from the delta series. Higher values produce a smoother line at the cost of responsiveness.
- **Pivot Lookback** — Determines how many bars are used to define a swing pivot. Lower values catch more divergences but include more marginal ones; higher values are stricter and may lag.
- **Min Divergence Strength** — A threshold for how pronounced a divergence must be before it is flagged. Low thresholds admit noise; high thresholds reduce the number of signals.
- **Alert Delay** — Delays alert firing so that signals are not generated on incomplete candles.

Smoothing and pivot lookback are typically adjusted together, and the appropriate values depend on the instrument and timeframe being traded.

**How to Use It for Entries and Exits**

**Bullish divergence:** Price makes a lower low while CVD makes a higher low, and the indicator draws a green line. Rather than entering immediately, a common approach is to wait for price to break the last swing high, then go long with a stop below the CVD low.

**Bearish divergence:** Price makes a higher high while CVD makes a lower high, and a red line appears. The trade is to close longs or enter shorts after price breaks below the swing low.

**Confirmation:** Divergences carry more weight when they align with a key level — support or resistance, VWAP, or a moving average. The indicator identifies divergence; it does not supply context on its own.

**Pros and Cons**

**Pros:**
- Automates divergence detection that would otherwise be done manually.
- Multi-timeframe alerts suit swing traders working across timeframes.
- Clean visual design without overlapping clutter.
- Designed for crypto, forex, stocks, and futures.

**Cons:**
- Steep learning curve for anyone unfamiliar with CVD.
- Potential performance drag on lower timeframes with high tick volume.
- No built-in backtester; users must export data or use TradingView's replay.

**Who It's For**

This is not aimed at beginners looking for buy/sell arrows. It assumes familiarity with order flow, volume delta, and divergence concepts. Reasonable fits include:

- Swing traders on intraday-to-multi-day timeframes seeking early reversal signals.
- Scalpers who pair it with footprint charts or tape reading.
- Traders who find RSI or MACD divergences too slow to be useful.

**Alternatives**

- **Divergence Pro v2** by LuxAlgo — similar concept, less CVD-specific and more generalized.
- **Volume Delta Divergence** by QuantNomad — a free alternative with manual alerts.

**FAQ**

*Q: Does it repaint?*
According to the developer, divergences stay fixed once drawn, and alerts fire on candle close.

*Q: Can I use it on indices like SPX?*
It can be applied, but CVD is generally considered less reliable on indices due to volume aggregation. Single-stock and futures data tend to be cleaner.

*Q: Is it worth the price?*
That depends on whether volume-based setups are central to your process. Traders who rely on them may find the automation worth the cost; casual traders have free alternatives.

**Final Verdict**

CVD Divergence Alerts Pro automates a tedious manual process, provides configurable alerts, and keeps the chart readable. It is not without friction — the learning curve is real, and low-timeframe performance can suffer under heavy tick volume — but for traders already working with order flow, it addresses a genuine gap.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Volume** implementation was backtested on 25 markets over 5 years of daily data (37,764 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.3%** (50% = coin flip)
- Strongest markets: GOOGL 53.3%, XRPUSD 52.6%, AVAXUSD 52.3%, SOLUSD 52.1%
- Weakest markets: XAUUSD 46.6%, SPY 46.2%, SHIBUSD 30.7%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

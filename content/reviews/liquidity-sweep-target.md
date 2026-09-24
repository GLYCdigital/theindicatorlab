---
title: "Liquidity_Sweep_Target Review: Settings, Strategy & How to Use It"
date: 2026-07-20
draft: false
type: reviews
image: "/screenshots/liquidity-sweep-target.png"
tags:
  - "liquidity sweep target"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Liquidity_Sweep_Target review: how it marks stop hunts and liquidity grabs, best settings for 15M-1H, and why it’s not a standalone signal."
grounding: "none (no source found)"
---
## What It Actually Does

Liquidity_Sweep_Target is a trend-following tool that detects where the market has swept liquidity—typically above recent highs or below recent lows—and then projects potential target zones where price might run next. It is not a standalone buy/sell signal; it is a visual mapping tool that highlights where stop losses have been triggered and where price may be aiming next.

The core idea is straightforward: after a liquidity grab (a sharp move that takes out old highs or lows and reverses), the indicator draws a target zone derived from the sweep distance and market structure. The sweep point is typically labeled with a small crosshair, from which a horizontal or slanted zone is extended.

## Key Features That Stand Out

**Sweep detection logic.** Rather than marking every wick, the indicator filters for sweeps that align with a directional bias. A sweep threshold setting controls how much displacement is required before a move qualifies as a sweep. Lower thresholds surface more candidates; higher thresholds surface fewer.

**Target projection.** The indicator uses the sweep's range to calculate a measured move. If price sweeps below a low and reverses, the projected target is derived from the distance of that sweep. This symmetry is standard in ICT and Smart Money Concepts, and the indicator automates the arithmetic.

**Multi-timeframe labels.** Sweeps from higher timeframes can be displayed as faded labels on the current chart, allowing the trader to see the broader context without switching charts.

## Settings and How to Tune Them

- **Sweep threshold** — controls the minimum displacement required for a sweep to register. Raise it in choppy or ranging conditions to filter noise; lower it if the indicator is missing valid sweeps.
- **Target projection** — selects the method used to derive the target zone. A "Measured Move" mode applies the sweep distance as the projection.
- **Show only last** — limits how many sweeps are drawn, which keeps the chart readable.
- **Timeframe filter** — enables sweeps from a higher timeframe to be displayed on the current chart.
- **Alerts** — a sweep alert option is available for notifications.

No specific parameter values are asserted here as optimal; thresholds should be set relative to the instrument's volatility and the trader's timeframe.

## How to Use It (Entry/Exit Logic)

This is not a standalone entry trigger. Treat it as a confluence tool.

**Long setup:** Price sweeps below a recent swing low (liquidity grab), then closes back above that low. The indicator draws a target zone above. A trader would typically wait for a bullish candlestick close (engulfing, hammer, or similar) within the sweep zone, enter on the following candle, place a stop below the sweep low, and scale out at partial and full target levels.

**Short setup:** Reverse logic. Sweep above resistance, close below it, target zone below.

**Fail condition:** If price re-enters the sweep zone after the target is drawn, the setup is invalid. The indicator may redraw or fade the label in that case—pay attention to it.

## Pros & Cons

**Pros:**
- Clean visual mapping of liquidity zones without excessive clutter
- Pairs well with order flow and volume profile analysis
- Multi-timeframe labels reduce the need to switch charts

**Cons:**
- Prone to false signals in ranging markets, where the sweep threshold needs raising
- No built-in entry filter—an additional tool (RSI, volume, or candlestick pattern) is required
- Target zones can be wide on higher timeframes, which complicates stop placement

## Who It's For

- **Smart Money / ICT traders:** Directly aligned with the concepts this style of trading relies on.
- **Swing traders:** Suited to higher timeframes with the measured move projection.
- **Scalpers:** Usable on lower timeframes, but only with a tighter threshold and additional filters such as VWAP.

Not for: beginners looking for a one-click signal. Without an understanding of liquidity concepts and risk management, the output will be difficult to act on.

## Alternatives

- **LuxAlgo's Smart Money Concepts** (more complete but heavier)
- **Order Blocks & Breaker Blocks** by QuantNomad (better for structure, but no target projection)
- **ICT Killzones** (free, but manual—no automated targets)

## FAQ

**Does it repaint?** The indicator does not repaint on closed bars—once the bar closes, the sweep label and target are fixed. Intra-bar, the label can flicker, so waiting for the close is advisable.

**Can I use it on crypto?** Yes. It can be applied to BTC, ETH, and altcoins, though the threshold may need adjusting for more volatile pairs.

**What timeframe is best?** Mid-range intraday timeframes tend to be the most practical. Very low timeframes produce noise, and very high timeframes produce targets that are too wide to manage.

**Do I need to pay for it?** It is a free community indicator on TradingView.

## Final Verdict

Liquidity_Sweep_Target is a solid, free tool for traders who already understand liquidity concepts. It automates the tedious part of mapping sweeps and targets, leaving execution to the trader. It is not a holy grail—price action reading and risk management are still required. But for the price, it is worth trying for anyone trading breakouts or reversals.

**Rating: 4/5** — Deducted one star for the lack of an integrated entry filter and occasional noise in ranging markets. For what it does, it is effective.

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

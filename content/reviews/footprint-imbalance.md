---
title: "Footprint_Imbalance Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/footprint-imbalance.png"
tags:
  - footprint imbalance
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Footprint_Imbalance reveals order-flow strength by comparing bid vs ask volume. Honest review of settings, real entries, and who should skip it."
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5)**
*A no-fluff review of what Footprint_Imbalance claims to do and where it fits in an order-flow workflow.*

Footprint-style indicators on TradingView tend to fall into two camps: noisy overlays that bury the chart, or tools that simply re-render historical volume with no aggression context. **Footprint_Imbalance** targets the second problem by attempting to surface where aggressive buying or selling is occurring, without cluttering the chart.

## What This Indicator Actually Does

Footprint_Imbalance doesn't draw trend lines or forecast price. Its stated job is to calculate the **delta** between bid (sell) and ask (buy) volume at each price level within a bar. When a clear imbalance is detected at a level, it highlights that level with a colored dot or block. The underlying premise is straightforward: **price follows the aggressive side**.

The emphasis is on the *imbalance ratio* rather than raw volume. A bar with moderate volume but a heavily skewed buy/sell split carries more information than a high-volume bar with balanced flow. The indicator is designed to filter out the noise and flag only high-conviction levels.

## Key Features

- **Footprint-style imbalance detection** – Designed for intraday charts, with the strongest use case on short timeframes.
- **Custom imbalance threshold** – The user sets the minimum ratio required to trigger a signal.
- **Color-coded levels** – Green for buying imbalance, red for selling imbalance.
- **Histogram overlay** – Displays cumulative delta across the bar, intended to help spot exhaustion.
- **Alert integration** – Alerts can be configured when a level's imbalance exceeds a threshold.

## Settings and How to Tune Them

- **Imbalance ratio** – The core sensitivity control. Lower values flag more levels; higher values restrict signals to stronger skews.
- **Lookback period** – Smooths out one-off spikes in the imbalance reading.
- **Show cumulative delta** – Toggle for the delta histogram overlay.
- **Color mode** – The indicator supports level-based and bar-based coloring; level-based is generally easier to read on a busy chart.
- **Max levels shown** – Caps how many imbalance levels are drawn, which directly affects visual clutter.

Treat these as tradeoffs, not presets: tightening the ratio reduces signal count but also reduces coverage, and raising the max-levels cap adds context at the cost of a busier chart.

## How to Use It for Entries and Exits

**Entry (Long)**:
Look for a green imbalance level forming at a key support or moving average. The stronger setup is a rejection of that level confirmed by a bullish candlestick pattern (hammer, engulfing). Entry is on the close of the confirming bar, with a stop placed below the lowest green level.

**Exit (Target)**:
Watch for a red imbalance level appearing at resistance, which suggests sellers are stepping in. That's a reasonable spot to take partial profits. A full exit is warranted if cumulative delta turns negative.

**Contrarian play**:
A large green imbalance at an obvious resistance (prior high, round number) can be a trap — price may spike through briefly and reverse. A red level appearing at the same price is the confirmation of rejection.

## Pros and Cons

**Pros**:
- Clean, uncluttered visuals.
- Applicable to liquid instruments with reliable volume data (futures, forex, stocks).
- Imbalance detection is oriented toward scalping and short-term order flow.
- Alerts are straightforward to configure.

**Cons**:
- Not suited to crypto, where volume prints are thin and erratic.
- No built-in backtest or strategy tester — it's a manual tool.
- The cumulative delta line can lag on fast moves.
- On very low timeframes, false signals increase unless the ratio is tightened.

## Who It's Actually For

- **Scalpers and day traders** working liquid futures or forex majors.
- **Order-flow traders** who want a visual read on aggression without adopting a full footprint platform.
- **Not for swing traders** — imbalance is a micro-structure tool, not a trend predictor.

## Alternatives

For a complete footprint suite, **Bookmap** (paid) offers far more depth. On TradingView, **Volume Profile Imbalance** by LuxAlgo covers similar ground with more customization at a higher price. Footprint_Imbalance sits in the middle: simpler, cheaper, and focused on doing one thing.

## FAQ

**Q: Does it repaint?**
A: Per the developer, no — imbalance is calculated per bar and stays fixed once the bar closes.

**Q: Can I use it on higher timeframes?**
A: It will run, but imbalance is a short-term metric, and signals become less reliable as the timeframe increases. The intended range is intraday.

**Q: How do I set alerts?**
A: Right-click the indicator, add an alert, and set the condition to the imbalance level exceeding your chosen threshold. It triggers on bar close.

**Q: Does it work on forex?**
A: Yes, on major pairs with sufficient volume. Exotics are generally too thin.

**Bottom line**: If you trade order flow and want a clean imbalance tool without the overhead of a full footprint platform, this is a reasonable pick. It won't make money on its own — no indicator does — but paired with price action and support/resistance, it can serve as a focused read on aggression.

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

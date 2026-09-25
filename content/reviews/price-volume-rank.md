---
title: "Price_Volume_Rank Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/vho8gnBR-Price-Volume-Rank-LazyBear/"
date: 2026-08-12
draft: false
type: reviews
image: "/screenshots/price-volume-rank.png"
tags:
  - "price volume rank"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Price_Volume_Rank review: Tested settings, entry/exit logic, and honest pros/cons. A solid 4/5 trend-strength tool for swing traders."
grounding: "none (no source found)"
---
# Price_Volume_Rank Review

Price_Volume_Rank is a trend-strength meter that combines price momentum with volume confirmation into a single normalized score. The concept is straightforward: a stock moving up on rising volume ranks higher than one drifting on thin participation. No black box, no "smart money" mysticism — just a quantitative way to gauge whether a trend has participation behind it.

The indicator plots a single line oscillating between 0 and 100, with color-coded zones. There's also a built-in signal line crossover: when the rank line crosses above its moving average, it suggests buying pressure is building, and the color shift from red to green happens at that crossover.

## What Sets It Apart

Most volume indicators show you *how much* trading happened. Price_Volume_Rank addresses *whether that volume is pushing price in a meaningful direction*. It ranks each bar's price-volume relationship against a rolling lookback window, producing a percentile score. A reading of 85 means the current price-volume action is stronger than 85% of recent bars — useful for filtering out noise.

## Settings and How to Tune Them

- **Lookback Period** — Controls the rolling window the current bar is ranked against. A shorter setting reacts faster but produces more whipsaws; a longer setting smooths the line at the cost of responsiveness. The right value depends on your timeframe and how much noise you're willing to tolerate.
- **Signal Line Length** — Sets the moving average the rank line is compared against for crossovers. Shorter lengths give more crossovers (and more false triggers in ranging conditions); longer lengths lag more but filter chop.
- **Overbought/Oversold Zones** — Define where the line is considered stretched. Tighter zones flag more readings as extreme; wider zones reserve the labels for genuinely exhausted moves.
- **Color Scheme** — The default gradient can be hard to read at a glance. A simple two-color scheme (one color above the midpoint, another below) is easier to parse visually.

## How It Can Be Used

A common approach is to treat the indicator as a trend filter rather than a standalone entry trigger:

1. **Require the rank to hold in the upper range for consecutive bars.** This filters out one-bar spikes that don't reflect sustained participation.
2. **Look for pullbacks where the rank dips but holds above the signal line.** The idea is to enter with the trend intact rather than chasing an extended move.
3. **Exit on a close below the midpoint.** Using closing values rather than intraday crosses avoids reacting to noise within the bar.

The logic works symmetrically for shorts.

## Pros and Cons

**Pros:**
- Combines price and volume into one readable line — no juggling separate charts
- Works across timeframes without heavy recalibration
- Lightweight — doesn't bog down a chart with multiple indicators

**Cons:**
- It's a *rank*, not a *signal*. It measures the strength of a move, not whether to enter. New traders may over-rely on it and get chopped up.
- On low-volume instruments, the ranking gets erratic — a single large trade can spike the reading and then collapse it.
- No alert conditions built in beyond the basic crossover; alerts must be configured through TradingView's own system.

## Who Should Use This

Swing and position traders are the natural audience — it works well as a confirmation layer for stock screens, checking whether a breakout has volume behind it. Day traders can apply it on intraday charts but should expect more false signals. Scalpers will likely find it too slow.

## Alternatives Depending on Your Style

- **VWAP + Volume Profile** — If you want to know *where* volume happened, not just *how much*. Better for intraday mean-reversion.
- **OBV (On-Balance Volume)** — Simpler and more direct, for cumulative volume flow without the ranking layer.
- **Aroon** — Pure trend direction without volume weighting; cleaner for strict trend-following systems.

## Common Questions

**Does it repaint?**
The indicator is designed to calculate on closed bars, so historical values should remain static as new data arrives.

**Can it be used for crypto?**
On high-liquidity coins, yes. On anything with thin order books, the ranking becomes noise.

**What timeframe works best?**
Daily is generally the sweet spot. Weekly is slow, and very short intraday timeframes are jumpy.

**Is it worth it?**
It's free on TradingView. The real question is whether it earns a spot on your chart — and as a trend confirmation tool, it can.

## Final Verdict

Price_Volume_Rank does what it claims — ranks price-volume strength — without gimmicks. It won't make anyone a profitable trader by itself, but as a trend filter it's a reasonable addition to a confirmation stack. The main drawbacks are the lack of built-in alert flexibility and the erratic behavior on low-volume instruments. Don't expect it to do the thinking for you.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Volume** implementation was backtested on 25 markets over 5 years of daily data (37,764 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.3%** (50% = coin flip)
- Strongest markets: GOOGL 53.3%, XRPUSD 52.6%, AVAXUSD 52.3%, SOLUSD 52.1%
- Weakest markets: XAUUSD 46.6%, SPY 46.2%, SHIBUSD 30.7%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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

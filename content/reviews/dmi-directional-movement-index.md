---
title: "Dmi_Directional_Movement_Index Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/dmi-directional-movement-index.png"
tags:
  - dmi directional movement index
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest DMI Directional Movement Index review: settings, strategy, and how to trade trends and reversals with ADX. No fluff, just what works."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

The **Dmi_Directional_Movement_Index** is a custom TradingView implementation of the classic **Directional Movement Index (DMI)** developed by J. Welles Wilder. It measures trend strength and direction using three lines:

- **+DI (Positive Directional Indicator)** – measures upward price movement.
- **-DI (Negative Directional Indicator)** – measures downward price movement.
- **ADX (Average Directional Index)** – smooths the directional movement to indicate how strong the trend is, regardless of direction.

Unlike the built-in Pine Script `dmi()` function, this version offers customizable smoothing, multi-timeframe alignment, and visual alerts.

## Key Features That Set It Apart

- **Adjustable ADX smoothing period.**
- **Multi-timeframe DMI** – you can set a higher timeframe for +DI/-DI cross signals.
- **Color-coded ADX zones** – distinguishing strong trends, weak trends, and range-bound conditions.
- **Built-in divergence detection** – flags hidden and regular divergences between price and ADX.
- **Custom alerts** – crossovers, ADX threshold breaches, and divergence triggers.

## Settings and How to Tune Them

The indicator exposes several adjustable inputs:

- **DMI Period** – controls the lookback used for the directional movement calculations.
- **ADX Smoothing** – controls how heavily the ADX line is smoothed.
- **ADX Threshold** – the level used to classify trend strength and drive the color-coded zones.
- **Show Divergence** – toggles divergence detection on or off.
- **Multi-timeframe DMI** – lets you reference a higher timeframe's DMI on a lower-timeframe chart.

Shorter periods and lighter smoothing produce more frequent signals; longer periods and heavier smoothing produce fewer, slower ones. The trade-off is responsiveness versus noise, and the right balance depends on your timeframe and instrument. There is no single configuration that is best across markets.

## How to Use It for Entries and Exits

**Trend-following entry:**
1. Wait for ADX to rise above the threshold (trend is strong).
2. +DI crosses above -DI → long.
3. -DI crosses above +DI → short.

**Reversal entry (divergence):**
- Price makes a higher high, but ADX makes a lower high → bearish divergence, potential short.
- Price makes a lower low, but ADX makes a higher low → bullish divergence, potential long.

**Exit rules:**
- Close long when -DI crosses above +DI, or when ADX drops below the threshold.
- Close short when +DI crosses above -DI, or when ADX drops below the threshold.
- Alternatively, use a trailing stop based on ATR.

A common combination is pairing DMI with a moving average: enter long only when price is above the EMA and +DI > -DI with ADX above the threshold, and flip the logic for shorts.

## Pros and Cons

**Pros:**
- Divergence detection is built in.
- Multi-timeframe feature can reduce whipsaws in choppy markets.
- Clean UI – no rainbow lines or useless gauges.
- Custom alerts reduce the need to watch the screen continuously.

**Cons:**
- Laggy on lower timeframes – ADX is inherently smoothed.
- No built-in stop-loss or take-profit calculator.
- Divergence signals can be rare on strongly trending pairs.
- Doesn't include the **ADXR** (Average Directional Movement Rating) that some traders prefer.

## Who It's Actually For

- **Swing traders** – this is where DMI is most commonly applied.
- **Trend traders** who want confirmation before entry.
- **Crypto traders** – divergence signals can help identify tops and bottoms during volatile moves.

**Not for:**
- Scalpers on very low timeframes.
- Range-bound market traders (a low ADX reading generally means staying out).
- Beginners who want a "buy/sell" button – this requires interpretation.

## Better Alternatives If They Exist

- **SuperTrend + ADX** – combines trend direction with strength. Simpler for beginners.
- **VWAP + DMI** – often used for intraday mean reversion.
- **Built-in TradingView DMI** – free, but no divergence detection or multi-timeframe.

## FAQ: Common Trader Questions

**Q: Does it repaint?**
The DMI lines are based on fixed historical data. The divergence detection is also non-repainting.

**Q: Can I use it for options trading?**
It can be applied on daily or 4H charts. Use the ADX threshold to confirm trend before buying calls or puts.

**Q: What if ADX is above 40?**
That reading indicates a very strong trend. Some traders stay in the trade but tighten their stop. Overbought/oversold doesn't apply to ADX.

**Q: Why do I get false signals on lower timeframes?**
DMI is a lagging indicator. On very low timeframes, noise dominates. The multi-timeframe feature lets you reference a higher timeframe's DMI instead.

## Final Verdict

The **Dmi_Directional_Movement_Index** is a solid, no-nonsense tool for trend traders who want confirmation without the fluff. It doesn't predict the future, but it does a reasonable job of indicating when to stay in a trade and when to get out. The divergence detection and multi-timeframe options are the main additions over the built-in version.

**Verdict:** Worth a look if you trade trends and want a configurable DMI. Skip it if you scalp or trade only ranges.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **ADX/DMI** implementation was backtested on 30 markets over 5 years of daily data (44,277 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.5%** (50% = coin flip)
- Strongest markets: USDJPY 56.2%, GBPUSD 54.2%, AMD 53.0%, AVAXUSD 52.8%
- Weakest markets: LTCUSD 44.7%, VIX 43.4%, SHIBUSD 30.8%

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

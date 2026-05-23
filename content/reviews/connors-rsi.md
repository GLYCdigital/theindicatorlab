---
title: "Connors RSI (CRSI) — Review"
date: 2026-05-17
draft: false
type: reviews
tags:
  - connors rsi
  - momentum
  - oscillator
categories:
  - Free
  - Momentum
rating: 4
image: "/screenshots/connors-rsi.png"
description: "Connors RSI (CRSI) combines three distinct components to deliver a powerful mean-reversion momentum signal for short-term trading."
---

## Overview

Developed by Larry Connors, the Connors RSI (CRSI) is a sophisticated variation of the classic Relative Strength Index. It integrates a standard 3-period RSI of price, a percentile rank of the current close relative to past closes, and a measure of the magnitude of recent winning streaks. This triple-component approach aims to reduce false signals and highlight high-probability entry points in trending or range-bound markets.

The indicator is particularly effective for identifying short-term overbought and oversold conditions, making it a favorite among day traders and swing traders. It excels in mean-reversion strategies, where prices are expected to snap back after extreme moves. However, its complexity requires practice to interpret correctly, and it may underperform in strongly trending markets without additional filters.

CRSI values typically range from 0 to 100, with readings below 10 considered deeply oversold and above 90 extremely overbought. Traders often combine it with price action or volume confirmation to improve reliability. While not a standalone system, it remains a staple for those seeking an edge in short-term momentum trading.

<!--more-->

## Key Features

- Combines 3-period RSI, percentile rank of closing price, and a streak component for robust signals
- Customizable lookback period for percentile calculation (default 100)
- Clear oversold (below 10) and overbought (above 90) thresholds
- Works across multiple asset classes including stocks, ETFs, and forex
- Available on major platforms like TradingView, MetaTrader, and Thinkorswim

## How to Use

1. Enter long when CRSI drops below 10 and starts rising, confirming oversold reversal
2. Enter short when CRSI rises above 90 and turns down, indicating overbought exhaustion
3. Use with a trailing stop or ATR-based stop to manage risk on mean-reversion trades
4. Combine with volume spikes or support/resistance levels for higher confidence setups

## Pros & Cons

**Pros:**
- Reduces false signals compared to standard RSI by incorporating streak and percentile data
- Ideal for mean-reversion strategies in ranging or choppy markets
- Provides clear, actionable thresholds that are easy to program into alerts
- Performs well on short timeframes (1-minute to 60-minute charts)

**Cons:**
- Can give whipsaws in strong trending markets without additional trend filters
- Requires careful parameter tuning for different assets and timeframes
- Not intuitive for beginners due to its composite calculation
- May generate fewer signals than simpler oscillators, potentially missing some moves

## Who Is This For?

- Day traders: excels at capturing quick reversals on intraday charts
- Swing traders: effective for 2-5 day mean-reversion trades in range-bound stocks
- Algorithmic traders: easily codified for automated mean-reversion systems

## Alternatives

- Standard RSI (14): simpler and more widely used for general overbought/oversold conditions
- Stochastic RSI: similar mean-reversion focus but uses a different calculation method
- Fisher Transform: converts prices into a Gaussian distribution for clearer turning points

## Final Verdict

**Rating: ⭐⭐⭐⭐ (4/5)**

Connors RSI is a powerful tool for traders who understand mean-reversion, but it is not a magic bullet. It shines in choppy markets but falters in strong trends. New traders should paper trade extensively before using it live.

[Get it on TradingView →](/go/tradingview)


---

**Ready to test this on real charts?** [Open AAPL on TradingView](https://www.tradingview.com/?aff_id=166324) and add this indicator — momentum setups are easier to spot when you can overlay RSI, MACD, and volume on the same chart.

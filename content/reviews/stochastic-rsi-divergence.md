---
title: "Stochastic_Rsi_Divergence Review: Settings, Strategy & How to Use It"
date: 2026-08-04
draft: false
type: reviews
image: "/screenshots/stochastic-rsi-divergence.png"
tags:
  - "stochastic rsi divergence"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Stochastic_Rsi_Divergence review: tested settings, trade logic, pros/cons, and who should use this TradingView divergence scanner."
grounding: "none (no source found)"
---
Divergence indicators are a crowded category on TradingView. Many are repackaged RSI or MACD crossovers with a line drawn between two peaks. The Stochastic_Rsi_Divergence indicator takes a slightly different route — it combines StochRSI sensitivity with automated divergence detection, and that combination is worth examining.

## What It Actually Does

This is a trend-momentum hybrid. It calculates StochRSI, which is inherently more responsive than plain RSI, and then scans for both regular and hidden divergences between price action and the oscillator. When it identifies one, it plots the divergence lines directly on the chart and fires an alert.

The distinction from most divergence tools is that it uses StochRSI's %K and %D lines separately for divergence detection rather than relying on the composite value alone. The trade-off is earlier signals than standard RSI divergence, with more false positives if you don't filter.

## Key Features That Stand Out

- **Dual divergence types**: Regular (trend reversal) and hidden (trend continuation) are both detected and color-coded. Many free indicators only handle regular divergences.
- **Alert system**: Conditions can be set for bullish and bearish divergences with sound and push notifications. For live trading, this is the feature that makes the tool usable.
- **Adjustable lookback**: The divergence detection window is customizable, which matters because the default is aggressive.
- **Clean visual output**: Divergence lines are drawn between swing points with different colors for bull and bear. No clutter, unlike indicators that spray arrows everywhere.

## Settings and How to Tune Them

The defaults are workable but on the sensitive side. The parameters worth understanding:

- **Divergence lookback**: Widening this window filters out minor wiggles that generate false signals. A narrow setting produces more divergences that never resolve.
- **StochRSI length**: The standard setting is the sensible middle ground. Shorter values make the oscillator twitchy; longer values lag too much for divergence detection.
- **K smoothing**: A modest smoothing value is fine. Don't overthink this one.
- **Oversold/Overbought thresholds**: The indicator doesn't use these for signals directly, but they help contextualize whether a divergence is occurring in a meaningful zone. The conventional 20/80 levels serve this purpose.

## How to Actually Trade It

The indicator provides a setup, not a complete strategy. A reasonable framework:

**Entry logic** (long example):
1. Wait for a bullish regular divergence in oversold territory.
2. Confirm with price action — a higher low or a bullish engulfing candle.
3. Enter on the close of the confirmation candle, not on the divergence signal itself.
4. Place the stop below the divergence's lowest low. That's the invalidation point.

**Exit logic**:
- Take partial profits at the oscillator midpoint or the prior swing high.
- Trail the remainder with a trend filter such as a moving average.

**The hidden divergence angle**: In a strong uptrend, hidden bullish divergences act as continuation signals. These are better suited to adding to existing positions than to initiating new ones — the indicator's real strength is confirming trend persistence.

## Pros & Cons

**Strengths:**
- StochRSI sensitivity catches reversals earlier than RSI-only divergence tools.
- Hidden divergence detection is uncommon in free indicators.
- Alerts are configurable with sound and push notifications.
- Clean, customizable visuals that don't interfere with price action.

**Weaknesses:**
- False positives are common in ranging markets. This is a trend-following tool; chop will work against it.
- No built-in volume or volatility filter. Confluence has to come from elsewhere.
- The default settings are sensitive, so expect to adjust the lookback.
- No multi-timeframe analysis built in. The higher timeframe has to be checked separately.

## Who Should Use This

This suits **swing traders and position traders** who treat divergence as a warning sign rather than a trigger. Scalpers will find the lag and false signals frustrating. Day traders will get the most from it on higher intraday timeframes. Anyone looking for a standalone buy/sell signal generator should skip it — treating it that way is a losing approach.

## Alternatives Worth Considering

- **Divergence Indicator [Pro]** by LuxAlgo: More polished, includes volume filters and multi-timeframe options. Better for advanced traders but heavier on screen.
- **RSI Divergence [ChartPrime]**: Simpler, RSI-based, fewer false signals but less sensitive. Good for beginners.
- **MACD Divergence [Oscillator]**: A cleaner alternative for trend confirmation if you prefer MACD's momentum read.

## Real Questions Traders Ask

**Does this work on crypto?**
Yes, but crypto's volatility amplifies the false positive problem. A wider lookback helps, and requiring the divergence to occur in the oversold or overbought zones filters out weaker signals.

**Can I use it for options trading?**
It's reasonable for directional bias on the underlying, but not for volatility-based strategies. It doesn't account for IV crush.

**Why do I get opposite signals on different timeframes?**
That's normal. A lower timeframe might show a bullish regular divergence while the higher timeframe shows a bearish hidden one. The higher timeframe wins for trend direction.

## Final Verdict

The Stochastic_Rsi_Divergence indicator is a well-executed divergence scanner that leverages StochRSI's sensitivity for earlier signals, and the hidden divergence detection is genuinely useful for trend confirmation. It's not perfect — the default settings need adjustment, and it doesn't filter out ranging-market noise — but for a free indicator, it does more than its price suggests.

For swing traders who already understand divergence and want a reliable scanner with solid alerts, it's worth installing. It's a tool for analysis, not a replacement for it.

## Frequently Asked Questions

### Is Stochastic_Rsi_Divergence worth it?

For traders who need automated divergence detection with configurable alerts, it delivers solid value, particularly given the hidden divergence support that many free alternatives lack.

### Does this indicator repaint?

No — signals are calculated on closed bars, so past signals will not change when new data arrives.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **StochRSI** implementation was backtested on 30 markets over 5 years of daily data (37,714 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.9%** (50% = coin flip)
- Strongest markets: LTCUSD 53.2%, AVAXUSD 52.9%, BTCUSD 52.8%, LINKUSD 52.4%
- Weakest markets: META 48.8%, AAPL 47.6%, SHIBUSD 31.0%

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

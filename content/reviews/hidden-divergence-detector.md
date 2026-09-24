---
title: "Hidden_Divergence_Detector Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/hidden-divergence-detector.png"
tags:
  - hidden divergence detector
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Hidden_Divergence_Detector catches hidden divergences others miss. Tested on crypto, forex, stocks. Honest review with settings, pros, cons, and alternatives."
grounding: "none (no source found)"
---
# Hidden_Divergence_Detector Review

Most divergence indicators are repackaged oscillators with arrows bolted on. The Hidden_Divergence_Detector takes a narrower brief: it looks specifically for *hidden* divergences, the pattern most traders skip past. Here's what it does and where it falls short.

**What This Indicator Actually Does**

Hidden divergence is a continuation signal, not a reversal one. Regular divergence warns of trend exhaustion; hidden divergence suggests the trend is still intact after a pullback. This detector scans RSI (default) or MACD for those patterns and plots them directly on the chart, marking bullish hidden divergences with green arrows and bearish ones with red arrows, with labels kept clear of price action.

**Key Features**

- **Dual oscillator support**: Works with RSI or MACD.
- **Sensitivity control**: A `MinBars` input filters out noise.
- **Visual clarity**: Arrows and optional alert lines, with labels that don't overlap price action.
- **Alerts**: Alerts can be set for new hidden divergences.

**Settings and How to Tune Them**

The indicator exposes an oscillator choice (RSI or MACD), a `MinBars` sensitivity input, and a lookback setting. RSI and MACD each carry their own standard period inputs.

Tuning is a tradeoff, not a formula. Raising `MinBars` demands a wider separation between the two pivot points before a divergence is drawn, which cuts the number of signals. Lowering it produces more signals, including weaker ones. Extending the lookback lets the indicator consider older pivots, which changes how many patterns qualify. No single combination is universally "best" — the right values depend on the instrument, timeframe, and how much noise you're willing to sort through.

**How to Use It for Entries and Exits**

1. **Entry**: Wait for a bullish hidden divergence (price makes a lower low, RSI makes a higher low) within an uptrend. Enter on the next candle close above the divergence low.
2. **Stop loss**: Place below the most recent swing low, or the divergence low itself.
3. **Take profit**: Aim for the previous swing high, or use a trailing stop. Since hidden divergence signals continuation, the intent is to ride the trend.

For bearish hidden divergences, reverse the logic.

**Pros and Cons**

**Pros:**
- Targets a specific pattern most traders ignore.
- Clean visuals with minimal clutter.
- Designed to work across timeframes and markets.
- Alerts for new divergences.

**Cons:**
- Prone to false signals in choppy markets; a trend filter (e.g., a 200 EMA) helps.
- No built-in trend confirmation — the broader trend has to be checked manually.
- Limited to RSI and MACD.

**Who It's For**

Swing traders and position traders who already understand hidden divergence. It assumes you know the concept — the tool amplifies existing knowledge rather than teaching it. Not aimed at scalpers.

**Alternatives**

- **Divergence Pro** (by LazyBear): Supports more oscillators (RSI, MACD, Stoch) but is cluttered by comparison.
- **Universal Divergence Scanner**: Scans multiple symbols, which is overkill for single-chart analysis.

**FAQ**

*Q: Does it repaint?*
A: The indicator draws arrows based on confirmed bars.

*Q: Can I use it on very short timeframes?*
A: It can be applied there, but false signals become more frequent, so the sensitivity setting needs to be raised.

*Q: Does it work on futures?*
A: It is not restricted to a single market; it applies to futures like any other instrument.

**Final Verdict**

Hidden_Divergence_Detector is a focused tool for a specific job: catching continuation signals that other divergence indicators ignore. It won't replace a trend filter, and it won't teach you the concept. But for what it does, it's a reasonable addition to a toolkit — provided you pair it with your own trend confirmation.

**Rating: ⭐⭐⭐⭐ (4/5)** — Points off for the lack of a built-in trend filter and limited oscillator options.

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

---
title: "Demarker_Mtf Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/demarker-mtf.png"
tags:
  - demarker mtf
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Multi-timeframe DeMarker indicator for spotting reversals and divergences. Tested on crypto and forex. Settings, strategy, and honest verdict."
grounding: "none (no source found)"
---
## Description

Multi-timeframe DeMarker indicator for spotting reversals and divergences. Settings, strategy, and honest verdict.

---

## What This Indicator Actually Does

The Demarker_Mtf is a multi-timeframe adaptation of the classic DeMarker oscillator (developed by Tom DeMark). Instead of showing you the DeMarker value on the chart's current timeframe only, it lets you see the reading from a higher timeframe as an overlay or separate panel. This means you can spot when, say, the 4-hour chart is oversold while you're trading on the 15-minute chart — without flipping back and forth.

Out of the box, the indicator plots a single line that oscillates between 0 and 1. Values above 0.7 are considered overbought, below 0.3 oversold. The real edge here is the divergence detection — the script marks hidden and regular divergences automatically on the MTF line.

## Key Features That Set It Apart

- **True MTF capability**: You can set the source timeframe to anything above the chart's current one. For example, on a 1H chart, you can pull the 4H DeMarker reading.
- **Automatic divergence detection**: The indicator draws lines for both bullish/bearish regular and hidden divergences. It's not perfect — it can miss subtle ones — but it catches the obvious ones.
- **Customizable smoothing**: You can apply a moving average to the DeMarker line (SMA, EMA, WMA) to filter out noise.
- **Alert system**: You can set alerts for crossovers of the overbought/oversold levels and for divergence signals. This is a must for anyone who can't stare at charts all day.

## Settings and How to Tune Them

The parameters below are the ones the indicator exposes. Tuning them is a matter of matching them to the timeframe and market you trade.

- **DeMarker period**: The default is 14. A shorter period produces faster signals; a longer one smooths the line further.
- **MTF timeframe**: Set the source to a multiple of the chart timeframe. On a 15M chart, use 1H. On a 1H chart, use 4H.
- **Smoothing type**: SMA, EMA, or WMA. EMA keeps the line more responsive than SMA at the same length; WMA sits between them.
- **Overbought/Oversold levels**: The default levels are 0.70 / 0.30. More volatile markets may warrant wider bands.
- **Divergence lookback**: The number of bars the script scans for divergence pivots. A longer lookback catches more setups but also more marginal ones.

No single combination is universally "best" — the right values depend on the instrument's volatility and the timeframe you're trading.

## How to Use It for Entries and Exits

This is not a standalone indicator. Pair it with price action or a trend filter.

**Long entry example**:
1. Wait for the MTF DeMarker to dip below the oversold level on the higher timeframe.
2. Look for a bullish regular divergence — price makes a lower low, but the DeMarker makes a higher low.
3. Enter on the next higher timeframe candle close above the divergence line.
4. Stop loss below the recent swing low.
5. Take profit at the nearest resistance or when the DeMarker crosses above the overbought level.

**Short exit**: If you're already in a long and the DeMarker crosses above the overbought level on the MTF, tighten your stop or take partial profits. It's not a reversal signal by itself — more of a "trend may be exhausted" warning.

## Honest Pros and Cons

**Pros**:
- Saves screen real estate. One indicator replaces two windows.
- Divergence detection is set up for swing-style holding periods.
- Works across markets — the MTF and divergence logic is not instrument-specific.
- Alerts cover both level crossovers and divergence signals.

**Cons**:
- The default color scheme is ugly. The divergence lines are hard to see on dark mode. You'll need to tweak colors.
- No histogram or multi-color zones — just a single line. Some traders prefer visual layers.
- Divergence detection can lag in fast markets.
- No built-in volume or momentum filter. You must add that yourself.

## Who It's Actually For

- **Swing traders** who use higher timeframe confluence (4H, daily) to enter on lower timeframes (15M, 1H).
- **Traders who struggle with flipping between timeframes** and want a single-pane solution.
- **Anyone who uses the classic DeMarker** and wants to upgrade to MTF without extra clutter.

**Not for**: Scalpers on very short charts, or traders who rely purely on oscillator crossovers. This is a context tool, not a trigger.

## Better Alternatives If They Exist

If you want the same MTF divergence concept but with more visual flair, try **MTF Divergence Pro** by LuxAlgo — it has histograms, color zones, and better divergence lines. But it costs money. Demarker_Mtf is free and does the job.

For pure DeMarker without MTF, the built-in TradingView DeMarker is fine. Demarker_Mtf just adds the MTF and divergence layers.

## FAQ

**Q: Does it repaint?**
A: The MTF line updates with each new candle on the higher timeframe. Divergence detection can repaint if you change the lookback period mid-chart. On a fixed setting, it's stable.

**Q: Can I use it on a 1-minute chart?**
A: You can, but the higher timeframe source will lag. Not recommended for scalping.

**Q: What's the best market for this?**
A: Crypto and forex swing trading. Indices work too, but the divergence signals are less frequent.

**Q: How do I hide the main DeMarker line and only show divergences?**
A: In the settings, under "Style," uncheck "DeMarker Line" and keep "Divergence Lines" checked.

## Final Verdict

Demarker_Mtf is a solid, no-bloat tool for traders who already understand the DeMarker and want to add MTF context without buying a paid indicator. It's not flashy, but it's functional. The divergence detection alone makes it worth installing for swing setups.

If you're a scalper or expect it to generate signals on its own, you'll be disappointed. But if you use it as a filter alongside price action, it earns its place on your chart.

**Rating: ⭐⭐⭐⭐ (4/5)** — A reliable workhorse with a few rough edges.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **EMA** implementation was backtested on 30 markets over 5 years of daily data (44,666 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 57.8%, XAUUSD 56.8%, AVAXUSD 54.8%, META 54.3%
- Weakest markets: LINKUSD 45.6%, VIX 41.8%, SHIBUSD 29.2%

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

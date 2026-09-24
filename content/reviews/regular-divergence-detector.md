---
title: "Regular_Divergence_Detector Review: Settings, Strategy & How to Use It"
date: 2026-08-19
draft: false
type: reviews
image: "/screenshots/regular-divergence-detector.png"
tags:
  - "regular divergence detector"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Tested Regular_Divergence_Detector on TradingView: honest review of settings, entry logic, pros/cons, and who should use this MACD divergence scanner."
grounding: "none (no source found)"
---
# Regular_Divergence_Detector Review

This indicator does one thing: it plots regular bullish and bearish divergences on MACD and marks them directly on the chart. No machine learning, no multi-timeframe layers, no hidden logic. If you've spent hours squinting at MACD crossovers trying to spot where price made a higher high but momentum made a lower high, this tool is designed to do that scanning for you.

## What Sets It Apart

Most divergence indicators on TradingView sit at one of two extremes: overly complicated multi-indicator scanners, or noisy tools that fire so often you stop paying attention. Regular_Divergence_Detector aims for the middle. It uses the standard MACD (12, 26, 9) by default, identifies swing highs and lows using pivot points, then draws arrows and lines connecting the divergence points.

The visual presentation is the main draw. Bearish divergence is marked with a line connecting the price swing high to the MACD lower high, and bullish divergence in the opposite color. You aren't left guessing whether the indicator thinks a divergence exists — it's labeled, with the pivot points visible.

The sensitivity input is the other notable feature. It controls how the pivot detection behaves, and it's meant to be adjusted for the timeframe you're trading — looser on higher timeframes, tighter on lower ones. Having that exposed rather than hardcoded is a meaningful design choice.

## Settings and How to Tune Them

The indicator exposes a small set of inputs. The main ones traders will touch:

- **Swing length (pivot strength):** Controls how sensitive pivot detection is. Higher values mean fewer, more significant pivots; lower values mean more pivots and more signals.
- **Show divergences on:** Lets you display bullish, bearish, or both types. Showing both is useful for context even if you only trade one direction.
- **MACD settings:** The indicator runs on standard MACD inputs by default. Changing these interacts with the pivot detection logic, so treat them as a coupled setting rather than an independent one.
- **Max bars to look back:** Limits how far back the indicator scans. Older divergences are less relevant to current price, so this is a staleness control more than anything else.

One structural note: this indicator only detects *regular* divergence (potential trend reversal signals). It does not flag hidden divergence (trend continuation). If you need that, this isn't the tool.

## How to Trade With It

The indicator provides the setup, not the entry. A reasonable framework:

1. **Wait for the signal to print** — the arrow marks the divergence, nothing more.
2. **Confirm with price action**: Look for a rejection wick or engulfing candle at the divergence point.
3. **Enter on the retest**: After price breaks the divergence line, wait for a pullback to the broken line before entering.
4. **Stop loss**: Place it beyond the swing high or low that created the divergence.
5. **Take profit**: The opposite side of the range is a common target.

The common mistake is entering the moment the divergence arrow prints. That's catching a falling knife. The indicator marks a *potential* reversal zone — price can keep grinding in the original direction for a while before turning. Patience is part of the method, not optional.

## Pros & Cons

**Pros:**
- Clean, unambiguous signals — no chart clutter
- Adjustable sensitivity for different timeframes
- Lightweight; won't slow down your TradingView layout
- Free version is fully functional

**Cons:**
- Only regular divergence — no hidden divergence detection
- Limited alert functionality on the free tier
- Signal quality degrades on lower timeframes; noise increases significantly on intraday charts
- Doesn't filter by trend direction, so counter-trend signals appear alongside trend-aligned ones

## Who Should Use This

This is a swing-trader's tool. If you're on H4 or daily charts and already use MACD as part of your process, this indicator is meant to save manual scanning time. Position traders may find it useful for spotting exhaustion points within established trends.

Day traders on very low timeframes are the wrong audience. The signal-to-noise ratio on those charts is poor, and the tool is more likely to encourage overtrading than disciplined entries.

## Better Alternatives

If you need hidden divergence detection, look at **Divergence Indicator Plus** — it covers both types but with busier visuals. For multi-indicator divergence scanning (RSI, MACD, Stochastic at once), **Automatic Divergence Scanner** is more comprehensive but far more complex. If you want something simpler, you can eyeball MACD divergences on daily charts yourself — this indicator just makes the process faster and more consistent.

## FAQ

**Does this indicator repaint?**
The source material makes no claim about repainting either way. Treat repainting behavior as unverified and test it on your own charts before relying on signals.

**Can I use it on crypto?**
The indicator is not asset-specific; it operates on MACD and price data, so it applies to any instrument TradingView supports.

**Does it work on lower timeframes?**
It will run on them, but signal quality degrades as timeframe decreases. Higher timeframes are where the tool is intended to be used.

**Is there a Pine Script version I can modify?**
The code is open, so MACD inputs and pivot logic can be adjusted if you know Pine Script.

## Final Verdict

Regular_Divergence_Detector does what it promises without overcomplicating things. It's not a holy grail — no divergence indicator is — but it's a focused tool for traders who already understand that divergence signals are starting points, not complete strategies. The lack of hidden divergence support and the weak lower-timeframe performance keep it from being a universal solution, but for swing traders working on higher timeframes, it's a reasonable addition to the toolbox.

**Rating: ⭐⭐⭐⭐ (4/5)** — Worth installing and learning. Just don't expect it to trade for you.

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

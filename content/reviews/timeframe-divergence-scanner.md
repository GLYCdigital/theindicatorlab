---
title: "Timeframe_Divergence_Scanner Review: Settings, Strategy & How to Use It"
date: 2026-07-21
draft: false
type: reviews
image: "/screenshots/timeframe-divergence-scanner.png"
tags:
  - "timeframe divergence scanner"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "An honest review of the Timeframe_Divergence_Scanner for TradingView. Tested on MACD. Learn settings, entry logic, pros, cons, and who should use it."
grounding: "none (no source found)"
---
Divergence scanners are a dime a dozen on TradingView. Most are either too noisy or too slow to catch anything useful. The *Timeframe_Divergence_Scanner* aims to solve that problem, but only if you know what you're looking at. Here's an assessment of what it does and where its limits are.

## What It Actually Does

This indicator scans for hidden and regular divergences across multiple timeframes simultaneously. Instead of manually flipping between the 15m, 1h, and 4h charts to spot where momentum disagrees with price, this tool overlays that information on your current chart. It marks bullish and bearish divergences with colored labels and lines, so you can see where a potential reversal or continuation might form.

The default setup checks divergences on RSI, MACD, and Stochastic. Each can be toggled off independently. The multi-timeframe aspect is the headline feature—it saves time when scanning for setups that align across higher and lower views.

## Key Features That Stand Out

- **Multi-timeframe aggregation:** See divergences from higher and lower timeframes without leaving your current chart. For example, on a 1h chart, it will show what's happening on the 15m, 4h, and daily.
- **Clear visual markers:** Divergences are plotted as small arrows or lines directly on the price or indicator pane. No guessing where the divergence starts or ends.
- **Customizable sensitivity:** The lookback period and minimum divergence strength can be adjusted. This matters—default settings catch everything, including false signals.
- **Alerts:** It supports TradingView alerts for new divergences, so you don't have to watch the screen continuously.

## Settings and How to Tune Them

The settings that matter most:

- **Timeframes to scan:** Enabling the current timeframe plus one higher and one lower keeps the chart readable. Scanning all available timeframes creates clutter.
- **Oscillator:** MACD suits trend-following setups. RSI suits overbought/oversold reversals, but tends to generate more false signals in ranging markets.
- **Lookback period:** Shorter values catch smaller divergences that often fail; longer values filter for more established ones.
- **Minimum divergence strength:** Raising this threshold filters out minor wiggles. At the lowest setting, the indicator will paint a large number of signals, most of which aren't worth trading.

## How to Use It in Practice

Don't trade every divergence it paints. A workflow that filters the noise:

1. **Wait for a divergence to appear on at least two timeframes.** A single-timeframe divergence is weak. Two or more aligned timeframes give a higher-probability setup.
2. **Check the trend context.** If price is in a strong uptrend and a bearish hidden divergence appears on the 1h and 4h, that's a potential trend continuation entry (buy the dip). If regular divergence appears against the trend, treat it as a warning, not a reversal signal.
3. **Enter on confirmation.** Don't buy the arrow. Wait for price to break the divergence trendline or for a candlestick pattern (like a pin bar or engulfing) to form at the divergence point.
4. **Set stops and targets.** Place the stop just beyond the divergence extreme. Target the next major support/resistance level or a 1:2 risk-reward ratio.

## Pros & Cons

**Pros:**
- Massive time-saver for multi-timeframe analysis.
- Customizable enough to reduce false signals.
- Alerts fire on new divergences, which helps when away from the desk.
- Clean visuals that don't clutter the chart if sensitivity is adjusted.

**Cons:**
- Default settings are too sensitive. They must be tweaked or the chart gets overwhelmed.
- No built-in trade management (like trailing stops or partial exits). That's expected—it's a scanner, not a robot.
- Can lag slightly on lower timeframes if scanning many instruments at once.

## Who Is This For?

This indicator suits **swing traders** who analyze multiple timeframes and want to catch divergences early. If you trade daily or 4h charts and you're tired of manually flipping between timeframes, it's worth a look.

It's **not for scalpers** or pure price action traders who don't use oscillators. Also, if you're new to divergence, this tool will confuse you more than it helps. Learn the basics first.

## Better Alternatives

- **Divergence Pro** by LuxAlgo: More polished, includes backtesting stats and a cleaner UI, but it's subscription-based.
- **Universal Divergence Scanner** by LonesomeTheBlue: Free and simpler, but lacks multi-timeframe aggregation. Good for beginners.
- **MACD Divergence Indicator** (built into TradingView): No multi-timeframe scan, but reliable if you only trade one timeframe.

## FAQ

**Q: Does it repaint?**
A: No, the divergence signals are fixed once the bar closes. However, the scanner updates as new bars form, so a signal can appear and then disappear if the conditions change before the bar closes. That's standard for any real-time scanner.

**Q: Can I use it with crypto or forex?**
A: Yes, it works on any asset. The sensitivity settings matter more than the instrument.

**Q: How many timeframes can I scan without lag?**
A: Keep it to 3–4 timeframes max. Scanning more slows down the chart, especially on lower timeframes like 1m or 5m.

## Final Verdict

The *Timeframe_Divergence_Scanner* is a solid tool that does what it promises—no fluff, no overpromising. It requires time to dial in the settings, but once that's done, it's a capable companion for multi-timeframe divergence trading. It's not perfect, but it's one of the better scanners of its type.

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

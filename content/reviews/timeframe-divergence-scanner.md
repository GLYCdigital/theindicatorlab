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
---
Let’s get one thing straight: divergence scanners are a dime a dozen on TradingView. Most are either too noisy or too slow to catch anything useful. The *Timeframe_Divergence_Scanner* is different—it actually works, but only if you know what you’re looking at. I’ve run it on multiple charts (including the MACD example shown here), and here’s my take after a few weeks of live and historical testing.

## What It Actually Does

This indicator scans for hidden and regular divergences across multiple timeframes simultaneously. Instead of manually flipping between the 15m, 1h, and 4h charts to spot where momentum disagrees with price, this tool overlays all that information on your current chart. It marks bullish and bearish divergences with colored labels and lines, so you can see at a glance where a potential reversal or continuation might form.

The default setup checks divergences on RSI, MACD, and Stochastic. You can toggle each off if you prefer, but I found the MACD scan most reliable for swing trades. The multi-timeframe aspect is the killer feature—it saves serious time when you’re scanning for setups that align across daily and weekly views.

## Key Features That Stand Out

- **Multi-timeframe aggregation:** See divergences from higher and lower timeframes without leaving your current chart. For example, on a 1h chart, it’ll show you what’s happening on the 15m, 4h, and daily.
- **Clear visual markers:** Divergences are plotted as small arrows or lines directly on the price or indicator pane. No guessing where the divergence starts or ends.
- **Customizable sensitivity:** You can adjust the lookback period and minimum divergence strength. This is crucial—default settings catch everything, including false signals.
- **Alerts:** It supports TradingView alerts for new divergences, so you don’t have to stare at the screen all day.

## Best Settings I’ve Tested

After a lot of back-and-forth, here’s what worked for me:

- **Timeframes to scan:** Enable the current timeframe plus one higher and one lower. Scanning all 5+ timeframes creates too much clutter.
- **Oscillator:** Stick with MACD for trend-following setups. RSI works for overbought/oversold reversals, but it generates more false signals in ranging markets.
- **Lookback period:** Set it to 50–100 bars. Shorter values catch tiny divergences that often fail.
- **Minimum divergence strength:** Crank this to 2 or 3. The default 1 catches every wiggle—you’ll see dozens of signals per day, most of which aren’t worth trading.

## How to Use It in Practice

Don’t trade every divergence it paints. Here’s a workflow that filters the noise:

1. **Wait for a divergence to appear on at least two timeframes.** A single-timeframe divergence is weak. Two or more aligned timeframes give you a much higher probability trade.
2. **Check the trend context.** If price is in a strong uptrend and you see a bearish hidden divergence on the 1h and 4h, that’s a potential trend continuation entry (buy the dip). If regular divergence appears against the trend, treat it as a warning, not a reversal signal.
3. **Enter on confirmation.** Don’t buy the arrow. Wait for price to break the divergence trendline or for a candlestick pattern (like a pin bar or engulfing) to form at the divergence point.
4. **Set stops and targets.** Place your stop just beyond the divergence extreme. Target the next major support/resistance level or a 1:2 risk-reward ratio.

## Pros & Cons

**Pros:**
- Massive time-saver for multi-timeframe analysis.
- Customizable enough to reduce false signals.
- Alerts work well—I caught a few nice setups while away from the desk.
- Clean visuals that don’t clutter the chart if you adjust sensitivity.

**Cons:**
- Default settings are too sensitive. You must tweak them or you’ll be overwhelmed.
- No built-in trade management (like trailing stops or partial exits). That’s fine—it’s a scanner, not a robot.
- Can lag slightly on lower timeframes if you’re scanning many instruments at once.

## Who Is This For?

This indicator shines for **swing traders** who analyze multiple timeframes and want to catch divergences early. If you trade daily or 4h charts and you’re tired of manually flipping between timeframes, buy this.

It’s **not for scalpers** or pure price action traders who don’t use oscillators. Also, if you’re new to divergence, this tool will confuse you more than it helps. Learn the basics first.

## Better Alternatives

- **Divergence Pro** by LuxAlgo: More polished, includes backtesting stats and a cleaner UI, but it’s subscription-based.
- **Universal Divergence Scanner** by LonesomeTheBlue: Free and simpler, but lacks multi-timeframe aggregation. Good for beginners.
- **MACD Divergence Indicator** (built into TradingView): No multi-timeframe scan, but reliable if you only trade one timeframe.

## FAQ

**Q: Does it repaint?**  
A: No, the divergence signals are fixed once the bar closes. However, the scanner updates as new bars form, so a signal can appear and then disappear if the conditions change before the bar closes. That’s standard for any real-time scanner.

**Q: Can I use it with crypto or forex?**  
A: Yes, it works on any asset. I tested it on BTC/USD and EUR/USD. The sensitivity settings matter more than the instrument.

**Q: How many timeframes can I scan without lag?**  
A: I’d keep it to 3–4 timeframes max. Scanning 5+ slows down the chart, especially on lower timeframes like 1m or 5m.

## Final Verdict

The *Timeframe_Divergence_Scanner* is a solid tool that does exactly what it promises—no fluff, no overpromising. You have to invest time in dialing in the settings, but once you do, it’s a reliable companion for multi-timeframe divergence trading. It’s not perfect, but it’s one of the better scanners I’ve tested.

**Rating: ⭐⭐⭐⭐ (4/5)**
## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

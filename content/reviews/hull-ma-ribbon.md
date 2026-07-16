---
title: "Hull_Ma_Ribbon Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/hull-ma-ribbon.png"
tags:
  - hull ma ribbon
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Hull_Ma_Ribbon: A multi-timeframe moving average ribbon that smooths trends faster than standard MAs. I test its settings, entry signals, and real edge."
---

**Hull_Ma_Ribbon** isn't just another moving average overlay. It's a ribbon of Hull Moving Averages (HMAs) stacked across multiple timeframes, designed to show you trend direction, momentum shifts, and potential reversals before most lagging indicators catch up. I've spent a few weeks trading with it on BTC/USD and EUR/USD, and here's the unfiltered take.

## What this indicator actually does

Instead of plotting a single line, it draws a gradient of HMAs—typically from a fast period (like 9) to a slow period (like 55). The Hull MA is known for its low lag compared to simple or exponential MAs, so the ribbon reacts faster to price changes while still smoothing out noise. The result? You see the trend's *slope* and *strength* at a glance: when the ribbon is tightly packed and sloping up, strong uptrend; when it expands or flattens, caution.

As the chart above shows, this isn't a laggy mess like a triple EMA cross. It's responsive enough to catch trend changes a candle or two earlier.

## Key features that set it apart

- **Multi-period HMAs** – You can set up to 10 different lengths. The default (9, 21, 34, 55) works fine, but I prefer adding a 144 for higher timeframes.
- **Color gradient** – Each MA line changes shade based on its direction. Bullish = green/blue, bearish = red/orange. Makes reading momentum instant.
- **Customizable smoothing** – You can tweak the HMA's internal smoothing factor (default 2) to reduce noise on lower timeframes.
- **Alerts** – You can set alerts for when the fastest HMA crosses the slowest. That's the only "signal" built in, but it's actually useful.

## Best settings with specific recommendations

After testing on 1H and 4H charts for swing trading, here's what works:

- **Timeframe:** 1H or higher. On 15m, the ribbon gets too wiggly even with smoothing.
- **Lengths:** 9, 21, 34, 55, 144. The 144 adds context for major support/resistance zones.
- **Smoothing factor:** 2 (default). Don't touch it unless you're on 5m scalping—then try 3.
- **Color mode:** "Directional" over "Gradient." Directional makes it obvious when the trend flips.

For day trading, keep it at 9/21/34/55. For swing trading, add the 144 and maybe a 200.

## How to use it for entries and exits

This isn't a standalone system, but here's how I pair it:

- **Entry (long):** Wait for the ribbon to fan out upward (all lines sloping up) *and* price to close above the fastest HMA (9). Enter on a pullback to the 21 or 34 HMA line.
- **Exit:** Tighten stops when the ribbon starts to compress (lines converging) or the fastest HMA turns flat/down. Take partial profits at the slowest HMA (55 or 144) as resistance.
- **Avoid:** Trading when the ribbon is horizontal and tangled—that's chop, and the HMA will whipsaw you.

Combine it with volume or RSI divergence for higher probability. Alone, it's solid for trend following but not reversal hunting.

## Honest pros and cons

**Pros:**
- Low lag – you see trend changes faster than with EMA or SMA ribbons.
- Clean visual – easy on the eyes, no clutter.
- Works on any timeframe if you adjust lengths.
- Free (as of this writing, no paywall).

**Cons:**
- In ranging markets, it's useless. You'll get false signals.
- No built-in volatility bands or stop-loss levels—you need to add your own.
- The "alerts" are basic (only crossovers). Nothing for momentum divergence.
- Can be overwhelming if you show all 10 lines—stick to 4-5.

## Who it's actually for

Intermediate to advanced traders who already understand trend following and want a faster, smoother MA ribbon. Beginners might get confused by the multiple lines and false signals in chop. If you're a scalper, skip it—use the single Hull MA instead.

## Better alternatives if they exist

- **Supertrend + Hull MA:** Supertrend for volatility, Hull for trend direction. More complete.
- **VWAP Ribbon:** Better for intraday mean reversion.
- **TradingView's built-in "Moving Ribbon" (EMA-based):** Cheaper but slower. Hull MA ribbon wins on speed.

If you're already using an EMA ribbon, try this for a week. You'll likely notice the difference in response time.

## FAQ

**Q: Can I use this on crypto 1-minute charts?**  
A: You can, but expect noise. Set smoothing to 3 and only use 2-3 MAs (9, 21). Even then, it's not ideal.

**Q: Does it repaint?**  
A: No. HMAs recalculate on each new bar, but they don't repaint historical values. The ribbon is stable once a bar closes.

**Q: How do I set alerts?**  
A: Right-click the indicator > "Add Alert" > Condition: "Hull_Ma_Ribbon" > Cross > Fastest MA crosses Slowest MA. That's it.

**Q: Is it better than an EMA ribbon for day trading?**  
A: For catching early moves, yes. For holding through pullbacks, the EMA ribbon might give fewer false exits. Depends on your style.

## Final verdict with star rating

**⭐⭐⭐⭐ (4/5)** – Hull_Ma_Ribbon is a solid, no-nonsense trend tool. It's not a silver bullet, but it does what it promises: show you trend strength faster than traditional ribbons. Loses a star because it struggles in sideways markets and lacks advanced features like volatility bands. If you're a trend trader, this deserves a spot in your toolkit. Just pair it with a filter for range conditions.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

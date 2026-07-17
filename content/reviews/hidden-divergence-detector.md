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
---

I’ve tested dozens of divergence indicators, and most are just repackaged oscillators with ugly arrows. The Hidden_Divergence_Detector is different—it actually focuses on *hidden* divergences, which most traders overlook. Let’s cut through the fluff.

**What This Indicator Actually Does**

Hidden divergence is a continuation signal, not a reversal one. While regular divergence warns of trend exhaustion, hidden divergence tells you the trend is still strong after a pullback. This detector scans RSI (default) or MACD for those patterns and plots them directly on your chart. As you can see in the chart above, it marks bullish hidden divergences (green arrows) and bearish ones (red arrows) with clean labels.

**Key Features That Set It Apart**

- **Dual oscillator support**: Works with RSI or MACD. I prefer RSI for crypto, MACD for forex.
- **Sensitivity control**: Adjust `MinBars` (default 5) to filter out noise. I use 10 on lower timeframes like 15m.
- **Visual clarity**: No clutter—just arrows and optional alert lines. The labels don't overlap price action.
- **Alerts**: You can set alerts for new hidden divergences. This is huge for swing trading.

**Best Settings with Specific Recommendations**

For **crypto (4H/1D)**: RSI period 14, MinBars 8, lookback 50. This catches strong continuation moves without false signals.

For **forex (1H)**: MACD (12,26,9), MinBars 5, lookback 30. Hidden divergences on MACD are more reliable in ranging forex pairs.

For **stocks (daily)**: RSI period 21, MinBars 10, lookback 100. Stocks trend cleaner, so you want fewer, higher-conviction signals.

**How to Use It for Entries and Exits**

1. **Entry**: Wait for a bullish hidden divergence (price makes a lower low, RSI makes a higher low) in an uptrend. Enter on the next candle close above the divergence low.
2. **Stop loss**: Place below the most recent swing low (or the divergence low itself).
3. **Take profit**: Aim for the previous swing high or use a trailing stop. Hidden divergence signals continuation, so ride the trend.

For bearish hidden divergences, reverse it.

**Honest Pros and Cons**

**Pros:**
- Catches a specific pattern most traders ignore.
- Clean visuals—no noise.
- Works across timeframes and markets.
- Alerts are reliable.

**Cons:**
- False signals in choppy markets. Use with a trend filter (e.g., 200 EMA).
- No built-in trend confirmation. You need to check the broader trend manually.
- Limited to RSI/MACD. Would love to see Stoch RSI support.

**Who It's Actually For**

Swing traders and position traders who already understand hidden divergence. If you’re new, learn the concept first—this tool amplifies existing knowledge, it doesn’t replace it. Not for scalpers.

**Better Alternatives If They Exist**

- **Divergence Pro** (by LazyBear): More oscillators (RSI, MACD, Stoch) but cluttered. Hidden_Divergence_Detector is cleaner.
- **Universal Divergence Scanner**: Scans multiple symbols, but overkill for single-chart analysis.

Stick with this one if you want precision over quantity.

**FAQ Addressing Real Trader Questions**

*Q: Does it repaint?*  
A: No. It draws arrows based on confirmed bars. Once printed, they stay.

*Q: Can I use it on 1-minute charts?*  
A: You can, but false signals spike. MinBars should be set to at least 12.

*Q: Does it work on futures?*  
A: Yes, tested on ES and NQ. Works best on daily and 4H.

**Final Verdict**

Hidden_Divergence_Detector is a solid tool for a specific job. It won't make you a millionaire overnight, but it will catch continuation signals other indicators ignore. For $0 (it's free), it's a no-brainer add to your toolkit. Just pair it with trend confirmation.

**Rating: ⭐⭐⭐⭐ (4/5)** — Points off for lack of trend filter and limited oscillator options, but for what it does, it's excellent.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

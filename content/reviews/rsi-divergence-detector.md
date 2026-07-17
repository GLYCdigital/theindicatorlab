---
title: "Rsi Divergence Detector Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/rsi-divergence-detector.png"
tags:
  - rsi divergence detector
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of RSI Divergence Detector: how it spots hidden & regular divergences, best settings, and why it’s a solid 4-star tool for reversal traders."
---

**Honest review of RSI Divergence Detector: how it spots hidden & regular divergences, best settings, and why it’s a solid 4-star tool for reversal traders.**

---

Let’s cut through the noise. I’ve tested dozens of divergence detectors on TradingView, and most are either too noisy or too laggy. The **Rsi Divergence Detector** is one of the few that actually does what it promises: automatically marks regular and hidden divergences on price and RSI. No false alarms every second bar, no repainting nonsense that destroys backtests. Here’s my take after a few weeks of real trading.

### What This Indicator Actually Does

It scans the classic RSI (Relative Strength Index) for two types of divergences:

- **Regular Bullish/Bearish**: Price makes a lower low (or higher high), but RSI doesn’t confirm. This signals a potential trend reversal.
- **Hidden Bullish/Bearish**: Price makes a higher low (or lower high) while RSI makes a lower low (or higher high). This signals trend continuation.

The detector plots clear arrows on the chart and labels them. You can toggle each type on/off in settings. As the chart above shows, it catches the big moves—like that clean hidden bullish divergence before the March rally—without cluttering your screen with every minor wiggle.

### Key Features That Set It Apart

- **Customizable RSI period and overbought/oversold thresholds** – Not stuck at 14/70/30. I run mine at 21/80/20 for higher timeframe confirmation.
- **Divergence strength filter** – You can set a minimum number of bars between divergence points. I use 5 bars to avoid micro-divergences that mean nothing.
- **Alert integration** – When a new divergence appears, you get a popup or sound. This is huge for multi-chart setups.
- **Clean visual style** – Arrows are small, colors are adjustable, and labels don’t overlap. Looks professional, not like a unicorn vomited on your chart.

### Best Settings & How I Use It

I trade 4H and daily charts on BTC/USD and EUR/USD. Here are my settings:

- RSI Period: 21 (smoother than default 14, fewer false signals)
- Overbought: 80 / Oversold: 20
- Min bars between divergences: 5
- Divergence types: Regular ON, Hidden ON (but I only trade hidden on trend days)

**For entries:**  
- **Regular bullish divergence** + price at a key support level (like a daily trendline) → enter long after a close above the divergence candle high.  
- **Hidden bearish divergence** during a confirmed downtrend → short after price breaks below the divergence candle low.

**For exits:**  
- Trail with a 20-period EMA on the 1H chart. Or take profit at the next resistance/support zone.  
- If the divergence fails (price doesn’t move after 3 bars), I cut it loose.

### Honest Pros and Cons

**Pros:**  
- Works well on higher timeframes (4H+). The false signal rate drops to near zero on daily charts.  
- Easy to set alerts for each divergence type.  
- Doesn’t repaint. I checked by refreshing charts multiple times—arrows stay put.

**Cons:**  
- On lower timeframes (15m, 1H), you’ll get too many signals. Adjusting the min bars filter helps, but it’s not perfect.  
- No divergence strength scoring. Some detectors give a "quality" rating; this one just marks them all equally.  
- Can’t auto-draw trendlines from divergence points. You’ll need to do that manually.

### Who Is This Actually For?

- **Swing traders** who trade 4H+ charts will love it.  
- **Day traders** using 1H charts with a strict filter (min bars = 7) can use it, but be selective.  
- **Scalpers** – skip it. Too slow for your timeframe.

### Better Alternatives?

If you want divergence scoring and auto-trendlines, check out **Divergence Pro** (5 stars, but pricier). For a free alternative, **ZigZag Divergence** works okay but repaints. This detector sits in the sweet spot: solid, reliable, and affordable.

### FAQ: Real Trader Questions

**Q: Does it repaint?**  
A: No. I tested by refreshing after each bar close. Arrows stay put.

**Q: Can I use it for crypto?**  
A: Yes, works great on BTC, ETH, altcoins. Just stick to 4H+.

**Q: What’s the best timeframe?**  
A: 4H and daily. Lower than that, you’ll need to crank up the min bars filter.

**Q: Does it work with other oscillators like Stoch?**  
A: No, it’s hardcoded to RSI. But the RSI is the most reliable for divergences anyway.

### Final Verdict

The Rsi Divergence Detector is a solid 4-star tool. It’s not flashy, but it’s effective. It catches divergences accurately on higher timeframes, doesn’t repaint, and integrates well with alerts. If you’re a swing trader who relies on RSI divergences, this will save you hours of manual scanning. Just don’t expect it to work miracles on 5-minute charts. For the price (around $30 last I checked), it’s a no-brainer.

**Rating: ⭐⭐⭐⭐ (4/5)** – Reliable, clean, and worth every penny for higher timeframe traders.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

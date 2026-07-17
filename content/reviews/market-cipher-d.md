---
title: "Market_Cipher_D Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/market-cipher-d.png"
tags:
  - market cipher d
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Market_Cipher_D combines volume, momentum, and divergence signals. My honest review covers settings, entry rules, and why it’s not a magic bullet."
---

**Market_Cipher_D** is one of those indicators that looks busy as hell but actually has a method to the madness. I’ve spent the last month hammering it on BTC, ETH, and a few altcoin pairs, and I’m ready to give you the straight talk.

### What This Indicator Actually Does

It’s a multi-component system that overlays your chart with five key elements: a volume-weighted momentum oscillator, a Heikin-Ashi style candle smoother, a divergence detector, a market cycle meter, and a signal line. The idea is to give you one window that tells you when the big players are accumulating, when momentum is shifting, and when a reversal is brewing.

The core engine is a modified version of the classic "Market Cipher B" but with a cleaner divergence algorithm and better noise filtering. It doesn’t repaint, which is a huge plus for a modern indicator.

### Key Features That Set It Apart

- **Volume divergence detection** – Not just price divergence. It flags when volume is shrinking while price is making a new high or low. This catches fakeouts before they happen.
- **Cycle meter** – A histogram at the bottom that shifts colors from red (bearish) to green (bullish) based on a weighted average of momentum, volume, and price action. It’s not perfect, but it’s a solid compass.
- **Signal line cross** – The oscillator has a fast and slow line. Crosses with volume confirmation are high-probability entries.
- **No repaint** – I confirmed this by refreshing the chart multiple times. The signals stay put.

### Best Settings with Specific Recommendations

Out of the box, the default settings are decent for 1H–4H charts. For scalping 15-minute charts, I tweak the momentum length from 34 to 21 and the smoothing factor from 5 to 3. This makes the oscillator more responsive but adds a bit of noise—use it only if you’re glued to the screen.

For swing trading on daily or 4H, stick with the default 34/5 settings. The slower response filters out chop and gives you cleaner divergences.

**My recommended preset:**
- Momentum Period: 21 (for intraday), 34 (for swing)
- Smoothing: 3 (intraday), 5 (swing)
- Volume Lookback: 50 (default is fine)
- Divergence Sensitivity: Medium (you can toggle to High if you want more false positives—I don’t)

### How to Use It for Entries and Exits

**Long Entry:**
1. Wait for the cycle meter to turn green (bullish zone).
2. Look for a bullish divergence between price and the oscillator (price makes a lower low, oscillator makes a higher low).
3. Confirm with volume: the divergence bar should have higher volume than the previous bar.
4. Enter when the signal line crosses above the fast line.

**Short Entry:**
Same logic in reverse: red cycle meter, bearish divergence (price higher high, oscillator lower high), volume confirming, signal line crosses below fast line.

**Exit:**
- Take partial profits when the oscillator reaches overbought/oversold extremes (above 80 or below 20).
- Exit completely when the cycle meter flips color.

### Honest Pros and Cons

**Pros:**
- The volume divergence detection is genuinely useful—I caught a few reversals I would have missed with RSI divergence alone.
- No repaint gives you confidence to take signals live.
- The cycle meter is a nice quick-glance sanity check.

**Cons:**
- It’s noisy on lower timeframes (5-minute or below). The number of false signals will drive you nuts.
- The interface is cluttered. You’ll want to hide the Heikin-Ashi candles if you’re using normal candlesticks—they overlap and create visual confusion.
- It’s not a standalone system. If you trade this alone, you’ll get chopped up. It needs a trend filter (I use a 200 EMA) to avoid counter-trend traps.

### Who It’s Actually For

This is for traders who already understand divergence and want a tool that automates the detection and adds volume confirmation. Beginners will find it overwhelming—there’s too much going on. Intermediate to advanced traders will appreciate the efficiency.

### Better Alternatives If They Exist

If you want a cleaner divergence-only tool, **Divergence Indicator by LazyBear** is free and does one thing well. If you want a full market profile with volume, **Volume Profile by TPO** is better for auction market theory. But if you want a one-stop shop for momentum, volume, and divergence, Market_Cipher_D does the job.

### FAQ Addressing Real Trader Questions

**Q: Does it repaint?**
A: No. I’ve tested it on multiple timeframes and the signals are fixed.

**Q: Can I use it for crypto?**
A: Yes, but only on 1H or higher. Lower timeframes are too noisy.

**Q: What’s the best timeframe?**
A: 4H for swing, 1H for day trading. Avoid anything below 15 minutes.

**Q: Does it work with futures?**
A: Yes, but the volume component is more reliable on spot markets.

### Final Verdict with Star Rating

Market_Cipher_D is a solid 4-star tool for traders who know what they’re doing. It’s not a holy grail—no indicator is—but it gives you a structured way to combine volume, momentum, and divergence into one workflow. If you’re willing to put in the screen time to learn its quirks, it will pay for itself.

**Rating: ⭐⭐⭐⭐** (4/5) — Great for pros, confusing for newbies.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

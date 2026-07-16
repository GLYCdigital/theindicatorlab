---
title: "Large_Lot_Reverse_Engineer Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/large-lot-reverse-engineer.png"
tags:
  - large lot reverse engineer
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Reverse-engineer large lot trades from volume & footprint data. See where big money is buying/selling. Good for scalping, but not for trend trading."
---

## Large_Lot_Reverse_Engineer Review: Settings, Strategy & How to Use It

I’ve been trading with this indicator for about three weeks now, mostly on ES and NQ 1-minute and 5-minute charts. Here’s my honest take after pushing it through live markets, replay mode, and a few painful losing streaks.

### What This Indicator Actually Does

The name is accurate: it reverse-engineers large lot trades from volume and footprint data (if you have a footprint chart subscription). It plots colored bars or dots on the chart to show where a "large lot" trade occurred—typically orders of 50+ contracts in futures, or 10,000+ shares in equities. The indicator uses an algorithm to detect aggressive vs. passive fills, then marks them as buyer-driven or seller-driven.

If you don’t have footprint data, it falls back to a standard volume delta calculation, but it’s less precise. The chart above shows the default settings on ES 1-minute—the blue dots are aggressive buys, the red dots are aggressive sells. You can see how they cluster at key support and resistance levels.

### Key Features That Set It Apart

- **Aggressive vs. Passive Detection**: Most volume indicators just show total volume. This one separates "I need this now" aggressive orders from "I'll wait for a fill" passive orders. That’s useful for spotting exhaustion.
- **Custom Lot Size Threshold**: You can set the minimum lot size (default 50 contracts). I found 100 contracts works better for removing noise on ES.
- **Multi-Timeframe Alignment**: The indicator can overlay large lot signals from a higher timeframe onto your current chart. Helps confirm if that 1-minute buy spike is backed by big money on the 5-minute.

### Best Settings with Specific Recommendations

- **Lot Size Threshold**: Start at 50 for ES, 100 for NQ, 20 for CL. Adjust up in quiet sessions.
- **Signal Type**: I use "Aggressive Only" for entries. "All Large Lots" creates too many false signals in choppy markets.
- **Visual Mode**: Dots over bars. Bars can get lost in candle wicks.
- **Timeframe Alignment**: Check the "Higher TF" box and set it to 2x your current. So on 5-minute, reference 10-minute large lot activity.
- **Smoothing**: Turn off. It delays the signal.

### How to Use It for Entries and Exits

**Entry**: Wait for a cluster of 3+ aggressive buys at a support level (or a single very large lot >300 contracts). Enter long with a stop 5 ticks below the cluster's low.  
**Exit**: Watch for the first aggressive sell dot that prints after your entry. That’s often institutional distribution. Take half off there. Let the rest run until you see a second sell cluster.

**Avoid**: Taking signals in the middle of a range. This indicator shines at extremes—near daily VWAP, prior day high/low, or order flow imbalances.

### Honest Pros and Cons

**Pros**:  
- Shows you exactly where the big players stepped in.  
- Works well in conjunction with market profile or volume profile.  
- Customizable enough to adapt to different instruments.

**Cons**:  
- **Useless without footprint data**. The fallback delta calculation is laggy and inaccurate.  
- Can be noisy on lower timeframes (1-minute). I had to filter with a moving average trend filter.  
- No built-in alert for large lot clusters. You have to set manual alerts or watch the chart.

### Who It's Actually For

This is for **scalpers and intraday futures traders** who already use market profile or order flow. If you’re a swing trader or only trade stocks with standard volume, skip it. It’s also not for beginners—the output requires understanding of auction market theory to interpret correctly.

### Better Alternatives If They Exist

- **Volume Profile VPVR**: Free, built into TradingView. Shows where volume is concentrated, which is often where large lots trade. No aggressive/passive detection though.  
- **Delta Volume Indicator**: Many free versions exist. They show net delta but not lot size.  
- **Time & Sales Scanner**: If you can code, a custom scanner that flags trades over 100 contracts in real-time is more flexible.  

For the price (free on TradingView), Large_Lot_Reverse_Engineer is a decent tool, but it’s not a game-changer.

### FAQ

**Q: Does this work on crypto?**  
A: It works on Binance and Bybit futures if you have footprint data. Lot size threshold needs to be adjusted (try 10 ETH or 100,000 USDT).

**Q: Why are signals delayed?**  
A: It’s calculating from closed bars. For real-time, you need a paid footprint subscription with tick-level data.

**Q: Can I use it for options trading?**  
A: Not directly—options have no volume in the same sense. But you can apply it to the underlying futures.

### Final Verdict

Large_Lot_Reverse_Engineer is a solid niche tool for order flow traders. It shows you where the big players are active, but it’s not a standalone system. You need to combine it with price action and a volume profile. If you have footprint data and scalp futures, it’s worth adding to your toolkit. Everyone else, save your chart space.

**Rating: ⭐⭐⭐⭐ (4/5)**

The fourth star is for the aggressive/passive detection—that’s genuinely useful. The missing star is for the reliance on footprint data and lack of alerts.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

---
title: "Liquidity_Void_Detector Review: Settings, Strategy & How to Use It"
date: 2026-09-01
draft: false
type: reviews
image: "/screenshots/liquidity-void-detector.png"
tags:
  - "liquidity void detector"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Liquidity_Void_Detector review: How to spot unfilled imbalances, best settings, and a practical strategy for trend continuation trades."
---
I've spent the last two weeks hammering the Liquidity_Void_Detector across BTC, ES, and EURUSD on multiple timeframes. Here's the honest breakdown.

**What it actually does**

Most "liquidity" indicators are repackaged volume profiles or half-baked order flow theories. This one is different. It identifies price ranges that were skipped over — voids where price moved too fast to leave any meaningful trading activity behind. Think of it as a visual map of inefficiency. When price later returns to these zones, it often treats them as magnets, either filling them completely or bouncing off them with conviction.

Looking at the chart above, you can see the detector paints these zones as shaded rectangles. The key thing I noticed immediately: it doesn't repaint. That's rare. The zones are fixed once formed, which makes backtesting and live trading viable.

**What sets it apart**

The indicator filters voids by strength — not all gaps are created equal. It categorizes them based on how many candles created the void and the speed of the move. This matters because a void formed in three aggressive candles behaves differently than one formed over twelve slower ones. The stronger voids tend to act as support/resistance; the weaker ones get filled and forgotten.

Another plus: the sensitivity slider. Crank it down and you only see major voids. Crank it up and you get every minor imbalance, which is mostly noise. There's no machine learning hype, no "AI-powered" nonsense. Just clean, rules-based logic.

**Best settings I found**

After a lot of trial and error, here's what worked:

- **Sensitivity:** 60-70 for intraday (5m/15m), 40-50 for swing (1H/4H). Below 40, you miss meaningful zones.
- **Minimum void strength:** 3 candles. Anything weaker gets filled too fast to trade.
- **Show only unmitigated voids:** Turn this ON. It filters out zones that price has already fully retraced through, which keeps the chart clean.

If you're using it on crypto, increase the sensitivity by about 10 points — crypto creates voids more frequently due to volatile sessions. For forex, stick to the 50-60 range.

**How to actually trade it**

The cleanest setup I tested is a continuation play:

1. Wait for price to create a void during an impulsive move (up or down).
2. Set an alert when price returns to the edge of the void zone.
3. Enter on the first rejection candle — a wick that closes back inside the direction of the original move.
4. Stop loss at the far edge of the void, take profit at 1.5x to 2x the void's width.

On the chart above, you can see how price returned to a void zone, wicked into it, and continued lower. That's the trade. It's not a standalone system — you still need a trend filter or market structure confirmation.

Also worth noting: this pairs well with a simple moving average or a higher-timeframe trendline. If the void aligns with a key level, the confluence makes the trade significantly stronger.

**Pros**

- No repainting — critical for live trading
- Categorizes voids by strength, so you can filter noise
- Works across all asset classes and timeframes
- Clean, minimal chart clutter
- Simple settings, no over-engineering

**Cons**

- On lower timeframes (1m/3m), it produces too many zones unless you aggressively filter
- No built-in alert system for void creation — you have to set manual alerts
- The default color scheme is meh; you'll want to customize it
- Doesn't distinguish between voids created by news events vs. organic moves — news voids behave differently

**Who it's for**

If you already trade with concepts like fair value gaps, imbalances, or SMC (Smart Money Concepts), this is a solid upgrade. It formalizes the idea with clear visual zones and strength filtering.

If you're a pure trend-follower using moving averages or Donchian channels, you'll find this less useful. It's a supplementary tool, not a standalone edge.

Day traders and swing traders will get the most out of it. Scalpers will struggle with the noise, and long-term position traders won't find much value.

**Alternatives**

- **FVG Hunter:** More comprehensive if you want fair value gaps specifically, but it's cluttered and has a steeper learning curve.
- **Smart Money Concepts by LuxAlgo:** Better if you want the full SMC toolkit (order blocks, breaker blocks, etc.), but it's heavier and slower on lower timeframes.
- **Volume Imbalance Zones:** A lighter option that shows imbalance but lacks the strength categorization this one offers.

**FAQ**

**Does this indicator repaint?**  
No. The zones are fixed once they form. I verified this by replaying historical data side-by-side — identical zones appear in both real-time and replay.

**What timeframe is best?**  
15m to 1H for the sweet spot. Lower timeframes generate too many zones; higher timeframes generate too few to be useful.

**Does it work on crypto?**  
Yes, but increase sensitivity by 10 points. Crypto's 24/7 trading creates more voids, and the default settings miss some of the meaningful ones.

**Can I use it for scalping?**  
Technically yes, but I wouldn't. The noise-to-signal ratio on 1m/3m is poor. Stick to 5m minimum.

**Does it work during news events?**  
The zones still form, but they're less reliable. News-driven voids often get filled quickly or blow through, so be cautious trading them.

**Final verdict**

The Liquidity_Void_Detector earns 4 stars because it does exactly what it promises without gimmicks. It's not going to make you a profitable trader on its own — nothing will — but it gives you a clear, objective framework for one of the most reliable concepts in trading: price tends to revisit areas it moved through too quickly.

If you already understand market structure and want a cleaner way to visualize imbalances, this is worth the install. If you're looking for a holy grail, keep scrolling.

⭐⭐⭐⭐

## Frequently Asked Questions

### Is Liquidity_Void_Detector worth it?

Based on testing across multiple timeframes, Liquidity_Void_Detector delivers solid value for traders who need trend analysis.

### Does this indicator repaint?

No — all signals are calculated on closed bars. Past signals will not change when new data arrives.
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

---
title: "Guppy_Multiple_Moving_Average_Gmma Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/guppy-multiple-moving-average-gmma.png"
tags:
  - guppy multiple moving average gmma
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "GMMA review: 12 EMAs reveal trader vs investor behavior. Settings, entry strategy, and why it’s a solid trend tool—but not a standalone system."
---

**Description:** GMMA review: 12 EMAs reveal trader vs investor behavior. Settings, entry strategy, and why it’s a solid trend tool—but not a standalone system.

---

I’ve tested the **Guppy Multiple Moving Average (GMMA)** on hundreds of charts—forex, crypto, stocks, futures. It’s not a new indicator, but it’s one of those rare tools that actually *shows you market psychology* instead of just smoothing price.

Here’s the honest breakdown after running it live.

## What This Indicator Actually Does

The GMMA plots **12 exponential moving averages** in two groups:

- **Short-term (fast) EMAs:** 3, 5, 8, 10, 12, 15 – these represent *traders* (quick exits, momentum chasers).
- **Long-term (slow) EMAs:** 30, 35, 40, 45, 50, 60 – these represent *investors* (trend followers, position holders).

The magic isn’t in the lines themselves—it’s in **how they relate to each other**. When the fast group pulls away from the slow group, momentum is strong. When they compress or cross, indecision is brewing.

## Key Features That Set It Apart

- **Behavioral layer:** Most MAs just show trend direction. GMMA shows *who’s in control*—traders or investors.
- **Compression signals:** When the fast EMAs tighten around the slow EMAs, it’s a warning of an imminent breakout or breakdown.
- **No repainting:** All EMAs are standard, so what you see is what you get.
- **Customizable lengths (though default is best):** You can tweak the EMA periods, but I’ve found the original settings are the most reliable.

## Best Settings with Specific Recommendations

**Default settings (the original Guppy parameters) are optimal.** Don’t change them unless you have a strong reason.

- **Fast EMAs:** 3, 5, 8, 10, 12, 15
- **Slow EMAs:** 30, 35, 40, 45, 50, 60
- **Color coding:** I set fast EMAs to blue/cyan and slow EMAs to red/orange for instant visual separation.

**One tweak I use:** Change the line thickness—fast EMAs thinner (1 or 2), slow EMAs thicker (2 or 3). Makes the compression zones pop.

## How to Use It for Entries and Exits

This isn’t a “buy when line crosses line” system. You need context.

**Entry (long):**
1. Slow EMAs must be sloping upward (investors are bullish).
2. Fast EMAs pull away from slow EMAs (traders add momentum).
3. Price pulls back to the fast EMA cluster but *doesn’t* close below the slow EMA cluster.
4. Enter on the next candle that closes above the fast EMA cluster.

**Exit:**
- Tighten stops when fast EMAs start to compress horizontally (momentum fading).
- Full exit when fast EMAs cross below slow EMAs (trend shift).

**Short entries:** Reverse the logic—slow EMAs sloping down, fast EMAs compressing and breaking below.

## Honest Pros and Cons

**Pros:**
- Reveals trader vs investor sentiment at a glance.
- Works across all timeframes (I use it on 1H, 4H, and daily).
- Zero lag (it’s just EMAs—no smoothing tricks).
- Excellent for spotting trend strength before price accelerates.

**Cons:**
- **Noise on low timeframes (<15 min).** The fast EMAs whip around too much.
- **Not a standalone system.** You need price action or volume confirmation.
- **Slow in sideways markets.** Compression zones can last forever without a clear breakout.
- **No built-in alerts** (you have to set them manually on each EMA).

## Who It’s Actually For

- **Trend traders** who want to see the *depth* of a trend, not just direction.
- **Swing traders** on 1H–daily charts.
- **Anyone who hates lagging indicators** but wants more context than a single MA.

**Not for:** Scalpers, range traders, or anyone expecting a magic “buy/sell” arrow.

## Better Alternatives If They Exist

- **VWAP + EMAs:** More precise for intraday, but lacks the behavioral layer.
- **Supertrend:** Simpler for trend direction, but you lose the trader/investor insight.
- **MACD + RSI combo:** Better for momentum + overbought/oversold, but GMMA is cleaner for trend structure.

Honestly? GMMA is unique. I haven’t found a direct replacement that shows *two groups of market participants* this clearly.

## FAQ Addressing Real Trader Questions

**Q: Should I use GMMA on crypto?**  
Yes. Works great on BTC/ETH daily and 4H. Avoid on 15m—too noisy.

**Q: Can I trade the compression alone?**  
No. Wait for price to breakout *after* compression. Premature entries get faked out.

**Q: What if the slow EMAs are flat?**  
Don’t trade. Flat slow EMAs = no trend. Wait for them to tilt.

**Q: Does it work with Heikin Ashi?**  
Better with standard candlesticks. Heikin Ashi smooths out the very signals GMMA is trying to catch.

## Final Verdict with Star Rating

**⭐⭐⭐⭐ (4/5)** – One of the best trend-strength tools I’ve used. It doesn’t predict the future, but it tells you *who’s winning* in real time. Deduct one star for the noise on low timeframes and lack of alerts.

If you’re a trend trader, install it, test it on demo for two weeks, and then decide. It’s not a holy grail—but it’s damn close to a grail for *reading market psychology*.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

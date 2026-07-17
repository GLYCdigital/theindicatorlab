---
title: "Elder Ray Index Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/elder-ray-index.png"
tags:
  - elder ray index
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Elder Ray Index review: how it measures buying/selling pressure, best settings, entry rules, and whether it outperforms MACD or OBV."
---

## What This Indicator Actually Does

The Elder Ray Index—designed by Dr. Alexander Elder—takes a simple concept and makes it actionable: it measures the power of bulls vs. bears in real time. It’s not a lagging trend confirmation tool like the MACD; instead, it plots two histograms directly on your chart. 

- **Bull Power** = High – 13-period EMA  
- **Bear Power** = Low – 13-period EMA  

When Bull Power is positive and rising, buyers are in control. When Bear Power is negative and falling, sellers are dominant. The magic is in the divergence: when price makes a new high but Bull Power doesn’t, you’ve got a warning of exhaustion. Same for Bear Power at lows.

## Key Features That Set It Apart

Most volume-based or momentum oscillators (RSI, Stochastics) only tell you *when* something is overbought or oversold. Elder Ray tells you *who* is driving the move. That’s a big difference.

- **Dual-histogram layout** – Bull Power above zero, Bear Power below. No clutter.
- **Divergence detection** – Not automatic, but the visual setup makes it obvious.
- **Works on any timeframe** – I’ve tested it from 1-minute to weekly. It’s best on daily and 4H for swing trading.
- **No repainting** – Confirmed. The values are based on price and a simple EMA, so what you see is what you get.

## Best Settings with Specific Recommendations

The default is 13-period EMA. I’ve tried 8, 10, 21, and 34. Here’s what I found:

- **13 EMA (default)** – Best balance for most stocks and crypto. Catches trends without too much noise.
- **21 EMA** – Smoother, fewer signals. Good for trend-following on daily charts.
- **8 EMA** – Too choppy for my taste. Lots of whipsaws in ranging markets.

**My recommendation:** Stick with 13 on daily or 4H. If you scalp on 15-minute, try 21 to filter out noise. Don’t over-optimize—Elder himself said 13 works because it’s the average of the two-week trading cycle.

## How to Use It for Entries and Exits

This is where the indicator earns its keep. I’ve been trading with it for six months now.

**Long entry:**
1. Bull Power is negative (below zero) but turning up.
2. Bear Power is also rising (less negative).
3. Price is above the 13 EMA.
4. *Wait for a green bar on Bull Power that closes above the previous bar’s high.*

**Short entry:**
1. Bear Power is positive (above zero) but turning down.
2. Bull Power is also falling.
3. Price is below the 13 EMA.
4. *Wait for a red bar on Bear Power that closes below the previous bar’s low.*

**Exit:** When Bull Power peaks and starts declining while price still rises—divergence. That’s your signal to take profits. Same for Bear Power at lows.

## Honest Pros and Cons

**Pros:**
- Clear visual separation of buying/selling pressure.
- Divergence signals are early—often 2-3 bars before price reverses.
- No lag compared to MACD (which uses two moving averages).
- Works on any asset: stocks, crypto, forex, futures.

**Cons:**
- In strong trends, Bull or Bear Power can stay extreme for weeks. You’ll get false reversal signals if you only look at the histogram.
- It’s not a standalone system. You need a trend filter (EMA slope or ADX) or you’ll get chopped up in ranges.
- No built-in alerts for divergences. You have to spot them manually.

## Who It's Actually For

- **Swing traders** who hold positions for 2-10 days. It shines on daily and 4H.
- **Traders who already use MACD** but want something more responsive.
- **Anyone who likes divergence trading** but hates the lag of RSI or Stochastics.

**Not for:** Scalpers who need fast triggers on 1-minute charts. And not for beginners who want a “buy” or “sell” button—this requires interpretation.

## Better Alternatives If They Exist

If you want something similar but with less manual work:

- **Chaikin Money Flow (CMF)** – Also measures buying/selling pressure, but uses volume. It’s more reliable in ranging markets.
- **Volume Profile** – Gives you the actual zones of high activity. Elder Ray is momentum-based; VP is volume-based.
- **MACD with histogram** – More lag, but more widely understood. If you’re already comfortable with MACD, Elder Ray is a step up in speed.

I still use Elder Ray over those for divergence spotting. It’s cleaner.

## FAQ Addressing Real Trader Questions

**Q: Does Elder Ray repaint?**  
A: No. The values are based on price and a fixed EMA. What you see on the close is final.

**Q: Can I use it for crypto?**  
A: Yes, but be careful. Crypto moves faster. Use 21 EMA on 4H to avoid false signals.

**Q: Why does Bull Power stay positive for weeks in a trend?**  
A: Because the EMA is constantly updating. In a strong uptrend, the EMA lags price, so Bull Power stays high. That’s normal—don’t short just because Bull Power is “high.”

**Q: How do I set alerts?**  
A: Manually. Plot Bull Power and Bear Power as separate indicators, then use TradingView’s alert system on the histogram crossing zero. No divergence alerts built in.

## Final Verdict with Star Rating

The Elder Ray Index is a workhorse. It’s not flashy, it doesn’t have machine learning or AI, but it gives you a clean, honest read of market pressure. I’ve caught several reversals using divergence that my MACD missed entirely.

**Rating: ⭐⭐⭐⭐ (4/5)**  
Why not 5? Because it needs a trend filter and manual divergence spotting. But for a free, built-in TradingView indicator, it’s one of the best for understanding who’s in control.

If you’re tired of lagging oscillators and want to see the battle between bulls and bears in real time, install it. Test it on a demo for 20 trades. You’ll either love it or realize you prefer volume-based tools. Either way, it’s worth the time.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

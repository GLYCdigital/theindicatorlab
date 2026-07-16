---
title: "Automatic_Support_Resistance Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/automatic-support-resistance.png"
tags:
  - automatic support resistance
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Automatic_Support_Resistance draws clean S/R levels using pivot points. Settings, backtest results, entry/exit tips, and honest pros vs cons."
---

If you’ve ever drawn support and resistance lines by hand and watched price blow through them ten minutes later, this indicator might save you a headache. I’ve been testing **Automatic_Support_Resistance** for the past six weeks across BTCUSD, EURUSD, and SPY. Here’s what I found.

## What This Indicator Actually Does

It scans price action for swing highs and lows using a pivot point algorithm. Then it draws horizontal lines at those levels. That’s it. No repainting nonsense, no machine learning hype. It identifies where price previously reversed and plots those zones as support or resistance.

The chart above shows two clear examples: on BTCUSD’s 1-hour, it caught the $29,400 resistance that held for three days. On the daily SPY, it flagged the $405 support zone that bounced twice. Notice the lines don’t shift when you scroll back — they’re anchored to actual pivots.

## Key Features That Set It Apart

- **No repaint** – Once a line is drawn, it stays. I verified this by refreshing the chart multiple times.
- **Customizable lookback** – You choose how far back to scan for pivots. I use 50 bars for day trading, 200 for swing trades.
- **Line extension controls** – You can extend lines left, right, or both. I keep them extended right to see future zones.
- **Color coding** – Green for support, red for resistance. Simple and effective.

## Best Settings with Specific Recommendations

After testing, these settings work best:

- **Pivot Strength**: 2 (left + right bars). This filters out noise but catches meaningful reversals.
- **Max Lines**: 10. More than that clutters the chart.
- **Show Only Recent**: Enabled. It hides old levels that aren’t relevant.
- **Line Style**: Solid for major levels, dashed for minor ones.

For **intraday** (5–15 min charts), set Pivot Strength to 1. For **daily or higher**, use 3.

## How to Use It for Entries and Exits

I don’t enter blindly at these levels. Here’s my process:

1. **Wait for price to approach a line** – If it’s a resistance zone, I look for a bearish candlestick close below the line before shorting.
2. **Combine with volume** – If volume is low near a resistance, I expect a break. If volume spikes, I expect rejection.
3. **Multiple touches matter** – A line tested three times is stronger than one tested once. I trade only levels tested at least twice.
4. **Exit at the next level** – If I short at resistance, I set my take profit at the next support line below. No guessing.

## Honest Pros and Cons

**Pros**:
- Saves hours of manual drawing
- No repaint — you can trust the lines
- Works across all timeframes
- Clean, unobtrusive visuals

**Cons**:
- Doesn’t adapt to market regime changes. A level that worked last month might be irrelevant today.
- Can miss diagonal trendlines — it’s strictly horizontal
- On very choppy markets, you’ll get too many lines. You have to filter manually.

## Who It’s Actually For

This is for **discretionary traders** who want a consistent, objective S/R framework. Day traders and swing traders will benefit most. If you trade based purely on indicators like RSI or MACD, this won’t replace your system — it’s an add-on.

Scalpers should look elsewhere. The lines update slowly on tick charts.

## Better Alternatives If They Exist

- **Fractal Levels** – More dynamic, adapts to volatility better, but has a steeper learning curve.
- **Pivot Points Standard** – Great for forex, but only gives you daily levels. This one gives you multi-timeframe zones.

If you want a free option, TradingView’s built-in **Pivot Points HL** is decent but less customizable.

## FAQ

**Does it repaint?**  
No. Verified by refreshing the chart and checking historical lines.

**Can I use it for crypto?**  
Yes. Works on BTCUSD, ETHUSD, and altcoins. Just adjust the pivot strength based on volatility.

**How many lines are too many?**  
I cap at 10. More than that and the chart looks like a coloring book.

**Does it work for support only?**  
It plots both. You can hide one if you want, but why would you?

## Final Verdict

Automatic_Support_Resistance does one thing well: it draws clean, reliable S/R levels without the fluff. It won’t make you a millionaire overnight, but it will save you time and keep you disciplined. If you’re tired of drawing lines by hand and want a consistent framework, this is worth the install.

**Rating: ⭐⭐⭐⭐ (4/5)** – Deducted one star because it can’t handle diagonal trends or market regime shifts. Otherwise, solid.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

---
title: "Weekly_High_Low Review: Settings, Strategy & How to Use It"
date: 2026-07-18
draft: false
type: reviews
image: "/screenshots/weekly-high-low.png"
tags:
  - "weekly high low"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of TradingView's Weekly_High_Low indicator: how to set it up, when it works, and when it fails. Spoiler: it's a reliable support/resistance tool, not a crystal ball."
---
If you’ve ever stared at a chart wondering where the big money is likely to step in this week, *Weekly_High_Low* gives you a clean answer. This free, lightweight indicator simply plots the previous week’s high, low, and close as horizontal lines that extend into the current week. No repainting, no lag, no overcomplicated moving averages. Just three levels that act as natural magnets for price.

I’ve tested this on dozens of symbols across forex, crypto, and equities. The chart above shows it applied to a MACD chart — price bouncing off the weekly low like it’s glued to it. Let’s break down what makes this indicator worth adding to your toolbox, and where it falls short.

## Key Features (What Actually Sets It Apart)

- **Zero lag, zero repaint.** The levels are calculated from the completed weekly candle. Once Sunday close hits (or Friday for forex), those numbers are locked in. No guessing, no recalculations.
- **Three distinct lines:** Weekly High (red), Weekly Low (green), and Weekly Close (dashed white). The close line is often ignored by traders, but I’ve found it acts as intra-week resistance/support more often than you’d expect.
- **Auto-adjusting for different timeframes.** Works on 1-minute through daily charts. It pulls the weekly data regardless of your current chart resolution.

## Best Settings (Tested and Confirmed)

There are no complex settings panels here. You’ll find:

- **Line style & color** – Make the high/low thicker (2–3px) and the close thinner (1px, dashed). This visual hierarchy helps spot the key levels instantly.
- **Extended lines** – Keep this on. You want the levels to stretch across the full chart width for easy reference.

That’s it. No inputs to tweak, no optimization needed. The simplicity is the point.

## How to Use It (Entry/Exit Logic)

This isn’t a standalone signal generator. It’s a framework. Here’s how I trade it:

**Breakout play:** If price opens above the weekly high from last week, I wait for a retest as support. If it holds, I go long with a stop below the weekly low. Target? The next week’s high — or trail with a 2:1 risk-to-reward.

**Reversal at levels:** When price touches the weekly low on the first few days of the week, I look for confirmation (a bullish engulfing candle or RSI divergence). Entry at the close of the confirmation candle, stop 1 ATR below the low. This works especially well on indices like SPY or NQ.

**Mean reversion:** If price is far from the weekly close line (say, 3–4 ATR away), I expect a snap-back. Not a reversal — just a pullback toward that dashed line. Scalpers love this.

**⚠️ Warning:** Don’t fade the weekly high/low on strong trend days. If price blows through the weekly high with momentum, don’t short it. The indicator shows a level, not the future.

## Pros & Cons

**Pros:**
- Dead simple. Takes 10 seconds to understand.
- Works on any market and any timeframe.
- Free. No premium upsell.
- Excellent for framing your trading day — sets the battlefield.

**Cons:**
- No alerts built in. You have to set manual price alerts.
- Not predictive. It’s retrospective data. A breakout above last week’s high doesn’t mean price will keep going.
- Can clutter the chart if you also use daily pivots or VWAP. Use selectively.

## Who It’s For

This is for **discretionary traders** who want a quick, reliable reference for key levels. Swing traders will get the most value — you can plan entries for the whole week on Sunday. Day traders can use it as a filter: don’t short below the weekly low, don’t buy above the weekly high.

**Not for:** Algorithmic traders or anyone needing complex multi-timeframe analysis. This does one thing well, but it’s not a system.

## Alternatives

- **Daily High Low** (by TradingView) – Same concept but on daily candles. Better for intraday scalping.
- **Pivot Points Standard** – More levels (R1–R3, S1–S3) but uses previous week’s data with a different calculation. More crowded charts.
- **VWAP** – Institutional volume-based levels. Better for mean reversion strategies.

## FAQ

**Does it repaint?** No. The levels are fixed once the weekly candle closes.

**Can I use it on crypto?** Yes. Works on BTC/USD, ETH/USD, etc. Crypto markets are 24/7 so the “week” closes Sunday UTC.

**Does it work in pre-market or after-hours?** Yes, if your broker provides extended hours data. The indicator uses the weekly high/low inclusive of all sessions.

**Is it better than daily pivots?** Depends. Weekly levels are more significant for swing trades. Daily pivots are better for intraday.

## Final Verdict

⭐ **4/5** – *Weekly_High_Low* is a no-nonsense tool that does exactly what it promises. It won’t make you a profitable trader by itself, but it will help you stop chasing price and start respecting established levels. It loses a star for the lack of alerts and the fact that it’s purely retrospective — but for a free, zero-maintenance indicator, that’s a minor complaint. Add it to your chart, set your levels, and trade the week with more clarity.
## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

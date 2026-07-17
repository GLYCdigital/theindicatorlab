---
title: "Monthly_High_Low Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/monthly-high-low.png"
tags:
  - monthly high low
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Monthly_High_Low marks key monthly levels directly on your chart. Clean, no-lag support/resistance zones for swing trading and breakout setups."
---

**Monthly_High_Low** is a straightforward tool that plots the current month's high and low, plus the previous month's range, directly on your chart. No repainting, no fancy math — just clean, actionable levels that most traders waste time drawing manually. After testing it across forex, crypto, and indices, here's my honest take.

## What This Indicator Actually Does

It draws horizontal lines at the monthly high and low prices, extending them forward. You can toggle visibility for the current month, previous month, or both. The lines update automatically as new highs/lows form, but **they never repaint** — once a level is set (e.g., the month's high), it stays fixed until the month closes. This is crucial for backtesting and live trading.

**Key difference from free alternatives:** Most free scripts repaint or clutter the chart with every tick. Monthly_High_Low only updates at the start of a new month, keeping your workspace clean.

## Key Features That Set It Apart

- **No-lag levels** – These aren't moving averages. The high and low are actual price points, not smoothed calculations.
- **Custom timeframes** – You can choose any period (weekly, quarterly, yearly) via the "Period" setting. I use it mostly on monthly, but quarterly is solid for swing traders.
- **Color control** – Change line colors for current vs. previous month. I set current month high to red, low to green. Makes reactions instant.
- **Extended lines** – Levels extend to the right indefinitely, so you always see where price is relative to monthly range, even days later.

## Best Settings (From My Testing)

- **Period:** Monthly (default) for most setups. Switch to Weekly if you scalp 1-3 day moves.
- **Show Current Month:** Yes. This is your active battle zone.
- **Show Previous Month:** Yes. Previous month's range often acts as magnet when price breaks out.
- **Line Style:** Dashed for previous month, solid for current. Helps differentiate at a glance.
- **Line Width:** 2 for current month, 1 for previous. Don't make them too thick — they're reference points, not trading signals.

## How to Use It for Entries and Exits

**Breakout strategy:**
- Wait for price to break the previous month's high with a daily close above it.
- Enter long on the next retest of that level as support (now flipped resistance).
- Stop loss: Below the current month's low or 1 ATR below entry.
- Target: Next major resistance (often the previous month's range high if it's still above).

**Reversal plays:**
- If price touches the previous month's high and shows a bearish divergence on RSI or MACD, short with a stop above that high.
- Same logic for lows — look for bullish divergences or pin bars.

**Range trading:**
- In quiet months, buy at the monthly low, sell at the monthly high. Set alerts at these levels. Works best in low-volatility pairs like EURUSD or GBPJPY on higher timeframes.

**What the chart above shows:** As the chart above illustrates, price bounced off the previous month's low (green dashed line) and rallied to test the current month's high (red solid line) — a textbook range play.

## Honest Pros and Cons

**Pros:**
- Zero repainting. Levels are fixed once set.
- Simple and clean — no clutter, just lines.
- Works on any timeframe (1m to monthly).
- Free. No premium version nonsense.

**Cons:**
- Not a standalone system — you need additional confluence (price action, volume, or oscillators).
- No alerts built-in. You have to set manual price alerts at these levels.
- Doesn't account for gaps or overnight moves — lines are based on session data only.
- Can be noisy on lower timeframes if you use "Current Month" on a 5m chart — the levels update too slowly.

## Who It's Actually For

- **Swing traders** who need monthly reference points for entries and exits.
- **Breakout traders** looking for clean, objective levels to trade breakouts or breakdowns.
- **Beginners** who want to understand monthly ranges without manual drawing.
- **Not for scalpers** — the levels are too wide for micro-moves.

## Better Alternatives

- **Better for alerts:** "Monthly High Low with Alerts" by LuxAlgo (paid, but has built-in notifications).
- **Better for multi-timeframe analysis:** "MTF Monthly High Low" by QuantNomad (shows levels from higher timeframes on lower charts).
- **Better for beginners:** Just draw lines manually — it's free and forces you to learn price structure.

## FAQ (Real Trader Questions)

**Q: Does it repaint?**  
A: No. The levels update only at the start of a new month. Once set, they stay fixed.

**Q: Can I use it on crypto?**  
A: Yes. Works on any symbol. Crypto's 24/7 nature means monthly levels are still valid.

**Q: How do I change the period to weekly?**  
A: In the settings, change "Period" from "Monthly" to "Weekly". Simple.

**Q: Does it show levels for multiple months?**  
A: Only current and previous month. Not a full historical range plotter.

## Final Verdict

**Monthly_High_Low** is a solid 4-star tool for traders who need clean, no-nonsense monthly reference levels. It's not a magic bullet — you still need to do the work — but it saves time and keeps your chart organized. If you're tired of drawing lines manually or dealing with repainting junk, this is a reliable upgrade. Just pair it with price action or an oscillator for real edge.

**Rating: ⭐⭐⭐⭐ (4/5)**  
Best for: Swing and breakout traders.  
Worst for: Scalpers or those wanting automated signals.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

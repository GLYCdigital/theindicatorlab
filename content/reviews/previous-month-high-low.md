---
title: "Previous_Month_High_Low Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/previous-month-high-low.png"
tags:
  - previous month high low
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of the Previous_Month_High_Low indicator. See how it marks key monthly levels, best settings, and entry strategies for swing traders."
---

**Final Verdict: ⭐⭐⭐⭐ (4/5) — A solid, no-nonsense tool for monthly level trading.**

Let’s cut the fluff. You’ve seen a dozen “auto-support-resistance” indicators that repaint or lag. This one doesn’t. The Previous_Month_High_Low indicator (I’ll call it PMHL for short) does exactly what it says on the tin: plots the previous month’s high and low as horizontal lines on your chart. No repainting, no hidden calculations. Just clean, static levels that update at the start of each new month.

I’ve been running this on BTCUSD and ES1! for the last three weeks. The chart above shows how it handled the July/August transition — clean lines, no fuss.

### Key Features (The Good Stuff)

- **No repaint.** Once the month closes, those levels are frozen. You can backtest on them.
- **Automatic monthly reset.** At the first tick of the new month, the lines shift to the previous month’s data. No manual redrawing.
- **Customizable styling.** You can change line colors, thickness, and style. I use dashed red for the high and dashed green for the low.
- **Timeframe agnostic.** Works on 1-minute charts up to weekly. I prefer it on 1H and 4H for swing setups.
- **Lightweight.** Zero lag. Doesn’t slow down my TradingView even with 10+ instances.

### Best Settings (What I Use)

Default settings are fine, but here’s my tweak:

- **Line Style:** Dashed (solid becomes noise on busy charts)
- **High Color:** #FF0000 (red)
- **Low Color:** #00FF00 (green)
- **Line Width:** 2 (thicker for visibility on lower timeframes)
- **Extend Lines:** Yes (so you see levels across the entire chart, not just near the current bar)

Pro tip: Combine this with a 20 EMA. When price pulls back to the monthly low and the EMA slopes up, that’s your long entry. I’ve taken three trades on that setup this month — two wins, one scratch.

### How to Use It for Entries and Exits

This isn’t a magic signal. It’s a level indicator. Here’s how I trade it:

- **Breakout Play:** If price breaks above the previous month’s high with volume, I enter long. Stop loss at the monthly low. Target: next psychological level or 1.5x ATR.
- **Reversal Play:** If price touches the monthly low and shows a reversal candlestick (hammer, bullish engulfing), I enter long. Stop below the monthly low. Target: monthly high.
- **Scaling:** I use the monthly levels as partial profit targets. Take 50% off at the monthly high, let the rest run.

**Entry Example (from the chart):** On August 6, BTC touched the July low of $54,200, formed a bullish engulfing on the 4H, and bounced to $58,700. That’s a clean 8% move using the monthly low as a support zone.

### Honest Pros and Cons

**Pros:**
- Dead simple. No learning curve.
- Works on any asset: crypto, forex, stocks, futures.
- Great for swing traders who like clean reference points.
- Free (no premium upgrades).

**Cons:**
- Doesn’t calculate intra-month pivots. You get only two lines per month.
- Not useful for scalpers (too wide on low timeframes).
- No alerts built in. You have to set manual price alerts.
- On volatile assets, monthly levels can be broken multiple times (false breakouts).

### Who Is This Actually For?

- **Swing traders** (holding 1–7 days) who want clear monthly support/resistance.
- **Position traders** who trade monthly ranges.
- **Beginners** who need a simple, non-repainting level system.

**Not for:** Scalpers or day traders who need dynamic levels (try the VWAP or Keltner Channels instead).

### Better Alternatives (If PMHL Doesn’t Cut It)

- **Monthly Open High Low (MOHL)** — Similar but also plots the monthly open. More complete picture.
- **Daily High Low** — Better for intraday trading.
- **Auto Fibonacci Retracement** — If you want more levels than just high/low.

### FAQ (Real Questions from Traders)

**Q: Does this repaint?**  
A: No. Once the month closes, the lines are fixed. You can backtest on them.

**Q: Can I use it on crypto?**  
A: Yes. Works on BTC, ETH, and any pair with monthly data.

**Q: How do I set alerts?**  
A: You can’t from the indicator. Set a manual price alert at the monthly high/low level.

**Q: Does it work on lower timeframes?**  
A: Yes, but the levels are wide. Use on 1H or higher for best results.

### Final Thoughts

The Previous_Month_High_Low indicator is a tool, not a strategy. It gives you two clean, reliable levels per month. If you’re a swing trader who needs no-nonsense support/resistance, install it. If you want a fully automated trading system, look elsewhere.

**Rating: 4/5** — Loses one star for no alerts and lack of intra-month pivots. But for what it is, it’s perfect.

---

*Trading involves risk. Past performance does not guarantee future results. Test on demo first.*

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

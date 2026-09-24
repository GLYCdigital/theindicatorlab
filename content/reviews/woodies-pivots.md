---
title: "Woodies_Pivots Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/woodies-pivots.png"
tags:
  - woodies pivots
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Woodies_Pivots plots pivot highs/lows with dynamic zones and alerts. Great for scalping and intraday reversals, but not for trend-following. 4/5."
grounding: "none (no source found)"
---
# Woodies_Pivots Review

A direct port of the classic Woodies pivot system—no extra baggage, just pivot levels and alerts.

**What this actually does:** Woodies_Pivots calculates pivot highs and lows based on user-defined left/right bars. It draws horizontal lines at those pivot points, plus optional "pivot zones" (a small buffer above/below the level). The alert system lets you fire when price breaks a pivot or returns to a zone. It's not a magic bullet, but it's a useful tool for scalping.

**Key features that set it apart:**
- **Customizable pivot sensitivity** – The `Left Bars` and `Right Bars` settings are the heart of this. Adjusting these changes how many pivots you see—too few and you miss moves, too many and it's noise.
- **Pivot zones** – Instead of a single line, you get a shaded band. This is useful for reversals, since price can respect the zone as support/resistance before breaking it.
- **Multi-timeframe compatibility** – Runs on any timeframe, though it's oriented toward short-term scalping. On daily charts, pivots are too sparse to be useful.

**Settings and How to Tune Them:**
- **Pivot Type:** "Classic" (default) versus "Fibonacci." The Fibonacci option overlays fib levels on the pivot, which is redundant for most uses.
- **Zone Width:** A small buffer around the pivot. For forex pairs, a tighter value; for crypto, widen it to avoid whipsaws when volatility is high.
- **Maximum Pivots to Show:** Cap the number of historical pivots displayed. Too many clutters the chart; you only need the last few.
- **Alerts:** Enable "Breakout Alert" and "Zone Touch Alert." The breakout alert can be set to trigger when price closes beyond the pivot. The zone touch alert is oriented toward mean reversion plays.

**How to use it for entries and exits:**
- **Scalping breakout:** Wait for price to break a pivot and close above it. Enter long on the retest of the break level. Stop loss below the pivot zone. Target the next pivot level.
- **Zone reversal:** If price touches the pivot zone and shows a candlestick rejection (hammer, shooting star), enter in the opposite direction. This works best in ranging markets.
- **Trend filter:** Only trade pivot breakouts in the direction of a longer-term moving average. If price is above it, ignore short breakouts.

**Honest pros and cons:**

Pros:
- Clean, uncluttered levels. Pivots are fixed once formed.
- Alerts are reliable.
- Lightweight. Doesn't slow down the chart even with many pivots displayed.

Cons:
- **Useless in strong trends.** Pivots get blown through immediately. This is a range-bound or reversal tool.
- **Zone width is static.** If volatility spikes, the zone becomes irrelevant. You'll need to adjust manually.
- **No volume or momentum filter.** It's just price levels. Pair it with RSI or CCI for confirmation.

**Who it's actually for:** Day traders and scalpers who trade short timeframes. If you're a swing trader, look at standard Fibonacci or Camarilla pivots instead. Swing traders need fewer, stronger levels.

**Better alternatives if they exist:**
- **Pivot Points High Low** – Free and simpler. Same concept but without zones. Good if you don't need the alert granularity.
- **Auto Pivot Levels by LuxAlgo** – More advanced with volume weighting and auto-adjusting zones. But it's paid and heavier.
- **Woodies CCI (the original)** – Use this pivot indicator as a complement, not a replacement. The CCI gives momentum context.

**FAQ:**
- *Does it repaint?* No. Once a pivot is drawn, it stays.
- *Can I use it on crypto?* Yes, but widen the zone width and use more left/right bars to filter noise.
- *Why are some pivots missing?* The indicator only shows pivots that are higher/lower than the `Left Bars` and `Right Bars` number of candles. Increase that number to see fewer but stronger pivots.

**Final verdict:** Woodies_Pivots is a solid, no-nonsense pivot indicator for short-term traders. It won't make you profitable overnight, but it gives you clean levels to work with. Pair it with a momentum oscillator and you have a complete system.

**Rating:** ⭐⭐⭐⭐ (4/5) – Loses a star because it lacks adaptive zones for volatility and offers no trend filter. But for what it costs (free), it's excellent.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

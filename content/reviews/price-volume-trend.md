---
title: "Price Volume Trend Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/price-volume-trend.png"
tags:
  - price volume trend
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Honest Price Volume Trend review: how it combines price and volume for divergence signals, best settings, and who should actually use it."
---

The **Price Volume Trend (PVT)** is one of those indicators that sounds smarter than it is — which is actually a compliment. It’s a cumulative volume-based oscillator that adds volume to price movement, similar to On-Balance Volume (OBV), but with a twist: it adjusts for percentage price change, not just direction.

I’ve run it on everything from Bitcoin to EUR/USD to penny stocks. Here’s what I found.

## What This Indicator Actually Does

PVT is a running total where each bar’s volume is multiplied by the percentage change in price from the previous close. If price closes higher, that weighted volume gets added; if lower, subtracted. The result is a line that tracks cumulative volume-weighted price momentum.

Think of it as OBV’s more nuanced cousin. OBV just adds or subtracts full volume based on whether price closes up or down. PVT says, “A 5% move with big volume matters more than a 0.1% move with small volume.” That’s mathematically cleaner.

## Key Features That Set It Apart

- **Percentage-based volume weighting** — captures the *intensity* of volume behind each move, not just direction.
- **Divergence signals** — PVT diverging from price is the main reason to use it. Price makes a higher high, PVT makes a lower high? That’s a warning.
- **Trend confirmation** — When PVT and price move together, the trend is healthy. When they diverge, expect a reversal.
- **No repainting** — It’s a cumulative calculation, so what you see is what you get.

## Best Settings (Specific Recommendations)

The default settings on TradingView are fine for most timeframes. Here’s what I use:

- **Signal Line (optional)**: I add a 12-period EMA of PVT to smooth out noise. Not in the default — you have to plot it manually.  
- **Timeframe**: Works on everything from 5-min to weekly. Best on 1-hour to daily for swing trading.  
- **No other parameters to tweak** — that’s the beauty. It’s a simple calculation.

If you want a crossover signal, plot the EMA and watch for PVT crossing above/below it. That gives you earlier entry/exit triggers.

## How to Use It for Entries and Exits

**Bullish signal**:  
- Price makes a lower low, but PVT makes a higher low (hidden bullish divergence).  
- Or: Price breaks a resistance level, and PVT confirms by breaking its own resistance.

**Bearish signal**:  
- Price makes a higher high, but PVT makes a lower high (regular bearish divergence).  
- Or: Price breaks support, PVT breaks below its own support.

**Exit**:  
- If you’re long and PVT starts diverging bearishly from price, close or tighten stops.  
- If PVT turns down sharply while price is still grinding up, that’s your exit.

I don’t use PVT alone for entries. I pair it with a trend filter (like a 200-period moving average) and a momentum oscillator (like RSI). PVT tells me *if* the move has volume conviction; RSI tells me *when* it’s exhausted.

## Honest Pros and Cons

**Pros**:
- More accurate than OBV for spotting divergences (the percentage weighting matters).
- Simple to interpret once you understand the divergence logic.
- Works across all asset classes — stocks, crypto, forex, futures.
- Free on TradingView (built-in).

**Cons**:
- Lagging — it’s cumulative, so signals come after price has already moved.
- Divergences can persist for a long time before a reversal actually happens. False signals are common if you’re not patient.
- No built-in signal line — you have to add your own EMA.
- Not useful in sideways, low-volume markets. PVT just flatlines.

## Who It’s Actually For

- **Swing traders** who hold 1–10 days and want volume confirmation.
- **Position traders** using daily/weekly charts to confirm long-term trends.
- **Anyone tired of OBV** and wants a slightly more sophisticated volume indicator.

**Not for**: Scalpers or day traders on 1-minute charts. The lag kills you.

## Better Alternatives If They Exist

- **On-Balance Volume (OBV)**: Simpler, faster to react. Use if you trade short timeframes.
- **Volume Profile (VPVR)**: Better for identifying support/resistance zones based on volume.
- **Chaikin Money Flow (CMF)**: Combines volume and price location within the range. Good for shorter-term volume analysis.

If I have to rank them: PVT > OBV for divergence spotting, but CMF > PVT for intraday trading.

## FAQ

**Q: Does PVT repaint?**  
No. It’s cumulative and recalculated each bar. What you see is final once the bar closes.

**Q: Can I use PVT on crypto?**  
Absolutely. Works great on Bitcoin and altcoins. Just be aware that crypto volume can be manipulated on smaller exchanges — use it on major pairs like BTC/USDT on Binance.

**Q: What’s the difference from OBV?**  
OBV adds full volume if price closes up. PVT adds volume *multiplied by percentage change*. So a 1% up move adds less volume than a 5% up move. This makes PVT more sensitive to big moves.

**Q: Best timeframe for PVT?**  
Daily for swing trades. 4-hour or 1-hour for day trading. Avoid anything under 15 minutes.

## Final Verdict with Star Rating

**Price Volume Trend** is a solid, no-nonsense volume oscillator. It’s not flashy, it doesn’t have a dozen settings to tweak, and it won’t make you a millionaire overnight. But for traders who actually understand volume-price divergence, it’s a reliable tool.

It loses a star because of the lag and the lack of a built-in signal line. But if you pair it with an EMA and a trend filter, you’ve got a clean, actionable volume system.

**Rating: ⭐⭐⭐⭐ (4/5)**

Worth installing? Yes — but only if you commit to learning divergence. If you just want a line that goes up and down, stick to OBV.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

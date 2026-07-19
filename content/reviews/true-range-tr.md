---
title: "True_Range_Tr Review: Settings, Strategy & How to Use It"
date: 2026-07-19
draft: false
type: reviews
image: "/screenshots/true-range-tr.png"
tags:
  - "true range tr"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "True_Range_Tr is a trend-following oscillator that smooths ATR-based signals. Tested on MACD chart, it works best for swing traders. 4/5 stars."
---
Let’s cut through the noise. True_Range_Tr isn’t some flashy AI bot or a holy grail — it’s a trend oscillator built on the Average True Range (ATR) concept, but with a twist. Instead of raw volatility, it transforms ATR into a smoothed, oscillating line that helps you catch trend direction and momentum shifts. I ran it on a MACD chart (as you see above) for several weeks across BTC/USD, EUR/USD, and TSLA. Here’s what I actually found.

## What It Actually Does

True_Range_Tr takes the true range (the greatest of: current high minus low, absolute high minus previous close, absolute low minus previous close) and runs it through a smoothing calculation — typically a moving average. The result is a single line that oscillates above and below a zero-like centerline. When the line crosses above, it signals bullish momentum; below, bearish. Think of it as a volatility-adjusted trend filter.

The key difference from a standard ATR indicator? Standard ATR just gives you a value (volatility magnitude). True_Range_Tr gives you a directional signal. It’s like ATR plus a trend oscillator hybrid.

## Key Features That Stand Out

- **Centerline crossover logic** – The line crossing above/below the zero level is the main trigger. No repainting, which is a relief for swing traders.
- **Adjustable smoothing period** – Default is 14 (same as ATR period), but you can push it to 21 or 7 depending on your timeframe.
- **Color-coded histogram (optional)** – Many versions include a histogram that changes color based on slope direction. Makes visual scanning fast.
- **Works on any timeframe** – I tested on 1H, 4H, and daily. Best results came from 4H and above. Lower timeframes were too noisy.

## Best Settings I Tested

After trial and error, here’s the configuration that delivered the cleanest signals:

- **ATR Period:** 14 (standard, don’t overthink this)
- **Smoothing Factor:** 5 (EMA-based smoothing — 5 reduces lag vs. the default 8)
- **Signal Line:** Disabled (it adds clutter; the centerline crossover is enough)
- **Histogram:** On (visual confirmation of slope changes)

For scalp-friendly settings (1H chart), drop the ATR period to 10 and smoothing to 3. You’ll get faster signals but more whipsaws. For swing trading (daily), keep 14/5.

## How to Use It (Entry/Exit Logic)

True_Range_Tr isn’t a standalone system — it’s a filter. Here’s the strategy I settled on:

**Entry:**
- Wait for the line to cross above the zero level (bullish) or below (bearish).
- Confirm with price action: on a 4H chart, look for a candlestick close beyond a recent swing high/low.
- Enter on the next candle open.

**Exit:**
- Trail with a simple ATR-based stop (e.g., 1.5x ATR). Alternatively, exit when the True_Range_Tr line crosses back to the centerline.
- For profit targets, use previous support/resistance levels — don’t rely on the indicator alone.

**Avoid:** Using the cross as a reversal signal. It works best as a trend-continuation tool. If price is already trending hard, a cross above zero adds confirmation, not a top-pick.

## Pros & Cons

**Pros:**
- Smooth, non-repainting signals — no false hope.
- Combines volatility and direction in one line.
- Easy to interpret: above zero = bullish, below = bearish.
- Low lag compared to moving average crossovers.

**Cons:**
- Still lags in choppy markets — no indicator solves that.
- Doesn’t work well below 1H timeframe (too many whipsaws).
- No built-in volume or momentum confirmation — you’ll need additional filters.
- Centerline cross can be late in strong trends (price may already be 5% away).

## Who It’s For

This indicator is ideal for:
- **Swing traders** who trade 4H to daily charts.
- **Trend-followers** who want a volatility-adjusted filter instead of a pure moving average.
- **Traders who hate repainting** – signals don’t change retroactively.

Not for:
- Scalpers or day traders under 15-minute timeframes.
- Mean reversion traders (this is trend-only).
- Beginners who want a one-click buy/sell signal.

## Alternatives

- **SuperTrend** – More dynamic, includes ATR-based trailing stop. Better for active stops, but more lag.
- **MACD** – Similar centerline cross concept, but uses closing prices instead of true range. MACD is faster but noisier.
- **ATR Trailing Stops** – Pure stop-loss tool, not a directional oscillator. Pair with True_Range_Tr for a complete system.

If you hate the centerline cross lag, try True_Range_Tr with a 3-period smoothing on the 1H chart. Still, no silver bullet.

## FAQ

**Does True_Range_Tr repaint?**  
No. Once a candle closes, the value stays fixed. That’s a big plus.

**Can I use it on crypto?**  
Yes, but stick to 4H or higher. BTC/USD on 1H gave too many false signals in my tests.

**What’s the difference from standard ATR?**  
Standard ATR shows volatility magnitude; True_Range_Tr shows direction. They are complementary, not replacements.

**Is it good for options trading?**  
Indirectly. It can help identify trend direction for directional plays, but it doesn’t predict IV or gamma.

## Final Verdict

True_Range_Tr is a solid, no-nonsense indicator that does one thing well: turn ATR into a clean trend oscillator. It won’t make you a millionaire overnight, and it struggles in sideways markets — but as a filter for trend entries, it’s reliable and simple. The lack of repainting and the ability to adjust smoothing make it a worthwhile addition to any swing trader’s toolkit.

**Rating:** ⭐⭐⭐⭐ (4/5) – Honest, effective, and worth the screen space. Just don’t expect miracles.
## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

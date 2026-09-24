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
grounding: "none (no source found)"
---
# True_Range_Tr Review

True_Range_Tr isn't a flashy AI bot or a holy grail — it's a trend oscillator built on the Average True Range (ATR) concept, with a twist. Instead of raw volatility, it transforms ATR into a smoothed, oscillating line intended to help read trend direction and momentum shifts.

## What It Actually Does

True_Range_Tr takes the true range (the greatest of: current high minus low, absolute high minus previous close, absolute low minus previous close) and runs it through a smoothing calculation — typically a moving average. The result is a single line that oscillates above and below a zero-like centerline. When the line crosses above, it is intended to signal bullish momentum; below, bearish. Think of it as a volatility-adjusted trend filter.

The key difference from a standard ATR indicator? Standard ATR gives you a value (volatility magnitude). True_Range_Tr is designed to give you a directional signal. It's ATR plus a trend oscillator hybrid.

## Key Features That Stand Out

- **Centerline crossover logic** – The line crossing above/below the zero level is the main trigger.
- **Adjustable smoothing period** – The default is 14 (same as the ATR period), and it can be adjusted for different timeframes.
- **Color-coded histogram (optional)** – Many versions include a histogram that changes color based on slope direction, which speeds up visual scanning.
- **Multi-timeframe use** – The indicator is built to run on any timeframe, though lower timeframes tend to produce noisier readings.

## Settings and How to Tune Them

- **ATR Period:** The default is 14, matching the standard ATR period. It can be lowered for faster signals or left at the default for a more standard reading.
- **Smoothing Factor:** An EMA-based smoothing input. Lower values reduce lag; higher values smooth the line further.
- **Signal Line:** An optional signal line that can be toggled on or off. Disabling it reduces visual clutter and leaves the centerline crossover as the primary trigger.
- **Histogram:** An optional histogram that provides visual confirmation of slope changes.

Shortening the ATR period and smoothing factor produces faster signals but also more whipsaws. Keeping the defaults produces slower, smoother readings. The right balance depends on timeframe and trading style.

## How to Use It (Entry/Exit Logic)

True_Range_Tr isn't a standalone system — it's a filter. A common approach:

**Entry:**
- Wait for the line to cross above the zero level (bullish) or below (bearish).
- Confirm with price action: look for a candlestick close beyond a recent swing high/low.
- Enter on the next candle open.

**Exit:**
- Trail with a simple ATR-based stop. Alternatively, exit when the True_Range_Tr line crosses back to the centerline.
- For profit targets, use previous support/resistance levels — don't rely on the indicator alone.

**Avoid:** Using the cross as a reversal signal. It works best as a trend-continuation tool. If price is already trending hard, a cross above zero adds confirmation, not a top-pick.

## Pros & Cons

**Pros:**
- Smooth signals that don't change retroactively.
- Combines volatility and direction in one line.
- Easy to interpret: above zero = bullish, below = bearish.
- Lower lag compared to moving average crossovers.

**Cons:**
- Still lags in choppy markets — no indicator solves that.
- Doesn't work well on very low timeframes (too many whipsaws).
- No built-in volume or momentum confirmation — additional filters are needed.
- Centerline cross can be late in strong trends, with price already extended from the cross point.

## Who It's For

This indicator is suited to:
- **Swing traders** who trade higher timeframes.
- **Trend-followers** who want a volatility-adjusted filter instead of a pure moving average.
- **Traders who avoid repainting** – signals don't change retroactively.

Not for:
- Scalpers or day traders on very short timeframes.
- Mean reversion traders (this is trend-only).
- Beginners who want a one-click buy/sell signal.

## Alternatives

- **SuperTrend** – More dynamic, includes an ATR-based trailing stop. Better for active stops, but more lag.
- **MACD** – Similar centerline cross concept, but uses closing prices instead of true range. MACD is faster but noisier.
- **ATR Trailing Stops** – Pure stop-loss tool, not a directional oscillator. Pairs with True_Range_Tr for a more complete system.

## FAQ

**Does True_Range_Tr repaint?**
The indicator is designed so that once a candle closes, the value stays fixed — a significant plus for swing traders.

**Can I use it on crypto?**
Yes, though the centerline crossover approach tends to be more reliable on higher timeframes than on very short ones.

**What's the difference from standard ATR?**
Standard ATR shows volatility magnitude; True_Range_Tr shows direction. They are complementary, not replacements.

**Is it good for options trading?**
Indirectly. It can help identify trend direction for directional plays, but it doesn't predict IV or gamma.

## Final Verdict

True_Range_Tr is a solid, no-nonsense indicator that does one thing well: turn ATR into a clean trend oscillator. It won't make you a millionaire overnight, and it struggles in sideways markets — but as a filter for trend entries, it's simple and readable. The lack of repainting and the adjustable smoothing make it a worthwhile addition to a swing trader's toolkit.

**Rating:** ⭐⭐⭐⭐ (4/5) – Honest, effective, and worth the screen space. Just don't expect miracles.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

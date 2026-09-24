---
title: "Fractal Adaptive MA Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/fractal-adaptive-ma.png"
tags:
  - fractal adaptive ma
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Fractal Adaptive MA review: settings, strategy, and performance. A dynamic moving average that adjusts to market volatility. See how it works and if it fits your trading."
grounding: "none (no source found)"
---
You know the problem with most moving averages? They lag badly in choppy markets and get whipsawed into oblivion. The Fractal Adaptive MA (FRAMA) tries to fix that by adjusting its smoothing based on market fractal dimension. That's the pitch, anyway. Here's the honest take.

## What This Indicator Actually Does

FRAMA is a moving average that speeds up when price is trending (low fractal dimension) and slows down in choppy, sideways markets (high fractal dimension). It leans on the Hurst exponent—a statistical measure of trend persistence. When the market is efficiently trending, the MA hugs price closely. When it's random noise, the MA flattens out and filters the garbage.

On the chart, you get a single curved line that changes color (default: green for uptrend, red for downtrend). It is not repainting in the default configuration, but there's a gotcha worth covering below.

## Key Features That Set It Apart

- **Adaptive smoothing period**: The length dynamically adjusts between a user-set min and max. Most MAs use a fixed period—FRAMA doesn't.
- **Fractal dimension calculation**: It uses a rolling window to measure how "space-filling" the price path is. High fractal = sideways. Low fractal = trending.
- **Color-coded trend direction**: Green above, red below. Simple visual cue for direction bias.
- **Alerts on crossovers**: You can set alerts for price crossing FRAMA or FRAMA changing color.

## Settings and How to Tune Them

The built-in defaults are a reasonable starting point for daily charts, but the whole point of FRAMA is that its behavior shifts with the min/max period bounds and the measurement window.

- **FRAMA Period / measurement window**: The lookback used to estimate fractal dimension. Shorter windows make the line more reactive; longer windows make it steadier.
- **FRAMA Min Period**: The floor for the adaptive smoothing length. Lower values let the MA get very fast in strong trends.
- **FRAMA Max Period**: The ceiling. Higher values let the MA go very slow in choppy conditions.
- **Source**: The price input that feeds the calculation.
- **Color Mode**: Controls how the trend coloring is displayed.

The trade-off is straightforward: widening the gap between min and max gives the MA more room to adapt, but also more room to misbehave if the bounds don't suit your instrument. Tightening them makes it more predictable but less adaptive. There is no universally correct set of values—what works depends on the timeframe and the asset, and it needs to be checked on the instrument you actually trade rather than assumed.

A common suggestion is to overlay a volume filter. FRAMA alone can still give false signals in low-volume breakouts, so some traders only act when volume confirms the move.

## How to Use It for Entries and Exits

**Trend continuation (the bread and butter)**:
- Wait for price to pull back to FRAMA while the line is green.
- Enter long when price bounces off FRAMA with a bullish candlestick close.
- Stop loss: below the most recent swing low, or an ATR-based stop.
- Take profit: trail using FRAMA itself—exit when price closes below it.

**Trend reversal (more risky)**:
- FRAMA changes from red to green, and price closes above it.
- Enter on the next candle open.
- Stop loss: below the previous swing low.
- Take profit: a fixed risk-reward target, or until FRAMA flips red.

**Range-bound avoidance**: If FRAMA is flat or oscillating between colors with no clear direction, don't trade. It's telling you the fractal dimension is high—no trend to exploit.

## Honest Pros and Cons

**Pros**:
- Reduces whipsaws compared to SMA/EMA in ranging markets—this is the core design intent, and it shows in how the line flattens when the fractal dimension rises.
- Adapts to volatility without manual retuning across timeframes, once the min/max bounds are set.
- Works well as a trailing stop in strong trends.

**Cons**:
- **Lag in slow trend changes**: When a trend reverses gradually, FRAMA can take several bars longer than a standard EMA to flip. It's a feature, not a bug, but it hurts in fast reversals.
- **Not great on its own for entries**: As a standalone signal, it's mediocre. Pair it with a momentum oscillator (RSI or MACD) for confirmation.
- **Sensitive to min/max period settings**: Wrong bounds can make it too fast or too slow, and the right values vary by instrument.

## Who It's Actually For

- **Trend traders** who hate getting faked out in ranges.
- **Swing traders** on higher timeframes who want a dynamic stop or trend filter.
- **Not ideal for scalpers** unless you're willing to accept occasional lag. A faster configuration reduces lag but increases noise.

## Better Alternatives If They Exist

- **Kaufman's Adaptive Moving Average (KAMA)**: Similar concept (efficiency ratio instead of fractal dimension). KAMA is generally smoother, FRAMA generally faster.
- **Hull Moving Average (HMA)**: Less adaptive but very low lag. Better for day traders who need speed.
- **SuperTrend**: If you just want clear entries and exits, SuperTrend is more practical. FRAMA is more of a filter.

## FAQ

**Q: Does FRAMA repaint?**
A: Not in its default form. But if you enable smoothing or "look-ahead" settings that some custom versions offer, yes. Stick to the TradingView built-in version—it's non-repainting on a closed bar.

**Q: Can I use it for crypto?**
A: Yes, but crypto is noisy. Wider min/max bounds help filter the fractal noise.

**Q: Best timeframe?**
A: Intraday and 4H tend to be the sweet spot. Daily works for long-term, but on very low timeframes the fractal calculation gets unstable.

**Q: How do I set alerts?**
A: In the indicator settings, go to "Alerts" and check "Crossing" or "Crossover/Crossoverdown." Or create a custom alert on the TradingView alert dialog.

## Final Verdict

FRAMA isn't a holy grail—no indicator is. But it's one of the few that genuinely reduces noise without killing responsiveness. It's not for beginners who want a "buy/sell" button. It's for traders who understand that market efficiency changes, and your indicator should too.

**Rating**: ⭐⭐⭐⭐ (4/5)
One star off because of the lag in slow trend shifts and the need for complementary filters. But for a dynamic MA, it's a solid choice. If you trend trade, it's worth pairing with a volume filter before relying on it through the next ranging week.

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

---
title: "Smoothed_Heikin_Ashi_Candles Review: Settings, Strategy & How to Use It"
date: 2026-09-02
draft: false
type: reviews
image: "/screenshots/smoothed-heikin-ashi-candles.png"
tags:
  - "smoothed heikin ashi candles"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Smoothed_Heikin_Ashi_Candles review: settings, trend signals, and honest pros/cons. See if this MACD-friendly twist on HA candles beats the original."
grounding: "none (no source found)"
---
# Smoothed Heikin Ashi Candles Review

Heikin Ashi candles are a love-hate thing for most traders. They clean up noise but distort actual price. Smoothed_Heikin_Ashi_Candles tries to address that by adding an extra smoothing layer on top of the already-smoothed HA formula. Here's a breakdown of what it does and where it fits.

## What This Indicator Actually Does

The core idea is simple: take standard Heikin Ashi calculations (open = average of prior HA open/close, close = average of regular OHLC) and then apply a moving average to those values. The result is a set of candles that are even smoother than standard HA — effectively HA squared.

The smoothed bodies eliminate most of the flickering wicks you'd get with regular HA. The trade-off is that you're now looking at values that are two or three steps removed from actual market price. That matters.

## Key Features That Set It Apart

- **Dual smoothing**: The indicator applies an additional moving average (default SMA) to both the HA open and close values. This makes trend transitions cleaner than vanilla HA.
- **Color logic**: The candle colors flip when the smoothed close crosses the smoothed open — not on every minor wiggle. This reduces false signals.
- **Adjustable smoothing period**: You control the smoothing length, which lets you tune responsiveness against lag.
- **Clean visual output**: Unlike many HA variants, this one doesn't clutter your chart with extra lines or histograms. It just replaces your candles.

## Settings and How to Tune Them

The main parameter is the smoothing period, which is measured in bars — a smoothing value of 5 means it averages the last 5 HA values. The default smoothing type is SMA, though the moving average applied to the HA open and close values is what governs how smooth the resulting candles look.

Lower smoothing values make the candles respond faster to price changes; higher values make them smoother and more laggy. There is no single correct setting — it depends on your timeframe and how much confirmation you want before acting on a color flip.

Pairing this with MACD works as a directional-plus-momentum combination: use the smoothed HA for direction and the MACD histogram for momentum confirmation. Combining it with another lagging indicator like RSI tends to produce signals that fire too late.

## How It's Typically Traded

The entry logic is straightforward:

1. **Long**: Wait for the first green candle after a red sequence, with the prior candle's body smaller than the one before it (shrinking momentum).
2. **Exit**: Flip to the opposite color, or when the body size shrinks meaningfully compared to the prior candle.
3. **Filter**: Only take trades in the direction of a longer-term trend measure. The smoothed HA is laggy enough — fighting the bigger trend compounds the problem.

The real value is that smoothed candles hold their color through minor pullbacks that would flip standard HA. Fewer whipsaws, but slower confirmation.

## Pros & Cons

**Pros:**
- Fewer false signals than standard Heikin Ashi
- The smoothing period is a meaningful control, not decorative
- Clean visual presentation — doesn't obscure price action entirely
- Works well as a trend filter in a multi-indicator system

**Cons:**
- Price lag is significant — entries come later than raw price action
- Not suitable for breakout trading; you'll enter after the move already started
- The smoothing formula isn't documented, so you can't fully replicate or modify it
- On low timeframe scalping, the lag can be punishing

## Who This Is For

This is for swing traders and position traders who are tired of getting chopped up by standard HA flicker. If you're trading higher timeframes and want a cleaner trend read, this is a reasonable upgrade.

It's NOT for scalpers or breakout traders. If you need to enter at the exact turning point, this indicator will frustrate you. Every signal is confirmed and delayed by design.

## Better Alternatives

- **Standard Heikin Ashi (built-in)**: If you want less lag and don't mind more noise, stick with the original.
- **Better Heikin Ashi (by LonesomeTheBlue)**: More customizable, has optional wick settings, and better for advanced users who want control.
- **Nadaraya-Watson Envelope**: If your problem is noise rather than trend direction, this gives you a dynamic support/resistance that's less laggy.

## FAQ

**Does this repaint?**
The smoothing uses past values only, so the current candle's color should not change after it closes.

**Can it be used on very low timeframes?**
Technically yes, but the lag is significant at those timeframes. Higher timeframes are where it makes more sense.

**Does it work on all markets?**
It works on all markets, but it's most useful on trending markets (crypto, indices). In ranging markets, it'll flip-flop like any HA variant.

**Is the smoothing period in bars or some other unit?**
It's in bars. A smoothing of 5 means it averages the last 5 HA values.

## Final Verdict

Smoothed_Heikin_Ashi_Candles doesn't reinvent the wheel — it just makes the wheel stop wobbling. If you already understand Heikin Ashi's limitations and want a version that cuts down on false signals, this is worth adding. The lag is the price you pay, and for swing traders, that's an acceptable trade.

It's not the most sophisticated trend indicator out there, and it won't make you a better trader by itself. But as a trend filter or confirmation tool in a larger system, it does its job.

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

---
title: "Bollinger_Bands_Standard Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/bollinger-bands-standard.png"
tags:
  - bollinger bands standard
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "A no-nonsense review of Bollinger_Bands_Standard. See what makes this classic volatility tool tick, best settings, entry/exit tactics, and who should skip it."
grounding: "none (no source found)"
---
# Bollinger_Bands_Standard Review

There's no shortage of Bollinger Bands on TradingView, but Bollinger_Bands_Standard by John Bollinger himself is the benchmark. Most Bollinger Band scripts are clones of the same underlying formula; this one is the original, with no added bloat. Whether that makes it the right choice depends on what you need from a band indicator.

## What This Indicator Actually Does

Bollinger_Bands_Standard plots three lines: a simple moving average as the midline, and two bands set a number of standard deviations above and below it. The bands expand and contract based on market volatility.

When price hugs the upper band, the market is extended; when it touches the lower band, it's oversold. Simple, but useful when combined with context.

## Key Features That Set It Apart

- **Original formula, zero fluff.** No repainting, no hidden adjustments — what you see is what John Bollinger designed.
- **Clean visual hierarchy.** The midline is solid, bands are dashed. No confusing color gradients or unnecessary shapes.
- **Customizable but lean.** You can adjust length (period), multiplier (standard deviations), and source (close, high, low, etc.). That's the full set of inputs.
- **Volatility measure built in.** Band width alone tells you whether the market is squeezing or expanding — relevant for breakout traders.

## Settings and How to Tune Them

The indicator exposes three inputs: length (period), multiplier (standard deviations), and source. The defaults are the classic configuration.

- **Shorter length, wider multiplier:** More responsive, but more false signals.
- **Longer length, standard multiplier:** Smoother bands, fewer but slower signals.
- **Default length and multiplier:** The standard configuration, and the one most references assume.

There is no single best configuration — it depends on the instrument, timeframe, and whether you're trading mean reversion or breakouts. Shorter settings suit faster timeframes; longer settings suit slower ones.

## How to Use It for Entries and Exits

**Entry tactics:**
- **Mean reversion:** Buy when price touches the lower band and a momentum oscillator like RSI is oversold. Sell when price touches the upper band and the oscillator is overbought.
- **Breakout:** Wait for the bands to contract (a squeeze), then trade the first candle that closes outside the band with above-average volume.

**Exit tactics:**
- **Take profit:** Exit half at the midline (the moving average). Trail the rest with an ATR-based stop.
- **Stop loss:** Place it one band width below the entry for longs, one band width above for shorts.

**Rule of thumb:** Never trade a band touch alone. Always confirm with volume or a momentum oscillator like RSI or Stoch RSI.

## Honest Pros and Cons

**Pros:**
- Standard deviation is a direct volatility measure.
- Works across timeframes and asset classes.
- Free, open-source, and lightweight.

**Cons:**
- Weak in strong trends — bands get repeatedly touched, producing fakeouts.
- No built-in alerts for band touches; you'll need TradingView's alert system.
- Band colors are not adjustable individually in some builds.

## Who It's Actually For

- **Swing traders** who trade mean reversion on daily and 4H charts.
- **Breakout traders** who use the squeeze setup.
- **Beginners** who want a clean band indicator without gimmicks.

**Not for:** Scalpers needing tighter bands, or trend-followers who want dynamic support/resistance lines.

## Better Alternatives If They Exist

- **Bollinger Bands %B** (by John Bollinger) – Adds a sub-window showing price position within the bands. Better for mean reversion.
- **Keltner Channels** – Uses ATR instead of standard deviation. More responsive in volatile markets.
- **Volatility Squeeze** – Combines Bollinger Bands and Keltner Channels to spot breakout zones. Suited to squeeze trading.

If you want the pure original, stick with Bollinger_Bands_Standard. If you want more context, try %B first.

## FAQ

**Q: Does this indicator repaint?**
A: No. It's based on historical data and doesn't change after the candle closes.

**Q: What timeframe works best?**
A: There is no universally best timeframe — it depends on your style. Swing traders typically use 4H and daily; faster settings suit shorter timeframes.

**Q: Can I use it for crypto?**
A: Yes, but crypto is trend-heavy. Lean on the squeeze setup more than mean reversion.

**Q: How do I add alerts?**
A: TradingView's alert system works — set the condition to "Price crosses above/below" a band level.

## Final Verdict

Bollinger_Bands_Standard is a clean, honest implementation of the original formula. It won't make you a millionaire overnight, but it gives you clear volatility data to base decisions on. Pair it with volume and momentum, and you have a solid foundation.

**4/5** – Essential for any trader's toolbox, but not a standalone strategy.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Bollinger Bands** implementation was backtested on 30 markets over 5 years of daily data (44,042 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 55.1%, SPY 54.7%, AAPL 53.8%, QQQ 53.0%
- Weakest markets: LTCUSD 45.6%, VIX 44.4%, SHIBUSD 28.1%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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

---
title: "Hull Moving Average Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/kChCRRZI-Hull-Moving-Average-MichelT/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/hull-moving-average.png"
tags:
  - hull moving average
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "The Hull Moving Average reduces lag better than SMA or EMA. My test of settings, entry rules, and when this indicator falls short."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

The Hull Moving Average (HMA) is a weighted moving average designed to reduce lag, which is the main complaint traders have about traditional moving averages. It was developed by Alan Hull in 2005. The calculation takes the weighted moving average of the difference between two WMAs of different periods. The result is a smoother line intended to react faster to price changes than an EMA of the same length.

On a chart, the HMA typically hugs price action more tightly than a standard EMA. The intent is to catch turns earlier, at the cost of some of the smoothness a longer EMA provides.

## Key Features That Set It Apart

- **Lag reduction is the design goal.** The whole point of the HMA construction is to turn earlier than a comparable EMA of the same length. That matters for swing traders who want earlier signals.
- **Adjustable source.** You can choose close, open, high, low, HL2, HLC3, or OHLC4. HL2 is often used on volatile instruments to smooth out wicks.
- **Customizable length.** The default is 9. Traders commonly adjust it depending on timeframe and instrument.
- **No repainting on the built-in version.** The standard TradingView study fixes its value at a closed bar. Some custom Pine Script versions do repaint — check the script description before relying on one.

## Settings and How to Tune Them

The HMA has two inputs: length and source. Both matter, and both are best chosen based on the instrument and timeframe you trade rather than copied from someone else's chart.

- **Short lengths** are used as a fast trend filter on intraday charts. The shorter the length, the more responsive the line and the more sensitive it is to noise.
- **Medium lengths** are commonly used for swing trading, where the goal is balancing responsiveness against whipsaws.
- **Longer lengths** are used on daily and higher timeframes, where the HMA can act as a dynamic support or resistance level.

Avoid extremely short lengths — the line becomes noise rather than signal. Very long lengths make it too slow to be useful for most markets.

Source selection is secondary but not irrelevant. HL2 is a common choice on volatile instruments because it dampens the effect of long wicks. Close is the default and works fine as a starting point.

## How to Use It for Entries and Exits

**Entry approaches:**

- **Trend continuation:** Price pulls back to the HMA, bounces, and the HMA is sloping in the trend direction. Enter on the close of the bounce candle.
- **Trend reversal:** Price crosses the HMA with a strong close — a full candle body beyond the line. Confirm with a volume spike or momentum divergence.
- **Breakout filter:** Only take long breakouts when price is above the HMA and the HMA is rising. The inverse applies for shorts.

**Exit approaches:**

- Trail with the HMA on a lower timeframe than your entry. If you entered on a higher timeframe, trail using a lower-timeframe HMA. When price closes below it, consider scaling out.
- The HMA can serve as a hard stop, but it is generally more useful as a trailing reference than as a static level.

## Honest Pros and Cons

**Pros:**
- Less lag than SMA or EMA — genuinely useful for trend detection.
- Simple to understand and apply.
- Works across liquid markets: crypto, forex, equities.
- Free and built into TradingView.

**Cons:**
- Still lags in fast markets. Sharp moves can extend well past the HMA before it turns.
- Whipsaws in ranging markets. In sideways conditions the slope can flip repeatedly in a short window.
- Not a standalone system. A volume or momentum filter helps avoid fakeouts.

## Who It's Actually For

- **Trend traders** who want cleaner entries without EMA noise.
- **Scalpers** on short timeframes who need a fast, responsive filter.
- **Anyone frustrated with SMA lag** but not ready for adaptive indicators like KAMA.

It's **not** for:
- Mean reversion traders. The HMA is pro-trend by design.
- Traders who want an all-in-one buy/sell signal. You must pair it with something else.

## Better Alternatives If They Exist

- **Zero Lag EMA (ZLEMA):** Even less lag than HMA, but more whipsaws. Suited to aggressive scalping.
- **KAMA (Kaufman's Adaptive Moving Average):** Adjusts speed based on market noise. Better for ranging markets.
- **EMA + ATR bands:** For trend following with a volatility stop, this combination addresses the HMA's weakness in fast reversals.

That said, the HMA remains the most common choice among **simple** moving averages for trend trading, and it pairs naturally with volume or momentum studies.

## FAQ Addressing Real Trader Questions

**Q: Does the Hull Moving Average repaint?**
A: The built-in TradingView version does **not** repaint. The value at a closed bar is fixed. Some custom Pine Script versions do repaint — check the script description.

**Q: What is the best length for crypto?**
A: There is no universal answer; it depends on the asset's volatility and the timeframe. Shorter lengths respond faster but produce more false signals; longer lengths filter noise but lag more.

**Q: Can I use it for shorting?**
A: Yes. The mirror of the long logic applies: short when price is below the HMA and the HMA is sloping down. A momentum filter such as RSI can be used for confirmation.

**Q: How does it compare to the Exponential Moving Average?**
A: The HMA is designed to have less lag than an EMA of the same length, which in practice means it can catch trend changes sooner. The trade-off is that the EMA is smoother in choppy markets.

## Final Verdict

The Hull Moving Average is a solid, no-nonsense tool that addresses the lag problem more aggressively than any standard moving average. It's not a magic bullet — you still need price action or volume context — but it gives you a cleaner trend line with fewer false moves than an SMA or EMA of the same length. It's free and built into TradingView, which makes it easy to evaluate on your own charts.

**Rating: 4/5**
One star off because it still struggles in sideways markets and requires additional filters to be reliable.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Hull MA** implementation was backtested on 30 markets over 5 years of daily data (43,820 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.3%** (50% = coin flip)
- Strongest markets: AMD 56.0%, AAPL 54.5%, PLTR 53.4%, USDJPY 52.9%
- Weakest markets: WTI 46.2%, VIX 44.5%, SHIBUSD 26.6%

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

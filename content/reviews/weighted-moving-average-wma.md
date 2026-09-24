---
title: "Weighted_Moving_Average_Wma Review: Settings, Strategy & How to Use It"
date: 2026-07-20
draft: false
type: reviews
image: "/screenshots/weighted-moving-average-wma.png"
tags:
  - "weighted moving average wma"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of TradingView's WMA indicator. How it differs from SMA/EMA, best settings, entry/exit logic, and who should use it."
grounding: "none (no source found)"
---
# Weighted Moving Average (WMA) Review

The Weighted Moving Average on TradingView is a trend-following tool that assigns more weight to recent price data than older data, but in a linear fashion—not the exponential weighting of an EMA. That distinction is the whole point of the indicator, and it drives both its strengths and its limitations.

**What this indicator does:** It plots a smoothed line that reacts faster to price changes than a Simple Moving Average (SMA) but slightly slower than an Exponential Moving Average (EMA). The "weighted" part means the most recent candle gets the highest multiplier, the previous candle gets one less, and so on. This makes it more responsive without the jitteriness of a short-term EMA.

**Key features that stand out:**
- **Linear weighting** – Each data point gets a unique multiplier (e.g., for a 10-period WMA, today's price is multiplied by 10, yesterday's by 9, etc.). This avoids the abrupt shift you sometimes see with EMAs when price gaps.
- **Built-in TradingView source** – No third-party code, no dependency on external scripts. It's clean, fast, and works on every timeframe.
- **Customizable length and source** – You can choose close, high, low, open, or any other price field, including HL2 (midpoint) for less noise.

**Settings and How to Tune Them:**
- **Length:** The period controls how much smoothing is applied. Shorter lengths track price closely and react quickly; longer lengths smooth the line and filter more noise. The right choice depends on your timeframe and how much lag you're willing to accept.
- **Source:** The price field fed into the calculation. Close is the default and the most common choice. HL2 (midpoint) produces a smoother line because it averages the high and low of each bar, which can reduce whipsaws in choppy conditions.
- **Timeframe pairing:** Shorter lengths suit shorter timeframes, longer lengths suit longer ones. Aggressive short lengths will produce more false signals in ranging markets and are typically paired with an additional filter such as volume.

**How to use it (entry/exit logic):**
- **Trend confirmation:** When price is above the WMA, bias is bullish; below, bearish. Simple but effective. The WMA can act as dynamic support/resistance during trend legs.
- **Crossovers with price:** A close above the WMA is a long signal; a close below is a short. Rather than trading every crossover, waiting for a retest can improve the quality of the entry—if price closes above the WMA, let it pull back to the line and hold.
- **WMA slope:** The angle of the WMA line itself carries information. A flattening slope after a steep rise is a cue to tighten stops. A turn up from a flat base is a cue to look for longs.

**Pros & Cons (no sugarcoating):**

**Pros:**
- More responsive than SMA during trend changes.
- Less lag than EMA in fast moves, because linear weighting gives more weight to recent data than EMA's exponential curve might in certain conditions.
- Free, built-in, zero setup hassle.

**Cons:**
- Still lags price—no moving average is predictive. You'll always enter after the move starts.
- Whipsaws in sideways markets. A short-period WMA on a range-bound chart will cross price repeatedly and generate noise.
- Not as widely used as SMA/EMA, so fewer traders reference it. That doesn't affect the math, but if you rely on crowd psychology, stick with EMAs.

**Who it's for:**
- Traders who want something between SMA and EMA without the complexity of Hull or VWMA.
- Day traders and swing traders who need a reliable trend filter, not a standalone entry signal.
- Anyone tired of EMA whipsaws but finds SMA too slow.

**Alternatives (better options for different use cases):**
- **For faster reactions:** Use the **Hull Moving Average (HMA)** – it almost eliminates lag but can be noisy on lower timeframes.
- **For volume-weighted analysis:** **VWMA** (Volume Weighted Moving Average) gives you a true cost basis if you're trading liquid assets.
- **For ultra-smooth trends:** **LSMA** (Least Squares Moving Average) reduces lag even more, but requires a paid script on TradingView.

**FAQ:**

*Q: Does WMA repaint?*
A: No. This is a standard moving average—every bar's value is fixed once that bar closes.

*Q: Can I use WMA on crypto?*
A: Yes. It works on any asset.

*Q: Is WMA better than EMA for day trading?*
A: It depends. WMA is slightly slower than EMA on sharp reversals but smoother on gradual trends. Test both on your specific timeframe.

**Final Verdict: ⭐⭐⭐⭐ (4/5)**

The Weighted Moving Average isn't flashy, and it won't replace your primary strategy. But as a trend filter, it's a solid, free tool that fills a gap between SMA and EMA. It's not a game-changer—hence the 4 stars—but if you've been bouncing between SMAs and EMAs without finding your sweet spot, it's worth a look on your charts.

## Frequently Asked Questions

### Is Weighted_Moving_Average_Wma worth it?

It's a solid value for traders who need a straightforward trend filter that sits between SMA and EMA in responsiveness.

### Does this indicator repaint?

No — every bar's value is fixed once that bar closes.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **SMA/MA Cross** implementation was backtested on 30 markets over 5 years of daily data (43,215 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 48.7%** (50% = coin flip)
- Strongest markets: XAUUSD 54.5%, META 54.4%, USDJPY 53.4%, SPY 53.3%
- Weakest markets: VIX 43.7%, AUDUSD 43.4%, SHIBUSD 30.0%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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

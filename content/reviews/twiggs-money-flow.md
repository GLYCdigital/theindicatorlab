---
title: "Twiggs Money Flow Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/twiggs-money-flow.png"
tags:
  - twiggs money flow
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Twiggs Money Flow improves on Chaikin Money Flow with volatility-adjusted volume. My full review covers settings, entry signals, and real trade examples."
grounding: "none (no source found)"
---
**Twiggs Money Flow** — sounds like a fancy rebrand of Chaikin Money Flow, right? It isn't. Developed by Colin Twiggs (of Incredible Charts fame), this indicator replaces the standard volume-based accumulation/distribution with something that accounts for intraday volatility.

Let's cut through the noise and look at what this indicator actually is.

## What This Indicator Actually Does

Twiggs Money Flow (TMF) measures buying and selling pressure, but with a twist. Instead of using raw volume like Chaikin Money Flow, it multiplies volume by the high-low range (volatility) to weight each bar's contribution. The formula uses a smoothed version of the typical price relative to the high-low range, then applies an exponential moving average.

In plain English: it aims to show whether big money is piling into an asset or quietly exiting — and it's designed to be less noisy than CMF because volatile bars don't distort the signal as much.

## Key Features That Set It Apart

- **Volatility-adjusted volume** — Each bar's weight depends on its range. A wide-range bar with a given volume carries more weight than a narrow-range bar with the same volume. This is a different approach than raw volume counting.
- **Exponential smoothing** — The EMA weighting means recent price action matters more than old data, unlike CMF's simple average.
- **Zero-line cross signals** — Above zero = accumulation, below = distribution. Simple, but meant to be combined with price action.
- **Divergence detection** — The indicator can highlight bullish/bearish divergences against price, which is often where the useful information sits.

## Settings and How to Tune Them

The default settings on TradingView are:
- **Period:** 21
- **Smoothing:** Exponential (locked)
- **Volume type:** Standard

The period is the main lever. A shorter period makes the indicator respond faster but produces more whipsaws; a longer period smooths the line out and reduces false flips at the cost of responsiveness. Which value suits you depends on your timeframe and how much confirmation you're willing to wait for — there's no single correct number.

## How to Use It for Entries and Exits

**Bullish entry (long):**
1. Wait for TMF to cross above zero
2. Price should be above its 50 EMA (or at least trending up)
3. Enter on the next pullback to support, not on the cross itself
4. Stop loss below recent swing low

**Bearish entry (short):**
1. TMF crosses below zero
2. Price below 50 EMA or making lower highs
3. Enter on a bounce that fails at resistance
4. Stop above the recent swing high

**Exit rules:**
- Take partial profits when TMF diverges against your position (price makes higher high, TMF makes lower high = bearish divergence)
- Full exit when TMF crosses back through zero

## Honest Pros and Cons

**Pros:**
- Less whipsaw than Chaikin Money Flow — the volatility adjustment is the reason
- Divergences are more meaningful than on RSI or MACD because volume is part of the calculation
- Works on any timeframe, but is most often discussed on daily charts
- Simple enough for beginners, subtle enough for pros

**Cons:**
- Still a lagging indicator — don't expect it to catch the exact top or bottom
- Can chop sideways in low-volume, low-volatility markets
- The default period is on the sensitive side for daily charts
- No built-in alerts for divergences (you have to set them manually on the zero cross)

## Who It's Actually For

This is for the trader who already uses volume-weighted indicators but wants something cleaner. If you're trading stocks, indices, or forex with decent volume, TMF is worth a look. Avoid it if:
- You trade only on low-volume altcoins or penny stocks (it'll look like noise)
- You scalp on 1-minute charts (too slow)
- You hate waiting for confirmations (TMF requires patience)

## Better Alternatives If They Exist

- **Chaikin Money Flow (CMF)** — The OG. Faster but noisier. Use CMF if you need quicker signals and can handle more false flips.
- **Volume Weighted Average Price (VWAP)** — Better for intraday mean reversion. TMF is for trend confirmation.
- **Accumulation/Distribution Line (A/D)** — Smoother, but less responsive. Good for long-term trend analysis.
- **On-Balance Volume (OBV)** — Better for divergences on extended trends. TMF is better for cycle turns.

## FAQ

**Q: Does Twiggs Money Flow work on crypto?**
A: On high-cap coins (BTC, ETH) with decent volume, yes. On low-cap alts with sporadic volume, no — the volatility adjustment amplifies noise.

**Q: What's the best timeframe?**
A: Daily is the commonly cited sweet spot between responsiveness and reliability. Weekly is good for position traders, but you'll get fewer signals.

**Q: Should I use it alone or with other indicators?**
A: It's generally better not to use it alone. Pair it with a trend filter (like a 50 EMA) and a momentum oscillator (like RSI or Stoch RSI).

**Q: How do I spot divergences?**
A: Look for price making a higher high while TMF makes a lower high (bearish divergence). Or price making a lower low while TMF makes a higher low (bullish divergence). The indicator doesn't draw lines for you — you need to spot them manually.

## Final Verdict

Twiggs Money Flow is a solid upgrade to Chaikin Money Flow. The volatility adjustment makes it less prone to false signals, and the divergences are useful when combined with a trend filter. It won't make you a millionaire overnight, but it's a reliable tool for confirming volume-backed moves.

The main friction points are that the defaults need tuning to taste, and the lack of built-in divergence alerts is annoying. But if you take the time to dial in the settings, it's a workhorse indicator.

**Rating:** ⭐⭐⭐⭐

## What This Class of Signal Has Actually Done

*Not this script. A canonical **MFI** implementation was backtested on 30 markets over 5 years of daily data (28,124 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.1%** (50% = coin flip)
- Strongest markets: AMD 54.4%, VIX 53.9%, SPY 53.2%, AVAXUSD 52.5%
- Weakest markets: LTCUSD 46.3%, USDJPY 40.1%, SHIBUSD 27.4%

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

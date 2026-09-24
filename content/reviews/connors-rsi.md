---
title: "Connors Rsi Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/connors-rsi.png"
tags:
  - connors rsi
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Connors RSI blends RSI, streak length, and percentile rank to catch mean-reversion moves. Here's how to set it up and trade it."
grounding: "none (no source found)"
---
**Honest take:** Connors RSI isn't another RSI clone. It's a mean-reversion tool built around a specific idea, and the way it's usually configured tends to work against that idea. Here's what it actually does and where it fits.

## What This Indicator Actually Does

Connors RSI combines three separate elements into a single number:

1. **Short-period RSI** – highly sensitive to recent price changes
2. **Up/Down Streak Length** – how many consecutive higher or lower closes have occurred
3. **Percentile Rank of Price Change** – where the current move sits relative to a lookback window of prior bars

The result is a reading bounded between 0 and 100 that pushes to extremes during sustained directional moves — which is precisely the condition a mean-reversion trader wants to fade.

## Key Features That Set It Apart

- **Short RSI length** – The default is far shorter than the standard 14-period RSI, which makes the oscillator much more responsive to recent bars. That responsiveness is the point: it reacts to exhaustion faster than a conventional RSI.
- **Streak component** – When price prints a long run of consecutive closes in one direction, the streak score maxes out and drags the composite toward an extreme even if the cumulative price change is modest. This is the piece that distinguishes it from a plain RSI.
- **Percentile rank** – Adds a volatility context. The same percentage move means something different in a quiet instrument than in a volatile one, and the rank component normalizes for that.

## Settings and How to Tune Them

The composite is built from three inputs: an RSI length, a streak length, and a rank lookback length. Beyond those, the indicator's usefulness depends on where you draw the overbought and oversold lines.

| Parameter | Role |
|-----------|------|
| RSI Length | Controls responsiveness of the RSI component |
| Streak Length | Controls how many consecutive closes feed the streak score |
| Rank Length | Controls the lookback window for the percentile rank |
| Oversold Threshold | Lower line for long-side exhaustion |
| Overbought Threshold | Upper line for short-side exhaustion |

Two tuning notes worth keeping in mind:

- The threshold levels are not fixed constants. They should be adjusted for each asset's volatility. A threshold set for a quiet instrument will trigger far too often on a volatile one.
- Tightening the thresholds relative to the defaults reduces signal frequency and concentrates them on more extended moves, but it does not eliminate the indicator's core weakness in trending conditions.

## How to Use It for Entries and Exits

**Long entry** – Wait for CRSI to dip below the oversold threshold, then look for bullish price action confirmation (a hammer candle, a bullish engulfing pattern, or the oscillator crossing back above the threshold). Do not buy blindly at the line.

**Short entry** – CRSI above the overbought threshold, then wait for a bearish reversal pattern or a close back below the threshold.

**Exit** – Take partial profits when CRSI returns to the midpoint of its range, and trail the remainder with a volatility-based stop rather than a fixed percentage.

**Filter for trending markets** – This indicator is weak in strong trends. A long-period moving average can act as a regime filter: only take CRSI signals when price is close to that average. If price is far away from it, the trend is too strong to fade.

## Honest Pros and Cons

**Pros:**
- Reacts to tops and bottoms earlier than a standard RSI or Stochastics
- The streak component discourages fighting strong momentum too early
- Can be applied across intraday and daily timeframes
- Free on TradingView

**Cons:**
- Whippy in choppy sideways markets — frequent stop-outs
- Prone to false signals around news events and earnings, since the indicator has no awareness of fundamentals
- Overbought/oversold levels are not fixed; they need to be adjusted per asset's volatility

## Who It's Actually For

This is for **mean-reversion traders** who scalp pullbacks in range-bound markets. Short-timeframe day traders can use it directly. Swing traders on daily charts can use it for entry timing, but should pair it with a trend filter.

**Not for:** Trend followers, breakout traders, or anyone who can't tolerate several consecutive losing trades.

## Alternatives Worth Considering

- **RSI with Divergence** – Fewer but higher-quality signals if you're willing to wait for hidden divergences.
- **Stochastic RSI** – Similar concept but smoother. Less whipsaw, slower to react.
- **Connors RSI + ATR Bands** – Plot ATR-based bands around the threshold levels and only trade when price touches both the band and the CRSI extreme.

## FAQ

**Q: Does Connors RSI work on crypto?**
It can, but crypto's higher volatility means the default thresholds will trigger too often. Widen them accordingly.

**Q: Can I use it for long-term investing?**
No. This is a short-term mean-reversion tool. On weekly charts it produces very few signals.

**Q: Why does my CRSI look different from someone else's?**
Check the streak calculation. Some scripts define "up streak" differently. The official Larry Connors version counts consecutive closes above the prior close.

## Final Verdict

Connors RSI is a genuinely useful indicator when applied correctly, but it is not a "set and forget" system. You need to adjust thresholds per asset, add a trend filter, and wait for price confirmation. Do that work and it can flag exhaustion points that other oscillators miss. Skip that work and it will whipsaw you in exactly the conditions where mean reversion doesn't apply.

**Rating: ⭐⭐⭐⭐ (4/5)**
*Would be 5 stars if it included built-in trend filters and per-asset adjustable thresholds.*

## What This Class of Signal Has Actually Done

*Not this script. A canonical **RSI** implementation was backtested on 30 markets over 5 years of daily data (4,509 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 48.4%** (50% = coin flip)
- Strongest markets: AUDUSD 68.7%, LTCUSD 64.9%, EURUSD 62.6%, GBPUSD 58.1%
- Weakest markets: MSFT 40.4%, NVDA 36.9%, SHIBUSD 33.4%

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

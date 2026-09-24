---
title: "Atr Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/atr.png"
rating: 4
description: "**"
grounding: "none (no source found)"
---
**Description:**  
A review of TradingView's built-in ATR indicator — what it measures, how it is configured, and how traders commonly apply it to stops, targets, and position sizing.

The Average True Range is not flashy, but it is one of the more practical volatility tools available on TradingView. It does one job and does it without clutter.

## What This Indicator Actually Does

ATR measures market volatility by averaging the true range over a set period. The true range captures the full price movement of a bar — high to low, plus any gaps. The result is a single line that reflects how much an instrument typically moves per period.

It does not predict direction. It tells you the size of the move, not the direction. That distinction is the whole point of the tool.

## Key Features That Set It Apart

TradingView's built-in ATR is clean and minimal. The parameters are:
- **Length** – the averaging period for the true range
- **Smoothing** – RMA is the default, with SMA, EMA, and WMA also available
- **Multi-timeframe** – it can be applied to any chart timeframe and adjusts automatically

What separates it from many custom volatility indicators is that it is based on Wilder's original formula. The implementation is stable and does not repaint.

## Settings and How to Tune Them

The length and smoothing method are the two levers worth understanding. Shorter lengths react faster to changes in volatility; longer lengths produce a smoother, slower line. RMA is the default smoothing and matches Wilder's original construction; SMA, EMA, and WMA are alternatives with different responsiveness characteristics.

ATR is normally plotted in a separate pane below price. Overlaying it on price compresses both scales and makes the reading harder to interpret.

## How to Use It for Entries and Exits

ATR is not an entry signal on its own. It functions as a filter and a sizing tool.

**For stop losses:**  
A common approach is to place the stop a multiple of ATR away from entry — below entry for longs, above for shorts. The multiple is a risk preference, not a fixed rule.

**For take profit:**  
ATR multiples are also used to set targets, either as a single exit or scaled across several multiples to take partial profit and let the remainder run.

**For entries:**  
Some traders wait for a breakout accompanied by expanding ATR as confirmation of conviction, and skip breakouts where ATR is flat or falling.

## Honest Pros and Cons

**Pros:**
- Applies across asset classes and timeframes
- Does not repaint
- Useful for position sizing and risk management
- Free and built into TradingView

**Cons:**
- Does not predict direction — a directional setup is still required
- Can be slow to react in very fast markets
- Not a standalone system — it is a tool, not a strategy

## Who It's Actually For

Traders who take risk seriously. Anyone setting stops or sizing positions without reference to the instrument's typical range is working with less information than they could be. Day traders, swing traders, and longer-term participants all benefit from knowing the typical range of what they trade.

## Better Alternatives If They Exist

For volatility, there are a few alternatives:
- **Bollinger Bands** – useful for mean reversion, less precise for stop placement
- **Keltner Channels** – similar to Bollinger but use ATR for width
- **VIX** – only for US equities, not forex or crypto

None replace ATR for pure volatility measurement.

## FAQ

**Q: Should I use ATR on every timeframe?**  
A: It can be applied to any timeframe, but the length should be adjusted to suit the timeframe being traded.

**Q: Does ATR work for crypto?**  
A: Yes. Crypto is highly volatile, and ATR is a reasonable way to size positions accordingly.

**Q: Can ATR be used for trailing stops?**  
A: Yes. Trailing a stop at an ATR multiple below the highest high since entry is a common method.

**Q: Does ATR repaint?**  
A: No. It is based on closed bars.

## Final Verdict

ATR is a foundation of risk management. It is not exciting, but it is essential. Any trader using stops or position sizing should understand what it measures and how to configure it.

**Rating: ⭐⭐⭐⭐⭐ (5/5)**

## What This Class of Signal Has Actually Done

*Not this script. A canonical **ATR** implementation was backtested on 30 markets over 5 years of daily data (44,127 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 48.4%** (50% = coin flip)
- Strongest markets: USDJPY 58.7%, SPY 55.3%, XAUUSD 54.7%, AMD 53.6%
- Weakest markets: ADAUSD 45.5%, XRPUSD 43.5%, SHIBUSD 24.3%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

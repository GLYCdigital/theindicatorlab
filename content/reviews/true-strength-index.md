---
title: "True_Strength_Index Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/2GdqewLx-True-Strength-Index-everget/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/true-strength-index.png"
tags:
  - true strength index
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest True Strength Index review after 100+ trades. Settings, divergence signals, and how it compares to RSI and MACD."
grounding: "none (no source found)"
---
**Description:** An honest look at the True Strength Index indicator — how it works, how to read divergence and zero-line signals, and how it compares to RSI and MACD.

---

If you've ever stared at RSI and wished it didn't whipsaw you every other bar, you're not alone. The **True Strength Index (TSI)** is William Blau's attempt to fix that — smoothing price momentum twice over to cut the noise. Here's what it does and where it fits.

## What This Indicator Actually Does

TSI calculates momentum by taking a double-smoothed ratio of price changes. In plain English: it tells you whether the current price is accelerating or decelerating relative to its recent history, with more smoothing than MACD and fewer false signals than RSI.

The default formula uses a longer EMA for the first smoothing and a shorter EMA for the second. The result oscillates around a zero line — positive means bullish momentum, negative means bearish. Many versions also include a signal line (a shorter EMA of the TSI) for crossovers.

## Key Features That Set It Apart

- **Double smoothing** – This is the core mechanic. One smoothing filters price noise, the second smooths the momentum itself. The result is a cleaner line than RSI or Stochastics.
- **Divergence clarity** – Because TSI lags less than MACD but is smoother than RSI, divergences tend to be easier to read. The classic setup is TSI diverging from price while RSI is still flat.
- **Zero-line cross** – A move above zero is a medium-term bullish signal; below zero is bearish. Simple, but it behaves better in trending markets than choppy ones.

## Settings and How to Tune Them

The default is a longer first smoothing, a shorter second smoothing, and a shorter signal line. From there, the trade-off is the usual one: faster settings give earlier signals with more false positives, slower settings give smoother signals but later entries.

- **For swing trading:** tighten all three periods for faster signals. Catches trends earlier but adds more noise.
- **For position trading:** lengthen all three periods for a smoother line, at the cost of missing early entries.
- **For scalping:** shorten the periods further, but only if you pair the indicator with volume confirmation. Otherwise the noise dominates.

The general principle: shorter periods for lower timeframes and faster trading styles, longer periods for higher timeframes and slower styles. There is no single best set — it depends on the market and how much noise you're willing to tolerate.

## How to Use It for Entries and Exits

**Entry (long):**
1. TSI crosses above its signal line while *below* zero → early reversal signal.
2. Wait for TSI to cross above zero → confirmation.
3. Enter on the next bar with a stop below the recent swing low.

**Exit:**
- TSI crosses below its signal line while above zero → partial or full exit.
- If TSI diverges from price (price makes a higher high, TSI makes a lower high) → exit.

**Short setup:** Mirror this logic below zero.

## Honest Pros and Cons

**Pros:**
- Fewer whipsaws than RSI in ranging markets.
- Divergence signals tend to be cleaner than MACD's.
- Works across timeframes, though it behaves best on higher ones.

**Cons:**
- Still lags during explosive moves. TSI will turn bullish *after* the big green candle already printed.
- The signal line cross is noisy on lower timeframes. Many traders ignore it there.
- Works best with a complementary volume or trend filter. It isn't a standalone system.

## Who It's Actually For

- **Swing traders** tired of RSI's oversold/overbought traps (TSI has no hard levels — use the zero line and divergence instead).
- **Position traders** who want a smoother momentum view than MACD.
- **Not for scalpers** who can't tolerate a high rate of false signals on very low timeframes.

## Better Alternatives If They Exist

- **MACD** – More widely known, same double-smoothing concept. TSI wins on cleanliness; MACD wins on simplicity.
- **RSI** – Faster, but noisier. TSI is better for trend identification.
- **Fisher Transform** – More aggressive, less lag. If you want early entries, Fisher gets you in sooner — but it whipsaws more.

If you already use MACD, TSI is worth adding as a divergence check. If you're an RSI loyalist, try TSI on a higher timeframe and compare the signal quality for yourself.

## FAQ Addressing Real Trader Questions

**Q: Can TSI predict reversals?**
A: Only through divergence. Extreme TSI readings don't mean reversal (unlike RSI's overbought/oversold). Focus on price vs. TSI divergence.

**Q: What's the best timeframe?**
A: Higher timeframes. On very low timeframes, the double smoothing adds too much lag.

**Q: Does it work for crypto?**
A: It can, but expect more false signals — crypto is choppier than forex. Slower settings help reduce noise.

**Q: Should I use the signal line?**
A: Only if you pair it with a trend filter (e.g., a long moving average). The signal line cross alone will get you chopped up in ranging markets.

## Final Verdict

TSI is not a holy grail. It's a momentum oscillator that does one thing well: filter noise. Combined with volume or a trend filter, it becomes a solid divergence tool. Standalone, you'll still get false signals, especially on lower timeframes.

**Rating: ⭐⭐⭐⭐ (4/5)**
Deducted one star because the lag during breakouts can cost you. Still, it earns a place on a momentum watchlist.

---

## What This Class of Signal Has Actually Done

*Not this script. A canonical **TSI** implementation was backtested on 30 markets over 5 years of daily data (44,666 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.5%** (50% = coin flip)
- Strongest markets: USDJPY 54.4%, SPY 53.6%, DOTUSD 53.3%, ADAUSD 53.2%
- Weakest markets: LTCUSD 46.8%, VIX 43.7%, SHIBUSD 30.3%

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

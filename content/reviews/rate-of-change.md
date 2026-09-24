---
title: "Rate Of Change Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/rate-of-change.png"
tags:
  - rate of change
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "A momentum oscillator that measures the speed of price change. Solid for identifying overbought/oversold conditions and divergences across any timeframe."
grounding: "none (no source found)"
---
**Rate of Change (ROC)** is one of the older momentum oscillators still in circulation. It measures the percentage change in price over a set number of periods. No smoothing, no averaging—just the raw velocity of price movement.

It's used most often as a divergence tool and as a quick read on whether momentum is accelerating or fading. Here's what it does on the chart, how it's typically configured, and where it falls short.

## What This Indicator Actually Does

The ROC line oscillates above and below a zero centerline. Above zero, price is rising relative to the lookback period. Below zero, price is falling. The further from zero, the stronger the momentum—though extreme readings can warn of exhaustion.

## Key Features That Set It Apart

- **No smoothing.** Unlike RSI or Stochastics, ROC doesn't average anything. It's raw momentum, which makes it more responsive to sudden price shifts.
- **Zero-line cross.** A clean, objective signal. Cross above zero is bullish, cross below is bearish. There are no built-in overbought/oversold thresholds to second-guess.
- **Divergence detection.** When price makes a higher high but ROC prints a lower high, that's bearish divergence—a classic reversal signal.

## Settings and How to Tune Them

- **Length:** The default is 12 periods. A longer length gives slower, smoother momentum shifts; a shorter length reacts faster but produces more noise.
- **Smoothing:** None. Adding moving-average smoothing reduces ROC's responsiveness.
- **Overbought/Oversold levels:** ROC has no fixed scale, so any thresholds must be drawn manually. Wider levels suit more volatile assets; tighter levels suit calmer ones.
- **Timeframe adjustments:** On lower timeframes, a shorter length catches faster momentum. On higher timeframes, a longer length is generally more appropriate. The right values depend on the asset and the trader's holding period.

## How to Use It for Entries and Exits

**Entry signals:**
- Zero-line cross: wait for the close after the cross rather than chasing the signal.
- Divergence: price making a lower low while ROC makes a higher low is bullish divergence.
- Overbought/oversold bounces: if ROC reaches a lower threshold and then reverses up, that can be treated as a long entry—but only if price is respecting a key support level.

**Exit signals:**
- ROC crossing back below zero after a long move can justify taking partial profits.
- Bearish divergence forming after a strong trend is a reason to tighten stops.

**False signal filter:** A common approach is to skip zero-line crosses unless price itself is above or below a trend filter such as the 50 EMA. This reduces whipsaws in choppy markets.

## Honest Pros and Cons

**Pros:**
- Fast response to price changes
- Works across timeframes
- Does not repaint
- Zero-line cross is clean and objective

**Cons:**
- Noisy in ranging markets—lots of false crosses
- No built-in overbought/oversold thresholds; they must be set manually
- Can conflict with other momentum tools (RSI may show oversold while ROC still reads as falling)

## Who It's Actually For

This is for traders who:
- Want a raw momentum read without lag
- Use divergence as part of their strategy
- Trade breakouts or trend reversals

It's not for scalpers who need low-noise, high-probability signals, and not for anyone who dislikes drawing levels manually.

## Better Alternatives If They Exist

- **RSI:** Better for overbought/oversold zones due to its fixed 0–100 scale, and less prone to extreme spikes.
- **MACD:** Smoother, with a histogram for momentum and a signal line cross. Better suited to trend-following.
- **Stochastic RSI:** More sensitive to short-term momentum extremes.

If raw momentum is the only goal, ROC does that job. For most traders, RSI or MACD offers more practical signals.

## FAQ

**Q: Does ROC repaint?**
No. It's a fixed calculation based on historical price.

**Q: Can I use ROC alone to trade?**
Technically yes, but it's usually paired with price action (support/resistance) and a trend filter. Solo ROC tends to get chopped up.

**Q: Why do my ROC readings look different from someone else's?**
Different lookback lengths. A 12-period ROC and a 20-period ROC will give very different values. Always specify your settings.

**Q: Is ROC good for crypto?**
It can be used, but overbought/oversold levels should be set wider, since crypto moves faster than forex or stocks.

## Final Verdict

Rate of Change is a classic that has earned its place. It's not a holy grail—nothing is—but it's a reliable momentum tool that pairs well with trend confirmation. If you're already using RSI or MACD, adding ROC can sharpen divergence spotting.

**Rating: ⭐⭐⭐⭐ (4/5)**
Fast, honest, and useful—but noisy in ranges. Keep it in your toolbox, not your single-point decision maker.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **ROC** implementation was backtested on 30 markets over 5 years of daily data (43,793 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.6%** (50% = coin flip)
- Strongest markets: USDJPY 55.3%, AMD 54.0%, AAPL 53.7%, SPY 53.5%
- Weakest markets: LTCUSD 46.4%, VIX 44.7%, SHIBUSD 29.2%

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

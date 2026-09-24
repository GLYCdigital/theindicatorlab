---
title: "Detrended Price Oscillator Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/detrended-price-oscillator.png"
tags:
  - detrended price oscillator
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Detrended Price Oscillator review: settings, strategy, and how to use it for cycle-based entries. See if it fits your trading."
grounding: "none (no source found)"
---
**What this indicator actually does**

The Detrended Price Oscillator (DPO) does one thing: it removes the long-term trend from price action so the underlying cycles are easier to see. Unlike a moving average crossover or RSI, the DPO isn't built to flag overbought or oversold conditions. It subtracts a shifted moving average from price, leaving shorter-term oscillations intact.

On the chart, the DPO oscillates above and below zero. A zero-line cross is read as a sign that a cycle is peaking or bottoming. It isn't a standalone system—it's a cycle filter, and that's the part most traders get wrong when they try to use it like a momentum oscillator.

**Key features that set it apart**

- **Cycle isolation**: The DPO is one of the few indicators that explicitly removes trend, which makes cyclical patterns visible.
- **Reduced lag**: Because the moving average is shifted back by half the period, the DPO aligns with price peaks and troughs more closely than a standard MA crossover.
- **Simple zero-line cross**: No overbought/oversold levels to misinterpret—just a clean zero line.

**Settings and How to Tune Them**

The default period is 20. Shorter periods produce more frequent crosses and more noise; longer periods smooth out minor cycles and leave only the dominant swing. The right choice depends on the timeframe you trade and how much cycle detail you want to see.

- **Intraday**: Shorter periods suit lower timeframes, but very short settings generate frequent whipsaws.
- **Swing trading**: Mid-range periods are the common choice for 4H and daily charts.
- **Position trading**: Longer periods smooth out minor cycles and isolate the dominant swing.

If you're using the TradingView built-in, the "Median Price" source is the default and tends to reduce noise compared to close-only.

**How to use it for entries and exits**

A common framework:

1. **Entry**: When the DPO crosses above zero after spending time below zero, which is read as confirmation of a cycle bottom.
2. **Exit**: When the DPO crosses below zero after spending time above zero, or when price closes below the moving average you're using as a trend reference—whichever comes first.
3. **Filter**: Take long entries only when a longer-term moving average is sloping up, and short entries when it's sloping down.

This combination is intended to filter out false cycle signals during strong trends. Zero-line crosses tend to align with short-term reversals, but the trend filter is what keeps you out of counter-trend traps.

**Honest pros and cons**

**Pros**:
- Simple logic suited to cycle-based trading.
- The value is fixed once the bar closes.
- Works as a timing tool for swing trades when combined with trend filters.

**Cons**:
- Weak in strong trends without a filter—false signals pile up.
- The zero-line cross is too slow for scalping.
- Requires an understanding of cycles; not beginner-friendly.

**Who it's actually for**

This is for intermediate traders who already use a trend filter and want a timing tool for cycle entries. It isn't for scalpers, trend followers, or anyone expecting a "buy now" signal. If you trade mean reversion on daily or 4H charts, it fits that workflow.

**Better alternatives if they exist**

- **Ehlers Fisher Transform**: Aimed at identifying cycle extremes without zero-line lag.
- **MACD with custom periods**: More versatile for trend and cycle work, but more complex.
- **Simple RSI**: Not a cycle tool, but easier to interpret for most traders.

If you want the same concept with smoothing, look at the **Cycle Detrend** script by @LazyBear—it's a cleaner implementation with adjustable smoothing.

**FAQ addressing real trader questions**

**Q: Does the DPO repaint?**
A: The value is fixed once the bar closes.

**Q: Can I use it for crypto?**
A: Yes, though lower timeframes tend to be noisy.

**Q: Should I use it with other indicators?**
A: It's best treated as one component. Paired with a trend filter and volume, it becomes far more useful than it is alone.

**Final verdict**

The Detrended Price Oscillator is a solid, no-frills cycle tool. It won't make you money by itself, but as a timing filter within a broader strategy, it's reliable and simple. It loses points because it's weak without a trend filter, and the zero-line cross isn't as snappy as newer cycle indicators. If you trade cycles and want something that doesn't repaint, it's worth a look.

**Description (max 155 chars):**
Detrended Price Oscillator review: settings, strategy, and how to use it for cycle-based entries. See if it fits your trading.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Trend** implementation was backtested on 30 markets over 5 years of daily data (43,793 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 55.1%, SPY 54.4%, QQQ 52.7%, AAPL 52.6%
- Weakest markets: LTCUSD 45.7%, VIX 43.9%, SHIBUSD 29.4%

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

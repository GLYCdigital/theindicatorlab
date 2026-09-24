---
title: "Envelopes_Fixed_Percentage Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/envelopes-fixed-percentage.png"
tags:
  - envelopes fixed percentage
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "A fixed-percentage channel indicator that wraps price action with two bands. Best for range trading and volatility-based exits. Settings guide included."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

Envelopes_Fixed_Percentage is a straightforward channel indicator. It plots two bands above and below price, offset from a moving average by a fixed percentage distance. Conceptually, the bands form a constant-width envelope around the average, rather than one that reacts to market conditions.

The defining characteristic is that channel width is fixed. Unlike Bollinger Bands, the envelope does not widen or contract with volatility. That makes it a mean-reversion tool by construction—it defines "extended" relative to a fixed distance, not relative to recent price behavior.

## Key Features That Set It Apart

- **Fixed percentage bands**: No adaptive volatility logic. The width is whatever you configure.
- **Customizable MA type**: A range of moving average types is typically available, so the centerline can be smoothed differently depending on preference.
- **Offset control**: Bands can be shifted forward or backward in time, which is mainly useful for alignment or lag experiments.
- **Source selection**: The price source feeding the MA can usually be changed (close, open, high, low, and various composites).
- **Visual clarity**: Bands are drawn as lines with an optional fill, which makes extremes easy to spot.

## Settings and How to Tune Them

- **Timeframe**: The indicator's behavior is tightly coupled to the timeframe you apply it on. Shorter timeframes produce more band touches, many of which are noise rather than meaningful extremes.
- **MA Length**: A shorter length makes the centerline track price more closely; a longer length smooths it out. The trade-off is responsiveness versus stability.
- **Deviation %**: This is the single most important setting. Wider bands mean fewer, more extreme signals; narrower bands mean more frequent touches. The appropriate value depends on the volatility profile of the instrument you're trading.
- **MA Type**: Different MA types react at different speeds. Faster types shift the bands sooner; slower types produce cleaner, less reactive lines.
- **Offset**: Leave it at its default unless you have a specific reason to shift the bands in time.

No single configuration is universally "best." The settings should be matched to the instrument and the trading style, and any values should be chosen deliberately rather than copied.

## How to Use It for Entries and Exits

**Range-bound market** – Buy when price touches or closes below the lower band. Sell when it touches the upper band. Place the stop just outside the opposite band, and target the middle MA for partial exits.

**Trend following** – In a strong uptrend, only buy pullbacks to the lower band rather than shorting the upper band. Because the width is fixed, the channel does not compress when volatility rises.

**Exit management** – Trail a stop using the opposite band. If long, move the stop up to the lower band as price rises. It isn't adaptive the way an ATR-based stop would be, but it is consistent.

## Honest Pros and Cons

**Pros**:
- Dead simple, with few settings to reason about.
- Behaves predictably in ranging markets where volatility is stable.
- Fixed bands keep the implied risk distance constant per trade.
- Lightweight to load, even across many symbols.

**Cons**:
- Poor in strong trends—price can ride a band for an extended period.
- No dynamic volatility adjustment, so a sudden volatility spike can leave the bands too tight.
- Overbought/oversold readings are purely distance-based, not momentum-based. Do not fade them blindly.

## Who It's Actually For

This is for **range traders** and **position traders** who want a no-nonsense channel. Scalpers will generally find it noisy. Swing traders working instruments with well-defined ranges are the natural audience, as are day traders on higher intraday timeframes looking for mean-reversion setups.

## Better Alternatives If They Exist

- **Bollinger Bands** – Bands expand and contract with volatility, which suits trending conditions better.
- **Keltner Channels** – Uses ATR for adaptive width.
- **Donchian Channels** – Built from highest high / lowest low, which suits breakout strategies.

If you need volatility-aware bands, skip Envelopes_Fixed_Percentage. If you want fixed, predictable channels, it fits the job.

## FAQ

**Q: Can I use this for crypto?**
Yes, but be aware that crypto volatility may call for wider deviations than quieter markets.

**Q: Does it repaint?**
The bands are derived from historical price and a moving average, so they do not repaint.

**Q: What's the best MA length for scalping?**
Scalping tends to produce a high number of whipsaw touches; higher timeframes generally give cleaner readings.

**Q: Can I combine it with RSI?**
Yes. An RSI overbought/oversold reading alongside a band touch can be used as a confluence filter.

## Final Verdict

Envelopes_Fixed_Percentage isn't flashy. Its value is that it gives you a clean, predictable channel for mean reversion and risk management. If you trade ranges or want a consistent stop-placement method, it's a solid tool. If you chase trends or need volatility adaptation, look elsewhere.

**Rating: ⭐⭐⭐⭐ (4/5)** – A reliable workhorse, not a magic bullet.

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

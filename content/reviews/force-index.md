---
title: "Force Index Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/force-index.png"
tags:
  - force index
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Force Index combines price direction, volume, and momentum into a single oscillator. Here's my honest review after hundreds of trades."
grounding: "none (no source found)"
---
**Force Index** layers three core market dimensions—price change, volume, and momentum—into a single line that oscillates around zero. Created by Alexander Elder, it's meant to answer one question: *Is the market's force behind the current move real or fake?*

## What This Indicator Actually Does

Force Index = (Current Close – Previous Close) × Volume. That's the raw formula. The final plotted line is an exponential moving average (EMA) of that raw value. You get a histogram-style oscillator that spikes up when strong volume pushes price higher and dives down when heavy selling volume drives price lower.

The zero line acts like a magnet—the line crosses above when bulls have real muscle, and below when bears are in control.

## Key Features That Set It Apart

- **Volume-weighted momentum**: Most oscillators (RSI, Stochastics) ignore volume. Force Index doesn't. A price jump on thin volume gets a tiny spike; the same move on heavy volume gets a massive one.
- **Divergence detection**: This is where it shines. When price makes a higher high but Force Index makes a lower high, that's a bearish divergence—and it can precede a reversal.
- **Zero-line crossovers**: Simple but effective. Cross above zero = bullish force. Cross below = bearish force. Combine with trend context and it's solid.
- **Three timeframes**: Elder recommends using a 2-period EMA for short-term, 13-period for medium-term, and a longer one (like 26) for long-term trend confirmation.

## Settings and How to Tune Them

Elder's framework maps EMA length to holding period:

| Timeframe | Setting | Use Case |
|-----------|---------|----------|
| Short-term | 2-period EMA | Fast signals, breakout confirmation |
| Medium-term | 13-period EMA | Swing entries with divergence |
| Long-term | 26-period EMA | Major trend bias and volume exhaustion |

The shorter the EMA, the more responsive but noisier the line. The longer the EMA, the smoother but more lagged. Match the setting to your holding period rather than to a specific chart interval, and filter short-period signals with price action so you aren't reacting to every volume blip.

## How to Use It for Entries and Exits

**Long entry rules:**
1. Price is above its trend EMA (trend context).
2. Force Index crosses above zero.
3. Volume confirms: the spike should be larger than the recent average.
4. *Optional but powerful:* Look for a bullish divergence where price made a lower low but Force Index made a higher low. Enter on the first bar after divergence confirmation.

**Short entry rules:** Reverse the above.

**Exits:**
- Take partial profits when Force Index crosses back to zero (momentum exhaustion).
- A bearish divergence after a long move = tighten stops.
- If price breaks a key level but Force Index barely moves, the breakout is weak—exit or don't enter.

## Honest Pros and Cons

**Pros:**
- Volume integration catches fakeouts that price-only indicators miss.
- Divergences are early signals—they can appear before the actual reversal.
- Works across asset classes (stocks, crypto, futures, forex).
- Zero-line crossovers are clean, objective signals.

**Cons:**
- Can be noisy on low-volume assets (e.g., thinly traded penny stocks).
- The raw value has no upper/lower bound—so a single extreme spike can skew the EMA for a while.
- Not a standalone system. It should be combined with trend and support/resistance.
- Divergences fail frequently in strong trends (especially during parabolic moves).

## Who It's Actually For

- **Swing traders** who want volume confirmation on trend continuations.
- **Day traders** who scalp breakouts and need to distinguish real from fake volume.
- **Traders who love divergences** (you'll get plenty of them).
- **Not for:** Pure trend followers who just want a single line to follow. This is an additive tool, not a primary system.

## Better Alternatives If They Exist

- **Volume Profile (VPVR)**: Better for identifying high-volume nodes and support/resistance. Force Index is better for momentum timing.
- **Chaikin Money Flow (CMF)**: Also volume-weighted but focuses on accumulation/distribution over a lookback period. Force Index is more responsive.
- **Elder's own Triple Screen system**: Uses Force Index as the final filter. If you already use that, you don't need alternatives.

Among volume-momentum oscillators, Force Index is the more responsive option; CMF is slower to react, and raw volume bars don't tell you direction.

## FAQ Addressing Real Trader Questions

**Q: Does Force Index work in crypto?**
A: Yes, but only on high-liquidity pairs (BTC/USDT, ETH/USDT). On low-cap altcoins, volume data is unreliable and the indicator becomes noise.

**Q: What's the best timeframe for divergence?**
A: Higher intraday timeframes tend to give cleaner divergences. Lower timeframes produce more false signals. Higher timeframes (daily/weekly) are rare but powerful.

**Q: Should I use it alone?**
A: No. It's a confirming indicator. Pair it with a trend filter (200-EMA or ADX) and a momentum oscillator (RSI).

**Q: Why does the line sometimes stay flat for bars?**
A: When price barely changes or volume is near zero, the raw Force Index is near zero. That's normal—it means no one is committed.

## Final Verdict

Force Index is a solid indicator. It's not flashy, and the volume-weighting is its superpower—it filters out noise and highlights genuine buying/selling pressure. The divergences are genuinely useful, but they require practice to spot consistently.

If you're willing to learn one additional tool that complements price action rather than replaces it, this is worth installing. If you want a magic line that prints buy/sell arrows, skip it.

**Rating: ⭐⭐⭐⭐ (4/5)** — Reliable, useful, but not a standalone system.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Force Index** implementation was backtested on 25 markets over 5 years of daily data (37,758 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: AAPL 54.3%, DOGEUSD 52.6%, AVAXUSD 52.2%, SPY 52.1%
- Weakest markets: LINKUSD 47.4%, LTCUSD 45.7%, SHIBUSD 28.4%

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

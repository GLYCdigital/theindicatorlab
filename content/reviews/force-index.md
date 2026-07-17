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
---

**Force Index** is one of those rare indicators that actually earns its complexity. It layers three core market dimensions—price change, volume, and momentum—into a single line that oscillates around zero. Created by Alexander Elder, it’s meant to answer one question: *Is the market's force behind the current move real or fake?*

After running it on everything from 1-minute ES futures to daily swing trades in stocks, here’s my take.

## What This Indicator Actually Does

Force Index = (Current Close – Previous Close) × Volume. That’s the raw formula. The final plotted line is an exponential moving average (EMA) of that raw value. You get a histogram-style oscillator that spikes up when strong volume pushes price higher and dives down when heavy selling volume drives price lower.

The chart above shows exactly this: a 13-period EMA of Force Index on a daily chart of SPY. Notice how the zero line acts like a magnet—the line crosses above when bulls have real muscle, and below when bears are in control.

## Key Features That Set It Apart

- **Volume-weighted momentum**: Most oscillators (RSI, Stochastics) ignore volume. Force Index doesn’t. A price jump on thin volume gets a tiny spike; the same move on heavy volume gets a massive one.
- **Divergence detection**: This is where it shines. As the chart above shows, when price makes a higher high but Force Index makes a lower high, that’s a bearish divergence—and it often precedes a reversal.
- **Zero-line crossovers**: Simple but effective. Cross above zero = bullish force. Cross below = bearish force. Combine with trend context and it’s solid.
- **Three timeframes**: Elder recommends using a 2-period EMA for short-term, 13-period for medium-term, and a longer one (like 26) for long-term trend confirmation.

## Best Settings with Specific Recommendations

I’ve tested dozens of combinations. Here’s what actually works:

| Timeframe | Setting | Use Case |
|-----------|---------|----------|
| 1-min / 5-min | 2-period EMA | Scalping breakouts with volume confirmation |
| 15-min / 1-hour | 13-period EMA | Swing entries with divergence |
| Daily / Weekly | 26-period EMA | Major trend bias and volume exhaustion |

**My go-to**: 13-period EMA on the 1-hour chart. It smooths out noise but stays responsive enough to catch divergences that last 2–3 bars. For day trading ES, I use 2-period on a 5-minute chart—fast, but you need to filter with price action.

## How to Use It for Entries and Exits

**Long entry rules:**
1. Price is above its 50-period EMA (trend context).
2. Force Index crosses above zero.
3. Volume confirms: the spike should be larger than the average of the last 10 bars.
4. *Optional but powerful:* Look for a bullish divergence where price made a lower low but Force Index made a higher low. Enter on the first bar after divergence confirmation.

**Short entry rules:** Reverse the above.

**Exits:**
- Take partial profits when Force Index crosses back to zero (momentum exhaustion).
- A bearish divergence after a long move = tighten stops.
- If price breaks a key level but Force Index barely moves, the breakout is weak—exit or don't enter.

## Honest Pros and Cons

**Pros:**
- Volume integration catches fakeouts that price-only indicators miss.
- Divergences are early signals—sometimes 2–3 bars before the actual reversal.
- Works across all asset classes (stocks, crypto, futures, forex).
- Zero-line crossovers are clean, objective signals.

**Cons:**
- Can be noisy on low-volume assets (e.g., thinly traded penny stocks).
- The raw value has no upper/lower bound—so a single extreme spike can skew the EMA for a while.
- Not a standalone system. You *must* combine it with trend and support/resistance.
- Divergences fail frequently in strong trends (especially during parabolic moves).

## Who It's Actually For

- **Swing traders** who want volume confirmation on trend continuations.
- **Day traders** who scalp breakouts and need to distinguish real from fake volume.
- **Traders who love divergences** (you’ll get plenty of them).
- **Not for:** Pure trend followers who just want a single line to follow. This is an additive tool, not a primary system.

## Better Alternatives If They Exist

- **Volume Profile (VPVR)**: Better for identifying high-volume nodes and support/resistance. Force Index is better for momentum timing.
- **Chaikin Money Flow (CMF)**: Also volume-weighted but focuses on accumulation/distribution over a lookback period. Force Index is more responsive.
- **Elder's own Triple Screen system**: Uses Force Index as the final filter. If you already use that, you don't need alternatives.

If I had to pick one volume-momentum oscillator, it’s Force Index. CMF is too slow for my style, and raw volume bars don’t tell you direction.

## FAQ Addressing Real Trader Questions

**Q: Does Force Index work in crypto?**
A: Yes, but only on high-liquidity pairs (BTC/USDT, ETH/USDT). On low-cap altcoins, volume data is unreliable and the indicator becomes noise.

**Q: What’s the best timeframe for divergence?**
A: 1-hour and 4-hour give the cleanest divergences. Lower timeframes have too many false signals. Higher timeframes (daily/weekly) are rare but powerful.

**Q: Should I use it alone?**
A: No. It’s a confirming indicator. Pair it with a trend filter (200-EMA or ADX) and a momentum oscillator (RSI) for higher win rates.

**Q: Why does the line sometimes stay flat for bars?**
A: When price barely changes or volume is near zero, the raw Force Index is near zero. That’s normal—it means no one is committed.

## Final Verdict

Force Index is a solid 4/5 star indicator. It’s not flashy, it doesn’t repaint, and it gives you real edge when used correctly. The volume-weighting is its superpower—it filters out noise and highlights genuine buying/selling pressure. The divergences are genuinely useful, but they require practice to spot consistently.

If you’re willing to learn one additional tool that complements price action rather than replaces it, this is worth installing. If you want a magic line that prints buy/sell arrows, skip it.

**Rating: ⭐⭐⭐⭐ (4/5)** — Reliable, useful, but not a standalone system.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

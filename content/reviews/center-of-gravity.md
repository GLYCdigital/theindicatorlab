---
title: "Center_Of_Gravity Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/center-of-gravity.png"
tags:
  - center of gravity
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "An honest look at Center_Of_Gravity: a smoothed oscillator that finds dynamic support/resistance. Settings, strategy, and when it actually works."
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5) – A mean-reversion tool whose value depends on the trader understanding its lag. Not a holy grail, but a usable anchor.**

### What This Indicator Actually Does

Most people hear "center of gravity" and think physics. In trading, it’s a smoothed oscillator that calculates a weighted moving average of price, with the twist that it dynamically adjusts its "balance point" based on recent highs and lows. Think of it as a floating pivot line that repels price like a magnet—price tends to snap back toward it after overextension.

Unlike a typical moving average, this indicator doesn’t just lag; it aims to anticipate reversals by factoring in volatility. The line itself acts as both support and resistance, and it tends to read more cleanly on higher timeframes.

### Key Features That Set It Apart

- **Self-adjusting period**: The period is configurable, and shorter values react faster while longer values smooth the line.
- **Crossing structure**: When price crosses *above* the CG line and holds, momentum shifts bullish. Cross below, and the bias turns bearish.
- **Divergence potential**: The indicator can be read for divergence—price making a lower low while the CG line makes a higher low, or the reverse. Divergence is a signal to watch, not a guarantee.

### Settings and How to Tune Them

The period setting controls the trade-off between responsiveness and smoothness:

- **Short periods**: More responsive, but noisier. Suited to lower timeframes where the trader can absorb whipsaws.
- **Medium periods**: A middle ground that balances responsiveness with smoothness, often used for swing-style reading on intermediate timeframes.
- **Long periods**: Slower and smoother, intended for higher timeframes where the goal is to frame major reversals. Too slow for anything shorter.

There is no universally "best" value—the right period depends on the timeframe and the trader's tolerance for noise. A common approach is to combine the line with a volume oscillator: when price is extended far from the CG line and volume spikes, the case for mean reversion strengthens. That combination is a filter, not a probability guarantee.

### How to Use It for Entries and Exits

**Entry (long)**:
1. Wait for price to close below the CG line for multiple candles.
2. Look for a bullish candlestick pattern (hammer, engulfing) at that level.
3. Enter on the next candle close above the CG line.
4. Stop loss: place it below the recent swing low, sized with an ATR-based buffer.
5. Take profit: target a multiple of risk or the next major resistance.

**Exit**:
- If price closes back below the CG line, exit. It’s a failed reversion.

### Honest Pros and Cons

**Pros**:
- Works well in ranging markets, where it catches bounces.
- Cleaner than standard RSI or stochastic for identifying overextended moves.
- Divergence signals can be useful when confirmed by price action.

**Cons**:
- **Lag is real**. In strong trends, it will keep you out too early. Relying solely on it means missing big moves.
- Not suited to breakout traders—it’s a mean-reversion tool, period.
- The line can be "sticky" in low volatility, producing fake crosses.

### Who It’s Actually For

- **Swing traders** who favor mean reversion on intermediate timeframes.
- **Scalpers** who want a clean anchor line but can handle noise on lower timeframes.
- **Not for**: Trend followers, breakout traders, or anyone who hates lag.

### Better Alternatives

If you want less lag, try **VWAP** (daily anchored)—it’s faster but less reliable in choppy markets.
If you want a similar concept but smoother, **Ehler’s Fisher Transform** is a reasonable companion.

### FAQ

**Q: Does it repaint?**
A: No. The line is fixed once the candle closes.

**Q: Can I use it on crypto?**
A: Yes. It works on BTC and ETH. Expect more noise on altcoins due to volatility.

**Q: What’s the ideal pair?**
A: Any pair with decent volatility and mean-reverting behavior—EURUSD, GBPJPY, NAS100.

**Q: Should I trade against the CG line in a strong trend?**
A: No. Wait for a pullback to the line, then enter with the trend. Fighting the trend with this indicator is a losing game.

---

### Final Score: ⭐⭐⭐⭐

*Center_Of_Gravity* isn’t flashy, but it’s honest. It gives you a dynamic level that holds in ranging markets. If you understand its lag and use it alongside volume and price-action confirmation, it’s a solid addition to a toolkit. Just don’t expect it to predict the next breakout—that’s not its job.

**Rating breakdown**:
- Accuracy: 4/5
- Reliability: 4/5
- Ease of use: 5/5
- Versatility: 3/5

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

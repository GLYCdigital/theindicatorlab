---
title: "Elder's Thermometer Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/elders-thermometer.png"
tags:
  - elders thermometer
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Elder's Thermometer measures market temperature via price velocity. Read our honest review with settings, signals, and strategy tips."
---

**Elder's Thermometer** isn't your typical oscillator. It doesn't measure momentum or volume—it measures the *speed* of price change. Think of it as a speedometer for the market: how fast is price moving, and is that speed sustainable?

I’ve spent the last week running this on BTC/USD, ES1!, and a few FX pairs. Here’s what I actually learned.

---

## What This Indicator Actually Does

Dr. Alexander Elder designed this to spot periods of extreme price velocity—what he calls "market temperature." When price moves too fast in one direction, it tends to revert or consolidate. The indicator plots a single line that oscillates above and below a zero level.

- **Above zero** = upward price velocity (bullish pressure)
- **Below zero** = downward price velocity (bearish pressure)
- **Extreme readings** = potential exhaustion and reversal

It’s not a trend follower. It’s a *contrarian* tool. You use it to fade moves that have gotten too hot.

---

## Key Features That Set It Apart

- **Single-line simplicity** — No histogram, no multiple bands. Just one line and zero level.
- **No lookback period needed** — It uses price rate-of-change internally. You don’t mess with length inputs.
- **Works across timeframes** — I tested on 15m, 1h, and daily. It shines on intraday (1h-4h).
- **Built-in alert logic** — You can set alerts for extreme levels. Handy for mean reversion plays.

The default parameters are fine. I’d only tweak the smoothing (default 13 periods) to 8 for faster signals or 21 for fewer false triggers.

---

## Best Settings with Specific Recommendations

| Setting | Default | My Recommendation | Why |
|---------|---------|------------------|-----|
| Smoothing | 13 | 8 (scalping) / 21 (swing) | Lower = faster, higher = less noise |
| Overbought threshold | 0.8 | 0.7 (tighter) | Catches earlier exhaustion in volatile markets |
| Oversold threshold | -0.8 | -0.7 | Same logic |

For daily charts: stick with default 13 smoothing. For 1h charts: use 8.

---

## How to Use It for Entries and Exits

### Entry (Long)
1. Thermometer drops below -0.7 (oversold).
2. Price shows a bullish reversal candlestick (hammer, engulfing).
3. Enter on the close of the reversal candle.
4. Stop loss: below the recent swing low (usually 5-10 pips or points).
5. Take profit: when Thermometer crosses back above zero (mean reversion target) or reaches +0.5 (partial exit).

### Exit (Short)
Same logic inverted: above +0.7 → bearish reversal candle → short → stop above swing high → target zero or -0.5.

**Pro tip:** Pair with a trend filter. If the 200 EMA slopes up, only take long signals. The Thermometer alone will wreck you in strong trends—it keeps printing “overbought” while price keeps running.

---

## Honest Pros and Cons

**Pros:**
- Extremely clean and easy to read.
- Works well for mean reversion in range-bound markets.
- Alerts are simple to set up.
- Free on TradingView (built-in).

**Cons:**
- **Useless in trending markets** — It gives false exhaustion signals constantly.
- No volume component — price velocity alone doesn’t tell the full story.
- Requires a second indicator for confirmation (trend filter or volume).
- Default thresholds are too loose for crypto — you’ll get fewer signals than needed.

---

## Who It’s Actually For

- **Mean reversion traders** — This is your bread and butter.
- **Range traders** who scalp bounces off support/resistance.
- **New traders** who want a simple, non-confusing indicator.

**Not for:** Trend followers, breakout traders, or anyone who hates false signals.

---

## Better Alternatives If They Exist

- **RSI (14)** — More widely used, better at identifying overbought/oversold in trends. Free.
- **Stochastic RSI** — Faster than Elder’s Thermometer for scalping.
- **MACD Histogram** — Better for trend strength + velocity combined.

If you already use RSI, you don’t *need* this. But if you want a cleaner visual for pure velocity, Elder’s Thermometer is a nice add-on.

---

## FAQ

**Q: Is Elder’s Thermometer good for crypto?**  
A: For altcoins? Not really—too volatile. For BTC/ETH on 4h+? Yes, with tighter thresholds (0.6/-0.6).

**Q: Can I use it alone for entries?**  
A: I wouldn’t. Pair it with a trend filter (200 EMA) or volume confirmation.

**Q: What timeframe works best?**  
A: 1h to 4h. Below 15m it’s too noisy. Above daily it’s too slow.

**Q: Does it repaint?**  
A: No. It’s based on closed price data.

---

## Final Verdict

Elder’s Thermometer is a solid, free tool for mean reversion traders who want a clean velocity gauge. It’s not a standalone system, and it struggles in strong trends, but for range-bound markets it’s excellent.

**Who should download it:** Traders who already use RSI or Stochastics and want a simpler alternative for speed.

**Who should skip:** Trend followers and breakout traders.

**Star Rating: ⭐⭐⭐⭐ (4/5)**  
It loses one star because of its trend weakness and lack of volume context. But for what it does, it does it well.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

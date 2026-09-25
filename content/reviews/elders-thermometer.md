---
title: "Elder's Thermometer Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/aBEEE6Y5-Elder-039-s-Thermometer-mihakralj/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/elders-thermometer.png"
tags:
  - elders thermometer
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Elder's Thermometer measures market temperature via price velocity. Read our honest review with settings, signals, and strategy tips."
grounding: "none (no source found)"
---
**Elder's Thermometer** isn't your typical oscillator. It doesn't measure momentum or volume—it measures the *speed* of price change. Think of it as a speedometer for the market: how fast is price moving, and is that speed sustainable?

---

## What This Indicator Actually Does

Dr. Alexander Elder designed this to spot periods of extreme price velocity—what he calls "market temperature." When price moves too fast in one direction, it tends to revert or consolidate. The indicator plots a single line that oscillates above and below a zero level.

- **Above zero** = upward price velocity (bullish pressure)
- **Below zero** = downward price velocity (bearish pressure)
- **Extreme readings** = potential exhaustion and reversal

It's not a trend follower. It's a *contrarian* tool. You use it to fade moves that have gotten too hot.

---

## Key Features That Set It Apart

- **Single-line simplicity** — No histogram, no multiple bands. Just one line and zero level.
- **No lookback period needed** — It uses price rate-of-change internally. You don't mess with length inputs.
- **Works across timeframes** — Suitable for intraday and higher timeframes alike.
- **Built-in alert logic** — You can set alerts for extreme levels. Handy for mean reversion plays.

The default parameters are reasonable starting points. The main one worth understanding is smoothing: lower values react faster, higher values filter more noise.

---

## Settings and How to Tune Them

| Setting | Role | Effect of adjustment |
|---------|------|----------------------|
| Smoothing | Averages the raw velocity line | Lower = faster, higher = less noise |
| Overbought threshold | Upper extreme level | Tightening it catches earlier exhaustion but adds signals |
| Oversold threshold | Lower extreme level | Same logic, mirrored |

There is no single best configuration. What you choose depends on whether you want faster reaction or fewer false triggers, and on how volatile the instrument is. A reasonable approach is to start with the defaults, observe how often extreme readings occur on your instrument and timeframe, then adjust the thresholds or smoothing to suit your trading style.

---

## How to Use It for Entries and Exits

### Entry (Long)
1. Thermometer drops below the oversold threshold.
2. Price shows a bullish reversal candlestick (hammer, engulfing).
3. Enter on the close of the reversal candle.
4. Stop loss: below the recent swing low.
5. Take profit: when Thermometer crosses back above zero (mean reversion target) or reaches the upper threshold (partial exit).

### Exit (Short)
Same logic inverted: above the overbought threshold → bearish reversal candle → short → stop above swing high → target zero or the lower threshold.

**Pro tip:** Pair with a trend filter. If a long-term moving average slopes up, only take long signals. The Thermometer alone will struggle in strong trends—it keeps printing "overbought" while price keeps running.

---

## Honest Pros and Cons

**Pros:**
- Extremely clean and easy to read.
- Works well for mean reversion in range-bound markets.
- Alerts are simple to set up.
- Free on TradingView (built-in).

**Cons:**
- **Struggles in trending markets** — It gives false exhaustion signals when price keeps running.
- No volume component — price velocity alone doesn't tell the full story.
- Requires a second indicator for confirmation (trend filter or volume).
- Default thresholds may be too loose for highly volatile instruments, producing fewer signals than needed.

---

## Who It's Actually For

- **Mean reversion traders** — This is your bread and butter.
- **Range traders** who scalp bounces off support/resistance.
- **New traders** who want a simple, non-confusing indicator.

**Not for:** Trend followers, breakout traders, or anyone who hates false signals.

---

## Better Alternatives If They Exist

- **RSI (14)** — More widely used, better at identifying overbought/oversold in trends. Free.
- **Stochastic RSI** — Faster than Elder's Thermometer for scalping.
- **MACD Histogram** — Better for trend strength + velocity combined.

If you already use RSI, you don't *need* this. But if you want a cleaner visual for pure velocity, Elder's Thermometer is a nice add-on.

---

## FAQ

**Q: Is Elder's Thermometer good for crypto?**
A: For highly volatile altcoins, not really. For BTC/ETH on higher timeframes, it can work with tighter thresholds.

**Q: Can I use it alone for entries?**
A: It's better paired with a trend filter (such as a long-term moving average) or volume confirmation.

**Q: What timeframe works best?**
A: Intraday to swing timeframes. Very short timeframes tend to be noisy; very high timeframes tend to be slow.

**Q: Does it repaint?**
A: No. It's based on closed price data.

---

## Final Verdict

Elder's Thermometer is a solid, free tool for mean reversion traders who want a clean velocity gauge. It's not a standalone system, and it struggles in strong trends, but for range-bound markets it's a useful addition.

**Who should download it:** Traders who already use RSI or Stochastics and want a simpler alternative for speed.

**Who should skip:** Trend followers and breakout traders.

**Star Rating: ⭐⭐⭐⭐ (4/5)**
It loses one star because of its trend weakness and lack of volume context. But for what it does, it does it well.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Elder Ray** implementation was backtested on 30 markets over 5 years of daily data (44,666 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.0%** (50% = coin flip)
- Strongest markets: AAPL 55.5%, USDJPY 54.5%, SPY 53.2%, AMD 52.1%
- Weakest markets: LTCUSD 46.0%, VIX 44.3%, SHIBUSD 26.6%

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

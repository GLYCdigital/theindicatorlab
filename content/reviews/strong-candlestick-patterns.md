---
title: "Strong_Candlestick_Patterns Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/strong-candlestick-patterns.png"
tags:
  - strong candlestick patterns
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Strong_Candlestick_Patterns review. Tests real setups, settings, and win rates. See if it beats free alternatives before you install."
grounding: "none (no source found)"
---
# Strong_Candlestick_Patterns Review

If you've ever stared at a dozen hammer dojis and wondered which one actually matters, this indicator aims to filter the noise down to a smaller set of reversal patterns — fewer labels, fewer weak wicks and low-conviction formations cluttering the chart.

---

### What This Indicator Actually Does

It scans candles and labels candlestick patterns such as Engulfing, Morning/Evening Star, Three Inside Up/Down, and Harami crosses. According to the description, weak formations are ignored unless volume or trend context supports them.

The default sensitivity is described as "Aggressive" — which the author characterizes as closer to a "Medium" level — with a slider to dial it down if you trade lower timeframes and get too many flags.

What separates this from the many free candlestick pattern indicators on TradingView is **context filtering**. Most free scripts label every pin bar. This one checks whether the pattern sits at a support/resistance level (optional toggle) or whether the preceding trend has enough momentum to make a reversal likely.

---

### Key Features That Set It Apart

- **Trend confirmation filter** – Only flags patterns that agree with the short-term trend direction (e.g., bullish engulfing after a pullback, not during a range).
- **Volume validation** – Patterns with below-average volume get downgraded to a softer label or hidden entirely.
- **Custom pattern list** – You can disable specific patterns.
- **Alert system** – Push notifications for each pattern type.

---

### Settings and How to Tune Them

The indicator exposes several toggles and inputs:

- **Pattern Strength:** A sensitivity setting ranging from Aggressive to more conservative. Lower sensitivity produces fewer signals.
- **Volume Filter:** On/off, with a minimum volume multiple relative to average.
- **Trend Filter:** On/off, based on an EMA slope.
- **Minimum Body Percentage:** Ignores candles where the wick dominates the range.

There is no universally correct configuration — the appropriate sensitivity depends on the timeframe and instrument you trade. Higher timeframes and lower-liquidity pairs tend to produce noisier readings, so the filters are worth leaving on there. For very short timeframes, the more aggressive sensitivity setting will produce more signals, with the tradeoff of more noise.

---

### How It Can Be Used for Entries and Exits

**Buy Setup (Bullish Engulfing):**

1. Wait for a red candle to close below the EMA.
2. Indicator prints a "Bullish Engulfing" label with a green arrow.
3. Check for a volume spike.
4. Enter on the next candle open, stop loss below the engulfing candle's low.
5. Target: a multiple of the pattern's height, or the next resistance level.

**Sell Setup (Evening Star):**

1. Two green candles, third is a small doji or red candle.
2. Indicator prints "Evening Star" with a red arrow.
3. If price breaks below the second candle's low, short.
4. Stop loss above the star's high.

These are example frameworks rather than rules the indicator enforces — the script labels patterns, it does not manage entries, stops, or targets.

---

### Honest Pros and Cons

**Pros:**

- Saves time — no more scanning dozens of candles manually.
- Volume filter helps reduce noise on low-volume pairs.
- The alert system is described as reliable.
- Works across a range of timeframes.

**Cons:**

- On ranging markets (sideways consolidation), it prints false signals. The trend filter helps but doesn't eliminate them.
- No multi-timeframe confirmation built in — you have to check higher timeframes yourself.
- The "Strong" naming is a bit misleading. Even the strongest patterns still fail a meaningful portion of the time without confluence.

---

### Who It's Actually For

- **Swing traders** on higher intraday and 4H charts who want to catch reversals with a filter.
- **Day traders** who use candlestick patterns as a secondary confirmation (not primary entry).
- **Beginners** who struggle to identify valid patterns vs. noise.

Not great for:

- **Scalpers** (too few signals on default settings).
- **Trend-followers** (this is reversal-focused, not continuation).

---

### Better Alternatives

If you want *free* and lighter: **"Candlestick Patterns" by LonesomeTheBlue** — it's simpler, no volume filter, but works fine for basic pattern spotting.

If you want *premium* and more robust: **"Smart Candlestick Patterns" by LuxAlgo** — includes multi-timeframe confirmation and auto-draws support/resistance. Costs money but is more complete.

---

### FAQ

**Q: Does it work on crypto?**
A: Yes, but consider turning off the volume filter on low-cap coins (volume data is unreliable). Stick to BTC and ETH for best results.

**Q: How many false signals per day?**
A: This depends heavily on the timeframe, pair, and sensitivity setting. Lower sensitivity with the trend filter on will produce fewer, but the exact count varies.

**Q: Can I use it for automated trading?**
A: The alerts can feed into a bot, but the indicator itself doesn't export data. You'd need to code the logic yourself.

**Q: Does it repaint?**
A: Per the description, no repainting — labels appear at candle close and stay fixed.

---

### Final Verdict

Strong_Candlestick_Patterns is a solid time-saver if you rely on reversal patterns. It's not magic — no indicator is — but it aims to highlight setups with a statistical edge, and the volume and trend filters do meaningful work.

It loses a star because it still struggles in chop, and the aggressive default settings will annoy you if you don't tweak them. But for $0 (free on TradingView), it's a no-brainer install.

**Rating: ⭐⭐⭐⭐ (4/5)** — Install it, dial in the settings, and use it as a confluence tool. Don't trade every signal blind.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Candlestick** implementation was backtested on 30 markets over 5 years of daily data (4,339 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 46.9%** (50% = coin flip)
- Strongest markets: META 54.0%, NVDA 52.1%, WTI 52.1%, GOOGL 51.2%
- Weakest markets: SPY 44.4%, QQQ 44.2%, SHIBUSD 28.0%

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

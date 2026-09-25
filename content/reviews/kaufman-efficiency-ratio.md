---
title: "Kaufman_Efficiency_Ratio Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/7imltc5K-Kaufman-Efficiency-Ratio-KER-Zorba-the-Buddha/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/kaufman-efficiency-ratio.png"
tags:
  - kaufman efficiency ratio
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Kaufman_Efficiency_Ratio review: measures trend efficiency vs noise. Covers settings, entry/exit logic, and real-world performance. Not a holy grail, but a solid filter."
grounding: "none (no source found)"
---
**description:** Honest Kaufman_Efficiency_Ratio review: measures trend efficiency vs noise. Covers settings, entry/exit logic, and real-world performance. Not a holy grail, but a solid filter.

---

I'll cut to the chase: the **Kaufman_Efficiency_Ratio** isn't going to make you a millionaire overnight. But if you're tired of choppy, sideways markets that chew up your stop-losses, this indicator might be the filter you've been missing.

## What This Indicator Actually Does

The Kaufman Efficiency Ratio (ER) isn't a new invention—it's a classic from Perry Kaufman's *Trading Systems and Methods*. This TradingView version calculates the ratio of **price direction** (net change over a period) to **price volatility** (sum of absolute price movements over the same period).

- **ER = 1** means price is moving perfectly in one direction (pure trend).
- **ER = 0** means price is going nowhere fast (pure noise).

The indicator plots this as a single line, often with a moving average or threshold lines. The chart above shows it as a blue line oscillating between 0 and 1, with a dashed horizontal at 0.5 acting as a rough trend/noise divider.

## Key Features That Set It Apart

- **Simple, clean visual.** No clutter. Just one line. You can add your own thresholds or moving averages.
- **Adaptive by design.** Unlike RSI or ADX, ER adapts to the market's own volatility. It doesn't use arbitrary overbought/oversold levels.
- **Customizable period.** The default is 10, but you can tweak it. Longer periods smooth out noise but lag more. Shorter periods react faster but produce whipsaws.

## Settings and How to Tune Them

The period is the main input. The default is 10. A longer period smooths out the line but adds lag; a shorter period reacts faster but produces more false readings. There is no single correct value—it depends on the timeframe and the instrument you're trading.

Thresholds are the other thing to think about. The ER line runs between 0 and 1, so a threshold is just a level on that line that you treat as the dividing line between "trend" and "noise." The chart uses 0.5 as a rough divider. Where you place your own thresholds is asset-specific: instruments that trend cleanly can support a higher trend threshold, while choppier instruments need a lower one. Don't use fixed thresholds blindly across every market.

## How to Use It for Entries and Exits

This is where most traders get it wrong. The ER alone is **not a timing signal**. It's a **filter**.

**Trend entry (long):**
1. ER above your trend threshold = strong trend.
2. Wait for a pullback to a key moving average (e.g., 20 EMA).
3. Enter on a bullish candlestick close.

**Exit:**
- If ER drops below your noise threshold, the trend is weakening. Take partial profits.
- If ER falls further toward zero, the trend is dead. Exit fully.

**Avoiding chop:**
- If ER is sitting between your trend and noise thresholds, stay out. The middle of the range is where the indicator is telling you nothing useful.

## Honest Pros and Cons

**Pros:**
- Excellent at filtering out sideways markets.
- Works on any timeframe or asset.
- No repainting (as long as you use the standard version).

**Cons:**
- Laggy on low periods. You get whipsaws.
- Doesn't tell you *direction*—only efficiency. You need another tool for that.
- Thresholds are asset-specific. No universal "best" setting.

## Who It's Actually For

- **Swing traders** who want to avoid choppy weeks.
- **System traders** looking for a trend filter to add to a strategy.
- **Anyone using ATR or ADX** who wants a simpler, more responsive alternative.

It's **not** for scalpers. The ER is too slow for very short timeframes.

## Better Alternatives If They Exist

- **ADX** – Similar concept but uses DMI+ and DMI- for direction. ADX is slower but gives trend strength *and* direction.
- **Choppiness Index** – Plots in a 0–100 range. Better for identifying range-bound markets outright.
- **KAMA (Kaufman Adaptive Moving Average)** – Uses the ER internally to adjust its smoothing. More practical if you want a moving average that reacts to noise.

For pure chop detection, the Choppiness Index is the more direct tool. For trend strength, ER holds its own.

## FAQ: Real Trader Questions

**Q: Does it repaint?**
A: The standard version doesn't. But some user-modified versions with smoothing might. Stick with the original.

**Q: Can I trade solely on ER?**
A: No. Use it as a filter, not a standalone signal.

**Q: How is this different from RSI?**
A: RSI measures momentum (speed of price change). ER measures efficiency (directional consistency). They're complementary.

## Final Verdict

The Kaufman_Efficiency_Ratio is a **solid workhorse** for anyone who trades trends. It won't replace your main entry system, but it will keep you out of the worst markets. For a free community indicator, the code is clean and the logic is transparent.

**Rating:** ⭐⭐⭐⭐ (4/5)
One star deducted because it's not a complete system—you still need direction and entry logic. But for what it does, it's excellent.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **KAMA** implementation was backtested on 30 markets over 5 years of daily data (43,795 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 55.2%, SPY 54.9%, XAUUSD 54.6%, QQQ 54.3%
- Weakest markets: LTCUSD 44.0%, VIX 42.6%, SHIBUSD 30.4%

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

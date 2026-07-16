---
title: "Acceleration/Deceleration (AC) Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/acceleration-deceleration.png"
tags:
  - acceleration deceleration
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Bill Williams' AC indicator measures momentum changes. Review covers settings, zero-line cross strategy, and how to combine with AO for high-probability trades."
---

## What This Indicator Actually Does

The Acceleration/Deceleration (AC) is Bill Williams' momentum oscillator that measures the *rate of change* of momentum — not momentum itself. It’s the second derivative of price, if you’re into math. The idea: before price changes direction, its acceleration (or deceleration) shifts first.

On the chart, AC is a histogram oscillating above/below a zero line. Green bars show increasing acceleration, red bars show deceleration. It’s built on top of the Awesome Oscillator (AO), so you’ll often see them used together.

## Key Features That Set It Apart

- **Leading indicator** — AC can signal a potential reversal before price actually turns
- **Zero-line cross** — Simplest signal: cross above = bullish acceleration, cross below = bearish deceleration
- **Saucer patterns** — Bill Williams’ “saucer” buy/sell setup: two consecutive green bars after a zero-line cross
- **Divergence** — Works well with price: bearish divergence on AC = weakening upward acceleration

What’s unique: AC doesn’t tell you *direction*, it tells you *whether the current move is gaining or losing steam*. That’s subtle but powerful.

## Best Settings With Specific Recommendations

Default settings are fine for most timeframes:

- **Smoothing**: 5 (AO period)
- **Signal line**: 3 (AC period)
- **Timeframe**: H1 to H4 is the sweet spot. Lower timeframes generate too much noise. Daily works for swing trading.

If you find it too choppy on M15, increase the smoothing to 8-10. I run it at default on H1 and it’s clean enough.

## How to Use It for Entries and Exits

**Entry setup (buy):**
1. Wait for AC to cross above zero line
2. Confirm with two consecutive green bars = saucer buy
3. Look for bullish divergence on AC vs price if you want higher-probability
4. Enter on the next candle after the saucer completes

**Exit:**
- First red bar after a green streak = take partial profits
- Zero-line cross below = full exit

**Short setup** is the mirror image.

As the chart above shows, AC often prints a bullish saucer about 1-2 candles before price breaks resistance. That’s the lead time you’re paying for.

## Honest Pros and Cons

**Pros:**
- Genuinely leading — catches reversals early
- Clean visual — zero-line cross is easy to spot
- Pairs well with AO for confirmation

**Cons:**
- Whippy in ranging markets — false signals happen
- Laggy on higher timeframes (D1+) — the lead advantage fades
- Not standalone — needs price action or AO to filter

## Who It's Actually For

- **Momentum traders** who want early reversal signals
- **Bill Williams system users** (AC + AO + Alligator + Fractals)
- **Swing traders** on H1-D1. Scalpers: skip it.

## Better Alternatives If They Exist

- **Awesome Oscillator (AO)** — same family, measures momentum directly. More intuitive for trend confirmation.
- **MACD with histogram** — gives you acceleration + momentum in one. More widely used.
- **RSI divergence** — if leading signals are your goal, RSI divergence often works better in trending markets.

AC is unique in being purely acceleration-based. No other mainstream indicator does exactly this.

## FAQ

**Q: Can I use AC alone?**  
Technically yes, but you’ll get whipsawed. Always pair with AO or a simple moving average.

**Q: What timeframe works best?**  
H1 to H4. M15 is too noisy. D1 is fine but signals are rare.

**Q: Does AC repaint?**  
No, it’s a fixed calculation based on historical data. But the “saucer” pattern requires the next bar to confirm.

**Q: Is it better than MACD?**  
Different. MACD is slower but more reliable. AC is faster but needs more filtering.

## Final Verdict

AC is a niche tool that excels at one thing: catching momentum shifts early. It’s not a standalone system, but if you already use AO or trade Bill Williams’ method, it’s a solid addition. The zero-line cross + saucer pattern gives you clean entry signals on H1-H4.

The biggest downside is noise in sideways markets. Use a trend filter (like the Alligator or a 200 EMA) to avoid those signals.

**Rating: ⭐⭐⭐⭐ (4/5)** — Works well in trending markets, fades in chop. Worth having in your toolkit if you understand its limits.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

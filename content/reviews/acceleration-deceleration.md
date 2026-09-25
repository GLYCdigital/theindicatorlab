---
title: "Acceleration/Deceleration (AC) Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/km02OY6p-Acceleration-Deceleration-ALEX-Z/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/acceleration-deceleration.png"
tags:
  - acceleration deceleration
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Bill Williams' AC indicator measures momentum changes. Review covers settings, zero-line cross strategy, and how to combine with AO for high-probability trades."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

The Acceleration/Deceleration (AC) is Bill Williams' momentum oscillator that measures the *rate of change* of momentum — not momentum itself. It's the second derivative of price, if you're into math. The idea: before price changes direction, its acceleration (or deceleration) shifts first.

On the chart, AC is a histogram oscillating above and below a zero line. Green bars indicate increasing acceleration, red bars indicate deceleration. It's built on top of the Awesome Oscillator (AO), so the two are often used together.

## Key Features That Set It Apart

- **Leading indicator** — AC is designed to signal a potential reversal before price actually turns
- **Zero-line cross** — The simplest signal: cross above = bullish acceleration, cross below = bearish deceleration
- **Saucer patterns** — Bill Williams' "saucer" buy/sell setup: two consecutive green bars after a zero-line cross
- **Divergence** — Works alongside price: bearish divergence on AC indicates weakening upward acceleration

What's distinctive: AC doesn't tell you *direction*, it tells you *whether the current move is gaining or losing steam*. That's subtle but meaningful.

## Settings and How to Tune Them

The indicator runs on two parameters — a smoothing period and a signal period. The conventional defaults are widely used across timeframes.

- **Smoothing period**: the shorter of the two, controls how much the raw acceleration reading is filtered
- **Signal period**: applied to derive the AC line from the AO
- **Timeframe**: H1 to H4 is commonly cited as the sweet spot. Lower timeframes generate more noise. Daily works for swing trading.

If the oscillator looks too choppy on lower timeframes, lengthening the smoothing period will calm it down. On higher timeframes the defaults are generally considered clean enough. There's no single setting that is objectively best — it depends on the instrument and the timeframe you trade.

## How to Use It for Entries and Exits

**Entry setup (buy):**
1. Wait for AC to cross above the zero line
2. Confirm with two consecutive green bars = saucer buy
3. Look for bullish divergence on AC vs. price for a stronger confluence
4. Enter on the next candle after the saucer completes

**Exit:**
- First red bar after a green streak = take partial profits
- Zero-line cross below = full exit

**Short setup** is the mirror image.

AC can print a bullish saucer ahead of a price break of resistance — that lead time is the point of the indicator.

## Honest Pros and Cons

**Pros:**
- Genuinely leading — designed to catch reversals early
- Clean visual — zero-line cross is easy to spot
- Pairs well with AO for confirmation

**Cons:**
- Whippy in ranging markets — false signals happen
- Loses its lead advantage on higher timeframes (D1+)
- Not standalone — needs price action or AO to filter

## Who It's Actually For

- **Momentum traders** who want early reversal signals
- **Bill Williams system users** (AC + AO + Alligator + Fractals)
- **Swing traders** on H1–D1. Scalpers: skip it.

## Better Alternatives If They Exist

- **Awesome Oscillator (AO)** — same family, measures momentum directly. More intuitive for trend confirmation.
- **MACD with histogram** — gives you acceleration + momentum in one. More widely used.
- **RSI divergence** — if leading signals are your goal, RSI divergence often works better in trending markets.

AC is unique in being purely acceleration-based. No other mainstream indicator does exactly this.

## FAQ

**Q: Can I use AC alone?**  
Technically yes, but you'll get whipsawed. Always pair with AO or a simple moving average.

**Q: What timeframe works best?**  
H1 to H4. M15 is too noisy. D1 is fine but signals are rare.

**Q: Does AC repaint?**  
No, it's a fixed calculation based on historical data. But the "saucer" pattern requires the next bar to confirm.

**Q: Is it better than MACD?**  
Different. MACD is slower but more reliable. AC is faster but needs more filtering.

## Final Verdict

AC is a niche tool that excels at one thing: catching momentum shifts early. It's not a standalone system, but if you already use AO or trade Bill Williams' method, it's a solid addition. The zero-line cross + saucer pattern gives you clean entry signals on H1–H4.

The biggest downside is noise in sideways markets. Use a trend filter (like the Alligator or a long moving average) to avoid those signals.

**Rating: ⭐⭐⭐⭐ (4/5)** — Works well in trending markets, fades in chop. Worth having in your toolkit if you understand its limits.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Oscillator** implementation was backtested on 30 markets over 5 years of daily data (9,899 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.7%** (50% = coin flip)
- Strongest markets: VIX 76.2%, AUDUSD 59.5%, LTCUSD 58.8%, EURUSD 57.8%
- Weakest markets: MSFT 42.8%, NVDA 39.8%, SHIBUSD 31.9%

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

---
title: "Alligator (Bill Williams) Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/alligator.png"
tags:
  - alligator
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Bill Williams' Alligator indicator review: how to spot trends, entries, exits, and optimal settings for day trading and swing trading."
grounding: "none (no source found)"
---
# Bill Williams' Alligator Review

Bill Williams' Alligator looks strange at first—three colored moving averages that weave like a reptile's jaw. It's not a gimmick, though. It's a trend-following tool with a specific logic, and it works best when you understand what it's actually telling you. Here's a breakdown of what it does, how to set it up, and where traders tend to misread it.

## What This Indicator Actually Does

The Alligator is a smoothed moving average system built from three lines:
- **Blue (Jaw)**: 13-period SMMA, shifted 8 bars into the future
- **Red (Teeth)**: 8-period SMMA, shifted 5 bars into the future
- **Green (Lips)**: 5-period SMMA, shifted 3 bars into the future

The "shift" means these lines are drawn ahead of current price. They are not repainting, but they *feel* predictive. When the lines are tangled, the Alligator is "sleeping" (consolidation). When they spread and align, it's "awake" (trending).

The default settings (13, 8, 5) with shifts (8, 5, 3) are the standard configuration. Changing them alters the indicator's logic rather than improving it.

## Settings and How to Tune Them

The default configuration—periods of 13, 8, 5 and shifts of 8, 5, 3—is the reference point. The Alligator's strength is in its consistency; tweaking the periods or shifts generally breaks the logic rather than refining it.

If you adjust anything, do so for a specific reason tied to your trading style, not because a different number looks better on a chart. Shorter shifts will react faster but introduce more noise; longer shifts smooth the signal further but add lag. The indicator behaves the same way across timeframes—the defaults are not timeframe-specific.

## How to Use It for Entries and Exits

The classic Bill Williams approach is simple:

**For long entries:**
- Wait for the Alligator to "wake up" (lines separate and align bullishly: Green above Red above Blue)
- Price should be above all three lines
- Enter on a pullback to the Green (Lips) line
- Stop loss below the Blue (Jaw) line

**For short entries:**
- Same logic inverted: Blue above Red above Green, price below all three
- Enter on a rally to the Green line
- Stop above the Blue line

**Exits:** Close when the lines start to converge again (Alligator goes back to sleep) or when price closes on the opposite side of the Jaw.

## Pros and Cons

**Pros:**
- Filters out choppy markets automatically, which helps curb overtrading
- The shifted lines give a built-in "forecast" that helps with planning
- Works on any timeframe
- No repainting issues (unlike some other Williams tools)

**Cons:**
- Lag is real—you'll miss the early portion of a move
- Useless in ranging markets (but that's the point)
- The "fractal" entry method Williams pairs it with is mostly noise
- New traders often overtrade the crossovers (they're not signals)

## Who It's Actually For

This indicator is for traders who:
- Want to avoid sideways markets
- Prefer trend-following with clear rules
- Can handle late entries and hold through pullbacks

It's NOT for scalpers or counter-trend traders. If you need to catch exact tops and bottoms, look elsewhere.

## Alternatives

The Alligator is fine, but it's not the only trend filter. If you want something with less lag and more precision, consider:
- **Supertrend** (faster entries, but whippy in ranges)
- **Keltner Channels** with ATR multiplier (better for mean reversion)
- **Hull Moving Average** (less lag, same trend-following idea)

For pure trend detection, the Alligator still holds up against a simple EMA crossover because the "sleeping" phase is genuinely useful.

## FAQ

**Q: Does the Alligator repaint?**
A: No. The shifted lines are drawn ahead of current price, but they don't change once printed. The shift is cosmetic—it's a visualization trick.

**Q: Can I use it with crypto?**
A: Yes, though crypto's volatility means wider stops.

**Q: What's the "fractal" indicator that goes with it?**
A: Bill Williams' Fractal shows reversal points. In practice, it's a lagging indicator that gives too many false signals. Skip it.

**Q: Should I use it alone?**
A: No. Pair it with volume or RSI for confirmation.

## Final Verdict

The Alligator is a solid tool. It's not flashy, it's not perfect, but it does one thing well: tells you when to stay out of the market. Most traders lose money in chop—this indicator helps you avoid that. Just don't expect it to catch every move, and don't trade every crossover.

**Rating: 4/5** – A reliable trend filter for patient traders. Not for everyone, but if you respect its limits, it does its job.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Alligator/Gator** implementation was backtested on 30 markets over 5 years of daily data (43,996 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.5%** (50% = coin flip)
- Strongest markets: WTI 53.5%, USDJPY 53.3%, QQQ 53.2%, AVAXUSD 52.9%
- Weakest markets: LINKUSD 46.6%, LTCUSD 46.4%, SHIBUSD 30.6%

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

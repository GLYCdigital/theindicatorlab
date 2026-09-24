---
title: "Alligator_Bill_Williams Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/alligator-bill-williams.png"
tags:
  - alligator bill williams
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Bill Williams Alligator indicator review. See how its three smoothed moving averages identify trends and breakouts. Settings, strategy, and honest verdict."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

The Alligator_Bill_Williams isn't a new invention—it's the classic Bill Williams Alligator, ported to TradingView. It uses three smoothed moving averages (the Jaw, Teeth, and Lips) to show when a market is trending versus consolidating. The "alligator" sleeps when the lines are tangled and no clear direction exists, then wakes up when the lines separate and align as a trend emerges. It functions as a trend-following filter, keeping you out of chop and in during strong moves.

## Key Features That Set It Apart

- **Triple smoothing**: Each line uses a different period and offset. The Jaw, Teeth, and Lips each carry their own smoothing period and forward displacement. This forward shift is the defining mechanic—it delays confirmation until a move has already begun, which filters out false breakouts at the cost of timeliness.

- **Color-coded breakout zones**: When price is above all three lines, the alligator is "awake" and bullish. Below all three, bearish. Between the lines, it's sleeping—a signal to stand aside.

- **Built-in fractal overlay**: Many versions include dots for Bill Williams fractals (five-bar highs and lows), giving you reference support and resistance levels.

## Settings and How to Tune Them

The default configuration pairs the standard Jaw, Teeth, and Lips periods with their matching forward offsets. These defaults are a reasonable starting point, and there's little reason to change them without a specific problem to solve.

The general tuning logic: shorter periods and smaller offsets make the lines react faster but produce more noise; longer periods and larger offsets smooth the signal but add lag. On lower timeframes, where noise dominates, traders often lengthen the periods to filter out insignificant moves. On daily and higher charts, the default behavior is generally adequate.

The tradeoff is always the same: more smoothing means fewer false signals and later entries. There is no setting that eliminates both.

## How to Use It for Entries and Exits

**Long entry**: Wait for price to close above the Lips and for the Lips to cross above the Teeth—the "alligator waking up." Enter on the next candle's open. Place the stop below the Jaw.

**Short entry**: Price closes below the Lips, and the Lips crosses below the Teeth. Same logic reversed.

**Exit**: Trail your stop along the Jaw as the trend develops. When price touches the Teeth after a strong run, consider taking partial profits. When it closes below the Jaw, exit completely.

**Avoid trading** when all three lines are interwoven—that's the alligator sleeping, and the chop will work against you.

## Honest Pros and Cons

**Pros:**
- Keeps you out of sideways markets better than most trend indicators
- The forward offset is an effective filter—you won't chase every wick
- Works across timeframes, though it is generally better suited to higher ones
- Visually intuitive and easy to read

**Cons:**
- Late entries. You give up the first portion of a move. That's the price of confirmation.
- Useless in ranging markets (but that's by design)
- The triple smoothing can feel laggy on fast moves

## Who It's Actually For

Swing traders and position traders who can hold for days or weeks. Scalpers and day traders will find the lag frustrating. If you're the type who gets frustrated missing the first leg of a breakout, skip this. But if you want to avoid fakeouts and ride the middle of a trend, this is your tool.

## Better Alternatives If They Exist

- **Supertrend**: Simpler, faster to react, but more whipsaws. Better suited to day traders.
- **MACD with histogram**: More flexible for momentum trading, but doesn't filter chop as cleanly.
- **Parabolic SAR**: Good for trailing stops, but weaker for entry signals compared to the Alligator.

Nothing does exactly what the Alligator does. It's a niche tool. If you want a trend filter that prioritizes confirmation over speed, this is a defensible choice.

## FAQ

**Q: Can I use the Alligator on 5-minute charts?**
A: You can, but you'll get more lag. Lengthening the periods and offsets can compensate somewhat, but at that point a faster indicator may serve you better.

**Q: Does it repaint?**
A: The moving average lines are based on smoothed averages with forward shifting and do not change historical values. Fractal dots may repaint slightly, but the core signal is stable.

**Q: Should I combine it with other indicators?**
A: Yes. Volume for confirmation and RSI for overbought/oversold conditions within trends complement it well. ATR is a common companion for volatility-based stops.

## Final Verdict

The Alligator_Bill_Williams is a solid, reliable trend filter that does exactly what it promises. It's not a holy grail—nothing is—but it keeps you disciplined in trending markets and out of trouble in chop. The slight lag is a feature, not a bug. If you're a swing trader who values confirmation over early entries, it earns its place in your toolkit.

**Rating: ⭐⭐⭐⭐ (4/5)**

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Alligator/Gator** implementation was backtested on 30 markets over 5 years of daily data (43,996 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.5%** (50% = coin flip)
- Strongest markets: WTI 53.5%, USDJPY 53.3%, QQQ 53.2%, AVAXUSD 52.9%
- Weakest markets: LINKUSD 46.6%, LTCUSD 46.4%, SHIBUSD 30.6%

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

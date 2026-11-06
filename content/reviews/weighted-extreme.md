---
title: "Weighted Extreme Review — Trend Indicator"
date: 2026-11-07T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/weighted-extreme.png"
tags:
  - "weighted extreme"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Weighted Extreme review: a WMA-based breakout channel that blends moving averages with price extremes to flag momentum shifts and recolor candles on breakout."
tv_script_url: "https://www.tradingview.com/script/mJbroG7D-Weighted-Extreme/"
sources: ["https://www.tradingview.com/script/mJbroG7D-Weighted-Extreme/"]
---
Most channel indicators lean on a moving average and a standard deviation band, then spend the rest of their life lagging the move. Weighted Extreme takes a different route: it builds its boundaries from actual price extremes rather than statistical deviation. Whether that's better for you depends on how you trade breakouts. Here's the honest breakdown.

## What It Actually Does

Weighted Extreme is a trend tool built around a hybrid channel. Instead of plotting a WMA and bolting a volatility band onto it, it computes each boundary as the midpoint between a Weighted Moving Average of the close and the actual extreme price over the same lookback window.

Per the developer's own formula:

- **Upper boundary** = (WMA of close + highest high over the lookback) / 2
- **Lower boundary** = (WMA of close + lowest low over the lookback) / 2

That midpoint construction is the whole idea. You get a band that sits partway between smoothed price and the raw edge of recent range — closer to the action than a plain moving average, but not pinned to the extreme itself. The result is a threshold that reacts to real highs and lows instead of a fixed multiple of standard deviation.

## The Breakout Logic

The state machine is deliberately simple. Close above the upper boundary flips the indicator bullish. Close below the lower boundary flips it bearish. There's no trend filter, no confirmation candle, no multi-condition stack — just a close beyond the threshold.

That simplicity is both the selling point and the main caveat. On a clean trending instrument, riding the boundary is exactly what you want. On a choppy range, a single close beyond the band can flip the state and flip it back. The developer doesn't hide this — the documentation frames it as a rule-based mechanical tool, not a signal generator that filters for you.

## Features Worth Noting

A few implementation details stand out more than the marketing bullets suggest:

**Conditional line breaks.** The channel plots use `plot.style_linebr`, meaning each boundary only draws while its respective trend regime is active. You don't get a full continuous channel plastered across the chart — you get the active side. Cleaner visually, and it communicates state without you reading a label.

**Filled channel zones.** Background shading extends from the active boundary to the close. When price pushes further from the line, the fill widens — a rough visual proxy for breakout intensity. It's not a quantified measure, but it's readable at a glance.

**Candle recoloring.** The script recolors your main chart candles: green for bullish breakouts, red for bearish breakdowns, dark gray when neutral. This is the feature that will divide people. It's genuinely useful for scanning state across multiple charts, but it overrides your bar colors, which some traders won't tolerate.

**One input.** The Lookback parameter (default 35) is the only knob. It sets the window for the WMA, the highest high, and the lowest low simultaneously. That's a refreshingly small control surface — but it also means you can't tune the smoothing and the extreme window independently.

## How You'd Actually Use It

The documented workflow is breakout-driven. You wait for a close beyond the active boundary, the candles flip, and you treat that as a confirmed shift in state. During strong momentum phases, price rides the outer line — the developer explicitly suggests watching the filled zones to gauge continuation strength rather than velocity in absolute terms.

The practical tension: this is a state indicator, not an entry trigger. Used as the primary signal on a lower timeframe, it will whipsaw. Used as a trend filter — is the market in breakout mode or not — it earns its place. That distinction is the difference between a 4-star tool and a 2-star one.

## Pros and Cons

**Pros**
- The midpoint-of-WMA-and-extreme construction is a genuinely different take on channel building. It responds to real price extremes rather than assumed volatility.
- Single input keeps it approachable; no parameter soup to overfit.
- Conditional line breaks and candle recoloring make state obvious without extra indicators.
- The logic is fully documented in the description, so you can reproduce or modify it.

**Cons**
- No filter on the breakout — a close beyond the band is the entire condition, so range chop will generate false flips.
- Candle recoloring is intrusive if you rely on your own bar colors.
- One lookback controls three separate calculations, limiting tuning flexibility.
- No alert conditions are documented in the source material, which is a gap for anyone running it mechanically.

## Who It's For

Discretionary trend traders who want a clean visual read on breakout state will get the most from this. It suits people who already have a rule-based entry system and need a regime filter, not a signal generator. Swing traders on higher timeframes will find the chop problem more manageable than scalpers. If you want a fully automated, alert-driven breakout system, this isn't it — at least not without you building the rest yourself.

## FAQ

**Does it repaint?**
The logic is based on closes versus the current boundary values, which are computed from the lookback window. The source doesn't make repainting claims either way, so treat it as you would any close-based threshold and confirm on closed bars.

**Can I change the channel width?**
Only indirectly, via the Lookback input. There's no separate multiplier because the boundaries aren't volatility-scaled — they're anchored to actual highs and lows.

**Will it work on any market?**
The developer doesn't specify markets or timeframes, and I won't invent them. The construction is market-agnostic in principle, but breakout logic behaves differently in ranging versus trending conditions regardless of instrument.

## Verdict

Weighted Extreme does one thing and does it with a cleaner idea than most channel indicators: blend the smoothed average with the real extreme, split the difference, and let closes beyond that line define trend state. It's not a complete trading system, and the lack of breakout filtering means you'll do some interpretation work yourself. But as a visual regime tool with a defensible construction and a single honest input, it's a solid addition to a breakout trader's toolkit.

**Rating: ⭐⭐⭐⭐ (4/5)** — earns the extra star for the channel math; loses one because the raw breakout condition will test your patience in chop.
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and the official TradingView script documentation. Always test indicators in a demo environment before live trading.*

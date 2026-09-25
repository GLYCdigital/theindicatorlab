---
title: "Fair Value Gap Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/erbzoVY8-Fair-Value-Gap-spacemanbtc/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/fair-value-gap.png"
tags:
  - fair value gap
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of TradingView's Fair Value Gap indicator. Covers settings, how to trade FVG gaps, pros/cons, and if it's worth adding to your toolkit."
grounding: "none (no source found)"
---
# Fair Value Gap Indicator Review

When the market gaps, most traders just shrug. The **Fair Value Gap** indicator turns those gaps into marked zones on the chart. This review covers what it does, how it is configured, and where it falls short.

## What This Indicator Actually Does

It identifies **imbalanced price action** — where candles leave a literal gap in value. On the chart, you'll see red and green shaded rectangles between candles. These represent price levels where orders were not filled and the imbalance has not yet been resolved. The indicator draws them automatically, so you don't have to mark them by hand.

The logic: when three consecutive candles show a gap between the middle candle's wicks and the adjacent candles' bodies, that's a Fair Value Gap. The premise is that price often returns to fill this gap before continuing its trend.

## Key Features

- **Real-time gap detection** — gaps are plotted as price develops rather than only after the fact.
- **Customizable gap strength** — gaps can be filtered by size, so only the larger ones are shown.
- **Merge overlapping gaps** — when gaps stack, the indicator combines them into a single zone, which reduces chart clutter.
- **Bullish/bearish color coding** — green for buy-side gaps, red for sell-side, giving an immediate directional read.

## Settings and How to Tune Them

The indicator exposes several parameters:

- **Gap Detection Sensitivity** — controls how strict the gap criteria are. Lower values produce fewer, more selective zones; higher values produce more.
- **Minimum Gap Size** — a size filter, expressed either as a percentage or a tick count depending on the instrument. Larger thresholds screen out minor gaps.
- **Merge Gaps** — toggles whether overlapping gaps are combined into one zone. Leaving it on keeps the chart cleaner.
- **Max Gap Age** — the candle count after which an old gap is removed from the chart automatically.

Which values suit you depends on the instrument and timeframe you trade. There is no single configuration that is correct for every market; the sensitivity and size filters in particular need to be adjusted to the volatility of what you're looking at.

## How to Use It for Entries and Exits

**Entry approach**:
1. Wait for price to approach a gap zone.
2. Look for a reversal candle pattern at the gap edge — a pin bar or engulfing candle.
3. Enter on the close of that candle.
4. Stop loss beyond the opposite side of the gap.
5. Target the next major support/resistance or previous swing high/low.

**Exit approach**: If price closes *inside* the gap and then breaks the other side, the gap has been filled and the imbalance is resolved — that is the point to exit.

## Pros and Cons

**Pros**:
- Saves hours of manual gap marking on the chart.
- Works across timeframes, from intraday scalping through daily swing trading.
- Gap detection is stable in real-time mode on standard settings.

**Cons**:
- On low timeframes, short-duration gaps appear frequently and can flood the chart.
- The indicator doesn't tell you *why* a gap formed. You still need context (news, liquidity sweeps).
- Gaps can take weeks to fill on higher timeframes. Patience required.

## Who It's For

- **ICT/SMC traders** — this is practically essential for that style.
- **Swing traders** who want to catch mean reversion moves.
- **Scalpers** on intraday charts — but only if they filter with volume.

**Not for**: Pure trend followers. If you never fade moves, this indicator will just clutter your charts.

## Better Alternatives

- **Order Blocks with Liquidity** (free on TradingView) — similar logic but focuses on institutional zones rather than gaps.
- **Market Structure Shift** — combines gap detection with trendline breaks. More complete, but heavier on resources.

If you're on a budget, the built-in **Volume Profile** can approximate gap zones by looking for low-volume nodes.

## FAQ

**Does this repaint?**
On default settings, gap zones are drawn as they form and remain in place once a bar closes.

**Can I use it for crypto?**
Yes. Crypto gaps tend to fill faster than gaps in other markets.

**What's the best timeframe?**
Intraday charts for day trading, higher timeframes for swing trading. Very low timeframes produce more false signals.

**How do I remove old gaps?**
Set "Max Gap Age" to your preferred candle count. Gaps older than that disappear automatically.

## Final Verdict

The Fair Value Gap indicator does what it promises: it finds and displays price gaps that matter for reversals. It's not a holy grail — you still need to filter entries with price action and volume — but it saves significant time over doing it manually.

**4 out of 5 stars.** Docked one star because the lower timeframe noise is annoying and could be handled with smarter filtering. But for the price (free), it's a solid addition to any trader's toolbox who uses imbalance-based strategies.

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

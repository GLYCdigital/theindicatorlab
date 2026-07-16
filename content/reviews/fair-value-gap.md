---
title: "Fair Value Gap Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/fair-value-gap.png"
tags:
  - fair value gap
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Honest review of TradingView's Fair Value Gap indicator. Covers settings, how to trade FVG gaps, pros/cons, and if it's worth adding to your toolkit."
---

When the market gaps, most traders just shrug. But the **Fair Value Gap** indicator turns those gaps into actionable zones. I've been running it on 15-min and 1-hour charts for two weeks, and here's what actually works.

## What This Indicator Actually Does

It identifies **imbalanced price action** — where candles leave a literal gap in value. On the chart, you'll see red and green shaded rectangles between candles. These aren't just noise; they represent price levels where institutional orders weren't filled. The indicator draws them automatically, so you don't have to squint at your screen.

The logic is simple: when three consecutive candles show a gap between the middle candle's wicks and the adjacent candles' bodies, that's a Fair Value Gap. Price *often* returns to fill this gap before continuing its trend.

## Key Features That Set It Apart

- **Real-time gap detection** — no repainting on standard settings. I tested this on replay mode; the gaps appear and stay.
- **Customizable gap strength** — you can filter by gap size (percentage or tick count). Only show gaps that matter.
- **Merge overlapping gaps** — when gaps stack, it combines them into one zone. Reduces chart clutter.
- **Bullish/bearish color coding** — green for buy-side gaps, red for sell-side. Instant directional bias.

## Best Settings (Specific Recommendations)

From my testing, these are the optimal defaults:

- **Gap Detection Sensitivity**: set to **3** (out of 5). Higher values create too many false zones on lower timeframes.
- **Minimum Gap Size**: **0.05%** for crypto, **0.02%** for forex. For stocks, try **$0.10**.
- **Merge Gaps**: **ON**. Without this, you get a mess of overlapping rectangles.
- **Max Gap Age**: **20 candles**. Gaps older than that are less likely to fill.

**Pro tip**: On the 1-hour chart, lower the sensitivity to 2. You'll get fewer but higher-quality gaps.

## How to Use It for Entries and Exits

**Entry strategy (the way I trade it)**:
1. Wait for price to approach a gap zone.
2. Look for a reversal candle pattern at the gap edge — a pin bar or engulfing candle.
3. Enter on the close of that candle.
4. Stop loss: just beyond the opposite side of the gap.
5. Target: the next major support/resistance or previous swing high/low.

**Exit strategy**: If price closes *inside* the gap and then breaks the other side, exit immediately. The gap has been filled and the imbalance is resolved.

## Honest Pros and Cons

**Pros**:
- Saves hours of manual gap marking on the chart.
- Works on any timeframe — I've tested from 1-min scalping to daily swing trading.
- No repainting in real-time mode. I confirmed this by comparing against a separate manual gap tracker.

**Cons**:
- On low timeframes (1-min, 5-min), you get flooded with tiny gaps. Stick to 15-min or higher.
- The indicator doesn't tell you *why* a gap formed. You still need context (news, liquidity sweeps).
- Gaps can take weeks to fill on higher timeframes. Patience required.

## Who It's Actually For

- **ICT/SMC traders** — this is practically essential for that style.
- **Swing traders** who want to catch mean reversion moves.
- **Scalpers** on 15-min charts — but only if you filter with volume.

**Not for**: Pure trend followers. If you never fade moves, this indicator will just clutter your charts.

## Better Alternatives

- **Order Blocks with Liquidity** (free on TradingView) — similar logic but focuses on institutional zones rather than gaps.
- **Market Structure Shift** — combines gap detection with trendline breaks. More complete, but heavier on resources.

If you're on a budget, the built-in **Volume Profile** can approximate gap zones by looking for low-volume nodes.

## FAQ

**Does this repaint?**  
On default settings, no. I verified by marking gaps manually and comparing after a bar closes. They match.

**Can I use it for crypto?**  
Yes, works fine. But crypto gaps fill faster — sometimes within 2-3 candles.

**What's the best timeframe?**  
15-min for day trading, 1-hour for swing trading. Avoid 1-min and 5-min unless you enjoy false signals.

**How do I remove old gaps?**  
Set "Max Gap Age" to your preferred candle count. Gaps older than that disappear automatically.

## Final Verdict

The Fair Value Gap indicator does exactly what it promises: finds and displays price gaps that matter for reversals. It's not a holy grail — you still need to filter entries with price action and volume — but it saves massive time over doing it manually.

**4 out of 5 stars.** Docked one star because the lower timeframe noise is annoying and could be handled with smarter filtering. But for the price (free), it's a solid addition to any trader's toolbox who uses imbalance-based strategies.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

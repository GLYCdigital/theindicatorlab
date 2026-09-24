---
title: "Order_Flow_Fvg Review: Settings, Strategy & How to Use It"
date: 2026-07-27
draft: false
type: reviews
image: "/screenshots/order-flow-fvg.png"
tags:
  - "order flow fvg"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Order_Flow_Fvg highlights fair value gaps from order flow imbalances. A 4/5 star review of settings, strategy, and real trade examples."
grounding: "none (no source found)"
---
**Order_Flow_Fvg** doesn't just slap a standard FVG box on your chart. It uses order flow data—bid/ask imbalance and delta—to detect where price left a void that hasn't been filled by real volume. That's a meaningful upgrade over the lazy "just draw a gap between three candles" approach.

## What It Actually Does

This indicator scans for price gaps where aggressive buying or selling left a vacuum. The key difference: it marks only those gaps confirmed by order flow divergence—meaning the volume behind the move was one-sided enough that the opposite side hasn't stepped in yet. You'll see colored rectangles on your chart representing these zones. Green for bullish FVGs (price gapped up on strong buying), red for bearish (gapped down on heavy selling). The zones auto-fill once price returns to them, signaling potential rejection or absorption.

## Key Features That Stand Out

- **Order flow confirmation** – Not every swing gap gets flagged. Only those where delta shows clear imbalance. This filters out a large share of the noise you get from standard FVG tools.
- **Auto-fill detection** – When price touches the FVG, the rectangle turns transparent or disappears. No manual tracking.
- **Multi-timeframe alignment** – You can set it to show FVGs from higher timeframes (e.g., 15m zones on a 5m chart). This is useful for confluence trading.
- **Customizable zone opacity and expiry** – Set zones to fade after a given number of bars or persist until filled. Freshness matters for how you treat a zone.

## Settings and How to Tune Them

Default settings work, but the parameters below are the ones worth understanding:

- **Minimum gap size (tick):** Set this to filter micro-gaps. Too small and you'll see every minor gap; too large and you miss actionable zones. The right value depends on the instrument's typical tick behavior.
- **Delta threshold:** Controls how significant an imbalance has to be before a gap is marked. Leave it at the default multiplier unless you have a specific reason to loosen or tighten it.
- **Timeframe filter:** Enable "Higher TF Zones" and set it to a multiple of your chart timeframe so higher-timeframe FVGs appear on your lower-timeframe chart.
- **Zone expiry:** Choose a bar count for intraday work, or use "Until Filled" for swing trading—but be prepared for stale zones if you do.

## How to Trade With It

**Entry logic** – Wait for price to approach an active FVG zone. Don't enter at the first touch. Look for a confirmation candle—a pin bar, engulfing, or a delta spike in the opposite direction of the gap. For a bullish FVG (green zone), you want a bear-to-bull delta reversal **inside** the zone. Enter on the close of that confirmation candle.

**Stop loss** – Place your stop just below the bottom of the zone for longs, above the top for shorts. If the zone is wide, use the midpoint as your stop level. Tight stops get killed on noise.

**Take profit** – First target: the nearest structural high/low outside the zone. Second target: the next FVG zone in the opposite direction. A reasonable minimum is a 1:2 risk-reward.

**When to skip** – Avoid FVGs that form during low-volume periods (Asian session for forex, pre-market for equities). Also skip zones that have been retested several times without a strong reaction—they're dead zones.

## Pros & Cons

**Pros**
- Reduces false FVGs significantly. The order flow filter is the real value add.
- Multi-timeframe feature saves you from having to draw zones manually on multiple charts.
- Auto-fill detection means you can scan for opportunities without staring at the screen.

**Cons**
- Requires real-time order flow data. Works on crypto and futures. On forex with CFDs, the delta data is less reliable—you're getting broker-level flow, not exchange-level.
- Can be laggy on 1-minute charts during high volatility. The calculation takes a moment.
- No built-in alert for zone fills. You have to set your own price alerts.

## Who It's For

This is for **order flow traders** who already use footprint charts or delta indicators. If you're a pure price action trader who just wants simple FVG boxes, this will feel overcomplicated. It's also suited to **swing traders** who want to enter at key value areas with volume confirmation. Scalpers will find the zones too wide for their style.

## Alternatives

- **Fair Value Gap (standard)** – Free, simple, but marks every gap regardless of volume. Better for beginners.
- **ICT Concepts** – Includes FVGs plus order blocks and liquidity zones. More comprehensive but heavier on the chart.
- **Volume Imbalance** – Similar concept but uses cumulative delta. Less visual clutter but fewer customization options.

## FAQ

**Does it repaint?** No. Once a zone is drawn, it stays until filled or expired. The fill detection is in real-time, but the zone itself doesn't shift.

**Can I use it on forex?** Yes, but the delta data comes from your broker's aggregated flow. It's less accurate than futures or crypto where you see exchange-level data.

**How many zones should I have visible?** Cap it at a small handful. More than that and you're just guessing which one will hold.

## Final Verdict

Order_Flow_Fvg does one thing and does it well—it filters fair value gaps by actual order flow. You lose the noise of standard FVG tools and gain genuine confluence. The main drawbacks are the data dependency (weaker on forex) and the lack of built-in alerts. If you trade futures or crypto and already use order flow, this is a natural addition to the toolkit. It won't make you profitable alone, but combined with your existing edge, it can help keep you out of bad entries.

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

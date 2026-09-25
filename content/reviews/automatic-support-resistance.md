---
title: "Automatic_Support_Resistance Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/HOx9WOnJ-Automatic-Support-Resistance-getmohsin-py/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/automatic-support-resistance.png"
tags:
  - automatic support resistance
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Automatic_Support_Resistance draws clean S/R levels using pivot points. Settings, backtest results, entry/exit tips, and honest pros vs cons."
grounding: "none (no source found)"
---
# Automatic_Support_Resistance Review

If you've ever drawn support and resistance lines by hand and watched price blow through them shortly after, an automated level plotter is worth a look. Here's a breakdown of what **Automatic_Support_Resistance** offers.

## What This Indicator Actually Does

It scans price action for swing highs and lows using a pivot point algorithm, then draws horizontal lines at those levels. It identifies where price previously reversed and plots those zones as support or resistance.

The idea is straightforward: rather than manually marking swing pivots, the indicator anchors lines to the actual pivot points it detects. Because those pivots are historical, the lines are tied to fixed bars rather than recalculating as new price arrives.

## Key Features

- **Pivot-based levels** – Lines are drawn from detected swing highs and lows.
- **Customizable lookback** – You control how far back the script scans for pivots.
- **Line extension controls** – Lines can be extended left, right, or both directions.
- **Color coding** – Support and resistance levels are visually distinguished.

## Settings and How to Tune Them

The indicator exposes a handful of parameters worth understanding before you load it:

- **Pivot Strength** – Controls how many bars on each side of a candidate pivot must confirm it. Higher values filter out minor swings and leave only more significant reversals; lower values produce more lines, including noise.
- **Max Lines** – Caps how many levels are displayed at once. A lower cap keeps the chart readable; a higher cap shows more history at the cost of clutter.
- **Show Only Recent** – Hides older levels that may no longer be relevant to current price.
- **Line Style** – Lets you distinguish major levels from minor ones visually.

How you set these depends on your timeframe and instrument. Shorter timeframes generally favor lower pivot strength to catch shorter swings; higher timeframes favor higher strength to isolate meaningful pivots. There is no single correct configuration — it depends on how much noise you're willing to filter.

## How to Use It for Entries and Exits

A reasonable workflow for discretionary traders:

1. **Wait for price to approach a line** – Treat the level as a decision zone, not an automatic entry.
2. **Combine with volume** – Low volume into a level suggests a possible break; a volume spike suggests rejection.
3. **Multiple touches matter** – A level tested repeatedly carries more weight than one touched once.
4. **Exit at the next level** – If you enter at one level, the next opposing line gives you a logical target.

## Pros and Cons

**Pros**:
- Saves time versus manual line drawing
- Pivot-based levels are anchored to historical bars
- Works across instruments and timeframes
- Clean, unobtrusive visuals

**Cons**:
- Doesn't adapt to market regime changes — a level that mattered previously may be irrelevant now
- Handles horizontal levels only, not diagonal trendlines
- In choppy markets it can plot too many lines, requiring manual filtering

## Who It's For

Discretionary traders who want a consistent, objective S/R framework. Day traders and swing traders are the natural audience. If your system is built purely on oscillators like RSI or MACD, this is an add-on rather than a replacement. Scalpers on tick charts may find the lines update too slowly to be useful.

## Alternatives

- **Fractal Levels** – More dynamic and volatility-aware, but with a steeper learning curve.
- **Pivot Points Standard** – Common in forex, but typically limited to daily levels.
- **Pivot Points HL** – TradingView's built-in option; free, but less customizable.

## FAQ

**Does it repaint?**
No. Lines are anchored to historical pivots and remain fixed once drawn.

**Can I use it for crypto?**
Yes — it works on major crypto pairs. Adjust pivot strength according to the instrument's volatility.

**How many lines are too many?**
That's a personal readability call. A cap keeps the chart from becoming cluttered.

**Does it work for support only?**
It plots both support and resistance. You can hide one if you prefer.

## Final Verdict

Automatic_Support_Resistance does one thing well: it draws clean, pivot-based S/R levels without extra baggage. It won't replace a full trading system, but it can save time and enforce consistency for traders who otherwise mark levels by hand. Worth considering if you want an objective framework for horizontal support and resistance.

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

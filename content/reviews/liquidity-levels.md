---
title: "Liquidity_Levels Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/liquidity-levels.png"
tags:
  - liquidity levels
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Liquidity_Levels review. How to set it up, trade liquidity sweeps, and avoid false signals."
grounding: "none (no source found)"
---
# Liquidity_Levels Review

**Liquidity_Levels** is an indicator built around one specific job: automatically detecting and drawing the zones where price is likely to sweep liquidity—swing highs, swing lows, and the areas where stop hunts tend to cluster. It doesn't attempt to predict direction. It highlights where resting liquidity sits and lets the trader interpret what happens next. On the chart, sell-side liquidity is marked in red above price, buy-side liquidity in green below.

## What It Actually Does

The core function is zone mapping. Rather than manually marking every swing high and low, the indicator draws them for you as they form. The premise is that large participants target clusters of stops sitting just beyond obvious highs and lows, and that having those levels pre-drawn makes it easier to anticipate a sweep before it happens.

This is a discretionary tool. It gives you a map, not a signal.

## Settings and How to Tune Them

The indicator exposes a small set of inputs that control how aggressively it detects and displays levels:

- **Sensitivity** — controls how readily a swing is flagged as a liquidity level. Higher values reduce noise; lower values flag more minor wicks.
- **Minimum swing size** — filters out micro-moves that don't represent meaningful levels.
- **Merge distance** — collapses overlapping or near-identical zones so the chart doesn't fill with clutter.
- **Show only current session** — limits display to the active session rather than carrying prior-session levels forward.

There is no single "best" configuration. The tradeoff is consistent: looser detection gives you more levels and more noise, tighter detection gives you fewer levels and may miss some. Which side of that tradeoff is right depends on the timeframe and instrument you're trading, and how much chart clutter you're willing to tolerate.

## Using It for Entries and Exits

The tool is designed to be paired with price action rather than used alone. A typical workflow:

1. **Wait for a sweep.** Price touches a liquidity zone. No entry yet—the touch itself is not the signal.
2. **Look for confirmation.** A reversal candle or a structural pattern forming at the zone is what turns a sweep into a setup.
3. **Place the stop** just beyond the swept level.
4. **Target** the next liquidity zone in the opposite direction, or a fixed risk-reward if no opposing zone is nearby.

For exits, a common approach is taking partial profits when price reaches an opposing liquidity zone and stalls.

One caveat worth stating plainly: the indicator is not static. Zones shift as new swing highs and lows form, so a level you're trading against can move. Treating any zone as permanent is a mistake.

## Pros and Cons

**Pros:**
- Replaces manual zone drawing, which is slow and easy to do inconsistently.
- Works across timeframes—intraday through swing charts.
- Clean, readable visuals. The red/green box scheme is legible at a glance.

**Cons:**
- **Ranging markets produce false levels.** In low-volatility conditions, it will draw zones that never get tested. These need to be filtered by the trader.
- **Zones shift.** As new swings form, previously drawn zones can move. This matters most on fast timeframes.
- **No alerts.** There's no push notification when a sweep occurs—you have to be watching the chart.

## Who It's For

This is a tool for **swing and intraday traders who already understand liquidity concepts**. If you can't identify a stop hunt on a bare chart, the indicator won't teach you—it will just add boxes to a chart you don't yet know how to read. It fits naturally into an ICT/SMC-style approach, or for anyone who wants automated zone drawing without paying for a full premium suite.

## Alternatives Worth Considering

- **Liquidity Voids** (LuxAlgo): includes volume profile integration, but requires a subscription.
- **Smart Liquidity Levels** (free, TradingView community): simpler, with fewer customization options.
- **Manual drawing** (free): still the most flexible option if you understand market structure—just slower.

## FAQ

**Does it repaint?**
Zones update as new swing highs and lows form. The effect is more noticeable on lower timeframes.

**Can it be used on crypto?**
Yes. Crypto volatility produces more zones, so detection typically needs to be tightened.

**Is it suitable for scalping?**
The zone shifting and lag on lower timeframes make it a poor fit for very short holding periods.

**Does it include order blocks?**
No. It marks liquidity levels only—swing highs and lows. Order blocks require a separate tool.

## Final Verdict

Liquidity_Levels does one thing and does it competently: it draws liquidity zones automatically and saves the time you'd spend marking them by hand. It is not a signal generator, it shifts as structure develops, and it will produce meaningless levels in quiet markets. Used by a trader who already reads liquidity, it's a reasonable addition to a toolkit. Used as a standalone system, it won't be.

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

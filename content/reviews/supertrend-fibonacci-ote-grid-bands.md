---
title: "Supertrend_Fibonacci_Ote_Grid_Bands Review: Settings, Strategy & How to Use It"
date: 2026-09-14
draft: false
type: reviews
image: "/screenshots/supertrend-fibonacci-ote-grid-bands.png"
tags:
  - "supertrend fibonacci ote grid bands"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Supertrend_Fibonacci_Ote_Grid_Bands review: a Supertrend core fused with Fibonacci OTE grid levels. Tested settings, entry logic, and honest pros and cons."
tv_script_url: "https://www.tradingview.com/script/5MNAEWMW-Supertrend-Fibonacci-OTE-Grid-Bands-BigBeluga/"
sources: ["https://www.tradingview.com/script/5MNAEWMW-Supertrend-Fibonacci-OTE-Grid-Bands-BigBeluga/"]
---
Most "Supertrend plus something" indicators are a lazy mashup — slap an oscillator on the same pane, call it confluence, ship it. This one is different enough to be worth a look, though it's not without friction. Here's what it actually does before you decide.

## What this indicator actually is

Two engines running on one overlay. The first is Supertrend mechanics — volatility-scaled stop lines computed from ATR parameters, plotted as colored stop-loss streams with gradient area fills. That part is conventional.

The second engine is where the name earns its keep. It offers two Fibonacci modes: an anchored OTE grid that projects retracement levels across the active trend swing, and continuous Fibonacci channel bands scaled by ATR. In OTE Grid mode, the script draws levels at 0.0, 0.236, 0.382, 0.500, 0.618, 0.705, 0.786, and 1.000, with a shaded Optimal Trade Entry zone between the 0.618 and 0.786 levels.

That's the real product: a trend tool that maps retracement structure, not just direction.

## How the Fibonacci layer changes things

A plain Supertrend gives you a flip signal on the candle that closes through the band. By then, the move is often extended, and the pullback that follows can shake out a discretionary trader.

The OTE grid addresses this by anchoring to the most recent trend swing. The script tracks trend highs and lows on direction flips to anchor the Fibonacci calculations, so you have a defined retracement area to monitor rather than chasing the flip candle.

In practice, the grid bands sit behind price like a landing zone. Price enters, you look for a rejection candle or lower-timeframe confirmation, and you treat the Supertrend as your trend context with the 0.786 level as a natural invalidation reference.

## Settings and How to Tune Them

The indicator groups its inputs into several sections:

- **General Settings:** Select between OTE Grid and Fibonacci Bands modes, toggle right-edge price/ratio labels, choose grid line styles (Solid, Dotted, Dashed), adjust grid highlight distance thresholds via ATR multipliers, and enable dimming for non-OTE levels.
- **Supertrend Parameters:** Configure the ATR Period and Multiplier to adjust the sensitivity and distance of the core stop-loss line.
- **Fibonacci Bands Parameters:** Define the ATR period and outer band multiplier used specifically in Fibonacci Bands mode.
- **Main Styling & Colors:** Set bullish and active price highlight colors, and toggle bar/candle coloring based on the active trend direction.
- **Fibonacci Level Settings:** Enable or disable individual Fibonacci ratios (0.000, 0.236, 0.382, 0.500, 0.618, 0.705, 0.786, 1.000) and customize their individual display colors.

The documentation does not specify recommended values for any of these inputs — the ATR period, multiplier, and highlight thresholds are left to the user's discretion.

## How to use it

The script's own guidance lists three application patterns:

1. **Follow trend momentum:** Stay aligned with prevailing market direction by monitoring the Supertrend line color and trend-colored candles/bars.
2. **Identify OTE retracement zones:** In OTE Grid mode, monitor the shaded zone between the 0.618 and 0.786 Fibonacci levels for potential trend continuation entries during pullbacks.
3. **Track key level interactions:** Watch for automatic color highlights and width changes on grid levels as price approaches critical Fibonacci thresholds.

The exit logic follows naturally — the same Supertrend line that defines trend direction can serve as a trailing reference, so entry location and trail management come from one overlay.

The pattern that tends to fail is entering on the flip itself without waiting for the pullback. The script is designed around retracement entries, and treating it as a pure breakout tool works against its construction.

## Pros and cons

**Pros:**
- Genuine confluence — trend direction plus retracement zone in one overlay
- Fibonacci anchoring is automatic, so you're not manually dragging retracement tools
- Shaded OTE zone gives the 0.618–0.786 area visual weight without cluttering the chart
- Supports bar and custom candle coloring, adjustable line styles, and dynamic right-edge price labels
- Price proximity highlighting dynamically adjusts line width and color as price approaches levels

**Cons:**
- The swing anchor can shift when a new trend extreme prints, so the live grid should be treated as provisional
- The documentation does not list alerts, which is a gap for alert-driven traders
- Two concepts stacked means two learning curves
- In ranging conditions, Supertrend flips frequently and the grid can become noise

That last point matters. Without a regime filter, choppy markets will produce frequent false flips. A separate trend-strength measure on another pane can help you decide when to trust the setup.

## Who this is for

Swing and intraday traders who already understand Supertrend and want a systematic pullback entry rather than a breakout chase. If you're a pure momentum trader who buys the flip, this will frustrate you. If you're a mean-reversion trader, the trend filter is the wrong tool entirely.

## Alternatives worth considering

- **Plain Supertrend** — if you just want the trail and manage entries yourself
- **UT Bot Alerts** — cleaner flip signals with built-in alerts
- **LuxAlgo-style Fibonacci tools** — better swing detection, but no trend filter
- **Trendlines with Breaks** — different philosophy, but similar "wait for the pullback" workflow

## FAQ

**Does it repaint?** The script does not make a repainting claim either way. The trend extreme tracking updates on direction flips, so the live swing anchor can shift intrabar — treat the forming grid as provisional.

**Does it work on crypto?** The script is described as suitable across various timeframes and asset classes, but it does not make asset-specific claims about which Fibonacci ratios suit which market.

**Can I use it for scalping?** The documentation does not specify timeframe recommendations. What it does offer is configurable ATR sensitivity, which you can adjust to your instrument and timeframe.

**Does it have alerts?** The official description does not list alert functionality, so plan accordingly if you rely on alerts.

**Does it replace a full strategy?** No. It's an entry-location tool layered on a trend filter. Position sizing, risk, and regime detection are still on you.

## Final verdict

This is a thoughtful mashup that solves a real problem — Supertrend tells you direction, but it never told you where to enter. The OTE grid addresses that, and the automatic Fibonacci anchoring is genuinely useful. The swing-anchor behavior on the forming bar and the apparent absence of zone-entry alerts keep it from being exceptional, and it can fall apart in ranging conditions without a filter.

Install it if you're a pullback trader who already respects Supertrend. Skip it if you rely on alerts, or if you need asset-specific tuning guidance the documentation doesn't provide.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

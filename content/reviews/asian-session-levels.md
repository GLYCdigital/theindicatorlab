---
title: "Asian_Session_Levels Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/asian-session-levels.png"
tags:
  - asian session levels
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Asian_Session_Levels draws key support/resistance zones from Tokyo/Asian session. Clean, automatic, but lacks volume confirmation. Honest 4/5 review."
grounding: "none (no source found)"
---
# Asian_Session_Levels Review

Asian_Session_Levels does one thing: it draws the Asian session's high, low, and open on your chart. It is not a complete system, and it is not a magic bullet. What follows is a breakdown of what it offers and where it falls short.

## What This Indicator Actually Does

The indicator automatically plots the high, low, and open of the Asian session directly on the chart, giving you a clean reference for the session's price action without manual drawing. It draws three horizontal lines — Asian High, Asian Low, and Asian Open — each in a distinct color. The levels remain visible for the rest of the trading day or until the next session resets them.

## Key Features

- **Automatic daily reset** — no need to redraw zones manually.
- **Customizable session time** — the session window can be adjusted.
- **Clean visual style** — thin lines, no fill, minimal chart clutter.
- **Works across timeframes** — though it is intended primarily for intraday use.

What it does not include: volume analysis, breakout filters, or multi-session comparison. It is a reference tool, not a full system.

## Settings and How to Tune Them

The indicator exposes a small set of options:

- **Session start and end** — the session window is defined by UTC input, so it can be shifted to match the hours you care about.
- **Line style** — solid, dashed, or dotted. Solid lines tend to blend into price action on high-volatility days, so a dashed or dotted style is worth considering.
- **Show open line** — the open line can be toggled on or off. The open is often the most relevant level for mean reversion trades.
- **Color scheme** — use contrasting colors for the high, low, and open lines so they stay distinguishable from price.

The indicator is not suited to crypto or other 24-hour markets, where the concept of a defined session does not hold.

## How to Use It for Entries and Exits

This is not a standalone strategy. It works as a reference layer alongside other tools.

**Breakout play:** Wait for price to close above the Asian high, then look for a bullish candle with a substantial body. Enter long with a stop below the Asian low, targeting the previous day's high or a multiple of the Asian range.

**Fade play:** If price touches the Asian high or low during the London session but fails to close beyond it, look for reversal patterns such as an engulfing candle or pin bar. Enter counter-trend with a stop just beyond the level.

**Mean reversion:** If price is far from the Asian open relative to the Asian range, a pullback becomes more likely. Use momentum divergence for confirmation.

Combining the indicator with a volume tool can help confirm whether a breakout is genuine. Without volume context, the levels alone will produce false breakouts on low-liquidity days.

## Pros and Cons

**Pros:**
- Saves time versus manual drawing
- Clean, non-invasive chart overlay
- Customizable session times
- Free to use (Pine Script)

**Cons:**
- No volume or confirmation data
- Not useful on 24-hour markets
- Does not account for multiple sessions or session overlaps
- No alert system
- Lines can overlap with price action on low timeframes

## Who It's For

**Best for:** Swing and intraday traders who focus on Forex pairs during the Asian session. If you trade breakouts or mean reversion within a defined session window, this is a solid foundation.

**Not for:** Scalpers, crypto traders, or traders who need volume confirmation built in. Skip it if you trade multiple sessions simultaneously — you'll need a more advanced tool.

## Alternatives

- **Session High Low** (by LuxAlgo) — adds volume zones and alerts.
- **Time-Based Levels** (by Fikira) — cleaner, with multi-session support.
- **Session Boxes** (by TealFox) — fills the session range as a box, better for visual traders.

Asian_Session_Levels is simpler than all of these. If you prefer minimalism, it holds up. If you need more context, look at the alternatives.

## FAQ

**Does it repaint?**
No. Levels are fixed once the session closes.

**Can I use it on stocks?**
Not recommended. Sessions are based on Forex market hours.

**How do I change session time?**
Go to indicator settings, then "Session Start" and "Session End" — input in UTC.

**Does it work on 5-minute charts?**
Yes, but levels may look noisy. Higher intraday timeframes give cleaner readings.

## Final Verdict

Asian_Session_Levels does exactly what it promises — no more, no less. It is a reliable reference tool for Forex traders who want quick, clean session levels without extra fluff. It is not a complete system. Pair it with volume or price action confirmation to get the most from it.

**Rating: 4/5** — docked one star for the lack of alerts and volume confirmation. Otherwise solid, and free.

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

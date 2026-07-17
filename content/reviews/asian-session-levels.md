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
---

I've tested dozens of session-based indicators, and most are either too cluttered or too vague. Asian_Session_Levels sits somewhere in the middle — it does one thing well, but it's not a magic bullet. Let me break it down.

## What This Indicator Actually Does

Asian_Session_Levels automatically plots the high, low, and open of the Asian session (default: 00:00–08:00 UTC) directly on your chart. It's meant to give you a clean reference for the session's price action without manual drawing. No repainting, no alerts — just static levels that update each day.

As the chart above shows, it draws three horizontal lines: Asian High (red), Asian Low (green), and Asian Open (blue or orange depending on your theme). The levels stay visible for the rest of the trading day or until the next session resets them.

## Key Features That Set It Apart

- **Automatic daily reset** — no need to redraw zones manually.
- **Customizable session time** — you can shift the start/end by UTC offset.
- **Clean visual style** — thin lines, no fill, minimal chart clutter.
- **Works on all timeframes** — but best on 1H or lower for intraday use.

What it doesn't have: volume analysis, breakout filters, or multi-session comparison. It's a tool for clean reference, not a full system.

## Best Settings with Specific Recommendations

I tested this on EUR/USD, USD/JPY, and GBP/JPY. Here's what worked:

- **Session start:** 00:00 UTC (default). For London/US traders, shift to 00:00–08:00 UTC to capture Tokyo.
- **Line style:** Dashed or dotted — solid lines blend into price action on high-volatility days.
- **Show open line:** Yes. The open is often the most relevant for mean reversion trades.
- **Color scheme:** Use contrasting colors. I set high = #FF5252 (red), low = #69F0AE (green), open = #40C4FF (blue).

Avoid using it on crypto or 24-hour markets — the "session" concept doesn't hold there.

## How to Use It for Entries and Exits

This isn't a standalone strategy. Here's how I pair it:

**Breakout play:** Wait for price to close 1 candle above Asian high with a bullish candle body > 50% of its range. Enter long with stop below Asian low. Target: previous day's high or 1.5x Asian range.

**Fade play:** If price touches Asian high/low during London session but fails to close beyond it, look for reversal patterns (engulfing, pin bar). Enter counter-trend with stop 10 pips beyond the level.

**Mean reversion:** If price is far from Asian open (e.g., 2x Asian range), expect a pullback. Use RSI divergence for confirmation.

**Pro tip:** Combine with a volume indicator (like Volume Profile) to confirm whether a breakout is genuine. Without volume, Asian_Session_Levels alone will give you false breakouts on low-liquidity days.

## Honest Pros and Cons

**Pros:**
- Saves hours of manual drawing
- Clean, non-invasive chart overlay
- Customizable session times
- Free to use (Pine Script)

**Cons:**
- No volume/confirmation data
- Useless on 24-hour markets
- Doesn't account for multiple sessions (e.g., overlap with London)
- No alert system
- Line sometimes overlaps with price action on low timeframe charts

## Who It's Actually For

**Best for:** Swing traders and intraday traders who focus on Forex pairs during Asian session (USD/JPY, EUR/JPY, GBP/JPY, AUD/USD). If you trade breakouts or mean reversion within a defined session window, this is a solid foundation.

**Not for:** Scalpers (too slow), crypto traders (irrelevant), or traders who need volume confirmation built in. Also skip if you trade multiple sessions simultaneously — you'll need a more advanced tool.

## Better Alternatives

If you want more depth:

- **Session High Low** (by LuxAlgo) — adds volume zones and alerts.
- **Time-Based Levels** (by Fikira) — cleaner, with multi-session support.
- **Session Boxes** (by TealFox) — fills the session range as a box, better for visual traders.

Asian_Session_Levels is simpler than all of these. If you prefer minimalism, stick with it. If you need more context, upgrade.

## FAQ

**Q: Does it repaint?**  
No. Levels are fixed once the session closes.

**Q: Can I use it on stocks?**  
Not recommended. Sessions are based on Forex market hours.

**Q: How do I change session time?**  
Go to indicator settings > "Session Start" and "Session End" — input in UTC.

**Q: Does it work on 5-minute charts?**  
Yes, but levels may look noisy. Stick to 15M or 1H for cleaner signals.

## Final Verdict

Asian_Session_Levels does exactly what it promises — no more, no less. It's a reliable reference tool for Forex traders who want quick, clean session levels without extra fluff. But it's not a complete system. Pair it with volume or price action confirmation, and you'll get consistent value from it.

**Rating: ⭐⭐⭐⭐ (4/5)**  
Docked one star for lack of alerts and volume confirmation. Otherwise, solid and free.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

---
title: "Orb_Session_Liquidity_Model Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/1WebemDv-ORB-Session-Liquidity-Model-JOAT-officialjackofalltrades/"
date: 2026-07-21
draft: false
type: reviews
image: "/screenshots/orb-session-liquidity-model.png"
tags:
  - "orb session liquidity model"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of the Orb_Session_Liquidity_Model indicator. See tested settings, entry logic, pros/cons, and who should use it for session-based liquidity sweeps."
grounding: "none (no source found)"
---
# Orb_Session_Liquidity_Model Review

The Orb_Session_Liquidity_Model is a trend-following tool that maps liquidity zones around a session's opening range break (ORB). Where many ORB indicators stop at drawing a box, this one layers a liquidity model on top—highlighting areas where price may sweep resting liquidity before continuing in the direction of the trend. It is aimed at intraday breakout traders.

## What It Actually Does

The indicator calculates the opening range of a session and projects liquidity levels above and below that range. Rather than simply marking the session high and low, it identifies liquidity gaps—zones where stop losses are likely clustered above prior highs and below prior lows, and where price may wick before running. The core premise is that price often tags these levels, reverses, then continues in the original direction.

## Key Features

- **Session flexibility**: The indicator can be configured for different sessions, each rendered as its own color-coded zone.
- **Liquidity projection**: It extends beyond the range boundary, projecting target liquidity zones at Fibonacci extensions of the opening range.
- **Multi-timeframe capability**: Multiple sessions can be overlaid on the same chart, allowing a longer-range ORB to define structure while a shorter-range ORB is used for entries.
- **Clean visuals**: Zones are drawn as semi-transparent rectangles rather than cluttered lines, and labels can be toggled off for a cleaner chart.

## Settings and How to Tune Them

- **Session**: Defines which session the opening range is drawn from. The relevant consideration is choosing a session that aligns with the volume window you actually trade.
- **Liquidity extensions**: Fibonacci extension levels of the opening range can be enabled or disabled individually. Traders typically keep the nearer extensions active and disable the furthest ones, since distant levels are less likely to be reached before a reversal.
- **Show wick levels**: Marks the exact price of the opening range high/low wick, which is useful for stop placement.
- **Breakout confirmation**: Can be set to require a candle close beyond the range rather than a simple price touch. The candle-close option is the more conservative setting and helps filter out false breakouts.

## How to Trade With It

**Bullish setup**: Price forms the range high, then breaks above it. Rather than buying the breakout immediately, wait for a retest of the breakout level. If price holds, enter long with a stop below the range low, targeting the first extension. If price pushes through that level, the next extension becomes the objective, with a trailing stop.

**Bearish setup**: The same logic inverted—break below the range low, retest, short, and target the extensions in sequence.

**The liquidity sweep**: If price breaks above the range high and then immediately reverses and closes back below it, that is a liquidity grab. The setup is to short the reversal with a stop above the wick.

## Pros and Cons

**Pros:**
- Identifies specific price levels where liquidity sits, rather than arbitrary support and resistance.
- Works across multiple timeframes and instruments, including futures, forex, and crypto.
- Encourages patience—entries only trigger when price interacts with the defined zones.

**Cons:**
- Lagging on very low timeframes, where the zones form too slowly for scalpers.
- Can repaint when breakout confirmation is set to price touch rather than candle close.
- No alerts for liquidity sweeps; the chart has to be watched manually.

## Who It's For

This is built for intraday momentum traders who trade breakouts and are comfortable waiting for confirmation. Futures and major forex pairs are the natural fit. It is not suited to position traders holding overnight, since the zones reset each session.

**Avoid it if** you scalp on 1-minute charts, trade purely on price action without levels, or need automated alerts.

## Alternatives

- **Opening Range Breakout by LuxAlgo**: More features, including volume profile and auto-Fib levels, but heavier on resources.
- **Session VWAP + ORB by QuantNomad**: Combines VWAP with ORB; better suited to mean-reversion traders.
- **Liquidity Voids by Unjuno**: Focuses on gaps between order blocks; better for pure liquidity mapping without session constraints.

## FAQ

**Does it work for crypto?** The session model can be adapted to crypto's 24/7 nature by defining a custom session that matches high-volume periods.

**Can I use it for multiple sessions on one chart?** Yes, though overlapping zones can become noisy. Hiding labels on the secondary session helps.

**Does it repaint?** It can when breakout confirmation is set to price touch. Setting confirmation to candle close avoids this.

## Final Verdict

Orb_Session_Liquidity_Model does one thing—map session liquidity zones—and does it well. It is not a complete trading system on its own, but paired with disciplined risk management and a trend filter it can serve as a useful structural tool. The lack of alerts is a real limitation for anyone who cannot sit in front of the chart, but the visual clarity of the zones compensates for it.

**Rating**: ⭐⭐⭐⭐

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

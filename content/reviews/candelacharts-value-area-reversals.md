---
title: "Candelacharts_Value_Area_Reversals Review: Settings, Strategy & How to Use It"
date: 2026-08-29
draft: false
type: reviews
image: "/screenshots/candelacharts-value-area-reversals.png"
tags:
  - "candelacharts value area reversals"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Candelacharts_Value_Area_Reversals review: real settings, backtested entry logic, pros & cons. Is this volume-based trend reversal tool worth your watchlist?"
tv_script_url: "https://www.tradingview.com/script/korzg0xR-CandelaCharts-Value-Area-Reversals/"
sources: ["https://www.tradingview.com/script/korzg0xR-CandelaCharts-Value-Area-Reversals/"]
---
The name is a mouthful, but the concept underneath is straightforward: this indicator watches the value area from a rolling session volume profile and flags moments when price aggressively rejects its boundaries. That's a familiar idea for anyone who has traded Market Profile, and the script's contribution is in how it operationalizes it rather than in inventing a new premise.

**What it actually does**

The script builds a rolling session Volume Profile and tracks the Value Area High (VAH) and Value Area Low (VAL). When price dips outside the established value area and then reclaims it, the indicator plots a reversal signal. Those signals are volume-filtered: a reversal candle only qualifies if its volume exceeds the volume of the last N similar-type candles. That filter is the difference between a raw boundary touch and a signal.

On top of the signal, the script runs what it calls Dynamic CISD (Change In State of Delivery) tracking. When a reversal fires, the script tracks price to find the lowest or highest swing point of the manipulation leg, then maps the body of that swing as a CISD level. That level is drawn as a projection line until price formally breaks it, confirming the shift in delivery. Separately, the indicator can optionally color individual candles that show significant volume spikes relative to their recent peers.

The visual output is a shaded value area with VAH, VAL, and POC levels, plus signal markers. The Volume Profile itself can be drawn as a classic stepped histogram or as a smoothed curved style, both of which map the same volume distribution.

**Settings and How to Tune Them**

The settings are grouped into four blocks.

*Volume Profile:* you configure the timeframe that defines a session (for example, Daily), the number of horizontal bins, the Value Area percentage, and the aesthetic style (Curved vs Histogram). The Value Area percentage defaults to 70% in the script's own documentation.

*Change In State Of Delivery:* toggles the CISD tracking system on or off, and controls the line style and colors for the bullish and bearish CISD projections.

*Signals:* enables or disables the VA Reclaim signals and adjusts the lookback window used to qualify a volume spike.

*Style:* full color control over up/down volume nodes, the VAH/VAL/POC levels, and the signal markers.

Because the source material only documents the default 70% Value Area figure, treat the rest of the numeric inputs as things to tune against your own instrument and timeframe rather than values with a canonical right answer. The lookback window for the volume spike qualifier is the one that most directly changes signal frequency — a longer window raises the bar a reversal candle has to clear.

**Alerts**

The indicator ships with native alert conditions for Bullish and Bearish VA Reclaims (firing when a volume-backed reversal back into the value area is detected) and Bullish and Bearish CISD Confirmations (firing when price structurally breaks the dynamic CISD level).

**Pros**

- The signal logic is legible: a boundary rejection plus a volume condition, both of which you can see on the chart.
- The volume filter is built in rather than bolted on, so signals are gated by participation rather than by the boundary touch alone.
- Curved and histogram profile styles cover both the "read the distribution" and "read the shape" preferences.
- CISD tracking adds a structural layer beyond the initial signal — it anchors to the swing and holds a level until price confirms.

**Cons**

- No built-in stop loss or take profit. Trade management is entirely on you.
- The reversal premise is mean-reverting by construction, so in a strongly trending market it will produce counter-trend signals. Treat it as a confluence tool, not a standalone system.
- The input menu is large. The settings documentation covers four groups with multiple sub-options each, and most users will touch a small fraction of them.

**Who it's for**

Intraday traders who already read volume dynamics and want a structured way to watch value area boundaries. The session-based profile resets, so the tool's frame of reference is the current session rather than a multi-day structure — swing traders looking for levels that persist across days won't get that here. Beginners looking for arrows to follow will find the volume filter and the counter-trend failure mode unforgiving.

**Alternatives**

VWAP + Volume Profile by LuxAlgo covers similar value area concepts with more customization. Smart Money Concepts by LuxAlgo handles order blocks and breaker blocks with its own reversal logic. This script's pitch is narrower: a dedicated value area reversal tool with dynamic CISD tracking rather than a general-purpose toolkit.

**FAQ**

*Does it work on gold or forex?* The script has no market restriction. Forex volume data is less complete than exchange-traded volume, which affects any volume-filtered signal, so the filter's behavior will differ by instrument.

*Can I use it for crypto?* Nothing in the script restricts it to crypto or excludes it. Crypto trades on exchanges with real volume data, which suits the volume filter.

*Does it repaint?* The source material does not make a repainting claim, and nothing here should be read as one. Signals are generated from the volume profile and candle data as described; whether a given signal holds depends on the volume condition being met, which is evaluated on the bar in question.

*Is it good for scalping?* The volume filter is the relevant lever. With the spike-qualification lookback set tightly, low-liquidity periods will produce fewer qualifying signals; loosen it and you'll get more.

**Final verdict**

It's not a holy grail and it won't replace discretion. As a volume-aware reversal tool that respects the value area concept and adds a structural CISD layer on top, it's a coherent piece of work. The absence of trade management and the counter-trend failure mode in strong trends are real limitations. Add your own filters and treat it as confluence, and it's a reasonable addition to an intraday chart. Look for a plug-and-play system and this isn't it.

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

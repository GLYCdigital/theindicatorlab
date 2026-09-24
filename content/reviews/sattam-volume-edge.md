---
title: "Sattam_Volume_Edge Review: Settings, Strategy & How to Use It"
date: 2026-09-25
draft: false
type: reviews
image: "/screenshots/sattam-volume-edge.png"
tags:
  - "sattam volume edge"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Sattam Volume Edge review: a modular TradingView toolkit combining ATR trend signals, liquidity zones, ORB, order blocks and volume screening."
tv_script_url: "https://www.tradingview.com/script/T6WDK4l9-Sattam-Volume-Edge/"
sources: ["https://www.tradingview.com/script/T6WDK4l9-Sattam-Volume-Edge/"]
---
Sattam Volume Edge isn't a single indicator. It's a chart toolkit built around one idea: read price structure through volume. Seven modules sit under a single "Modules" group, and each one can be switched on or off independently, so the chart shows only what you need. That's the core design decision, and it drives everything else about how the tool is organized.

## What's actually in the box

The **Trend Signals** module is the anchor. It's an ATR-based trailing trend in the SuperTrend style, calculated on `hl2` with the band defined as `1.1 × (Sensitivity + 2) × ATR(25)`. Bars are coloured by trend direction, Buy/Sell labels mark flips, and a `+` is appended to a flip when it agrees with a 186-period WMA filter. TP1 and TP2 checkmarks print when price reaches 1× and 2.5× the band from the entry bar. That's a self-contained trend system with a built-in confluence filter and two defined profit references.

**Liquidity** turns pivot highs and lows (10 left / 5 right) into resistance and support zones, with height derived from ATR(300). Each zone displays the buy/sell split of the pivot candle's volume plus a running Delta of volume traded inside it, and it retires when price closes through it. This is the most interesting module conceptually — most support/resistance tools draw a line and leave it there indefinitely. Attaching volume participation to the zone and letting it expire is a more honest model.

**Order Blocks** go further in the same direction. The wick zone of a swing candle is stored along with its volume, and every later bar trading inside the zone consumes a proportional share of that volume. The label shows remaining volume with a rating: High at ≥ 9%, Medium at ≥ 3%, Low at ≥ 2% of the 20-day average daily volume. Blocks expire when exhausted, or convert to a grey Breaker Block if that option is enabled. It's a decay model rather than a static box.

The remaining modules round things out: **ORB** for opening range breakouts with a user-defined session and UTC offset, one breakout or breakdown signal per session on a close through the range; **TrendLines** drawing time-linear wedge trendlines from consecutive pivots, extended 75 bars past the confirming pivot, with preset pivot lengths from Small (10/5) to Macro (30/15); **RMI Trend**, a momentum ribbon averaging RSI and MFI that flips colour when momentum crosses its positive and negative thresholds; **Capital Risk**, a position-sizing table taking capital, risk per trade, target RR and stop-loss percentage; and **Volume Screener**, a table of daily dollar volume (close × volume) for up to 40 symbols, tinted green or red against a "Trading Capital" threshold in millions.

## How you'd actually use it

The modular design means the sensible workflow is subtractive, not additive. Start with Trend Signals alone to establish directional bias, then layer in whichever structural module matches your style — Liquidity or Order Blocks for level-based entries, ORB if you trade session opens, TrendLines if you want diagonal structure. The screener and risk table are utilities rather than signals; they belong on a separate layout or hidden behind the single show/hide switch until you need them.

Both tables can be placed in any of nine screen positions, which matters more than it sounds — a screener table covering your price action defeats the purpose of having it.

One caveat worth stating plainly: the description itself says nothing here predicts the future. That's accurate, and it's the right framing. Every module describes what price and volume are doing. None of them tell you what to do.

## Pros and cons

**Pros.** Genuine modularity — the on/off switches make it seven tools in one slot. The volume-decay logic in Order Blocks and Liquidity is more sophisticated than the typical static-zone approach. Documented formulas mean you can reason about the maths rather than guess at it. The `+` WMA confluence filter on trend flips is a small touch that saves manual checking. Works on any symbol and timeframe, and the RMI Trend module properly credits and reuses TZack88's open-source RMI Trend Sniper under MPL 2.0 — a good sign on the author's part.

**Cons.** Seven modules in one script means a real learning curve and a settings panel that takes time to learn. Nothing here is original research — SuperTrend-style trailing bands, pivot zones, order blocks and ORB are all established concepts, assembled well rather than invented. The RMI Trend module is borrowed code, which is fine and disclosed, but it's not the author's own work. And the tool is descriptive by design: if you want entries handed to you, this won't do it.

## Who it's for

Discretionary traders who already have a process and want volume context layered onto structure — particularly those working with liquidity zones or order blocks manually. It's less suited to anyone wanting a single mechanical signal, and anyone who won't invest time learning the module interactions will find it noisy.

## FAQ

**Does it repaint?** The source material doesn't address this, so treat it as an open question and verify on your own chart before relying on any label.

**Can I run just one module?** Yes. That's the point of the Modules group.

**Does it work on crypto and forex?** The description states any symbol and timeframe.

**Is the volume meaningful on forex?** The source material doesn't address how volume is sourced per market, so judge for yourself.

## Verdict

Volume Edge is a well-organised, genuinely modular toolkit rather than a repackaged single signal. The volume-aware zone and order block decay logic gives it a real point of view, and the documentation is unusually specific about formulas and thresholds — a rarity. It loses a star for being an assembly of known concepts rather than anything novel, and for the cognitive load of seven modules in one script. If you trade structure with volume context, it's worth a look.

**Rating: ⭐⭐⭐⭐ (4/5)**

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

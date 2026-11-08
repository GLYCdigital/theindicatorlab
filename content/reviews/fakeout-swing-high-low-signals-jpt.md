---
title: "Fakeout Swing High Low Signals Jpt Review — Trend Indicator"
date: 2026-11-09T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/fakeout-swing-high-low-signals-jpt.png"
tags:
  - "fakeout swing high low signals jpt"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Fakeout & Swing High/Low Signals [JPT] review: pivot-based swing detection, ATR strength grading, and liquidity-sweep reversal markers for TradingView."
tv_script_url: "https://www.tradingview.com/script/GWBieecD-Fakeout-Swing-High-Low-Signals-JPT/"
sources: ["https://www.tradingview.com/script/GWBieecD-Fakeout-Swing-High-Low-Signals-JPT/"]
---
Most swing indicators stop at drawing a line and calling it support. Fakeout & Swing High/Low Signals [JPT] goes a step further — it tries to grade the quality of each swing and then flag the moments where price breaks a level and snaps back. That second part is the interesting bit.

## What it actually does

The script is a price-action study built around confirmed pivot highs and lows. Pivot detection uses a configurable "Pivot Strength" — the number of candles required on each side before a swing is confirmed. That means nothing prints in real time at the turning point; a swing only appears once the confirmation window has closed. This is stated plainly in the description, and it matters for how you use the tool.

Once a swing is confirmed, it isn't treated as generic. Each one is evaluated against three conditions: its distance from the previous swing relative to ATR, the percentage of the candle taken up by the upper or lower wick, and the candle body percentage. From that, the indicator classifies swings as **Strong, Normal, or Weak**. You get a visual hierarchy of which levels probably matter and which are noise.

On top of that, it draws dynamic horizontal swing levels, marks bullish and bearish breakouts when price closes beyond the latest confirmed swing, and — the headline feature — flags fake breakouts.

## The fakeout logic

A bullish fake breakout, per the documentation, occurs when price moves below a confirmed swing low but closes back above it. The bearish version is the mirror: price pokes above a swing high and closes back below. In both cases you're looking at a liquidity sweep followed by rejection.

When that happens after a confirmed sweep-and-reclaim, the indicator plots BUY or SELL markers. There are additional wick, candle-color, and ATR filters to refine these conditions, plus an optional ATR sweep-distance filter so you can ignore sweeps that barely clear the level.

The developer is explicit that these are candle-close conditions and not a guaranteed reversal. A sweep alone is not an entry — that's a refreshingly honest caveat and one you should take literally.

## How you'd actually use it

Treat the swing levels as a map of where stops likely sit. Strong swings are your higher-conviction reference points; weak ones you can probably ignore. When price breaks a level, the breakout marker tells you a close confirmed it. When price breaks and closes back inside, you get the fakeout context and, if the filters agree, a reversal marker.

From there it's a normal confluence workflow: check broader trend direction, check market structure, then decide whether the reversal signal is worth acting on. Set alerts on the breakout and reversal conditions so you're not staring at the chart. The description explicitly recommends confirming with additional price action and market structure before entry, and pairing signals with stop-loss and risk management.

## Pros and cons

**Pros**
- Swing strength grading is genuinely useful. Most pivot tools give you a binary "here's a swing" and leave the judgment to you. ATR-relative distance plus wick and body analysis is a sensible way to rank levels.
- The fakeout detection is the point of the script, and the logic is transparent: break the level, close back inside. No black box.
- The ATR sweep filter is a practical touch — it lets you filter out trivial pokes that don't represent meaningful liquidity grabs.
- Customizable labels, levels, markers, and alerts, so it can fit an existing chart rather than fighting it.

**Cons**
- Confirmation lag is unavoidable. Pivot strength means swings appear late, and reversal markers are close-based, so you're never getting the exact wick. If you want real-time turning points, this isn't that.
- The strength classification is a heuristic, not a probability. "Strong" doesn't mean "will hold" — it means the swing met certain geometric conditions.
- No performance data is offered, and none is claimed. That's honest, but it also means you have to do the work of validating the signals in your own context.
- It's a price-action tool layered on pivot logic — if you already run a market-structure or liquidity-sweep indicator, there's meaningful overlap.

## Who it's for

Discretionary price-action traders who already think in terms of swing highs, swing lows, and liquidity. If you trade breakouts and retests and want a cleaner read on which levels are worth watching, the strength grading earns its place. It also suits traders who want sweep-and-reclaim context without building it from scratch. It is not for anyone expecting a standalone system or real-time entries.

## FAQ

**Does it repaint?** Swings only appear after the Pivot Strength window completes, so they're confirmed late rather than repainting in the usual sense. The description is clear that confirmation candles are required.

**Can I use the BUY/SELL markers as entries?** The developer explicitly says no — a sweep is not an automatic entry. Use them as context alongside your own analysis and risk management.

**Does it work on any timeframe or market?** The source doesn't specify, so I won't invent one. The logic is timeframe-agnostic in principle, but you'll need to test it against your own instrument and style.

## Verdict

This is a well-scoped indicator that does one thing properly: it maps swing structure, grades it, and flags the sweeps that matter. The transparency about confirmation lag and the refusal to oversell the signals are points in its favour. It loses a star because the strength classification is heuristic and the tool overlaps with plenty of existing structure indicators — but if liquidity sweeps are central to how you read a chart, it's a solid addition.

**Rating: ⭐⭐⭐⭐ (4/5)**
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and the official TradingView script documentation. Always test indicators in a demo environment before live trading.*

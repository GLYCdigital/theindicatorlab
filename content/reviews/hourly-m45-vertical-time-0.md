---
title: "Hourly M45 Vertical Time 0 Review — Trend Indicator"
date: 2026-10-21T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/hourly-m45-vertical-time-0.png"
tags:
  - "hourly m45 vertical time 0"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Hourly + M45 Vertical Time V1.0 review: marks H1 opens, a :45 warning line, and pre-H1 swing structure. Honest look at what it does and who it suits."
sources: ["https://www.tradingview.com/script/HxO6vCmr-Hourly-M45-Vertical-Time-V1-0/"]
---
Most indicators try to tell you what price will do. This one tells you when the clock is about to turn and where the recent structure sits before it does. That's a narrower job, and it's worth being clear about it up front: **Hourly + M45 Vertical Time V1.0** is a timing and market-structure visualization tool, not a signal generator.

## What it actually does

The indicator draws vertical lines at each hourly `:00` open, with an optional timestamp. It can also draw a second line at `:45` of every hour, which in practice acts as a 15-minute heads-up that the next H1 candle is about to begin. On top of that, it plots the nearest confirmed swing high and swing low leading into each H1 open, so you can see pre-hour structure at a glance.

The author frames the design around a simple sequence: **time → warning → structure → H1**. Everything in the script maps to one of those four steps. Nothing here predicts direction, and the source is explicit that the swing feature is contextual only — it does not declare that a swing will be swept, reversed from, or traded.

## The parts that earn their place

The **M45 warning line** is the most useful idea here. Intraday traders working off hourly opens often get caught flat-footed by the turn. A visible `:45` marker with a countdown label (`15m`) or a minimal `:45` tag does one job well: it forces you to be ready before the candle flips. The four label options — full time, minimal, countdown, or none — cover the realistic preferences without clutter.

The **swing identification** is the more sophisticated piece. Two details matter and both are documented: markers are placed on the *original* swing candle, not the later candle where the pivot became confirmed, and swing strength is adjustable. Higher strength yields fewer, more significant pivots; lower strength makes it more sensitive. That's an honest description of pivot logic, and placing the marker back on the actual candle is the right call — otherwise you'd be drawing structure at a price that never traded.

**Time zone control** covers New York and Chicago with DST-aware handling. Narrow, but correct for the audience this seems built for — intraday traders on US hours.

## How you'd actually use it

The workflow is sequential. Set the time zone and format, decide whether you want the H1 line solid or dashed, turn on the `:45` warning with whichever label reads cleanly on your chart, then enable the swing markers with a search window — current hour, last 90 minutes, or last two hours. From there it's a discretionary read: you know the next H1 open is approaching, and you can see where the last confirmed swing high and low sit relative to current price.

The source offers starting settings for a 4-minute chart, which tells you something about intended use: lower intraday timeframes where an hourly boundary is a meaningful event rather than just another bar.

## Pros and cons

**Pros**
- Does one job — time awareness — and does it without adding a signal to interpret.
- The swing markers are placed correctly (on the confirming structure's origin candle).
- Genuinely configurable: line style, width, color, timestamp placement, marker shape and size.
- Two alerts included: H1 open and the M45 warning.
- DST-aware time zones remove a real source of error.

**Cons**
- Only two time zones supported. Traders outside US hours are out of luck.
- It's a visual aid. If you don't already have a model for what to do at an H1 open, the lines won't help you.
- Confirmed pivots lag by definition — the source is upfront that a swing needs candles on both sides, so the marker appears after the fact.

## Who it's for

Intraday traders who treat the hourly open as a decision point — particularly those on US sessions working lower timeframes. If your process already involves watching H1 transitions and nearby liquidity, this removes friction. If you're looking for entries, keep looking; that's not what this is.

## FAQ

**Does it repaint?** The swing markers are placed on the original pivot candle once confirmed. That's back-placement, not repainting of a live signal — the indicator doesn't claim the pivot in real time.

**Will it work on any timeframe?** The source suggests a 4-minute chart for initial use. The swing search windows are expressed in minutes, which implies intraday application.

**Can I use it outside US hours?** Only New York and Chicago are offered. Other sessions aren't covered.

## Verdict

A clean, well-scoped utility. It doesn't oversell itself, and the swing logic is more carefully thought through than most timing indicators. The narrow time zone support and its purely contextual nature keep it at four stars — it's very good at a specific, limited job, and useless outside that job.

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

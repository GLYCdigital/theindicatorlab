---
title: "Gann_Reversal_Confluence Review: Settings, Strategy & How to Use It"
date: 2026-08-16
draft: false
type: reviews
image: "/screenshots/gann-reversal-confluence.png"
tags:
  - "gann reversal confluence"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Gann_Reversal_Confluence review: tested settings, entry logic, and honest pros/cons. Is this 4-star trend reversal indicator worth adding to your toolkit?"
tv_script_url: "https://www.tradingview.com/script/Q18RGwxV-Gann-Reversal-Confluence/"
sources: ["https://www.tradingview.com/script/Q18RGwxV-Gann-Reversal-Confluence/"]
---
This one is worth a closer look precisely because it doesn't pretend to be something it isn't. Most "Gann" scripts on TradingView plot a raw bar pattern and stop there — every swing break gets a triangle, meaningful turn or noise. This indicator keeps the classic pattern detection but scores each trigger against the context, so you can see how much is lining up rather than just that a shape appeared.

## What It Actually Does

The script detects one of three classic reversal triggers, selectable in settings:

- **Swing** — price closes beyond the recent N-bar high/low.
- **Key Reversal** — a new extreme that closes back through the prior close.
- **Outside Bar** — engulfs the prior range and closes in the reversal direction.

Every raw pattern is then checked against up to five independent factors, and the results are tallied into a confluence score shown next to each signal and in the status table. It is not firing arrows indiscriminately — the entire premise is that a shape alone is a trigger, not a signal, and the score tells you how much context agrees.

## Key Features That Matter

**Confluence scoring** — This is the differentiator. Each pattern is checked against:

- **Range (ATR)** — was the bar itself big enough to matter, or just noise?
- **Volume** — did participation back the move?
- **Momentum (RSI)** — was the market actually stretched, or was this a mid-range wiggle?
- **Trend (EMA)** — is this a pullback with the trend, or a potential trend change against it? This one is shown, not scored against you.
- **Hour-ruler (optional)** — a traditional Chaldean planetary-hour tag. Descriptive only, not a validated filter.

**Cooldown** — a minimum bar gap between signals stops the same swing from re-triggering repeatedly.

**Bar-close commitment** — everything commits on bar close only. Nothing here repaints or changes after the fact.

## Settings and How to Tune Them

The settings are grouped into four sections:

- **Logic** — reversal method, swing length, close vs. wick confirmation, minimum bars between signals.
- **Confluence** — independently toggle ATR/Volume/RSI/Trend, tune each threshold, and set the minimum score required to show a signal.
- **Astro (optional)** — off by default; enables the hour-ruler tag and lets you set a location for the sunrise/sunset calc it depends on.
- **Display** — swing band, signal level lines, background highlight, confluence score label, status table (with position control), colors, and line styling.

The recommended starting point is the defaults. Watch how the confluence score moves with the setups you'd have taken anyway. When you're ready to filter, raise the minimum confluence score to hide everything below your conviction threshold — for example, set it to 3 to only see signals where 3+ factors agree.

## How to Use It

The signal level line each signal draws is a reference point for how price behaved on the next visit — not a target. The indicator is a confluence aid, meant to sit alongside your own read of the chart and risk management, not a standalone entry/exit system. It gives you the trigger and the context score; the entries and exits are on you.

## The Honest Trade-Offs

**Pros:**
- Selectivity is built in — the score filters raw patterns rather than flagging all of them
- The confluence logic is transparent and itemized, not a black box
- The astro layer is clearly labeled descriptive, not evidence
- Non-repainting — every signal is final the moment it prints

**Cons:**
- No built-in stop loss or take profit levels. This is a signal generator, not a complete system.
- During ranging markets it produces almost nothing. That's by design, but frustrating if you don't check the broader market context first.
- The hour-ruler tag may read as signal to traders who don't heed the "descriptive only" caveat.

## Who Should Use This

This is for traders who already have a direction bias and want an objective reversal trigger with a visible context score. If you're manually drawing structure and waiting for confirmations, this automates the confirmation step. It's less useful for beginners who want a "buy/sell" arrow they can blindly follow — that's not what this does.

## FAQ

**Is it a repaint?**
No. Everything commits on bar close only, and every signal is final the moment it prints.

**What does the hour-ruler do?**
It's an optional, off-by-default Chaldean planetary-hour tag layered on top of the technical factors. Treat it as a curiosity, not evidence on its own.

**Can I use it without the confluence factors?**
The ATR, Volume, RSI, and Trend checks are independently toggleable, and the minimum score is adjustable, so you control how much filtering is applied.

## Final Verdict

This script earns its place by doing one thing well: keeping the classic Gann reversal patterns but scoring each one against the context that matters, so you can see how much is lining up rather than just that a shape appeared. It's not a complete system — no stops, no targets — but as a confluence filter alongside your existing strategy, it's a defensible tool. The selectivity is its strength and its limitation. If you're patient and already have a directional framework, it sharpens the trigger step. If you're looking for a magic arrow machine, keep scrolling.

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

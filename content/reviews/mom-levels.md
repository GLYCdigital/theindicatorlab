---
title: "Mom Levels Review — Trend Indicator"
date: 2026-09-28
draft: false
type: reviews
image: "/screenshots/mom-levels.png"
tags:
  - "mom levels"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Mom Levels plots session highs and lows, the previous day's range and the daily flip line on one chart with clean, aligned labels. Honest 4-star review."
tv_script_url: "https://www.tradingview.com/script/lwMEIL8n-MoM-LEVELS/"
sources: ["https://www.tradingview.com/script/lwMEIL8n-MoM-LEVELS/"]
---
Mom Levels is a session-and-daily-level mapper. It draws the previous day's high and low, the Asia, London and New York session extremes, and a "daily flip" line — the level where the daily candle's direction changes. That's it. No signals, no oscillators, no prediction. What separates it from the pile of session-level scripts on TradingView is the labelling: every level's text sits in a single vertical column to the right of price, on a transparent background, so nothing runs through the words.

That sounds like a small thing until you've used a level indicator that scatters tags across the chart at the exact moments you're trying to read price.

## What it actually draws

The previous day's high and low (PDH/PDL) come from the prior daily candle's range and refresh at each new daily open. The three session pairs — Asia, London, New York — track their extremes live while the session is open, then freeze at session close and extend to the right as a static reference for the remainder of the day.

Each level has its own on/off toggle, its own colour, and its own line style. Text wording is editable too, so you can rename anything to match your own shorthand. You build the set you actually trade rather than accepting a fixed bundle.

The daily flip line is the more interesting piece. When the daily candle is bullish, a red line sits at the body bottom — the daily open. When it's bearish, a green line sits at the body top. It's drawn at the flip and extended until the next one, so the current flip level is always on screen. Direction is defined as close versus open, though the description notes that switching to close-versus-previous-close is a one-line change if that suits you better.

## How to use it

The workflow is straightforward. Set your session windows in exchange time — not local time — to match your broker and instrument. The defaults (1800–0000 Asia, 0700–1000 London, 1330–1600 NY) are common FX and crypto windows, but they're starting points, not universal truths.

From there it's a reference tool. Session highs and lows mark where liquidity has already been taken; the previous day's range gives you the broader frame; the flip line gives you the daily directional anchor. Whether you trade breaks, fades or continuations, those levels are the context, not the trigger.

The Padding control sets how many bars right of the live candle the label column sits. Because Pine can't pin text to the pane's right edge, the column anchors to the live bar and shifts right one bar as new candles form — so Padding is your only lever on how far out it floats. Text Align decides whether labels grow away from or toward the column.

Two alerts ship with it: New Day and Daily Flip.

## Pros and cons

**Pros**
- The aligned label column is genuinely well thought out. Nine levels, nine tags, one clean stack — no boxes, pills, or lines slicing through text.
- Per-level toggles, colours, styles and editable wording. You configure the set, not the other way round.
- Session levels freeze at close and extend right, which is exactly how a reference level should behave.
- The flip line's colour logic is inverted from what you might expect (bullish daily = red line at the open), but it's internally consistent and documented.

**Cons**
- Session times must be entered in exchange time. Get this wrong and your levels are quietly useless — there's no guard against it.
- Toggling a session off hides new lines but won't delete ones already drawn. Late changes to your setup leave stale levels on the chart until you refresh.
- It's purely a level plotter. If you want confluence scoring, trend classification or entry signals, this isn't that tool.
- Padding is a workaround for a Pine limitation, not a design choice — the column never truly pins.

## Who it's for

Intraday traders on FX, futures or crypto who already have an entry method and need session and daily context without clutter. If your strategy depends on knowing where Asia's high sits relative to London's open, or whether the daily candle has flipped, this delivers that cleanly. Swing traders using daily opens as anchors will find the flip line useful too.

It's not for anyone looking for signals or a complete system. And if you trade instruments with unusual session structures, budget time for the exchange-time setup.

## FAQ

**Does it repaint?** Session levels update live while the session is open — that's the point — then freeze at close. The flip line is drawn at the flip and extends until the next one.

**Can I change the flip definition?** Yes. The default is close versus open, and the description notes that close versus previous close is a one-line code change.

**Can I rename the labels?** Yes, the wording of every label is editable in settings.

**Why do my session levels look wrong?** Almost certainly exchange time versus local time. Check that first.

## Verdict

Mom Levels does one job and does it with unusual care. The label column alone puts it ahead of most session-level scripts, and the flip line adds a daily directional anchor that's easy to read at a glance. The trade-offs are real — exchange-time configuration, no deletion of already-drawn levels, and a Padding workaround for a Pine constraint — but none of them undermine the core function.

If you want clean session and daily levels and nothing else, this is a solid pick.

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

---
title: "Advance Range Detector Review — Trend Indicator"
date: 2026-09-30
draft: false
type: reviews
image: "/screenshots/advance-range-detector.png"
tags:
  - "advance range detector"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Advance Range Detector review: a rule-based TradingView tool that auto-detects consolidation boxes, confirms breakouts, and flags fakeouts. 4/5."
tv_script_url: "https://www.tradingview.com/script/qGaz8m1K-Advance-Range-Detector/"
sources: ["https://www.tradingview.com/script/qGaz8m1K-Advance-Range-Detector/"]
---
Most range tools ask you to draw the box. This one draws it for you, then keeps score.

## What Advance Range Detector Actually Does

Advance Range Detector is a TradingView study that automatically finds consolidations — periods where price stops trending and moves sideways inside a box — tracks them while they're alive, and flags the moment they break up or down. It also flags the moment a breakout fails and price slides straight back inside.

The pitch is straightforward: manual range drawing is subjective. Two traders look at the same chop and draw two different boxes, neither able to defend the boundaries with anything better than instinct. This indicator replaces that with a defined rule set built from volatility, touch counts, internal rotation, and price drift. Every rectangle on your chart is something the tool detected, sized, and is actively tracking — nothing hand-drawn.

That's a meaningful distinction. Most "range" indicators are just a Donchian channel with a nicer coat of paint.

## The Detection Engine Is the Real Story

At every candle, the indicator doesn't commit to one fixed lookback. It tests a base window, and optionally a double and triple length window, then keeps the longest one that satisfies every requirement. That's why you'll see consolidations of noticeably different sizes on the same chart instead of one forced uniform length — a design choice that mirrors how ranges actually form.

For each candidate window, the top and bottom boundaries come from whichever method you select: a percentile band (which uses a high percentile of highs and a mirrored percentile of lows, so one spike can't define the whole box), absolute extremes, or body extremes that ignore wicks entirely.

Then five checks must pass together before a box is accepted:

- **Tightness** — box height measured in ATR units and ranked against a rolling history of recent candidate heights on that symbol and timeframe
- **Rotation** — how many times price crosses the box's own midpoint, which stops a V-shaped reversal from being mistaken for a range
- **Touches** — top and bottom boundaries each checked separately for minimum reaches
- **Drift** — first-half average price vs. second-half, rejecting tilted structures as channels rather than ranges
- **Containment** — the percentage of closes that actually stayed between the boundaries

Only when all five pass does a qualified range exist. And even then, the box isn't drawn around the test window — its left edge walks backward bar by bar, extending until it captures where the consolidation really began, up to a limit you control.

## Provisional vs. Confirmed — a Genuinely Useful Distinction

A fresh range starts with a **dashed border** and provisional status. Only after surviving a minimum number of bars does it flip to a **solid, confirmed border**. A break during the provisional stage is deleted with no marker at all. A break after confirmation produces a labeled signal.

This matters more than it sounds. It means the tool refuses to call a range real until it's proven itself, and it refuses to spam you with signals from boxes that never established. In practice, that's the difference between a tool you can leave on a chart and one you mute after a week.

The **absorb overshoot** feature is a nice piece of engineering too: if a candle's body closes back inside the box but its wick pokes out by a small allowed amount, the boundary stretches to include the wick and the same range keeps living — rather than ending and restarting a near-identical box a few ticks away.

## The Fakeout Handling Is the Differentiator

When a confirmed breakout happens, the box locks, recolors, updates its label with the final bar count and height as a percentage of price, and places a **Breakout** marker on the triggering candle. Standard stuff.

The interesting part is **merge deviations**. If enabled, a broken range enters a brief waiting window. If price closes back inside the old boundaries before that window runs out, the breakout is treated as a fakeout: the Breakout marker is removed, a **Deviation** marker is placed at the exact extreme of the failed wick, and the original range simply continues. After any range ends, a cooldown period stops the explosive candles that often follow a real breakout from being immediately misread as a new tiny range.

That fakeout-revival logic is the kind of thing discretionary traders do in their heads and almost never see coded cleanly.

## How to Actually Use It

Use the box top as resistance and the bottom as support while the range is open. The dotted equilibrium line through the middle — the same midline used internally to count rotations — plus the 25% and 75% quartile lines help you judge whether a bounce inside the box is happening near the middle or is already stretched toward an edge.

Treat dashed boxes with caution. Give more weight to solid ones. When a Breakout marker appears, that's the indicator's read that the sideways phase ended in that direction. If a Deviation label shows up shortly after instead, the initial break was a trap and the prior range is still alive — useful for anyone who reacted to the original break too fast.

## Pros & Cons

**Pros**
- Rule-based detection removes the subjectivity that makes manual range drawing unreliable
- The five-condition filter is genuinely thorough — tightness, rotation, touches, drift, and containment all have to agree
- Provisional-to-confirmed state transition keeps noise down
- Fakeout detection with the Deviation marker is a real differentiator
- Absorb overshoot prevents the annoying range-restart churn
- Everything — windows, boundary method, touch tolerance, drift limits, breakout mode, colors — is adjustable

**Cons**
- The settings list is long, and understanding how the five conditions interact takes genuine study
- A wick-based breakout mode with a tight buffer can still produce marginal signals on volatile instruments
- No performance claims are made, and none should be assumed — this describes structure, not edge
- It defines ranges mechanically and says nothing about the wider trend, so it can't be used in isolation

## Who It's For

Discretionary traders who already trade breakouts and range reversals but want objective boundaries instead of hand-drawn ones. It suits anyone who's tired of redrawing the same box three times. It's less suited to pure systematic traders looking for an entry signal — this defines structure, and the author is explicit that it doesn't replace your judgment about trend, other levels, or risk.

## FAQ

**Does it repaint?** A provisional range can be deleted if it breaks early, and a Breakout marker can be replaced by a Deviation marker if price returns inside. Those are documented behaviors, not bugs — but they mean the chart's history isn't frozen.

**Can I use it on any market?** The settings cover instruments, timeframes, and preferences, and the tightness check ranks against that symbol's own recent history. The specifics are yours to tune.

**Does it tell me what to trade?** No. The source is clear: it's a technical analysis tool, not financial advice, and a detected range or marker describes a pattern in past and current price action, not a guarantee.

## Final Verdict

Advance Range Detector is a well-constructed piece of work. The multi-window scanning engine, the five-condition qualification system, and the fakeout-revival logic are all things most range indicators don't bother with. It's not a signal generator and it doesn't pretend to be — it's a structure engine, and a disciplined one.

The cost is complexity. You'll spend real time understanding the settings before the output makes sense, and a few of the breakout modes can still fire on marginal pokes. But if you trade consolidations and want the boxes drawn by rules instead of feelings, this earns its place on the chart.

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

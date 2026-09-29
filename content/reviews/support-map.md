---
title: "Support Map Review — Support & Resistance Indicator"
date: 2026-09-29
draft: false
type: reviews
image: "/screenshots/support-map.png"
tags:
  - "support map"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Support Map review: flat support zones and inclined support graded by how long each floor has held, not by touch count. Honest 4-star verdict."
tv_script_url: "https://www.tradingview.com/script/sYaDygcg-Support-Map/"
sources: ["https://www.tradingview.com/script/sYaDygcg-Support-Map/"]
---
Most support indicators do the same thing: find every swing low, draw a line, move on. You're left staring at fifteen horizontal levels wondering which one actually matters. Support Map takes a different angle. Instead of asking *how many times* a level was touched, it asks **how long** that floor has been respected — and whether the structure above it is opening up or closing in.

That reframe is the whole point of the tool, and it's a good one.

## What It Actually Draws

Two things. First, flat support zones. The script treats support as a band rather than a line — which matches how price actually behaves. Price reverses across a range, not at one tick. Each zone is built from a swing low, running from the wick low (the deepest point sellers reached) up to the body bottom of that candle, where buying finished and the candle closed. That's the area where demand genuinely showed up.

Two ATR-based guards keep the band sensible: it's never thinner than a set fraction of ATR and never thicker than a set multiple. Because it's ATR-normalized, the same settings carry across a large cap and a volatile small cap. Nearby swing lows get merged into one shelf with a touch count.

Second, an inclined support line — plus a dashed upper boundary.

## The Risk Grading Is The Core Idea

Here's where Support Map separates itself. Zones aren't graded by touch count. They're graded by the **span** of their touches:

- **Green / LOW risk** — first-to-last touch spans 180 bars or more
- **Amber / MID risk** — 120 bars or more
- **Red / HIGH risk** — 60 bars or more
- Below 60 bars — not drawn at all

The reasoning is sound. A floor that has held across three quarters has survived multiple earnings cycles and whatever the sector threw at it in between. Three touches in three weeks tells you almost nothing by comparison. A zone is also discarded if price closed below it between its first and last touch, with a small noise allowance.

This is the kind of grading logic that most retail support tools simply don't bother with.

## The Inclined Line Avoids A Classic Trap

Two-point trendlines are hostage to a single spike low. One bad anchor and the entire angle is wrong. Support Map fits the angle across *all* swing lows in the window instead — ignoring the worst spikes while measuring, then placing the line so roughly 20% of lows sit below it. That mirrors what your eye does when you glance at a chart and read the general direction of the lows without checking every wick.

A window only qualifies if the line starts on a real low and a minimum number of lows actually sit on it. It also has to stay within a set ATR distance below current price, so it doesn't drift off into ancient history.

The dashed upper line is fitted independently — never parallel. It's anchored from the highest high in the window and fitted through the highs that followed, sitting *on* the highs rather than through them. That detail matters. A parallel upper line makes every chart look like a healthy channel, which hides the structure you most need to see.

## Reading The Output

Labels are compact and readable. Something like `FLAT · LOW · 210d · ×3 845.5–880.8` means a flat zone, low risk, touches spanning 210 bars, three touches, band from 845.5 to 880.8. The inclined version adds whether the base and highs are rising. When highs slope down, both lines turn grey and the label adds **CONVERGING** — rising lows into falling highs is a closing structure, and the script flags it plainly.

## Inputs Worth Touching

Swing strength controls how many levels you get. Risk thresholds (180/120/60 bars) let you define your own "quarter." Merge-within helps nearby shelves combine on high-priced stocks. Minimum lows on the line defaults to 4 — drop to 3 if no inclined line appears. Lookback sits at 750 bars, roughly three years of daily data. Built for the daily chart, but it works on any timeframe; on the weekly it surfaces genuinely long-term floors.

## Pros & Cons

**Pros:**
- Duration-based risk grading is genuinely more useful than touch counting
- ATR-normalized bands travel well across instruments
- The fitted inclined line sidesteps the two-point trendline problem
- The independent (non-parallel) upper line exposes converging structures honestly
- Readable labels; no clutter

**Cons:**
- No signals — it marks where buyers appeared, nothing more
- The author's own admitted limitation: it measures how many bars a low dominated, not how much time or volume price spent at that price. A long consolidation and a sharp V-bottom can produce the same swing low. Your eye can tell them apart; the script can't
- Needs your own trend, volume and fundamental work alongside it

## Who It's For

Swing traders and positional traders working the daily or weekly chart who want context on *which* support levels are worth respecting. If you already draw your own levels and want a second opinion on durability, this fits. If you want entries and exits handed to you, it won't.

## FAQ

**Does it give buy or sell signals?** No. It marks where buyers previously appeared and does not predict.

**What timeframe is it built for?** The daily chart, though it works on any timeframe. On the weekly it finds long-term floors suited to positional work.

**What if no inclined line shows up?** Lower the minimum-lows-on-the-line input from its default of 4 down to 3.

**Can I change the risk thresholds?** Yes — the 180/120/60 bar values are adjustable to your own definition of a quarter.

## Verdict

Support Map solves a real problem: too many levels, no way to rank them. Duration-based grading is a smarter lens than touch count, and the fitted inclined line avoids the anchor-spike trap that ruins naive trendlines. It's not a signal generator, and it openly admits it can't distinguish a long consolidation from a sharp V-bottom at the same price — a limitation worth respecting rather than hiding.

For traders who build their own levels and want a durability filter on top, this earns its place. ⭐⭐⭐⭐
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

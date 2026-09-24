---
title: "Msl_Crypto_Breadth Review: Settings, Strategy & How to Use It"
date: 2026-08-31
draft: false
type: reviews
image: "/screenshots/msl-crypto-breadth.png"
tags:
  - "msl crypto breadth"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Msl_Crypto_Breadth review: a market breadth tool for crypto trend analysis. Tested settings, entry logic, pros/cons, and real alternatives."
tv_script_url: "https://www.tradingview.com/script/2ARcraNQ-MSL-Crypto-Breadth/"
sources: ["https://www.tradingview.com/script/2ARcraNQ-MSL-Crypto-Breadth/"]
---
Most crypto "breadth" indicators are repackaged moving averages with a fancy name. This one is not that. It measures the internal strength of a market by aggregating participation across a basket of coins, then plotting that reading against the reference symbol. If you have ever watched Bitcoin rally while altcoins bleed, you already know why the distinction matters.

## What This Indicator Actually Does

The script watches a basket of 20 coins at once and answers a question a single chart cannot: out of those 20, how many are actually taking part in the move on screen right now. That answer changes what the same candle means. If Bitcoin gains five percent and 17 of the 20 coins gain with it, the move has something under it. If Bitcoin gains the same five percent while only 3 coins follow, one name is carrying everything and the rest of the market has already turned away. On a price chart those two days look identical.

Two lines do the work. **Participation** is a state: how many coins of the basket are trading above their own moving average, drawn as a percentage from 0 to 100. It moves only when a member crosses its average, which is a large event, so the line is slow and honest. **Pressure** reacts on every bar, counting how many coins closed up against how many closed down and accumulating that difference over time, so it turns while participation is still standing still.

The indicator then watches the reference symbol and participation together. While they move the same way, nothing is drawn. When they split and go opposite ways, the stretch of time between them is shaded red or green and stays shaded until they come back together. Red means price is being pulled up while fewer and fewer coins follow it. Green means price is falling while more and more coins are quietly recovering underneath it.

## Key Features That Set It Apart

The standout feature is **divergence detection between the reference and the basket**. One window, two measurements, no pivots: the reference must travel at least the configured percentage across the window while participation moves the other way by at least the configured number of points. A vertical line marks the bar the disagreement opened and a band runs until the pair comes back together.

The event is measured on participation alone. The pressure line takes no part in it — hide it and not one band, glyph or alert changes. Participation sits on a fixed scale where ten points has a stated meaning: two members out of twenty changing sides. Pressure is normalised against its own recent range, where ten points would mean nothing statable. Read together, a band with pressure agreeing is a warning confirmed twice; a band against it is the narrow kind that more often dissolves.

The **basket is fully configurable** — twenty symbol slots, and any symbol your plan can open works. The basket does not have to be crypto, so the same engine measures a sector, an index or a watchlist. The basket does not change with the chart, so the reading is about the market rather than the instrument in front of you.

Agreement produces nothing at all. Both sides moving up together, or both down, is what a healthy market looks like, and it is exactly what closes an open band. A move too small to clear either threshold does nothing either, so an open band is never cancelled by noise.

## Settings and How to Tune Them

**Core.** Basket Timeframe — empty follows the chart, and a higher setting keeps a slow reading on a fast chart. MA Length — a long-term reading versus a swing one. MA Type across SMA, EMA, WMA and RMA. Coins Counted, how many of the twenty slots take part. Minimum Live Feeds, the smallest sample that may be published at all.

**Basket.** Twenty symbol slots.

**Divergence.** Reference Symbol, Comparison Window, Reference Move percent and Breadth Gap Points — the two thresholds that define an event.

**Visuals.** The second line and its swing window; how events are drawn, as line and band, band only, line only or glyph only; the arrow on the edge; on-chart explanations and how many are kept; whether events show in the pane, on the chart or both; four colours.

**Dashboard.** Table on or off, its corner out of eight, and the text size.

## How to Actually Use It

The script's own usage notes map participation states to position sizing, not to entries:

- **Participation above 50 and rising** — the market is broad, most of the basket holds its average. The only state where adding makes sense.
- **Participation between 30 and 50** — the move is carried by a few names. Half size, closer targets.
- **Participation below 30** — breakouts in the basket mostly fail. Stand aside, or trade the reference symbol alone.
- **Participation above 80** — everybody is already in, advances are crowded. Not a place to open; reduce and tighten the stop.
- **A red band opens** — the reference is being carried while participation leaks away. Stop adding, protect what is open. A warning, not an exit, and it can run for weeks.
- **A green band opens while participation is below 20** — the reference is falling while more members repair underneath it. Prepare, do not enter yet; this stage can last weeks.
- **Participation then crosses 50 upward** — the repair is confirmed by the state, not only by pressure. The entry window of the reversal sequence, late by design and verified by design.
- **A band closes** — the pair moved the same way again, the disagreement is resolved and the warning is lifted.
- **Participation crosses 50 downward** — most of the basket has lost its average. The last and bluntest exit reason.

Five alerts cover this without watching the screen: participation crossing above and below half, the two divergence conditions, and the bar an open disagreement closes.

## Pros & Cons

**Pros:**
- Divergence detection is built in and measured on a scale with a stated meaning, rather than left to interpretation
- Multi-asset aggregation that excludes silent members instead of counting them as weakness
- The basket is configurable and need not be crypto
- Nothing is drawn against a candle or at a price level, so the output cannot be mistaken for an entry signal

**Cons:**
- Steeper learning curve than a single-line trend indicator
- Divergences almost never fire on H1, because a genuine disagreement between a whole basket and Bitcoin inside a day is rare; divergence is a 4h and daily tool
- Members are read through the chart, so their history begins where the chart history begins — a 200 length average needs 200 chart bars before the first reading exists
- Breadth describes the crowd, not the next bar

## Who It's For

This is for traders who already have an entry system and want a second opinion on whether a signal deserves full size, half size, or nothing at all. It does not tell you where to buy. It tells you whether the trade your own system just found is backed by a broad market or carried by one name. Day traders working intraday will find the divergence component largely silent.

## Alternatives Worth Considering

- **Crypto Market Breadth by Fadly** — free and simpler, but without paired open-and-close divergence events.
- **Total Crypto Market Cap Overlay** — not a breadth tool, but useful if you only trade BTC and ETH.
- **BTC Dominance Indicator** — complements a breadth reading; use both for a fuller market picture.

## FAQ

**Does it work for stocks?**
Yes. Any symbol your plan can open works as a basket slot, and the basket does not have to be crypto — the same engine measures a sector, an index or a watchlist.

**Does it repaint?**
Not stated in the source material. What is stated: each member is requested on the selected timeframe with lookahead disabled, and its moving average is computed inside its own context on its own data. A member that has not returned data contributes nothing — it leaves both sides of the division rather than being counted as a coin below its average. No share is published at all until a minimum number of members have answered.

**Does it give entry signals?**
No. Nothing is drawn against a candle and nothing sits at a price level, and the indicator produces no entries. A shape placed on a bar is read as an entry whatever the description says.

## Final Verdict

This is a breadth tool built with unusual care about what a breadth reading can honestly claim. The exclusion of silent members, the minimum sample gate before any percentage is published, and the detrending of the cumulative count are the details that separate a real internals reading from a decorative one. The divergence event is deliberately narrow — measured on participation alone, on a fixed scale where ten points means two members out of twenty — and it produces no entries, only context.

It is not a standalone system. Low participation is not a reason to short on its own, and a thin market can stay thin for weeks while price grinds higher on two names. Used as a sizing and confirmation layer on top of your own signals, it does the one thing it promises: it tells you when a market is lying about its strength, with a count anyone can check.

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

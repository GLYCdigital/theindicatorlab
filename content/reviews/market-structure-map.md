---
title: "Market Structure Map Review — Market Structure Indicator"
date: 2026-11-16T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/market-structure-map.png"
tags:
  - "market structure map"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Market Structure Map [JOAT] review: two-scale swing structure, BOS/CHoCH events with data tags, and a premium/discount dealing range. No signals."
tv_script_url: "https://www.tradingview.com/script/KGxkpkNv-Market-Structure-Map-JOAT/"
sources: ["https://www.tradingview.com/script/KGxkpkNv-Market-Structure-Map-JOAT/"]
---
Market Structure Map is a structure reader, not a signal engine. It tracks where highs and lows are made and broken at two scales, labels every break with the numbers that produced it, and turns the current leg into a dealing range split into premium and discount. The author is explicit that it gives no entries, targets or buy/sell calls. What it does instead is quantify structure — and that is a more useful thing than it sounds.

## Two structure scales, one bias each

The indicator runs two pivot engines in parallel. Swing pivots define the main structure, using a 12-bar dominance length by default; internal pivots use a 4-bar length for the small legs inside it. Each has its own BOS/CHoCH state machine and its own bias, which is why the dashboard's Internal row can disagree with the Structure row — the accent colour flags exactly that, and it is a decent visual shorthand for a pullback inside a larger leg.

Internal structure is computed continuously but only drawn when you switch it on. That is the right default for fast charts, where a 1m or 5m screen would otherwise be buried in lines.

## What is actually printed on the chart

Every confirmed swing gets a tag — H / HH / LH above the candle in the bear colour, L / HL / LL below in the bull colour — with its price attached. Breaks are drawn as lines from the broken swing to the break bar, carrying a data tag with the break level, the leg size in ATR, the leg size in points and the leg duration in bars. The tooltip adds how far the break close sat beyond the level.

Two details stand out. First, CHoCH is set apart by line style and weight — dashed line, bold word — rather than colour alone, so a change of character never reads as a continuation break at a glance. Second, state is encoded by opacity: the freshest event glows, older events dim, and a break that price later closes back through turns grey and dotted and is labelled "failed." That last one is the most honest feature in the script. Most structure tools quietly leave stale breaks on the chart as if they still mattered.

Only closes count as breaks. A wick through a swing high and back is not an event, which will annoy anyone who trades wick sweeps and please anyone who has been faked out by them.

## The dealing range

The range runs from the last swing low to the last swing high, trailed forward to any newer extreme. The upper half is tinted in the bear colour, the lower half in the bull colour, both fading toward a dotted equilibrium. The close's position is a plain percentage: 0% at the range low, 100% at the range high.

The right edge reads the whole thing back as short data tags: STRONG / WEAK HIGH and LOW with prices, RANGE size in points and ATR, EQ with price, PREMIUM and DISCOUNT halves, and a close-position tag like "close 68% · premium." Each tag is capped at 28 characters to fit the margin, with the detail pushed into tooltips — band prices, distance from equilibrium in ATR. The strong/weak naming follows standard practice: the extreme the latest break leg started from is the one structure defends; the opposite extreme is the one it ran to.

An optional OTE band marks the 62–79% retracement of the range from the latest extreme. It is a zone to read, not a trigger, and it is off by default.

## Pros and cons

**Pros**
- The event tags carry real information — ATR, points, bars — not just a letter. You can judge whether a break was a serious leg or a grind.
- Failed breaks are marked and greyed rather than silently abandoned.
- Non-repainting by construction: pivots confirm only after the bars to their right close, so tags do not move once placed.
- Sensible clutter control: internal structure off by default and capped at four events when on; swing events capped and retired oldest-first; the latest swing CHoCH is always kept.
- Every dashboard row is also drawn on the chart, so the panel is a summary rather than a second, separate interface.

**Cons**
- Every pivot tag appears a full pivot length after the high or low it marks. That is the price of non-repainting, but it means the labels are lagging by design.
- ATR-based leg and range sizes change meaning across timeframes, so the numbers are not comparable between charts.
- Structure starts from the first pivots inside available history — on a free account that is roughly 5,000 bars, so older events are retired to stay within drawing limits.
- It is a reading tool. If you want alerts to do the thinking, this is not that.

## Who it is for

Discretionary price-action traders who already think in terms of BOS, CHoCH and premium/discount, and who want those concepts measured rather than eyeballed. It suits multi-timeframe work — swing structure for bias, internal structure for timing — and it suits anyone who wants to see whether a break was backed by a meaningful leg or was noise. It is not for traders looking for entries, and it will frustrate anyone who refuses to wait for pivot confirmation.

## FAQ

**Does it repaint?** No. Pivots, events and historical tags are placed on confirmed bars only. The right-edge tags, the range and the dashboard do follow the live bar.

**Does it give buy or sell signals?** No. It draws structure, ranges and zones describing past price behaviour, and the author states plainly that these are not predictions.

**Why did my swing tag appear late?** Because a pivot only counts once the pivot length has closed to its right. With the default swing length, that is a delay by design.

**Can I use it on a 1-minute chart?** Nothing stops you, but internal structure is off by default partly for that reason, and ATR-based figures shift meaning across timeframes.

## Verdict

Four stars. The core idea — structure as a measurable object rather than a hand-drawn sketch — is executed with unusual care: data-carrying event tags, failed breaks that admit failure, and a dealing range that reads back as actual numbers. It loses a star because the confirmation lag is structural, the ATR figures are timeframe-dependent, and it deliberately stops short of telling you what to do with any of it. If you already read structure by eye and want a second, quantified opinion, this earns its place on the chart. If you want signals, keep looking.
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

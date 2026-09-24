---
title: "Tail_Range_Percentile_Radar_Pineify Review: Settings, Strategy & How to Use It"
date: 2026-09-11
draft: false
type: reviews
image: "/screenshots/tail-range-percentile-radar-pineify.png"
tags:
  - "tail range percentile radar pineify"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Tail_Range_Percentile_Radar_Pineify review: how this tail-range percentile trend tool works, tested settings, entry logic, and who it's actually for."
tv_script_url: "https://www.tradingview.com/script/NBAp559r-Tail-Range-Percentile-Radar-Pineify/"
sources: ["https://www.tradingview.com/script/NBAp559r-Tail-Range-Percentile-Radar-Pineify/"]
---
Most "trend" indicators are just another moving average with a fresh coat of paint. This one isn't. Tail Range Percentile Radar [Pineify] takes a genuinely different angle: instead of smoothing price, it separates candle rarity from candle shape. Four aligned scan lanes compare true range, real body, upper wick and lower wick against their own recent histories. That sounds like jargon until you read the lanes — then it becomes a compact explanation of whether a bar's movement is unusual, and whether that movement lives in the body or the wicks.

## What It Actually Measures

The core idea is percentile ranking of candle components, not a single volatility score. Rather than asking "is price above the average," it asks two questions: is this component unusual, and does it occupy enough of this candle to matter?

True range is the largest of high-low, the distance from high to the previous close, and the distance from low to the previous close. Body is absolute close minus open; wicks are the distances from the body edges to high and low. Each magnitude is rounded to the symbol's tick size, then ranked against its own prior-only population.

The design deliberately rejects averaging all four ranks. A single blended score would let a large body mask an exceptional wick. Retaining four lanes costs screen space but preserves the reason for each event. This is a regime/context tool, not a signal generator, and treating it as the latter will get you chopped up.

## Key Features That Stand Out

- **Four prior-only percentile populations** with explicit zero handling, so an extreme cannot alter its own baseline.
- **Independent range and share-qualified body or wick flags** — rarity and geometric relevance are separate conditions.
- **Tie-aware ranking** using half-weight ties, so repeated tick sizes aren't treated as distinct observations.
- **A confirmed anatomy strip, close-only alerts and optional statistics.**

The percentile approach is the real differentiator. An ATR multiple measures distance from an average, but the same multiple can occur in very different distributions. Fixed ATR multipliers break down across regimes; separate ranks preserve anatomy that one volatility score hides.

## Settings and How to Tune Them

The script's published design starting points are N=200, Q=95, wick share=20% and body share=55%. These are starting points, not optimized settings.

- **Lookback length (N):** Shorter N responds sooner but uses fewer comparisons.
- **Percentile threshold (Q):** Higher Q rejects more bars. A flag needs rank at or above Q.
- **Body and wick shares:** Body and wick flags additionally need their configured share of high-low. Higher shares reject more bars. A zero high-low gives zero shares.
- **Statistics window:** Defaults to 100 chart bars. Its rates use eligible closed bars, with sample coverage shown; overlapping flags can sum above 100%.
- **Display options:** Guides, tips, strip, table and four colors are configurable.

Note that rank 95 is a sample comparison, not a 5% future probability, and it does not measure how far beyond history a new maximum lies.

## How to Read It

Read the lanes from top to bottom: gold TR, purple body, orange upper wick, teal lower wick. Each uses its own zero baseline and equal height for 0-100; stacked positions are not a shared numeric axis. Dashed rails mark Q, vivid columns show qualifying components and dots confirm them at close. Use the table or Data Window for actual ranks and anatomy codes. The diamond strip marks the selected closed-bar type.

The displayed type prioritizes dual tail, upper tail, lower tail, directional body, gap-led range, then range only. Gap-led requires extreme TR and at least 35% of TR outside high-low. Component flags remain independent of this display priority.

## How to Use It

The logic that holds up:

1. **Watch for a qualifying lane.** An upper-tail event identifies an unusually large upper wick — not proven selling pressure or a short entry. A lower tail is equally descriptive.
2. **Compare context.** A tail inside ordinary TR and a range event dominated by a body answer different anatomy questions.
3. **Review clusters on the chart.** Clusters invite chart review but do not establish reversal odds.
4. **Keep decisions independent.** There is no entry, exit, profitability or reversal model here.

The trap is reading a flag as a directional call. It describes anatomy, not the next move. Pair it with your own directional method and it becomes a useful context layer.

## Pros & Cons

**Pros:**
- Separates rarity from shape instead of collapsing both into one score
- Prior-only, tie-aware populations with explicit zero handling
- Zero suppression prevents absent wicks from becoming exceptional merely because a reference sample contains many zeros
- Complements momentum tools instead of duplicating them

**Cons:**
- No directional bias on its own — you must supply the trend filter
- Four lanes cost screen space
- Takes practice to interpret fluently; not plug-and-play
- Requires at least N valid prior observations plus previous-close coverage

## Who It's For

Discretionary traders who already have a directional method and want a context layer describing observed tail volatility. It is not for anyone wanting a standalone buy/sell arrow, and it is not a reversal model.

## Alternatives

If you want a pure volatility-expansion signal with clearer triggers, a well-tuned Squeeze Momentum or TTM Squeeze does similar regime work. For straightforward trend following, SuperTrend or a Hull MA is more direct. The prior-only, tie-aware four-population comparison with geometric qualification is the differentiator here — if that concept clicks for you, this is worth the install over the alternatives.

## FAQ

**Does it repaint?** Live ranks, shading and table type can change intrabar; tips, strip and alerts require close. Choose once per bar close.

**Can I use it alone?** Not recommended. It's a context tool; add a directional filter.

**What data does it need?** Standard OHLC charts. Synthetic candles change the meaning of anatomy. No volume or order-flow data is used.

**How many alerts will I get?** Alerts apply to every qualifying closed bar, so consecutive bars can each alert and dual tails can trigger both tail alerts.

**Is it worth the install?** Yes, if you treat it as a candle-anatomy radar rather than a signal generator.

## Final Verdict

Tail Range Percentile Radar [Pineify] does one thing well: it distinguishes unusual total movement from unusual candle parts while keeping rarity and shape separate. It loses a star because it demands a companion directional tool and takes real practice to read — it won't hand anyone a signal. For traders who want a compact explanation of observed tail volatility, it's a solid add.

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

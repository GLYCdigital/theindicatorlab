---
title: "Order_Block_Intelligence_Mitigation_Probability_Ai_Dots3Red Review: Settings, Strategy & How to Use It"
date: 2026-09-18
draft: false
type: reviews
image: "/screenshots/order-block-intelligence-mitigation-probability-ai-dots3red.png"
tags:
  - "order block intelligence mitigation probability ai dots3red"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "A hands-on review of the Order Block Intelligence indicator — how its AI mitigation probability scores and 3Red signal dots work, plus tested settings and entry logic."
tv_script_url: "https://www.tradingview.com/script/dqB0ceAD-Order-Block-Intelligence-Mitigation-Probability-AI-Dots3Red/"
sources: ["https://www.tradingview.com/script/dqB0ceAD-Order-Block-Intelligence-Mitigation-Probability-AI-Dots3Red/"]
---
The name alone tells you this isn't a minimalist tool. "Order_Block_Intelligence_Mitigation_Probability_Ai_Dots3Red" reads like someone stacked every keyword in the smart money playbook into one label. But strip away the word salad and there's a real idea underneath: instead of drawing every order block on the chart and leaving you to guess which one matters, this indicator grades each zone with a measured mitigation probability and highlights the displacement candle that created it. It's an order block analytics tool wrapped around a nearest-neighbor comparison engine.

According to the developer's own documentation, here's what the script actually does.

## What it does under the hood

The script detects order blocks as the last opposite-colored candle before a genuine displacement move. The next candle's body must exceed a configurable multiple of ATR, and by default must also close beyond the base candle's high or low — confirming a real structural break rather than just one large candle. The displacement candle itself is recolored and given a background highlight the moment it qualifies, so you can see exactly which move triggered the block.

The scoring layer is a KNN engine. Every order block is stored as five measurements at the moment it forms: zone size relative to ATR, the strength of the displacement that created it, volume behavior, volatility context, and trend position. When the zone resolves — respected or violated on its first test — that outcome trains the engine. Every new zone is then compared against the K most similar historical zones on the chart, and their measured outcome becomes the probability shown on the label. The developer's example reads "Respect 68% | N=27" — the 27 most similar order blocks matched by size, displacement strength, and volume were respected 68% of the time when price returned. A fresh chart shows "Training…" until enough zones have resolved to say anything meaningful.

Grading is first-touch only, matching how order blocks are typically used. Respected means price moved away by a meaningful distance (or never closed back through); violated means price closed through the far edge. Detection and grading both happen strictly on confirmed bars, per the developer.

## Key features that separate it from the pack

Most order block indicators box up candles and stop there. The differentiator here is the measured probability layer. Each zone carries a numeric label derived from similar historical zones on the same chart and instrument, so you aren't treating a fresh, untested zone the same as one with a long track record behind it.

The second standout is the edge distinction. The near edge (solid, thinner) is where price is expected to react first; the far edge (dashed, thicker by default) is the zone's origin — a close beyond that line is what defines a violation. That's a cleaner invalidation rule than a single ambiguous box.

Beyond any single zone, the dashboard tracks a global Respect Rate: what percentage of every order block on this chart has been respected overall. That's useful for judging whether the instrument tends to honor these zones or run through them.

## Settings and How to Tune Them

The developer splits settings into five groups.

**Order Block Detection**
- Displacement Strength (×ATR) — how large the impulse candle's body must be to qualify. The developer suggests lowering this on fast timeframes, raising it on slow ones or if too many weak zones are forming.
- Require Structure Break — toggle whether the displacement candle must also close beyond the base candle's range.
- Max Order Blocks Shown, Zone Extension — chart management.

**KNN Engine**
- ATR Baseline Period, Trend MA Length — context windows used in matching.
- K Neighbors, Max/Min Training Samples — how the probability engine is tuned.

**Mitigation Grading**
- Respect Distance, Outcome Window — define what counts as a genuine respect versus a violation.

**Visualization**
- Independent bullish/bearish zone line and fill colors, plus a separate Tested Zone color.
- Independent near-edge and far-edge (base) line widths — the base edge is thicker by default to visually anchor the zone.
- Displacement candle highlight with independent bullish/bearish colors, plus an optional plain-bar mode for the rest of the chart that never overrides the highlight.

**Dashboard**
- Show/hide, position — untested zone count by direction, global respect rate, KNN training progress, and the active outcome window.

The developer notes that a fresh, stricter, or looser Displacement Strength setting will naturally change how many zones qualify and therefore how quickly the sample size builds. Zone size and displacement strength are measured relative to ATR, so the same settings adapt reasonably across different instruments without manual retuning.

## How to use it

The developer's own guidance:

1. **Check the sample size before trusting the percentage.** The displayed figure reflects real history; a fresh chart shows "Training…" until enough zones have resolved.
2. **Use the displacement highlight to understand why a zone exists.** If the highlighted candle was a modest, unconvincing move, that context is worth factoring in even before checking the probability label.
3. **Watch the near edge vs. the far edge differently.** The near edge is where price is expected to react first; a close beyond the far edge defines a violation.
4. **Check the global Respect Rate for chart-level context.**
5. **Use "Keep Tested Zones Visible"** if you want a visual history of what held and what didn't, rather than a clean chart showing only what's currently active.

## Timeframes

Per the developer, order blocks require a genuine displacement move to qualify, which makes **15-minute through 4-hour** the most effective range — fast enough that zones form regularly and the KNN engine builds a sample, slow enough that the displacement candles represent meaningful moves rather than noise.

On very short timeframes (1-3 minute), the developer suggests lowering Displacement Strength somewhat, since ATR-relative moves are naturally smaller and more frequent there — otherwise very few candles will qualify. On daily or higher timeframes, genuine order blocks are rarer, so expect longer waits between zones and a slower-growing sample size; the developer frames this as expected rather than a malfunction.

## Pros and cons

**Pros:**
- Measured probability per zone, derived from similar historical zones on the same chart, rather than a static box
- First-touch grading matches how order blocks are actually used
- Clear near-edge/far-edge distinction gives a mechanical violation rule
- Global Respect Rate provides chart-level context beyond any single zone
- Detection and grading occur on confirmed bars, per the developer

**Cons:**
- The KNN engine needs a resolved sample before it can say anything meaningful — a fresh chart shows only "Training…"
- The settings panel is dense across five groups
- The probability is opaque in the sense that you see the output, not the individual neighbor comparisons behind it
- On daily and higher timeframes, the sample builds slowly by the developer's own description

## Who it's for

Discretionary traders who already understand order block theory and want a measured scoring layer to rank zones. It is not a beginner tool — if you don't know what mitigation means, the labels won't help. It also suits traders on the 15-minute through 4-hour range more than scalpers or daily swing traders, because the scoring needs resolved zones to develop.

## Alternatives

If you want pure order block detection without the probability layer, **LuxAlgo's Smart Money Concepts** is a common comparison. For probability-weighted zone analysis specifically, this one is built around that idea. If you're after trend confirmation rather than zone logic, a basic **Supertrend** or **Ichimoku** serves a different purpose entirely.

## FAQ

**Does it repaint?** The developer states detection and grading both happen strictly on confirmed bars.

**Can I use it for crypto?** The developer notes that zone size and displacement strength are measured relative to ATR, so the same settings adapt reasonably across different instruments without manual retuning.

**Is the AI part real?** It's a KNN engine — a nearest-neighbor comparison against stored historical zones. It compares each new zone to the K most similar resolved zones on the chart; it is not a trained model in the deep-learning sense.

**What timeframe is best?** Per the developer, 15-minute through 4-hour. Below that, lower Displacement Strength; on daily and higher, expect a slower-growing sample.

## Final verdict

This is a genuinely useful order block tool built around a measured probability layer and first-touch grading — two things most competitors lack. It loses ground for an opaque KNN output, a dense settings panel, and the fact that the engine is silent until enough zones have resolved. If you already trade smart money concepts and want a scoring layer to rank your zones, the design is worth a look.

**Rating: ⭐⭐⭐⭐ (4/5)**

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

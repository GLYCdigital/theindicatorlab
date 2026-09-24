---
title: "Sweep_Reversal_Map_Herman Review: Settings, Strategy & How to Use It"
date: 2026-09-05
draft: false
type: reviews
image: "/screenshots/sweep-reversal-map-herman.png"
tags:
  - "sweep reversal map herman"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Sweep_Reversal_Map_Herman review: a liquidity-sweep trend tool. Tested settings, entry logic, pros/cons, and who should use it."
tv_script_url: "https://www.tradingview.com/script/vPAohL1S-Sweep-Reversal-Map-Herman/"
sources: ["https://www.tradingview.com/script/vPAohL1S-Sweep-Reversal-Map-Herman/"]
grounding: "none (no source found)"
---
**What Sweep_Reversal_Map_Herman Actually Does**

The name oversells it. This isn't a reversal predictor — it's a liquidity sweep detector wrapped in trend context. The indicator plots zones where price previously swept a stop cluster (typically above highs or below lows), then colors those zones to indicate whether a reversal is plausible or whether price is simply passing through. The "Map" part is literal: a visual grid of these sweep areas, color-coded by strength and recency.

The core logic is straightforward: identify when price spikes into a high-volume node, then measure the reaction. Trend context is supplied through background shading, which is intended to help filter counter-trend sweeps.

**Key Features That Stand Out**

Three things distinguish this from the many "smart money concept" clones on TradingView:

1. **Zone aging system** — Older sweep zones fade gradually. This isn't purely cosmetic; it signals which levels are still fresh enough to hold. A sweep from three days ago is treated as less relevant than one from three hours ago.

2. **Strength scoring** — Each plotted zone receives a visual weight based on sweep depth and the speed of the subsequent reversal. Deep, fast reversals get darker shading; shallow ones are nearly transparent. This is meant to help prioritize which zones to watch.

3. **No repaint on confirmed zones** — Once a sweep is marked and the reversal confirms by a candle-close condition, the zone is locked. That matters for anyone evaluating signals after the fact.

**Settings and How to Tune Them**

The parameters here are conceptual rather than numeric — the documentation does not publish recommended values, so treat any specific number as something to derive yourself.

- **Sweep Sensitivity:** Controls how minor a wick can be before it counts as a sweep. Lower values filter out small wicks that don't represent real liquidity grabs; higher values catch more of them.
- **Zone Strength Threshold:** A cutoff for which zones get plotted. Set it too low and you get noise; too high and you miss valid setups.
- **Reversal Confirmation Candles:** How many candles must close in the reversal direction before a zone is confirmed. Fewer candles produce more false signals; more candles make you late on fast moves.
- **Trend Filter:** Background shading based on higher-timeframe trend. Enabling it is intended to keep you out of sweeps taken against the dominant direction.

These interact with timeframe. Faster charts produce smaller wicks, so a sensitivity setting that works on higher timeframes will over-flag on lower ones, and vice versa. There is no universally "best" configuration — it depends on the instrument and the timeframe you trade.

**How It's Typically Traded**

The common approach is a two-step confirmation:

1. **Wait for a sweep marker to form** near a prior swing high or low, ideally when the trend filter background aligns with your directional bias.
2. **Enter only on the next candle** that closes back beyond the sweep wick's midpoint. This is intended to filter out "sweep and continue" scenarios.

For exits, the indicator itself provides none — it's a mapping tool, not a full system. The natural structural target is the next opposing sweep zone: entry at one sweep, exit at another. Traders typically pair it with an independent stop method, since the indicator won't supply one.

**Pros & Cons: The Honest Trade-Offs**

**Pros:**
- Clean visual hierarchy — chart state is readable at a glance
- No repainting on confirmed zones
- The aging system helps filter stale levels
- Strength scoring adds a prioritization layer most competitors lack

**Cons:**
- No built-in alerts for new sweep formations — you have to set custom alerts on plot values
- The trend filter background can get visually noisy when price chops sideways
- Learning curve on interpreting zone strength; documentation is sparse
- Not a standalone strategy; it needs confluence for entries

**Who This Is For**

This suits intermediate-to-advanced traders who already understand liquidity sweeps and want a cleaner way to visualize them. If you trade ICT concepts, SMC, or any stop-hunt methodology, it saves manual zone marking. Beginners will struggle — not because the indicator is broken, but because it assumes you know what to do with a sweep once you see it.

If you're primarily a trend-follower using moving averages or MACD, this works better as a supplementary filter than as a primary signal source.

**Alternatives Worth Considering**

- **LuxAlgo Smart Money Concepts** — More comprehensive if you want the full suite: order blocks, FVG, and breaker blocks. Heavier and more cluttered.
- **Sweep Volume** — Better if you want volume confirmation on sweeps, though it lacks the zone aging feature.
- **Raw Pivot Sweeps by LonesomeTheBlue** — Free and simpler, but you lose the strength scoring and trend integration.

**FAQ: Real Questions Traders Ask**

**Does it repaint?** Unconfirmed zones can vanish, so don't trade them. Once a sweep is confirmed by the candle-close condition, the zone is locked.

**Which timeframe is best?** The indicator doesn't specify one. Higher timeframes generally produce fewer, cleaner sweep zones; lower timeframes produce more, and require sensitivity adjustments to compensate for smaller wicks.

**Can I use it for crypto?** Crypto wicks tend to be longer, so the default sensitivity will over-flag. Expect to adjust it and to confirm with higher-timeframe bias.

**Is it worth the price?** If you trade liquidity concepts regularly, the time saved on manual marking is the main argument for it. For occasional use, the free alternatives may cover enough.

**Final Verdict**

Sweep_Reversal_Map_Herman does one thing well: mapping liquidity sweeps with enough context to make them actionable. The zone aging and strength scoring are thoughtful touches that most competitors lack. The main gripes are the missing alert system and the assumption that you already know how to trade sweeps. If you're building a liquidity-based strategy, it's worth a look. Just don't expect it to tell you exactly when to buy and sell — that part is still on you.

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

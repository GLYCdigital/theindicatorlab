---
title: "Order Block Strength Review — Market Structure Indicator"
date: 2026-10-23T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/order-block-strength.png"
tags:
  - "order block strength"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Order Block Strength scores every bullish and bearish order block from 0% to 100% using volume, displacement and FVG — a clearer way to rank supply and demand zones."
tv_script_url: "https://www.tradingview.com/script/6Nsh9Mdm-Order-Block-Strength/"
sources: ["https://www.tradingview.com/script/6Nsh9Mdm-Order-Block-Strength/"]
---
Most order block indicators have the same flaw: they draw every zone the same way. A block formed on a quiet drift gets the same box as one left behind by a violent, high-volume break — and the trader is left to eyeball which one deserves attention. Order Block Strength tries to fix that by scoring each zone numerically at the moment it forms. It's a study, not a strategy, and it's built around market structure rather than arbitrary support/resistance levels.

## What the indicator actually does

The detection logic is structural. The indicator confirms swing highs and lows using pivots, with a "Swing Length" input controlling how many bars on each side are required. A bullish break of structure is registered when price closes above the latest swing high. At that point the script searches back to the swing point and picks the lowest bearish candle in that range as the bullish order block — falling back to the lowest candle if no bearish one exists. Bearish blocks mirror this: a close below the latest swing low, then the highest bullish candle before the move.

That's a reasonable, defensible definition of an order block. Nothing exotic, but it's the correct starting point. The interesting part is what happens next.

## The strength score

Each block is scored at formation on a 0–100% scale, built from three weighted components:

- **Volume** (default weight 35%): the order block candle's volume relative to its moving average. Reaching a ratio of 2x average, adjustable, awards the full score.
- **Displacement** (default weight 40%): how far price travelled away from the block on the breaking candle, measured in ATR. A 3 ATR move, adjustable, gives full marks.
- **Fair Value Gap** (default weight 25%): whether the impulse after the block left an imbalance.

The weights are adjustable, which is the right call — different instruments produce different volume and volatility profiles, and what counts as a meaningful displacement on one market won't on another. The result appears on the label, e.g. "Bull OB 82%", and stronger blocks are drawn with a more opaque box. That visual gradient is a small touch that does a lot of work: you can rank zones at a glance without reading every number.

One honest limitation: this is a snapshot score. It measures the quality of the candle that created the block, not the probability that price will react to it later. Those aren't the same thing, and the indicator doesn't pretend otherwise — but it's worth being clear about.

## Retests and mitigation

This is where the tool earns its place. Every time price returns into an active block, the score is reduced (default 15% per retest) and the label updates with the current score and retest count. A block that gets tapped repeatedly degrades in front of you, which is a more realistic model of how these zones behave than treating them as permanent lines.

Mitigation is handled cleanly: a block is considered mitigated when price closes beyond it, or wicks beyond it if "Wick" is selected. Mitigated blocks are removed by default. If you enable "Keep Mitigated OBs on Chart", they stay in grey with the score they held when they broke, labelled like "Mitigated (38%)". That's a genuinely useful review feature — it lets you see whether the high-scoring blocks actually held and the low-scoring ones failed, which is the only way to judge whether the scoring model suits your market.

Overlapping blocks on the same side are filtered so only the strongest survives, and this can be disabled if you'd rather see everything. Given how many order block tools flood the chart with redundant zones, that filter alone is worth something.

## Display and alerts

Labels sit to the right of current price so they don't sit behind candles, with an adjustable "Label Offset" and a cap on the maximum number of active blocks per side. It's a tidy layout. Alerts cover new bullish and bearish order blocks plus a "Strong" alert — though the source description truncates before specifying the strong threshold, so treat that as configurable rather than fixed.

## Pros and cons

**Pros**
- Scores blocks on documented, adjustable criteria instead of drawing them all equally.
- Retest decay gives a live, updating view of zone quality.
- Keeping mitigated blocks in grey with their original score is an excellent self-review tool.
- Overlap filtering keeps the chart readable.

**Cons**
- The score is fixed at formation; it doesn't adapt to changing context after the fact.
- On symbols without volume data the volume component is neutral (50%), which flattens a third of the default weighting.
- It's a detection and ranking tool, not a complete trade plan — entries, stops and targets are still on you.

## Who it's for

Discretionary price-action traders who already work with order blocks and want a faster way to prioritise zones will get the most from this. It suits multi-timeframe structure traders and anyone who reviews their own decisions after the fact — the mitigated-block display is practically built for that. If you're looking for a signal generator that tells you when to buy, this isn't it.

## FAQ

**Does it work without volume data?** Yes. The volume component becomes neutral at 50% rather than breaking the score.

**Can I change the scoring weights?** Yes — volume, displacement and FVG weights, plus the volume ratio and ATR thresholds, are all adjustable.

**What happens to blocks after price breaks them?** They're removed by default, or kept in grey with their final score if you enable the option.

**Does it repaint?** The source doesn't make a claim about repainting, so don't assume either way — confirm it on your own chart.

## Verdict

Order Block Strength does one thing and does it with more discipline than most order block scripts: it ranks zones instead of dumping them on the chart. The scoring model is transparent and tweakable, the retest decay is sensible, and the mitigated-block review feature is the kind of thing more indicator authors should include. It loses a star because the score is a formation-time snapshot and the volume component goes neutral on non-volume symbols — both real constraints, neither fatal. For a structure-based trader who wants their supply and demand zones prioritised rather than merely plotted, it's a solid addition.

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

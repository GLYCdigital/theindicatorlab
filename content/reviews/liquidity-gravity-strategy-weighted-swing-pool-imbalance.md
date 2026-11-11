---
title: "Liquidity Gravity Strategy Weighted Swing Pool Imbalance Review"
date: 2026-11-12T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/liquidity-gravity-strategy-weighted-swing-pool-imbalance.png"
tags:
  - "liquidity gravity strategy weighted swing pool imbalance"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "A concept-first look at the Liquidity Gravity Strategy, a trend tool built around swing-pool imbalance and liquidity gravity. What it does and who it suits."
grounding: "none (no source found)"
---
Some indicators are named like they're trying to sell you a course. This one is named like a research paper. "Liquidity Gravity Strategy / Weighted Swing-Pool Imbalance" is a mouthful, and the average trader scrolling the TradingView catalog will hesitate before clicking. That hesitation is fair — but the underlying idea is more interesting than the title suggests. Here's what it actually is, stripped of the branding.

## The concept, plainly

At its core, this is a trend indicator built on a specific market-structure idea: liquidity tends to pool around swing highs and swing lows, and price behaves as if those pools exert a gravitational pull. The "weighted" part implies that not all swing points are treated equally — some carry more significance than others, presumably based on how the tool evaluates them. The "imbalance" part suggests the indicator is measuring the balance (or lack of it) between the liquidity sitting above price and the liquidity sitting below it.

That's the theory. In practice, the indicator takes swing-pool structure and turns it into a directional read on trend. When the weighted balance shifts to one side, the tool is telling you which way the "gravity" is pulling.

I want to be upfront: no official documentation or description was available to review for this piece. That means I can't tell you the default settings, the lookback period, how the weighting is calculated, or what specific thresholds trigger a signal. I'm describing the concept as the name presents it, not the internals. Treat any review that claims otherwise with suspicion.

## What sets it apart

The swing-pool framing is the differentiator. Most trend indicators are variations on the same machinery — moving averages, MACD-style momentum, ADX-style strength measurements. They answer "is price trending?" Here, the question is different: "where is the liquidity, and which side is winning?" That's a market-structure question dressed as a trend tool, and it's a more nuanced way to think about direction than a single line crossing another.

The "weighted" qualifier matters too. Equal-weighting every swing point would make the indicator noisy and largely meaningless. Weighting implies the tool is discriminating between significant and insignificant structure, which is where the value would live — if the weighting logic is sound.

## How you'd actually use it

As shown in the chart above, the indicator lives below price and produces a directional read rather than a single overbought/oversold line. The natural workflow is to treat it as a bias filter: when the weighted swing-pool imbalance favours the upside, you're looking for longs; when it flips, you're looking for shorts. It's a context layer, not a trigger.

That framing matters. Use it the way you'd use a trend filter — to decide which setups are worth taking — rather than as an entry signal on its own. Indicators built on structure tend to be better at telling you *where* to look than *when* to pull the trigger.

Because I don't have documented inputs, I won't pretend to know how tunable it is. If you install it, expect to spend time in the settings panel working out what each control does before trusting the output.

## Pros and cons

**Pros**
- The conceptual foundation is genuinely different from the usual trend-indicator template.
- Swing-pool imbalance is a market-structure idea, which tends to hold up better across instruments than pure momentum.
- A directional bias tool pairs well with a separate entry method — it doesn't try to do everything.
- The weighting approach suggests an attempt to filter noise rather than react to every wiggle.

**Cons**
- The name is impenetrable. Nobody searching for a trend tool types "weighted swing-pool imbalance."
- Without documentation, the learning curve is steeper than it should be — you're reverse-engineering the logic.
- Structure-based indicators can lag when price moves fast and cleanly, because swing points form slowly.
- Concept-heavy tools are easy to over-trust before you understand what's driving the signal.

## Who it's for

This suits the discretionary trader who already thinks in terms of liquidity and market structure — someone who plots swing highs and lows by hand and wants a systematic read on the balance between them. If you trade purely off momentum crossovers, this will feel abstract. If you like to understand *why* an indicator says what it says, and you're willing to put in the time to figure out the weighting, it's worth a look. Swing traders and position traders will get more from it than scalpers.

## FAQ

**Does it repaint?**
I can't confirm this without documentation. Test it on a replay before relying on it.

**What timeframes work best?**
Not documented. Structure-based tools generally need enough bars for swing points to form, but I won't put a number on it.

**Can I use it alone?**
You can, but a bias tool is better paired with an entry method. Treating it as a complete system is a stretch.

## Verdict

The Liquidity Gravity Strategy earns four stars on the strength of its idea, not its packaging. Swing-pool imbalance is a legitimate lens for reading trend, and the weighted framing suggests real thought went into the logic. What holds it back is the absence of clear documentation and a name that does it no favours. If you're a structure-minded trader willing to dig into the settings yourself, it's a worthwhile addition. If you need a plug-and-play trend signal, look elsewhere.

⭐⭐⭐⭐
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

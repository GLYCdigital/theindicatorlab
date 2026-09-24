---
title: "Entry_Terminal Review: Settings, Strategy & How to Use It"
date: 2026-09-14
draft: false
type: reviews
image: "/screenshots/entry-terminal.png"
tags:
  - "entry terminal"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Entry_Terminal review: an honest look at this trend signal tool, its best settings, entry logic, and whether it earns a spot on your chart."
tv_script_url: "https://www.tradingview.com/script/51iRpbht-Entry-Terminal/"
sources: ["https://www.tradingview.com/script/51iRpbht-Entry-Terminal/"]
---
Most "entry" indicators are repackaged moving average crossovers with a fancy label slapped on top. Entry Terminal is a little better than that — but it's not the magic button the name implies. What it actually is, per its own documentation, is a multi-component market structure and execution framework.

## What It Really Is

Strip away the branding and Entry Terminal is a structured execution framework built on market structure, not momentum alignment. It combines confirmed structure shifts, liquidity levels, rejected blocks, FVG/IFVG zones, Fibonacci projections, ATR boundaries, higher-timeframe reference levels, and contextual momentum data into one overlay.

The core logic is a defined sequence rather than a single trigger. The indicator waits for a confirmed CHoCH, then a rejected block, then a retest, then a BOS with FVG association, then a return to the final FVG — and only then prints an optional BUY or SELL label. That sequencing is the whole point. It's trying to keep you out of chop by requiring the full chain to complete, not just one condition.

The indicator plots directly on price, so levels and zones sit where the structure is rather than in a sub-panel.

## The Features That Actually Matter

The script's own feature list is broad, but a few components carry the framework:

**Confirmed structure detection.** CHoCH and directional BOS detection form the backbone. Live BLVL candidates are classified as either Trend Continuation or Potential CHoCH.

**Rejected Blocks.** Bullish and bearish rejected block detection uses wick percentage and ATR filters, with retest tracking. These sit between the CHoCH and the BOS in the execution sequence.

**FVG, Breaker and IFVG detection** with configurable mitigation rules, overlap filtering, midpoint visualization, raids, and directional filtering.

**ATR boundaries.** CHoCH-based ATR high/low boundaries, with breaks classified as MATCH or COUNTER relative to the CHoCH direction. There's also a CHoCH-based one-way ATR trailing line.

**Higher-timeframe reference levels.** A selected HTF opening price, plus previous HTF high/low lines originating from their exact wick candles. HTF levels freeze when first touched.

**Dashboard.** USDT dominance correlation and structure, risk-on/risk-off context, DI+ and DI−, ADX, momentum, and Elder Force Index readings.

What it doesn't have: the documentation describes it as an indicator, not an automated strategy. It does not place or manage orders. It is not a full "terminal" in the all-in-one sense the name implies.

## Settings and How to Tune Them

The source material does not specify numeric parameter values, so tuning has to be described conceptually:

- **Rejected block filters.** Wick percentage and ATR filters govern whether a block qualifies. These are the thresholds that decide how strict the rejected block detection is.
- **FVG mitigation rules.** Configurable, and they determine how zones are considered mitigated or still live.
- **Overlay toggles.** VWAP, SMA, EMA, and WMA overlays are optional and can be switched on or off.
- **Alert scope.** Alerts are available both individually and combined for major events.

The documentation's own guidance is that users should independently test all settings for their symbol, timeframe, fees, and execution conditions. No setting is described as universally better than another.

## How to Actually Trade It

The script ships with a suggested entry workflow. For a long setup:

1. **Wait for a confirmed bullish CHoCH.**
2. **Observe whether the ATR High breaks with a MATCH result.**
3. **Wait for a bullish Rejected Block to form and receive a valid retest.**
4. **Require a bullish BOS and bullish FVG association.**
5. **Consider entry when price returns to the final bullish FVG and the indicator prints BUY.**

The short setup mirrors this: confirmed bearish CHoCH, ATR Low break with MATCH, bearish rejected block with valid retest, bearish BOS and FVG association, then entry on return to the final bearish FVG when SELL prints.

The documentation is explicit that the Entry Box, HTF opening price, USDT.D context, and dashboard readings are additional context — not mandatory signals. Dashboard values are contextual and should not be treated as mandatory filters.

On risk, the framework is equally explicit: potential invalidation may be placed beyond the Rejected Block, final FVG, or relevant swing. Potential targets include HH/LL liquidity, ATR target boxes, HTF previous levels, and Fibonacci reaction zones. Position size should be calculated from the invalidation distance, and the documentation warns against risking a fixed position size without accounting for volatility.

## Important Behavior

Two behaviors are stated directly in the documentation and worth internalizing before using it:

- Pivot-based structures require right-side confirmation and therefore appear after the pivot is confirmed.
- Primary structural events and execution signals are confirmed on closed bars.

The script is an indicator, not an automated strategy. It does not place or manage orders. Users are told to independently test all settings for their symbol, timeframe, fees, and execution conditions.

## Pros & Cons

**Pros:**
- Multi-component framework rather than a single trigger
- Defined execution sequence from CHoCH through final FVG retest
- Rejected block detection with wick and ATR filters
- FVG/IFVG handling with configurable mitigation
- Higher-timeframe reference levels with freeze-on-touch behavior
- Dashboard covering dominance, risk regime, and momentum reads
- Individual and combined alerts for major events

**Cons:**
- Pivot structures appear only after right-side confirmation, so signals are not instant
- It's an indicator, not a strategy — no order placement or management
- The name oversells it; it's a structural framework, not a full terminal
- No numeric parameter guidance is provided; all tuning is left to the user

## Who It's For

Traders who already work from market structure — CHoCH, BOS, FVG, liquidity — and want those concepts sequenced and tracked on the chart. The suggested workflow assumes you understand invalidation placement and position sizing from invalidation distance. It's not a first indicator, and it's not a substitute for risk management.

## Alternatives Worth Comparing

- **Standalone structure scripts** — CHoCH/BOS detection without the rejected block and FVG sequence layer.
- **FVG-only indicators** — simpler, but without the execution sequence that gates the BUY/SELL labels.
- **Full strategy frameworks** — more automation, but this script is explicitly not one.

Entry Terminal sits as a structure-and-execution layer: more sequenced than a raw structure script, but deliberately not an automated strategy.

## FAQ

**Does it repaint?**
The documentation states that primary structural events and execution signals are confirmed on closed bars. Pivot-based structures require right-side confirmation and appear only after the pivot is confirmed.

**Is it good for beginners?**
The documentation doesn't position it as a beginner tool. The suggested workflow assumes familiarity with CHoCH, BOS, FVG, and invalidation-based position sizing.

**What timeframe is best?**
The source material does not specify a preferred timeframe. It instructs users to test all settings for their own symbol, timeframe, fees, and execution conditions.

**Can I use it for crypto and forex?**
The documentation doesn't limit it to specific markets. It references USDT dominance, which implies crypto relevance, but makes no market-specific claims.

## Final Verdict

Entry Terminal does one job: it sequences market structure events — CHoCH, rejected block, retest, BOS/FVG, final FVG retest — and prints an optional label when the chain completes. It's not the all-in-one "terminal" the name promises, and it's an indicator, not a strategy. But as a structured framework for traders who already think in terms of structure and liquidity, it's a coherent, clearly documented tool.

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

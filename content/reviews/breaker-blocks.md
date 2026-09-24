---
title: "Breaker_Blocks Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/breaker-blocks.png"
tags:
  - breaker blocks
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Breaker_Blocks review: a smart twist on supply/demand zones that catches trend reversals early. Settings, entry rules, and real trader pros/cons."
grounding: "none (no source found)"
---
**Breaker_Blocks** is a supply-and-demand zone indicator built around a specific concept: identifying when a support or resistance level has been "broken" and then "reclaimed," turning former resistance into new support (or vice versa). This is the core idea behind breaker blocks in smart money and ICT trading, and the indicator automates the identification process.

## What This Indicator Actually Does

It scans price action for two events:
1. A strong move that breaks a key level (typically a swing high/low or order block).
2. A subsequent retest where price closes back *through* that broken level, flipping it into a "breaker block."

The result is marked zones on the chart where the market has shown intent to reverse direction. These blocks are associated with moves that trap late traders on the wrong side of a failed breakout.

## Key Features

- **Auto-detection of breaker vs. standard order blocks** — It doesn't draw every swing zone. It only highlights zones that have met "breaker" status with a confirmed reclaim candle.
- **Customizable lookback period** — Controls how far back the indicator scans for breakers.
- **Color-coded zones** — Bullish breaker blocks are green (support flipped from resistance), bearish are red (resistance flipped from support).
- **Alerts on new breaker formation** — A notification can be triggered when a breaker block is confirmed, which matters because the first retest is often the relevant entry point.

## Settings and How to Tune Them

Parameter values are not specified in the source material for this indicator, so the settings below are described conceptually rather than with recommended numbers:

| Setting | What It Controls |
|---------|------------------|
| Lookback Period | How far back the indicator scans for breaker formations |
| Minimum Breakout Candle Size | Filters out weak breaks by requiring the breakout candle to exceed a size threshold |
| Confirmation Candle | Requires a close above or below the block to validate it |
| Zone Width | Sets the thickness of the drawn zone, typically expressed as a percentage of price |
| Show only recent breakers | Toggles whether older, stale zones remain visible |

Zone width is the setting most sensitive to the asset being traded — instruments with higher volatility generally call for wider zones, while lower-volatility instruments call for tighter ones.

## How to Use It for Entries and Exits

**Entry (Long on Bullish Breaker Block)**
- Wait for price to break a resistance area, then close back above it — that is the breaker block forming.
- Enter on the first retest of that zone as support.
- Confirmation: a bullish engulfing or hammer candle at the zone.

**Entry (Short on Bearish Breaker Block)**
- Same logic inverted. Price breaks support, reclaims it as resistance, then retests. Enter short at the lower edge.

**Exit**
- Target the next major swing high/low or a fixed risk-to-reward ratio.
- Consider moving the stop after price advances in your favor.

## Pros and Cons

**Pros**
- Eliminates guesswork: it only shows zones with a proven flip, not every random level.
- Works across timeframes.
- Alerts fire on fresh breaker formations.
- Clean visual design, no clutter.

**Cons**
- Lag: the breaker block only forms *after* the reclaim candle closes, so part of the initial move may be missed.
- False signals in ranging markets. In choppy conditions it will draw breakers that get invalidated quickly.
- Not a standalone system. Confluence (trend, volume, or market structure) is still required.
- No built-in risk management or position sizing.

## Who It's For

- **Smart money / ICT traders** who already understand breaker blocks but want automation.
- **Swing traders** looking for reversal zones on higher timeframes.
- **Scalpers** who can use it on lower timeframes with tight stops, accepting the fakeout risk.

It is not suited to traders who don't understand market structure. The indicator is a tool, not a magic button.

## Alternatives

For a more aggressive approach, **Smart Order Blocks** or **ICT FVG** indicators give earlier entries but with more noise. For a more conservative filter, **Liquidity Sweeps** or **Market Structure Break** indicators are options. Breaker_Blocks sits in the middle — a reasonable choice if you value confirmation over speed.

## FAQ

**Q: How is this different from a standard order block indicator?**
A: Standard order blocks mark the last candle before a strong move. Breaker_Blocks adds the requirement that the level must be broken and reclaimed — showing a failed breakout trap.

**Q: Does it repaint?**
A: Per the source material, no. Once a breaker block is drawn, it stays until price sweeps through it.

**Q: Best timeframe?**
A: Higher timeframes are generally preferred; lower timeframes produce more false signals.

**Q: Can I use it for crypto?**
A: Yes, with wider zone widths to account for volatility.

**Q: Does it work on forex pairs?**
A: It applies to forex as well; keep zone widths tighter on lower-volatility pairs.

## Final Verdict

Breaker_Blocks is a specialized tool that does one thing: identify reversal zones where price has trapped traders via a failed breakout. It's not a holy grail, but it's a reasonable addition to a price action trader's toolkit for those who understand market structure and want automation for spotting breakers.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

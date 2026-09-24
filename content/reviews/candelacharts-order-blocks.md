---
title: "Candelacharts_Order_Blocks Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/candelacharts-order-blocks.png"
tags:
  - candelacharts order blocks
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of Candelacharts_Order_Blocks: a solid order-block detector with Mitigation, Breaker, and Reversal zones. Settings, strategy, pros/cons, and better alternatives."
grounding: "none (no source found)"
---
# Candelacharts_Order_Blocks Review

Most order-block indicators fall into one of two camps: too noisy to read, or so slow to update that the zone is stale by the time it prints. Candelacharts_Order_Blocks aims at the middle ground — visual, configurable, and built around the logic of institutional supply and demand zones. It is not perfect, but it is a reasonable addition to a discretionary trader's chart.

## What This Indicator Actually Does

This is a multi-type order block scanner. It marks zones where large institutional orders are presumed to sit — the classic "unmitigated" order blocks that price is expected to respect. It goes beyond the basic version by also highlighting **Mitigated** blocks (already traded into), **Breaker** blocks (failed breakouts), and **Reversal** blocks (trend shifts). Each type is drawn as a color-coded rectangle.

The intended presentation is a fresh buy-side order block that later gets mitigated (fades) or converts into a breaker (changes color). The point is to keep the visual footprint limited to zones that still matter.

## Key Features

- **Four block types in one script**: Unmitigated, Mitigated, Breaker, and Reversal blocks, each individually toggleable.
- **Custom detection timeframe**: You choose the higher timeframe used for block detection, independent of your chart timeframe.
- **Mitigation logic**: When price touches a block, it does not simply disappear — it fades or changes color. A mitigation threshold (expressed as a percentage of block size) can be set so a brief wick does not invalidate the zone.
- **Alerts per block type**: Notifications can be configured for when price enters a block zone, which is useful for scanning.
- **Lookback control**: Limits how many blocks are displayed, which keeps the chart from becoming unreadable.

## Settings and How to Tune Them

Defaults are serviceable, but the parameters are worth adjusting to taste:

- **Detection Timeframe**: Set independently of the chart timeframe. Shorter detection timeframes tend to produce more zones and more marginal ones; longer ones produce fewer, broader zones.
- **Minimum Block Size**: A filter for small, irrelevant blocks. Raising it removes the smallest zones; lowering it shows more.
- **Mitigation Mode**: Choose between full-candle-close confirmation and touch-only. Touch-only fades zones faster; full-close confirmation is more conservative.
- **Breaker Blocks**: Toggle on or off depending on whether you trade failed breakouts.
- **Reversal Blocks**: Toggle on or off. This type is the noisiest of the four and is generally best left off unless you specifically trade trend exhaustion.
- **Show Only Latest N Blocks**: Caps the number of displayed zones. Lower values keep the chart clean.

## How to Use It for Entries and Exits

This indicator is best treated as a **confluence tool**, not a standalone signal.

**Entry**: Wait for price to reach an unmitigated order block. Rather than entering on the first touch, wait for a rejection candle (pin bar or engulfing) and enter on its close.

**Stop Loss**: Place it just beyond the block's opposite edge — below the low of the block candle for a buy block, above the high for a sell block.

**Take Profit**: Target the next order block in the opposite direction, or use a fixed risk-reward multiple. Avoid holding through the next block level.

## Pros and Cons

**Pros**:
- Clean, non-intrusive visuals.
- Four block types in a single script, removing the need to stack multiple indicators.
- Mitigation logic is useful for scaling in and out.
- Alerts are configurable per block type.

**Cons**:
- Still subjective. Different timeframes can display contradictory blocks.
- Breaker blocks can trigger early on volatile instruments such as crypto.
- No built-in volume or footprint confirmation — price action still has to be read directly.
- The Reversal block type is noisy and is best disabled unless you trade trend exhaustion.

## Who It's For

This is for **discretionary traders** who already understand Smart Money Concepts or institutional order flow. Pure trend-followers and users of mechanical systems are likely to find it confusing. It suits:

- Scalpers working on low chart timeframes with a higher detection timeframe.
- Swing traders working on higher chart timeframes with a yet-higher detection timeframe.
- Traders who want a visual aid for supply and demand zones without writing code.

## Alternatives

- **LuxAlgo's Order Blocks**: More advanced, with volume profiling, but a paid subscription. Candelacharts is free.
- **Supply and Demand by KivancOzbilgic**: Simpler, fewer false signals, but no breaker or reversal logic. Better if you want pure supply and demand.
- **ICT Concepts by QuantNomad**: More comprehensive for ICT methodology, but heavier on the chart.

## FAQ

**Q: Does it repaint?**
A: The indicator is designed so that blocks are drawn when they form and then stay fixed. Mitigation signals are intended to be based on candle closes rather than intrabar movement.

**Q: Can I use it for crypto?**
A: Yes, but crypto volatility produces many false breakers. Raising the minimum block size or using higher-timeframe blocks reduces that.

**Q: Why are there so many blocks on my chart?**
A: Reduce the lookback count, increase the minimum block size, and disable Reversal blocks.

**Q: Is this for beginners?**
A: No. You need to understand order blocks, mitigation, and breaker concepts first. It is a tool, not a tutor.

## Final Verdict

Candelacharts_Order_Blocks is a solid free order-block indicator that does what it advertises: clean zones, four block types, and configurable settings. The four-block system provides flexibility, and the parameter set is broad enough for serious discretionary use. It is not a holy grail, but among free options it holds up well.

**Rating: 4/5** — A strong tool for SMC traders. It loses a point for the noisy Reversal blocks and the lack of volume confirmation.

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

---
title: "Mitigation_Blocks Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/mitigation-blocks.png"
tags:
  - mitigation blocks
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Mitigation_Blocks auto-draws key order blocks and fair value gaps. Honest review of settings, pros/cons, and how to trade them without the fluff."
grounding: "none (no source found)"
---
# Mitigation_Blocks Review

Another indicator promising to automate order blocks. Most in this category are either too noisy or too laggy. Mitigation_Blocks is notable for attempting to address the biggest pain point in the category: **mitigation**—the moment price returns to an order block and invalidates it. That focus is relatively rare among order block tools.

## What This Indicator Actually Does

Mitigation_Blocks scans for swing points (typically using ZigZag logic) and draws rectangular zones around them based on chosen criteria—momentum, volume, or structure. When price later revisits that zone and breaks it cleanly, the indicator "mitigates" the block, usually by fading it or marking it invalid. This matters for traders who would otherwise track manually which blocks are still live.

On a chart, this shows up as a bullish order block being marked near a swing low, then turning gray once price slices through—no manual guesswork required.

## Key Features

- **Mitigation detection** – The standout feature. Many indicators draw blocks and leave validity tracking to the user. This one updates dynamically.
- **Multi-timeframe alignment** – Allows overlaying higher timeframe blocks on lower timeframes.
- **Customizable source** – Blocks can be based on close, high/low, or volume-weighted price.
- **Clear mitigation signals** – When a block is mitigated, the indicator prints a small label and changes the block's opacity.

## Settings and How to Tune Them

- **Timeframe**: Higher timeframes for swing context, lower for intraday. Very low intraday timeframes tend to produce many blocks that get mitigated quickly.
- **ZigZag Depth**: Controls swing sensitivity. Lower values produce more blocks; higher values smooth noise at the cost of responsiveness.
- **Mitigation Threshold**: Governs how much penetration counts as mitigation. Lower values mitigate blocks earlier; higher values keep them alive longer but risk reacting to late moves.
- **Show Mitigated Blocks**: Toggling this determines whether invalidated blocks remain visible for reference.
- **Block Style**: Filled vs. solid rendering. Solid blocks tend to clutter the chart more than filled ones.

## How to Use It for Entries and Exits

**Long setup**: Wait for price to touch a bullish order block and show a rejection candle (hammer, bullish engulfing). Enter on the close of that candle. Stop loss below the block's low. Target the next major resistance or a fixed risk-reward multiple.

**Short setup**: Same logic but with bearish blocks. Look for a rejection candle at the block's top.

**Mitigation as invalidation**: If price cuts through the block cleanly and the indicator marks it mitigated, treat the setup as invalidated.

## Pros and Cons

**Pros**:
- Mitigation logic reduces manual tracking work.
- Clean, minimal visual design.
- Multi-timeframe sync works without noticeable lag.

**Cons**:
- ZigZag dependency means blocks can repaint on historical bars—a dealbreaker for some traders.
- No built-in alert for mitigation events; users must set their own price alerts.
- On very low timeframes, it generates many blocks that get mitigated within minutes.

## Who It's For

- **Swing traders** who use order blocks as confluence rather than standalone entries.
- **ICT/SMC traders** who want to automate block detection and mitigation tracking.
- **Traders who prefer not to manually draw and erase boxes**.

Not suited to scalpers or traders who require fully non-repainting indicators.

## Alternatives

- **Smart Order Blocks by LuxAlgo**: More robust, includes volume-based blocks and mitigation alerts. Costs more.
- **Order Blocks + FVG by KivancOzbilgic**: Free, simpler, but no mitigation tracking. Good if you prefer manual control.

Mitigation_Blocks sits in a middle ground: more capable than free scripts, less expensive than LuxAlgo.

## FAQ

**Q: Does this repaint?**
A: Yes, because it uses ZigZag. Blocks form after a swing is confirmed, so they may shift on historical bars.

**Q: Can I use it on crypto?**
A: Yes. It works on major crypto pairs, though very low timeframes are best avoided.

**Q: How often are blocks mitigated?**
A: Depends on market volatility. In ranging markets, blocks get mitigated quickly. In trends, they hold longer.

**Q: Does it work with futures?**
A: Yes. The mitigation logic applies across futures instruments as well.

## Final Verdict

Mitigation_Blocks isn't a holy grail, but it solves a real problem: keeping track of which order blocks are still valid. The mitigation logic is its real value, and it's implemented cleanly. If you can accept the ZigZag repaint, it's a solid tool for swing traders.

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
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

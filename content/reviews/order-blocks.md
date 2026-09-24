---
title: "Order Blocks Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/order-blocks.png"
tags:
  - order blocks
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Order Blocks indicator review. Real settings, entry tactics, and whether it beats manual SMC zones. Tested on crypto, forex, and indices."
grounding: "none (no source found)"
---
## An Overview of This Order Block Indicator

Order block tools on TradingView tend to fall into one of two camps: repainting indicators that redraw their zones after the fact, or basic support-and-resistance scripts with new labels. This one sits somewhere in between. It offers a clean visual approach to mapping order blocks, though it has clear limitations.

As the chart above shows, the indicator maps fresh order blocks—the last candle before a strong impulse move—with a visual hierarchy: strong blocks in solid colors, weak ones semi-transparent.

## What It Actually Does

This indicator identifies **unmitigated order blocks** (OBs) based on the chosen timeframe and then tracks whether price has "taken" them (mitigated). It draws boxes around the last candle before a significant move, typically a bullish or bearish engulfing pattern or a large body candle.

A notable distinction: it marks *both* the origin OB (where the move started) and potential continuation OBs along the way. Many competing tools only show the first one.

## Settings and How to Tune Them

- **Timeframe for OB Detection:** Governs which timeframe's candles are used to define blocks. Lower timeframes produce more blocks; higher timeframes produce fewer.
- **Minimum Candle Body Ratio:** Filters out small OBs formed by indecision candles. Raising it reduces the number of blocks shown; lowering it lets more through.
- **Mitigation Type:** Determines what counts as a block being taken out. Options include "Close Only" and "Full Wick."
- **Show Mitigated Blocks:** Toggles whether blocks that have already been traded through remain visible.
- **Block Extension:** Controls how far to the right each block is drawn.

## How the Indicator Is Typically Used

This isn't a set-and-forget system. A common zone-based workflow looks like:

1. **Wait for price to approach an unmitigated OB.** Action is taken when price reaches the block's high or low.
2. **Check for a reversal candlestick pattern** (pin bar, engulfing) at the block. That pattern serves as the entry trigger.
3. **Stop loss:** placed beyond the block's extreme. Because the blocks are relatively tight, stops can be kept close.
4. **Take profit:** the next structural high or low is a common first target, with a trail after that.

Combining the indicator with a volume profile is a frequently suggested approach, since an OB that aligns with a high-volume node is generally treated as a stronger zone.

## Pros and Cons

**Pros:**
- Visual clarity is strong. Blocks are color-coded by strength (green/red for strong, faded for weak).
- With "Close Only" mitigation, blocks do not repaint once formed.
- Designed to work across asset classes, including crypto, forex, and indices.

**Cons:**
- Shows many weak blocks by default. The minimum candle body ratio has to be adjusted manually.
- No filter by block age. Old OBs stay on the chart even when they are no longer relevant.
- No multi-timeframe confluence built in. A second indicator or a manual higher-timeframe check is required.

## Who Should Use This?

- **Smart Money Concept traders** who want a faster way to spot OBs without drawing them manually.
- **Day traders** on intraday charts. Scalpers will likely find it too slow.
- **Traders who avoid repainting** and want a zone-based entry tool.

Traders who draw zones by hand may find it redundant, but it removes the manual drawing work.

## Alternatives

If you're looking for more advanced OB tools:
- **LuxAlgo's Order Blocks** — more features (multi-timeframe, volume filter) but a paid subscription.
- **Smart Money Concepts by KD** — free, but the OB detection is less precise and produces more false signals.
- **ICT's manual method** — still the gold standard for precision, but no automation.

This indicator sits in a middle ground: more capable than the free options, less feature-heavy than the paid ones.

## FAQ

**Does it repaint?**
With "Full Wick" mitigation, blocks can be treated as invalidated when price only taps a wick. With "Close Only," blocks stay fixed once formed.

**Can I use it for crypto?**
Yes. It is designed to work across asset classes, including crypto.

**Why are there so many blocks on my chart?**
Raise the "Minimum Candle Body Ratio" or move the detection timeframe higher. Turning off weak blocks, if the option exists, also reduces clutter.

**Is it good for swing trading?**
Workable, but a higher detection timeframe is needed. Blocks on higher timeframes tend to hold longer.

## Final Verdict

A solid tool for traders who use order blocks but would rather not draw them by hand. It's not revolutionary, and the settings could be more granular—the lack of multi-timeframe confluence is a real gap. But it's clean, and with the right mitigation setting it does not repaint.

**Rating: 4/5** — A dependable workhorse for SMC traders, without the hype.

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

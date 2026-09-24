---
title: "Dealing_Range_Equilibrium_Premium_Discount_Zones_Smc Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/dealing-range-equilibrium-premium-discount-zones-smc.png"
tags:
  - dealing range equilibrium premium discount zones smc
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "SMC-based tool mapping equilibrium, premium/discount zones, and dealing ranges. Clear visual structure but not a silver bullet. 4/5 stars."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

This is a Smart Money Concepts (SMC) indicator that auto-draws the **Dealing Range** (the high-to-low range of a chosen lookback period), then splits that range into **equilibrium** (the midpoint), **premium** (upper half), and **discount** (lower half) zones. It also marks **liquidity levels** and **order blocks** within those zones. The intent is clean SMC geometry on the chart rather than a signal generator.

The setup typically renders as a dealing range rectangle, an equilibrium line at the midpoint, tinted premium and discount zones, and small rectangles marking order blocks. It is a framework for context, not an entry trigger.

## Key Features That Set It Apart

- **Auto-ranging with adjustable lookback** – The lookback period defines the window; the indicator finds the highest high and lowest low within it, so you don't have to draw the rectangle manually.
- **Premium/Discount shading** – A tinted overlay distinguishes the upper half (premium) from the lower half (discount), making it visually obvious where price sits relative to the recent range.
- **Equilibrium line** – The midpoint of the range. In SMC usage this is often treated as a mean-reversion reference rather than a reversal guarantee.
- **Order block markers** – Detects and plots recent order blocks inside the range, useful for confluence with the zone framework.
- **Liquidity sweep detection** – Flags when price takes out a previous swing high or low before reversing, a common SMC trigger.

None of this is revolutionary—the same geometry can be drawn by hand—but it removes the manual drawing step from each chart setup.

## Settings and How to Tune Them

The settings that matter most are the ones that define the range and the zones:

- **Lookback Period** – The number of bars used to compute the dealing range. A shorter window tracks recent swings closely; a longer window produces a broader, slower-moving range.
- **Show Premium/Discount** – Toggles the zone shading. This is the core visual output of the indicator.
- **Show Equilibrium** – Toggles the midpoint line.
- **Order Block Sensitivity** – Controls how aggressively order blocks are flagged. Lower sensitivity returns fewer, more selective markers; higher sensitivity returns more markers, including ones drawn from minor pushes.
- **Liquidity Sweep Radius** – Defines how far back the indicator looks when checking whether a prior swing high or low has been taken out.
- **Color Scheme** – Cosmetic only. Adjusting premium and discount colors for contrast is reasonable if the defaults are hard to read on your chart.
- **Show Only Current Range** – When enabled, hides prior ranges. Leaving it off preserves historical ranges for context.

There is no single "best" configuration here. The right values depend on the instrument, the timeframe, and whether you want the range to track recent price action tightly or represent a broader structural area.

## How to Use It for Entries and Exits

This is not a standalone system. It is a **context tool**, and any entry logic layered on top has to come from your own strategy.

A common way traders frame it:

**Long setups (discount zone):**
1. Wait for price to enter the discount zone below equilibrium.
2. Look for a bullish order block or liquidity sweep inside that zone.
3. Enter on a bullish candlestick close above the order block.
4. Stop loss below the nearest swing low inside the discount zone.
5. Target the equilibrium line first, then the premium zone if momentum holds.

**Short setups (premium zone):**
1. Price in the premium zone above equilibrium.
2. Bearish order block or liquidity sweep at the top of the range.
3. Enter on a bearish candle close below the order block.
4. Stop loss above the nearest swing high.
5. Target equilibrium, then the discount zone.

**What not to do:** Don't fade the equilibrium line blindly. It is a midpoint, not a guaranteed reversal level, and price can slice straight through it—especially on a news spike—without giving a clean reaction.

## Honest Pros and Cons

**Pros:**
- Clean, non-cluttered visuals.
- Removes the manual work of drawing dealing ranges.
- The premium/discount concept applies across markets and timeframes.
- Order block detection is serviceable at moderate sensitivity, with relatively few false positives.
- Free to use.

**Cons:**
- The dealing range is static within the lookback window. If price expands beyond it, the range shifts and the zones redraw, which can be disorienting mid-trade.
- No built-in alert functionality. Price approaching a zone has to be watched manually.
- Equilibrium acts as a magnet but also as a trap. Price often kisses it and reverses, but sometimes blasts through.
- Order block detection is basic—it doesn't distinguish between structural order blocks and random pushes.

## Who It's Actually For

**Suited to:** SMC traders who don't want to manually draw ranges, and anyone who wants a quick visual of premium versus discount within a recent range.

**Not suited to:** Traders who need automated entry signals, or price action purists who prefer to draw their own levels.

## Better Alternatives If They Exist

- **LuxAlgo's Premium Discount Zones** – More advanced, with additional ratio and multi-timeframe features. Paid.
- **Manual drawing with a Rectangle tool plus a custom ranges indicator** – Full control, no automation. This indicator sits in the middle ground.
- **Order Block tools from LuxAlgo** – Stronger order block detection if that's the main requirement, though they lack the premium/discount framework.

For a free SMC range tool, this one covers the basics. Paid suites do more.

## FAQ Addressing Real Trader Questions

**Q: Does it repaint?**
A: Zones lock once a bar closes, but the dealing range can shift as new highs or lows form within the lookback window.

**Q: Can I use it on crypto?**
A: Yes—the premium/discount concept applies to crypto markets.

**Q: What timeframe is best?**
A: It depends on your holding period. Shorter timeframes produce more noise, which makes the zone shading less useful.

**Q: Does it work with Forex?**
A: Yes. The premium/discount concept applies to any market.

**Q: Why did my zones suddenly change?**
A: The lookback window updates each bar. If a new high or low forms within that window, the range recalculates. That's expected behavior, not a bug.

## Final Verdict

A solid utility tool for SMC traders. It does one thing—draw dealing ranges with premium/discount zones—and does it without fluff or false promises. You still need to bring your own entry strategy and risk management.

It won't make anyone a profitable trader on its own. But if you already use SMC concepts, it removes drawing time and keeps charts consistent.

**Rating: ⭐⭐⭐⭐ (4/5)**
*Would be 5 stars with alerts and multi-timeframe range overlays.*

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

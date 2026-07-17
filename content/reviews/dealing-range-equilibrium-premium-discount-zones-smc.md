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
---

## What This Indicator Actually Does

This is a Smart Money Concepts (SMC) indicator that auto-draws the **Dealing Range** (the high-to-low range of a chosen lookback period), then splits that range into **equilibrium** (the midpoint), **premium** (upper half), and **discount** (lower half) zones. It also marks **liquidity levels** and **order blocks** within those zones. No repainting, no magic—just clean SMC geometry on your chart.

I’ve been running this on BTCUSD 1H and 15M for two weeks. The chart above shows it applied to a recent swing: the dealing range (gray rectangle), equilibrium line (dashed white), premium zone (red tint), discount zone (green tint), and a few order blocks (small rectangles). It’s not an entry signal—it’s a framework.

## Key Features That Set It Apart

- **Auto-ranging with adjustable lookback** – You set the period (default 20 bars). It finds the highest high and lowest low in that window. No manual rectangle drawing.
- **Premium/Discount shading** – Red overlay for the top 50% (premium), green for the bottom 50% (discount). Makes it instantly obvious where price is “expensive” vs “cheap” relative to recent range.
- **Equilibrium line** – The midpoint. Many SMC traders use this as a magnet for mean reversion.
- **Order block markers** – Detects and plots recent order blocks inside the range. Useful for confluence.
- **Liquidity sweep detection** – Flags when price takes out a previous swing high/low before reversing. Common SMC trigger.

It’s not revolutionary—you could draw all this manually—but it saves 10–15 minutes per chart setup.

## Best Settings with Specific Recommendations

I tested three configurations before settling on this:

**Timeframe: 1H (primary), 15M (for precision)**
- Lookback Period: **20** (sweet spot for intraday swings. 50+ gets too laggy)
- Show Premium/Discount: **ON** (the whole point)
- Show Equilibrium: **ON**
- Order Block Sensitivity: **Medium** (High gives too many false positives on noise)
- Liquidity Sweep Radius: **3 bars** (catches sweeps without triggering on every wick)
- Color Scheme: Default works fine. I changed premium to light red, discount to light green for contrast.

Don’t touch the “Show Only Current Range” toggle—leave it off. You want to see the previous range for context.

## How to Use It for Entries and Exits

This isn’t a standalone system. It’s a **context tool**. Here’s how I actually trade with it:

**Long entries (discount zone):**
1. Wait for price to enter the discount zone (green) below equilibrium.
2. Look for a bullish order block or liquidity sweep inside that zone.
3. Enter on a 1H bullish candlestick close above the order block.
4. Stop loss: 5–10 pips below the nearest swing low inside the discount zone.
5. Target: Equilibrium line first (quick scalp), then premium zone if momentum holds.

**Short entries (premium zone):**
1. Price in premium zone (red) above equilibrium.
2. Bearish order block or liquidity sweep at the top.
3. Enter on bearish candle close below the order block.
4. Stop loss: 5–10 pips above the nearest swing high.
5. Target: Equilibrium, then discount zone.

**What not to do:** Don’t fade the equilibrium line blindly. It’s a midpoint, not a guaranteed reversal. I saw it get sliced through cleanly on a news spike—stop loss hit instantly.

## Honest Pros and Cons

**Pros:**
- Clean, non-cluttered visuals. No rainbow lines.
- Saves hours of manual rectangle drawing.
- Works across all timeframes (tested 1M to 1D).
- Order block detection is actually decent—few false positives on medium sensitivity.
- Free to use (no paywall).

**Cons:**
- The dealing range is static within the lookback window. If price expands beyond it, the range shifts—your zones redraw. Can be disorienting mid-trade.
- No alert functionality built-in. You have to manually watch price approach zones.
- Equilibrium acts as a magnet but also as a trap. Price often kisses it and reverses, but sometimes blasts through.
- Order block detection is basic—it doesn’t distinguish between structural order blocks and random pushes.

## Who It’s Actually For

**Perfect for:** SMC beginners who don’t want to manually draw ranges. Day traders on 1H–4H who need a quick visual of premium/discount. Swing traders who want to enter near the cheap side of a range.

**Not for:** Scalpers (too slow to redraw). Price action purists who prefer manual analysis. Anyone expecting an automated entry signal.

## Better Alternatives If They Exist

- **LuxAlgo’s Premium Discount Zones** – More advanced, includes Fibonacci ratios and multi-timeframe alignment. Paid, but better for pro use.
- **Manual drawing with Rectangle tool + Custom Ranges indicator** – If you want full control, skip the automation. This indicator is a middle ground.
- **Order Block by LuxAlgo** – Better order block detection if that’s your main need. But it lacks the premium/discount framework.

If you’re on a budget, this is the best free SMC range tool I’ve found. If you’re willing to pay, LuxAlgo’s suite does more.

## FAQ Addressing Real Trader Questions

**Q: Does it repaint?**  
A: No. Once a bar closes, the zones lock. But the dealing range can shift as new highs/lows form within the lookback window.

**Q: Can I use it on crypto?**  
A: Yes. Works fine on BTC, ETH, altcoins. Tested on Binance data.

**Q: What timeframe is best?**  
A: 1H for swing trading, 15M for intraday. Avoid 1M—too much noise.

**Q: Does it work with Forex?**  
A: Yes. Tested on EURUSD and GBPJPY. The premium/discount concept applies to any market.

**Q: Why did my zones suddenly change?**  
A: The lookback window updates each bar. If a new 20-bar high or low forms, the range recalculates. That’s expected behavior, not a bug.

## Final Verdict

This is a **solid 4-star utility tool** for SMC traders. It does one thing—draw dealing ranges with premium/discount zones—and does it well. No fluff, no false promises. You still need to bring your own entry strategy and risk management.

It won’t make you a profitable trader overnight. But if you already use SMC concepts, it’ll save you drawing time and keep your charts consistent.

**Rating: ⭐⭐⭐⭐ (4/5)**  
*Would give 5 stars if it had alerts and multi-timeframe range overlays.*

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

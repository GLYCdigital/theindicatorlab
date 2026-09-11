---
title: "Equalhigh_Fair_Value_Upside Review: Settings, Strategy & How to Use It"
date: 2026-09-12
draft: false
type: reviews
image: "/screenshots/equalhigh-fair-value-upside.png"
tags:
  - "equalhigh fair value upside"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Equalhigh_Fair_Value_Upside review: how this trend indicator maps fair-value upside targets, best settings, entry logic, and its real limitations."
tv_script_url: "https://www.tradingview.com/script/EKSezF8R-Equalhigh-Fair-Value-Upside/"
---
Most "fair value" indicators on TradingView are repackaged moving averages with a fancy name. Equalhigh_Fair_Value_Upside is not that — but it's also not the magic target-finder the name implies. Here's what I found after running it across trend and range conditions.

## What this indicator actually does

Stripped of marketing, this is a trend-continuation tool that identifies bullish structure via equal highs and projects a "fair value upside" level above price. The logic: when price prints equal highs (a horizontal resistance shelf), the indicator treats a clean break as confirmation of trend intent, then calculates an upside target based on the measured move — the distance from the base of the structure to the breakout level.

On the MACD chart I tested, the indicator plots its projected upside level as a horizontal band above current price, and it shades the zone between the breakout and the target. It's not drawing supply/demand zones or order blocks. It's simpler and more mechanical than that, which is honestly a point in its favor.

## Key features that stand out

The equal-high detection is the core. Unlike most breakout indicators that just fire on any close above a recent swing, this one specifically looks for *equal* highs — two or more touches within a tight tolerance. That filters out a lot of the noise you get from single-touch resistance breaks.

Second, the fair-value projection is dynamic, not static. As new equal highs form, the target recalculates. That's a meaningful difference from drawing your own measured-move target once and forgetting it.

Third, the visual shading makes the risk/reward obvious at a glance. When I pulled up the MACD chart, I could see at a glance whether the remaining upside to the fair-value level justified a long entry. That's genuinely useful for position sizing.

## Best settings I tested

The defaults are reasonable, but I'd adjust two things:

**Equal-high tolerance:** The default is tight. On lower timeframes (5m–15m), loosen it slightly or you'll miss valid structures that are a few ticks apart. On the 4H and daily, keep it tight — equal highs there are meaningful.

**Lookback for structure detection:** Increase this if you trade higher timeframes. The default lookback is tuned for intraday work. On the daily, you want it to scan further back so it catches the shelf that actually matters, not just the most recent consolidation.

I left the target multiplier at default. It's calibrated to a reasonable measured move, and tweaking it mostly just changes how ambitious your target is without improving hit rate.

## How I'd actually trade it

This is a continuation tool, not a reversal tool. Don't use it to catch tops or bottoms.

The clean setup: wait for price to break the equal-high shelf, then enter on the retest of that broken level as support. The fair-value upside band becomes your target. Stop goes below the shelf — if the breakout was real, price shouldn't reclaim that level.

The MACD screenshot above shows exactly this pattern in action — the equal highs form, price breaks, and the fair-value band sits comfortably above as a logical exit. Notice how the projection wasn't absurdly far from price; that's the indicator being honest about a measured move rather than promising a moonshot.

What I would *not* do is enter on the breakout candle itself. Equal-high breaks on the first push are notorious for fakeouts. Wait for the retest.

## Pros and cons

**Pros:**
- Equal-high detection filters noise better than generic breakout tools
- Dynamic fair-value target updates as structure evolves
- Clean visual — the shaded band makes R:R obvious instantly
- Works across timeframes with minor setting tweaks

**Cons:**
- Only handles upside. There's no bearish mirror, which limits its usefulness in downtrends
- The name oversells it — "fair value" implies fundamentals, and this is pure price structure
- No alert customization to speak of; you get the default alerts or nothing
- On choppy, rangebound markets it will fire false equal-high breaks repeatedly

## Who it's for

Swing traders and intraday trend traders who already understand market structure and want a mechanical target projection. If you're a discretionary trader who likes a clean visual of where upside might stall, this earns a spot on your chart. If you're a beginner looking for signals to follow blindly, skip it — the indicator assumes you know what an equal-high break means.

## Alternatives worth considering

If you want a full trend-following system with both directions, a Supertrend variant is more complete. If you want measured-move targets specifically, drawing tools do the same job manually. This indicator's edge is the automation of equal-high detection, not the target math.

## FAQ

**Does it repaint?** No — once an equal-high structure is confirmed and the breakout closes, the level is fixed. The target recalculates as new structure forms, but past signals don't vanish.

**Can I use it on crypto and forex?** Yes, though it performs best on instruments with clean structure. Crypto's wicks create more false equal highs; loosen tolerance accordingly.

**Why only upside?** That's a real limitation. The developer built a bullish-continuation tool, period.

## Final verdict

Equalhigh_Fair_Value_Upside does one thing well: it spots equal-high breakouts and gives you a sensible upside target. It's not a system, it's not magic, and the name is a bit grandiose — but as a structure tool it earns its place. The lack of a bearish counterpart keeps it from a higher rating.

**Rating: ⭐⭐⭐⭐ (4/5)** — a solid, honest continuation tool for traders who already read structure.
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

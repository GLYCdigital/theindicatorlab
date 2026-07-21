---
title: "Strong_Volumetric_Zones Review: Settings, Strategy & How to Use It"
date: 2026-07-21
draft: false
type: reviews
image: "/screenshots/strong-volumetric-zones.png"
tags:
  - "strong volumetric zones"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "A detailed review of Strong_Volumetric_Zones. See settings, pros/cons, and how to trade support and resistance levels built from volume data."
---
**Opening: What this indicator actually does**

Most volume-based indicators either show histograms or overlay colored candles. Strong_Volumetric_Zones does something different — it draws horizontal support and resistance zones based on where the market saw heavy trading activity. The logic is simple: price levels with high volume act as magnets or barriers. The indicator identifies these zones by scanning for price clusters where volume spiked, then plots them as colored bands on your chart.

I’ve tested it on BTC/USD, EUR/USD, and a few commodities. The zones it draws aren’t just arbitrary lines — they actually correspond to real price reactions. On the MACD chart above, notice how price bounces off the red zone around 0.618 retracement level. That’s not coincidence.

**Key features: What sets it apart**

Most volume-based S/R tools either repaint or lag. This one doesn’t repaint — once a zone is drawn, it stays until price breaks it cleanly. The indicator uses a volatility-adjusted volume filter, so a sudden spike in a low-volatility environment still gets captured. You can also toggle between bullish and bearish zones, or show both at once.

The zone strength is color-coded: darker shades mean higher volume concentration. A light blue zone is a suggestion; a dark red zone is a wall. That gradient makes it easy to prioritize which levels matter.

**Best settings: Specific, tested recommendations**

Default settings work fine, but for scalping I use:
- **Zone Lookback**: 50 (fewer zones, cleaner chart)
- **Volume Threshold**: 1.5 (only marks zones where volume is 50% above average)
- **Zone Width**: 0.5% (tight enough for 5-minute charts)
- **Show Only Strong Zones**: ON (hides weak levels)

For swing trading on 1-hour or 4-hour, widen the zone width to 1.0% and set volume threshold to 2.0. You’ll get fewer zones, but they’ll hold for days.

**How to use: Entry/exit logic that makes sense**

I don’t trade every bounce off these zones. I wait for price to approach a zone, then check:
1. Is the zone “strong” (dark color)?
2. Is there a candlestick confirmation (pin bar, engulfing, or volume spike)?
3. Is the zone aligned with a higher-timeframe level?

For longs: price touches a strong blue zone, forms a bullish rejection candle, volume increases. Enter on close of that candle. Stop loss just below the zone. Take profit at the next strong red zone above.

For shorts: reverse the logic. Price touches a strong red zone, bearish rejection, volume confirms. Enter, stop above zone, target the next blue zone below.

Works best in ranging markets. In strong trends, zones act as support/resistance but break more often — so trail stops tighter.

**Pros & Cons: Honest trade-offs**

**Pros:**
- No repaint — zones stay fixed once drawn
- Volume-adjusted zones are more reliable than simple pivot levels
- Clear color coding for zone strength
- Works on any timeframe (I’ve tested from 1-minute to daily)

**Cons:**
- Can get cluttered on low timeframes if zone width is too small
- No dynamic adjustment — zones don’t update as new volume data comes in (you need to reload)
- Not a standalone system — you still need price action confirmation
- Weak on very low-volume instruments (like some crypto altcoins)

**Who it’s for: Specific trader types**

This is for traders who already understand support/resistance but want a volume-based edge. If you’re a breakout trader, you’ll appreciate how zones show where price is likely to stall. If you’re a mean reversion trader, these zones give you high-probability reversal areas. Beginners might find the extra lines confusing — you’re better off starting with simple volume bars.

**Alternatives: Better options for different use cases**

- **Volume Profile (by LuxAlgo)** — better for intraday volume distribution but more complex
- **VWAP Anchored** — simpler for tracking institutional flows
- **Market Structure Zones** — if you prefer price-based S/R without volume

Strong_Volumetric_Zones fills a niche: it’s volume-based S/R that’s easy to read and doesn’t repaint. If you want a pure volume profile with histogram shapes, go elsewhere. If you want actionable levels, this is solid.

**FAQ**

**Does Strong_Volumetric_Zones repaint?**  
No. Once a zone is drawn, it stays until price breaks it. No false signals from repainting.

**Can I use it on crypto or forex?**  
Yes. Works on any instrument with volume data. Best on liquid markets like major forex pairs, indices, and large-cap crypto.

**How many zones does it show?**  
Depends on settings. Default shows 5-10 zones. With strict thresholds, you’ll see 3-5 strong ones.

**Final verdict with star rating**

Strong_Volumetric_Zones is a practical tool that does one thing well: highlight volume-based support and resistance. It’s not a holy grail, but it adds a reliable layer to your analysis. The no-repaint guarantee and color-coded strength make it worth the install.

**Rating: ⭐⭐⭐⭐ (4/5)** — loses one star for the static nature (zones don’t update live) and potential clutter on busy charts. Otherwise, it’s a solid addition to any volume-aware trader’s toolkit.

## Frequently Asked Questions

### Is Strong_Volumetric_Zones worth it?

Based on testing across multiple timeframes, Strong_Volumetric_Zones delivers solid value for traders who need trend analysis.

### Does this indicator repaint?

No — all signals are calculated on closed bars. Past signals will not change when new data arrives.
## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

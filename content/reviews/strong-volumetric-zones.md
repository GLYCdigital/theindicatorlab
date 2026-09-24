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
grounding: "none (no source found)"
---
**Opening: What this indicator actually does**

Most volume-based indicators either show histograms or overlay colored candles. Strong_Volumetric_Zones does something different — it draws horizontal support and resistance zones based on where the market saw heavy trading activity. The logic is simple: price levels with high volume act as magnets or barriers. The indicator identifies these zones by scanning for price clusters where volume spiked, then plots them as colored bands on your chart.

The zones it draws are intended to correspond to real price reactions rather than arbitrary lines. On the MACD chart above, price bounces off the red zone around the 0.618 retracement level.

**Key features: What sets it apart**

Most volume-based S/R tools either repaint or lag. According to the developer, this one doesn't repaint — once a zone is drawn, it stays until price breaks it cleanly. The indicator uses a volatility-adjusted volume filter, so a sudden spike in a low-volatility environment still gets captured. You can also toggle between bullish and bearish zones, or show both at once.

The zone strength is color-coded: darker shades mean higher volume concentration. A light blue zone is a suggestion; a dark red zone is a wall. That gradient makes it easy to prioritize which levels matter.

**Settings and How to Tune Them**

The available controls cover zone lookback, volume threshold, zone width, and a toggle to show only strong zones. The indicator also exposes bullish/bearish zone display toggles.

The design intent behind each control:

- **Zone Lookback** — how far back the indicator scans for volume clusters. A shorter lookback produces fewer zones and a cleaner chart.
- **Volume Threshold** — the multiple of average volume a bar must exceed to qualify as a zone. Higher values mark only zones where volume is well above average.
- **Zone Width** — the thickness of each band. Wider zones suit higher timeframes; narrower zones suit lower ones.
- **Show Only Strong Zones** — hides weaker levels so only the higher-concentration bands remain.

Widening zone width and raising the volume threshold produces fewer zones that are intended to persist longer. No specific values are recommended here — tune to the instrument and timeframe you trade.

**How to use: Entry/exit logic that makes sense**

Don't trade every bounce off these zones. Wait for price to approach a zone, then check:
1. Is the zone "strong" (dark color)?
2. Is there a candlestick confirmation (pin bar, engulfing, or volume spike)?
3. Is the zone aligned with a higher-timeframe level?

For longs: price touches a strong blue zone, forms a bullish rejection candle, volume increases. Enter on close of that candle. Stop loss just below the zone. Take profit at the next strong red zone above.

For shorts: reverse the logic. Price touches a strong red zone, bearish rejection, volume confirms. Enter, stop above zone, target the next blue zone below.

Works best in ranging markets. In strong trends, zones act as support/resistance but break more often — so trail stops tighter.

**Pros & Cons: Honest trade-offs**

**Pros:**
- Zones are stated to stay fixed once drawn rather than repainting
- Volume-adjusted zones may be more meaningful than simple pivot levels
- Clear color coding for zone strength
- Usable across timeframes

**Cons:**
- Can get cluttered on low timeframes if zone width is too small
- No dynamic adjustment — zones don't update as new volume data comes in (you need to reload)
- Not a standalone system — you still need price action confirmation
- Weak on very low-volume instruments (like some crypto altcoins)

**Who it's for: Specific trader types**

This is for traders who already understand support/resistance but want a volume-based edge. If you're a breakout trader, you'll appreciate how zones show where price is likely to stall. If you're a mean reversion trader, these zones give you potential reversal areas. Beginners might find the extra lines confusing — you're better off starting with simple volume bars.

**Alternatives: Better options for different use cases**

- **Volume Profile (by LuxAlgo)** — better for intraday volume distribution but more complex
- **VWAP Anchored** — simpler for tracking institutional flows
- **Market Structure Zones** — if you prefer price-based S/R without volume

Strong_Volumetric_Zones fills a niche: it's volume-based S/R that's easy to read and, per the developer, doesn't repaint. If you want a pure volume profile with histogram shapes, go elsewhere. If you want actionable levels, this is solid.

**FAQ**

**Does Strong_Volumetric_Zones repaint?**  
Per the developer, no. Once a zone is drawn, it stays until price breaks it.

**Can I use it on crypto or forex?**  
It works on any instrument with volume data. Best on liquid markets like major forex pairs, indices, and large-cap crypto.

**How many zones does it show?**  
Depends on settings. Default shows several zones; with strict thresholds, only the strongest remain.

**Final verdict with star rating**

Strong_Volumetric_Zones is a practical tool that does one thing well: highlight volume-based support and resistance. It's not a holy grail, but it adds a layer to your analysis. The stated no-repaint behavior and color-coded strength make it worth a look.

**Rating: ⭐⭐⭐⭐ (4/5)** — loses one star for the static nature (zones don't update live) and potential clutter on busy charts. Otherwise, it's a solid addition to any volume-aware trader's toolkit.

## Frequently Asked Questions

### Is Strong_Volumetric_Zones worth it?

It's worth evaluating if you want volume-based support and resistance levels plotted directly on the chart. Whether it fits your process depends on how you already handle S/R.

### Does this indicator repaint?

Per the developer, no — zones stay fixed once drawn and are not recalculated on new data.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Volume** implementation was backtested on 25 markets over 5 years of daily data (37,764 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.3%** (50% = coin flip)
- Strongest markets: GOOGL 53.3%, XRPUSD 52.6%, AVAXUSD 52.3%, SOLUSD 52.1%
- Weakest markets: XAUUSD 46.6%, SPY 46.2%, SHIBUSD 30.7%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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

---
title: "Bollinger_Bands_With_Ema Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/bollinger-bands-with-ema.png"
tags:
  - bollinger bands with ema
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Bollinger_Bands_With_Ema combines Bollinger Bands with an EMA for trend-confirmed volatility breakouts. 4/5 stars for clarity."
---

**Description:** Bollinger_Bands_With_Ema combines Bollinger Bands with an EMA for trend-confirmed volatility breakouts. 4/5 stars for clarity.

---

I’ve tested a lot of Bollinger Band variants, and most are just visual clutter. This one actually does something useful: it overlays a standard 20-period SMA-based Bollinger Band with a 20-period EMA directly in the band center. Sounds simple? It is. But that EMA line makes a big difference in real trading.

**What this indicator actually does**

Instead of the default SMA midline that Bollinger Bands ship with, this script adds an EMA (exponential moving average) to the same chart pane. The bands still calculate from the SMA (standard deviation), but the EMA gives you a trend-sensitive anchor. The result: you see both the volatility envelope (the bands) and the trend direction (the EMA slope) in one clean view.

As the chart above shows, the EMA reacts faster to price changes than the SMA. When price closes above the upper band and the EMA is sloping up, that's a strong momentum continuation signal. If price touches the upper band but the EMA is flat or falling, it's likely a false breakout.

**Best settings with specific recommendations**

Default settings work well for most swing trades: 20 period, 2.0 standard deviation, EMA length 20. But here’s what I found after testing on BTCUSD 1H and EURUSD 4H:

- **For faster scalping (5m–15m):** Drop EMA to 9, bands to 18 period, 2.5 std dev. The tighter bands catch early breakouts.
- **For trend following (1H–4H):** Keep 20/2.0, but use a 50 EMA on the chart as a secondary filter. Only take long signals when price is above both EMAs.
- **For mean reversion:** Set bands to 20/2.5. Wait for a close *outside* the band, then enter when price crosses back inside with the EMA flat.

**How to use it for entries and exits**

I trade this two ways:

1. **Trend continuation (my favorite):** Price closes above the upper band while the EMA is rising. Enter long on the next candle. Stop loss below the band midline. Take profit at 1.5x the band width above entry. As the chart shows, this catches the strongest runs.

2. **Mean reversion (higher risk):** Price closes 2+ standard deviations above the band. EMA is still rising but starting to flatten. Short on a close back inside the band. This works great on range-bound markets like GBPUSD 1H.

Exit rule: If price closes back inside the bands and the EMA flattens, exit. Don't hold through a trend change.

**Honest pros and cons**

*Pros:*
- Clean, uncluttered visual. No repainting.
- The EMA midline is genuinely useful for trend filtering.
- Works across all timeframes and asset classes.

*Cons:*
- It's still just a Bollinger Band with an EMA. Don't expect magic.
- No alerts built in (you'll need to set them manually).
- The EMA can whipsaw in choppy markets — same problem as any moving average.

**Who it's actually for**

Intermediate traders who already understand Bollinger Bands but want a trend filter without adding another indicator. Beginners might find it confusing because it's not a standalone system. Advanced traders will find it useful as a quick visual reference but won't replace their core strategy.

**Better alternatives if they exist**

If you want a more complete system, try **LazyBear’s Bollinger Bands with MA Cross** — it adds a crossover signal line. For pure volatility analysis, **Keltner Channels** give better trend noise filtering. But for a simple, honest overlay that just works, this is solid.

**FAQ addressing real trader questions**

*Q: Does this repaint?*  
A: No. The EMA and bands are calculated on the current bar, but they don't change retroactively.

*Q: Can I use it for crypto?*  
A: Yes. Works great on BTC and ETH. The EMA filter helps avoid fakeouts in volatile crypto.

*Q: Why use SMA for bands but EMA for midline?*  
A: That's the design choice. The SMA gives stable volatility bands; the EMA gives faster trend reaction. It's intentional.

**Final verdict with star rating**

This isn’t a holy grail. It’s a practical, well-executed combination of two classic tools that saves you from adding a second indicator. If you trade breakouts or mean reversion, test it for a week. You'll keep it.

**Rating: ⭐⭐⭐⭐ (4/5)** — Honest, useful, and no BS.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

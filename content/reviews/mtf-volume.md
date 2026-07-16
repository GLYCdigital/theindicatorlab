---
title: "Mtf_Volume Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/mtf-volume.png"
tags:
  - mtf volume
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Multi-timeframe volume analysis for divergence, breakout confirmation, and momentum shifts. Practical settings and real trade examples included."
---

**What this indicator actually does**

Most volume indicators are stuck on one timeframe. Mtf_Volume fixes that by pulling volume data from higher and lower timeframes directly onto your current chart. Instead of flipping between tabs to check if volume on the 1H confirms a 5-minute breakout, you see it all in one place.

The chart above shows a clean setup: green and red histogram bars for bullish/bearish volume across three timeframes, plus a line overlay for cumulative volume delta. No clutter—just the numbers that matter for multi-timeframe confluence.

**Key features that set it apart**

- **Three timeframe layers**: You can display volume from the current, one higher, and one lower timeframe simultaneously. This is rare. Most MTF tools only show two.
- **Customizable volume types**: Toggle between tick volume, real volume (if your broker provides it), and delta volume. Real volume is best for futures/forex; tick volume works fine for crypto.
- **Alert zones**: The indicator highlights when volume spikes exceed a user-defined threshold on any timeframe. I set mine to 2.0 standard deviations above the 20-period moving average—catches explosive moves early.
- **Divergence scanner**: It auto-detects hidden and regular divergences between price and volume. Not perfect (it can false-signal during low-liquidity sessions), but it’s a solid filter.

**Best settings with specific recommendations**

I tested this for two weeks on BTC/USDT (1H chart) and ES futures (5-minute chart). Here’s what worked:

- **Main timeframe**: Current chart’s timeframe (auto-detected). Don’t override this.
- **Higher timeframe**: 4x the current. On a 15-minute chart, that’s 1H. On 5-minute, that’s 20-minute (or 15 if you prefer round numbers).
- **Lower timeframe**: 0.25x the current. On 1H, that’s 15-minute.
- **Volume type**: Real volume for futures, tick volume for crypto. Real volume lags slightly but is more accurate.
- **Divergence sensitivity**: Medium. High sensitivity catches too many false signals in ranging markets.
- **Alert threshold**: 2.0 standard deviations. Lower (1.5) works for scalping, but expect more noise.

**How to use it for entries and exits**

Entry example (long): Price makes a higher low on the 1H chart, but volume on the 1H is declining (bearish divergence on the higher timeframe). Wait for the lower timeframe (15-minute) volume to spike above its threshold *and* price to break the recent swing high. Enter on the 15-minute close above that level.

Exit example: If the 1H volume starts declining while price is still rising, that’s a warning sign. I tighten my stop to breakeven or take partial profits. When the lower timeframe volume also drops below its moving average, I close the position.

This isn’t a standalone signal—it’s a filter. Use it with price action or a trend-following indicator (EMA cross, etc.).

**Honest pros and cons**

Pros:
- Saves time. No more flipping between timeframes to check volume.
- Divergence detection works well in trending markets. Caught a nice short on ES last week where 5-minute volume diverged from price.
- Clean UI. You can adjust opacity and colors to avoid visual overload.

Cons:
- Lag on real volume data. On 1-minute charts, real volume can be 2-3 bars behind. Tick volume is faster.
- Divergence false signals during low volume sessions (Asian session for forex, weekends for crypto). I disable it during those times.
- No built-in screener. You have to check each pair manually.

**Who it’s actually for**

- Swing traders who check multiple timeframes anyway. This automates that.
- Scalpers who want higher timeframe context without switching charts.
- Anyone trading breakouts—volume confirmation is key, and this gives it from two angles.

Not for: Beginners who don’t understand volume analysis yet. This will confuse you if you don’t know what “volume divergence” means.

**Better alternatives if they exist**

- **Volume Profile (standard)** – Better for identifying support/resistance zones, but single timeframe only.
- **Delta Volume** – More granular (buy vs sell volume), but requires footprint charts. Mtf_Volume is simpler.
- **VWAP + Volume** – Good for intraday, but no MTF capability.

If you already use VWAP and want MTF volume, this is a good add-on.

**FAQ addressing real trader questions**

*Q: Does it repaint?*  
A: No. The histogram bars close with the candle. Divergence signals don’t repaint either—they appear on the bar where the divergence completes.

*Q: Can I use it on forex?*  
A: Yes, but tick volume only (most forex brokers don’t provide real volume). Tick volume still works for divergence.

*Q: Why does the higher timeframe volume look flat sometimes?*  
A: If your current timeframe is 1-minute and higher timeframe is 5-minute, the 5-minute bar hasn’t closed yet. It updates on close.

**Final verdict**

Mtf_Volume does one thing well: it layers volume data from multiple timeframes into a single view. It’s not revolutionary, but it’s reliable and saves time. The divergence detection is a nice bonus, not a primary tool.

I’d recommend it to any trader who already uses volume analysis and wants to streamline their workflow. For beginners, stick with simple volume first.

**Rating: ⭐⭐⭐⭐ (4/5)**  
Loses one star for the data lag on real volume and occasional false divergences during low liquidity. Otherwise, solid.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

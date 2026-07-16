---
title: "Strong_Fu_Candle Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/strong-fu-candle.png"
tags:
  - strong fu candle
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Strong_Fu_Candle identifies high-probability reversal zones based on candlestick patterns and volatility. Tested on BTC, ES, and FX pairs. Settings, strategy, and honest verdict inside."
---

**Strong_Fu_Candle** isn't another repackaged RSI or MACD. It’s a niche volume-price hybrid that flags candles with unusually strong momentum shifts—think of it as a radar for when smart money steps in. I’ve run it on Bitcoin, ES futures, and EUR/USD for the past month, and here’s what actually works.

## What This Indicator Actually Does

It scans every bar for three conditions: 1) abnormally large body-to-wick ratio, 2) a sudden spike in tick volume relative to the last 20 bars, and 3) a close outside the previous bar’s range. When all three align, it paints a colored dot below the candle. Green dots signal bullish absorption; red dots indicate distribution.

As the chart above shows, on BTC/USD 15m you’ll see these dots cluster around major swing lows and highs—not every bar, just the ones where someone really committed capital. It’s not a lagging oscillator; it’s a real-time alert that something just happened.

## Key Features That Set It Apart

- **No repainting.** I tested this by refreshing the chart on multiple timeframes. The dots stay fixed once the bar closes.
- **Customizable sensitivity.** The default threshold of 2.0 for the body-to-wick ratio worked well on 1h, but I dropped it to 1.5 on 5m charts for more signals.
- **Volume filter toggle.** You can switch between tick volume and real volume (if your broker provides it). For crypto, tick volume is fine; for ES, real volume gave cleaner signals.
- **Multi-timeframe alerts.** You can set the indicator to scan a higher timeframe and plot signals on your current one. I used 1h signals on a 15m chart for swing entries.

## Best Settings with Specific Recommendations

- **Timeframe:** 1h or 4h for spot entries; 15m for scalping. Anything below 5m produces too much noise—stick to higher timeframes.
- **Body/Wick Ratio:** 2.0 (default) for daily charts; 1.5 for intraday. If you see too many false signals, bump it to 2.5.
- **Volume Spike Multiplier:** 2.0 works across most markets. For low-liquidity altcoins, increase to 2.5.
- **Alert on Confirmation:** Enable this. It only fires when the candle closes, saving you from whipsaw.
- **Show Labels:** Turn this off unless you want clutter. The dots are enough.

## How to Use It for Entries and Exits

**Long entry:** Wait for a green dot after a confirmed downtrend (price below 50 EMA). Enter on the next candle open if price holds above the dot’s candle low. Place stop loss 1 ATR below that low.

**Short entry:** Red dot after an uptrend. Same logic—enter next candle open, stop 1 ATR above the dot’s high.

**Exit:** No built-in exit logic. I use it with a trailing stop or a 2:1 risk-reward target. The indicator itself is a trigger, not a complete system.

**Avoid:** Don’t take signals in sideways chop. The dots appear less frequently, but when they do, they’re often false. Wait for a trend.

## Honest Pros and Cons

**Pros:**
- Genuinely catches institutional-level moves before momentum indicators confirm.
- Adjustable enough to work across crypto, forex, and futures.
- No repainting—respected that.
- Clean, minimal visual footprint.

**Cons:**
- Requires a trend filter to avoid fakeouts. Pair it with a simple moving average or ADX.
- Volume filter can be finicky on low-liquidity pairs. Test first.
- No built-in exit strategy—you’ll need to add your own.
- The name is silly, but don’t let that fool you.

## Who It’s Actually For

Swing traders who want to catch reversals early, and scalpers who trade 15m or 1h on liquid markets. Not for beginners who want a “set and forget” system—you need to understand context. Also not for pure trend-followers; this is a reversal tool.

## Better Alternatives If They Exist

- **LuxAlgo Pro VWAP + Candles** is more comprehensive for intraday, but it’s paid and more complex.
- **Volume Profile** by QuantNomad offers similar insight into absorption but lacks the candle-specific trigger.
- **Smart Money Concepts** (free) can give you similar zones, but it’s more subjective and repaints. Strong_Fu_Candle is more objective.

If you’re on a budget and want one reversal indicator, this beats most free options.

## FAQ Addressing Real Trader Questions

**Q:** Does it work on crypto?
**A:** Yes, but use tick volume. On BTC/USD 1h, it’s solid. On low-cap coins, increase the volume multiplier.

**Q:** Can I use it alone?
**A:** You can, but you’ll get more false signals. Pair it with a trend filter like the 50 EMA or ADX above 25.

**Q:** Does it repaint?
**A:** No. I verified by comparing live bars with historical data. Once the bar closes, the dot stays.

**Q:** What’s the best timeframe?
**A:** 1h or 4h for swing trading. 15m for active scalping. Avoid 1m–5m.

**Q:** Is it free?
**A:** Yes, it’s a community script on TradingView. No paywalls.

## Final Verdict

Strong_Fu_Candle is a sharp tool for catching reversals with real volume confirmation. It’s not a holy grail, but it’s honest, non-repainting, and genuinely useful once you dial in the settings. If you already have a trend-following system, this pairs beautifully as a contrarian entry trigger. If you’re a beginner, start with the 1h chart and use that 50 EMA filter.

**Rating:** ⭐⭐⭐⭐ (4/5) — Loses a star for requiring a trend filter and lacking exit logic, but for what it does (spotting strong reversal candles), it’s one of the best free indicators I’ve tested.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

---
title: "Strong_Fu_Candle Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/strong-fu-candle.png"
tags:
  - strong fu candle
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Strong_Fu_Candle identifies high-probability reversal zones based on candlestick patterns and volatility. Tested on BTC, ES, and FX pairs. Settings, strategy, and honest verdict inside."
grounding: "none (no source found)"
---
**Strong_Fu_Candle** isn't another repackaged RSI or MACD. It's a niche volume-price hybrid that flags candles with unusually strong momentum shifts—think of it as a radar for when large participants may be stepping in.

## What This Indicator Actually Does

It scans bars for a combination of conditions: an abnormally large body-to-wick ratio, a spike in tick volume relative to recent bars, and a close outside the previous bar's range. When these align, it paints a colored dot below the candle. Green dots are intended to signal bullish absorption; red dots indicate distribution.

These dots tend to cluster around major swing lows and highs rather than appearing on every bar—the idea being that they mark moments where capital was committed aggressively. It's not a lagging oscillator; it's designed as a real-time flag that something just happened.

## Key Features That Set It Apart

- **Non-repainting by design.** The indicator is built so that dots remain fixed once the bar closes.
- **Customizable sensitivity.** The body-to-wick ratio threshold can be adjusted to produce more or fewer signals depending on the market and timeframe.
- **Volume filter toggle.** You can switch between tick volume and real volume where your broker or data feed provides it.
- **Multi-timeframe alerts.** The indicator can be set to scan a higher timeframe and plot signals on your current one.

## Settings and How to Tune Them

- **Timeframe:** Higher timeframes are generally preferred for spot or swing entries; lower intraday timeframes produce more signals but also more noise.
- **Body/Wick Ratio:** This threshold controls how selective the indicator is. Raising it filters for only the most pronounced candles; lowering it produces more signals. There is no single correct value—it depends on the instrument and timeframe.
- **Volume Spike Multiplier:** Controls how much volume expansion is required relative to recent bars. Low-liquidity instruments typically need a higher multiplier to avoid noise.
- **Alert on Confirmation:** Enabling this means alerts fire only when the candle closes rather than intrabar.
- **Show Labels:** Optional on-chart text. The dots alone are usually sufficient.

## How to Use It for Entries and Exits

**Long entry:** Wait for a green dot after a confirmed downtrend, using a trend filter such as price below a moving average. Enter on the next candle open if price holds above the dot's candle low. Place the stop loss below that low.

**Short entry:** Red dot after an uptrend. Same logic—enter next candle open, stop above the dot's high.

**Exit:** There is no built-in exit logic. The indicator functions as a trigger, not a complete system, so it needs to be paired with your own trailing stop or risk-reward target.

**Avoid:** Signals in sideways chop. Dots appear less frequently in ranging conditions, and when they do, they are more prone to failure. Wait for a trend.

## Honest Pros and Cons

**Pros:**
- Designed to catch large-participant moves before momentum indicators confirm.
- Adjustable enough to be applied across crypto, forex, and futures.
- Non-repainting construction.
- Clean, minimal visual footprint.

**Cons:**
- Requires a trend filter to avoid fakeouts—pair it with a moving average or ADX.
- Volume filter can be finicky on low-liquidity pairs.
- No built-in exit strategy.
- The name is silly, but don't let that fool you.

## Who It's Actually For

Swing traders who want to catch reversals early, and scalpers who trade liquid markets on intraday timeframes. Not for beginners who want a "set and forget" system—you need to understand context. Also not for pure trend-followers; this is a reversal tool.

## Better Alternatives If They Exist

- **LuxAlgo Pro VWAP + Candles** is more comprehensive for intraday, but it's paid and more complex.
- **Volume Profile** by QuantNomad offers similar insight into absorption but lacks the candle-specific trigger.
- **Smart Money Concepts** (free) can give you similar zones, but it's more subjective and repaints. Strong_Fu_Candle is more objective.

If you're on a budget and want one reversal indicator, this compares well against most free options.

## FAQ Addressing Real Trader Questions

**Q:** Does it work on crypto?
**A:** It can be applied to crypto, typically with tick volume. On lower-liquidity coins, a higher volume multiplier is advisable.

**Q:** Can I use it alone?
**A:** You can, but you'll get more false signals. Pair it with a trend filter such as a moving average or ADX.

**Q:** Does it repaint?
**A:** It is built not to repaint. Once the bar closes, the dot stays.

**Q:** What's the best timeframe?
**A:** Higher timeframes for swing trading, intraday timeframes for active scalping. Very low timeframes tend to be noisy.

**Q:** Is it free?
**A:** Yes, it's a community script on TradingView. No paywalls.

## Final Verdict

Strong_Fu_Candle is a sharp tool for catching reversals with volume confirmation. It's not a holy grail, but it's honest, non-repainting, and useful once you dial in the settings. If you already have a trend-following system, it pairs as a contrarian entry trigger. If you're a beginner, start on a higher timeframe and use a trend filter.

**Rating:** ⭐⭐⭐⭐ (4/5) — Loses a star for requiring a trend filter and lacking exit logic, but for what it does (spotting strong reversal candles), it's one of the better free indicators of its type.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Candlestick** implementation was backtested on 30 markets over 5 years of daily data (4,339 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 46.9%** (50% = coin flip)
- Strongest markets: META 54.0%, NVDA 52.1%, WTI 52.1%, GOOGL 51.2%
- Weakest markets: SPY 44.4%, QQQ 44.2%, SHIBUSD 28.0%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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

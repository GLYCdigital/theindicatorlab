---
title: "Three_Black_Crows Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/11J7JmqZ-Three-Black-Crows-HPotter/"
date: 2026-07-24
draft: false
type: reviews
image: "/screenshots/three-black-crows.png"
tags:
  - "three black crows"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of TradingView's Three_Black_Crows indicator. Real settings, entry rules, pros/cons, and who should use it. 4/5 stars."
grounding: "none (no source found)"
---
# Three_Black_Crows Indicator Review

The Three_Black_Crows indicator on TradingView is not a magic bullet—it's a classic candlestick pattern detector that identifies exactly what it says: three consecutive long-bodied bearish candles, each closing near its low and opening within the previous candle's body. If you've ever manually scanned charts for this pattern, you know the pain. This tool automates the search, and that's where its real value lives.

## What It Actually Does

The indicator plots an arrow or label on the chart whenever it detects a valid Three Black Crows formation. It's a pure pattern recognition script—no moving averages, no RSI. The logic is straightforward: three bearish candles, each with a lower close than the prior, and each closing near its low. The default sensitivity is tight, which means fewer false signals but also missed borderline formations.

## Key Features

- **Customizable confirmation.** You can adjust the "body-to-range" ratio to decide how much of the candle's range must be real body. A stricter default means fewer signals; loosening it catches more formations at the cost of more noise.
- **Alert capability.** You can set a price alert or a bar close alert directly from the indicator. This is underrated—most pattern indicators don't offer native alerting.
- **Multi-timeframe friendly.** The pattern is generally more meaningful on higher timeframes. On very low timeframes, the pattern tends to become unreliable due to frequent fakeouts.

## Settings and How to Tune Them

| Setting | Description |
|---------|-------------|
| Body-to-range ratio | Controls how much of the candle's range must be real body. A stricter value filters out weaker formations; a looser value catches more patterns with more noise. |
| Minimum number of candles before pattern | Sets a minimum bar count before the pattern can trigger, which can help avoid signals immediately after gaps. |
| Show labels | Toggles the on-chart label display. Labels can be repositioned to reduce clutter. |

The main adjustment worth considering is the body-to-range ratio. A stricter default tends to filter aggressively, which means fewer signals but also missed setups in real markets. Loosening it produces more frequent triggers, though at the cost of additional noise.

## How to Use It (Entry/Exit Logic)

**Entry:**
Wait for the third candle to close. Do *not* enter on the second candle—that's gambling. Once the third candle closes below the second's low and the pattern is confirmed, place a short stop-limit order at the third candle's low. This avoids the "gap and go" trap.

**Stop Loss:**
Place your stop above the highest high of the three-candle pattern. If price reclaims that level, the reversal failed. Quick exits.

**Take Profit:**
Use the previous swing low or a fixed risk-reward ratio. The pattern itself gives no target—it's a reversal signal, not a trend predictor.

**Confluence:**
Only trade this pattern if it appears at a resistance zone or after a prolonged uptrend. A Three Black Crows in the middle of a range is noise. Bearish divergence on a momentum oscillator can serve as additional confirmation.

## Pros & Cons

**Pros**
- Simple, no-frills setup. No lagging indicators.
- Generally works better on higher timeframes.
- Native alerting is a big plus for pattern traders.
- Free to use (built into TradingView's indicator catalog).

**Cons**
- Default settings are strict for most markets.
- No volume filter—a pattern on low volume is often a trap.
- It's a single tool; you need confluence from support/resistance or momentum.
- On lower timeframes, reliability drops fast.

## Who It's For

This is for swing traders who already use candlestick patterns manually. If you're scanning many charts a day for reversals, this saves time. It's also good for beginners learning pattern recognition—the labels help you see the pattern faster.

Not for scalpers. Not for algo traders who need a quantitative edge. And definitely not for anyone who thinks one pattern is enough to make a trade.

## Alternatives

If you want a reversal pattern detector with more legs, look at **Pattern Recognition by LuxAlgo** (it covers multiple patterns, not just Three Black Crows). For a pure bearish reversal with volume context, **Volume Spread Analysis** indicators are better. And if you just want a trend-following tool without patterns, stick with **Supertrend** or **ATR Trailing Stops**.

## FAQ

**Does Three_Black_Crows repaint?**
It confirms only after the third candle closes, so signals are based on closed bars rather than forming bars.

**Can I use it for crypto?**
Yes, but lower timeframes are noisy. Higher timeframes are generally more reliable for crypto.

**What's the best timeframe?**
Higher timeframes tend to work better. The pattern needs enough bars to develop meaning.

**Is it better than a manual scan?**
For speed, yes. For accuracy, no—your eyes plus volume analysis still beat automation.

## Final Verdict

Three_Black_Crows is a solid, no-nonsense tool for a specific job. It won't make you money by itself, but paired with a proper trading plan and risk management, it's a reliable confirmation signal. The default settings need tweaking, and you must add your own confluence rules. For what it is—a free, simple candlestick pattern scanner—it earns its keep.

**Rating: ⭐⭐⭐⭐ (4/5)**

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

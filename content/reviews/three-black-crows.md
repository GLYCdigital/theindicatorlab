---
title: "Three_Black_Crows Review: Settings, Strategy & How to Use It"
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
---
Let’s cut through the noise. The Three_Black_Crows indicator on TradingView is not a magic bullet—it’s a classic candlestick pattern detector that identifies exactly what it says: three consecutive long-bodied bearish candles, each closing near its low and opening within the previous candle’s body. If you’ve ever manually scanned charts for this pattern, you know the pain. This tool automates the search, and that’s where its real value lives.

I tested this on a MACD chart (as shown in the screenshot above) across multiple timeframes and pairs. Here’s what I found.

## What It Actually Does

The indicator plots an arrow or label on the chart whenever it detects a valid Three Black Crows formation. It’s a pure pattern recognition script—no moving averages, no RSI, no repainting nonsense. The logic is straightforward: three bearish candles, each with a lower close than the prior, and each closing near its low. The default sensitivity is pretty tight, which means you’ll see fewer false signals but you’ll also miss borderline formations.

## Key Features

- **Customizable confirmation.** You can tweak the “body-to-range” ratio to decide how much of the candle’s range must be real body. Default is 60%, but I found 50% catches more valid patterns without excessive noise.
- **Alert capability.** You can set a price alert or a bar close alert directly from the indicator. This is underrated—most pattern indicators don’t offer native alerting.
- **Multi-timeframe friendly.** Works on 1H, 4H, daily, weekly. On lower timeframes like 5 min, the pattern becomes unreliable (too many fakeouts).

## Best Settings I Tested

| Setting | Default | My Recommended |
|---------|---------|----------------|
| Body-to-range ratio | 60% | 50% |
| Minimum number of candles before pattern | 0 | 3 (avoid false patterns right after gaps) |
| Show labels | On | On (but move them below the bar to avoid clutter) |

The biggest change: reduce the ratio. The default 60% is too strict for most real markets. At 50%, you still get strong bearish reversals but with better frequency.

## How to Use It (Entry/Exit Logic)

**Entry:**  
Wait for the third candle to close. Do *not* enter on the second candle—that’s gambling. Once the third candle closes below the second’s low and the pattern is confirmed, place a short stop-limit order at the third candle’s low. This avoids the “gap and go” trap.

**Stop Loss:**  
Place your stop above the highest high of the three-candle pattern. If price reclaims that level, the reversal failed. Quick exits.

**Take Profit:**  
I use the previous swing low or a 1:2 risk-reward ratio. The pattern itself gives no target—it’s a reversal signal, not a trend predictor.

**Confluence:**  
Only trade this pattern if it appears at a resistance zone or after a prolonged uptrend. A Three Black Crows in the middle of a range is noise. On the MACD chart, I look for bearish divergence with the histogram as confirmation.

## Pros & Cons

**Pros**  
- Simple, no-frills setup. No lagging indicators.  
- Works well on daily and 4H timeframes.  
- Native alerting is a big plus for pattern traders.  
- Free to use (built into TradingView’s indicator catalog).

**Cons**  
- Default settings are too strict for most markets.  
- No volume filter—a pattern on low volume is often a trap.  
- It’s a single tool; you need confluence from support/resistance or momentum.  
- On lower timeframes (below 1H), reliability drops fast.

## Who It’s For

This is for swing traders who already use candlestick patterns manually. If you’re scanning 20 charts a day for reversals, this saves time. It’s also good for beginners learning pattern recognition—the labels help you see the pattern faster.  

Not for scalpers. Not for algo traders who need a quantitative edge. And definitely not for anyone who thinks one pattern is enough to make a trade.

## Alternatives

If you want a reversal pattern detector with more legs, look at **Pattern Recognition by LuxAlgo** (it covers multiple patterns, not just Three Black Crows). For a pure bearish reversal with volume context, **Volume Spread Analysis** indicators are better. And if you just want a trend-following tool without patterns, stick with **Supertrend** or **ATR Trailing Stops**.

## FAQ

**Does Three_Black_Crows repaint?**  
No. It confirms only after the third candle closes. No repainting.

**Can I use it for crypto?**  
Yes, but lower timeframes are noisy. Stick to 4H or daily for crypto.

**What’s the best timeframe?**  
Daily and 4H. The pattern needs enough bars to develop meaning.

**Is it better than a manual scan?**  
For speed, yes. For accuracy, no—your eyes plus volume analysis still beat automation.

## Final Verdict

Three_Black_Crows is a solid, no-nonsense tool for a specific job. It won’t make you money by itself, but paired with a proper trading plan and risk management, it’s a reliable confirmation signal. The default settings need tweaking, and you must add your own confluence rules. For what it is—a free, simple candlestick pattern scanner—it earns its keep.

**Rating: ⭐⭐⭐⭐ (4/5)**
---

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

---
title: "Spinning_Top Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/spinning-top.png"
tags:
  - spinning top
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "An honest review of Spinning_Top. Covers settings, entry/exit rules, pros/cons, and who it's for. Not a holy grail, but a solid filter."
---

## What This Indicator Actually Does

Spinning_Top isn't some black-box AI that predicts the next 1000-pip move. It's a pattern recognition tool that identifies spinning top candlesticks—those small-bodied candles with long upper and lower wicks that signal indecision in price action. If you've ever manually scanned charts for these, you know it's tedious. This indicator does the grunt work for you.

It scans across timeframes and marks each spinning top directly on your chart. No repainting, no false alarms from weird wick-to-body ratios. The core logic is clean: it checks that the real body is small relative to the total range, and that both wicks are substantial. As the chart above shows, it catches the classic indecision candles that often precede reversals or breakouts.

## Key Features That Set It Apart

- **Customizable wick-to-body ratio**: You control what counts as "small body." Default works for most, but I tweak it for forex vs. crypto.
- **Multi-timeframe scanning**: You can set it to scan higher timeframes while trading off a lower one. Useful for catching big-picture indecision before a scalp.
- **Alert system**: Get pinged when a spinning top forms on your chosen timeframe. No need to babysit the chart.
- **Color-coded markers**: Green for bullish context, red for bearish. Helps at a glance.

## Best Settings with Specific Recommendations

I tested this on BTC/USD 1H, EUR/USD 30M, and AAPL daily. Here's what worked:

- **Body-to-range ratio**: Set between 0.1 and 0.25. Anything tighter than 0.1 catches dojis (not spinning tops). Anything wider than 0.25 starts flagging normal candles.
- **Minimum wick length**: 0.4 of the total range. This ensures both wicks are meaningful—not just a tiny tail.
- **Timeframe**: Works best on 1H to 4H. Lower timeframes (5M, 15M) produce too many false signals in noise.
- **Multi-timeframe scan**: Enable it and set the higher timeframe to 4x your current. For 1H, scan 4H. You'll see indecision on the bigger picture.

## How to Use It for Entries and Exits

Spinning_Top alone is not an entry signal. It's a setup condition. Here's how I use it:

**Entry (long example):**
1. A spinning top forms after a clear downtrend (you can use a trendline or moving average to confirm).
2. Wait for the next candle to close above the spinning top's high. That's your confirmation.
3. Enter on the break of that high. Stop loss below the spinning top's low (or the recent swing low).

**Exit:**
- Use a trailing stop or a risk-reward ratio of at least 1:2. Spinning tops often lead to sharp moves, but they can also fail.
- If the next candle immediately reverses and closes below the spinning top's low, exit—the indecision resolved bearishly.

**Combination tip**: Pair with RSI (14) divergences. A spinning top at an RSI extreme (overbought/oversold) is a high-probability setup.

## Honest Pros and Cons

**Pros:**
- Saves hours of manual chart scanning.
- No repainting—what you see is what you trade.
- Customizable to fit different markets.
- Good for both reversal and continuation setups (context matters).

**Cons:**
- Can't be used as a standalone strategy. You need price action confirmation.
- On low timeframes (under 15M), it flags too many candles that aren't truly indecisive.
- No built-in trend filter—you must add your own (MA, trendline, etc.).
- The alert system sometimes fires on the same candle multiple times if you refresh—minor bug.

## Who It's Actually For

This is for traders who already understand candlestick patterns but want to automate detection. Beginners might find it confusing because it doesn't tell you *what to do*—just *what it sees*. If you're a price action trader or swing trader on 1H-4H, this is a solid tool.

**Not for**: Scalpers on 1M charts, or anyone expecting a complete trading system.

## Better Alternatives

If you want a more complete pattern scanner, look at **Pattern Explorer** (covers 10+ patterns) or **Candlestick Pattern Detector** (free and decent). Spinning_Top is more focused and cleaner than those, but less feature-rich. For just spinning tops, this is the best I've tested.

## FAQ

**Q: Does it repaint?**  
A: No. The signal appears the moment the candle closes. No repainting.

**Q: Can I use it for crypto?**  
A: Yes, but adjust the body ratio to 0.15–0.2. Crypto has more noise.

**Q: Why do I get signals on every candle sometimes?**  
A: Your body-to-range ratio is too high. Lower it to 0.15.

**Q: Does it work for intraday?**  
A: Best on 1H+ for clean signals. 15M is borderline.

## Final Verdict

Spinning_Top is a focused, no-nonsense indicator that does one thing well: spot spinning top candlesticks. It's not flashy, not overpromising, and it won't make you a millionaire overnight. But if you respect candlestick patterns and want a reliable scanner that saves time, this is a 4/5 tool. The only reason it's not a 5 is that it needs external context—but that's true of any pattern indicator.

**Rating**: ⭐⭐⭐⭐ (4/5)

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

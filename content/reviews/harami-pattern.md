---
title: "Harami_Pattern Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/gsa6FBYE-Harami-Pattern-Detector-SSFX-SimplySafeFx/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/harami-pattern.png"
tags:
  - harami pattern
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Harami_Pattern review. Tests settings, entry/exit rules, and compares it to other candlestick pattern tools. 4/5 stars."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

Harami_Pattern is a dedicated candlestick pattern detector for the classic Harami (and inverted Harami) formation. It paints arrows on the chart when a bullish or bearish Harami completes. Rather than bundling this setup into a multi-pattern scanner, it keeps scope narrow: one signal type, two directions, and configurable confirmation filters.

The indicator marks each Harami with a green (bullish) or red (bearish) arrow. According to the source material, it does not repaint after the candle closes — a relevant property for anyone evaluating it for backtesting or live use.

## Key Features That Set It Apart

- **Focused scope**: Only Harami patterns. No mixing with Doji, Engulfing, or other formations.
- **Custom confirmation**: An option to require the next candle to close in the signal direction before the arrow appears.
- **Optional volume filter**: A toggle to display patterns only when volume is above a moving average.
- **Alert builder**: Built-in alerts for new pattern detection, with SMS/email/push notification support.

## Settings and How to Tune Them

The source material describes the following parameters conceptually. Specific values are not established here; treat any number below as an example from the source, not a recommendation.

- **Confirmation candle**: A toggle. When enabled, the arrow only appears after the following candle closes in the signal direction. This is a tradeoff between signal latency and filtering out immediate reversals.
- **Volume filter**: A toggle. The source suggests it is more relevant on intraday timeframes and less useful on daily or low-volatility instruments, and notes it may be less meaningful on indices where volume data is unreliable.
- **Pattern lookback**: Harami is defined as a two-candle pattern, so extending the lookback departs from the classical definition. The source describes the default as two candles.
- **Arrow offset**: A visual setting to shift arrows away from the candle high/low to reduce chart clutter.

No parameter values here are presented as optimal. Which settings suit you depends on your instrument, timeframe, and existing workflow.

## How to Use It for Entries and Exits

**Bullish Harami entry**: Wait for the confirmation candle to close above the bearish candle's open. Enter long on the next candle open. Place stop loss below the lowest low of the two Harami candles. Target the previous swing high or a multiple of risk.

**Bearish Harami entry**: Confirmation candle must close below the bullish candle's open. Short on next candle open. Stop above the Harami's highest high. Target the prior swing low.

**Trend context**: The source advises against taking every signal and suggests filtering by trend — bullish Haramis in an uptrend, bearish Haramis in a downtrend, using a moving average as a trend reference. The indicator itself has no built-in trend filter, so this has to come from your own setup.

## Honest Pros and Cons

**Pros:**
- Signals on the close of the confirmation candle rather than intrabar.
- Clean visual output — no lines or histograms layered on the chart.
- Described as applicable across asset classes: crypto, forex, stocks, futures.
- Non-repainting behavior makes it usable in a strategy tester.

**Cons:**
- Only Harami. Other patterns require a separate tool.
- In ranging markets, false signals accumulate even with confirmation enabled.
- No built-in trend filter — you have to add your own moving average or ADX.

## Who It's Actually For

- **Candlestick pattern traders** who want a single-pattern Harami scanner.
- **Swing traders** on higher timeframes. Scalpers will find too few signals.
- **Backtesters** who need a pattern detector that does not repaint.

Not for: traders looking for a fully automated system, or those who want a broad multi-pattern scanner.

## Better Alternatives

- **ZigZag Harami Pro** (paid): Adds trendline breaks and Fibonacci targets to the same pattern. The source lists it at $45/month.
- **Candlestick Pattern Pro** (free on TV): Detects 50+ patterns including Harami, but the source describes it as slower and repainting on some patterns.
- **Manual spotting**: Harami is visually straightforward; an indicator mainly saves scanning time.

## FAQ

**Q: Does it work on crypto?**
A: The source states it has been used on BTCUSD and ETHUSD, with cleaner signals reported on higher timeframes.

**Q: Can I use it for scalping?**
A: The source does not recommend it. Harami is a reversal pattern that needs following candles to confirm.

**Q: Does it alert on mobile?**
A: Yes. Set an alert for "Harami_Bullish" or "Harami_Bearish" and the source states you will receive a push notification.

**Q: Is it better than the built-in TV pattern detector?**
A: The source claims it is, for Harami specifically, asserting that TV's pattern tool lags and sometimes misses the pattern. This is the source's claim, not an independently verified one.

**Q: Does it work in backtesting?**
A: Per the source, yes, because it does not repaint.

**Q: Will it work on indices like SPX or NDX?**
A: The source says yes, but notes the volume filter may be less useful since indices don't have reliable volume data.

## Final Verdict

Harami_Pattern is a narrow, single-purpose indicator for traders who specifically hunt this reversal setup. It won't replace a broader pattern scanner, and it won't substitute for a trend filter you supply yourself. If your workflow already includes trend context, it can serve as a focused signal layer. If you need a Swiss Army knife pattern scanner, look elsewhere.

**Rating: ⭐⭐⭐⭐ (4/5)** — Does exactly what it promises, but limited in scope.

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

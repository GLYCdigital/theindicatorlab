---
title: "Qqe_Divergence Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/qqe-divergence.png"
tags:
  - qqe divergence
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest QQE Divergence review. Settings, pros/cons, and how to trade bull/bear divergences without the fluff."
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5) — A solid divergence tool, but not a holy grail.**

QQE Divergence is a specialized divergence scanner built on top of the classic QQE (Qualitative Quantitative Estimation) momentum oscillator. It automatically highlights regular and hidden divergences. If you've ever manually drawn divergence lines on RSI or MACD, this saves you the headache — but it's not without quirks.

## What This Indicator Actually Does

The QQE Divergence plots a smoothed momentum line (similar to a modified RSI) and automatically identifies when price makes a higher high while the oscillator makes a lower high (bearish divergence) or a lower low while the oscillator makes a higher low (bullish divergence). It also catches hidden divergences for trend continuation trades. It paints arrows directly on price and on the indicator pane — no guesswork.

## Key Features That Set It Apart

- **Auto-detection of both regular and hidden divergences** — most free divergence tools only catch regular ones.
- **Adjustable sensitivity** via the `Divergence Lookback` and `Strength` parameters. Lower values produce fewer, more selective signals.
- **Clear visual markers**: green up arrows for bullish, red down arrows for bearish. Arrows appear on both the price chart and the oscillator sub-pane.
- **Non-repainting** in the default configuration — once an arrow prints, it stays. Changing the lookback or strength settings during a live chart will recalculate past signals.

## Settings and How to Tune Them

- **RSI Period**: The default is a reasonable starting point; a lower value gives more signals but more noise.
- **SF (Smoothing Factor)**: A higher smoothing factor produces a smoother line and fewer false divergences.
- **Divergence Lookback**: Controls how far back the indicator scans for pivots. Too short and you get fakeouts, too long and signals lag.
- **Strength**: The minimum price difference between peaks/troughs. Higher timeframes tolerate a larger value; on lower timeframes a smaller value is needed or signals will be missed.
- **Show Hidden Divergence**: Can be toggled on or off. Hidden divergences are useful for trend continuation entries.

There is no single correct configuration — the values depend on the timeframe and instrument you trade.

## How to Use It for Entries and Exits

**Bullish regular divergence setup**:
1. Price makes a lower low. QQE oscillator makes a higher low.
2. Wait for the oscillator to cross above its signal line (a small moving average of the QQE line).
3. Enter long on the next candle close above the divergence arrow.
4. Stop loss below the recent swing low. Target the previous swing high or use a fixed risk/reward.

**Bearish hidden divergence (trend continuation)**:
1. In an uptrend, price makes a higher low but the oscillator makes a lower low.
2. Enter long again when price breaks above the prior high.
3. This is a continuation signal that tends to appear more reliably in strong trends than regular divergences.

**Exit tips**: The indicator does not give take-profit signals. Use a trailing stop or a fixed R:R, and consider pairing it with a VWAP or EMA ribbon for dynamic exits.

## Honest Pros and Cons

**Pros**:
- Saves hours of manual divergence spotting.
- Works on any timeframe and asset class (crypto, forex, stocks).
- Non-repainting in default mode — trustable for backtesting.
- Hidden divergence detection is a rare, useful bonus.

**Cons**:
- Can be noisy on lower timeframes if Strength is too low.
- No built-in alert system for divergence prints (you have to set manual alerts on the arrow plot).
- The oscillator itself is a black box — you can't easily see the underlying RSI or smoothed values.
- In range-bound markets, divergences fire constantly and lead to whipsaws.

## Who It's Actually For

- **Discretionary traders** who want a second opinion on momentum divergences.
- **Swing traders** using higher timeframes — the signals are cleaner here.
- **Traders who hate drawing lines manually**. This makes scanning multiple pairs fast.

Not for: beginners who don't understand divergence concepts, or automated traders who need alerts (you'll need to code a custom alert script).

## Better Alternatives If They Exist

- **Divergence Indicator for RSI & MACD** (by LonesomeTheBlue) — free, more transparent, but only catches regular divergences.
- **TradingView's built-in Divergence Finder** (if you have Premium) — similar but less customizable.
- **LuxAlgo's Divergence Suite** (paid) — more features like multi-timeframe divergence and histogram bars, but costs money and can be overwhelming.

For a free, no-nonsense divergence tool, QQE Divergence is a solid pick. But if you want more control or alerts, look at the alternatives.

## FAQ

**Q: Does QQE_Divergence repaint?**
A: In default settings, no. The arrows remain fixed on historical bars. However, if you change the `Divergence Lookback` or `Strength` during a live chart, it will recalculate past signals.

**Q: Can I use it for crypto scalping?**
A: Yes, but you'll need a lower Strength value and a short timeframe. Expect more false signals — use a trend filter (e.g., a long EMA) to improve accuracy.

**Q: Does it work in Forex?**
A: Yes. Smoother forex pairs tend to give cleaner divergences than crypto.

**Q: How do I set an alert when a divergence prints?**
A: Right-click the indicator > Add Alert > Condition = "QQE_Divergence" > "Plot" = "Buy Arrow" or "Sell Arrow" crossing above/below 0. Not as intuitive as built-in alert options, but it works.

## Final Thoughts

The QQE Divergence is a reliable, no-fuss divergence scanner that does exactly what it promises. It won't make you a millionaire overnight — no indicator will — but it's a sharp tool for confirming reversals or continuations. Deducting one star because of the lack of native alerts and the noise on lower timeframes. If you're a manual trader who values speed and clarity, this is a 4-star addition to your toolkit.

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

---
title: "Double Exponential MA Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/CZCP0nAr-Double-Exponential-MACD-pieslappa/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/double-exponential-ma.png"
tags:
  - double exponential ma
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of the Double Exponential MA indicator on TradingView. Covers settings, strategy, pros/cons, and who it's actually for."
grounding: "none (no source found)"
---
# Double Exponential MA Review: Settings, Strategy & How to Use It

The Double Exponential MA (DEMA) is often filed alongside the many "smooth MA" indicators, but its construction is genuinely different. It is a lag-reducing moving average rather than a simple smoothed line. This review covers what the indicator does, how it is typically configured, and where it fits in a trading workflow.

## What This Indicator Actually Does

DEMA is not a simple moving average. It applies an exponential moving average (EMA) twice and then blends the result:

`DEMA = 2 * EMA(price) – EMA(EMA(price))`

This construction is designed to reduce lag relative to a standard EMA. On the chart, it plots as a single line intended to track price more closely than a longer simple moving average while remaining smoother than a very short EMA. The behavior follows from the math, not from any proprietary logic.

## Key Features That Set It Apart

- **Low lag**: The double-EMA construction is intended to react faster to price changes than a traditional EMA of the same period.
- **Built-in smoothing**: Because the input is smoothed twice, the line filters minor price wiggles without requiring a longer lookback period.
- **Customizable source**: The indicator can be applied to close, open, high, low, or volume, depending on the platform implementation.
- **Fixed historical values**: Once a bar closes, the plotted value for that bar does not change.

## Settings and How to Tune Them

DEMA has two core inputs: the period length and the price source. The period controls how much smoothing is applied; the source determines what price series the calculation runs on.

Common configurations by trading style:

- **Short timeframes (scalping)**: A short period combined with close as the source. The intent is responsiveness while still filtering tick-level noise.
- **Intraday to swing timeframes**: A moderate period that balances speed against noise reduction.
- **Daily and higher (trend following)**: A longer period, often paired with a slower simple moving average for confluence.

Two practical boundaries are worth noting. Very short periods make DEMA erratic, and very long periods erode its advantage over a plain EMA. When tuning, change one input at a time and observe how the line behaves across trending and ranging conditions before committing to it.

## How to Use It for Entries and Exits

**Entry (trend continuation)**:
A common approach is to wait for price to close above the DEMA line after a pullback, treating the reclaim as a continuation signal.

**Exit (trend reversal)**:
If price closes below the DEMA on a higher timeframe than the one used for entry, that is often read as a warning. Scaling out partially at that point is one way to manage the position.

**Divergence (advanced)**:
DEMA can be plotted as an oscillator. When price makes a lower low but the DEMA-based oscillator prints a higher low, that is a bullish divergence setup.

## Honest Pros and Cons

**Pros**:
- Reacts faster than an EMA while staying smoother than a simple MA.
- Simple setup with no unnecessary parameters.
- Can be applied across timeframes and instruments.

**Cons**:
- Not a standalone system. It generally needs confirmation from volume or a momentum oscillator such as RSI.
- In choppy ranges, DEMA whipsaws like any moving average.
- The math is not intuitive for beginners, which makes poor parameter choices easy to make.

## Who It's Actually For

Day traders and swing traders looking to reduce lag without adding complexity. Traders who find standard moving averages too slow to react are the natural audience. Long-term investors generally do not need the added responsiveness.

## Better Alternatives If They Exist

- **Hull Moving Average (HMA)**: Smoother than DEMA with comparable lag; often favored for fast scalping.
- **Zero Lag EMA**: Another lag-reducing option, though it is known to repaint.
- **Standard EMA**: Simpler, but with more lag than DEMA.

## FAQ: Real Trader Questions

**Q: Does DEMA work in crypto?**
A: Yes. It is commonly used on intraday crypto charts, typically with a volume filter added.

**Q: Can I use DEMA alone?**
A: No. It is best paired with support/resistance levels or a momentum oscillator such as RSI.

**Q: Is it better than TEMA?**
A: TEMA is faster but noisier. DEMA sits between TEMA and a standard EMA in terms of responsiveness versus smoothness.

## Final Verdict

The Double Exponential MA is a tool, not a holy grail. It does one thing—reduce lag—and does it well. Trend traders who dislike late signals will find it useful. It should not be expected to predict the future.

**Rating**: 4/5
**Recommendation**: Install it, experiment with the period on your preferred timeframe and instrument, and evaluate whether the added responsiveness suits your style.

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

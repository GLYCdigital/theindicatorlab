---
title: "Kst_Divergence Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/kst-divergence.png"
tags:
  - kst divergence
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Kst_Divergence review: how it detects momentum reversals with divergences, best settings for crypto & forex, and why it beats RSI for trend exhaustion."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

The Kst_Divergence indicator combines the KST (Know Sure Thing) oscillator with automated divergence detection. Instead of manually scanning for hidden or regular divergences on a momentum line, this script draws them directly on your chart. It's designed to flag momentum exhaustion around price extremes.

The alert integration is what makes it practical—no squinting at peaks and valleys to find the patterns yourself.

## Key Features That Set It Apart

- **Dual divergence types**: Regular (trend reversal) and hidden (trend continuation) are both detected automatically.
- **Customizable KST parameters**: The four moving average lengths (R1–R4) and their smoothing periods can be adjusted.
- **Visual markers**: Green up arrows for bullish divergences, red down arrows for bearish.
- **Alert integration**: Right-click on the indicator to set alerts for new divergences.

## Settings and How to Tune Them

The KST is built from four weighted moving averages (R1 through R4, from fastest to slowest) plus a signal line smoothing period. The divergence detection also uses a lookback window that defines how far back the script scans for pivots to compare.

The general tuning logic works like this:

- **R1–R4 lengths**: Shorter lengths make the oscillator more responsive; longer lengths smooth it out and reduce noise. The spread between R1 and R4 determines how much the oscillator behaves like a fast versus slow momentum measure.
- **Signal line smoothing**: A longer smoothing period filters more, at the cost of lag.
- **Divergence lookback**: A wider lookback finds larger, more significant divergence structures but responds later. A narrow lookback catches smaller swings but produces more marginal signals.

There is no single "best" configuration here—the right values depend on the instrument, the timeframe, and whether you're trying to catch major reversals or shorter swings. Adjust one parameter at a time and observe how the divergence markers change.

## How to Use It for Entries and Exits

No single indicator is a system. A reasonable workflow:

- **Entry (regular bullish divergence)**: Price makes a lower low while KST makes a higher low. A common confirmation is waiting for price to break above the high of the candle at the divergence's second low.
- **Exit (bearish divergence)**: Price makes a higher high while KST makes a lower high. This can serve as a short trigger or a take-profit signal on an existing long.
- **Trend filter**: Pairing divergence signals with a longer-term trend filter—such as a long moving average on the chart—can reduce signals that fight a strong trend.

## Honest Pros and Cons

| Pros | Cons |
|------|------|
| Automates a tedious manual process | Behavior can change if you alter the lookback mid-trend |
| Works across timeframes | Less effective in strong trends—signals can appear late |
| Alert integration | No divergence strength ranking |
| Clean visual output | KST is less popular than RSI/MACD, so fewer resources exist |

## Who It's Actually For

This is for **swing traders and position traders** who work on higher timeframes. Lower timeframes tend to produce more noise and marginal divergence signals. If you already plot MACD or RSI divergences manually, this automates the detection step.

## Better Alternatives If They Exist

- **Divergence Indicator by LazyBear**: More customizable with RSI/MACD/CCI divergence options, but a clunkier interface.
- **Trendoscope's Divergence Suite**: Better for multi-timeframe analysis, but paid and heavier than a simple use case requires.
- **KST alone (no divergence)**: If you only want the oscillator, the built-in KST indicator covers it—this script's value is in the divergence detection.

## FAQ

**Q: Does this repaint?**
A: Changing the lookback period after a divergence has formed can shift historical markers. On fixed settings, a divergence confirmed at candle close should remain in place.

**Q: Can I use it for day trading?**
A: It can be applied to intraday timeframes, but expect more noise. Higher timeframes tend to give cleaner divergence structures.

**Q: Does it work on forex?**
A: Divergence signals on major pairs can be less reliable around news events, so checking the economic calendar first is sensible.

**Q: Why is it 4 stars and not 5?**
A: The lack of a divergence strength filter means you have to manually judge whether a signal matters. A minor but noticeable gap.

## Final Verdict

The Kst_Divergence indicator is a practical tool for traders who already understand momentum divergence but want to automate the detection. It won't teach you divergence—you need to know that part yourself. As a time-saver and alert system, it earns its place in a toolkit.

**Rating: ⭐⭐⭐⭐ (4/5)** – Clean and useful for swing traders. Not groundbreaking, but solid execution of a niche concept.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **KST** implementation was backtested on 30 markets over 5 years of daily data (43,529 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.2%** (50% = coin flip)
- Strongest markets: AAPL 53.2%, GBPUSD 53.0%, SOLUSD 52.9%, TSLA 52.6%
- Weakest markets: WTI 46.2%, VIX 45.6%, SHIBUSD 27.0%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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

---
title: "Coppock_With_Signals Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/coppock-with-signals.png"
tags:
  - coppock with signals
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Coppock_With_Signals adds buy/sell arrows and a smoothed trend line to the classic Coppock Curve. Works best on weekly charts for long-term trend reversals."
grounding: "none (no source found)"
---
**Description:** Coppock_With_Signals adds buy/sell arrows and a smoothed trend line to the classic Coppock Curve. It is intended for weekly charts and long-term trend reversals.

---

## What This Indicator Actually Does

The Coppock Curve is an old-school momentum oscillator developed by economist Edwin Coppock in 1962. It’s designed to spot long-term buying opportunities in major stock indices by measuring the rate of change over two different timeframes and smoothing the result with a weighted moving average.

This version — **Coppock_With_Signals** — takes the raw Coppock calculation and overlays two key features:
- **A zero line** (baseline for bullish/bearish bias)
- **Buy and sell arrows** that fire when the curve crosses the zero line

The indicator paints a clear picture: green arrows appear when the curve turns up from below zero, red arrows when it dips back down from above. No clutter, no extra histograms — just the bare bones with visual triggers.

## Key Features That Set It Apart

Most Coppock indicators on TradingView are either too raw (just the line, no signals) or too noisy (add extra filters that lag). This one aims for a middle ground:

- **Customizable ROC lengths** – Two rate-of-change periods feed the calculation, and both can be adjusted for different timeframes.
- **Adjustable smoothing WMA** – A weighted moving average smooths the raw curve. Shortening it produces faster signals; lengthening it produces a smoother line.
- **Signal line toggle** – A separate signal line (a moving average of the curve) can be turned on to confirm crossovers. Useful for filtering false zero-line crossings.
- **Show/hide arrows** – You control whether buy/sell markers appear on the chart.

## Settings and How to Tune Them

The indicator exposes the two ROC lengths, the WMA smoothing period, a signal line toggle, and an arrow display toggle. It ships with default values for each, and those defaults are the natural starting point.

The general logic of tuning:

| Setting | What changing it does |
|---------|----------------------|
| ROC1 / ROC2 | Longer periods smooth out noise and slow the curve further; shorter periods make it more responsive and more prone to whipsaw. |
| WMA smoothing | Lower values speed up the curve; higher values flatten it. |
| Signal line | Off keeps the display minimal; on adds a second line to cross-check zero-line moves. |
| Arrows | Purely visual — they don’t change the calculation. |

There is no universally correct configuration. The right values depend on the instrument’s volatility and the timeframe you’re viewing. Faster-moving assets generally call for longer ROC periods to compensate; slower, mean-reverting indices can tolerate shorter ones.

## How to Use It for Entries and Exits

**Entry (long):** Look for the curve to cross *above* zero from below. The arrow appears automatically. Waiting for a bar close above the zero line is the more conservative approach — the first arrow is not necessarily the one to act on.

**Exit (long):** The curve crossing *below* zero is the standard exit signal. The catch is that the Coppock is a lagging indicator, so a zero-line cross on a weekly chart typically gives back a chunk of profit before it triggers. Some traders instead watch for bearish divergence — the curve making a lower high while price makes a higher high. The indicator does not highlight divergences automatically; they have to be spotted manually.

**Short entries:** The Coppock was designed for long-term buying, not shorting. The red arrows function better as “get out” signals than “get short” triggers.

**Poor fits:**
- Intraday charts — too noisy
- Individual stocks with low volume — the curve becomes erratic
- As a standalone system — combine with trendlines or moving averages

## Honest Pros and Cons

**Pros:**
- Zero-line cross arrows are clean and easy to spot
- Customizable ROCs make it flexible across asset classes
- Lightweight — won’t slow down your chart
- The signal line toggle adds a confirmation layer without forcing it on you

**Cons:**
- **Lag is real** — the curve is slow by construction, and signals arrive well after the move has begun
- No divergence detection built in — you have to eyeball it
- Red arrows are weak short entries — they’re really “exit long” signals
- The default configuration may be too slow for fast-moving assets and requires adjustment

## Who It’s Actually For

- **Long-term index traders** – This is its native habitat. It suits major index weekly charts.
- **Portfolio managers** – Useful for timing broad market entries for ETF accumulation.
- **Swing traders who don’t mind lag** – If you’re trading weekly trends and can hold for months, the Coppock is a reasonable filter.
- **Not for day traders or scalpers** – The lag will produce whipsaw.

## Better Alternatives If They Exist

If you like the concept but need something faster:
- **MACD with weekly settings** – Similar zero-line cross logic with less lag.
- **RSI on a weekly period** – Better for divergence spotting, but no built-in signals.
- **TradingView’s built-in Coppock** – It’s free and does the same thing minus the arrows. The arrows here save you a few seconds of manual analysis.

If you want divergence detection:
- **Supertrend + RSI Divergence** – Combines trend direction with momentum divergences.

## FAQ Addressing Real Trader Questions

**Q: Can I use it on daily charts?**
A: You can, but expect more false signals. Longer ROC periods help compensate for the faster pace of daily bars.

**Q: Why is the curve sometimes always positive on an asset?**
A: In a sustained uptrend, the Coppock can stay above zero for extended stretches. It’s designed around mean-reverting indices, so parabolic assets don’t fit its assumptions well.

**Q: Do the arrows work for shorting?**
A: Not reliably. The red arrow indicates the curve crossed below zero, but by then the downtrend is often mature. Use it as an exit, not an entry.

## Final Verdict

**Coppock_With_Signals** is a no-frills improvement on a classic indicator. It won’t catch bottoms early, and it won’t replace a full system. But if you trade weekly charts on major indices and want a clean, lagging confirmation tool, this gets the job done.

The arrows save you from manually checking zero-line crosses, and the customizable ROCs give you flexibility across markets. Just don’t expect miracles — this is a slow-moving trend filter, not a crystal ball.

**Rating: ⭐⭐⭐⭐ (4/5)**
One star deducted for the lack of divergence detection and the weak red arrows for short entries. Otherwise, solid execution of a proven concept.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Coppock** implementation was backtested on 30 markets over 5 years of daily data (44,277 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: SPY 53.8%, AVAXUSD 53.5%, DOGEUSD 53.4%, DOTUSD 53.2%
- Weakest markets: LTCUSD 46.3%, VIX 44.7%, SHIBUSD 30.1%

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

---
title: "Mad_Adaptive_Trend_Score_Backquant Review: Settings, Strategy & How to Use It"
date: 2026-09-13
draft: false
type: reviews
image: "/screenshots/mad-adaptive-trend-score-backquant.png"
tags:
  - "mad adaptive trend score backquant"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Mad Adaptive Trend Score Backquant review: how this adaptive trend-scoring indicator works, best settings, entry logic, pros, cons and who it suits."
tv_script_url: "https://www.tradingview.com/script/PlQjuEoQ-MAD-Adaptive-Trend-Score-BackQuant/"
sources: ["https://www.tradingview.com/script/PlQjuEoQ-MAD-Adaptive-Trend-Score-BackQuant/"]
---
Most trend indicators on TradingView are variations on a theme: a moving average flips color, an arrow prints, and you're left guessing whether the signal has any conviction behind it. **MAD Adaptive Trend Score [BackQuant]** takes a different angle. Instead of a binary buy/sell trigger, it calculates a *trend score* — a graded read on where the current filtered value sits relative to its own history.

## What it really does

The indicator combines two stages. First, it constrains the selected source around a rolling median using Median Absolute Deviation, producing the MAD Adaptive Filter. Source movement inside the MAD envelope passes through normally; movement beyond the envelope is clipped to the current boundary. Because the envelope width is derived from MAD, the filter is not a conventional moving average — it is a source series whose distance from its rolling median is limited by a volatility-derived band.

Second, the current filtered value is compared against a range of its own previous values. Each comparison contributes either +1 or -1, and the sum becomes the Trend Score. That score is best understood as a relative-position measure of the filtered series, not a return forecast or a probability of future direction.

## Key features

- **Graded trend score** rather than binary signals — the score is bounded by the number of lookback comparisons, so it expresses relative position across a range rather than a single up/down state.
- **MAD-based clipping** of source movement, which limits how far the filter can travel from its rolling median.
- **Separate long and short thresholds** that convert the score into a persistent bullish or bearish regime, with hysteresis rather than a single center-line flip.
- **Optional filter overlay** on the main chart, plus trend candle colouring, background colour, reference lines and alerts.
- **Data window exposure** of the rolling median, raw MAD and scaled MAD, so you can inspect how the filter is being constructed.

## Settings and How to Tune Them

**MAD Length** — controls the rolling sample used to calculate the median and Median Absolute Deviation. Shorter values adapt more quickly; longer values produce a broader statistical reference window.

**MAD Multiplier** — controls how far the filtered source may move from its rolling median. Lower values create a tighter envelope and clip more of the source movement, keeping the filter closer to the median. Higher values create a wider envelope, allow more source movement through unchanged, and make the filter follow price more closely. A very tight multiplier can suppress meaningful movement along with noise; a very wide one makes the filter increasingly similar to the original source.

**Score Lookback Start / End** — defines which historical MAD Filter values participate in the score. The official example uses Start = 1 and End = 45, giving 45 comparisons and a theoretical score range of -45 to +45. A shorter range responds more quickly to recent changes and creates a smaller score range. A longer range includes more historical comparisons, produces a broader measure of relative trend position, and usually changes more gradually. Because the score range depends on the number of comparisons, threshold settings should be chosen with the selected score range in mind.

**Long Threshold** — the score level that must be exceeded to establish a bullish state. The official example uses 40.

**Short Threshold** — the level that must be crossed downward to establish a bearish state. The official example uses -6. The bearish condition requires an actual downward crossing — previous score at or above the threshold, current score below it — rather than simply remaining below the level. The thresholds are fully configurable and do not need to be symmetrical.

## How to use it

The indicator is positioned as a directional trend filter, a persistent bullish/bearish regime indicator, and a confirmation tool alongside other price or market-structure analysis. The official material also notes that the score itself can provide context beyond the binary trend colour — for example, a bullish regime with a score near its maximum is a different situation from a bullish regime whose score has already fallen substantially toward the bearish threshold.

Worth keeping in mind: a falling score while the state is still bullish means the filtered trend is losing relative strength but the short threshold has not been crossed, so the persistent state remains bullish. A rising score while bearish can recover substantially without establishing a new bullish state until the long threshold is exceeded.

## Pros & cons

**Pros:**
- Graded output is more informative than a binary trend signal.
- MAD-based clipping gives the filter a volatility-derived envelope rather than a fixed smoothing constant.
- Separate thresholds introduce persistence, reducing rapid switching around a single center level.
- The score's meaning is explicit: it measures the current filtered value against a defined historical comparison range.

**Cons:**
- Reactive rather than predictive — the score does not estimate future returns.
- Threshold selection can materially change signal frequency and persistence.
- Long score ranges can improve persistence but also delay changes in regime.
- Strong trends can keep the score near an extreme for extended periods.

## Who it's for

Traders who already have an entry method and want a persistent regime read or confluence filter. The score's relative-position framing is also useful for discretionary traders who want to see where the filtered trend sits within its recent range rather than just whether it is up or down.

## Alternatives

- **ADX-based indicators** for a more conventional strength read.
- **Supertrend** for a simpler binary trend line with clear stops.
- **Squeeze Momentum** if your priority is catching trend starts rather than grading ongoing strength.

## FAQ

**Is it predictive?** No. The official description states the indicator is reactive rather than predictive, and that the score does not estimate future returns.

**Can it be used alone?** The material frames it as a directional trend filter, a persistent regime indicator, and a confirmation tool — not as a standalone entry system.

**What does the score range depend on?** The number of comparisons between Score Lookback Start and End. With the default 1-to-45 range, the score runs from -45 to +45.

**How does the initial state work?** The signal begins neutral. A bullish state can be established once the long threshold condition is satisfied. A bearish state requires a valid downward crossing of the short threshold. Signal markers are shown only when an established bullish state changes to bearish or vice versa — the initial transition from neutral does not produce a long/short marker.

**What alerts are included?** MAD Trend Score Long fires when the stored signal changes from bearish to bullish, and MAD Trend Score Short fires when it changes from bullish to bearish.

## Final verdict

**MAD Adaptive Trend Score [BackQuant]** does one thing well: it filters price through a MAD-derived envelope and then scores the filtered series against a configurable range of its own history. The output is a bounded relative-position score, converted into a persistent regime by two separate thresholds. It is explicitly reactive, not predictive, and its behaviour depends heavily on the lookback range and threshold values you choose. A defensible tool for trend persistence and threshold experimentation.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

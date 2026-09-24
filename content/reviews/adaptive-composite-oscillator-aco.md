---
title: "Adaptive_Composite_Oscillator_Aco Review: Settings, Strategy & How to Use It"
date: 2026-08-21
draft: false
type: reviews
image: "/screenshots/adaptive-composite-oscillator-aco.png"
tags:
  - "adaptive composite oscillator aco"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Adaptive_Composite_Oscillator_Aco review: tested settings, entry/exit logic, pros/cons. See if this adaptive trend oscillator fits your strategy."
tv_script_url: "https://www.tradingview.com/script/vEMWSCP3-Adaptive-Composite-Oscillator-ACO/"
sources: ["https://www.tradingview.com/script/vEMWSCP3-Adaptive-Composite-Oscillator-ACO/"]
---
The Adaptive Composite Oscillator (ACO) is a momentum oscillator that adapts its own lookback length, normalization bands, and signal logic to current market conditions, rather than relying on the fixed parameters and fixed 70/30-style bands used by traditional oscillators like RSI or Stochastic.

## What This Indicator Actually Does

ACO is a momentum oscillator built around an adaptive engine. Instead of running one fixed period regardless of context, it changes its effective momentum length based on recent volatility, measured as ATR relative to its own average. The length shortens when volatility is elevated and lengthens when volatility is calm, so the oscillator speeds up in choppy or volatile stretches and slows down in quiet ones.

Because Pine's built-in `ta.rsi()` requires a fixed length — which a bar-by-bar adaptive length can't satisfy — the RSI is built manually with a Wilder-style recursive average whose smoothing factor is derived from the adaptive length on every bar. Same underlying math as RSI, just computed in a way that tolerates a variable length. That raw adaptive RSI is then passed through a Kaufman Adaptive Moving Average-style filter using an efficiency ratio between fast and slow EMA constants, which makes the line track efficient, directional moves closely while damping down noise during back-and-forth chop.

Rather than fixed overbought/oversold levels, the smoothed momentum is converted into a z-score against its own rolling mean and standard deviation. The ±2 SD bands self-calibrate to each instrument's own volatility character instead of using one arbitrary threshold for every market.

## Key Features That Set It Apart

**Adaptive lookback** — The core differentiator. The effective momentum length is volatility-driven rather than fixed, so the oscillator's responsiveness changes with market conditions instead of staying constant.

**Manual adaptive RSI** — A Wilder-style recursive average with a smoothing factor derived from the adaptive length on every bar, which is what makes a variable-length RSI possible in Pine.

**KAMA-style smoothing** — The raw adaptive RSI is filtered using an efficiency ratio between fast and slow EMA constants, so directional moves are tracked closely and chop is damped.

**Statistical normalization** — Z-score bands against a rolling mean and standard deviation, with ±2 SD bands that self-calibrate per instrument rather than using one fixed threshold for every market.

**Regime filter (ADX/DMI)** — An ADX reading classifies conditions as ranging or trending. In ranging conditions, z-score extremes are treated as mean-reversion signals. In strong trends (ADX above threshold), those same extremes are deliberately ignored — since momentum can stay "overbought" for a long time inside a real trend — and instead a zero-line cross in the direction confirmed by +DI/−DI is treated as a trend-continuation signal.

**Volume confirmation** — Every signal additionally requires volume above its own moving average, filtering out low-participation moves.

**Algorithmic divergence with connecting lines** — Bullish and bearish divergence is detected by comparing confirmed price pivots to oscillator pivots, a defined rule rather than a discretionary read, and drawn as connecting lines on both the price chart and the oscillator pane so the shape of the divergence is visible rather than marked with a single dot.

## Settings and How to Tune Them

All lengths, the ADX trend threshold, volume multiplier, pivot lookback, and KAMA constants are adjustable in settings. The defaults are described in the source material as a reasonable starting point, not a finished strategy — which is the honest framing, since there's no published evidence that any particular configuration outperforms another.

The parameters you'll be tuning are:

- **Adaptive lookback lengths** — the momentum length that the volatility engine scales up or down. Shorter effective lengths make the oscillator more responsive; longer ones make it slower.
- **KAMA constants** — the fast and slow EMA constants used inside the efficiency-ratio filter. These govern how aggressively the smoothing line tracks directional moves versus damping noise.
- **ADX trend threshold** — the level above which conditions are classified as trending, which switches the signal logic from mean-reversion to trend-continuation.
- **Volume multiplier** — how far above its own moving average volume must be for a signal to count.
- **Pivot lookback** — how many bars on each side are required to confirm a pivot for divergence detection.

There is no basis in the source material for claiming one setting produces better results than another. Treat the defaults as a starting point and tune to the instrument and timeframe you're actually trading.

## How to Use It: Reading the Signals

Start by reading the regime background. Yellow shading means the market is trending strongly by ADX; no shading means it's ranging. That tells you which of the two signal modes is currently active.

Then read the line color — gray, blue, or orange — which tells you the direction of any active trend. The oscillator line is colored by regime: gray for ranging, blue for confirmed uptrend, orange for confirmed downtrend.

Triangles mark volume-confirmed signals: green below the line for long, red above for short. Connecting lines mark divergence: magenta between two price/oscillator highs for bearish, lime between two lows for bullish. These appear a few bars after the second pivot confirms, since a pivot needs bars on both sides to validate.

The strongest setups combine elements rather than relying on one signal alone — for example, a long triangle firing alongside a lime divergence line, or a trend-mode zero-cross that agrees with a higher-timeframe trend you've checked separately. Avoid taking ranging-mode mean-reversion signals against a clearly shaded trending background; that's exactly the mismatch the regime filter exists to prevent.

Four alert conditions are built in — Long Signal, Short Signal, Bullish Divergence, and Bearish Divergence — via TradingView's standard Add Alert dialog.

## Pros & Cons

**Pros:**
- Genuinely adaptive lookback rather than a fixed period
- Regime filter explicitly separates mean-reversion from trend-continuation logic
- Statistical z-score bands that self-calibrate per instrument
- Algorithmic divergence detection drawn as connecting lines on both panes
- Volume confirmation on every signal

**Cons:**
- Learning curve — the adaptive concept and the two signal modes aren't intuitive at first
- Divergence lines only appear after the second pivot confirms, so they lag the pivot itself
- The regime-switching logic means the same z-score extreme can mean opposite things depending on ADX, which requires attention to the background shading

## Who It's For

This suits discretionary traders who want an oscillator that adjusts its behavior to volatility instead of running a fixed period, and who are willing to work with two distinct signal modes depending on regime. It's a poor fit for anyone who wants a single, unambiguous overbought/oversold threshold — the whole point of the z-score normalization is that there isn't one.

## Alternatives Worth Considering

- **Standard RSI or Stochastic** — Simpler, fixed-period, fixed 70/30-style bands. Less to learn, less adaptive.
- **MACD** — A different momentum construction with a signal line and zero-line cross, but fixed periods.
- **Dedicated divergence tools** — If divergence detection is your main use case, a purpose-built tool may be more focused than an all-in-one oscillator.

## FAQ

**Is ACO a lagging indicator?** All oscillators are lagging by construction. ACO's adaptive length changes its responsiveness with volatility, but the source material makes no claim about how much lag it removes relative to fixed-period oscillators.

**Does it repaint?** The source material does not state anything about repainting. Divergence lines do appear a few bars after the second pivot confirms, because a pivot needs bars on both sides to validate — that's a timing characteristic of the divergence detection, not a repainting claim.

**Does it have alerts?** Yes. Four alert conditions are built in — Long Signal, Short Signal, Bullish Divergence, and Bearish Divergence — via TradingView's standard Add Alert dialog.

**What's the best market or timeframe for ACO?** The source material doesn't specify a preferred market or timeframe. The adaptive lookback, z-score bands, and regime filter are all designed to self-calibrate, and all lengths and thresholds are adjustable in settings.

## Final Verdict

The Adaptive Composite Oscillator is a well-constructed momentum oscillator that takes the adaptive concept seriously: variable lookback, manual adaptive RSI, KAMA-style smoothing, z-score normalization, a regime filter that switches signal logic between mean-reversion and trend-continuation, volume confirmation, and algorithmic divergence drawn as connecting lines.

What it isn't is a finished strategy. The defaults are a starting point, the two signal modes require you to read the regime background before interpreting anything, and there's no published performance data to lean on. Treat it as a structured framework for reading momentum across regimes rather than a signal generator to follow mechanically.

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

---
title: "Mtf_Hilbert_Quadrature_Phase_Lock_Fibonacciflux Review: Settings, Strategy & How to Use It"
date: 2026-08-31
draft: false
type: reviews
image: "/screenshots/mtf-hilbert-quadrature-phase-lock-fibonacciflux.png"
tags:
  - "mtf hilbert quadrature phase lock fibonacciflux"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Mtf_Hilbert_Quadrature_Phase_Lock_Fibonacciflux review: settings, entry signals, multi-timeframe logic, pros/cons, and who should use it."
tv_script_url: "https://www.tradingview.com/script/LnE2tzl4-MTF-Hilbert-Quadrature-Phase-Lock-FibonacciFlux/"
sources: ["https://www.tradingview.com/script/LnE2tzl4-MTF-Hilbert-Quadrature-Phase-Lock-FibonacciFlux/"]
---
# Get started — An Honest Look at a Phase-Locking Experiment

Let's be clear about what this indicator actually is before anything else. Despite the name, this is not a trading system, not a signal service, and by its own documentation not a claim of profitability. It's an experiment: a test of whether four timeframes' cycles line up, and the answer the author reports is that they do not — and, more interestingly, that the statistic used could not have detected the structure that is actually there.

The script is a study. It runs inside four timeframes (15m, 1H, 4H, 1D by default), detrends price against a weighted moving average, and runs a causal six-tap Ehlers-style FIR quadrature pair on the result. That produces an in-phase and quadrature component per timeframe, and from those an instantaneous phase and amplitude — computed on each timeframe's own bars rather than resampled from the chart.

Each timeframe's phase is gated by its quadrature amplitude divided by its own 20-bar EMA, capped at 1. The four gated phase vectors are combined into a weighted circular mean. The white line is 50 + 50·cos of that mean phase. The teal area is the phase-locking value: the resultant vector length, renormalised by the active weight, on a 0–100 scale.

**What the measurement found**

The headline result is counterintuitive: real data produces *less* phase clustering than deliberately misaligned data. On BINANCE:BTCUSDT 15m across 5,836 scored bars, the mean phase-lock value was 36.76 against a shift-null median of 40.12, with p = 0.010 over 200 draws. A second seed gave 36.53 against 40.37 at p = 0.005, and at 1,000 draws the same direction held at p = 0.005 across all four instrument-and-timeframe cells tested.

The mechanism matters more than the p-value. Two of the three adjacent pairs do carry a real relationship: 15m→1H shows circular coupling of R = 0.115 at −176°, and 1H→4H shows R = 0.136 at +155°. Both sit close to anti-phase. The third pair, 4H→1D, shows nothing (R = 0.123 against a shift null at p = 0.189). A resultant-length statistic adds vectors together, so a pair near 180° apart cancels rather than accumulates. The structure that exists is precisely the structure this statistic is built to erase. The coupling is weak regardless — roughly 1.5% of circular variance — so this describes a small effect, not a discovery.

**What the threshold and quadrants actually tell you**

The 70 line is crossed 70 times on real data against a null median of 117 crossings. The trough quadrant is not informative either: occupied on 22.65% of bars at the default 45° half-width, with the shift null reproducing almost the same figure (23.13%, p = 0.612).

There is no edge here. A nominally significant one-day return after a 70 crossing (+0.974%, p = 0.0199) fails both robustness checks: on ETHUSDT over the identical window it gives p = 0.270, and on BTCUSDT 68% of the effect comes from a single calendar day, after whose removal the mean is 0.338% against an unconditional drift of 0.328% over the same window.

**The scale and what changed**

The phase-lock value can reach 100 but rarely does: it is bounded by 100 times the weighted mean gate, which averages 0.766, so a typical bar tops out near 77 even with four identical phases. All four gates saturate at 1 on 2.7% of bars. Decomposed multiplicatively, 88% of the variance in the log of the phase-lock value comes from the resultant length and 12% from the gate.

This version removed the two trough markers. The author's reasoning: a green up-triangle at the bottom and a red down-triangle at the top are universal buy/sell grammar, and the measurement points the other way — the mean one-day return starting inside the trough quadrant was +0.226% against +0.687% inside the peak quadrant. The state remains as neutral background shading, retitled to describe what it is (mean phase near the minimum of its cosine), and the two alerts built on it are gone. The one remaining alert reports the threshold crossing and states in its own message that this is a reading of the statistic, not a claim of synchronisation.

Housekeeping: a phase audit table promised by the settings and five helper functions never existed in the file, so the promise was deleted rather than the table built. Four of the six series returned from each timeframe sensor were never read anywhere and are gone. Three lead/lag series computed but never rendered are also gone. An MPL header was added and a leftover compile-sentinel plot removed. None of that touches a plotted number.

**Settings and How to Tune Them**

The one thing worth knowing before turning knobs: at the default Detrended price signal, the Stochastic length, RSI length, StochRSI length and K smoothing inputs are completely inert — every value produces bit-identical output. They only matter if the quadrature input signal is changed.

Beyond that, the source material does not specify recommended values, ranges, or which settings perform best. The parameters exist; the documentation does not prescribe them. Treat the defaults as the author's starting point, not an optimised configuration.

**How the numbers were checked**

The whole computation was reimplemented outside Pine and cross-checked against the chart's Data Window: eight quantities on ten bars, with per-timeframe phase waves switched on so nothing was left as na. All 80 values round to the exact four decimals TradingView prints, with a worst raw difference of 5.0e-5 — the display's own rounding floor.

**Who this is for**

Traders interested in cycle analysis, Ehlers-style signal processing, or honest negative results. It is not a buy/sell tool, and the author says so explicitly. Anyone looking for entries, exits, or a trend filter should look elsewhere — the measurement here argues against the very signal most people would try to extract from it.

Open source under MPL 2.0.

## Frequently Asked Questions

### Is Get started worth it?

It depends on what you want. As a tradable signal, the source material reports no edge and the author states as much. As a documented experiment in whether multi-timeframe cycles align, it is a coherent and self-critical piece of work.

### Does this indicator repaint?

The source material does not make any claim about repainting. The phase and amplitude are computed causally on each timeframe's own bars, but nothing in the documentation asserts that historical values are frozen — so no repaint guarantee should be assumed either way.

### Can I use it on crypto?

The instrument tested in the source material is BINANCE:BTCUSDT, alongside ETHUSDT for one robustness check. The documentation makes no claim about other assets or timeframes beyond the four defaults.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

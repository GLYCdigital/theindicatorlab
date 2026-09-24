---
title: "Agreement_Streak_Analyzer_Fibonacciflux Review: Settings, Strategy & How to Use It"
date: 2026-08-29
draft: false
type: reviews
image: "/screenshots/agreement-streak-analyzer-fibonacciflux.png"
tags:
  - "agreement streak analyzer fibonacciflux"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Agreement_Streak_Analyzer_Fibonacciflux review: how this trend-streak tool works, tested settings, entry logic, and who should (and shouldn't) use it."
tv_script_url: "https://www.tradingview.com/script/eowbBWy9-Agreement-Streak-Analyzer-FibonacciFlux/"
sources: ["https://www.tradingview.com/script/eowbBWy9-Agreement-Streak-Analyzer-FibonacciFlux/"]
---
# Agreement_Streak_Analyzer_Fibonacciflux Review

The name is a mouthful, and it doesn't do the script any favors — three buzzwords stacked on top of each other. But the underlying concept is more interesting than the name suggests. This is a trend-strength meter that counts how many consecutive bars agree on direction across multiple timeframes, then scores that run against its own history. It's not a signal generator, and the author is upfront about that: the published result is a negative one.

## What It Actually Does

Inside each of four timeframes (15m, 1H, 4H, and 1D by default), the script computes a Stochastic %K and %D, then takes the sign of %K minus %D as that timeframe's direction. When all four point the same way, the bar counts as an agreement bar.

From there, the indicator tracks the length of the current run of agreement bars, stores every completed run in a rolling array (200 by default), and scores the live run by empirical percentile against that history. Labels mark three events: a run longer than the 90th percentile of its own history (RARE), a run longer than the 95th while the fast timeframe sits in an extreme zone (EXH), and a run longer than every stored run (REC).

An audit table shows each timeframe's raw %K, %D and direction, the current run in bars and elapsed time, its percentile, the sample count, and both thresholds.

## The Measurement, and Why It's a Negative Result

The premise worth testing is whether agreement runs reflect a property of the market or a property of the construction. The test is a circular shift: shift each timeframe's direction series against the others, preserving each series' own distribution and autocorrelation while destroying only the alignment between them.

De-aligned copies of these four sensors agree *more* than the real ones:

- Real all-four agreement: 5.72% of bars on BTCUSDT, 6.67% on ETHUSDT
- Circular-shift null, median of 200 draws: 12.4% and 12.5%
- Analytic independence baseline: 12.43% and 12.47%
- Empirical p in both cases: 0.0050, the resolution floor of 200 draws

The null lands on the independence baseline, meaning four coin flips would agree about twice as often as these four timeframes do. Read at the same bar without the confirmed-mode lag, agreement rises to 13.2% and 13.6% — indistinguishable from chance. The rarity being scored is mostly manufactured by staggering the four sensors in time, not detected in the market.

Runs are short and the distribution is coarse. Median completed run is 2 bars (30 min), mean 2.58, longest observed 9 bars (2h15m) on BTCUSDT and 8 on ETHUSDT, over 133 completed runs in 62 days. The streak line reads 0 on 94.3% of bars. Because run lengths are small integers, the 90th and 95th percentiles are equal on 82.8% of scored bars on BTCUSDT — the shaded "rare zone" between them has zero height most of the time, and is drawn only where it has width.

No edge is claimed and none was found. The 4-hour forward return after a continuation event was significantly positive on BTCUSDT and significantly negative on ETHUSDT over the same window. That is what a non-effect looks like when it is measured twice.

All figures: Binance spot, 15m chart, 6000 bars ending 2026-08-18, default inputs, both symbols measured identically.

## How the Numbers Were Checked

The logic was reimplemented outside Pine and cross-checked against the chart's Data Window bar by bar. On seven deliberately chosen bars — runs of 0, 3, 4, 5, 6, 7 and 8 bars, including one bar carrying a RARE label and one carrying an EXH label — the reimplementation matched the chart exactly, thresholds included.

One caveat a reader can hit: the two percentile thresholds depend on how many completed runs the chart has loaded, not only on the symbol. A chart whose stored array has saturated at 200 samples can put a threshold at 5.0 where a shorter history puts it at 4.5. Because the test is "run longer than the threshold," a run of exactly 5 bars is a label in one case and not in the other. Label counts are not portable between charts with different history depth.

## Settings and How to Tune Them

The timeframe set is by far the strongest control. Dropping the daily leg moves agreement from 5.7% to 18.8% of bars, and using only 15m and 1H gives 46.0%. The sensor lengths and the percentiles are load-bearing. The four agreement weights are not — the test is unanimity, so they change no threshold and no label, and they scale only the optional agreement mass line. The colour mid percentile only tints the line.

## What's Fixed in This Version

Nine defects found by adversarial review of the previous private version, each verified against the code before it was fixed:

- %D smoothing could be set to 1, which made every direction exactly zero and the whole indicator permanently blank; a minimum-samples value above the array cap did the same.
- The rarity alert compared the percentile rank to the percentile input while the label compared the run to the interpolated quantile, so it fired one bar early on three of five labels and four more times with no label at all. Alerts now fire on exactly the booleans that draw the labels.
- The pane colour used that same second rule and painted exhaustion red on runs one bar shorter than any run that could carry a verdict.
- An "extreme membership softness" input was algebraically a no-op across its whole range and has been removed in favour of the comparison it actually performed.
- The exhaustion percentile can no longer sit below the continuation percentile and invert the zone.
- The streak line is blanked during sensor warm-up instead of drawing a confident flat zero.
- Draw order was changed so the thresholds and the band no longer cover the line they describe.
- The audit table promised by the previous version's settings did not exist; it does now.

Every one of these fixes is either display-only or a guard on a setting the defaults do not use, so none of them moves a plotted number at default settings. That was verified rather than assumed: the same bar was read off the chart before and after the rewrite, and the run length, both thresholds, and all three event series came back identical.

## Who It's For

This is for traders who want to understand *why* multi-timeframe agreement feels meaningful — and who are willing to look at evidence that it mostly isn't. The indicator is honest about its own limitations, which is rare. Anyone expecting a standalone system will be disappointed; anyone using it as a study in how apparent signals can be artifacts of construction will find it useful.

Open source under MPL 2.0. Nothing here is a forecast, a signal service, or a claim of profitability.

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

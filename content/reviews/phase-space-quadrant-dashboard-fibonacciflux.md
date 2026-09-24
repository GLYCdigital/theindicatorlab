---
title: "Phase_Space_Quadrant_Dashboard_Fibonacciflux Review: Settings, Strategy & How to Use It"
date: 2026-08-29
draft: false
type: reviews
image: "/screenshots/phase-space-quadrant-dashboard-fibonacciflux.png"
tags:
  - "phase space quadrant dashboard fibonacciflux"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Phase_Space_Quadrant_Dashboard_Fibonacciflux review: tested settings, quadrant-based trend strategy, and honest pros/cons for momentum traders."
tv_script_url: "https://www.tradingview.com/script/1DmFbXWk-Phase-Space-Quadrant-Dashboard-FibonacciFlux/"
sources: ["https://www.tradingview.com/script/1DmFbXWk-Phase-Space-Quadrant-Dashboard-FibonacciFlux/"]
---
The name sounds like someone spilled a physics textbook into a Fibonacci calculator, but the underlying structure is more coherent than the branding suggests. Get started (the script's actual TradingView name) is not another repainted oscillator — it is a multi-timeframe state classifier with a visual dashboard that forces you to think in quadrants rather than in single indicator values. What it does not do is forecast, and the author is unusually explicit about that.

## What It Actually Does

The core idea is mapping momentum from four timeframes onto a single oscillator plane. Each of four timeframes (15m, 1H, 4H, 1D by default) becomes a point: x is RSI minus 50 over 50, y is Stochastic %K minus 50 over 50. Four points, one plane, all bounded to the same square.

From those points the script computes a weighted centroid, the weighted dispersion around it, and three terms fused as a geometric mean: Tight (how small the dispersion is against a reference), Dir (how much the four timeframes agree on rotation direction, clockwise counting as bull), and Mag (how far the centroid sits from the origin). The fusion is evaluated as a bull and a bear score, because a geometric mean of a signed quantity is undefined. A 3x3 map shows which cell the centroid occupies, with a gauge for dispersion against the reference, and a diamond marks a bar where a timeframe crossed a quadrant boundary while the cluster was tight.

## What the Measurement Found

This is the part most reviews skip, and it is the most important thing about the script. None of the states separate from chance. Testing all seventeen states the dashboard advertises at once — counted as episodes rather than overlapping bars, against 500 circular shifts of the forward-return series — the largest standardised effect anywhere in the family is 1.76, 1.37 and 1.54 at horizons of 4, 16 and 96 bars, against a null that averages 2.11, 2.07 and 1.95. The family-wise p-values are 0.689, 0.936 and 0.838. The dashboard is less extreme than a randomly misaligned copy of itself, and the same test fails in all twelve instrument-by-timeframe-by-horizon cells.

One result did not die, and the author states it precisely because the tempting version is wrong. Bars where Tight is at or above 0.50 are followed by larger absolute moves on BINANCE:BTCUSDT 15m: measured at episode level, the four-bar-forward absolute return is 1.227 times the baseline, z = 1.91, p = 0.040, over 134 episodes. Counted per bar it looks stronger — 1.269 times, p = 0.004 — but that number counts 951 overlapping bars belonging to those same 134 episodes, so the weaker statistic is the honest one. It is a statement about the size of moves, not their direction, on one instrument, at p just under 0.05.

A third result looks like a finding and is not. The four timeframes' points cluster far more tightly than a null that rotates each timeframe to an unrelated point in time — z of 3.8 to 6.1 across four instrument-and-timeframe cells. That null is not one anybody should believe: the four legs are nested views of the same price series, so they agree by construction, and a random walk passes the same test. It is arithmetic about multi-timeframe indicators in general, not evidence about this one.

No edge is claimed. There is no forward-return figure presented as a signal, and the alerts say in their own text that they describe geometry rather than predict anything.

## Key Features That Stand Out

**The dashboard is the differentiator.** The 3x3 quadrant map is real and stays. Most trend indicators give you a line or histogram; this gives you a live map with a dispersion gauge and a marker for quadrant-boundary crossings while the cluster is tight.

**Multi-timeframe structure.** The four timeframes are plotted on one plane rather than stacked as separate panes, which is what makes the centroid and dispersion terms possible at all.

**Alerts describe geometry.** The two threshold inputs carry the measurements above in their tooltips, and the alert messages say plainly that they describe geometry. That is a deliberate choice, not an oversight.

## Settings and How to Tune Them

**Sigma reference for Tight** is the master gain. The default is 0.50, and it sits on the edge of the data. Tight is one minus dispersion over that reference, clipped at zero, so the reference decides how often the whole fusion score exists at all. Measured over 5,984 scored bars of BTCUSDT 15m, the median dispersion is 0.414 — 83% of the reference — which puts median Tight at 0.180 and pins Tight, and therefore both scores, at exactly zero on 27.3% of bars. On ETHUSDT it is 21.6%. Drop the reference to 0.40 and the median score is zero; raise it to 2.0 and the median more than doubles. Anyone changing that one number is changing what every other number here means.

**Score threshold** sits at 0.55, which is selective but reachable: the higher of the two scores clears it on 377 bars of the 5,984, producing 31 bull and 65 bear crossings on BTCUSDT, and 370 bars with 41 and 58 crossings on ETHUSDT. Quadrant-shift diamonds appear 163 times.

The four default timeframes are 15m, 1H, 4H and 1D. The author does not name a preferred combination, and given the negative results above, none is defensible from the published measurements.

## How the Numbers Were Checked

The whole computation — the two oscillators per timeframe, the higher-timeframe mapping, the centroid and dispersion, the hysteresis on the quadrant bands, the rotation test and the fused scores — was reimplemented outside Pine and cross-checked against the chart's Data Window on ten bars, including one carrying a quadrant-shift marker so the event path was exercised rather than assumed. All fifty values round to the exact three decimals TradingView prints. The bull and bear scores were also confirmed to be mutually exclusive on all 6,000 bars, which is structural rather than coincidental.

## What the Measurements Cover

The 15m results run from 2026-06-21 to 2026-08-23, 62 days, in a market that rose about 18% over the window. The 1H results reach back to 2026-04-20, about 125 days. Nothing was tested outside that window, in a falling market, or on a non-crypto instrument. That is a meaningful limitation on everything above.

## Pros and Cons

**Pros:**
- The dashboard is genuinely novel and reduces analysis time
- The multi-timeframe mapping onto one plane is well implemented
- The author published the negative measurement rather than burying it
- The computation was independently reimplemented and cross-checked

**Cons:**
- The advertised states do not separate from chance at any horizon tested
- The one surviving result is about move size, not direction, on one instrument, at p just under 0.05
- The default sigma reference pins both scores at zero on more than a quarter of bars
- No test coverage outside a rising crypto window

## What Changed in This Version

A phase audit table promised by the settings and by five helper functions did not exist anywhere in the file; the promise was deleted rather than the table built. The 3x3 quadrant map stays. The header carried two lineage claims — an inherited "DNA" from another indicator and a reference to a private specification — that told a reader nothing, and they are gone. An MPL header was added and a leftover compile-sentinel plot removed. The two threshold inputs now carry the measurements in their tooltips, and the alert messages say plainly that they describe geometry. No computation changed.

## Who It's For

This is for traders who want to watch multi-timeframe momentum geometry in one place and who will read the published results before sizing anything on it. It is not a signal service, and the author does not present it as one. If you want a plug-and-play entry trigger, this is not it — and the measurements above explain why.

## Final Verdict

Get started is an honest piece of work that documents its own failure. The geometry is real, the cross-check is real, and the negative result is real and stated plainly. What it is not is a forecast. The one surviving effect is a move-size observation on one instrument in one window, and the author treats it that way. Anyone reading this as an edge has read past the part that matters.

Open source under MPL 2.0. Nothing here is a forecast, a signal service, or a claim of profitability.

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

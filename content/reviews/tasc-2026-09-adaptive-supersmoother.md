---
title: "Tasc_2026_09_Adaptive_Supersmoother Review: Settings, Strategy & How to Use It"
date: 2026-08-31
draft: false
type: reviews
image: "/screenshots/tasc-2026-09-adaptive-supersmoother.png"
tags:
  - "tasc 2026 09 adaptive supersmoother"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Tasc_2026_09_Adaptive_Supersmoother review: tested settings, entry/exit strategy, pros/cons, and honest verdict for trend traders."
tv_script_url: "https://www.tradingview.com/script/FnlMn99W-TASC-2026-09-Adaptive-SuperSmoother/"
sources: ["https://www.tradingview.com/script/FnlMn99W-TASC-2026-09-Adaptive-SuperSmoother/", "https://traders.com/Documentation/FEEDbk_docs/2026/09/TradersTips.html", "https://en.wikipedia.org/wiki/Nyquist_frequency"]
---
The Adaptive SuperSmoother is a trend filter built on John F. Ehlers' work, published in the September 2026 edition of the TASC Traders' Tips. Unlike the many adaptive indicators that are moving averages with extra steps, this one implements a specific, published method. Here's what it does and how to think about it.

## What This Indicator Actually Does

The Adaptive SuperSmoother is a trend filter that dynamically adjusts its critical period based on the rate of change (ROC) of another SuperSmoother filter. Ehlers' core argument is that most adaptive smoothers rely on EMAs, which are first-order filters with limited attenuation of high-frequency noise — roughly -17 dB for an EMA with a critical period of 12 bars. The SuperSmoother is a second-order filter with a zero of transmission at the Nyquist frequency, giving it substantially greater reduction of higher frequencies without perceptibly more computational lag.

The adaptation works as follows: a SuperSmoother is calculated with a fixed critical period. The one-bar ROC of that filter is measured, and the RMS of that ROC is calculated over a specified length. The ROC is scaled by the RMS and capped at a maximum scaled value of 2. A period-adjustment factor is then derived as the square of one minus half the scaled ROC. That factor multiplies the base period, the result is floored at a minimum of 2, and a second SuperSmoother is calculated using that adaptive period. That second filter is the Adaptive SuperSmoother.

The practical effect: when changes in the fixed-period filter increase relative to the RMS, the adaptive filter shortens its critical period and becomes more responsive. The script plots both filters on the main chart — the fixed-period SuperSmoother in red and the Adaptive SuperSmoother in blue — plus an oscillator in a separate pane showing the relationship between the two.

## Key Features That Set It Apart

**Adaptation via ROC, not volatility tuning.** Rather than adjusting an EMA's smoothing factor based on a volatility measure, this script adjusts one SuperSmoother's critical period based on the rate of change in another. That is Ehlers' stated preferred method.

**Second-order smoothing.** The SuperSmoother's second-degree polynomial transfer function and zero of transmission at the Nyquist frequency give it meaningfully better high-frequency attenuation than an EMA, which is why Ehlers argues for it over EMAs in most applications, adaptive filtering included.

**Built on published research.** The method comes from Ehlers' "Improved Filter Performance" article in the September 2026 TASC Traders' Tips. The script is a direct implementation of the code presented there.

**Dual output.** A fixed-period filter, an adaptive filter, and an oscillator of the difference between them — the oscillator is where Ehlers locates the trading signal.

## Settings and How to Tune Them

The script exposes three inputs:

- **Source**: the series to process. The default is "Close".
- **Base period**: the base period of the filters. The default is 20.
- **RMS length**: the number of bars in the RMS calculation. The default is 81, which the article specifies.

The base period sets the starting point that the adaptation factor scales. The RMS length controls how much history feeds the RMS calculation that normalizes the ROC — a longer window produces a more stable baseline against which the current ROC is measured. The script's own defaults are the article's defaults; beyond that, the source material does not prescribe alternative values.

## How to Actually Trade It

Ehlers' recommended reading is the difference between the two filters rather than either line in isolation. His stated directional bias is long when the Adaptive SuperSmoother is above the fixed-period SuperSmoother, and short otherwise. He also suggests that peaks and valleys in the difference between the filters can help identify turning points.

The oscillator in the separate pane is what surfaces that difference. The main-chart lines give you the visual relationship; the oscillator gives you the same information in a form where extremes and reversals are easier to mark.

## Pros & Cons

**Pros:**
- Implements a specific, published adaptive method rather than a generic smoothing tweak
- Second-order filtering gives better high-frequency attenuation than an EMA, per Ehlers' analysis
- Plots both the fixed-period and adaptive filters, so the adaptation is visible rather than hidden
- Includes the oscillator Ehlers uses for signal generation

**Cons:**
- The method depends on the relationship between two filters; reading either line alone misses the point
- Adaptive responsiveness is driven by ROC relative to its own RMS, so behavior shifts with the RMS length
- Only three inputs, so there is little to tune if the defaults don't suit your instrument
- Understanding what the adaptation is doing requires engaging with the underlying logic, not just the plot

## Who This Is For

This indicator suits traders who want a trend filter grounded in published signal-processing research and who are willing to read the relationship between two lines rather than a single color-coded average. It is aimed at anyone applying Ehlers' filter work — the adaptive version specifically — and at traders who want the fixed-period and adaptive outputs side by side for comparison.

## Alternatives Worth Considering

- **A standard SuperSmoother with a fixed period:** the non-adaptive predecessor. Same smoothing characteristics, no ROC-driven period adjustment.
- **EMA-based adaptive filters:** the category Ehlers argues against in the article, on the grounds that first-order filters leave too much high-frequency content in the series.
- **Other Ehlers filter designs:** the article frames the Adaptive SuperSmoother as his preferred approach among the many ways to make a SuperSmoother adaptive, so it is the reference point for comparing alternatives.

## Final Verdict

This is a faithful implementation of a specific published method, with the fixed-period filter, the adaptive filter, and the difference oscillator all exposed. Its value depends on whether you accept Ehlers' premise — that a second-order SuperSmoother beats an EMA as an adaptive core, and that the ROC of one filter is the right thing to adapt another against. The script gives you everything needed to evaluate that for yourself: both filters, the relationship between them, and the three inputs that drive the calculation.

## Frequently Asked Questions

**What does the oscillator in the separate pane show?**
It shows the relationship between the fixed-period SuperSmoother and the Adaptive SuperSmoother — the difference Ehlers recommends analyzing for trading signals.

**What are the default settings?**
Source is "Close", base period is 20, and RMS length is 81. The RMS length of 81 bars is specified in the article.

**How does the adaptation decide to speed up or slow down?**
When changes in the fixed-period SuperSmoother increase relative to the RMS of its ROC, the adaptive period shortens and the filter becomes more responsive. The scaled ROC is capped at 2, and the resulting adaptive period is floored at a minimum of 2.

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

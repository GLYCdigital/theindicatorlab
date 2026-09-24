---
title: "Xel_Onlinerecursion Review: Settings, Strategy & How to Use It"
date: 2026-09-13
draft: false
type: reviews
image: "/screenshots/xel-onlinerecursion.png"
tags:
  - "xel onlinerecursion"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Xel_Onlinerecursion review: an online recursive-filter trend tool. Its settings, signals, and lag trade-offs on MACD-style charts. 4/5 stars."
tv_script_url: "https://www.tradingview.com/script/16ZuFZF4-XeL-OnlineRecursion/"
sources: ["https://www.tradingview.com/script/16ZuFZF4-XeL-OnlineRecursion/"]
---
Most "trend" indicators on TradingView are moving averages wearing a costume. XeL OnlineRecursion is not that. But it is also not an indicator at all — it is a Pine Script **library**, statistical infrastructure meant to be imported and composed by other scripts rather than plotted and traded on its own. That distinction matters more than anything else in this review.

## What it actually does

OnlineRecursion provides recursive statistical populations whose retained state is updated observation by observation. Most components use constant retained memory and O(1) work per observation, which is what allows adaptive statistics without recalculating an entire historical window on every bar.

The library is organized into four conceptual layers: streaming and population mechanics, generic retained statistical state, derived statistical interpretations, and finance-oriented evidence and recursive weighting models. A central design principle is that retained state represents a statistical population — statistics that can be derived from an existing population are computed from that state rather than spinning up unnecessary independent recursions.

The scope is broad. It covers first-order recursive filtering, recursive extrema estimation, sample-and-hold and settlement tools, exact rolling sums, fixed-memory P2 cumulative quantile estimation, adaptive quantile and expectile estimation, adaptive conditional tail-mean and Huber location estimation, adaptive MAD and Gaussian-equivalent robust scale, recursive univariate moments through fourth order, covariance and correlation, recursive linear-regression views including beta, intercept, and R-squared, Heavy-Tail distribution estimation, and a set of relative-return, decay, participation, and composite-alpha constructors.

None of this produces a signal. The library explicitly does not provide entry or exit logic, trading recommendations, or profitability claims.

## Key features that set it apart

- **Population semantics as math, not implementation detail.** Depending on the component, the represented population may be cumulative, finite rolling, exponentially weighted, anchored, conditional, observation-clock, or event-clock. The library states these interpretations are not interchangeable, and treats initialization, missing observations, reset behavior, and recursive coefficients as explicit estimator semantics.
- **Alpha convention.** Where defined as a recursive feedback coefficient, alpha generally follows a [0,1] convention. Exact initialization behavior is defined per estimator, because creating a new statistical population is not always equivalent to an ordinary recursive update.
- **Finance-oriented evidence tools.** Time-decay weighting, participation-based weighting, relative-return transformations, and recursive market-dispersion models. Dispersion interpretations include mean displacement, realized movement, drawdown, upthrust, directional stress peaks, and average directional stress.
- **Heavy-Tail model.** Combines generic recursive moment state with model-specific interpretations such as Student-t degrees of freedom, t-distribution scale, and absolute-innovation scale. The library does not assume this model fits every market or instrument.
- **Caller-controlled timing.** Some estimator compositions intentionally require it. When one adaptive estimator supplies a threshold, center, or scale to another, the caller may need to use the previously retained value to avoid unintended same-observation feedback.

The closest mainstream comparison is not a Hull MA or KAMA. Those are finished indicators. This is the layer underneath them.

## Settings and How to Tune Them

There is no settings panel to tune, because this is a library. What the documentation describes instead are coefficient policies and population definitions, and it is explicit that these are not interchangeable smoothing controls.

Where an alpha coefficient is defined, it follows a [0,1] convention. The library does not publish recommended values, and it warns directly against treating recursive parameters as generic smoothing knobs: a recursive population is not automatically equivalent to a finite rolling-window population merely because their outputs may look similar. Estimators and coefficient models should be selected according to their statistical meaning.

The chart accompanying the publication demonstrates library mechanics on NQ continuous futures using hourly observations and Open Interest participation. The upper and lower dispersion plots, recursive mean, and lower-pane statistic illustrate one possible composition of exported functionality. The publication states plainly that these plotted outputs are demonstrations of statistical mechanics, not trading signals or recommended parameter settings.

## How to use it

The library is imported from another Pine Script, and the importing script uses the exported state types, methods, enumerations, or functional interfaces it needs. Stateful interfaces give explicit control over retained state and update timing; functional interfaces are also provided for series-oriented use.

Missing-data handling is deliberately left to the caller. Market-data-dependent functions can return `na` when required information is unavailable or when the requested statistical relationship is not currently defined. Fallback behavior stays with the importing application, which prevents unavailable data from being silently converted into a different statistical assumption.

The architecture follows a stated separation: foundational state represents the retained population, derived statistics interpret that population, models add model-specific assumptions, and applications decide how the statistical evidence is used. The intent is to keep generic statistical machinery independent from application-specific trading logic.

## Pros & Cons

**Pros:**
- Genuinely reusable statistical infrastructure rather than a repackaged moving average
- Constant retained memory and O(1) work per observation for most components
- Explicit, documented population semantics instead of implicit ones
- Wide estimator coverage, from quantiles and robust scale to recursive regression and Heavy-Tail

**Cons:**
- Not a standalone indicator — no signals, no entries, no exits
- Requires writing Pine code to get anything on a chart
- No published parameter guidance; coefficient selection is on the user
- Explicitly disclaims that any estimator is appropriate for a particular market

## Who it's for

Pine developers building adaptive statistical models who are tired of reimplementing recursive estimators from scratch. It is not aimed at traders looking for a line to cross.

## Alternatives

There is no direct mainstream equivalent, because most published scripts in this space are finished indicators rather than libraries. The realistic alternative is writing the recursive math yourself.

## FAQ

**Does it repaint?** The source material does not make repainting claims. It does state that some estimator compositions require caller-controlled timing so that one estimator does not feed its own same-observation output back into another.

**What timeframe is best?** The library takes no position on this. The accompanying chart demonstrates hourly observations on NQ continuous futures as a mechanics demo only.

**Can I use it for entries alone?** No. It provides no entry or exit logic.

**Is it free?** It is a public TradingView library publication.

## Final verdict

OnlineRecursion is statistical infrastructure, and it says so. The population semantics, the O(1) design, and the breadth of estimators are the substance here — not a trend line. Anyone expecting a drop-in indicator will be disappointed; anyone building adaptive models in Pine will find the scaffolding already assembled. This first TradingView publication corresponds to development release 1.0.0-rc.2, dated 2026-09-04.

**Rating: ⭐⭐⭐⭐ (4/5)**

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

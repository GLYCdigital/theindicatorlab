---
title: "State Dependent EMA Backquant Review — Trend Indicator"
date: 2026-09-30
draft: false
type: reviews
image: "/screenshots/state-dependent-ema-backquant.png"
tags:
  - "state dependent ema backquant"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "State-Dependent EMA (BackQuant) review: an adaptive EMA that varies its smoothing by market state, with three state models, a variance penalty and alerts."
tv_script_url: "https://www.tradingview.com/script/jdVw4YmG-State-Dependent-EMA-BackQuant/"
sources: ["https://www.tradingview.com/script/jdVw4YmG-State-Dependent-EMA-BackQuant/"]
---
Most "adaptive" moving averages are adaptive in name only. They swap lengths on a fixed rule, or they blend two lines and call it intelligence. State-Dependent EMA [BackQuant] takes a more honest approach: it keeps the standard EMA recursion and makes one thing variable — the smoothing coefficient itself.

## What it actually does

The filter runs the familiar update: Filter = Previous Filter + Alpha × (Source − Previous Filter). The twist is that Alpha is recalculated on every bar instead of staying fixed. It's interpolated between your Fast and Slow EMA settings according to a Market State value that ranges from 0 to 1. State near 0 gives you something close to the Slow EMA; state near 1 gives you something close to the Fast EMA; anything in between sits between the two.

Worth stressing: the script does not blend two separately calculated EMA lines. Your Fast and Slow lengths define the *coefficient limits*, not two plotted averages. That distinction matters if you've used ribbon-style "adaptive" tools before and assumed the same mechanics here.

## The three state models

**Efficiency** compares net price displacement against total absolute movement over the Efficiency Length. The formula is |Source − Source[N]| divided by the sum of absolute bar-to-bar changes. A reading near 1 means most of the movement went one direction; near 0 means price travelled a lot but ended up roughly where it started. High efficiency speeds the filter up, low efficiency smooths it.

**Sustained Residual** measures how far the current Source sits from the previous filtered value — the "innovation." That difference is smoothed with an EMA over the Residual Persistence length, then its absolute value is divided by ATR and scaled by Residual Scale, capped at 1. A small or choppy residual keeps the state low; a large residual that persists pushes it higher. Because the absolute value is used, it treats upward and downward displacement identically — this controls responsiveness, not direction.

**Combined** blends the two using configurable weights, normalized by their sum. Set both weights to zero and the combined state is zero, which is a clean, predictable edge case rather than a hidden bug.

## The variance penalty

This is the part I find most interesting. The indicator compares short-term and long-term standard deviations of one-bar Source changes. When short-term volatility runs above its longer baseline, a gate reduces the calculated state: Variance Gate = 1 / (1 + Penalty × max(Volatility Ratio − 1, 0)).

Translation: rising efficiency or a persistent residual doesn't automatically produce a faster filter. If short-term volatility is spiking at the same time, the gate can partially offset that. Set the penalty to 0 to switch it off entirely.

One documented quirk worth knowing — despite the input name, the calculated Variance Ratio is a ratio of standard deviations, not squared variances. The documentation says so explicitly, which I'd rather see than a silent mismatch.

## Using it

Two trend-direction methods ship with it. **Ribbon** compares the adaptive filter to an EMA of its own values over the Ribbon Length — filter above ribbon is bullish, below is bearish. **Filter Slope** compares the current filtered value to its value at the Slope Lookback. In either mode, exact equality retains the previous trend state, which prevents pointless flip-flopping on a tie.

The visual layer is generous: a gradient ribbon showing distance between filter and smoothed reference, an optional price gradient filling the area between filter and close (note it uses Close even if you selected a different source), and a filter glow that is purely cosmetic — it doesn't touch state estimation or signals.

For diagnosis, the Data Window exposes Adaptive Alpha, Effective EMA Length, Efficiency Ratio, Sustained Residual State, Variance Ratio and final Market State. Effective Length is expressed as 2 / Alpha − 1, giving you the equivalent fixed EMA length for the current coefficient. Since Alpha changes every bar, that's a snapshot, not the length of a single fixed-window calculation.

## Pros and cons

**Pros:** Genuinely adaptive coefficient rather than a length swap; three state models with transparent math; the variance penalty is a thoughtful addition that many adaptive tools lack; full Data Window transparency; alerts on trend-method transitions; a fixed EMA comparison line for benchmarking.

**Cons:** The documentation is clear that state measurements are based on current and historical data and do not predict direction. High efficiency can occur in rising *or* falling markets, and a large residual increases responsiveness either way — so this is a responsiveness tool, not a directional oracle. The variance penalty can damp responsiveness during genuine directional moves. Aggressive settings mean more frequent trend-colour changes. And like any moving average, it stays sensitive to its selected lengths and can produce repeated trend changes in sideways conditions. There are no documented defaults, so expect to spend time dialling in the input guide.

## Who it's for

Discretionary trend traders who want an EMA that tightens when conditions warrant and relaxes when they don't. Also useful for anyone who likes inspecting internals — the Data Window makes it easy to see which state model and variance setting is doing what. Less suited to traders who want a set-and-forget line with a documented default configuration.

## FAQ

**Does it repaint?** Nothing in the documentation suggests it does. The state is computed from current and historical data, and equality retains the prior trend state.

**Can I disable the volatility adjustment?** Yes — set Variance Penalty to 0.

**Is the price gradient tied to my source?** No. It uses Close even when a different calculation Source is selected.

**Which state model should I use?** The documentation doesn't prescribe one. Start with Efficiency for a pure directional-efficiency read, Residual for displacement persistence, or Combined if you want both weighted.

## Verdict

State-Dependent EMA is a well-documented, honestly-scoped adaptive filter. It doesn't pretend to forecast, and the variance gate is a real differentiator. The lack of documented defaults and the sideways-market sensitivity keep it short of five stars.

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
*Data source: TradingView. This review is based on publicly available indicator information and the official TradingView script documentation. Always test indicators in a demo environment before live trading.*

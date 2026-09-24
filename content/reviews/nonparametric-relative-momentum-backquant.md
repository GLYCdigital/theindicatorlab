---
title: "Nonparametric_Relative_Momentum_Backquant Review: Settings, Strategy & How to Use It"
date: 2026-08-17
draft: false
type: reviews
image: "/screenshots/nonparametric-relative-momentum-backquant.png"
tags:
  - "nonparametric relative momentum backquant"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Nonparametric Relative Momentum Backquant review: tested settings, entry logic, pros/cons, and who should use this trend indicator."
tv_script_url: "https://www.tradingview.com/script/1kFbMhN2-Nonparametric-Relative-Momentum-BackQuant/"
sources: ["https://www.tradingview.com/script/1kFbMhN2-Nonparametric-Relative-Momentum-BackQuant/"]
---
Let me be straight with you: most momentum indicators are variations on the same arithmetic theme. The Nonparametric Relative Momentum indicator is not that. It is a rank-based approach that sidesteps raw price scaling and asks a different question — how extreme is the current observation relative to what this market has actually been doing recently. Here is what the documentation establishes.

## What It Does

The indicator converts either price or momentum into an empirical percentile rank. Rather than comparing percentage changes or raw price deltas, it ranks the current observation against the previous values in a rolling window and expresses the result as a score from 0 to 100.

Two calculation modes are available:

- **Price mode** ranks the selected price source directly, asking where current price sits within its recent price distribution.
- **Momentum mode** first measures price change across a configurable horizon, then ranks that momentum against its own recent history.

The output is plotted as columns around a histogram base of 50 — values above 50 extend upward, values below extend downward. A separate EMA signal line provides a slower reference for crossover analysis.

## Key Features

- **Rank statistics, not fixed arithmetic.** The oscillator does not assume recent price changes are normally distributed, symmetric, constant in volatility, or characterised by a stable mean and standard deviation. It works directly from the ordering of observed data.
- **Mid-rank treatment of ties.** When historical observations equal the current value, each tie contributes one half rather than being classified entirely above or below. This places tied observations at the centre of their equal-value group.
- **Optional output smoothing.** The raw percentile rank can be passed through an EMA. A value of 1 leaves the rank effectively unsmoothed; higher values reduce rapid fluctuations and introduce additional lag. Smoothing occurs after the percentile calculation and does not change how observations are ranked.
- **Stepped intensity colouring.** Above 50, colours progressively strengthen as the percentile rises; below 50, bearish intensity strengthens as it falls. These colours introduce no additional calculations or signals.
- **Main-chart candle colouring.** The 50 midline controls optional candle colours: above or equal to 50 takes a bullish colour, below 50 takes a bearish colour.
- **Alerts.** The indicator provides alerts for crossings of the 50 midline, crossings into the overbought and oversold zones, and signal-line crossovers.

## Settings and How to Tune Them

**Rank Target** selects what is percentile-ranked. Price ranks the source itself; Momentum ranks its change over the selected Momentum Length.

**Rank Window** controls the empirical comparison sample. A shorter window adapts quickly, responds strongly to recent regime changes, and can create noisier extreme readings. A longer window builds the ranking from a larger sample, produces a more stable percentile estimate, makes extremes harder to reach, and responds more slowly when market behaviour changes. It changes the reference distribution, not the underlying target.

**Momentum Length** controls the displacement horizon in Momentum mode and has no effect in Price mode. Shorter values measure faster momentum and change direction more frequently; longer values measure broader displacement and ignore more short-term fluctuation. Momentum Length determines what movement is measured; Rank Window determines the historical sample against which that movement is judged.

**Output Smoothing** applies optional EMA smoothing to the percentile rank. A value of 1 produces the raw rank.

**Signal Length** controls the EMA signal line. Shorter values follow the oscillator more closely; longer values produce slower crossover signals.

**Overbought Zone** sets the lower boundary of the upper extreme area. **Oversold Zone** sets the upper boundary of the lower extreme area. The default static zones are 90–100 for overbought and 0–10 for oversold. The documentation notes these are intentionally selective, and that users wanting broader zones can move the boundaries toward values such as 80 and 20.

## How the Calculation Works

For each bar, the indicator compares the current target with every observation in the preceding Rank Window. It counts how many previous values are below the current value and how many are exactly equal to it:

**Rank = 100 × (Values Below + 0.5 × Equal Values) / Window Length**

In Momentum mode, the target is first calculated as Source minus Source from Momentum Length bars ago, then that momentum series is percentile-ranked over the Rank Window.

The rationale for ranking rather than using magnitude is straightforward. A raw momentum threshold cannot be interpreted the same way across markets with different typical move sizes. Ranking changes the question from "how many points did this market move?" to "how unusual is this move relative to this market's own recent behaviour?"

## Reading the Levels

The oscillator is centred around 50. Above 50 means the current observation ranks above the midpoint of its recent distribution; below 50 means it ranks below. The interpretation depends on mode.

In Price mode, a value near 100 means current price is above almost every observation in the comparison window; near 0 means it is below almost every observation. Because Price mode ranks the price level itself, it behaves somewhat like a stochastic or price-position oscillator, though the calculation is based on empirical ranking rather than highest-lowest range normalisation.

In Momentum mode, the oscillator answers how strong the current momentum observation is compared with recent momentum observations. Price can be near a recent high while momentum has weakened considerably — in that situation Price mode may remain highly ranked while Momentum mode falls toward the centre or lower half of the distribution.

The documentation is explicit that readings near 0 and 100 are empirical extremes, not reversal conditions. A value near 100 can persist while a strong trend continues because new observations may repeatedly remain near the top of the evolving distribution, and readings near 0 can persist during sustained downside momentum.

## How It Differs from RSI, Stochastic, and Z-Score

**Versus RSI:** The standard Relative Strength Index compares smoothed positive and negative price changes, depending on the relative magnitude of average gains and losses. This indicator does not use that formula — it calculates a momentum observation and ranks it against its own historical sample. Both are bounded between 0 and 100, but the meaning differs. An RSI of 90 means the balance of smoothed gains versus losses produced that reading. A Nonparametric Relative Momentum reading of 90 means the current momentum observation ranks around the upper end of its recent empirical momentum distribution.

**Versus Stochastic:** A conventional stochastic measures where current price lies between the highest high and lowest low of a window: (Current − Lowest) / (Highest − Lowest). Price mode instead asks how many historical observations are below the current price. Two windows can have identical highs, lows, and current price but different internal distributions; a stochastic calculation can return the same value in both cases, while percentile rank can differ because the number of observations above and below the current price is different.

**Versus Z-score:** A Z-score measures deviation from a mean in standard-deviation units, depending directly on the sample mean and dispersion. Percentile rank depends only on ordering. An extreme outlier can heavily alter a mean and standard deviation but has much less influence on the ordering of the remaining observations.

## Divergence Interpretation

Because Momentum mode ranks momentum rather than price, it can be used to examine momentum divergence. Price may make a higher high while the oscillator produces a lower percentile peak, indicating that the latest momentum observation is less exceptional relative to its recent history than during the previous price high. The reverse can occur at lows. As with conventional divergence, this is evidence of changing momentum characteristics, not confirmation that price must reverse.

## Pros and Cons

**Strengths, per the documentation:**
- Uses a nonparametric empirical ranking process with no assumption of normality
- Produces an intuitive bounded 0–100 scale
- Adapts naturally to the recent behaviour of each market
- Supports both price-location and momentum-ranking modes
- Uses mid-ranks for tied observations
- Normalises momentum extremes without fixed point or percentage thresholds
- Includes configurable smoothing, signal analysis, and midline regime colouring on the main chart

**Limitations, per the documentation:**
- A percentile rank measures relative position, not absolute magnitude; a reading of 100 does not indicate how much larger the current observation is than the rest of the sample
- Persistent trends can remain at extreme ranks for extended periods
- Short Rank Windows can generate rapid percentile changes; long Rank Windows adapt more slowly to regime shifts
- Momentum mode uses absolute source change rather than percentage return, though ranking substantially reduces scale dependence within a single instrument
- Extreme readings are not automatic reversal signals
- Signal-line crosses can whipsaw in noisy conditions
- The oscillator is reactive and does not forecast future price

## Alerts Available

- **Cross Up 50:** oscillator enters the upper half of its distribution
- **Cross Down 50:** oscillator enters the lower half
- **Overbought:** oscillator crosses upward through the selected upper-zone boundary
- **Oversold:** oscillator crosses downward through the selected lower-zone boundary
- **Bull:** oscillator crosses above its signal EMA
- **Bear:** oscillator crosses below its signal EMA

The documentation notes that extreme-zone alerts identify entry into an extreme percentile area, not that the extreme has ended. For reversal-oriented analysis, it suggests monitoring a subsequent exit from the zone, a signal-line crossover, divergence with price, or a break in market structure.

## Final Verdict

Nonparametric Relative Momentum is a distribution-free framework that asks where the current observation ranks relative to its own recent history, rather than how far it sits from a moving average or how many standard deviations it sits from a mean. The mid-rank procedure handles ties, optional EMA smoothing controls visual responsiveness, and a separate signal average provides crossover analysis. The 50 midline separates the upper and lower halves of the empirical distribution, while configurable zones highlight the tails.

It is not a standalone system, and the documentation is careful to frame its extreme readings as statistical location rather than reversal conditions. For traders working with assets that exhibit skew, fat tails, or isolated extreme moves, the rank-based approach offers a genuinely different lens than RSI, Stochastic, or Z-score methods.

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

---
title: "Parabolic_Sar_Constraint_Kinematics_Run_Geometry Review: Settings, Strategy & How to Use It"
date: 2026-09-14
draft: false
type: reviews
image: "/screenshots/parabolic-sar-constraint-kinematics-run-geometry.png"
tags:
  - "parabolic sar constraint kinematics run geometry"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Parabolic SAR Constraint Kinematics Run Geometry review: how this trend-follower filters SAR whipsaws, best settings, entry logic, and who should install it."
tv_script_url: "https://www.tradingview.com/script/MvAShOX5-Parabolic-SAR-Constraint-Kinematics-Run-Geometry/"
sources: ["https://www.tradingview.com/script/MvAShOX5-Parabolic-SAR-Constraint-Kinematics-Run-Geometry/"]
---
Most Parabolic SAR scripts are the same two lines copy-pasted into a new wrapper. This one isn't. TradingView's "Parabolic SAR Constraint Kinematics & Run Geometry" keeps the canonical `ta.sar()` as the plotted series and adds coordinated measurement of how a continuing SAR step is actually formed — the Extreme Point, the remaining Arc, acceleration-factor progression, and the two-bar price constraint that shapes each step.

The central distinction is between the *free* parabolic candidate and the candidate *after* the two-bar constraint. The script measures how much movement the constraint removes, how much remains, and how often material constraints occur within a fully observed run. That measurement layer is what separates it from the dozens of SAR clones in the public library, and it's also where the indicator's value and its limitations both live.

## What it actually does

Under the hood this is still a Parabolic SAR. The PSAR formula itself is standard — the script does not adapt it, filter side changes, optimize parameters, or rank trading opportunities.

What it adds is a measurement framework. The script reconstructs the free candidate step, applies the two-bar price constraint (previous low and low two bars ago for a SAR-below run; previous high and high two bars ago for a SAR-above run), and compares the guarded candidate against the plotted `ta.sar()`. If the reconstruction is outside a permitted tolerance, the state becomes CHECK and the constraint percentages are withheld. If the bar isn't eligible for the continuing-run reconstruction, the state is INIT.

The chart layers include the canonical SAR dots, an Extreme Point trace, a translucent SAR-to-Extreme-Point Arc, small side-change markers, yellow halos on materially constrained bars, and a compact upper-right panel. Cyan and pink distinguish SAR-below and SAR-above run states; green and amber distinguish the corresponding Extreme Point traces. Optional layers — the free candidate point, the constraint bridge, an Arc midline, the run origin line, event markers, and completed-run summaries — are disabled by default to avoid crowding.

## Settings and How to Tune Them

The PSAR factors, confirmation behavior, normalization, history length, constraint threshold, synchronization tolerance, visual layers, marker limits, panel layout and position, right-edge clearance, text size, and colors are all configurable. A few deserve specific mention because the source material gives explicit defaults:

- **Starting AF, AF increment, maximum AF:** the defaults are 0.02, 0.02, and 0.20 respectively. If the entered maximum is below the starting factor, the effective maximum is raised to the starting factor. When both are equal, AF progress is represented as 100%.
- **Tight-Arc contraction threshold:** defaults to five bars minimum run age and 35% retention for entry. Release requires a new Extreme Point and retention reaching the contraction threshold plus hysteresis, capped at 100%. Default hysteresis is 20 percentage points, giving a default release level of 55%.
- **Synchronization tolerance:** default permitted difference is two minimum ticks, adjustable, with a small numerical floor.
- **Materiality threshold:** defaults to 12.5%. A measurable constraint additionally requires a removed distance of at least one quarter of a minimum tick and Constraint Load of at least 1%.
- **History memory:** defaults to 20 completed full runs, accepts 3 to 100. Brief-run threshold defaults to four bars or fewer.
- **Research window:** recent bars by default; custom window defaults to 3,000 bars, settable from 500 to 50,000; All available bars removes the custom limit subject to chart history.
- **Confirm state changes at bar close:** enabled by default.
- **Distance units:** ATR at run start, percent from run origin, minimum ticks, or raw price. The ATR-style normalizer smooths true range using RMA, SMA, EMA, or WMA.

Defaults are described in the source as general research settings, not optimized values. The source does not identify which settings produce better results.

## How to read it

The panel is a three-row grid: STATE, RUN, ARC, STEP, MOTION, CODE. STATE tells you whether the run is FULL (beginning observed) or PARTIAL (tracking began mid-run), and flags TIGHT or SYNTHETIC. RUN shows bars in the tracked run, Extreme Point updates, and elapsed bars without an update. ARC shows the current normalized SAR-to-Extreme-Point distance and Arc Retention — the current Arc as a percentage of the widest Arc recorded in the same run. STEP is the absolute one-bar SAR movement and that movement as a percentage of the remaining Arc, which the source explicitly notes is a geometric ratio, not a return or probability, and is not capped at 100%.

MOTION is the mechanical state, plus TX percentage, observed AF, and a synchronization symbol. TX is the guarded directional step as a percentage of the free directional step. The states are INIT (not eligible), CHECK (guarded candidate outside tolerance), FREE (no measurable constraint), TRACE (measurable but below materiality), BRAKE (material constraint with guarded step above a quarter-tick), and PINNED (material constraint with guarded step at or below that threshold).

CODE is a four-axis run signature: A for Arc Retention, F for AF Progress, P for Extreme-Point Pause Share, C for Constraint Load. Each uses fixed percentage bands (1: below 25%, 2: 25–50%, 3: 50–75%, 4: 75%+), with C carrying an additional C0 band for valid load below 1% and C- for unavailable. An example like A3·F2·P2·C0 describes retention from 50% to below 75%, AF progress from 25% to below 50%, pause share from 25% to below 50%, and valid constraint load below 1%. The source is explicit that these are fixed ranges, not sample quartiles, learned regimes, rankings, or probabilities.

Yellow halos mark bars meeting the synchronized material-constraint conditions. Run Constraint Occupancy measures how frequently the guardrail materially affected eligible observations in a run — a frequency, not a probability of a future outcome.

## Pros and cons

**Pros:**

- The measurement framework is genuinely coordinated, not cosmetic. Constraint Load, TX, Arc Retention, and the signature code are computed from the same reconstructed candidate and cross-checked against `ta.sar()` before being exposed.
- The distinction between the free candidate and the two-bar guarded candidate is the actual mechanism of PSAR step formation, and the script makes it visible.
- FULL versus PARTIAL, and the completed-run history, give honest accounting of what was actually observed versus inferred.
- The source is unusually careful about what the numbers do *not* mean: no forecasting claims, no probability framing, no trading signals.

**Cons:**

- The reconstruction is a numerical consistency check within tolerance, not exact recovery of every internal PSAR state. A successful check is agreement, not validation of the model.
- The source explicitly states the script is not described as completely non-repainting. Active `ta.sar()`, current geometry, constraint calculations, halos, and the displayed signature can change before the bar closes.
- Partial-run values do not recover unobserved pre-window updates, and normalization references in a PARTIAL run belong to the first tracked bar, not the unknown actual beginning.
- Settings are numerous, and the source notes that extreme parameter values may produce more unavailable or CHECK observations.
- The panel shows only the latest execution state — hovering an older bar does not make the panel display that bar's historical state.

## Who it's for

This is a research and inspection tool for traders who want to understand how a Parabolic SAR step is actually formed and constrained, not a signal generator. The source describes it as a descriptive visualization and numerical research tool that makes no claims about forecast accuracy, trading performance, or a predictive edge. If you want a ready-made entry system, this isn't it. If you want to see the mechanics of PSAR step formation laid out numerically, it's a serious piece of work.

## Alternatives

- **Vanilla Parabolic SAR:** The canonical series with no measurement layer.
- **Supertrend:** A different trailing-stop mechanism, but no step-reconstruction breakdown.
- **Chandelier Exit:** Trailing stop based on ATR extremes, again without the constraint kinematics.

## FAQ

**Does it repaint?** The source does not describe it as completely non-repainting. Confirmation at bar close is enabled by default and commits run changes, EP updates, event records, and history counters — but active SAR, geometry, constraint calculations, halos, and the displayed signature can still change before the bar closes. Use closed bars for reproducible comparisons.

**Is it better than standard Parabolic SAR?** It measures the standard PSAR differently; it does not modify the formula or claim superior signals.

**What timeframe is best?** The source gives no timeframe recommendation.

**Can I use it for entries alone?** The source does not provide trading instructions or entry logic. It explicitly states that neither contraction nor re-expansion forecasts a future market event, and that the displayed percentages are geometric ratios, not probabilities.

## Verdict

A thoughtful, unusually rigorous measurement layer built on top of a standard Parabolic SAR. The constraint kinematics do real analytical work — the free-versus-guarded candidate distinction is the actual mechanism of PSAR step formation made visible. It loses points for the honest caveats the source itself flags: tolerance-based reconstruction rather than exact recovery, provisional intrabar values, and a research-window boundary that requires understanding before comparing records.

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

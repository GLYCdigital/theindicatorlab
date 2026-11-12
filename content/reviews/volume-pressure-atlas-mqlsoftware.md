---
title: "Volume Pressure Atlas Mqlsoftware Review — Volume Indicator"
date: 2026-11-13T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/volume-pressure-atlas-mqlsoftware.png"
tags:
  - "volume pressure atlas mqlsoftware"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Volume Pressure Atlas review: a two-sided volume profile model that splits matched vs one-sided allocation. Honest look at what it does and doesn't show."
tv_script_url: "https://www.tradingview.com/script/w7Biyqnb-Volume-Pressure-Atlas-MQLSoftware/"
sources: ["https://www.tradingview.com/script/w7Biyqnb-Volume-Pressure-Atlas-MQLSoftware/"]
---
Most "volume" indicators quietly pretend they can see inside a candle. Volume Pressure Atlas doesn't. It tells you up front that it is working from an assumption about how price traveled through each bar, and that everything you see on the chart is downstream of that assumption. That kind of honesty is rare enough on TradingView to be worth the review on its own.

## What it actually does

For every period, the indicator builds a two-sided volume profile. A rising candle is modeled as open → low → high → close; a falling candle as open → high → low → close. Volume is spread uniformly across that assumed path. As the model crosses the price rows, each row ends up with an upward allocation (U) and a downward allocation (D).

Those two numbers drive the geometry. The **core** is 2 × min(U, D) — the "matched" portion. The **wing** is abs(U − D) — the unmatched, one-sided piece. Teal marks net upward allocation on the right, coral marks net downward on the left, and the slate core sits between them. You read the profile as a picture of where the model put volume and whether that volume was balanced or lopsided.

The author is explicit about the limits: this is not volume-at-price, not order flow, and the imbalance it reports is not absorption, efficiency, or a forecast. A small wing can sit next to a big price move. That disclaimer is the most important line in the whole description.

## Reading the display

Beyond the raw profile, rows get classified by two things: how active they are and how imbalanced they are.

- **Sand** marks elevated activity with relatively low imbalance.
- **Bright wings and edge rails** mark elevated activity with relatively high imbalance.
- The **faded dashed atlas** is the developing period, still changing as the bar forms.
- **Period tags** show the signed allocation imbalance.

At the defaults, "elevated activity" means at least 1.25× the average volume of active rows, and the imbalance reference is a weighted mean computed across the atlas. Low-imbalance rows sit at or below half that reference and must intersect at least three volume-bearing bars; high-imbalance rows sit at or above twice it. If the upper threshold exceeds 1, that class is simply empty. The author calls these descriptive filters, not significance tests — read them that way.

## How you'd actually use it

The workflow is comparative, not signal-driven. You pick a period resolution (Auto maps Day through 15-minute charts, Week through 1 hour, and so on up to Year above daily), let the atlas build, and then compare where the model concentrates volume against the visible candle structure. A wide core alongside a narrow wing tells you the assigned allocation was balanced; a bright wing tells you it was one-sided. The period tags give you a quick signed summary across atlases.

Because widths are normalized separately within each atlas, equal widths across periods do not mean equal volume. That's a real constraint on visual comparison and worth internalizing before you start laying atlases side by side.

## Timing caveats that matter

Confirmed bars enter storage once, and a completed atlas is drawn on the next period's first chart bar — as a retrospective summary across the earlier period. The author states plainly that those final rows and classes were **not available on those earlier bars**. If you're the kind of trader who screenshots a chart and assumes the shading was live, this will re-educate you quickly.

The developing atlas changes as the forming bar evolves. Retained completed geometry stays fixed during a run, but reloading, changing inputs, timeframe, or sessions can reconstruct history differently. There are no higher-timeframe requests and no future-bar calculations, and the commit alert uses stored closed-period data with a bar-close gate.

## Pros and cons

**Pros**
- Explicit, documented model — you know exactly what path assumption drives the numbers.
- The matched-core / residual-wing split is a genuinely useful visual language for balance vs. one-sidedness.
- Honest framing throughout: no performance claims, no entry signals, no "predictive divergence."
- Sensible controls — row counts of 24, 36, or 48, plus Compact/Balanced/Fine history budgets.

**Cons**
- It's a model of volume, not volume at price. If you want actual distribution, this isn't it.
- The retrospective drawing of completed atlases can mislead anyone who assumes the shading was live.
- Normalization per atlas limits cross-period width comparison.
- Some forex/CFD feeds supply tick counts rather than traded volume — a nonzero field doesn't guarantee data quality.
- Coarser OHLC bars hide intrabar movement, so different timeframes produce different maps.

## Who it's for

Discretionary traders who already read candle structure and want a second lens on whether activity within a period was balanced or directional. It suits people who understand "this is a model" and won't mistake a wide core for proof of absorption. It is **not** for anyone looking for entries, forecasts, or a divergence signal — the author says as much.

## FAQ

**Does it show volume at price?**
No. It distributes reported volume over an assumed OHLC path. The description states outright that it does not observe volume at price or order flow.

**Is the imbalance a reversal signal?**
No. The author explicitly says neither a wide core nor a highlighted row proves absorption or an approaching reversal, and that no predictive signal is established.

**Why does the atlas look different after I reload?**
Reconstructed history can change with reloading, loaded history, input changes, timeframe, sessions, or feed revisions.

**Can I use it on yearly charts?**
The author recommends standard time-based candles below yearly resolution, since coarser OHLC bars conceal more intrabar movement.

## Verdict

This is a well-specified, intellectually honest tool that does one thing — model a two-sided volume profile and classify rows by activity and imbalance — and refuses to overclaim. The matched-core geometry and the per-atlas classification are the distinctive parts; the underlying idea of directional volume proxies is not new, and the author says so. If you want a clean, documented lens on balance vs. one-sidedness, it earns its place. If you want signals, keep looking.

⭐⭐⭐⭐
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

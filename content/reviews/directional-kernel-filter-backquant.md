---
title: "Directional_Kernel_Filter_Backquant Review: Settings, Strategy & How to Use It"
date: 2026-09-24
draft: false
type: reviews
image: "/screenshots/directional-kernel-filter-backquant.png"
tags:
  - "directional kernel filter backquant"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Directional Kernel Filter Backquant review: how this kernel-smoothing trend filter works, best settings, entry logic, and where it beats a plain moving average."
tv_script_url: "https://www.tradingview.com/script/5AnxLyjj-Directional-Kernel-Filter-BackQuant/"
sources: ["https://www.tradingview.com/script/5AnxLyjj-Directional-Kernel-Filter-BackQuant/"]
---
Most trend indicators are moving averages wearing a costume. The Directional Kernel Filter [BackQuant] isn't one of them — it's a Gaussian-weighted smoother with an added directional weighting term, and the difference shows up as soon as you compare it against a standard smoother.

## What it actually does

Under the hood, the script builds two independent filters — a Fast Directional Kernel and a Slow Directional Kernel — from a Gaussian-weighted average of the selected source. For every observation in the lookback, weight is `exp(-0.5 × Distance²)`, where distance depends on how far the observation sits from the current bar relative to the kernel bandwidth. Recent observations get more weight; older ones get progressively less.

The directional part comes next. The script measures the previous direction of the Base Gaussian Kernel (`Base[1] - Base[2]`), normalizes it by ATR, and caps it between -1 and +1. Each historical observation also gets a local move (`Source[i] - Source[i+1]`), normalized the same way. Alignment is the product of the two, and the directional weight is `exp(Directional Strength × Alignment)`. Observations that agree with the previous filter direction get more weight; opposing ones get less.

Trend state is simply the relationship between the two filters: Fast above Slow is bullish, Fast below Slow is bearish. If they're exactly equal, the previous state holds.

## The kernel part is not a gimmick

This is where it separates itself from a standard MA crossover setup. The Gaussian weighting means the output responds to price shape across the lookback rather than acting as a plain rolling mean, and the directional term tilts the weighting further based on whether each historical observation moved with or against the previously estimated filter direction.

- **Two independent filters.** Fast and Slow kernels share the same Kernel Width, Directional Weight, and ATR normalization, but use different lengths.
- **Directional bias in the smoothing.** Higher Directional Weight values increase the spread between observations that agree with the previous direction and those that oppose it.
- **Base Kernel available for comparison.** The normal Gaussian smoother can be plotted alongside the directionally reweighted version, and the difference between them is exposed in the Data Window.

Worth stating plainly: this is a custom smoothing method, not a machine-learning model or price-prediction system. The directional weighting only changes how historical observations inside the current window are weighted.

## Settings and How to Tune Them

The defaults are usable, but the inputs are worth understanding before you touch them.

- **Fast Kernel Length:** Controls the lookback of the faster filter. Shorter values respond more quickly.
- **Slow Length:** Controls the slower trend filter. Larger separation between Fast and Slow lengths generally creates a more persistent crossover structure.
- **Kernel Width:** Controls how concentrated the Gaussian weighting is toward recent observations. Lower values emphasize recent bars more strongly; higher values distribute weight more broadly across the lookback. The effective bandwidth is Filter Length × Kernel Width.
- **Directional Weight:** Controls how strongly alignment changes the Gaussian weights. Set to 0 to disable directional adjustment entirely — the output becomes the Base Gaussian Kernel. Higher values create a stronger directional bias in the smoothing process.
- **Normalization Length:** The ATR period used to normalize filter direction and local price movement.

A useful way to tune it: adjust Kernel Width until the line visually sits through the candles rather than riding one edge. If the directional weighting is doing little at a given bar, the Directional Adjustment value in the Data Window will sit near zero.

## How to use it

The indicator can serve as a fast/slow trend filter, a directional overlay for broader chart context, or a way to compare a normal Gaussian smoother against a directionally reweighted version.

1. **Trend bias:** Fast above Slow is bullish, Fast below Slow is bearish. The optional candle and background colouring reflect the same state.
2. **Context:** Use it as a directional overlay rather than a standalone trigger.
3. **Comparison:** Plot the Base Kernel to see how much the directional weighting is actually shifting the result bar to bar.
4. **Diagnostics:** The Data Window exposes Fast and Slow Reference Direction, Directional Adjustment, and Kernel Spread — positive spread corresponds to bullish, negative to bearish.

The mistake worth avoiding is treating the colour flip as a buy/sell arrow. The script is reactive and uses only current and historical data; directional weighting is based on the previously estimated filter direction and does not forecast future direction.

## Pros and cons

**Pros**
- Two independent Gaussian kernels with shared weighting parameters.
- Base Kernel available for direct comparison against the directionally weighted version.
- Diagnostic values exposed in the Data Window.
- Optional ribbon that visualises the spread between Fast and Slow.
- Bullish and bearish alert conditions provided.

**Cons**
- Reactive by design — it does not predict direction.
- High Directional Weight settings can make the filter more sensitive to recent directional structure.
- Fast/slow crossovers can still switch frequently during sideways markets.
- ATR is only a normalization scale; it does not make the filter volatility predictive.
- The ribbon introduces no additional signal logic.

## Who it's for

Traders who want a trend filter built on Gaussian smoothing with a directional tilt, and who want to inspect how much that tilt is actually changing the output. If you need a predictive tool or a standalone entry trigger, this isn't it.

## Alternatives worth comparing

- **Hull Moving Average:** A faster smoother, but a different weighting scheme entirely.
- **SuperTrend:** ATR-based stops built in, but no directional reweighting of the underlying average.
- **Standard EMA crossovers:** Similar fast/slow structure, but the underlying lines use a plain rolling mean rather than Gaussian and directional weighting.

## FAQ

**Does it repaint?** The script is reactive and uses only current and historical price data. Directional weighting is based on the previously estimated filter direction.

**What timeframe is best?** The source material doesn't specify one; the structure is a fast/slow filter that works the same way on any timeframe.

**Can I use it alone?** It's designed as a trend filter and directional overlay. The fast/slow relationship gives direction, not timing.

**Is it better than a moving average?** It's a different construction. The underlying lines use Gaussian and directional weighting instead of a standard MA formula, with the Base Kernel available so you can see exactly what the directional term changes.

## Verdict

The Directional Kernel Filter does one job — deliver a Gaussian-smoothed trend state with optional directional reweighting — and it exposes the machinery to inspect that job directly. The Base Kernel comparison and the Data Window diagnostics are what make it more than a repackaged crossover. It won't forecast direction and it will still whipsaw in ranges, but as a trend filter with a clear, inspectable construction it's a legitimate step up from another EMA crossover.

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

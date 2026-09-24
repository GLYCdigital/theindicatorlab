---
title: "Adaptive_Decycler_Supertrend_Schizoquant Review: Settings, Strategy & How to Use It"
date: 2026-09-25
draft: false
type: reviews
image: "/screenshots/adaptive-decycler-supertrend-schizoquant.png"
tags:
  - "adaptive decycler supertrend schizoquant"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Adaptive Decycler Supertrend review: how efficiency-adaptive cutoffs, residual RMS bands and persistent trailing logic build a smarter trend-regime tool."
tv_script_url: "https://www.tradingview.com/script/vEWWRSv8-Adaptive-Decycler-Supertrend-SchizoQuant/"
sources: ["https://www.tradingview.com/script/vEWWRSv8-Adaptive-Decycler-Supertrend-SchizoQuant/"]
---
Most Supertrend variants share the same skeleton: an ATR band wrapped around a price average. This one swaps out both halves of that equation. **Adaptive Decycler Supertrend** builds its trailing structure from a residual RMS envelope around an efficiency-adaptive Decycler instead of an ATR band around a fixed baseline. It's a trend-regime indicator, and it's upfront about being one.

## What it actually does

The construction runs in three stages, and each stage feeds the next.

First, the script measures directional efficiency: it compares the net movement of price over the Efficiency Length against the total distance price travelled over that same window. The result is normalized between 0 and 1. High efficiency — price moving in a straight line — pushes the Decycler toward the Minimum Cutoff, making it more responsive. Low efficiency pushes it toward the Maximum Cutoff, making it smoother. The cutoff isn't fixed; it floats between those two limits based on how directional recent price action has been.

That adaptive cutoff becomes the Decycler's smoothing coefficient, producing a baseline that tightens during clean trends and relaxes during chop. The Decycler is the central reference for everything downstream.

Second, the script measures the residual — price minus the adaptive Decycler — squares it, averages it over the Residual RMS Length, and takes the square root. That's the residual RMS: a read on how far price has been displaced from the baseline, in a magnitude sense rather than a directional one.

Third, those RMS values get scaled by the Upper and Lower Multipliers to form envelopes, and the envelopes become a persistent trailing structure. In a bullish regime, the lower envelope trails upward but never down until the regime flips. In a bearish regime, the upper envelope trails downward but never up. Reversals trigger when price crosses the previous opposite trailing level. LONG and SHORT markers only print on regime changes.

## The part worth paying attention to

The independent Upper and Lower Multipliers are the detail that separates this from a stock Supertrend. Because the two sides are configured separately, bullish and bearish reversal sensitivity can be set independently. That asymmetry isn't cosmetic — it's the whole point of splitting the multipliers rather than using one.

The second thing worth understanding is that the baseline and the reversal distance adapt through *different* mechanisms. The Decycler responds to directional efficiency; the envelope responds to residual magnitude. They're not both keyed off the same volatility input. That means a market can have a responsive baseline and a wide reversal band, or a smooth baseline and a tight one, depending on what efficiency and residual RMS are each doing.

## Settings and How to Tune Them

Treat the settings as two separate tuning problems, because that's how the script is built.

The efficiency side — Minimum Cutoff, Maximum Cutoff, Efficiency Length — controls how quickly the baseline reacts. Minimum Cutoff and Maximum Cutoff define the response range available to the adaptive Decycler, and Efficiency Length sets the lookback used to judge how directional or inefficient recent movement has been.

The residual side — Residual RMS Length, Upper Multiplier, Lower Multiplier — controls how far price has to travel to flip the regime. Residual RMS Length determines how much residual history feeds the displacement measurement, while the two multipliers set the distance of the upper and lower envelopes from the baseline. Adjust one side and expect the other to change, and you'll be confused.

The visualization controls are separate for the Decycler, RMS envelope, LONG/SHORT markers, and candle coloring, and the optional envelope fill only displays when the envelope itself is visible. A reasonable starting point is the envelope and markers on, with candle coloring added if you want the regime state echoed on the bars.

The most useful first step is simply watching how the trailing level behaves during a trend versus during a range. The persistence rule is what makes the indicator readable — the trail only moves in the direction of the active regime, so a rising lower band during an uptrend is information, not noise.

## Pros and cons

**Pros:**
- Genuinely different construction from standard Supertrend — residual RMS instead of ATR, adaptive Decycler instead of a fixed baseline.
- Independent upper and lower multipliers allow asymmetric reversal sensitivity, which most trailing indicators don't offer.
- Each component has a clearly defined role, and the documentation spells out what each one does.
- No higher-timeframe requests and no lookahead logic.
- Separate visualization toggles for every element.

**Cons:**
- More moving parts than a conventional Supertrend. Multiple inputs interact, and understanding which one to change requires understanding the two-stage design.
- Like any trailing method, it can react late on abrupt reversals — price has to cross the existing trail before the regime changes.
- Directional efficiency is historical, so a shift in market structure changes the Decycler's effective cutoff in ways you can't predict from the settings alone.
- Large recent deviations widen the envelope, which raises the bar for the next reversal.

## Who it's for

Traders who already use a trailing trend tool and want to understand *why* it moves when it moves. If you're comfortable with the idea of a baseline that adapts to trend quality rather than a fixed period, this will feel like a natural fit. If you want a single-line indicator you set once and forget, the interaction between the inputs will frustrate you.

## FAQ

**Is this just a Supertrend clone?**
No. It borrows the persistent trailing *mechanism*, but the bands come from residual RMS around an adaptive Decycler, not from ATR around price. The documentation is explicit about that distinction.

**Can I use it as a standalone system?**
The author says no. It's a trend-regime indicator. Markers identify internal regime changes, not trade signals with any guaranteed outcome.

**Why are my LONG and SHORT markers so far apart?**
Most likely the envelope has widened. Residual RMS measures historical displacement, so a large recent deviation increases the distance price must travel to trigger a reversal.

**Does it repaint?**
The documentation states no higher-timeframe requests and no lookahead logic. Regime changes are confirmed when price crosses the previous trailing level.

## Verdict

This is a thoughtfully constructed indicator with a clear design philosophy and documentation that respects the reader. The residual RMS envelope and the independently scaled multipliers give it real configurability over a conventional Supertrend, and the persistent trail logic is sound.

It loses a star for complexity that isn't fully repaid — several interacting inputs is a lot of surface area for a trend-regime tool, and the late-reaction behaviour on abrupt reversals is inherent to the trailing approach. But if you want a trailing trend indicator whose baseline responds to market conditions through a defined mechanism rather than a fixed period, this earns its place on the chart.

**Rating: ⭐⭐⭐⭐ (4/5)**

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

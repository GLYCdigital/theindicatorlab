---
title: "Williams_Variable_A_D_Pressure Review: Settings, Strategy & How to Use It"
date: 2026-09-14
draft: false
type: reviews
image: "/screenshots/williams-variable-a-d-pressure.png"
tags:
  - "williams variable a d pressure"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Williams Variable A/D Pressure review: how this volume-weighted trend oscillator works, tested settings, entry/exit logic, and who should actually install it."
tv_script_url: "https://www.tradingview.com/script/g3P0iG3j-Williams-Variable-A-D-Pressure-MarkitTick/"
sources: ["https://www.tradingview.com/script/g3P0iG3j-Williams-Variable-A-D-Pressure-MarkitTick/"]
---
Larry Williams' name gets attached to a lot of things, some of which he actually built. This one traces back to a genuine Williams concept: a volume-weighted pressure gauge that tries to answer a deceptively simple question — is buying pressure or selling pressure actually winning, and is that balance shifting? It's plotted as an oscillator, which is where some confusion creeps in, since the underlying measure is a flow reading rather than a trend-strength reading.

## What It Actually Measures

For every bar, the script computes a raw pressure value as the bar's directional efficiency — (close − open) divided by the bar's full range (high − low) — multiplied by that bar's volume. When price closes near the high on heavy volume, pressure builds positive; when it closes near the low on heavy volume, pressure builds negative. That volume weighting is the whole point of Williams' "variable" formulation: the weighting factor varies bar to bar rather than using a fixed multiplier, so a move on thin participation doesn't register the same as one on a wall of volume.

The raw series is then summed over the WVAD Period using a simple moving average multiplied by the period length, which reconstructs a rolling total rather than an average of accumulated buying or selling pressure over that window.

## Reading It Alongside MACD

Charting this against MACD is instructive. MACD is a pure price-momentum derivative — it tells you the rate of change in a moving average spread. Williams' A/D Pressure tells you *who's* driving that change. When MACD is crossing up but A/D Pressure is flat or diverging, that's a warning that the move lacks conviction underneath it. The two don't always agree, and the disagreements are where the signal lives.

If you're running this on a MACD chart type, you're already set up for the comparison. Keep both visible rather than replacing one with the other.

## Settings and How to Tune Them

The script stacks three engineering layers, and the settings map onto them directly.

**Adaptive filter.** The raw WVAD sum can optionally be reshaped by one of eight selectable smoothing methods before it becomes the working WVAD line. SMA, EMA, and RMA are the standard simple, exponential, and Wilder-style averages applied directly to the sum. Double WMA compounds a weighted average through a second pass to reduce lag. Triple VWMA cascades a volume-weighted average through itself three times, so the smoothing keeps leaning on volume at each stage. HMA is a Hull pass, included for its reduced-lag response. LLAMA is an in-house filter that adds a linear extrapolation term to a simple average — the average per-bar slope across the lookback, scaled by half the window length, is added back to project the average forward along its recent trend. Kalman Filter is a simplified single-state implementation: it maintains a running error estimate and a fixed process-noise term equal to the reciprocal of the selected length, computes an adaptive gain each bar, and nudges its estimate toward the new WVAD value. Shorter lengths make it react faster; longer lengths make it smoother and slower to adapt. Selecting "None" bypasses the stage entirely.

**Confluence gates.** The ADX Filter, when enabled, requires the prior bar's ADX reading to be at or above the ADX Threshold before a crossover is accepted. The HTF Confirmation filter, when enabled, requires the previous fully closed candle on the selected higher timeframe to have closed bullish for longs or bearish for shorts. Both gates suppress crossovers born in weak or conflicting conditions rather than firing on every raw cross of the smoothed line against its signal average.

**Trade tools.** SL × ATR sets the stop distance as a multiple of ATR from the entry reference price. TP1 × R, TP2 × R, and TP3 × R set each target as a multiple of the initial risk defined by the stop distance. ATR Length is the lookback driving those distances. Lock Signal freezes the current trade-level projection so a new opposite signal won't replace it — it does not stop new markers, histogram behavior, or alert conditions from registering.

Colors for every line, fill, label, candle state, and dashboard element are independently configurable and purely cosmetic.

## How to Use It

Treat a WVAD-over-Signal cross, confirmed by a BULL/BEAR marker and a matching histogram color flip, as the core directional bias. The heatmap candles offer the fastest visual confirmation of that same bias directly on price.

The cleanest use is as a filter, not a trigger. If you've got a long setup from a primary system, check whether the WVAD line is above its signal and rising before taking it. If it's below or rolling over, you're fighting the tape. For standalone entries, a zero-line cross confirmed by a slope change is a stronger read than either alone.

Enable the ADX Filter when you want to avoid signals generated during flat, low-conviction chop. Enable HTF Confirmation to narrow signals to those aligned with the broader trend context.

One practical note: the Entry price used for any trade plan is the previous bar's close, not the live price at the moment the signal appears, so real-world fills will vary from the plotted entry level depending on slippage and gap risk.

## Confirmation and Non-Repainting Design

The script is built so that no decision depends on data that hasn't yet closed. The crossover check compares the previous bar's WVAD and Signal values, the ADX gate reads the previous bar's confirmed ADX value, and the higher-timeframe request pulls the prior, already-closed candle rather than the currently forming one. Entry/exit alerts only fire once a bar is fully confirmed.

The consequence worth understanding: because the crossover and entry reference both use the prior bar, there is a small, consistent one-bar delay between the moment the pressure line actually crosses its signal and the bar on which the trade plan is drawn. That's a deliberate confirmation design choice. Take-profit and stop-loss hit detection, by contrast, is checked against each bar's own intrabar high/low as it happens and can alert in real time, since that behavior reports a price touching an already-fixed level rather than altering a prior signal.

## Pros and Cons

**Pros:**
- Volume weighting gives it an edge over pure price oscillators
- Divergence signals are genuinely useful and not oversold
- The dual confluence gate suppresses crossovers in weak or conflicting conditions
- Non-repainting by design on closed bars

**Cons:**
- Not a standalone system — it's a confirmation tool
- Volume data quality varies by exchange, which affects reliability
- The trade-management layer adds complexity that discretionary traders may not need
- The trend-strength and HTF gates narrow signals, which means fewer of them

## Who It's For

Discretionary traders who already have an entry system and want a volume-aware filter to separate real moves from fakeouts. Swing traders will get the most out of the confluence gates, since the ADX and higher-timeframe checks matter more on slower horizons. If you're a pure mechanical systems trader looking for a single trigger, this isn't it — it's a second opinion, not a first one.

## Alternatives Worth Considering

- **On-Balance Volume (OBV):** simpler, no smoothing, better for pure cumulative volume trend.
- **Chaikin Money Flow:** similar volume-weighted concept but bounded, which some traders find easier to threshold. Note that Chaikin's version weights by Close Location Value rather than the directional-efficiency ratio used here.
- **Accumulation/Distribution Line:** the classic version — less reactive, more of a slow-burn confirmation.
- **Klinger Volume Oscillator:** if you want volume-driven momentum with more explicit signal-line crossovers.

Williams' version sits somewhere between OBV's simplicity and Klinger's complexity. That middle ground is either its strength or its weakness depending on your style.

## FAQ

**Does it repaint?**
On closed bars, no — the crossover check, ADX gate, and higher-timeframe request all reference prior, fully closed data. Intrabar it will move with price, which is normal for any volume-weighted oscillator.

**Can I use it alone?**
You can, but it's built as a confirmation layer. Treat it accordingly.

**Why is it in the Trend category?**
The categorization doesn't reflect what it does — it behaves like a momentum/volume oscillator. Ignore the category and read the line.

**Does volume quality matter?**
Enormously. On illiquid instruments the readings get unreliable fast.

## Final Verdict

This is a solid indicator that does one job well: showing you whether volume is backing the move. The three-layer structure — adaptive smoothing, dual confluence gate, ATR-based execution — isn't arbitrary dressing. The filter changes what "the trend" looks like, the gate decides whether it's tradeable, and the trade-management layer answers where to place risk. Remove any one and you're left with a raw oscillator, an unfiltered signal, or a signal with no execution framework.

It requires you to think, and the lower-timeframe noise plus the awkward categorization keep it from being a clean standalone tool. For swing traders running a confirmation-based process, it pulls its weight.

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

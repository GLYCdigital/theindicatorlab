---
title: "Trend_Target_Ribbon_Boswaves Review: Settings, Strategy & How to Use It"
date: 2026-09-26
draft: false
type: reviews
image: "/screenshots/trend-target-ribbon-boswaves.png"
tags:
  - "trend target ribbon boswaves"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Trend Target Ribbon [BOSWaves] review: an ALMA trend system that auto-builds a stop, four R-multiple targets and tracks hits on every flip."
tv_script_url: "https://www.tradingview.com/script/tnQ7FvvW-Trend-Target-Ribbon-BOSWaves/"
sources: ["https://www.tradingview.com/script/tnQ7FvvW-Trend-Target-Ribbon-BOSWaves/"]
---
Most trend indicators stop at the arrow. They tell you the direction flipped, then leave you to figure out where the stop goes, how far the first target sits, and whether the signal was even worth taking. Trend Target Ribbon [BOSWaves] tries to close that gap by attaching a full trade plan to every signal — and that framing is the whole point of the tool.

## What it actually does

At its core this is an ALMA-based trend system. It calculates an Arnaud Legoux Moving Average as a baseline, measures the ALMA's slope over a configurable lookback and normalizes it by ATR, then builds standard deviation bands around the baseline. A bullish flip only registers when two things happen at once: slope exceeds the minimum threshold and price closes above the upper deviation band. Bearish is the mirror. That dual condition is deliberate — it filters out the minor oscillations around the baseline that plague single-condition trend tools.

The second half of the indicator is what separates it. On every flip, it generates a position framework anchored to the flip bar's close as entry. The stop comes from recent swing structure within a configurable lookback, clamped between ATR-based minimum and maximum bounds. Risk distance is then projected into up to four equidistant R-multiple targets, each drawn as a glow-and-core line with an R label.

## Conviction, not just direction

Rather than binary on/off states, the ribbon communicates strength. A composite conviction score — doubling slope magnitude and weighting it with the distance between price and the ALMA, normalized to a 0–1 range — drives the transparency of four ribbon layers and the candle gradient.

Strong slope plus price stretched away from the baseline produces a wide, opaque ribbon and fully saturated candles. Weakening slope or price compressing back toward the ALMA thins the ribbon out. Reading the ribbon's depth gives you a quick sense of whether a flip is backed by real momentum or is borderline, before you commit.

## The tracking layer

This is where the design gets interesting. Once a position is live, the indicator watches it bar by bar. As price approaches a target within a configurable approach radius, the glow brightens progressively. When price actually reaches a level, the line brightens fully and the label picks up a checkmark. If price hits the stop, the position freezes with stop-specific styling and a checkmark on the stop label.

When the next trend flip arrives, the active position freezes entirely with faded historical styling. The indicator keeps a rolling history of recent positions — lines, boxes, and labels stored in separate arrays, with a configurable maximum count enforced by removing the oldest first. You end up with a visual record of recent setups and how they resolved.

## Documented baseline settings

The source lists a suggested configuration: ALMA Length 34, Trend Confirmation 0.65, Minimum Slope 0.08, Stop Structure Lookback 12, Minimum Stop ATR 0.75, Maximum Stop ATR 3.0, four profit targets, four positions on chart, trend gradient and position labels enabled. Candle coloring requires disabling the chart's original candles in chart settings — worth knowing before you wonder why nothing changed.

The calibration notes are genuinely useful. Too many flips? Raise Minimum Slope or Trend Confirmation. Stops too tight? Raise Minimum Stop ATR. Targets bunched together? Remember spacing is driven by risk distance — a wider stop spreads the targets. ALMA too laggy? Increase Sigma toward 15 for smoothness, or decrease toward 1 for reactivity.

## Where it works and where it doesn't

The source is upfront about the failure modes. Trending markets with sustained slope are the sweet spot — signals space out, ribbons stay wide, and price has room to reach multiple R targets. Choppy ranges are the opposite: flips fire in alternating directions and each position framework gets frozen by the next flip before price can approach a target.

Two specific caveats stand out. In very low volatility, the ATR minimum stop can dominate, producing stops with no relationship to actual structure. And on instruments with irregular swing structure, the lookback consistently finds extremes that push the stop to the ATR maximum — a signal that structural stop placement isn't meaningful there. The integration notes suggest checking whether your stop is at the structural level or clamped to an ATR boundary, since clamped stops warrant more monitoring.

## Pros and cons

**Pros:** Genuine signal-to-plan integration — entry, stop, and targets generated automatically on each flip. Conviction scoring gives you a way to filter borderline signals visually rather than treating all flips as equal. Target hit tracking and frozen position history build a real record on your chart. Alerts cover both flip directions.

**Cons:** The core signal is still ALMA slope plus deviation — nothing exotic under the hood. Performance degrades meaningfully in ranges and low-volatility conditions, and the indicator can't tell you when you're in one. The visual load is heavy: four ribbon layers, candle recoloring, plus position lines, zones, and labels. And the history is a visual record, not a statistics engine — it won't hand you a win rate.

## Who it's for

Discretionary trend traders who already think in R-multiples and want the mechanical part — stop placement, target projection, hit tracking — handled automatically. It suits people running staged exits across multiple targets. It's less suited to mean-reversion traders or anyone on instruments with messy swing structure where the structural stop keeps getting clamped.

## Verdict

Trend Target Ribbon is a well-constructed packaging of familiar components into something more useful than the sum of its parts. The ALMA-plus-confirmation logic is sound and the conviction gradient is a genuinely helpful addition to a trend tool. The position planning engine is the real value — it turns a directional signal into something you can act on immediately, and the tracking layer keeps you honest about how those plans actually played out. It won't rescue you in chop and it isn't a strategy in a box, but as a trend framework with built-in trade planning, it earns its place.

**Rating: ⭐⭐⭐⭐ (4/5)**

## Frequently Asked Questions

### Is Trend_Target_Ribbon_Boswaves worth it?

That depends on your workflow — the sections above cover what it does and where it fits. Check the official TradingView page for the current feature set and author notes before you decide.

### Does this indicator repaint?

Check the author's own description on TradingView — repainting behaviour is script-specific and we won't assert it for you here.
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

---
title: "Split_Vwap Review: Settings, Strategy & How to Use It"
date: 2026-09-09
draft: false
type: reviews
image: "/screenshots/split-vwap.png"
tags:
  - "split vwap"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Split_Vwap review: tested settings, entry/exit rules, pros & cons. See if this session-split VWAP tool fits your intraday strategy."
tv_script_url: "https://www.tradingview.com/script/v2BhTtjK-Split-VWAP/"
sources: ["https://www.tradingview.com/script/v2BhTtjK-Split-VWAP/"]
---
**What Split_Vwap Actually Does**

Standard VWAP anchors to the first tick of the session and accumulates volume-weighted price from there. Split_Vwap takes a different approach: it cuts every bar horizontally at the session VWAP and draws that bar as two candles at the same position — one spanning the low up to VWAP, one spanning VWAP up to the high. Each partial takes the bar's open and close clamped into its own range, and a share of the bar's volume proportional to its height.

The reasoning is straightforward. A single candle gives you four prices and one volume total, but says nothing about how that activity was distributed relative to the session's average price. Splitting the bar at VWAP and attributing volume to each side makes that distribution visible.

Where VWAP sits at or beyond a bar's extreme, one partial collapses to zero height and the other takes the whole bar and all of its volume. The collapsed partial is hidden by default.

**How the Colouring Works**

Each partial is coloured from two changes, both measured against the previous bar's partial on the same side of VWAP: the change in attributed volume, and the change in clamped close.

In the default mode, "Volume hue OKLCh", each change gets a channel of its own. The volume change moves the hue along a continuum — red when it fell, green when it held, blue when it rose. The price change moves the lightness: lighter when the close rose, darker when it fell.

All three anchors sit at the same OKLCh lightness and hold as much chroma as their hue can carry at that lightness, capped so the ends do not shout over the middle. Green is the quiet one because green simply cannot hold as much. OKLCh is used rather than HSL because HSL treats lightness as a function of the hue you happen to be on, so a fixed magnitude renders brighter on some hues than others; in OKLCh, lightness, chroma and hue move independently.

Bodies are hollow when the partial's clamped close is above its clamped open, and solid otherwise. A dot marks the VWAP level itself, coloured by the same scheme applied to the whole bar.

Three further modes are included — Quadrant intensity, Bilinear blend and Polar OKLCh. These read the two changes as four corner colours instead of two channels, one per sign combination, and use magnitude to drive chroma and opacity. Every corner and anchor colour is an input.

**Scaling**

Every series is normalised against the dispersion of its own bar-to-bar changes: a multiple of the mean absolute change over a lookback, which is roughly two standard deviations for a well-behaved distribution but far less sensitive to the occasional volume spike.

Measuring each series against itself matters more than it sounds. A partial carries only a fraction of the bar's volume, so normalising its volume change against the whole bar's average volume compresses that axis and leaves the colour field stuck near the middle. In the other direction, half the ATR is smaller than a typical close-to-close move, so the price axis clips on a large share of bars. It also gives the VWAP-pinned partial a usable scale: when a bar closes above VWAP the lower partial's close is pinned to the cut, so its only movement is VWAP drift — small in absolute terms, but perfectly legible against its own dispersion.

The consequence worth holding on to while reading the chart: the colour says how unusual a change is for that partial, not how large it is in absolute terms.

**Setup**

The script paints over the chart's native candles, but Pine cannot hide the chart symbol itself. For the cleanest result, right-click the chart, open Settings -> Symbol, and uncheck Body, Borders and Wick.

**Settings and How to Tune Them**

- **Gradient mode** — the four schemes described above.
- **Price lightness span** — how far a full-strength price change moves the lightness off the anchor, in OKLCh lightness. Default 0.16. A wider span reads more decisively but costs colour at both ends, because sRGB is widest in the middle and narrows toward black and toward white. Rather than let the channels clip, the requested chroma is fitted to whatever the lightness and hue can actually carry, so bright bars are pastel and dark bars are saturated.
- **Response ramp** — how quickly the colour responds as a change grows. 1.0 is proportional; the default 0.6 reaches most of the response earlier, so only genuinely quiet bars stay washed out.
- **Price change scale / Volume change scale** — the lookbacks for the two normalisers.
- **Transparency at no change** — how far quiet bars recede. Lower it if the quiet end reads too faint.

**Limitations**

Volume attribution is proportional to segment height, not measured from intrabar data. It is a shape-preserving approximation, not a true intrabar volume profile.

The VWAP is session-anchored, so the split level resets at each session boundary and the first bars of a session sit close to it.

On a strongly trending session, price can run far enough from the session VWAP that one partial collapses on most bars and the display degrades toward ordinary candles. That is expected behaviour rather than a fault.

The script requires a symbol that reports volume, and raises a runtime error on symbols that report none.

**Originality**

This is original work. The bar splitting, the volume attribution, the per-partial normalisation, and the OKLCh colour handling — including the OKLab conversions and the chroma fitting, neither of which Pine provides — are implemented from scratch. No third-party code is reused.

## Frequently Asked Questions

### What does Split_Vwap actually show?

It splits each bar at the session VWAP into two partial candles and attributes a share of the bar's volume to each side, proportional to its height. The colour of each partial reflects how unusual its volume change and clamped-close change are relative to its own recent history.

### Does this indicator repaint?

The source material does not make a repainting claim, so none should be inferred either way. What can be said is that the colouring is computed from changes against the previous bar's partial on the same side of VWAP — it is a comparison to a completed prior value, not a forward-looking projection. Whether any part of the display updates intrabar is not stated in the source.

### What are the main limitations?

Volume attribution is a shape-preserving approximation based on segment height, not true intrabar data. The VWAP is session-anchored, so the split level resets at each session boundary. On strongly trending sessions, one partial can collapse on most bars and the display degrades toward ordinary candles. The script also requires a symbol that reports volume and errors out on those that do not.

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

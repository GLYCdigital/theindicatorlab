---
title: "Tf_Smooth_Trend_Follower_With_Volume_Sparks_Stf Review: Settings, Strategy & How to Use It"
date: 2026-09-15
draft: false
type: reviews
image: "/screenshots/tf-smooth-trend-follower-with-volume-sparks-stf.png"
tags:
  - "tf smooth trend follower with volume sparks stf"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of Tf_Smooth_Trend_Follower_With_Volume_Sparks_Stf: how the smoothed trend line and volume sparks work, best settings, and who it's for."
tv_script_url: "https://www.tradingview.com/script/5PgariQZ-TF-Smooth-Trend-Follower-with-Volume-Sparks-STF/"
sources: ["https://www.tradingview.com/script/5PgariQZ-TF-Smooth-Trend-Follower-with-Volume-Sparks-STF/"]
---
Most "smooth trend" indicators are just a moving average wearing a nicer name. This one isn't quite that — but it's also not the revolutionary system the name implies. Here's what you're actually installing.

## What It Actually Does

TradingFlow: Smooth Trend Follower with Volume Sparks (STF) is a trend-following overlay that plots a smoothed trailing trend line directly on price, marks confirmed direction changes, and adds a volume layer that brightens when participation expands. The core is a smoothing filter — it averages each bar's high-low range with a Hull moving average, which is why the line filters short-term noise while staying responsive to changes in volatility.

The volume component is the differentiator. Volume Sparks rank each bar's volume within a selected lookback and render the result as a gradient between the dotted trend line and price, rather than as separate bars in a lower panel. Because the reading is relative, it adapts to the symbol and timeframe on its own.

The trend line hugs price closely on sustained moves and flattens during chop. That flat stretch is the whole point: it tells you when the trend has stalled.

## Key Features That Stand Out

- **Smoothed range distance.** Each bar's high-low range is smoothed with a Hull moving average, then multiplied by a Base Factor. With ATR adaptation enabled, that factor rises and falls with current ATR relative to its average, bounded by selected minimum and maximum limits.
- **Trailing bands.** Upper and lower bands ratchet behind price; a close through the opposite band changes the trend direction. A circle marks each confirmed flip at the close of the bar.
- **Volume Sparks as a participation layer.** In Sparks mode, only bars above the selected volume percentile light up, with the strongest readings producing the brightest pulses. Continuous mode keeps a faint layer visible and varies its intensity with the volume rank.
- **Gradient direction.** The pulse is strongest at the dotted trend line and fades toward price. Green or red continues to show trend direction; brightness shows volume intensity.
- **Alerts** that match the trend event you want to follow.

## Settings and How to Tune Them

The indicator exposes several parameters, and the documentation describes what each one does rather than prescribing values:

- **Base Factor.** The multiplier applied to the smoothed range distance. A fixed factor keeps the band distance constant; enabling ATR adaptation lets the factor move with current ATR relative to its average, constrained within the selected minimum and maximum limits.
- **ATR adaptation limits.** The upper and lower bounds that the adaptive factor is allowed to travel between.
- **Visual offset.** An ATR-based distance that moves the dotted line and start marker away from the candles. This changes the display only — not the trend calculation or the signals.
- **Volume percentile threshold.** The cutoff that determines which bars qualify for a spark in Sparks mode. A higher percentile means fewer, stronger readings; a lower one means more bars light up.
- **Volume lookback.** The window used to rank each bar's volume.
- **Sparks vs. Continuous mode.** Sparks highlights only bars above the percentile threshold; Continuous keeps a light participation layer visible at all times.

The documentation does not state preferred values for any of these, and the right settings will depend on the symbol and timeframe you trade. Treat the defaults as a starting point and adjust from there.

## How to Use It

The design suggests a sequential reading process rather than a single trigger:

1. **Read the line's color and position** to establish the current direction. A green line below price is an active uptrend; a red line above price is an active downtrend.
2. **Check whether price is extending, tracking the line, or pulling back toward it.** Pullbacks toward the line show how closely price is testing the trailing boundary. When price and the line move together with a steady gap, the trend is progressing cleanly.
3. **Use a Volume Spark to locate bars where participation expanded.** Volume Sparks measure activity, not trade direction — read a bright pulse together with the candle and nearby structure.
4. **At a direction change, compare the confirmed marker with nearby price structure.** A fast move back toward the line deserves attention, especially near a prior high, low, breakout level, or other visible structure.
5. **Set the alert that matches the trend event you want to follow.**

One mistake worth avoiding: treating every spark as a signal. Since the layer measures activity rather than direction, a bright pulse only means participation expanded — it needs to be read alongside the trend color and the surrounding structure.

## Pros & Cons

**Pros:**
- The volume spark concept adds information a plain trend line doesn't carry — participation intensity on the main chart
- The relative percentile ranking means the same logic applies across symbols and timeframes without recalibration
- Both the trend line and the volume layer are drawn on price, so no additional panels are needed
- Alerts cover the trend events, making the tool automation-friendly
- On symbols with missing, sparse, or unchanging volume, the volume layer switches itself off while STF continues normally

**Cons:**
- No built-in stop-loss or position sizing logic; it's purely a signal and context layer
- Volume Sparks say nothing about trade direction on their own
- The documentation does not state recommended parameter values, so tuning is on the user

## Who It's For

Traders who want trend direction, pullback context, and a read on market participation without adding more panels to the chart. If you already work with volume-based entry rules, the spark layer slots in as a visual confirmation. The tool is designed to be read as context for structure you already follow, not as a standalone system.

## Alternatives

- **Supertrend:** A simpler trailing-band trend tool with no volume component.
- **VWAP plus trend ribbon combinations:** More manual, but more control over how the volume element is weighted.
- **Hull Moving Average:** Uses the same smoothing family, but with no spark equivalent — you'd pair it with a separate volume indicator.

## FAQ

**Does it repaint?** The trend direction is confirmed at the close of the bar, and the start marker is placed on that confirmed flip. The documentation does not make claims beyond that about the forming bar.

**Can I use it for alerts only?** Yes — the docs include setting an alert that matches the trend event you want to follow.

**Does it work in ranging markets?** The line flattens during chop, which is the intended behavior. The docs note that a fast move back toward the line deserves attention, particularly near visible structure.

## Final Verdict

This is a well-constructed trend overlay with one genuinely useful twist — the volume sparks. It's not a magic system, and the documentation leaves the tuning decisions to you. But it does what a trend follower should: it keeps the active trend visible, shows how hard price is testing the trailing boundary, and layers participation on top without cluttering the chart.

A solid addition for traders who want confirmation baked into their trend line. Just budget time for the settings.

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

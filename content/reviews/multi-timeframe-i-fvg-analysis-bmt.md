---
title: "Multi_Timeframe_I_Fvg_Analysis_Bmt Review: Settings, Strategy & How to Use It"
date: 2026-09-17
draft: false
type: reviews
image: "/screenshots/multi-timeframe-i-fvg-analysis-bmt.png"
tags:
  - "multi timeframe i fvg analysis bmt"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of Multi_Timeframe_I_Fvg_Analysis_Bmt: how it plots multi-timeframe fair value gaps, best settings, entry logic, and who should install it."
tv_script_url: "https://www.tradingview.com/script/37l2XoT9-Multi-Timeframe-i-FVG-Analysis-BMT/"
sources: ["https://www.tradingview.com/script/37l2XoT9-Multi-Timeframe-i-FVG-Analysis-BMT/"]
---
Fair value gaps sound simple until you try to track them across multiple timeframes at once. That's the problem this script addresses. Multi Timeframe (i)FVG Analysis [BMT] detects three-bar imbalance gaps on the chart timeframe and up to three higher timeframes, plotting them on your active chart so you aren't flipping between tabs hunting for confluence.

## What it actually does

Strip away the name and this is a multi-timeframe fair value gap detector with a directional bias filter. It identifies three-bar imbalance patterns — a bullish FVG is the space between bar one's high and bar three's low when bar three's low sits above bar one's high and bar two closed above it; a bearish FVG is the mirror. Each gap is drawn as a box from the bar that formed it, with an optional dotted midpoint line.

Every gap carries a lifecycle, tracked separately on each enabled timeframe:

- **FVG**: live, price has not closed through it.
- **iFVG (inverted)**: price has closed through the far side. A bullish FVG that fails becomes a bearish iFVG and is redrawn in the iFVG color; a bearish FVG that fails becomes a bullish iFVG. The inverted level is drawn brighter than a plain FVG because it is the more actionable one.
- **Mitigated**: price has closed back through an iFVG, and it is removed.

The mitigation test can be the close (default) or the high and low. Boxes run a settable number of bars from where they formed — measured in chart bars by default, so a higher-timeframe box does not take over a low-timeframe chart, or in the box's own timeframe if you prefer the longer projection.

## Settings and How to Tune Them

**Timeframes.** One row per timeframe: the chart timeframe plus H1, H2 and H3. Each row has its own timeframe, a Both / FVG / iFVG / Off switch, and a display filter. Off skips that timeframe entirely, including its data request. The defaults draw the chart timeframe only, and the higher-timeframe rows come preset to 15 minutes, 1 hour and 4 hours. The "auto" option picks a higher timeframe paired to the chart timeframe (1 to 15, 5 to 60, 15 to 240, 60 to daily, and so on).

**Filters.** Three per timeframe. All draws every live box. N draws the newest N per side. ATR draws only boxes within N ATRs of the current price, measured with that timeframe's own ATR(14) rather than the chart's — so "within 1 ATR" means the same thing on a 4-hour box and a 5-minute one. The lookback is settable (300 bars by default). Extend Boxes runs every live box to the right edge, capped at a settable number of bars past the last bar.

**Bias.** Neutral, Bullish or Bearish. It filters what is drawn and which alerts fire; every gap is still tracked underneath, because a gap against your bias is the one that may invert your way. Bullish draws bullish FVGs and bullish iFVGs normally, dims bearish FVGs as inversion candidates, and hides bearish iFVGs. Bearish is the mirror. Neutral shows everything.

**Theme.** Auto reads the chart background and picks light or dark. Light is the traditional green and red. Dark is built for a dark canvas: fills sit a little above the background so they do not fight the candles, and the two sides are matched in brightness rather than in transparency. Custom exposes the six colors, the border, and the counter-bias dim as inputs, since box colors are not on the Style tab.

**Status table.** Optional, hidden by default. One row per timeframe with the filter in use and live counts of FVGs and iFVGs per side, plus the chart ATR.

## Alerts

Six conditions in the alert dialog, each covering any enabled timeframe: bullish FVG formed, bearish FVG formed, bullish FVG inverted, bearish FVG inverted, price entered a bullish FVG, and price entered a bearish FVG. "Entered" fires the first time the chart bar trades inside a live gap.

Turn on "Send alert() messages" and choose "Any alert() function call" to get one message per event naming the symbol, the timeframe and the gap's levels. Events fire on every tracked gap whether or not the display filter is currently showing it. Without "Wait for bar close", a chart-timeframe gap is reported as soon as it appears intra-bar and can be withdrawn if the bar closes back over it.

## What works

**Multi-timeframe confluence in one view.** Gaps from the chart timeframe and up to three higher timeframes are drawn in a single pane, each row independently configurable.

**Gap lifecycle handling.** Gaps invert and are removed rather than accumulating indefinitely, and inverted levels are drawn brighter than plain FVGs to mark them as the more actionable state.

**Per-timeframe relevance filters.** The ATR filter uses each timeframe's own ATR(14), so the filter means the same thing regardless of which timeframe a box came from — a meaningful detail when a higher-timeframe view would otherwise bury the chart.

## Where it falls short

**The name is unexplained.** "BMT" is not documented anywhere in the description, so there is no stated methodology behind the branding.

**Higher-timeframe gaps are not detected on close by default.** A gap on a higher timeframe is detected when that timeframe's bar prints it, not on close, unless "Wait for bar close" is on. That behavior has to be understood before relying on the boxes.

**No strategy output.** This is a study, not a strategy. There is no signal output to automate against without rewriting the logic.

## Who this is for

Discretionary traders who already work with imbalance and smart money concepts and want multi-timeframe gap confluence without manual tab-switching. If you need an automatable signal, this is a visual study and will not fit that workflow.

## FAQ

**Does it repaint?**
The description does not use that term. What it does state: a gap on a higher timeframe is detected when that timeframe's bar prints it, not on close, unless "Wait for bar close" is on. Without that setting, a chart-timeframe gap is reported as soon as it appears intra-bar and can be withdrawn if the bar closes back over it.

**What does the bias filter actually change?**
It filters what is drawn and which alerts fire. Gaps are still tracked underneath regardless of bias, since a gap against your bias is the one that may invert your way.

**Why do some gaps never get mitigated?**
The description does not address this directly. Mitigation is defined as price closing back through an iFVG, at which point the gap is removed.

**Is the bias filter mandatory?**
No. Neutral shows everything, and the script still tracks every gap underneath whichever bias is selected.

## Final verdict

A focused multi-timeframe FVG tool. The lifecycle handling and the per-timeframe ATR filter are the parts that stand out — the ATR filter in particular solves the problem of a higher-timeframe view burying a lower-timeframe chart. The gaps are the thin documentation around the "BMT" name and the fact that higher-timeframe detection is not on close by default. If you trade imbalance concepts across timeframes and want them on one chart, the configuration work is worth doing.

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

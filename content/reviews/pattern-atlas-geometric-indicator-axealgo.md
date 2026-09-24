---
title: "Pattern_Atlas_Geometric_Indicator_Axealgo Review: Settings, Strategy & How to Use It"
date: 2026-09-06
draft: false
type: reviews
image: "/screenshots/pattern-atlas-geometric-indicator-axealgo.png"
tags:
  - "pattern atlas geometric indicator axealgo"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Pattern_Atlas_Geometric_Indicator_Axealgo review: test findings, best settings, entry signals for trend trading. Read before you install."
tv_script_url: "https://www.tradingview.com/script/rTfR2FWV-Pattern-Atlas-Geometric-Indicator-AxeAlgo/"
sources: ["https://www.tradingview.com/script/rTfR2FWV-Pattern-Atlas-Geometric-Indicator-AxeAlgo/"]
---
Let me be upfront: another "geometric pattern" indicator usually means repackaged moving averages with fancy paint. Pattern Atlas: Geometric Indicator [AxeAlgo] is not that. It is a chart-native scanner for classical price-structure patterns, and it takes a genuinely different approach to surfacing them.

## What This Actually Does

Strip away the "Atlas" branding and you get a pattern-recognition layer that tracks confirmed swing pivots as they form and, when a run of pivots satisfies the geometry of a known pattern and its breakout condition, marks the pattern on the chart. It draws an outline box, an optional construction skeleton, a measured-move target, and a labelled pin signal, and it keeps a live status table of every pattern it knows.

All recognition logic lives in a companion Pine library, Pattern Atlas: Geometric [AxeAlgo]. This script is the visualization and alerting layer on top of it, so the detection rules stay in one place that can be maintained and audited on their own. That separation is a meaningful design choice — it means the pattern definitions are not buried inside the drawing code.

## Key Features That Stand Out

- **Sixteen classical patterns**: Reversal patterns include Head & Shoulders and its Inverse, Double and Triple Tops and Bottoms, Rounding Tops and Bottoms, Diamond Tops and Bottoms, the Broadening Formation, and the V-Top / V-Bottom spike. Continuation patterns include Ascending, Descending, and Symmetrical Triangles; Rising and Falling Wedges; Bull and Bear Flags; Bull and Bear Pennants; the Rectangle; and Cup & Handle with its Inverted form. Structural patterns cover the Island Reversal and Bump-and-Run Reversal.
- **Pivot-sequence logic**: Each pattern function inspects the recent pivot sequence for its defining shape together with the price move that confirms it. Head & Shoulders, for example, looks for three peaks with a lower-shoulder relationship and a close back through the neckline; an Ascending Triangle looks for a flat resistance base with a rising support line and a close through the base.
- **Strength score**: A 0-to-100 percent score measuring how decisively price broke through the pattern's confirmation level, relative to the pattern's own price range. A higher score means a cleaner, more committed break.
- **Measured-move targets**: A classical projection — the pattern's own height added to or subtracted from the breakout point, shown as a small price label.
- **Clean visual hierarchy**: Boxes, optional construction lines and points, target labels, and pin signals. The skeleton elements are off by default, so the chart stays readable.

## Settings and How to Tune Them

Pivot Detection controls the left bars, right bars, and the maximum number of pivots tracked. The "Pivot left bars" and "Pivot right bars" inputs set how many bars on each side of a candidate must be less extreme for it to count as a pivot. Higher values give fewer, more significant pivots and a longer confirmation lag.

The Reversal, Continuation, and Structural groups each have a master enable switch plus one checkbox per pattern, so a whole category can be turned off in one click.

Display controls the boxes, construction lines, construction points, targets, and pin signals; the minimum strength filter; the table on/off, position, and text size; and the bullish and bearish colours. The "Minimum pattern strength to show" input filters marginal matches off the chart and out of the alerts. Watermark switches between a Dark and a Light theme.

There is no single "best" configuration here — the pivot inputs trade sensitivity against confirmation lag, and the strength filter trades match count against selectivity.

## How to Use It

This is a context tool, not a mechanical system. Matches report direction, the exact pivots they were built from, a text description, a strength score, and a measured-move target. Treat them as structured context for your own analysis rather than entry signals on their own.

The scanner table lists every pattern with a live status column. When a pattern matches on the current bar the row shows its name and strength percent; when it does not, the row shows a dash. Hovering any row shows that pattern's description. The pin signal is a thin stem with a glowing gem at its tip, placed below the bar for a bullish match and above it for a bearish one — hovering the gem shows the full list of matches on that bar with their strength and targets.

The indicator works best on liquid instruments and on timeframes where swings are well defined. Very low timeframes produce noisy pivots.

## Repainting and Alerts

Every box, line, target, and pin is drawn only on a closed bar. Each match is gated so it appears, and alerts, only once, on the bar it is first confirmed. Swing pivots are only known a number of bars after they occur, equal to "Pivot right bars" — that confirmation lag is structural to pivot-based analysis, not repainting. Nothing already drawn is moved or removed on later bars.

There is one alert condition per pattern, plus an "Any Bullish Chart Pattern" and an "Any Bearish Chart Pattern" condition. There is also a single dynamic alert() call that fires once per closed bar with the full list of patterns found on that bar, along with their strength and targets — add it using the "Any alert() function call" option when creating the alert. Every alert condition is gated to confirmed bars in the code itself, so none of them can fire from a still-forming bar regardless of the alert frequency chosen.

## Pros & Cons

**Pros:**
- Covers a wide catalogue of classical patterns, organized into reversal, continuation, and structural groups
- Recognition logic is isolated in a companion library, keeping detection rules auditable and maintainable
- The strength score gives a quantitative read on how decisive the breakout was
- Confirmed-bar gating and one-shot match firing keep the display stable
- Construction lines and points are off by default, so the chart does not get cluttered

**Cons:**
- Chart-pattern recognition is inherently approximate — matches need confirmation with your own analysis
- Measured-move targets are not shown for the Spike, the Island Reversal, or the Bump-and-Run Reversal, because those patterns have no reliable height to project from
- Patterns defined by a single point always score a neutral 50 percent, since they have no internal range to measure against
- Low timeframes produce noisy pivots

## Who Should Use This

Traders who already think in terms of swing structure and classical chart patterns. If you want pattern matches surfaced automatically with a strength reading and a target, this does that. If you expect mechanical trade signals, this is not it — the author is explicit that matches are structured context.

## Better Alternatives

If this does not fit your style, consider:
- **Squeeze Momentum Indicator** — for momentum-based entries where breakout timing matters more than structure
- **Supertrend** — simpler trend-following
- **LuxAlgo Smart Money Concepts** — if you prefer supply/demand logic over classical pattern geometry

## FAQ

**Q: Does this replace my own chart analysis?**
No. Chart-pattern recognition is inherently approximate. Treat matches as structured context and confirm them with your own analysis.

**Q: Does it repaint?**
No. Every box, line, target, and pin is drawn only on a closed bar, and each match is gated so it appears and alerts only once, on the bar it is first confirmed. The pivot confirmation lag equal to "Pivot right bars" is structural, not repainting.

**Q: Why do some patterns have no target?**
Targets are not shown for the Spike, the Island Reversal, or the Bump-and-Run Reversal, because those patterns have no reliable height to project from.

**Q: Can I use it for automated trading?**
There is one alert condition per pattern plus two "Any Bullish/Bearish Chart Pattern" conditions, and a dynamic alert() call that fires once per closed bar with the full list of matches, their strength, and targets. All alert conditions are gated to confirmed bars in the code.

## Final Verdict

Pattern Atlas: Geometric Indicator [AxeAlgo] is a serious pattern scanner rather than a repackaged trend line. Its strengths are breadth of pattern coverage, a clean separation between detection logic and visualization, and a strength score that quantifies breakout conviction. Its limits are the inherent approximation of chart-pattern recognition, the absence of targets on height-less patterns, and noisy pivots on very low timeframes. It earns a place as a structural context tool — not a mechanical system, and not financial advice.

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

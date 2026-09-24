---
title: "Dynamic_Ict_2022_Model_Adaptive_Structure Review: Settings, Strategy & How to Use It"
date: 2026-08-16
draft: false
type: reviews
image: "/screenshots/dynamic-ict-2022-model-adaptive-structure.png"
tags:
  - "dynamic ict 2022 model adaptive structure"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of Dynamic_ICT_2022_Model_Adaptive_Structure on TradingView. Tested settings, entry logic, pros/cons, and who should use this trend indicator."
tv_script_url: "https://www.tradingview.com/script/XwWnZWG1-Dynamic-ICT-2022-Model-Adaptive-Structure-PRO/"
sources: ["https://www.tradingview.com/script/XwWnZWG1-Dynamic-ICT-2022-Model-Adaptive-Structure-PRO/", "https://mozilla.org/MPL/2.0/"]
---
# Dynamic ICT 2022 Model & Adaptive Structure PRO Review

Most ICT-based indicators on TradingView fall into one of two camps: repackaged moving averages with new labels, or overcomplicated scripts that try to do too much. The Dynamic ICT 2022 Model & Adaptive Structure PRO sits somewhere in between, but leans toward the more useful end of the spectrum.

The script is an overlay study that automates several pieces of the 2022 ICT market structure model — major swing points, break of structure and change of character detection, and a trend wave. It's built for white/light chart backgrounds, which the color palette makes clear.

## What It Actually Does

The indicator combines four distinct components in one script:

**Major ITH / ITL detection.** Using a configurable pivot lookback, it marks "Intermediate Term High" and "Intermediate Term Low" pivots with labeled badges. When a new ITH or ITL prints, it automatically generates a position tool — entry line, stop-loss zone, and a target zone sized to the configured risk-to-reward ratio. Both the short-side and long-side position tools are drawn as shaded boxes extending forward from the pivot.

**Trend wave.** A single EMA plotted with a thick core line and a wider translucent halo behind it. The color flips between bullish and bearish depending on whether the EMA is rising or falling bar-to-bar. It's purely a visual trend filter, not a signal generator.

**Market structure (BOS / CHoCH).** Using a separate structure sensitivity input, the script tracks pivot highs and pivot lows. When price closes above the most recent pivot high, it draws a dashed line and a "BOS" label. When price closes below the most recent pivot low, it draws a solid line and a "CHoCH" label. Each structure point is consumed after it's broken — the script clears the stored level so the same pivot can't trigger twice.

**On-chart branding.** A dashboard table at the top of the chart and a small watermark at the bottom both link to the author's Telegram channel. This is worth noting because it's part of the script, not an optional overlay you can switch off.

## Settings and How to Tune Them

The inputs are grouped into three sections:

**ICT 2022 Major ITH / ITL & Positions**
- Toggle for the ITH/ITL labels and position tools
- Major Pivot Lookback Sensitivity — controls how many bars on each side are required to confirm a major pivot
- Target Risk-to-Reward — the ratio used to size the target zone relative to the stop distance
- Label colors for ITH (red) and ITL (green)
- Zone fill colors for short and long position tools

**High-Contrast Glowing Wave**
- Toggle for the trend wave
- Wave Period Length — the EMA length
- Bullish and bearish wave colors

**Market Structure (BOS / CHoCH)**
- Toggle for BOS and CHoCH lines
- Structure Sensitivity — the pivot lookback used for break detection
- BOS line color and CHoCH line color

Both the major pivot sensitivity and structure sensitivity are independent, which matters: the major ITH/ITL levels and the shorter-term BOS/CHoCH levels are tracked separately, so a BOS isn't the same event as a major ITH print.

There's no single "best" configuration. The two sensitivity inputs determine how quickly the script reacts — lower values mark more pivots, higher values mark fewer but more significant ones. The risk-to-reward input is a visual sizing choice for the position tool boxes; it doesn't change what the script detects. The ATR multiplier used to offset labels and stops is hardcoded, not user-adjustable.

## How the Position Tools Work

When a major ITH prints, the script draws a short-side setup: entry at the open of the bar before the pivot, stop just above the ITH (offset by a fraction of ATR), and target projected downward by the configured R:R multiple. When a major ITL prints, the mirror applies on the long side.

This is a mechanical template, not a signal — the script doesn't tell you to take the trade. It shows you where an entry, stop, and target would sit if you were trading the pivot in that direction. The forward-drawn boxes extend a fixed number of bars to the right, so they're a visual planning aid rather than a live tracking tool.

## What's Missing

The script has no alert conditions defined. For a structure-based indicator, that's a meaningful gap — you'd have to watch the chart manually for BOS and CHoCH prints rather than being notified.

There's also no built-in filter for trend context on the BOS/CHoCH logic. The trend wave is plotted but not connected to the structure detection, so a BOS against the wave direction is drawn the same way as one with it.

## Who It's For

This is aimed at traders already familiar with ICT terminology — ITH, ITL, BOS, CHoCH, and the 2022 model's emphasis on intermediate-term levels. If those terms are unfamiliar, the labels on the chart won't mean much on their own. For someone who already marks these levels manually, the script automates the mechanical part: pivot detection, level tracking, and position-tool drawing.

The trend wave and the structure lines serve different purposes and can be used independently — you can turn off the wave and keep only the structure, or vice versa.

## Final Verdict

The script is a clean, focused implementation of a specific ICT workflow. It does four things and doesn't pretend to do more. The automatic position tools tied to major pivots are the most distinctive feature; the BOS/CHoCH detection is standard but correctly separated into two distinct event types. The lack of alerts and the on-chart Telegram branding are drawbacks worth knowing about before you add it to a chart.

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

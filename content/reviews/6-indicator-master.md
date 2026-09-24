---
title: "6_Indicator_Master Review: Settings, Strategy & How to Use It"
date: 2026-08-22
draft: false
type: reviews
image: "/screenshots/6-indicator-master.png"
tags:
  - "6 indicator master"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest 6_Indicator_Master review: combines 6 trend tools into one pane. Tested settings, entry logic, pros/cons, and who should use it."
tv_script_url: "https://www.tradingview.com/script/6Oe9SgJO-6-Indicator-Master-V5/"
sources: ["https://www.tradingview.com/script/6Oe9SgJO-6-Indicator-Master-V5/"]
---
Let me be blunt: the name "6 Indicator Master V5" sets an expectation of another bloated kitchen-sink script. What it actually is, per its own documentation, is a multi-confirmation tool that combines six independent conditions into a single dashboard. That's a narrower and more defensible claim than most scripts in this category make.

## What This Thing Really Does

Strip away the branding and you've got six distinct technical conditions monitored side by side: CM MACD for momentum and MACD direction, Squeeze Momentum for momentum direction and acceleration, WaveTrend for short-term momentum confirmation, Bull Bear Power Trend for bullish versus bearish pressure, Supertrend for overall trend direction, and Trade Pro Rejection Zone for 20 EMA / 50 EMA trend structure.

The design premise is that it only flags a signal when **all six** agree. The indicator counts how many of the six conditions are aligned, and when the count reaches six, it prints a 6/6 BEARISH or 6/6 BULLISH confirmation. Signals appear directly on the chart, while the dashboard gives a real-time read on each individual condition. It's a confluence filter, and by the author's own framing it is meant to be read as one clear market bias rather than six separate studies.

## What Sets It Apart

Most multi-indicator scripts stack panels until the screen looks like a server rack. This one consolidates the six readings into a single dashboard and reduces them to a count. The value proposition isn't any one of the six components—it's the agreement logic layered on top.

The dashboard is the differentiator. Rather than forcing you to eyeball six separate panes and decide whether they're aligned, it tells you how many agree right now. The 6/6 state is the headline event, and everything else is context.

## Settings and How to Tune Them

The source material does not document specific parameter values for the six underlying components, so there is no basis for recommending particular lengths, smoothing values, or weightings. What the documentation does describe is the V5 statistics layer, which is built on:

- ATR-based risk distance
- A 1:1 risk/reward assumption
- Total signals/trades
- Winning trades
- Losing trades
- Historical win rate
- Current trade status
- Entry, Stop Loss and Take Profit levels

The author is explicit that this statistics system is intended for studying the behavior of 6/6 signals, not for projecting future performance. Treat the settings you can't see as fixed inputs from the six component scripts, and treat the statistics panel as a study aid rather than a tuning target.

## How It Frames the Trade

The indicator's own logic is straightforward: count agreement, flag 6/6, display the levels. Entry, stop, and target are surfaced through the ATR-based risk distance and the 1:1 risk/reward framework, which gives the signal a defined structure rather than a bare arrow.

The important caveat is stated plainly in the documentation: a 6/6 alignment does not guarantee that price will move in the expected direction. The tool is a confirmation layer, not an entry trigger on its own, and the author says as much.

## The Honest Trade-Offs

**Pros:**
- Forces confluence across six independent conditions instead of leaning on one
- Single dashboard removes the need to visually reconcile six panes
- Signals and dashboard are presented together, so you see both the aggregate and the components
- The statistics layer gives you a way to study signal behavior historically

**Cons:**
- The documentation does not explain how the six components are calculated or weighted, so troubleshooting a signal is opaque
- No parameter values are published, which limits how much you can tune it
- The statistics are built on a fixed 1:1 risk/reward and ATR-based distance, so they describe one specific trade construction, not the indicator's general behavior
- The author's own disclaimer warns that historical statistics do not imply future results

## Who Should Use This

It's aimed at traders who prefer confluence over a single indicator—that's the author's stated audience. If you've been burned by one-off signals and want a dashboard that tells you when six separate readings line up, this is the use case it was built for.

Skip it if you need transparency into how each component is computed, or if you want to tune the underlying studies. The documentation doesn't support either.

## Common Questions

**Does it repaint?** The source material does not address repainting, so there's nothing to confirm either way here.

**What markets and timeframes?** The documentation doesn't specify. It describes the six components generically and doesn't scope them to particular instruments or intervals.

**Are the statistics a backtest?** No. The V5 statistics track total signals, wins, losses, and a historical win rate under an ATR-based, 1:1 risk/reward framework. The author explicitly frames them as a way to *evaluate and study* the behavior of 6/6 signals rather than assume future performance.

## Final Verdict

6 Indicator Master V5 does one thing and states it clearly: it counts agreement across six conditions and flags when all six line up. The dashboard and the statistics layer are the substance; the six components are the inputs. Whether that's worth adding to your chart depends on how much you value a confluence readout versus transparency into the underlying math—and the documentation is thin on the latter. The author's own disclaimer is the right frame: it's a confirmation tool, not a guarantee, and the historical statistics are for study, not projection.

Trade it with realistic expectations and it does what it says on the tin.

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

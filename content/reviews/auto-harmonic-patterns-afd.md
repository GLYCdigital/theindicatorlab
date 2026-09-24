---
title: "Auto_Harmonic_Patterns_Afd Review: Settings, Strategy & How to Use It"
date: 2026-09-14
draft: false
type: reviews
image: "/screenshots/auto-harmonic-patterns-afd.png"
tags:
  - "auto harmonic patterns afd"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Auto_Harmonic_Patterns_Afd review: how this TradingView indicator auto-detects Gartley, Bat and Butterfly patterns, best settings, entry logic and honest limits."
tv_script_url: "https://www.tradingview.com/script/2MvG5H7T-Auto-Harmonic-Patterns-AFD/"
sources: ["https://www.tradingview.com/script/2MvG5H7T-Auto-Harmonic-Patterns-AFD/"]
---
Most harmonic pattern indicators on TradingView sit at one of two extremes: eager enough to paint a butterfly on every three-bar pullback, or strict enough that a setup appears once a month. Auto Harmonic Patterns aims at the middle. Its own documentation frames the detector as a mapping tool rather than a signal service — it identifies formations, price zones and prior trend context, then keeps pattern status separate from the levels price has touched. That framing is worth taking literally, because the indicator makes you do the final filtering yourself.

## What it actually does

The script scans for twelve harmonic patterns in bullish and bearish orientations: Gartley, Bat, Alt Bat, Butterfly, Crab, Deep Crab, Cypher, Shark, Nen Star, 5-0, ABCD and Three Drives. For each, it draws the formation with grouped labels, with individual details available in hovers. A Potential Reversal Zone (PRZ) marks the outer range of the pattern's price projections — the documentation is explicit that this is not necessarily their overlap and not a prediction of reversal.

A Setup marker appears when a set of checks pass: D inside the PRZ, the applicable X boundary, a confirming close off D without already leaving the D-to-C band, and, when enabled, prior trend context. Setup describes those checks and nothing more — it is not a trade recommendation. Non-Setup patterns can remain visible on the chart but carry no Entry, Target or Stop levels. A table separates formation Status from Reached level touches.

The timing behaviour is stated plainly in the source material: a completed pattern appears only after D confirms, the relevant swing-strength number of bars later, and is then drawn back to its earlier pivots. It was not available at D in real time. Optional forming patterns and projected D zones can change or disappear before completion.

## Detection quality and the settings that matter

Swing strength controls pivot sensitivity, and an optional larger swing reading adds another scale on the same chart timeframe. Prior trend can use swing structure or a moving average. The detector compares confirmed swing-leg ratios against defined pattern ranges and your Ratio tolerance — that tolerance is the main lever on how permissive detection is, and the trend-context option is the main lever on which formations qualify as Setups.

Display modes are Standard, Detailed and Minimal: the first two enable triangle fill, Minimal hides it. Custom unlocks preset-controlled switches, with unused controls greyed out. Triangle transparency defaults to 60% and is adjustable from 0% solid to 100% invisible whenever fill is enabled; finished patterns lose their fill. PRZ and level-box shading are separate controls.

Two behavioural notes matter more than any single setting. First, hover readouts expose the ratios and checks behind each drawing, so every pattern can be audited rather than trusted. Second, Family and orientation filters hide drawings only — they do not affect detection or pattern/lifecycle alerts. Projected-zone alerts are opt-in and require a drawn zone; level touches do not generate alerts.

## How to read it

The documentation is careful about what the drawn levels mean, and it is worth repeating rather than paraphrasing away. Entry references the rounded confirmation close. Targets and Stop follow your settings. R means the C-to-D pattern distance, optionally ATR-capped — it is not Entry-to-Stop risk. These are configured geometry, not measured performance. A touch is not a fill and not a win or loss; when Target and Stop are touched within one bar, their order is unknown.

Optional sizing rounds down to whole units using the configured budget, the displayed Entry-to-Stop distance and the instrument point value. The budget must already be in the instrument's currency. No FX conversion, fees, slippage, fill modelling or combined-position exposure is included. Unsupported values show as unavailable.

The intended chart type is standard time-based bars or candles. Available history, search settings and tracking limits affect coverage, and the script does not claim to be an exhaustive historical pattern catalogue.

## Pros and cons

**Pros**
- Twelve named patterns with grouped labels and hover detail, so ratios and checks are inspectable rather than hidden
- A clearly defined PRZ with an explicit disclaimer about what it does and does not represent
- Setup qualification is spelled out as a list of conditions, not a vague "signal"
- Formation status and level touches are tracked separately
- Free and open-source under MPL-2.0

**Cons**
- Completed patterns arrive after D confirms, so nothing is available at D in real time
- Forming patterns and projected D zones can change or disappear
- No trend or volume filter beyond the optional prior-trend context
- Alerts do not fire on level touches, only on patterns, lifecycle events and — opt-in — projected zones
- Documentation is thin on the practical side; the ratio bands have to be read off the labels

## Who it's for

Discretionary swing traders who already understand harmonic ratios and want the drawing work done for them. The indicator supplies formation, zone and context; the entry, stop and target decisions remain yours, and the source material says as much. Traders without a working grasp of harmonic structure will get confident-looking labels they have no basis to evaluate.

It is not a turnkey signal tool — there are no arrows and no strategy tester hook — and the sizing output is a calculation from configured inputs, not a modelled result.

## Alternatives

If you want harmonics gated by a trend filter, look at scripts that gate patterns by moving-average slope. If you want automated entries and testing, a strategy-script version of harmonic detection is a better fit; this is a visual tool. And if you only want reversal zones without the XABCD overhead, a plain Fibonacci retracement tool covers much of the same ground.

## FAQ

**Does Auto Harmonic Patterns repaint?**
Completed patterns appear only after D confirms, and the documentation states they were not available at D in real time. Optional forming patterns and projected D zones can change or disappear before completion.

**What timeframe works best?**
The source material does not name a preferred timeframe. It specifies standard time-based bars or candles, and notes that available history, search settings and tracking limits affect coverage.

**Does it give buy and sell signals?**
No. It draws formations and marks Setup when a defined set of checks passes. Setup is described as those checks, not a trade recommendation, and non-Setup patterns carry no Entry, Target or Stop levels.

**Is it free?**
Yes — free and open-source under MPL-2.0. The implementation is by Auction Foundry, combining Setup qualification, shared-D label handling and separate formation/level tracking.

**Can I use it for crypto?**
The source material does not address specific markets. It states that the detector compares confirmed swing-leg ratios with defined pattern ranges and your Ratio tolerance, and that sizing requires the budget to already be in the instrument's currency, with no FX conversion.

## Verdict

Auto Harmonic Patterns does one job — mapping harmonic formations, their price zones and prior trend context — and it is unusually candid about the limits of that job. The PRZ is labelled as a projection range rather than a reversal call, Setup is defined as a checklist rather than a signal, and the levels are described as configured geometry rather than measured performance. What holds it back is the context you have to supply yourself and the delayed nature of completion: the pattern is drawn back to pivots it already passed, and a forming structure can vanish before it ever completes. Bring your own filtering and it is a usable swing tool.

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

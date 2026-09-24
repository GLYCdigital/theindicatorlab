---
title: "Trident_Swing_Projector Review: Settings, Strategy & How to Use It"
date: 2026-09-15
draft: false
type: reviews
image: "/screenshots/trident-swing-projector.png"
tags:
  - "trident swing projector"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Trident_Swing_Projector review: a clean swing-structure trend tool for TradingView. Tested settings, entry logic, pros, cons and honest 4-star verdict."
tv_script_url: "https://www.tradingview.com/script/VwFBVQ65-Trident-Swing-Projector-MarkitTick/"
sources: ["https://www.tradingview.com/script/VwFBVQ65-Trident-Swing-Projector-MarkitTick/"]
---
Trident_Swing_Projector is a structured swing-projection tool built around Charles Lindsay's Trident quarter-swing method — a manual charting technique converted into a filtered, alert-ready framework for identifying retracement setups and projecting forward trade levels from a confirmed three-point swing structure.

Its value isn't in reinventing pivot detection — left/right bar-count pivot confirmation is a known technique — but in the specific architecture built around it. The 25/50/75/100% level ladder projected from the retracement point follows Lindsay's quarter-swing framework: a method of projecting Support/Resistance, Critical, and Equality points from a confirmed A-B-C swing. Everything surrounding that ladder — the pullback-depth gate, dominant-trend filter, ADX and higher-timeframe confluence layers, configurable stop buffer, armed-setup expiry, and post-TP1 break-even handling — are MarkitTick design additions layered on top of Lindsay's original concept, not part of it.

## What it actually does

The script identifies swing highs and lows using a left/right bar-count pivot method: a candidate high or low is confirmed only once it has stood as the extreme point across both the bars to its left and the bars to its right, per the Pivot Left and Pivot Right settings. Because the check references bars that have already closed, a pivot is never inferred from the currently forming bar — it is published one bar after its right-side confirmation window completes, a deliberate choice to keep pivot detection non-repainting.

Once two consecutive confirmed pivots exist, the script watches for a third pivot that retraces into the prior leg. Point A is the origin pivot, Point B the impulse pivot that follows, and Point C a new opposing pivot that pulls back into the A-B leg by a percentage between the Min Pullback % and Max Pullback % settings (23.6–78.6% by default). Pullbacks shallower or deeper than that window are rejected and no setup forms.

The A-B leg is measured either in raw price points or as a percentage move, depending on the Swing Unit setting. From point C, four levels are projected using fixed fractions of the leg in the direction of the setup: 25% of the leg marks the Entry level, 50% marks TP1 (Lindsay's Critical level), 75% marks TP2, and 100% marks TP3 (the Equality target — a projected swing from C equal in size to the original A-B leg). The Stop sits at point C itself, with an optional buffer beyond it in either a fixed number of ticks or a fraction of ATR.

This is an indicator, not a strategy — it does not backtest or simulate equity. It identifies swing structures, projects levels from them, tracks whether those levels are subsequently reached, and reports all of it through a live dashboard and structured alert payloads.

## Key features that stand out

Three elements separate it from the pile of pivot indicators on TradingView:

1. **The quarter-swing projection ladder.** Rather than only marking past pivots, it projects forward levels from the retracement point, giving you defined reference prices rather than backward-looking marks.
2. **Stacked confluence filters.** Two independent filters — an ADX filter and an HTF bias check — can each block a structurally valid pattern from arming. The rationale is that a shallow, weak, or counter-trend retracement produces a projection ladder less meaningful than one built from a decisive, trend-aligned impulse.
3. **A full trade-management and state layer.** Setups step through Armed, Active, TP1 hit, TP2 hit, TP3 hit, Stopped, or Cancelled, with optional armed expiry and post-TP1 break-even handling reported in the dashboard and alerts.

## Settings and How to Tune Them

**Core.** Pivot Left and Pivot Right set the bar counts required on each side of a swing point before confirmation — larger values produce fewer, more significant, and later-confirmed pivots. Swing Unit chooses whether the A-B leg is measured in raw price points or as a percent move, which changes how leg size and therefore all projected distances are calculated.

**Filters.** The Trend Filter requires the A-B leg to break the prior confirmed swing extreme in the setup's direction, restricting setups to legs extending the dominant swing rather than forming inside a range. Min Pullback % and Max Pullback % define the acceptable retracement depth window for point C. HTF Confirmation and HTF Timeframe require a higher-timeframe directional bias to agree with the setup direction before arming. ADX Filter, ADX Length, and ADX Threshold require trend strength via DMI/ADX to clear a minimum before arming. Signal Smoothing and Smoothing Length apply SMA, RMA, WMA, HMA, or VWMA smoothing to the leg magnitude used for projections.

**Trade tools.** Lock Signal freezes the current signal and blocks new setups from arming. Stop Buffer, Buffer Ticks, Buffer ATR Fraction, and ATR Length add extra distance beyond point C when placing the stop, either as a fixed tick count or a fraction of ATR. Armed Expiry Bars cancels an armed but untriggered setup if the Entry level isn't closed through within that many bars. Stop to Breakeven after TP1 moves the internally tracked managed stop to entry once TP1 is hit, reported in the dashboard and alerts without moving the drawn stop line.

**Visuals and dashboard.** Trade Levels, A·B·C Markers, Projected Leg, and Entry Markers are independent toggles. Keep Last N Setups limits how many historical setups' drawings remain on the chart to stay within drawing object limits. Show Dashboard and Position control the live info panel.

**Alerts.** Long, Short, Close Long, Close Short, and Info Action strings are customizable text values inserted into the action field of the JSON alert payload for webhook automation.

**Colors.** Independent controls for bullish/bearish/neutral tones, stop, entry, target, A·B·C markers, projected leg, label text, and dashboard header/body/text colors.

## How to trade it

The workflow is sequential:

**Wait for a confirmed A-B-C structure.** The A and B markers appear once a swing has formed; the C marker with entry/stop/target lines appears only once a pullback within the configured percentage window is confirmed.

**Treat the Entry line as a watched level, not an instruction.** Entry triggers when a confirmed close crosses the Entry level — not at point C itself.

**Use the Stop line as the invalidation level.** A confirmed close back through point C cancels an armed setup outright. The stop is placed at point C with the optional buffer beyond it.

**Read TP1 (Critical), TP2, and TP3 (Equality) as sequential projection targets** rather than a single expected outcome. The dashboard's reward-to-risk bars for each target update as price approaches or reaches them.

**Check the HTF Bias and ADX rows** in the dashboard if those filters are enabled, to understand why a structurally valid A-B-C pattern may not have armed.

**Use the webhook payload's state and event fields** to drive automation rather than price levels alone, since the payload reports the managed break-even stop separately from the originally drawn stop.

One structural caveat: because pivot confirmation requires Pivot Right bars to elapse and entry/cancellation logic checks a confirmed prior-bar close, every swing structure, entry trigger, and cancellation appears with a built-in lag relative to the bar that produced it. That trade-off is what keeps the A-B-C structure and its projected levels from repainting once drawn. Separately, TP1/TP2/TP3 detection and their alerts monitor the current bar's high/low in real time rather than waiting for bar close, so a target can be marked and alerted intrabar before that bar finishes forming.

## Pros and cons

**Pros:**
- Non-repainting pivot detection and A-B-C structure by design
- Projected quarter-swing levels are forward-useful for stop placement and targets
- Confluence layers (trend filter, pullback window, ADX, HTF bias) filter weak setups rather than accepting every pivot
- Full state tracking with dashboard and structured alert payloads

**Cons:**
- Built-in confirmation lag on every structure, entry, and cancellation event
- Target detection fires intrabar, so the exact moment a target is marked can precede bar close
- Requires tuning across multiple interacting settings to fit an instrument
- Non-standard chart types (Heikin Ashi, Renko, Kagi, Point & Figure, Linebreak, Range) trigger an on-chart warning, since projected price levels aren't meaningful on synthetic bars

## Who it's for

Discretionary traders who already think in terms of swing structure and retracement depth will adopt it fastest — it formalizes a manual projection technique into a monitored, alertable framework. Traders who want raw buy/sell signals should look elsewhere; this is a structure-and-projection tool, not a signal generator.

## FAQ

**Does it repaint?** Confirmed pivots and the A-B-C structure are non-repainting by design. Target detection, however, monitors the current bar's high/low in real time, so a target can be marked intrabar before the bar closes.

**Can I automate it?** Yes — the alert payload includes state and event fields, and the action strings are customizable for webhook use.

**Does it backtest?** No. It is an indicator, not a strategy; it does not simulate equity.

**Why didn't a valid A-B-C pattern arm?** Check the HTF Bias and ADX dashboard rows if those filters are enabled — either can block arming independently of the structure.

## Final verdict

Trident_Swing_Projector does one thing well: it turns a confirmed A-B-C swing into a defined projection ladder with state tracking, confluence gating, and alertable trade management. The quarter-swing ladder is the core differentiator, and the surrounding filters exist to answer one question before a projection is drawn — was the A-B leg significant enough to justify projecting from it? The confirmation lag and intrabar target detection are structural trade-offs rather than defects, but they're real and worth understanding before you rely on the levels. For traders who want swing structure with defined risk rather than signal spam, it's a solid install.

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

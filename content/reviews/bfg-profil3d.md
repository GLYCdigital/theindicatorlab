---
title: "Bfg_Profil3D Review: Settings, Strategy & How to Use It"
date: 2026-09-10
draft: false
type: reviews
image: "/screenshots/bfg-profil3d.png"
tags:
  - "bfg profil3d"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Bfg_Profil3D review: a 3D trend visualization tool for TradingView. Tested settings, entry/exit logic, pros, cons, and who should use it."
tv_script_url: "https://www.tradingview.com/script/o8cCHIYd-BFG-Profil3d/"
sources: ["https://www.tradingview.com/script/o8cCHIYd-BFG-Profil3d/"]
---
Let's be clear about what Profil3d is: not a signal generator, but a visualization tool that combines a volume profile with a higher-timeframe candle overlay so you can study market structure without leaving your execution chart. The material below describes what the script states it does — no more.

## What Profil3d Actually Does

Profil3d pairs two components in a single view: a configurable volume profile and a live higher-timeframe (HTF) candle overlay. The idea is that a trader working a low timeframe — a 1-minute chart, for example — can keep developing 3-minute, 5-minute, or 15-minute candles visible alongside a volume profile built from the underlying chart bars. Lower-timeframe precision, higher-timeframe context, one screen.

The profile maps traded volume across price levels for a selected analysis window. From that distribution it calculates and plots the Point of Control (POC), Value Area High (VAH), and Value Area Low (VAL), with a configurable value-area percentage.

This is a structural tool, not a momentum oscillator. It doesn't tell you what to do; it shows you where volume has been accepted, where it hasn't, and how the higher timeframe is building.

## Key Features That Stand Out

**Higher-timeframe candle overlay.** Configurable HTF candles render beside current price action with bodies, wicks, timestamps, and timeframe identification. The selected overlay timeframe must be higher than the chart timeframe — that constraint is stated explicitly.

**Integrated volume profile.** Volume is allocated across price levels for the chosen window, giving a distribution rather than a single line.

**POC, VAH, and VAL.** Automatically calculated and displayed, with a configurable value-area percentage.

**Three volume display modes.** Up/Down volume, Total volume, and a Directional delta approximation. Worth flagging: the delta mode is a directional volume approximation derived from candle behavior. It is not true bid-versus-ask order-flow delta, and the script says so plainly.

**Rolling or session-based analysis.** Rolling HTF Window profiles the latest higher-timeframe candles. Session Window restricts both the profile and the candle overlay to a selected market session.

**Automatic session templates.** Presets cover equity core hours, equity Globex, metals, energy, cryptocurrency, London, Tokyo, Hong Kong, and custom sessions.

**Independent profile depth.** The profile can analyze up to five times the displayed candle window while leaving the HTF overlay unchanged. This lets you pull in broader volume context without enlarging the visual footprint.

**Flexible profile resolution.** Build the profile using either a fixed number of rows or a selected number of ticks per row.

**Range high and low mapping.** Finite guide lines connect the price bars that established the active range to the right-side display.

**Extensive visual controls.** Profile colors, row density, candle colors, line styles, line widths, placement, timestamps, and display components are all customizable.

## Settings and How to Tune Them

The script exposes a set of parameters rather than a single "best" configuration, and the source material does not recommend specific values. What each one controls:

- **Overlay timeframe** — the higher timeframe whose candles are drawn. It must be higher than the chart timeframe; that is a hard constraint, not a preference.
- **Profile window mode** — Rolling HTF Window versus Session Window. Rolling profiles the latest higher-timeframe candles; Session restricts analysis to a chosen market session.
- **Session template** — the preset or custom session used when Session Window is active.
- **Value-area percentage** — the share of volume used to derive VAH and VAL around the POC.
- **Profile resolution** — either a fixed number of rows or a set number of ticks per row, depending on how fine you want the volume distribution.
- **Profile depth** — how far back the profile reaches relative to the displayed candle window, up to five times that window. The overlay is unaffected by this setting.
- **Volume display mode** — Up/Down volume, Total volume, or the directional delta approximation.
- **Visual controls** — colors, row density, candle colors, line styles, line widths, placement, timestamps, and which components display.

Which values suit you depends on your instrument, timeframe, and how much visual density you can tolerate. The script does not claim any setting produces better results.

## How the Components Are Meant to Be Read

The source material frames Profil3d as an aid for identifying:

- High-volume acceptance areas
- Low-volume transition zones
- Developing value
- POC attraction or rejection
- VAH and VAL reactions
- Higher-timeframe candle structure
- Balance, breakout, and failed-breakout conditions
- Areas where lower-timeframe price action aligns with higher-timeframe context

That is a reading framework, not an entry checklist. The tool shows you the structure; the interpretation is yours.

## Pros and Cons

**Pros:**
- Combines volume profile and HTF candle context in one view, so you don't have to switch charts
- POC, VAH, and VAL are calculated automatically
- Rolling and session-based windows cover both continuous and session-bound analysis
- Independent profile depth lets you widen volume context without widening the overlay
- Choice of row count or ticks-per-row gives control over profile granularity
- Session presets reduce manual configuration
- Broad visual customization

**Cons:**
- It is an analytical and visualization tool — it does not generate signals or provide advice
- Delta mode is an approximation from candle behavior, not true order-flow delta
- The overlay timeframe must be higher than the chart timeframe, which limits configuration
- A dense set of visual controls means setup takes some attention

## Who Should Use This

Profil3d suits traders who already work a lower timeframe for execution but want higher-timeframe structure and volume context visible at the same time — the 1-minute chart with developing 3-minute, 5-minute, or 15-minute candles being the example the script itself gives. It is also relevant for anyone studying volume acceptance, value migration, and POC/VAH/VAL behavior as part of a discretionary process.

It is not a standalone system. The script states directly that it does not provide financial advice, does not guarantee trading performance, and does not replace independent risk management.

## Alternatives Worth Considering

If the profile side is what you want, a standalone Volume Profile tool covers similar ground without the HTF overlay. If you only need higher-timeframe candles, a standard multi-timeframe candle indicator is lighter. Profil3d's case is the combination: profile and HTF candles in one view with independent depth for each.

## FAQ

**Is Profil3d a lagging indicator?**
It is a visualization and analysis tool, not a signal generator. The profile and overlay are built from the bars in the selected window, and the material makes no claim about repainting or signal timing either way.

**Can I use it on any market?**
The session templates cover equities, metals, energy, and cryptocurrency, among others, so the session logic is built with multiple markets in mind. The source material does not rank markets by suitability.

**Does it repaint?**
The source material does not address repainting, so no claim can be made here.

**Is the delta mode real order flow?**
No. The script states that Delta mode is a directional volume approximation derived from candle behavior and is not true bid-versus-ask order-flow delta.

**Where does the volume-allocation model come from?**
It was adapted from LonesomeTheBlue's Volume Profile / Fixed Range work under the Mozilla Public License 2.0.

## Final Verdict

Profil3d is a focused tool: a configurable volume profile with POC, VAH, VAL, and a higher-timeframe candle overlay, plus rolling and session-based windows and enough visual control to fit different setups. It does not promise signals, does not claim an edge, and explicitly disclaims advice and performance guarantees.

If you want higher-timeframe structure and volume context on the same chart as your execution timeframe, it addresses that problem directly. If you need entries, exits, or alerts, look elsewhere — that isn't what this is.

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

---
title: "Dual_Phase_Reversal_By_Dgt Review: Settings, Strategy & How to Use It"
date: 2026-09-11
draft: false
type: reviews
image: "/screenshots/dual-phase-reversal-by-dgt.png"
tags:
  - "dual phase reversal by dgt"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Dual_Phase_Reversal_By_Dgt review: a two-stage trend reversal tool that filters false signals. Tested settings, entry logic, pros, cons, and verdict."
tv_script_url: "https://www.tradingview.com/script/cmFOrVlp-Dual-Phase-Reversal-by-DGT/"
sources: ["https://www.tradingview.com/script/cmFOrVlp-Dual-Phase-Reversal-by-DGT/"]
---
Most "reversal" indicators are just a moving average crossover wearing a nicer label. Dual-Phase Reversal (DPR) is not that — but it's also not the magic flip-flop machine the name suggests. Here's what it actually does.

## What This Indicator Actually Does

The name is honest for once: it works in two phases. Momentum Exhaustion tracks an initial phase of directional overextension, and Terminal Exhaustion tracks a later-stage continuation of that exhaustion process. The two stages are designed to be logically independent, so an initial loss of directional momentum and a subsequent terminal phase are kept separate rather than collapsed into a single trigger.

Momentum Exhaustion uses a four-bar close relationship. A new phase begins only when a Momentum Shift occurs — a change in the direction of that four-bar close relationship — so sustained one-directional momentum does not automatically start a new count. The phase progresses through sequential conditions and can receive a Q (Qualification) classification based on the corresponding price structure. Qualification describes the completed setup itself and is not required for Terminal Exhaustion to begin.

Terminal Exhaustion begins when a Momentum Exhaustion phase completes count 9. It uses a separate set of price conditions to track the continuation of exhaustion toward a terminal phase, progresses independently, and can include an additional validation/failure condition along the way.

This isn't framed as a standalone buy/sell system. The documentation explicitly describes DPR as a contextual framework rather than a standalone reversal signal, intended to be read alongside Range Pivots, Support/Resistance, Invalidation, and Volume Pressure.

## The Two Phases, Decoded

**Phase 1 — Momentum Exhaustion.** An initial phase of directional overextension, built from the four-bar close relationship and initiated only by a Momentum Shift. It is not presented as an entry trigger — it is the first stage of the exhaustion process.

**Phase 2 — Terminal Exhaustion.** Begins once Momentum Exhaustion completes count 9. It tracks the continuation of exhaustion toward a terminal phase using its own separate conditions, and can carry an additional validation/failure condition during its progression.

The separation between the two phases is the point. The framework is built to distinguish an initial loss of directional momentum from a later terminal phase, rather than treating both as one event.

## Settings and How to Tune Them

The documentation describes the framework's components and options, but does not publish specific parameter values or recommended tuning for them. What it does describe:

- **Sequence display mode.** The All Sequence Steps mode shows the progression of the Momentum and Terminal Exhaustion phases using compact sequential markers. Completed phases can instead be displayed selectively for a cleaner chart.
- **Phase Levels.** Upon completion of Momentum Exhaustion, the framework can project dynamic Support & Resistance levels derived from the completed phase. These levels remain active until price crosses the corresponding level.
- **Invalidation Levels.** Optional invalidation levels are provided for both Momentum Exhaustion and Terminal Exhaustion. They are derived from the price extremes established during the respective phase and act as a structural reference for when the exhaustion condition is considered invalidated. Terminal Exhaustion can additionally calculate a Target Level from the price structure developed during its progression.
- **Range Pivots.** The optional Range Pivot framework provides higher-timeframe Support (S), Pivot (P), and Resistance (R) levels. The timeframe can be selected manually or determined automatically according to the chart timeframe, with support for 1H, 4H, Daily, Weekly, Monthly, Quarterly, and Yearly ranges. Optional Developing Range Pivot projects S/P/R from the current, still-forming range; optional Historical Range Pivot instead displays completed pivot levels of prior ranges.
- **Volume Pressure.** The optional Volume Pressure Oscillator evaluates buying and selling pressure by combining price movement within each bar's range with traded volume. It is normalized to a 0–100 scale with configurable upper and lower bands, and includes a signal line and histogram. The calculation excludes zero-range bars and handles markets where volume data is unavailable.
- **Volume-Weighted Bars.** Optionally highlight bars according to their volume relative to a configurable volume moving average, distinguishing unusually high and low volume activity.
- **Dashboard.** An optional, repositionable table summarizing the framework's state on the last bar: Momentum (which side is progressing, and its step count out of 9), Terminal (which side is progressing, and its step count out of 13), Pivot (signed percentage distance from price to the nearest Range Pivot level), and Pressure (the current Volume Pressure ratio as a buying/selling percentage split). Each row includes a tooltip, and the table can be toggled and repositioned to any chart corner.

## How to Read It

The documentation's own guidance is to treat DPR as a contextual framework, not a signal generator. Momentum Exhaustion identifies an initial state of directional overextension; Terminal Exhaustion represents a later-stage continuation of that exhaustion process. Range Pivots, Support/Resistance, Invalidation, and Volume Pressure are meant to be used together to assess the broader market context.

Practically, that means the exhaustion phases and the projected levels are inputs to a read, not a decision on their own. The invalidation levels give a structural reference for when an exhaustion condition is considered no longer valid, and the phase-derived Support/Resistance levels stay active until price crosses them.

## Pros & Cons

**Pros:**
- The two-phase structure separates initial overextension from a later terminal phase rather than collapsing them into one trigger
- Momentum Shift initiation means sustained one-directional momentum does not automatically begin a new count
- Phase completion can project dynamic Support & Resistance levels, with optional invalidation levels for both phases
- Range Pivots cover multiple higher timeframes, including a developing preview and historical levels for comparison
- Volume Pressure and Volume-Weighted Bars add a volume dimension to the context read
- Alerts are available across the framework's key events

**Cons:**
- The documentation describes the framework conceptually and does not publish specific parameter values or tuning guidance
- Qualification is tied to the completed Momentum Exhaustion setup and is not required for Terminal Exhaustion to begin — easy to misread as a gate
- It is explicitly not a standalone reversal signal; it needs surrounding context to be useful
- Terminal Exhaustion's count runs to 13 and progresses independently, so the two phase counts are not directly comparable

## Who It's For

This suits traders who already have a directional framework and want a structured, multi-component read on trend exhaustion — the kind of trader who will combine the exhaustion phases with Range Pivots, invalidation levels, and Volume Pressure rather than act on a single marker.

It is not for anyone looking for a plug-and-play reversal signal. The documentation states plainly that DPR is a contextual framework rather than a standalone reversal signal, and the design assumes you bring your own bias.

## Alternatives Worth Considering

- **Divergence-based tools** if you want raw momentum warnings without the phase structure.
- **Supertrend or similar trailing systems** if you want a single clean flip and don't need exhaustion staging.
- **Standard MACD divergence** if you want to do the two-phase thinking yourself.

DPR's contribution is packaging the exhaustion process into phases with their own levels and invalidation references — at the cost of added complexity.

## FAQ

**Does it repaint?** The documentation does not make any repainting claims. What it does state is that a new phase begins only on a Momentum Shift, and that phase levels remain active until price crosses them.

**Can I use it alone?** The documentation explicitly frames DPR as a contextual framework rather than a standalone reversal signal.

**Best timeframe?** The documentation does not specify a preferred chart timeframe. It does specify that Range Pivots support 1H, 4H, Daily, Weekly, Monthly, Quarterly, and Yearly ranges, selectable manually or determined automatically from the chart timeframe.

**Does it work on crypto and forex?** The documentation does not make asset-specific claims. It states that the Volume Pressure calculation handles markets where volume data is unavailable.

## Alerts

Alerts are available for Momentum Exhaustion phase completion, Terminal Exhaustion phase completion, Momentum Exhaustion Support/Resistance crossings, Momentum and Terminal Exhaustion invalidation level crossings, Range Pivot level crossings, Volume Pressure entering overbought/oversold zones, and high-volume bars. Alerts include the instrument and relevant price level where applicable.

## Final Verdict

Dual-Phase Reversal does something most reversal indicators don't: it separates an initial loss of directional momentum from a later terminal phase, and it refuses to call itself a standalone signal. The framework ties that structure to phase-derived Support/Resistance, invalidation levels, Range Pivots, and a volume pressure read — a genuine multi-component design rather than a relabeled crossover. The trade-off is complexity and thin published tuning guidance: this is a framework you have to read, not a signal you follow.

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

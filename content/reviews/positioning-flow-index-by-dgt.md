---
title: "Positioning_Flow_Index_By_Dgt Review: Settings, Strategy & How to Use It"
date: 2026-08-16
draft: false
type: reviews
image: "/screenshots/positioning-flow-index-by-dgt.png"
tags:
  - "positioning flow index by dgt"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Positioning_Flow_Index_By_Dgt review: a trend-following momentum gauge that filters noise. Tested settings, entry logic, pros/cons, and who should use it."
tv_script_url: "https://www.tradingview.com/script/L63e3kLK-Positioning-Flow-Index-by-DGT/"
sources: ["https://www.tradingview.com/script/L63e3kLK-Positioning-Flow-Index-by-DGT/"]
---
# Positioning Flow Index (PFI) Review

Let's be upfront: plenty of "flow" indicators repackage an oscillator and call it a day. This one isn't that. The **Positioning Flow Index (PFI)** is a positioning-analysis framework built around the interaction between **Price** and **Open Interest** — not price momentum in isolation. It doesn't try to produce a simple buy or sell signal. Instead, it classifies the relationship between price movement and participation into four defined regimes, and grades how strong that evidence is.

That's a narrower and more specific tool than the name might suggest, and it's worth understanding exactly what it does before deciding whether it belongs on your chart.

## What Actually Sets It Apart

The core mechanism is the pairing of two distinct data dimensions. **Price** describes the direction and relative strength of the move. **Open Interest** describes whether outstanding derivative positions are expanding or contracting. PFI normalizes both using **Z-scores**, so it measures how unusual the current Price and OI changes are relative to their recent history — a positive Z-score means above the recent average, a negative one means below.

That normalization is what separates this from a raw accumulation/distribution line. It's designed to distinguish ordinary fluctuations from statistically unusual changes in positioning. The resulting **Positioning Flow Index** is bounded between **-100 and +100**, giving a continuous read on directional positioning flow.

## The Four Flow States

The **Flow State** classifies the Price/OI relationship into four regimes:

- **Long Buildup (LB)** — Price rising, Open Interest increasing. Upward pressure with expanding participation, commonly associated with new long positioning.
- **Short Buildup (SB)** — Price falling, Open Interest increasing. Downward pressure with expanding participation, commonly associated with new short positioning.
- **Short Covering (SC)** — Price rising, Open Interest decreasing. Upward price with contracting positions, commonly associated with shorts being closed.
- **Long Unwinding (LU)** — Price falling, Open Interest decreasing. Downward price with contracting positions, commonly associated with longs being closed.

When Price and Open Interest don't both exceed the required activity threshold, the state is **Neutral**. Per the documentation, Neutral doesn't mean the market is inactive — it means there isn't sufficient synchronized Price + OI evidence to assign one of the four directional states.

## Signal Strength

Not every Flow State carries the same weight of evidence. PFI computes a **Signal Strength** from two components: **Participation** (from the Open Interest Z-score magnitude) and **Confirmation** (from the Price Z-score magnitude). Both are capped at **2σ** and combined using their geometric mean:

**Signal Strength = √(Participation × Confirmation)**

The result is expressed as a percentage. Higher values indicate stronger synchronized evidence. Importantly, the documentation is explicit that this is **not a probability** that the move will continue — it measures the strength of the evidence supporting the current Flow State.

## Early Warnings vs. Confirmed Signals

This is the part worth reading carefully, because it's where repainting enters the picture — deliberately.

**Early Flow Warning** uses the live, still-forming candle to flag a potential transition before the candle closes. These warnings are intentionally provisional and may change or disappear as Price or OI moves during the candle.

**Confirmed Flow Signals** are evaluated only when the candle closes. Once confirmed, the LB / SB / SC / LU marker is based on the completed candle and does not change afterward.

So the design explicitly separates **early information** from **confirmed information** rather than hiding the natural evolution of live data. Early warnings repaint during the active candle; confirmed markers do not.

## Settings and How to Tune Them

The script exposes a **Flow Model** selector, which changes how the Positioning Flow Index is calculated:

- **Model A — OI × sign(Price):** Open Interest sets the magnitude, Price sets the direction. Emphasizes participation strength and can produce a strong reading even when the price move itself is small.
- **Model B — OI × Price:** The two Z-scores are multiplied directly. Captures the interaction of both dimensions, but unusually large Price Z-scores can dominate the result.
- **Model C — Price Direction × OI Magnitude × Price Confirmation:** Price drives directional pressure, OI drives participation magnitude, and the absolute Price Z-score contribution is capped to reduce the influence of extreme price moves. **This is the default model.**

The three models are provided as different ways of interpreting the same underlying Price/OI relationship, not as competing signals. The documentation does not state that any one produces better results — only that they differ in emphasis.

There's also an optional **Price Sentiment** component, a smoothed and normalized view of price behavior on the same **-100 to +100** scale, allowing direct comparison with PFI. And an optional **State Ribbon** on the main chart: **teal** for Long Buildup, **red** for Short Buildup, **yellow** for Short Covering, **orange** for Long Unwinding, and **gray** for Neutral. Ribbon intensity is influenced by Signal Strength.

## How to Read It

PFI is positioned by its author as a **contextual positioning tool**, not a standalone entry system. A strong Long Buildup suggests rising price with expanding OI; a strong Short Buildup suggests falling price with expanding OI; Short Covering suggests rising price with contracting OI; Long Unwinding suggests falling price with contracting OI. Signal Strength helps separate stronger synchronized conditions from weaker ones, while PFI itself gives the continuous directional measure.

The documentation is candid that these states describe the current Price/OI relationship — they do not guarantee future direction.

## The Honest Trade-Offs

**Pros:**
- Combines two genuinely independent dimensions (Price and OI) rather than repackaging price momentum
- Z-score normalization distinguishes unusual positioning changes from ordinary noise
- A clearly defined, non-repainting confirmation layer alongside explicitly provisional early warnings
- Bounded -100 to +100 PFI and a separate Signal Strength metric give both direction and evidence quality

**Cons:**
- Requires markets where **Open Interest data is available** — this rules out instruments without it
- The Flow State reflects the relationship between Price and OI and should not be read as a direct measure of individual trader intent
- Early warnings will repaint during the active candle by design, which will bother traders who don't separate them from confirmed markers
- The three Flow Models mean the PFI reading is model-dependent, adding a layer of interpretation

## Who Should Use This

Traders working in derivatives markets where Open Interest is meaningful — futures, options-driven instruments, and crypto perpetuals — are the natural audience. Anyone doing discretionary positioning or market-structure analysis will find the four-state framework and Signal Strength a useful structured lens. It's explicitly framed for incorporation into existing frameworks, not as a replacement for one.

**Skip it if** you trade instruments without Open Interest data, or if you want a mechanical entry signal. This isn't that, and the author doesn't claim it is.

## FAQ

**Does it repaint?** It depends on which layer you're looking at. Early Flow Warnings are intentionally repaintable during the active candle because they use live, developing data. Confirmed Flow markers are non-repainting, since they're generated only after the candle closes.

**What does the Signal Strength percentage mean?** It measures how strongly Price and Open Interest are moving together — the strength of evidence supporting the current Flow State. It is explicitly **not** a probability of continuation.

**Which Flow Model should I use?** The default is Model C, which caps the Price Z-score contribution to reduce the influence of extreme moves. The documentation presents all three as different interpretations rather than ranked options, so the choice depends on whether you want participation-weighted, interaction-weighted, or direction-and-confirmation-weighted flow.

**What markets does it work on?** Markets where Open Interest data is available. The documentation does not specify timeframes.

## Final Verdict

Positioning Flow Index is a focused, well-documented positioning framework rather than another momentum oscillator with a new coat of paint. Its value is in forcing a specific question — *what is happening to market positioning as price moves?* — and answering it with normalized, bounded, and separately-graded measurements. The explicit split between repaintable early warnings and non-repainting confirmed markers is handled honestly, which is more than most scripts manage.

The limitations are real: no Open Interest, no indicator, and the framework describes positioning rather than predicting direction. But for traders in OI-bearing markets who want structure rather than signals, it's a legitimate analytical addition.

**Rating: ⭐⭐⭐⭐ (4/5)** — A point off for the Open Interest dependency and the interpretative overhead of three Flow Models. For a free script, that's a solid deal.

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

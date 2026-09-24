---
title: "Footprint_Delta_Auction_Map_Bullbyte Review: Settings, Strategy & How to Use It"
date: 2026-08-30
draft: false
type: reviews
image: "/screenshots/footprint-delta-auction-map-bullbyte.png"
tags:
  - "footprint delta auction map bullbyte"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Bullbyte's Footprint_Delta_Auction_Map overlays order flow on trend charts. Honest review of settings, strategy, and whether it beats standard delta tools."
tv_script_url: "https://www.tradingview.com/script/73u5eagK-Footprint-Delta-Auction-Map-BullByte/"
sources: ["https://www.tradingview.com/script/73u5eagK-Footprint-Delta-Auction-Map-BullByte/"]
---
I'll be straight with you: most footprint-style indicators on TradingView are either overpriced eye candy or repackaged volume histograms. BullByte's Footprint Delta Auction Map sits somewhere in the middle — and that's not a bad thing. Here's what actually matters.

**What it really does**

This is not a delta overlay with zones bolted on. It's an auction-market-theory qualification framework built around four questions asked on each confirmed bar: is there directional pressure, is the candle convincing, is price at a location the market has already respected, and what kind of session is this. Only when those align does it mark a scenario and draw a reference-level map.

The pressure reading comes from a 3-tier delta engine. Tier 3 uses TradingView's native volume footprint via `request.footprint()` and requires a Premium or Ultimate plan on a supported symbol. Tier 2 is the default and reconstructs intrabar pressure from lower-timeframe sub-bars using `request.security_lower_tf()` plus a close-in-range volume heuristic. Tier 1 is a single-bar OHLCV proxy — `buyPressure = (close − low) / range × volume` — and acts as the universal fallback. All three normalize to a bounded -100 to +100 scale before entering the score. The dashboard always shows which tier is active, which matters because the tiers are not statistically equivalent even on the same scale.

**How the qualification works**

The composite score is `Fingerprint Score × 0.60 + Ladder Score × 0.40`. The fingerprint side combines auction pressure conviction (up to 40 points), candle body and range structure (up to 35 points), and volume/pressure balance magnitude (up to 25 points). The ladder side scores proximity to POC, VAH/VAL, session high/low, prior day high/low, weekly high/low, and configurable round numbers using a triangular decay kernel — `score = 1 − (distance / tolerance)` inside tolerance, zero outside.

The 60/40 split is a deliberate design choice: location confirms, pressure and structure trigger. When native footprint data is active, the genuine volume-profile references get the highest ladder weights. When it isn't, those weights are reduced so the ladder doesn't treat session-derived proxies as real volume-profile levels. That's a detail most confluence indicators skip.

**What the IB classifier actually changes**

The Initial Balance classifier compares today's IB range against a rolling median of prior sessions — today is never included in its own median. Wider than 1.25x → Trend Day, threshold raised by 5, Extension scalar 1.15x. Narrower than 0.75x → Balance Day, threshold lowered by 5, Extension scalar 0.85x. Otherwise Neutral Day. This layer adjusts only the threshold and the Extension multiplier — it does not touch the 60/40 composite weights. Signals are also suppressed until the current IB has formed and at least three completed historical IB samples exist.

The descriptive text is candid that this is a heuristic regime signal, not a factual market classification. That honesty is worth noting.

**Settings and How to Tune Them**

Timeframe defaults are documented. On 5m–15m charts, HTF defaults to 60 with 1m intrabar reconstruction. On 30m–1H, the description suggests considering HTF 240. On 1m charts, leaving Intrabar Reconstruction at the default "1" causes the lower-timeframe request to fall back to Tier 1, because the requested resolution isn't lower than the chart timeframe. Setting Intrabar Reconstruction to a seconds-based resolution on 5m or higher charts can exceed TradingView's intrabar request cap.

The settings the author flags as frequently changed: Composite Score Requirement (default 58), HTF Resolution (default 60), and Cooldown Period (default 20 bars). The per-market tunables are Round Number Step and the IB Window — on a 15-minute chart the default 6-bar IB window represents 90 minutes.

The defaults intended to rarely need adjustment: ATR inputs, Pressure Normalization Lookback, Sizing Regime Lookback, Auto Sizing Band Lookback, and Level Tolerance % (default 1.2%).

Advanced toggles: Footprint Engine should stay OFF unless you have the plan and symbol support. Intrabar Reconstruction stays ON by default. Dynamic Extension Sizing, Auto-Derive Sizing Band, and Require Next-Bar Confirmation are the other switches worth knowing.

**Entry, Reaction, Extension, Invalidation**

All four levels are sized as multiples of a shared Sizing Unit, not raw ATR. The Sizing Unit is a percentile-bounded percentage of price, with its band auto-derived from the instrument's own historical ATR-as-percent-of-price distribution (10th and 90th percentiles by default). Entry is the signal bar close. Reaction is Entry ± k1 × Sizing Unit (default k1 = 1.5). Invalidation is Entry ± k3 × Sizing Unit (default k3 = 1.5). Extension uses an effective k2 that is the larger of (k1 + 0.5) and (k2 base × IB scalar × volatility regime scalar) when dynamic sizing is on, or the larger of (k1 + 0.5) and k2 base (default 2.5) when it's off. The volatility scalar clamps current ATR over baseline ATR between 0.8x and 1.6x so a single spike can't produce a runaway target.

The scenario lifecycle runs Pending → Reaction Zone Reached (a first-touch alert, not a resolution) → Resolved-Extension or Resolved-Invalidation. On resolution, right-edge tags are removed, lines freeze, and a cooldown begins.

**The same-bar disclosure**

When one bar touches both Extension and Invalidation, OHLC data alone cannot establish which came first. The script uses a deterministic proximity convention — the level closer to the prior bar's close is assumed reached first. This is documented as a convention, not an observation of intrabar sequence, and it's disclosed on-chart. Credit where due: many indicators in this space quietly ignore the problem.

**Alerts**

Five alert conditions are selectable in the TradingView dialog: Long Scenario Marked, Short Scenario Marked, Reaction Zone Reached, Extension Zone Reached, and Invalidation Level Reached. The script also issues dynamic `alert()` messages once per confirmed bar close, including direction, active-tier pressure reading, nearest qualifying level, and session character.

**Limitations worth knowing**

The script does not calculate P&L, win rate, or historical strategy performance — it's a discretionary analytical indicator, not a backtest. The IB classifier is a heuristic. The confluence ladder weights are pre-defined analytical weights, not statistically derived reliability scores. Footprint mode may behave inconsistently during Bar Replay due to TradingView's footprint data caching, and the script displays an on-chart notice recommending you disable it for replay testing.

The script does not natively detect Fair Value Gaps or Order Blocks. If you use those, they're external context you compare against the reference-level map — they are not generated or validated by this script.

**Who it's for**

Intraday traders on 5m, 15m, 30m and 1H charts on liquid instruments: crypto pairs, index futures and CFDs, liquid FX, and large-cap equities during regular session hours. The author explicitly does not recommend it for very illiquid instruments, daily or higher timeframes (the IB logic is intraday by design), or symbols with no volume data.

**What to try instead**

If you want raw footprint data with bid/ask split on every price, a dedicated footprint chart from a platform like Sierra Chart or Bookmap is the honest answer — this script is not that. If you want a simpler volume-profile view, TradingView's built-in Volume Profile tools cover that ground without the qualification layer.

**FAQ**

**Does it repaint?** The HTF EMA filter is explicitly built on the confirmed previous higher-timeframe bar using `barmerge.lookahead_on` on a `[1]` offset — the documented non-repainting pattern for confirmed HTF references. The HTF resolution is validated to be strictly higher than the chart timeframe before the request is made; if not, the script halts with an explicit error. Beyond that, the source material does not make blanket repainting claims for the pressure tiers or level plots.

**Is it free?** Published as open-source under the Mozilla Public License 2.0.

**Can I use it for automated trading?** It's a discretionary analytical indicator, not a strategy script. It does not produce audited P&L or position sizing.

**Does it work on crypto?** The author lists liquid crypto pairs among the intended instruments, with the same caveat applying: volume data quality drives the usefulness of any volume-derived reading.

**Final verdict**

This is a framework, not a signal generator, and it's built with unusual transparency about what each layer does and doesn't do. The 3-tier architecture is a genuine practical concession to plan tiers, the IB classifier is scoped to exactly two outputs, and the same-bar resolution limitation is disclosed rather than hidden. If you want a single auditable process that brings order flow, candle structure, location, and session regime into one qualification — and you're willing to accept that signals are intentionally infrequent — this earns a look. If you want a footprint chart with true bid/ask granularity, this isn't that, and the description says so.

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

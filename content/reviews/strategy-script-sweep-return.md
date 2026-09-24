---
title: "Strategy_Script_Sweep_Return Review: Settings, Strategy & How to Use It"
date: 2026-09-17
draft: false
type: reviews
image: "/screenshots/strategy-script-sweep-return.png"
tags:
  - "strategy script sweep return"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Strategy_Script_Sweep_Return review: how this sweep-and-reclaim trend tool works, best settings, entry logic, and whether it beats manual liquidity hunting."
tv_script_url: "https://www.tradingview.com/script/7OLnQI4B-STRATEGY-SCRIPT-Sweep-Return-v1/"
sources: ["https://www.tradingview.com/script/7OLnQI4B-STRATEGY-SCRIPT-Sweep-Return-v1/"]
---
Most "sweep" indicators on TradingView are just pivot markers with a fancy name. EE Sweep Return v1 is not that. It's a full strategy script built around the failure of Opening Range Breakouts — the moment price sweeps above or below the morning range, traps breakout traders, then reverses back inside. The sweep itself is a trap half the time. The return is the tell.

## What the script is doing under the hood

The architecture is a three-phase sequence, anchored to Central Time:

**Calibration (08:30–09:30 CT).** The script maps the absolute high (`orH`) and low (`orL`) of the cash session open, visualized as a shaded box.

**Arming (09:30–15:00 CT).** The indicator monitors for a breach. A break above `orH` arms a potential short trap; a break below `orL` arms a potential long trap.

**Execution (09:30–15:00 CT).** The trigger fires. A SHORT prints if price sweeps the high but closes back below `orH`. A LONG prints if price sweeps the low but closes back above `orL`.

The return condition is the whole point. A sweep with no close back inside the range is just a breakout. The script refuses to signal until the reversion happens, which is why it behaves differently from raw breakout tools.

## Features that earn their place

**Same-bar logic.** By default (`sameBar = true`), the indicator allows the break and the reversion to happen on a single candle — a wick rejection. Toggled off, it requires one candle to close outside the range and a subsequent candle to close back inside. This is the setting that changes the character of the signals: the default is faster and more permissive, the alternative is stricter and slower.

**Timezone alignment.** The `America/Chicago` timezone anchors the logic to Central Time, keeping the 08:30–09:30 calibration window aligned with the initial hour of the New York equities open.

**Strategy mode.** It runs as a strategy script, not just a visual overlay, so the signal logic is backtestable.

## Settings and How to Tune Them

The documented parameter is `sameBar`, which toggles between single-candle wick rejections and a two-candle sequence requiring a close outside the range followed by a close back inside. That's the tradeoff to tune: same-bar on for more frequent, more permissive triggers; same-bar off to demand a confirmed close outside the range before accepting the reversion.

The source material also describes several conceptual extensions rather than shipped settings — granular micro-structure analysis of the sweep itself, contextual volatility filtering to disable the sweep logic on high-trend-probability days, and dynamic adjustment of the opening range window based on the asset's real-time ATR and relative volume. These are framed as directions for an AI-integrated model, not as current configuration options.

## How the logic trades

The mechanical sequence is fixed by the calibration window: the range is set between 08:30 and 09:30 CT, and execution only occurs inside the 09:30–15:00 CT window. A short requires a sweep of `orH` followed by a close back below it; a long requires a sweep of `orL` followed by a close back above it. Everything else — position sizing, targets, exits — is left to the trader.

## Pros and cons

**Pros:**
- The return-confirmation requirement is genuinely more selective than a bare sweep marker
- The three-phase structure is explicit and mechanical, with defined reference levels
- Works as both a visual indicator and a backtestable strategy
- The `sameBar` toggle gives a real choice between permissive and strict confirmation

**Cons:**
- Confirmation delay means you never catch the exact low or high
- The logic is tied to a fixed session window, so it isn't a general-purpose tool
- Limited documentation beyond the architectural breakdown
- The AI-integration material describes intended extensions, not built-in functionality

## Who it's for

Discretionary intraday traders who already understand liquidity concepts and want a mechanical trigger instead of eyeballing wicks around the opening range. It is not for trend followers — this is a counter-move tool by construction, and fighting that framing will get you hurt.

## FAQ

**Does it repaint?** The source material doesn't address repainting directly. The execution logic requires a close back inside the range, so a short or long prints only once that close condition is met.

**What markets does it work on?** The source material only describes the cash session open and New York equities timing. It doesn't make claims about other asset classes.

**Is it a buy/sell indicator or a full strategy?** A strategy script. The visual shaded box and the signal markers are part of the same script.

**Why no signal on an obvious sweep?** Most likely because the close didn't come back inside the range — either within the same bar (if `sameBar` is on) or on a subsequent candle (if it's off).

## Verdict

EE Sweep Return v1 does one job and does it well: it forces patience around opening-range liquidity grabs instead of letting you chase the wick. The confirmation requirement is a feature, not a bug — it's the reason the signals mean something. It's not a holy grail, and the fixed session window limits where it applies, but for traders who already fade opening-range breakouts manually, this is a clean mechanical structure.

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

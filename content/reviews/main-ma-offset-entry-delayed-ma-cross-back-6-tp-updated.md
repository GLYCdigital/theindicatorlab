---
title: "Main Ma Offset Entry Delayed Ma Cross Back 6 Tp Updated Review"
date: 2026-10-04
draft: false
type: reviews
image: "/screenshots/main-ma-offset-entry-delayed-ma-cross-back-6-tp-updated.png"
tags:
  - "main ma offset entry delayed ma cross back 6 tp updated"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "A Nasdaq-focused MA cross strategy with offset entries, structure-based stops, six scaling targets, and a cross-back exit. Honest review of how it works."
tv_script_url: "https://www.tradingview.com/script/CjwDVYvb-Main-MA-Offset-Entry-Delayed-MA-Cross-Back-6-TP-updated/"
sources: ["https://www.tradingview.com/script/CjwDVYvb-Main-MA-Offset-Entry-Delayed-MA-Cross-Back-6-TP-updated/"]
---
Most moving-average strategies are one idea dressed up as a system: cross the line, enter, hope. This one is different in a way that matters — it treats the MA as both an entry trigger and an ongoing trade manager, then layers position sizing and exits on top. If you trade NQ or MNQ and already think in terms of MA structure, this is worth understanding before you install it.

## What it actually does

The core is a single configurable moving average. The default is the 200 EMA, but the author allows SMA, WMA, VWMA, or VWAP. Price crossing that line generates the entry signal — long above, short below.

The wrinkle is the offset. Rather than entering at the cross itself, the strategy enters a configurable distance beyond the MA — one point by default. That offset is fully adjustable. The intent is presumably to avoid getting filled right at the line where price often chops.

Two optional filters narrow direction. The daily candle filter, on by default, looks at the previous daily bar: green means longs only, red means shorts only. The slope filter, off by default, measures price slope over a configurable candle count and timeframe — default 15 candles on the 1-minute chart — with positive slope allowing longs and negative allowing shorts. When both are active, slope takes priority.

## The trade management is where it earns its keep

The initial stop is structural, not arbitrary. It sits at the low of the cross candle for longs and the high for shorts. That means your risk is defined by the bar that created the signal, which is a cleaner logic than a fixed point stop. It can be toggled off.

Then there's the cross-back protection. Once a trade moves a configurable number of points into profit — one point by default — the MA becomes a trailing exit. Cross back below the MA on a long, or above it on a short, and the remaining contracts close. You can push that activation distance out to 5, 10, 20, 50 points or wherever you want the leash to start.

Position sizing is baked in: each trade opens six contracts, one per take-profit target. The defaults step up from 40 points through 80, 140, 200, 300, and finally 500 points. All six are independently adjustable. It's a scale-out ladder, and the cross-back rule protects whatever hasn't been taken off yet.

There's also a weekly risk control that closes remaining positions before the week ends — Friday 4:00 PM New York by default, optional and time-adjustable.

## How you'd actually run it

You'd pick your MA type and length first, because everything keys off it. Then decide your filters: the daily candle filter is the passive default, while the slope filter is the more active choice and overrides the daily logic when enabled. Set your entry offset, confirm the stop toggle is where you want it, and decide your cross-back activation distance.

The six targets are where personal preference dominates. The defaults are aggressive on the back end — a 500-point final target assumes you catch a genuine trend leg. If you're scalping, you'll likely compress that ladder. If you're swinging the NQ, the defaults may suit you as-is.

## Pros and cons

**Pros:**
- Entry offset avoids fills directly on the MA, which is where the noise lives
- Structure-based stop tied to the cross candle, not an arbitrary number
- The cross-back exit is genuinely clever — the same line that gets you in manages you out
- Six independent targets give real control over the risk/reward profile
- Weekly close-out prevents weekend gap exposure by default

**Cons:**
- Built specifically for MNQ/NQ; nothing here adapts it to other instruments
- Six contracts per trade is a heavy size assumption — small accounts will need to rethink the ladder
- Two direction filters with a priority rule adds a layer of logic you must actually understand before trusting it
- The 500-point final target is ambitious and won't fill in choppy conditions
- No documented guidance on which MA type or length suits which regime

## Who it's for

Futures traders working NQ or MNQ who already use MA structure and want an automated framework rather than a signal. It rewards someone willing to tune the ladder and filters. It's not for beginners, and it's not for anyone trading a small account where six contracts is fantasy sizing.

## FAQ

**Does it work on anything other than Nasdaq futures?** The author designed it for MNQ/NQ. Nothing in the description claims broader applicability.

**What's the default configuration?** 200 EMA, previous-day direction filter, one-point entry offset, cross-candle stop, cross-back protection, and the six progressive targets.

**Can I disable the stop loss?** Yes, it's toggleable.

**What happens if the slope filter and daily filter disagree?** The slope filter takes priority when enabled.

## Verdict

This is a thoughtfully assembled strategy, not a repackaged crossover. The offset entry, structural stop, and cross-back exit form a coherent idea: get in slightly beyond the noise, define risk by structure, and let the MA manage the remainder while a ladder books profit. The NQ-specific design and six-contract assumption are real limitations, but for the trader it's built for, the logic holds together.

⭐⭐⭐⭐
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and the official TradingView script documentation. Always test indicators in a demo environment before live trading.*

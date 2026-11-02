---
title: "Blackcat L3 Squeeze Dynamics Review — Volatility Indicator"
date: 2026-11-03T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/blackcat-l3-squeeze-dynamics.png"
tags:
  - "blackcat l3 squeeze dynamics"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Blackcat L3 Squeeze Dynamics V2 review: a squeeze-momentum signal engine with a position state machine, ATR risk levels and a live dashboard."
tv_script_url: "https://www.tradingview.com/script/dudnzu8a-blackcat-L3-Squeeze-Dynamics-V2/"
sources: ["https://www.tradingview.com/script/dudnzu8a-blackcat-L3-Squeeze-Dynamics-V2/"]
---
The original squeeze momentum studies told you when volatility was compressing. They never told you what to do about it. **L3 Squeeze Dynamics V2** keeps the V1 calculation core — squeeze, momentum, SAR and volume weighted RSI — and rebuilds everything around it into a full long/short signal engine. The pitch here isn't a new indicator; it's a trade-management layer bolted onto a familiar one.

## What it actually does

The core logic is a Bollinger-vs-Keltner comparison. When the Bollinger envelope sits fully inside the Keltner envelope, the market is compressed and an expansion is pending. Fully outside means the move has already started. The mixed state is explicitly treated as noise and blocked — which is the right call, because most squeeze scripts fire in that grey zone and generate junk.

On top of that sit three confluence filters:

- **Squeeze momentum** — a linear regression of price against its channel mid-range, signed for bias, with the slope versus the prior bar as acceleration.
- **Parabolic SAR** — price must be on the correct side of the trailing reversal system.
- **Volume weighted RSI** — pressure must be above or below a center line.

A signal only fires when squeeze and momentum are in a decisive state *and* momentum is accelerating away from zero, with SAR and RSI confirming.

## The part that matters: governance

Most multi-filter scripts are just AND gates. L3 V2 adds a **position state machine** that tracks long, short and flat. Signals fire on their first bar only, a cooldown bar setting suppresses clusters, the opposite condition closes the trade, and same-bar reversals collapse into one combined event. Exits always outrank entries, so the state can't contradict itself.

This is the feature that separates it from a stack of plots. A cooldown is a blunt tool, and the developer says so in the limitations — flat ranges release the squeeze repeatedly and the cooldown "does the heavy lifting." At least they're honest about it.

## Risk levels and the dashboard

ATR-based take-profit and stop levels are frozen at entry, so they don't drift while the trade is open. You can optionally exit when those levels are hit. The live dashboard reads out position, squeeze state, momentum, RSI, SAR bias, entry, target, stop and bars in trade — enough to read the setup without hovering over plots.

There are seven alert conditions (long entry, short entry, long exit, short exit, reversal, target hit, stop hit) with dynamic text containing ticker, timeframe and price. Alerts default to once per bar close on confirmation, so they don't repaint.

## Pros and cons

**Pros**
- The signal logic is genuinely filtered — squeeze, momentum acceleration, SAR and volume weighted RSI all have to agree.
- The state machine prevents the classic problem of a script screaming both long and short within the same cluster.
- ATR levels frozen at entry is a small detail that shows the author thought about live trading, not just chart aesthetics.
- Everything visual is optional. You can run it lean.
- The limitations section is unusually candid, including flagging its own odd SAR defaults.

**Cons**
- The volume weighted RSI block needs a real volume feed, so it won't behave properly on instruments without one.
- The long Bollinger and Keltner periods mean few signals on low timeframes — this is not a scalping tool.
- The SAR defaults are strange: the increment exceeds the ceiling, so the SAR behaves like a fixed step system. The developer tells you to lower the increment for a classic response, but shipping odd defaults is a trap for anyone who doesn't read the description.
- Squeeze logic is a known family of study; the value here is the wrapper, not the engine.

## Who it's for

Discretionary swing and position traders on higher timeframes who want a structured volatility-expansion setup with pre-defined risk. Also useful for traders who already like squeeze momentum but are tired of manual filter-stacking — the state machine does that bookkeeping for you. Scalpers and lower-timeframe traders should look elsewhere given the period lengths.

## FAQ

**Does it repaint?** Alerts default to once per bar close on confirmation, per the documentation, so the signals are designed not to repaint.

**Can I run long and short at the same time?** No. The position state machine allows one position at a time. Same-bar reversals can flip you without a flat bar if that option is enabled.

**Why does the SAR look odd?** The default increment exceeds the ceiling, so it acts like a fixed step. Lower the increment for a conventional response.

**Is it a complete trading system?** No. The ATR levels are explicitly a risk frame, not a guarantee of a profitable trade.

## Verdict

L3 Squeeze Dynamics V2 is a well-engineered wrapper around a familiar squeeze core. The confluence filters and the state machine are real additions, not decoration, and the frozen ATR levels reflect live-trading thinking. It loses a star for the odd SAR defaults and the volume-feed dependency, but if you trade volatility expansion on higher timeframes, it's worth a look.

**Rating: ⭐⭐⭐⭐ (4/5)**
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

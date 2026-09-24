---
title: "Ml_Vsa Review: Settings, Strategy & How to Use It"
date: 2026-08-31
draft: false
type: reviews
image: "/screenshots/ml-vsa.png"
tags:
  - "ml vsa"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Ml_Vsa review: how this volume-spread analysis tool flags smart money moves, best settings, entry logic, and who should use it."
tv_script_url: "https://www.tradingview.com/script/HXOgXfMr-ml-vsa/"
sources: ["https://www.tradingview.com/script/HXOgXfMr-ml-vsa/"]
---
Ml_Vsa is a Pine v6 **library**, not a standalone indicator — and that distinction matters before anything else. It doesn't plot anything on its own. It's a shared dependency that other scripts import to get a consistent vocabulary for Volume Spread Analysis (VSA) readings. If you were expecting a chart overlay you can drop on and trade, this isn't that.

**What it actually does**

The library packages the classic VSA effort-vs-result reading of a bar into named, directional events with fixed definitions. The premise: volume is effort, the spread and close location are result. Effort with no result — heavy volume, narrow spread — is absorption. Result with no effort — wide spread, light volume — is a move with nothing behind it. A new extreme that gets rejected on volume is a trap.

Rather than describing absorption vaguely ("price made a high but the oscillator didn't"), a script importing this library can name the event — "Upthrust" or "Stopping Volume" — so the same event means the same thing across every script built on it.

**Key features that matter**

- **Primitives**: `closePos` (where the bar closed in its range, 0 to 1), `spreadPct` (current range as a percentile of recent history — the result axis), and `volPct` (current volume as a percentile of its history — the effort axis).
- **Named events**: `noDemand` (bearish), `noSupply` (bullish), `upthrust` (bearish, new high rejected on high volume), `shakeout` (bullish, new low rejected on high volume), `stoppingVolume` (bullish, wide down-bar on very high volume closing off the low), `climax` (returns +1/−1/0 for selling/buying exhaustion), and `effortNoResult` (a non-directional absorption flag).
- **Composites**: `vsaBias` nets the events to a direction (+1/−1/0, deliberately excluding the non-directional absorption flag), `vsaCode` identifies which event dominates as an integer, and `vsaLabel` returns the dominant event as a string for a dashboard or marker.
- **Self-contained events**: Each one-bar classification is its own function, so you can call only what you need.

**Settings and How to Tune Them**

This is a library, so there are no chart-level settings — the parameters are function arguments, and the host script decides what to expose.

- **Window lengths**: Each function takes simple window lengths for its rolling history. The source material describes these as "yours" — the library leaves them to the caller. The example in the documentation uses an integer input for a VSA history window and a separate lookback for new-extreme detection, exposed as inputs in the host script.
- **Percentile thresholds**: These follow standard VSA practice and are baked in, not user-adjustable. The exception is the climax threshold, which the source material specifies as the 90th percentile.
- **Pivot lookback**: The trap events (`upthrust`, `shakeout`) take a separate pivot length defining how far back the "new high" or "new low" is measured.

There is no sensitivity slider, no volume moving average length, and no signal-strength filter to adjust — those don't exist in this library. Tuning happens entirely through the window lengths the host script passes in.

**How to use it**

The documented pattern is to mark the events and read a shared direction:

```
import Market_Logic_India/ml_vsa/1 as vsa

ut = vsa.upthrust(high, low, close, volume, len, piv)
so = vsa.shakeout(high, low, close, volume, len, piv)
sv = vsa.stoppingVolume(high, low, close, volume, len)

bias = vsa.vsaBias(high, low, close, volume, len, piv)   // +1 / -1 / 0
```

The events pair naturally with level and flow tools. An Upthrust into resistance, or Stopping Volume at support, is a stronger read than either alone — that framing comes straight from the documentation.

**Notes that matter**

- **Non-repainting**: Every read is a pure function of closed-bar spread, volume, close and their rolling history (`ta.percentrank` / `ta.highest` / `ta.lowest`). Nothing looks ahead. To be certain a live bar's event never flickers, the documentation advises gating on `barstate.isconfirmed` in the host script.
- **State safety**: The composites call each event unconditionally and then select, so the `ta.*` inside every event runs on every bar. If you call individual events yourself, keep them out of `if`/ternary branches for the same reason.
- **Types**: Pass series for price/volume inputs and simple int for window lengths.
- **Scope**: These are OHLCV-based proxies for the classic tape reads, not exchange-grade order flow. The documentation explicitly recommends pairing every event with a forward test before trusting its edge on your instrument.
- **Volumeless symbols**: On a symbol with no volume, `volPct` is flat and the volume-gated events never fire.

**Credit and license**

VSA and the effort-vs-result principle — with named events No Demand, No Supply, Upthrust, Shakeout/Spring, Stopping Volume, Buying/Selling Climax and Test — descend from Richard D. Wyckoff and the VSA tradition associated with Tom Williams. This library is described as an original, dependency-free Pine v6 packaging of those public techniques, unaffiliated with any originator. Licensed under Mozilla Public License 2.0, as required for TradingView libraries.

**Who it's for**

Pine developers building studies that need a consistent VSA vocabulary — not end users looking for a plug-and-play signal generator. If you don't already understand what a no-demand bar is or why volume spread matters, the library won't teach you; it assumes the framework. The real value is consistency: `vsaBias` means the same thing on every engine you build on top of it.

**Final verdict**

As a library, Ml_Vsa does one job cleanly: it names VSA events with fixed definitions and nets them to a direction. The non-repainting design and the unconditional-call pattern show it was written by someone who understands Pine's state pitfalls. It's not a trading system and makes no performance claims — the documentation is explicit that these are proxies needing forward validation. Judge it on whether a shared VSA vocabulary is useful to you, not on whether it prints winning signals.

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

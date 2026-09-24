---
title: "Range_Breakout_By_Av Review: Settings, Strategy & How to Use It"
date: 2026-09-18
draft: false
type: reviews
image: "/screenshots/range-breakout-by-av.png"
tags:
  - "range breakout by av"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Range_Breakout_By_Av review: how this TradingView range breakout indicator plots levels, its best settings, entry logic, pros, cons and rating."
tv_script_url: "https://www.tradingview.com/script/169CP9sj-Range-Breakout-by-AV/"
sources: ["https://www.tradingview.com/script/169CP9sj-Range-Breakout-by-AV/"]
---
Range Compression Breakout does one job and does it without ceremony: it detects periods of low-volatility consolidation, draws and maintains the range in real time, and signals when price transitions into expansion. No fixed price distance, no assumptions about which market you're trading.

That sounds modest. It is also the kind of infrastructure range traders actually need, because the hard part of range trading has never been spotting the range — it's being disciplined about *which* range counts and *when* it's broken.

## What the indicator actually plots

The range is drawn on price as a dynamic box: a top boundary, a bottom boundary, and a midline. Once a range is detected, the box expands to absorb new highs and lows while price stays contained, capturing the full churn of the consolidation instead of resetting on every probe.

Compression is measured relative to the market's own recent behavior rather than a fixed price distance. In Adaptive Percentile mode, a range qualifies when its high-low span sits among the quietest percentile of its recent history — so the same settings work across futures, FX, crypto, and equities without retuning. ATR Multiple mode is also available for a fixed volatility-based threshold.

**The features that earn their keep:**

- Dynamic range box that expands to absorb new highs and lows during consolidation
- Two compression modes: Adaptive Percentile (relative to recent history) and ATR Multiple (fixed volatility threshold)
- Break signals with an optional buffer beyond the boundary, optional multi-bar confirmation, and an optional volume-spike filter
- Wick Long / Wick Short signals for failed probes that close back inside the range
- A cooldown period after each break that prevents the box from immediately reforming on the expansion move
- Diagnostic values including the range-to-ATR ratio and compression state available in the Data Window for calibration

## Settings and How to Tune Them

Four preset profiles configure lookback, tightness, minimum bars, confirmation, and cooldown together:

- **Tight Ranges** — for low-timeframe scalping
- **Normal Ranges** — for intraday
- **Swing Trading** — for multi-day consolidations
- **Options Selling** — for extended sideways chop

Custom mode exposes all parameters individually. Box fill, borders, midline, and signal colors are fully adjustable, and each signal type toggles independently.

Two settings deserve particular attention. The volume-spike filter should be left off on spot FX and other symbols reporting tick-based volume — the filter assumes real volume data. And the compression mode choice matters: Adaptive Percentile is the mode that travels across instruments without retuning, while ATR Multiple gives you a fixed volatility threshold if you prefer to define compression in absolute terms.

## How to trade it

The Break signal fires when price closes decisively beyond the boundary plus a buffer, with optional multi-bar confirmation and an optional volume-spike filter. The Wick Long / Wick Short signals are a different play entirely: a failed probe outside the range that closes back inside on a long wick, confirmed by the following bar, indicating mean reversion toward the midline.

The two signal types point in opposite directions. Break trades the expansion; Wick signals trade the rejection. Treating them as the same setup is a mistake.

## Pros and cons

**Pros**

- Range detection is relative to the market's own recent behavior, so settings carry across futures, FX, crypto, and equities
- The box expands to absorb new highs and lows rather than resetting on every probe, so the consolidation is captured in full
- Multiple confirmation layers available: buffer, multi-bar confirmation, volume-spike filter
- Cooldown after each break prevents the box from immediately reforming on the expansion move
- Four preset profiles cover scalping through extended sideways chop without manual configuration
- Diagnostic values in the Data Window let you calibrate compression state directly

**Cons**

- Volume-spike filter is unusable on spot FX and other tick-volume symbols
- Four preset profiles and a Custom mode mean there are a lot of parameters to understand before the tool behaves as you expect
- No built-in guidance on which compression mode suits which market — that's on you to calibrate via the Data Window

## Who it's for

Discretionary traders who want a mechanical, self-calibrating definition of compression and expansion rather than a fixed lookback range. The preset profiles map to distinct trading styles — scalping, intraday, swing, and options selling — so the tool is aimed at traders who already know which of those they are. If you want a range tool that requires no calibration, the Adaptive Percentile mode gets you closest, but the Data Window diagnostics exist because calibration is expected.

## Alternatives

- **Donchian Channel** — simpler, built-in, and covers fixed-lookback breakout ground
- **Opening Range Breakout scripts** — better if you trade the first hour of a session specifically
- **Support/Resistance zone indicators** — better if you want dynamic zones rather than a compression-defined box

Range Compression Breakout isn't trying to beat Donchian on simplicity. It's trying to distinguish quiet consolidation from ordinary price movement, and for traders who care about that distinction, that's the whole point.

## FAQ

**Does it repaint?**
The source material describes the box as dynamic — it expands to absorb new highs and lows while price stays contained. It does not make any claim about repainting either way.

**What timeframe is best?**
The preset profiles are organized by trading style rather than timeframe: Tight Ranges for low-timeframe scalping, Normal Ranges for intraday, Swing Trading for multi-day consolidations, and Options Selling for extended sideways chop.

**Can I use it for mean reversion?**
Yes. The Wick Long / Wick Short signals are designed for exactly that — a failed probe outside the range that closes back inside, indicating mean reversion toward the midline.

**Does it work on crypto and forex?**
Adaptive Percentile mode is designed so the same settings work across futures, FX, crypto, and equities without retuning. On spot FX and other symbols reporting tick-based volume, leave the volume-spike filter off.

## Verdict

A focused compression and expansion tool that does one thing and does it without requiring you to retune per instrument. The Adaptive Percentile mode is the reason it travels; the preset profiles are the reason it's usable out of the box; the Data Window diagnostics are the reason you can calibrate it when the presets don't fit. The main caveat is the volume-spike filter, which is unusable on tick-volume symbols, and the sheer number of parameters once you leave the presets.

**Rating: ⭐⭐⭐⭐ (4/5)** — well-built and instrument-agnostic, docked one star for the volume filter's limited applicability and the calibration burden the presets only partly remove.

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

---
title: "Mr_Market_Maker Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/mr-market-maker.png"
tags:
  - mr market maker
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of Mr_Market_Maker — a liquidity-based indicator for detecting smart money footprints. Settings, strategy, and real trader verdict inside."
grounding: "none (no source found)"
---
**Verdict at a Glance:** A liquidity-detection tool aimed at price-action traders who want to see where large orders may be resting, without a flood of alerts. It does not generate trade signals on its own.

---

## What This Indicator Actually Does

Mr_Market_Maker is not an oscillator or a moving-average overlay. It is positioned as a **liquidity detection tool** that highlights levels where market makers and institutional traders are likely placing large orders — high-probability zones rather than predictions.

The intended presentation is horizontal bands drawn at key liquidity levels, with color-coded strength ratings. Green zones are described as fresh, yellow as fading, and red as exhausted. The design goal is a clean chart with minimal clutter.

## Key Features That Set It Apart

- **Dynamic Liquidity Zones** – Unlike static support/resistance, these bands are meant to adjust as volume shifts, so you are not looking at stale levels.
- **Strength Decay System** – Each zone fades over time, moving through the green → yellow → red progression. The purpose is to indicate when a level is losing relevance.
- **Volume-Weighted Anchoring** – Zones are drawn from tick volume clusters rather than arbitrary timeframes, which is the stated basis for its difference from standard pivots.
- **Alert Integration** – Alerts can be configured for zone breaks or strength changes.

## Settings and How to Tune Them

The indicator exposes several parameters that shape how zones are drawn and how long they persist:

**Timeframe:** The tool is intended for higher intraday and swing timeframes; very short timeframes tend to produce noise.

**Zone Strength Threshold:** Controls how strong a volume cluster must be before a zone is drawn. Lower values produce more zones; higher values produce fewer, more selective ones.

**Decay Rate:** Controls how quickly a zone fades from fresh to exhausted. Shorter decay suits faster trading styles; longer decay keeps levels visible for longer holds.

**Max Zones Displayed:** Caps how many zones appear on the chart at once, keeping the display readable.

Exact values are not specified here — tune them to your instrument and holding period.

## How It Can Be Used for Entries and Exits

**Entry:** A common approach is to wait for price to touch a fresh (green) zone and print a rejection candle such as a pin bar or engulfing bar. If price passes through a fresh zone without reaction, that level can be treated as compromised.

**Exit:** Partial profits can be taken at the next zone in the opposite direction — for example, scaling out of a long at a fading resistance zone. A volatility-based stop such as an ATR multiple can trail the remainder.

**Stop Loss:** Placing the stop beyond the next zone rather than at a fixed pip value lets the stop adapt to volatility.

**Pairing:** Combining the indicator with a volume profile tool can help confirm whether a zone has actual volume behind it. Used alone, it can produce false positives during low-volume chop.

## Honest Pros and Cons

**Pros:**
- Zones are drawn from closed candles, so historical zones do not repaint.
- Zones are intended to align with institutional levels rather than arbitrary pivots.
- Clean interface with low chart overhead.
- The decay system is genuinely useful for filtering out stale levels.

**Cons:**
- Steep learning curve — new users tend to overtrade every zone.
- Less reliable on instruments with thin order books.
- No multi-timeframe alignment view; the indicator must be loaded per timeframe.
- Occasional false zone during news spikes — check the economic calendar.

## Who It's Actually For

**For:** Discretionary traders who already use support/resistance and want to add a liquidity dimension. Suited to forex majors, index futures, and high-volume cryptocurrencies.

**Not for:** Traders looking for a "buy/sell" arrow. This is a tool, not a signal service. It is also poorly suited to very fast scalping, where zones change too quickly to act on.

## Better Alternatives (If This Isn't for You)

- **Liquidity Voids Pro** – Cheaper and simpler, but less precise on zone strength.
- **Smart Money Concepts (SMC) Suite** – More feature-rich but cluttered by comparison.
- **Volume Profile Visible Range** – Free and useful for confirming zones, but it does not attempt to detect institutional footprints.

Mr_Market_Maker sits between free options and heavier premium SMC suites in terms of complexity and noise.

## FAQ

**Q: Does it repaint?**
A: Zones are drawn from closed candles, so historical zones are not redrawn.

**Q: Can I use it on crypto?**
A: It is best suited to high-volume cryptocurrencies such as BTC and ETH. Low-volume alts produce unreliable zone detection.

**Q: Best timeframe?**
A: Higher intraday and swing timeframes work best. Very short timeframes are too noisy.

**Q: Is it worth the price?**
A: If you trade liquidity-based strategies, it can fit. If you want a "buy/sell" indicator, look elsewhere.

**Q: Does it work on commodities?**
A: It can be applied to commodities, though results depend on the instrument's volume characteristics.

---

## Final Verdict

Mr_Market_Maker does what it sets out to do — highlight liquidity zones — without gimmicks. It is not a holy grail, but paired with price action and volume confirmation it can add a useful dimension to chart reading.

**One-line takeaway:** Smart money footprints made visible, but you still need to read the map.

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

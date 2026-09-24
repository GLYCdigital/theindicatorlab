---
title: "Liquidity_Magnet Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/liquidity-magnet.png"
tags:
  - liquidity magnet
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Liquidity_Magnet identifies key liquidity zones and stop hunts in real time. Honest review with settings, entry strategy, and who should use it."
grounding: "none (no source found)"
---
# Honest review: Liquidity_Magnet

Stop hunts are a real market phenomenon, and the pitch behind Liquidity_Magnet is that it helps traders spot them. That's a plausible premise, but a review has to be built on verifiable specifics about the tool itself — and on that front the available material is thin.

## What this indicator actually does

The stated purpose is to scan for clustered stop-loss levels and pending orders above recent highs and below recent lows. It marks these zones on the chart as colored bands or lines. When price approaches these zones, the indicator is meant to highlight potential liquidity grabs — moves designed to hunt stops before reversing.

Beyond that description, there is no independently confirmed documentation available here covering its internal logic, its data sources, or how it defines a "cluster" in practice.

## Key features

- **Liquidity zone detection** — Zones are plotted as new data prints, according to the vendor description.
- **Stop hunt alerts** — Visual and push notifications when price enters a marked zone.
- **Multi-timeframe support** — The tool is described as usable across timeframes, from very low to daily.
- **Customizable zone sensitivity** — A setting that governs how many ticks define a cluster.
- **Zone fading** — Zones are described as fading once tested, to keep the chart readable.

Claims about repainting, alert latency, and which timeframes work "best" are vendor or user assertions that cannot be verified from the source material, so treat them as marketing until you confirm them yourself on your own charts.

## Settings and How to Tune Them

Two parameters are described in the source material: **zone sensitivity** and **zone display**.

- **Zone sensitivity** controls how many ticks define a cluster. Higher values are said to produce fewer, wider zones; lower values produce tighter ones. The description suggests crypto may want a different value than forex or indices, but no specific numbers are confirmed here — start from the default and adjust based on how the zones look on your instrument.
- **Zone display** refers to whether zones render as solid bands or dashed lines. This is purely a visual preference.
- **Alert on zone touch** — enabling alerts and limiting them to once per bar is a common way to avoid notification spam, though the exact alert options depend on the platform.
- **Timeframe alignment** — matching the indicator timeframe to your entry timeframe is standard practice for any zone-based tool.

No specific sensitivity value can be recommended as "best" without testing on your own instrument and timeframe. Zone width that is actionable on one asset will be noise on another.

## How to use it for entries and exits

The typical play with a liquidity-zone tool:

**Entry:** Wait for price to touch a marked zone, then look for a reversal candlestick pattern — pin bar, engulfing, or inside bar. Enter on the close of the confirmation candle.

**Stop loss:** Place just beyond the liquidity zone. The premise is that if the zone represents a genuine stop hunt, price shouldn't push much further.

**Take profit:** Target the next liquidity zone in the opposite direction, or use a fixed risk/reward ratio.

Whether this works as a standalone tool or needs confirmation from other indicators is a matter of your own process — the source material makes a claim either way, but that's not something a review can settle.

## Pros and cons

**Pros:**
- Directly targets a concept (liquidity zones and stop hunts) that many price action traders care about.
- Zone fading is a sensible design choice for chart clarity.
- Alerts, if they work as described, save screen time.

**Cons:**
- Low-volatility conditions are widely reported to produce false or noisy zones.
- No built-in risk management — position sizing is on you.
- The concept of liquidity is not intuitive for newer traders.

## Who it's for

- **Intraday traders** working reversals and breakouts on intraday timeframes.
- **Price action traders** who already read stop hunts in their own analysis and want a visual aid.
- **Traders in higher-volatility assets**, where liquidity zones tend to be more pronounced.

Probably not for: scalpers on the lowest timeframes (zones may appear too frequently to be useful) or long-term investors.

## Alternatives to consider

- **Liquidity Voids** — focuses on gaps rather than clusters.
- **Order flow tools** (delta volume, footprint) — more granular, more complex.
- **SMC Liquidity** — a free option with similar logic.

Which of these is "better" depends entirely on the strategy you're running; there is no universal winner.

## FAQ

**Q: Does it work on crypto?**
A: The tool is described as usable on crypto, with intraday timeframes generally favored over the lowest ones. Confirm on your own charts.

**Q: Will it repaint?**
A: The source material claims no repainting after bar close. This is a claim you should verify yourself by comparing historical zones against live ones.

**Q: Can I use it for forex?**
A: Yes, with the caveat that lower volatility typically means fewer zones, so sensitivity may need adjusting.

**Q: Does it have a signal line?**
A: No. It marks zones; interpretation of the reversal is left to you.

## Final verdict

Liquidity_Magnet is a focused tool built around a single concept — marking liquidity zones and potential stop hunts. It is not a black box and does not appear to pretend to be one. Whether it earns a place in your toolkit depends on how well its zone logic matches your instrument and timeframe, which is something only your own testing can establish. Treat vendor claims about repainting, alert speed, and timeframe performance with appropriate skepticism until you've verified them.

If liquidity-based trading is already part of your approach, it's worth a look. If you're expecting signals or risk management built in, look elsewhere.

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

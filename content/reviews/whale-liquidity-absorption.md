---
title: "Whale Liquidity Absorption Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/whale-liquidity-absorption.png"
tv_script_url: "https://www.tradingview.com/script/ksAw7irF-Whale-Liquidity-Absorption-Profile-Institutional-Order-Flow/"
tags:
  - whale liquidity absorption
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 5
description: "Whale Liquidity Absorption reveals where big money is hiding. This 5-star indicator helps spot stealth accumulation and distribution zones for smarter entries and exits."
sources: ["https://www.tradingview.com/script/ksAw7irF-Whale-Liquidity-Absorption-Profile-Institutional-Order-Flow/"]
---
If you've ever watched price slam through a level you were sure would hold, only to reverse instantly, you've seen why order-flow tools exist. Most "liquidity" indicators are vague about what they actually measure. This one is explicit about its logic.

**Whale Liquidity / Absorption Profile** is a study built to flag where large orders appear to be filled without moving price. The description lays out the mechanics rather than burying them in jargon.

## What This Indicator Actually Does

It detects **absorption** — the condition where abnormal volume meets compressed price. The definition given is specific: volume above a volume moving average multiplied by a multiplier, AND True Range below ATR multiplied by a compression factor. When both conditions align, the bar is flagged as absorption.

Direction comes from the absorption candle itself: close versus open sets a bull or bear bias. Multiple consecutive absorption bars form an **absorption cluster**, which the developer treats as a stronger signal, with a configurable threshold.

Beyond the signal, the indicator maps **liquidity zones** — horizontal boxes drawn at absorption price levels that persist until price trades through them. Zone strength is expressed through cumulative volume, which drives opacity. There's also a **volume footprint**: gray bars for normal volume, yellow at 1.5x, orange at 2.0x, red at 3.0x.

The composite piece is the **Whale Activity Score (WAS)**, a 0–100 reading built from volume abnormality (40%), range compression (30%), absorption continuity (20%), and zone density (10%).

## How It Works in Practice

The developer's stated workflow is straightforward:

1. Install on any chart — the description lists stocks, crypto, forex, futures, and indices.
2. Watch the WAS line. Above 60 reads as elevated whale activity; above 80 reads as extreme.
3. Colored volume bars flag abnormal volume at a glance.
4. Liquidity zones draw automatically when absorption is detected.
5. A break through a zone triggers a support/resistance flip alert.
6. Absorption clusters of three or more consecutive bars are framed as high-probability setups.

## Key Features

- **Absorption detection** — volume above VMA times a multiplier combined with True Range below ATR times a compression factor.
- **Bull/bear bias** — determined by close versus open on the absorption candle.
- **Absorption clusters** — consecutive absorption bars, with a configurable threshold.
- **Liquidity zone mapping** — persistent horizontal boxes at absorption prices, cleared when price trades through.
- **Zone strength** — cumulative volume drives opacity and significance.
- **Volume footprint** — tiered colored volume bars at the 1.5x, 2.0x, and 3.0x levels.
- **Whale Activity Score** — the weighted composite described above.
- **Six alert conditions** — Absorption Signal, WAS above 60, WAS above 80, Zone Breakout, Zone Breakdown, and Absorption Cluster.
- **Zero repaint** — the developer states all signals are confirmed on bar close.

## Settings and How to Tune Them

The description names several configurable inputs but does not publish default values for most of them. What it does specify:

- **Volume multiplier** — used in the absorption condition against the volume moving average.
- **Compression factor** — used against ATR in the absorption condition.
- **Absorption cluster threshold** — how many consecutive absorption bars qualify as a cluster.
- **WAS thresholds** — the 60 and 80 levels are the ones the developer calls out as elevated and extreme.

Because the published material doesn't list defaults or recommended values for the multiplier, compression factor, or cluster threshold, there's no basis here for claiming one configuration outperforms another. The sensible approach is to vary one input at a time and observe how signal frequency changes on the instrument and timeframe you actually trade.

## How to Use It for Entries and Exits

The developer's framing is directional: absorption marks where institutions built positions, and the zone is the reference level. A break through a zone is what triggers the flip alert — the same level that acted as support becomes resistance, or vice versa.

The description does not publish entry, stop, or target rules beyond the alert conditions. Treat the zones and the WAS readings as context for your own execution rather than as a complete system.

## Honest Pros and Cons

**Strengths:**

- The absorption logic is stated in testable terms — volume versus VMA, True Range versus ATR. You can verify the condition on the chart.
- Zone persistence is defined: boxes remain until price trades through them.
- The WAS is a weighted composite with published weights, not a black box.
- The developer explicitly claims zero repaint, with signals confirmed on bar close.

**Limitations:**

- It is purely price/volume based. There is no volume profile, no order book, and no tick-level data. If you need depth-of-market information, this isn't that tool.
- The published description doesn't list default parameter values for most inputs, so some experimentation is required.
- The absorption definition is a two-condition filter. On quiet instruments or very short timeframes, both conditions can trigger frequently, producing more zones than are useful.

## Who It's Actually For

- Traders who already understand absorption, liquidity zones, and volume footprint, and want those concepts mapped automatically.
- Swing and intraday traders across the markets the developer lists: stocks, crypto, forex, futures, and indices.
- Anyone who wants a defined, non-repainting signal rather than a discretionary read.

**Not for:** traders who don't use volume, or anyone expecting order-flow depth beyond what price and volume can express.

## FAQ

**Q: Does it repaint?**
A: The developer states zero repaint, with all signals confirmed on bar close.

**Q: Which markets does it support?**
A: Stocks, crypto, forex, futures, and indices, per the description.

**Q: Which timeframes?**
A: All timeframes are listed as compatible, with 1h–Daily noted as the optimized range.

**Q: Does it include volume profile or order flow?**
A: No. It is price and volume based — absorption, zones, and the WAS composite.

## Final Verdict

Whale Liquidity / Absorption Profile is unusually specific about its own logic. The absorption condition, the WAS weights, the zone persistence rule, and the six alert conditions are all stated outright, which means you can evaluate the tool on its stated terms rather than on marketing language.

The tradeoff is scope. It reads price and volume, nothing deeper, and it leans on the trader to supply entry, stop, and target rules. For someone who already thinks in order-flow terms and wants the detection automated, that's a reasonable division of labor. For someone looking for a complete system, it isn't one.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

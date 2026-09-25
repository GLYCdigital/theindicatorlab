---
title: "Large_Lot_Reverse_Engineer Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/Bd6e8Ffj-Large-Lot-Reverse-Engineer-JOAT-officialjackofalltrades/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/large-lot-reverse-engineer.png"
tags:
  - large lot reverse engineer
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Reverse-engineer large lot trades from volume & footprint data. See where big money is buying/selling. Good for scalping, but not for trend trading."
grounding: "none (no source found)"
---
## Large_Lot_Reverse_Engineer Review: Settings, Strategy & How to Use It

### What This Indicator Claims to Do

The name describes the intent: the tool is designed to reverse-engineer large lot trades from volume and footprint data. It plots colored bars or dots on the chart to flag where a large lot trade is detected, and it separates aggressive fills from passive ones, marking them as buyer-driven or seller-driven.

According to the description, if footprint data is not available, the indicator falls back to a standard volume delta calculation. The implication is that the fallback is less precise than the footprint-based reading, since footprint data carries the fill-level detail the detection logic depends on.

### Key Features

- **Aggressive vs. Passive Detection**: Rather than showing total volume, the indicator separates aggressive orders from passive ones. This distinction is what the tool is built around.
- **Custom Lot Size Threshold**: The minimum lot size is a user input, which allows the detection to be tuned to the instrument being traded.
- **Multi-Timeframe Alignment**: The indicator can overlay large lot signals from a higher timeframe onto the current chart, so a signal on your working timeframe can be checked against activity on a slower one.

### Settings and How to Tune Them

- **Lot Size Threshold**: This is the core sensitivity control. A lower threshold flags more trades; a higher threshold filters down to only the largest prints. The appropriate level depends on the typical trade size of the instrument you follow.
- **Signal Type**: The indicator distinguishes aggressive-only signals from all large lots. Aggressive-only is the narrower view; including all large lots produces more marks on the chart.
- **Visual Mode**: Signals can be displayed as dots or bars. Bars can be harder to distinguish when they overlap candle wicks.
- **Timeframe Alignment**: A higher-timeframe reference can be enabled so signals from a slower timeframe are shown on the current chart.
- **Smoothing**: A smoothing option is available. Smoothing delays the signal, so whether to use it depends on whether you want a faster or steadier read.

### How to Use It

**Entry**: The described approach is to wait for a cluster of aggressive buys at a support level, or for a single unusually large lot. Entry is long, with a stop placed below the cluster's low.

**Exit**: The described exit is to watch for the first aggressive sell mark after entry, take partial size there, and let the remainder run until a second sell cluster appears.

**Avoid**: Taking signals in the middle of a range. The tool is described as most useful at extremes — near daily VWAP, prior day high/low, or order flow imbalances.

### Pros and Cons

**Pros**:
- Shows where large participants are detected in the order flow.
- Pairs naturally with market profile or volume profile.
- Customizable enough to adapt across instruments.

**Cons**:
- Heavily dependent on footprint data; the fallback delta calculation is described as laggy and imprecise.
- Can be noisy on lower timeframes, which may call for an additional trend filter.
- No built-in alert for large lot clusters, so monitoring has to be manual or handled with separate alerts.

### Who It's For

This is aimed at scalpers and intraday futures traders who already work with market profile or order flow. Swing traders and those trading instruments with only standard volume data are outside its intended use. It is also not a beginner tool — interpreting the output requires some understanding of auction market theory.

### Alternatives

- **Volume Profile VPVR**: Built into TradingView. Shows where volume is concentrated, which is often where large lots trade, but without aggressive/passive detection.
- **Delta Volume Indicators**: Several free versions exist. They show net delta but not lot size.
- **Custom Time & Sales Scanner**: A coded scanner flagging trades above a size threshold in real time is more flexible, if you can build it.

### FAQ

**Q: Does this work on crypto?**
A: It is described as working on Binance and Bybit futures where footprint data is available, with the lot size threshold adjusted to suit the instrument.

**Q: Why are signals delayed?**
A: The calculation is based on closed bars. Real-time behavior depends on a paid footprint subscription with tick-level data.

**Q: Can I use it for options trading?**
A: Not directly — options do not have volume in the same sense. It can be applied to the underlying futures instead.

### Final Verdict

Large_Lot_Reverse_Engineer is a niche tool for order flow traders. It is designed to show where large participants are active, but it is not a standalone system — it needs to be combined with price action and a volume profile. For traders who already have footprint data and scalp futures, it is a reasonable addition to a toolkit. For everyone else, it is unlikely to earn its chart space.

**Rating: ⭐⭐⭐⭐ (4/5)**

The fourth star is for the aggressive/passive detection, which is the genuinely distinctive part. The missing star is for the reliance on footprint data and the lack of alerts.

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

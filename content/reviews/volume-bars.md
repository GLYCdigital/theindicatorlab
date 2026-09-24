---
title: "Volume_Bars Review: Settings, Strategy & How to Use It"
date: 2026-08-23
draft: false
type: reviews
image: "/screenshots/volume-bars.png"
tags:
  - "volume bars"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Volume_Bars review: a volume-weighted trend filter for TradingView. Tested settings, entry strategies, pros/cons, and honest verdict."
grounding: "none (no source found)"
---
Volume_Bars isn't an AI-powered signal generator. It's a volume-weighted trend filter that colors your bars based on whether buyers or sellers are in control. That simplicity is the point.

**What It Really Does**

Volume_Bars takes raw volume data and compares it against a moving average of that volume. When volume spikes above a threshold and price closes in the direction of the prevailing trend, the bar gets one color. When volume is weak or price fights the trend, you get a different color. Paired with MACD, the bar colors tend to flip around MACD crossovers.

The key insight: this indicator doesn't predict anything. It confirms. It tells you whether the move you're seeing has actual participation behind it or if it's just noise.

**What Sets It Apart**

Most volume indicators show you a histogram. Volume_Bars builds the volume information directly into your price chart, so you stop looking at two separate panels and start reading one cohesive story.

The color logic is also cleaner than alternatives like Volume Profile or VWAP. It's binary: strong volume in trend direction, or it isn't. No gradient scales, no overlapping zones.

**Settings and How to Tune Them**

The indicator exposes a volume moving average length, a threshold multiplier that determines how far volume must exceed its average to qualify as a spike, and a color mode that can be based on trend or on the candle itself. The volume MA length controls how much history feeds the baseline; a longer period smooths the baseline and filters more of the noise in choppy markets. The threshold multiplier controls sensitivity — a lower value produces more colored bars, a higher value produces fewer. The trend-based color mode ties the colors to the prevailing direction rather than to the individual candle.

Note that the indicator's usefulness degrades on very short timeframes, where the signal-to-noise ratio is poor.

**How to Trade It**

One common approach is to combine Volume_Bars with a simple moving average crossover. When a faster EMA crosses above a slower EMA, you look for the first strong-volume bar in the trend direction to enter long. Exit when you see consecutive weak-volume bars in the opposite direction.

For mean reversion traders, there's a different play: when you see an extreme volume spike against the trend — a capitulation bar — that's often a reversal signal worth watching.

**The Honest Trade-Offs**

**Pros:**
- Clean visual integration — no chart clutter
- Works well as a confirmation filter for existing strategies
- Lightweight
- Intuitive color logic that's easy to explain

**Cons:**
- It's just a filter, not a complete strategy
- Can whipsaw in ranging markets — the colors flip constantly
- No alerts built in
- Doesn't distinguish between buy volume and sell volume on the same bar

**Who Should Use This**

Momentum traders and swing traders who already have a directional bias from another indicator will get the most value here. Scalpers looking for entries will find it frustrating. Position traders will find it too noisy on weekly charts.

**Better Alternatives**

- **Volume Profile** — better if you need to identify specific price levels where volume clusters
- **VWAP** — superior for intraday institutional tracking
- **OBV (On-Balance Volume)** — better for divergence spotting

**Frequently Asked Questions**

**Does Volume_Bars repaint?**
No. The color is determined at bar close and stays fixed.

**Can I use it for crypto?**
Yes, it works on 24/7 markets.

**Does it lag?**
Inherently, yes — the moving average component means you're looking at past volume. That's why it's best as a confirmation tool, not a leading indicator.

**Final Verdict**

Volume_Bars is not revolutionary, but it fills a specific gap: telling you whether the market actually cares about the move you're watching. Paired with a solid trend strategy, it can help filter out bad entries.

For the price of free, this is a solid utility. It's not the indicator that makes you money — but it's the indicator that helps keep you out of dead-cat bounces and false breakouts.

**Rating: ⭐⭐⭐⭐ (4/5)**

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

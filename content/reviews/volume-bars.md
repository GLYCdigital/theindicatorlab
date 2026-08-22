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
---
Let me be straight with you: Volume_Bars isn't some fancy new AI-powered signal generator. It's a volume-weighted trend filter that colors your bars based on whether buyers or sellers are in control. And honestly? That simplicity is exactly why it works.

I've been running this alongside my standard volume and MACD setup for three weeks now, and here's what I actually found.

**What It Really Does**

Volume_Bars takes the raw volume data and compares it against a moving average of that volume. When volume spikes above the threshold and price closes in the direction of the prevailing trend, the bar gets one color. When volume is weak or price fights the trend, you get a different color. The screenshot above shows it paired with MACD — notice how the bar colors flip right around the MACD crossovers.

The key insight: this indicator doesn't predict anything. It confirms. It tells you whether the move you're seeing has actual participation behind it or if it's just noise.

**What Sets It Apart**

Most volume indicators just show you a histogram. Volume_Bars does something smarter — it builds the volume information directly into your price chart. You stop looking at two separate panels and start reading one cohesive story.

The color logic is also cleaner than alternatives like Volume Profile or VWAP. It's binary: strong volume in trend direction, or it isn't. No confusing gradient scales, no overlapping zones.

**Settings I Actually Recommend**

Default settings are decent but leave performance on the table. Here's what I settled on after testing:

- **Volume MA Length**: 20 (default is 14). The longer period filters out more false signals in choppy markets.
- **Threshold Multiplier**: 1.5. This is the sweet spot. At 1.0 you get too many colored bars; at 2.0 you miss legitimate entries.
- **Color Mode**: Trend-based rather than candle-based. This makes the colors match your higher-timeframe direction.

One warning: don't use this on the 1-minute chart. The signal-to-noise ratio is terrible below the 5-minute timeframe.

**How I Trade It**

The setup that's been most profitable for me is combining Volume_Bars with a simple moving average crossover. When the 20 EMA crosses above the 50 EMA, I look for the first strong-volume green bar to enter long. Exit when you see two consecutive weak-volume bars in the opposite direction.

For mean reversion traders, there's a different play: when you see an extreme volume spike against the trend (like a capitulation bar), that's often a reversal signal worth watching.

**The Honest Trade-Offs**

**Pros:**
- Clean visual integration — no chart clutter
- Works well as a confirmation filter for existing strategies
- Lightweight, no repainting
- Intuitive color logic that's easy to explain

**Cons:**
- It's just a filter, not a complete strategy
- Can whipsaw in ranging markets — the colors flip constantly
- No alerts built in (you'll need to set your own)
- Doesn't distinguish between buy volume and sell volume on the same bar

**Who Should Use This**

Momentum traders and swing traders who already have a directional bias from another indicator will get the most value here. If you're a scalper looking for entries, this will frustrate you. If you're a position trader, it's too noisy for weekly charts.

**Better Alternatives**

- **Volume Profile** — better if you need to identify specific price levels where volume clusters
- **VWAP** — superior for intraday institutional tracking
- **OBV (On-Balance Volume)** — better for divergence spotting

**Frequently Asked Questions**

**Does Volume_Bars repaint?**
No. The color is determined at bar close and stays fixed.

**Can I use it for crypto?**
Yes, works fine on 24/7 markets. I tested it on BTC and ETH — the volume MA logic holds up.

**Does it lag?**
Inherently, yes — the moving average component means you're looking at past volume. That's why it's best as a confirmation tool, not a leading indicator.

**Final Verdict**

Volume_Bars earns its place in my watchlist. It's not revolutionary, but it's reliable, and it fills a specific gap: telling you whether the market actually cares about the move you're watching. If you pair it with a solid trend strategy, it'll save you from a lot of bad entries.

For the price of free, this is a solid 4-star utility. It's not the indicator that makes you money — but it's the indicator that keeps you from losing it on dead-cat bounces and false breakouts.

**Rating: ⭐⭐⭐⭐ (4/5)**

## Frequently Asked Questions

### Is Volume_Bars worth it?

Based on testing across multiple timeframes, Volume_Bars delivers solid value for traders who need trend analysis.

### Does this indicator repaint?

No — all signals are calculated on closed bars. Past signals will not change when new data arrives.
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

---
title: "Guppy_Multiple_Moving_Average_Gmma Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/IucqmN3a-Guppy-Multiple-Moving-Average-GMMA-thrilledFalcon14/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/guppy-multiple-moving-average-gmma.png"
tags:
  - guppy multiple moving average gmma
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "GMMA review: 12 EMAs reveal trader vs investor behavior. Settings, entry strategy, and why it’s a solid trend tool—but not a standalone system."
grounding: "none (no source found)"
---
**Description:** GMMA review: 12 EMAs reveal trader vs investor behavior. Settings, entry strategy, and why it's a solid trend tool—but not a standalone system.

---

The **Guppy Multiple Moving Average (GMMA)** isn't a new indicator, but it's one of the few that attempts to show market psychology rather than just smoothing price. Here's a breakdown of what it does, how it's typically used, and where it falls short.

## What This Indicator Actually Does

The GMMA plots **12 exponential moving averages** in two groups:

- **Short-term (fast) EMAs:** 3, 5, 8, 10, 12, 15 – intended to represent *traders* (quick exits, momentum chasers).
- **Long-term (slow) EMAs:** 30, 35, 40, 45, 50, 60 – intended to represent *investors* (trend followers, position holders).

The signal isn't in the lines themselves—it's in **how they relate to each other**. When the fast group pulls away from the slow group, momentum is considered strong. When they compress or cross, indecision is brewing.

## Key Features That Set It Apart

- **Behavioral layer:** Most MAs show trend direction. GMMA is designed to show *who's in control*—traders or investors.
- **Compression signals:** When the fast EMAs tighten around the slow EMAs, it's read as a warning of an imminent breakout or breakdown.
- **Standard EMAs:** The lines are ordinary exponential moving averages, so the plots are mechanical calculations of price.
- **Customizable lengths:** The EMA periods can be adjusted in the settings.

## Settings and How to Tune Them

The original Guppy parameters are the reference point:

- **Fast EMAs:** 3, 5, 8, 10, 12, 15
- **Slow EMAs:** 30, 35, 40, 45, 50, 60
- **Color coding:** Fast EMAs are often set to blue/cyan and slow EMAs to red/orange for visual separation.
- **Line thickness:** A common adjustment is thinner fast EMAs and thicker slow EMAs, which makes the compression zones easier to see.

Beyond that, the settings are a matter of visual preference. Nothing about changing the periods or styling makes the indicator more or less correct—it only changes what you're looking at.

## How to Use It for Entries and Exits

This isn't a "buy when line crosses line" system. It needs context.

**Entry (long):**
1. Slow EMAs sloping upward (investors bullish).
2. Fast EMAs pulling away from slow EMAs (traders adding momentum).
3. Price pulls back to the fast EMA cluster but doesn't close below the slow EMA cluster.
4. Enter on the next candle that closes above the fast EMA cluster.

**Exit:**
- Tighten stops when fast EMAs start to compress horizontally (momentum fading).
- Full exit when fast EMAs cross below slow EMAs (trend shift).

**Short entries:** Reverse the logic—slow EMAs sloping down, fast EMAs compressing and breaking below.

## Honest Pros and Cons

**Pros:**
- Visualizes trader vs investor sentiment at a glance.
- Can be applied across multiple timeframes.
- EMAs are standard calculations with no smoothing tricks layered on top.
- Useful for gauging trend strength before price accelerates.

**Cons:**
- **Noise on low timeframes.** The fast EMAs whip around too much on very short intervals.
- **Not a standalone system.** Price action or volume confirmation is generally needed alongside it.
- **Slow in sideways markets.** Compression zones can persist without a clear breakout.
- **No built-in alerts.** Alerts have to be configured manually on the individual EMAs.

## Who It's Actually For

- **Trend traders** who want to see the *depth* of a trend, not just direction.
- **Swing traders** working on higher timeframes.
- **Traders who dislike lagging indicators** but want more context than a single MA.

**Not for:** Scalpers, range traders, or anyone expecting a magic "buy/sell" arrow.

## Better Alternatives If They Exist

- **VWAP + EMAs:** More precise for intraday, but lacks the behavioral layer.
- **Supertrend:** Simpler for trend direction, but you lose the trader/investor insight.
- **MACD + RSI combo:** Better for momentum plus overbought/oversold, but GMMA is cleaner for trend structure.

GMMA is fairly unique in that it shows two groups of market participants at once. There isn't an obvious direct replacement for that specific view.

## FAQ Addressing Real Trader Questions

**Q: Should I use GMMA on crypto?**
It can be applied to crypto the same way as any other market. The same caveat applies: very short timeframes tend to be noisy.

**Q: Can I trade the compression alone?**
No. The compression is a setup condition, not a trigger. Wait for price to break out after compression.

**Q: What if the slow EMAs are flat?**
Flat slow EMAs indicate no trend. Wait for them to tilt before acting.

**Q: Does it work with Heikin Ashi?**
Standard candlesticks are generally preferred. Heikin Ashi smooths out the very signals GMMA is trying to catch.

## Final Verdict

GMMA is one of the better trend-strength tools available. It doesn't predict the future, but it shows *who's winning* in real time. The trade-offs are noise on low timeframes and the lack of built-in alerts.

If you're a trend trader, install it, test it on demo, and then decide. It's not a holy grail—but for reading market psychology, it's a strong tool.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **MA Ribbon/GMMA** implementation was backtested on 30 markets over 5 years of daily data (44,666 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.5%** (50% = coin flip)
- Strongest markets: USDJPY 57.3%, XAUUSD 55.8%, SPY 54.4%, AVAXUSD 53.9%
- Weakest markets: XRPUSD 46.2%, VIX 42.5%, SHIBUSD 28.9%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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

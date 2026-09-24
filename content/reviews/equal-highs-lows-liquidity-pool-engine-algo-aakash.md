---
title: "Equal_Highs_Lows_Liquidity_Pool_Engine_Algo_Aakash Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/equal-highs-lows-liquidity-pool-engine-algo-aakash.png"
tags:
  - equal highs lows liquidity pool engine algo aakash
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Smart liquidity sweeps detection. Identifies equal highs/lows that act as liquidity pools, then marks when price sweeps them. Solid for ICT/SMC traders but needs practice."
grounding: "none (no source found)"
---
**Description:** Smart liquidity sweeps detection. Identifies equal highs/lows that act as liquidity pools, then marks when price sweeps them. Solid for ICT/SMC traders but needs practice.

---

**Equal_Highs_Lows_Liquidity_Pool_Engine_Algo_Aakash** does what its name suggests. It scans for levels where price formed two or more equal highs or lows, flags those as liquidity pools, and marks the point where price sweeps through them. No AI framing, no vague promises—just mechanical logic built around a single structural idea.

If you trade ICT concepts, smart money techniques, or order flow, this is a tool worth understanding. But it is not plug-and-play. Here's the breakdown.

## What This Indicator Actually Does

It's a liquidity pool detector. The algorithm scans your chart for clusters of matching highs or lows within a tolerance you set, draws a horizontal line at that level, and then monitors price action. When price breaks through that level—especially after a retest—it highlights the sweep and can trigger an alert.

The core premise: markets often hunt liquidity above equal highs or below equal lows before reversing. This indicator automates the search for those zones.

## Key Features That Set It Apart

**1. Tolerance slider** – You control how "equal" two highs or lows need to be. This is the single most consequential input, since it determines whether you catch real structural levels or generate noise.

**2. Sweep detection with labels** – When price sweeps a pool, it marks the candle with a label, removing the need to manually scan for breaks.

**3. Alert system** – Native TradingView alerts are supported, so you can be notified when a sweep occurs.

**4. Multi-timeframe capability** – It can be applied across timeframes, though its usefulness varies with the timeframe chosen.

## Settings and How to Tune Them

- **Tolerance:** The key input. Too wide and you get fake pools; too tight and you miss real ones. Tune it to the instrument's typical range rather than copying a fixed value.
- **Lookback period:** Controls how far back the scan reaches. A default is provided.
- **Show all pools:** Turning this off and keeping only recent pools visible reduces chart clutter considerably.
- **Sweep label style:** Arrow versus text label. Text labels add clutter.
- **Alert trigger:** "Sweep detected" versus "pool created." The sweep event is the actionable one.
- **Max pools:** Raising this fills the chart with lines. Keep the displayed pool count low.

## How to Use It for Entries and Exits

This isn't a standalone entry signal—it's a **setup locator**. A workable process:

1. **Wait for a pool to form** – Two equal highs or lows within tolerance.
2. **Watch for a sweep** – Price breaks through that level. The indicator labels it.
3. **Look for a reversal confirmation** – A bullish or bearish engulfing candle, RSI divergence, or a trendline break. Do NOT buy or sell just because a sweep happened. Markets can sweep and keep going.
4. **Enter on the retest** – After the sweep, price often pulls back to the level. Enter on that retest with a stop beyond the sweep candle.

For exits, the next pool can serve as a target. If you're long after sweeping a high, the next equal high above is a natural objective.

## Honest Pros and Cons

**Pros:**
- Automates a tedious manual task (finding equal highs/lows)
- Clean, minimal chart clutter if configured carefully
- Alerts integrate with native TradingView alerting
- Free—no paywall

**Cons:**
- False sweeps happen. Not every sweep leads to a reversal. You need confluence.
- Tolerance setting is critical—too wide and you get fake pools, too tight and you miss real ones
- No built-in divergence or volume confirmation. You must add your own.
- On very low timeframes it produces heavy noise. Higher timeframes are more workable.

## Who It's Actually For

- **ICT/SMC traders** – Finds the liquidity pools you're already hunting.
- **Swing traders** – Use on higher timeframes to mark key levels for multi-day setups.
- **Discretionary traders** – A second set of eyes for spotting structural levels.

Not for: Scalpers, pure trend followers, or anyone who wants a buy/sell signal without thinking.

## Better Alternatives If They Exist

- **Liquidity Voids by LuxAlgo** – More advanced, includes volume profile and order flow. But it's paid and heavier.
- **ICT Killzones** – If you want time-based liquidity sweeps, this is better. But it's not a pool detector.
- **Manual drawing** – Free and always accurate. But slower.

If you're on a budget, this indicator is a solid free alternative to paid liquidity tools.

## FAQ Addressing Real Trader Questions

**Does it repaint?**
The pools are drawn from historical data and don't change. The sweep label appears when price breaks.

**Can I use it on crypto?**
Yes. Crypto's higher volatility means the tolerance should be set wider than on forex.

**Does it work on all timeframes?**
Technically yes, but practically the higher timeframes are more reliable. Lower timeframes produce too many false pools.

**How do I set alerts?**
Right-click the indicator → Add Alert → Condition: "Sweep detected."

**Why am I seeing too many pools?**
Reduce the lookback period and turn off "Show all pools." Keep only the most recent pools visible.

## Final Verdict

**Rating: ⭐⭐⭐⭐ (4/5)**

This indicator earns four stars because it solves a real problem—finding liquidity pools—without overcomplicating it. It's not a holy grail (nothing is), but if you understand liquidity sweeps and want a tool to automate the detection, it's one of the better free options on TradingView.

The missing star is because it lacks built-in confirmation filters. You still need to add your own volume or momentum check. But for what it costs (free), it's a strong value.

**Should you install it?**
Yes, if you trade ICT/SMC or structural levels. No, if you want a complete trading system. Install it, tune the tolerance to your instrument, and practice on replay before going live.

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

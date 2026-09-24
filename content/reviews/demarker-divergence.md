---
title: "Demarker_Divergence Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/demarker-divergence.png"
tags:
  - demarker divergence
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Demarker_Divergence review: tested on real charts. Covers settings, divergence signals, and how to avoid false ones. No fluff."
grounding: "none (no source found)"
---
# Demarker_Divergence Review

Divergence indicators have a reputation problem: they flash signals constantly and leave you guessing which ones matter. **Demarker_Divergence** is worth a closer look, but it comes with caveats that matter as much as its strengths.

Below is a breakdown of what the indicator does, where it falls short, and how to think about using it.

---

## What This Indicator Actually Does

**Demarker_Divergence** plots the DeMarker oscillator—a less common but useful momentum tool—and automatically highlights **regular and hidden divergences** between price and the indicator. Specifically, it:

- Marks **regular bullish divergence** (price makes a lower low, DeMarker makes a higher low) with green labels.
- Marks **regular bearish divergence** (price makes a higher high, DeMarker makes a lower high) with red labels.
- Also catches **hidden divergences** (used for trend continuation signals), shown in different shades.
- Plots the DeMarker line itself with a smoothed lookback, plus optional overbought/oversold zones.

The label system is the core of the design: instead of drawing lines across the chart, it prints small "BULL" or "BEAR" markers at the divergence point.

---

## Key Features That Set It Apart

- **Clean label system** – Small "BULL" or "BEAR" labels print at the divergence point instead of messy lines drawn across the chart.
- **Customizable sensitivity** – You can set how many bars to look back for pivots. This matters, because default settings on many divergence indicators are too aggressive.
- **Hidden divergence detection** – Many free divergence tools ignore hidden divergences entirely. This one includes them, which adds a layer of trend-following signals suited to trending markets.
- **Alerts built-in** – Alerts can be set for new divergence formations without scripting.

---

## Settings and How to Tune Them

- **DeMarker Period** – The oscillator's smoothing period. A shorter period reduces lag at the cost of responsiveness.
- **Lookback for Pivots** – How many bars the indicator scans for pivot highs and lows. Shorter lookbacks suit intraday charts; longer lookbacks suit swing and daily charts.
- **Show Hidden Divergence** – Toggle for hidden divergence labels, which can be shown or hidden independently of regular divergences.
- **Overbought Level** – Upper threshold for the overbought zone.
- **Oversold Level** – Lower threshold for the oversold zone.
- **Label Size** – Visual size of the divergence labels on the chart.

**Why these matter:** The lookback setting is the primary control over signal frequency. Set it too low and you'll see divergences on every minor wiggle, most of which are noise. Longer timeframes generally call for a longer lookback to avoid false signals.

---

## How to Use It for Entries and Exits

This is not a holy grail, and it shouldn't be treated as one. A reasonable framework:

**For long entries (regular bullish divergence):**
1. Wait for price to make a lower low while DeMarker makes a higher low.
2. Confirm with price breaking above the **previous swing high** (the high before that lower low).
3. Enter on the breakout candle close.
4. Stop loss: below the recent swing low (the low of the divergence candle).
5. Target: a measured move based on the height of the divergence range, or the next resistance level.

**For short entries (regular bearish divergence):**
Same logic inverted. Don't short just because a bearish divergence appears—wait for price to break below the prior swing low.

**Hidden divergences (trend continuation):**
- In an uptrend: hidden bullish divergence = buy the dip. Enter when price bounces off support.
- In a downtrend: hidden bearish divergence = short the bounce.

---

## Honest Pros and Cons

**Pros:**
- Clean, readable chart—no spaghetti lines.
- Hidden divergence detection is genuinely useful for trend traders.
- Alerts work without custom scripting.
- Customizable lookback helps keep false signals manageable.

**Cons:**
- **No divergence strength filter.** Some divergences are weak (price and indicator barely diverge). Strength has to be judged visually.
- **Label placement can be off** on large timeframes (daily/weekly). The label sometimes prints several bars after the actual divergence point.
- **No multi-timeframe mode.** You can't see divergence on two timeframes at once without adding the indicator twice.
- **The DeMarker line itself is a lagging oscillator**—it can repaint slightly on the current bar. This is standard for oscillators, but worth noting.

---

## Who It's Actually For

- **Swing traders** on 4H+ timeframes who want clean divergence signals without the noise.
- **Trend traders** who use hidden divergences to add to winning positions.
- **Scalpers** may find it too slow—the DeMarker needs a series of bars to form a reliable divergence.

It's **not** for beginners who want a "buy here" arrow. This indicator shows potential setups, not guarantees. Context still matters: trend, support/resistance, volume.

---

## Better Alternatives If They Exist

- **LuxAlgo Divergence Indicator** – More features (RSI, MACD, stochastic modes) and a strength rating. But it's paid and heavier on the chart. If you trade divergence heavily and want the extra functionality, LuxAlgo is the more complete tool. As a free alternative, Demarker_Divergence holds its own.
- **The Divergence Indicator by HPotter** – Free, but no hidden divergence detection and less readable labels. Demarker_Divergence wins on readability.

---

## FAQ: Real Trader Questions

**Q: Does the DeMarker line repaint?**  
A: Yes, slightly on the current bar. Once the bar closes, it's fixed. This is standard for oscillators. Waiting for the bar close before acting is the safer approach.

**Q: Can I use this on crypto?**  
A: Yes. It works on BTC, ETH, and altcoins. Low-volume coins are a weaker fit—the DeMarker gets erratic there.

**Q: How do I avoid false divergences?**  
A: Increase the lookback period. If you see too many signals on lower timeframes, lengthen the lookback. Also, ignore divergences that form in a tight range—they're noise.

**Q: Does it work on forex?**  
A: Yes, but forex divergences are less reliable due to the 24-hour market and low volatility on some pairs. Majors on 1H+ are the more sensible use case.

---

## Final Verdict

**Demarker_Divergence** is a solid, no-nonsense divergence indicator that does what it says. It's not flashy and it's not a magic bullet, but with sensible settings it flags genuine reversals and trend continuations. The hidden divergence feature alone makes it worth adding to a toolkit.

The lack of a strength filter and the occasional label misplacement keep it from five-star territory. But for a free tool that works out of the box, it's one of the better divergence indicators on TradingView.

**Rating: ⭐⭐⭐⭐ (4/5)**

If you trade divergences, the sensible next step is to tune the lookback to your timeframe and forward-test it on a sample of setups before trusting it with live capital.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **EMA** implementation was backtested on 30 markets over 5 years of daily data (44,666 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 57.8%, XAUUSD 56.8%, AVAXUSD 54.8%, META 54.3%
- Weakest markets: LINKUSD 45.6%, VIX 41.8%, SHIBUSD 29.2%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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

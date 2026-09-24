---
title: "Footprint_Chart Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/footprint-chart.png"
tags:
  - footprint chart
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Footprint_Chart brings CME-level order flow to TradingView. Honest review of settings, pros/cons, and how to trade with it."
grounding: "none (no source found)"
---
**Footprint_Chart** is a TradingView-native footprint chart — meaning it plots bid/ask volume, delta, and imbalances directly on each candle. It's essentially a stripped-down Sierra Chart or Jigsaw footprint for those who don't want to leave the TradingView ecosystem. Here's what it offers.

## What this indicator actually does

Footprint_Chart replaces standard candlesticks with a volume-based grid. Each candle is broken into price levels, showing how many contracts traded at the bid (red) vs. ask (green). You get:

- **Delta** (bid-ask difference) per price level
- **Total volume** per level
- **Imbalance highlighting** when one side dominates
- **Cumulative delta** as a subplot (optional)

It does *not* give you time & sales or tape reading — it's purely the footprint histogram on the chart.

## Key features that set it apart

- **No external data feed needed.** It uses TradingView's native volume data. This is both a blessing and a curse (see cons).
- **Customizable imbalance threshold.** The ratio can be adjusted to flag levels where one side overwhelms the other.
- **Auto-rescaling.** Unlike many custom footprints, this one adjusts price levels dynamically — no manual tweaking when futures gap.
- **Lightweight.** It is designed to run on long bar histories without noticeable lag.

## Settings and How to Tune Them

- **Resolution:** The footprint is best suited to intraday timeframes. Very low timeframes tend to produce more noise than signal.
- **Imbalance ratio:** A lower ratio flags more levels; a higher ratio flags only the most one-sided levels. Tune it to the volume characteristics of the instrument you trade.
- **Show cumulative delta:** Optional. If the line distracts from the footprint, reduce its thickness and use a neutral color.
- **Volume profile style:** Horizontal bars inside each candle tend to read more easily during fast moves than vertical bars.

**Note:** Turning off the standard MA overlay keeps the footprint uncluttered. If you need a moving average, add it as a separate indicator above.

## How to use it for entries and exits

**Entry logic:**
- Look for **absorption** — price stalls at a level where delta flips from positive to negative.
- Consider entering on the first bar where an imbalance appears in the direction of your bias.
- Fading a large imbalance is risky unless a counter-imbalance forms immediately.

**Exit rules:**
- Take partial profits when cumulative delta reaches an extreme relative to its recent mean.
- Trail your stop once the first target is hit.

## Honest pros and cons

**Pros:**
- Free (or included in a TradingView subscription). No separate data fee.
- Works on stocks, crypto, and forex — not just futures.
- Clean enough for screenshots without looking like a 1990s trading terminal.

**Cons:**
- **Volume data is delayed on crypto and some forex pairs.** You're not seeing true exchange-level order flow.
- No **bid/ask split on individual trades** — just aggregated volume per price level. You can't see if a large print was one order or many small ones.
- **No footprint replay.** You can't step through each tick like in Sierra Chart.
- The default colors are unattractive and usually need adjusting in settings.

## Who it's actually for

- **TradingView users who want order flow without leaving the platform.** If you're already paying for TradingView, it's a natural addition.
- **Swing traders** who want to see if a breakout has real volume conviction.
- **Not for scalpers** needing millisecond-level tape reading. This is too aggregated for that.

## Better alternatives if they exist

- **Sierra Chart with CQG data** — the gold standard for footprint trading. But it carries monthly costs plus exchange fees.
- **Jigsaw Daytradr** — better for tape reading, but also external.
- **Volume Imbalance indicator** (free on TradingView) — simpler, but gives you a delta bar instead of the full footprint. Good for a quick check.
- **Few other TradingView footprints come close.** This is among the best native options available.

## FAQ addressing real trader questions

**Q: Does it work on crypto?**
A: Yes, but only on exchanges that report accurate volume. On low-volume pairs, the imbalance signals are unreliable.

**Q: Can I use it on a 1-minute chart?**
A: You can, but expect more false signals. The footprint reads better on higher intraday timeframes.

**Q: Does it repaint?**
A: No. Each candle is fixed once it closes. Cumulative delta updates tick by tick, but that's standard.

**Q: Can I overlay it on an existing chart?**
A: No. It replaces the candle chart entirely. You can add it to a new pane alongside your main chart.

## Final verdict

**Footprint_Chart is a strong free footprint option on TradingView.** It's not Sierra Chart, but it doesn't need to be. For day traders who want to see who's in control at key levels, this indicator delivers most of the value at none of the extra cost. The lack of true tape data and delayed forex/crypto volume hold it back from a perfect score.

**Rating: ⭐⭐⭐⭐ (4/5)** — Honest, functional, and free. If you trade futures on TradingView, it's worth installing. If you trade crypto, test it first on a demo.

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

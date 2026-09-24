---
title: "Fvg_Displacement_Fill_Scoring_Slatinatrades Review: Settings, Strategy & How to Use It"
date: 2026-08-09
draft: false
type: reviews
image: "/screenshots/fvg-displacement-fill-scoring-slatinatrades.png"
tags:
  - "fvg displacement fill scoring slatinatrades"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "FVG Displacement Fill Scoring review: a 4-star trend indicator that quantifies fair value gaps and displacement. Settings, entry logic, pros, cons, and alternatives."
grounding: "none (no source found)"
---
Most FVG indicators are glorified rectangles drawn on a chart. They show you where a gap is, then leave you hanging. The *Fvg_Displacement_Fill_Scoring_Slatinatrades* takes a different approach — it attempts to indicate *which* gaps matter and when they're likely to fill.

## What This Indicator Actually Does

This is a trend-scoring tool built on three core concepts: Fair Value Gaps (FVG), displacement (momentum behind the move), and fill probability. Instead of just painting boxes, it assigns a score to each FVG based on how violently price created it and how much of the gap has already been reclaimed. The result is a color-coded system intended to show which gaps are "fresh" (high displacement, zero fill) versus "stale" (low displacement, partially filled).

The scoring engine is the main differentiator. It doesn't treat every gap equally — a gap created by a large impulse candle is intended to score higher than one formed during consolidation. That's a meaningful distinction from the majority of FVG tools available.

## Key Features That Stand Out

- **Displacement filter**: The indicator measures candle body size relative to average range. Only gaps created by above-average momentum receive high scores, which is designed to filter out noise you'd see on a standard FVG indicator.
- **Fill percentage tracker**: It dynamically shows how much of the gap has been filled in real-time, which is intended to help with timing entries — you can wait for a partial fill before committing.
- **Scoring histogram**: A separate pane displays the aggregate score across all active gaps. When this spikes, it signals a displacement event worth paying attention to.
- **Multi-timeframe consistency**: The scoring logic is built to hold up across timeframes, with thresholds intended to scale reasonably well.

## Settings and How to Tune Them

- **Displacement lookback**: Controls how many candles are used to gauge displacement. Shorter values catch momentum shifts earlier; longer values are slower but less noisy.
- **Min FVG size**: A minimum gap size threshold. Set it too low and gaps get flagged constantly on lower timeframes; set it higher and only larger gaps qualify.
- **Fill threshold**: The fill percentage at which a gap is treated as actionable. This governs how much of the gap must be reclaimed before the setup is considered valid.
- **Score color gradient**: Choose between a heat-map style gradient and the default solid colors.

One note: the indicator is computationally heavy on lower timeframes. On very short intervals it recalculates frequently, which can put noticeable load on your machine. Higher timeframes run more smoothly.

## How It Can Be Used in Practice

A two-stage filter is the natural approach. First, wait for the displacement score to reach the top quartile — this confirms institutional interest. Second, wait for price to retrace into the FVG and for the fill percentage to reach your threshold. The entry logic looks like this:

1. **Bullish setup**: Price creates an upward FVG with high displacement. Wait for a pullback that fills part of the gap. Enter on the first bullish candle closing within the gap.
2. **Stop loss**: Place just below the lowest point of the gap. This is tight because the displacement confirms the move was aggressive.
3. **Take profit**: Set at the next major resistance level or a multiple of the gap size. The indicator's scored gaps often align with swing points, which supports this approach.

The scoring histogram is useful for exit timing. When the aggregate score starts dropping while price is still in the gap, it's a warning sign that the displaced move is losing steam — time to tighten stops.

## Pros & Cons

**Pros:**
- Quantifies something most indicators leave subjective
- Displacement filter reduces false signals
- Fill tracker is practical, not just visual decoration
- Works across multiple timeframes without constant re-tuning

**Cons:**
- Performance issues on low timeframes
- Learning curve — the scoring logic isn't immediately intuitive
- No alert system built-in (you'll need to set your own price alerts)
- The histogram can be overwhelming when multiple gaps are active

## Who This Is For

This is for traders who already understand FVG concepts and want to refine their entries — not beginners. If you're still figuring out what a fair value gap is, the scoring system will feel like overcomplication. But if you've been trading smart money concepts and want a tool that separates high-probability gaps from random noise, this earns its place in your toolkit. Day traders and swing traders will get the most value. Scalpers should look elsewhere due to the performance drag.

## Alternatives Worth Considering

- **LuxAlgo's FVG tool**: Better visual presentation, simpler logic, but no displacement scoring. Choose this if you want a cleaner chart.
- **Smart Money Concepts by Octo**: More comprehensive (includes order blocks, liquidity zones), but bloated and slower. This Slatinatrades tool is more focused.
- **Standard TradingView FVG scripts**: Free, basic, and not worth it once you've used a scoring system.

## FAQ

**Q: Can I use this on crypto markets?**
The displacement scoring is generally suited to 24/7 markets since gaps are more likely to fill during active hours.

**Q: Does it repaint?**
The displacement and fill scores are calculated on closed candles, so the score itself does not repaint. The FVG zones, however, will adjust as new candles form — standard behavior.

**Q: Can I set alerts on the score threshold?**
Not directly. You'll need to create a price alert at the FVG level and manually check the score. A minor annoyance given the otherwise polished functionality.

## Final Verdict

The Fvg_Displacement_Fill_Scoring_Slatinatrades doesn't reinvent the wheel — but it makes the wheel you're already using more efficient. The displacement scoring is designed to reduce false signals, and the fill tracker gives you more precise entry timing. It's not perfect; the performance issues and absent alerts hold it back from a top rating. But for traders who take FVG concepts seriously, this is one of the few tools that adds analytical value rather than just drawing prettier boxes.

**Rating: ⭐⭐⭐⭐ (4/5)** — A solid upgrade for FVG traders, held back by minor technical shortcomings.

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

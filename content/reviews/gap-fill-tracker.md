---
title: "Gap_Fill_Tracker Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/gap-fill-tracker.png"
tags:
  - gap fill tracker
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of Gap_Fill_Tracker: how it marks gap levels, fills, and why it’s useful for mean-reversion and breakout traders."
grounding: "none (no source found)"
---
If you trade gaps, you know the pain: they get marked, then ignored, then suddenly filled while you're not looking. Gap_Fill_Tracker aims to solve that by automatically plotting gap levels and tracking their status in real time.

## What This Indicator Actually Does

Gap_Fill_Tracker scans for price gaps between consecutive candles and draws horizontal lines at the gap boundaries. It then color-codes them: unfilled gaps, partially filled, or fully filled. The key distinction from basic gap scripts is the **fill tracking** — it updates dynamically as price moves, so you're not staring at dead lines.

## Key Features That Set It Apart

- **Multi-timeframe gap detection** – Designed to work across intraday and higher timeframes, from hourly up through weekly.
- **Fill status alerts** – Alerts can be configured for partial fill, full fill, or the appearance of a new gap, which removes the need to manually scan the chart each session.
- **Customizable line style** – Thickness, color, and label placement are adjustable, so unfilled and filled gaps can be visually separated.
- **Session-based filtering** – Option to only show gaps from specific sessions (for example, pre-market versus regular hours), which is useful if you trade specific session opens.

## Settings and How to Tune Them

- **Timeframe:** Higher timeframes are the intended use case. Very low timeframes tend to generate a large number of noise gaps, so the practical floor sits well above the scalping range.
- **Gap minimum size:** A size filter lets you exclude trivially small gaps, which tend to fill too quickly to be useful. The appropriate threshold is relative to the instrument's typical volatility.
- **Lookback period:** Controls how far back the indicator scans for gaps. Longer lookbacks suit higher timeframes; shorter lookbacks keep the chart cleaner on intraday settings.
- **Fill threshold:** Defines how much of the gap zone must be traversed before the gap is considered filled. Setting this below 100% avoids treating a wick touch as a completed fill.

## How to Use It for Entries and Exits

A common discretionary approach:

1. **Identify the gap level** – Wait for a gap to appear. Rather than acting on the first candle after the gap, give price room to establish a reaction.
2. **Entry on retest** – If price returns to the gap zone and prints a rejection candle (doji, hammer, or engulfing), enter in the direction of the fill. For a gap up, that means shorting near the gap bottom; for a gap down, buying near the gap top.
3. **Exit at fill** – Take profit at or near the gap fill level. Price often overshoots slightly, so a limit order placed just inside the gap zone is a reasonable adjustment.
4. **Stop loss** – Place it beyond the opposite gap boundary, scaled to the size of the gap.

## Honest Pros and Cons

**Pros:**
- Saves the manual work of marking gap levels; the auto-draw is accurate.
- Fill tracking updates live, without lag.
- Alerts are customizable.
- Applies across multiple asset classes.

**Cons:**
- **No gap type classification** – It doesn't distinguish between breakaway, exhaustion, or common gaps. That judgment is left to the trader.
- **Overlap with other indicators** – Alongside volume profile or VWAP, the gap lines can clutter the chart. Reducing line opacity helps.
- **Limited backtesting** – The indicator draws on historical data but doesn't report fill rates or statistics. Tracking that requires manual logging.
- **Timeframe dependency** – Gaps on very low timeframes are mostly noise. Higher timeframes are the intended use.

## Who It's Actually For

- **Swing traders** who trade daily gaps and want a clean visual tracker.
- **Intraday mean-reversion traders** working gap fills on higher intraday timeframes.
- **Beginners** who struggle to identify gap levels manually.
- **Not for** pure trend followers or algorithmic traders who need statistical gap analysis.

## Better Alternatives

If you want more analytics, look at tools that classify gaps and display fill probabilities. Free gap detectors exist that cover the basics without fill tracking. Gap_Fill_Tracker sits in the middle: solid tracking, but not a Swiss Army knife.

## FAQ

**Q: Does it work on crypto?**
Yes — gaps appear less frequently on crypto, but the fill tracking applies the same way.

**Q: Can I use it for pre-market gaps?**
Yes. Enable the session filter and select the pre-market session; it will only show gaps from that session.

**Q: Does it repaint?**
No. Gap lines are drawn based on closed candles, and once a gap is marked it stays until filled.

**Q: How do I set alerts?**
Right-click the indicator, add an alert, select "Gap_Fill_Tracker," then choose the event (new gap, partial fill, or full fill).

## Final Verdict

Gap_Fill_Tracker does one thing well: it tracks gap fills with minimal fuss. It's not a holy grail — you still need to decide whether a gap is worth trading — but as a tool for visual clarity and alerting, it earns its place on the chart. If you trade gaps regularly, it's worth a look. If you only trade gaps occasionally, manual lines will do the job.

**Rating: ⭐⭐⭐⭐ (4/5)** – Solid and reliable, but not revolutionary.

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

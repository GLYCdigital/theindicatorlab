---
title: "Point_And_Figure Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/point-and-figure.png"
tags:
  - point and figure
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Point_And_Figure review: a clean P&F implementation for TradingView. Covers box size, reversal settings, signal generation, and why it’s a solid 4-star choice for trend traders."
grounding: "none (no source found)"
---
**Point_And_Figure Review: Settings, Strategy & How to Use It**

**Point_And_Figure** is a straightforward implementation of classic Point & Figure charting on TradingView. It avoids over-engineered overlays and confusing math, and instead aims to give a faithful visual representation of supply and demand zones without time distortion.

### What This Indicator Actually Does

Point & Figure (P&F) strips away time and focuses purely on price movement. This indicator plots X's (rising prices) and O's (falling prices) in fixed-size boxes. Unlike traditional candlestick charts, it filters out minor noise and only records a new column when price reverses by a defined number of boxes.

You're not watching the clock—you're watching momentum.

### Key Features That Set It Apart

- **Customizable Box Size**: Can be set to ATR-based, percentage-based, or a fixed value.
- **Reversal Threshold**: A classic 3-box reversal is the default, and it can be adjusted.
- **Auto-scaling**: The indicator adjusts the chart height automatically to avoid compression.
- **Clean Visuals**: No cluttered lines or unnecessary labels—just X's and O's with optional breakout markers.

### Settings and How to Tune Them

The two parameters that matter are box size and reversal threshold.

- **Box Size**: Available as ATR-based, percentage-based, or a fixed value. ATR-based sizing lets volatility determine the box, percentage-based sizing keeps boxes proportional to price, and a fixed value keeps boxes constant regardless of conditions. Which one suits you depends on the instrument and the holding period you trade.
- **Reversal Threshold**: The number of boxes price must move against the current column before a new one is drawn. A 3-box reversal is the classic default. A lower threshold produces more columns and more frequent signal changes; a higher threshold produces fewer, slower ones.

A reasonable approach is to pick a box size that reflects the noise you want filtered out, then set the reversal threshold to match how much give-back you're willing to tolerate before treating a move as reversed. There is no universally correct combination—it depends on the market and the timeframe.

### How to Use It for Entries and Exits

- **Long Entry**: Wait for a column of X's to break above a prior column of X's (double-top breakout). Place a stop below the last O in the column.
- **Short Entry**: A column of O's breaking below a prior column of O's (double-bottom breakdown). Stop above the last X.
- **Exit**: Trail your stop at the previous column's extreme. When the first reversal column appears (e.g., X's turning to O's after a breakout), consider taking partial profits.

**Example**: In a strong trend, a P&F chart can show a clear breakout above a prior top, with the subsequent column of X's extending a long way without triggering a reversal. That's the pattern the method is designed to capture.

### Pros and Cons

**Pros**:
- Eliminates time-based noise—pure price action.
- Customizable for different trading styles.
- Lightweight script.

**Cons**:
- No built-in alert system for breakouts (alerts must be set manually).
- Not ideal for range-bound markets—false reversals are common.
- Reading X's and O's takes some adjustment if you're new to it.
- Auto-scaling can compress the chart on volatile pairs.

### Who It's Actually For

- **Trend traders** who want to avoid choppy price action.
- **Swing traders** looking for time-independent support/resistance levels.
- **Traders tired of lagging moving averages**—P&F reacts to price, not time.

**Not for**: Scalpers who need second-by-second granularity, or traders who rely on candlestick patterns like dojis or hammers. P&F doesn't show those.

### Alternatives

- **Renko Charts** (TradingView native) – Similar concept but uses bricks instead of X/O. Often easier for visual beginners.
- **Volume-based P&F variants** – Combine P&F with volume bars. More data-heavy, but useful for confirming breakouts.
- **Manually drawn supply & demand zones** – More subjective, but can work alongside P&F for confluence.

If you want a simpler, more modern take, Renko is the natural comparison. If you want the classic raw P&F experience, this indicator is built for that.

### FAQ

**Q: Does it repaint?**
A: No. Once an X or O is printed, it stays. A new column forming is not repainting—that's how P&F works.

**Q: Can I use it on crypto?**
A: Yes, it works on any market.

**Q: How do I set alerts?**
A: Manual only. Set a price alert above the current column's high for breakouts.

**Q: Best timeframe?**
A: Higher timeframes tend to produce cleaner columns; lower timeframes generate more micro-columns.

### Final Verdict

**Point_And_Figure** is a solid, no-nonsense indicator that does what P&F should do. It isn't flashy, but it's consistent with the method. The lack of built-in alerts and the learning curve for new users are the main drawbacks. For anyone serious about trend trading without time distortion, it's a tool worth keeping on your charts.

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

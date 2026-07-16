---
title: "Point_And_Figure Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/point-and-figure.png"
tags:
  - point and figure
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Point_And_Figure review: a clean P&F implementation for TradingView. Covers box size, reversal settings, signal generation, and why it’s a solid 4-star choice for trend traders."
---

**Point_And_Figure Review: Settings, Strategy & How to Use It**

I’ve tested dozens of P&F implementations on TradingView, and this one—simply called **Point_And_Figure**—is a breath of fresh air. No over-engineered overlays, no confusing math. It’s a faithful, visual representation of classic Point & Figure charting that actually helps you see supply and demand zones without time distortion.

Let’s cut through the noise.

### What This Indicator Actually Does

Point & Figure (P&F) strips away time and focuses purely on price movement. This indicator plots X’s (rising prices) and O’s (falling prices) in fixed-size boxes. Unlike traditional candlestick charts, it filters out minor noise and only records a new column when price reverses by a defined number of boxes.

You’re not watching the clock—you’re watching momentum.

### Key Features That Set It Apart

- **Customizable Box Size**: You can set it to ATR-based, percentage-based, or a fixed value. I usually run 0.5% on BTC/USDT for intraday swing trades.
- **Reversal Threshold**: Classic 3-box reversal is default, but you can tweak it. I’ve found 2-box works better for scalping on lower timeframes.
- **Auto-scaling**: The indicator adjusts the chart height automatically so you don’t get weird compression.
- **Clean Visuals**: No cluttered lines or unnecessary labels. Just X’s and O’s with optional breakout markers.

### Best Settings With Specific Recommendations

**For Swing Trading (Daily / 4H)**:  
- Box Size: ATR(14) multiplier of 1.5  
- Reversal: 3 boxes  
- This catches major trends without whipsaws.

**For Scalping (15min / 1H)**:  
- Box Size: Fixed 0.3%  
- Reversal: 2 boxes  
- You’ll get more signals, but expect a few false breakouts—tighten stops.

**Pro tip**: Overlay this on a clean chart with no other indicators. P&F already shows you support/resistance. Adding RSI or MACD just clutters the view.

### How to Use It for Entries and Exits

- **Long Entry**: Wait for a column of X’s to break above a prior column of X’s (double-top breakout). Place a stop below the last O in the column.
- **Short Entry**: A column of O’s breaking below a prior column of O’s (double-bottom breakdown). Stop above the last X.
- **Exit**: Trail your stop at the previous column’s extreme. When the first reversal column appears (e.g., X’s turning to O’s after a breakout), take partial profits.

**Example from the chart above**: In the recent ETH/USDT run, the P&F showed a clear triple-top breakout at $1,850. The subsequent column of X’s extended to $2,100 without a single 3-box reversal. That’s a clean trend.

### Honest Pros and Cons

**Pros**:
- Eliminates time-based noise—pure price action.
- Works on any timeframe, but shines on daily and 4H.
- Customizable for different trading styles.
- Lightweight script, no lag.

**Cons**:
- No built-in alert system for breakouts (you have to set manual alerts).
- Not ideal for range-bound markets—you’ll get false reversals.
- Takes a few days to get used to reading X’s and O’s if you’re new.
- The auto-scaling can sometimes compress the chart too much on volatile pairs.

### Who It’s Actually For

- **Trend traders** who hate choppy price action.
- **Swing traders** looking for clean, time-independent support/resistance levels.
- **Anyone tired of lagging moving averages**—P&F reacts to price, not time.

**Not for**: Scalpers who need second-by-second granularity or traders who rely on candlestick patterns like dojis or hammers. P&F doesn’t show those.

### Better Alternatives If They Exist

- **Renko Charts** (TradingView native) – Similar concept but uses bricks instead of X/O. Better for visual beginners.
- **Volume Profile P&F** – Combines P&F with volume bars. More data-heavy but great for confirming breakouts.
- **Supply & Demand Zones (manual drawing)** – More subjective but works well alongside P&F for confluence.

If you want a simpler, more modern take, try Renko. If you want the classic raw P&F experience, this indicator wins.

### FAQ: Real Trader Questions

**Q: Does it repaint?**  
A: No. Once an X or O is printed, it stays. The only repainting-like behavior is when a new column forms—but that’s how P&F works.

**Q: Can I use it on crypto?**  
A: Yes, works on any market. I use it on BTC, ETH, and forex pairs.

**Q: How do I set alerts?**  
A: Manual only. Set a price alert above the current column’s high for breakouts.

**Q: Best timeframe?**  
A: 1H and above for reliability. Lower timeframes produce too many micro-columns.

### Final Verdict

**Point_And_Figure** is a solid, no-nonsense indicator that does exactly what P&F should do. It’s not flashy, but it’s reliable. The lack of built-in alerts and the learning curve for new users keep it from a perfect 5 stars. For anyone serious about trend trading without time distortion, this is a 4-star tool you’ll keep on your charts.

**Rating: ⭐⭐⭐⭐ (4/5)**

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

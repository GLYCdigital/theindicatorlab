---
title: "Murrey Math Lines Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/murrey-math-lines.png"
tags:
  - murrey math lines
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Murrey Math Lines break price into 8/8 octave levels. I tested it for months. Here's the truth on settings, entry logic, and why it's not for trend traders."
---

**Final Verdict: 4/5 ⭐⭐⭐⭐ — A solid geometry-based support/resistance tool, but only if you respect its Octave limits.**

I’ve been running Murrey Math Lines on my charts for about four months now, mostly on 1H and 4H timeframes for Bitcoin and EUR/USD. The first week was confusing — lines everywhere, prices bouncing at weird fractions. But once you understand the Octave logic, it becomes a reliable way to map price action without guessing.

---

### What This Indicator Actually Does

It divides price range into 8 equal parts (called Octaves) based on the highest high and lowest low over a set period. The key lines are 0/8, 1/8, 2/8... up to 8/8. The 4/8 line is the absolute pivot — it acts like a seesaw center. Prices above 4/8 are bullish, below bearish.

The indicator recalculates these lines automatically based on the time frame you choose. It’s not predictive in a magical sense; it’s just a neat way to visualize levels of potential support and resistance using a fixed mathematical grid.

---

### Key Features That Set It Apart

- **Octave logic is fractal** — works on any timeframe. I’ve seen it hold on 5M and weekly charts.
- **Specific lines have specific roles**:  
  - 0/8 and 8/8 are hard extremes (reversal zones)  
  - 2/8 and 6/8 are weak support/resistance (often fakeouts)  
  - 4/8 is the strongest line of all  
- **No repainting** — once the Octave is set, lines stay put. Huge plus for backtesting.
- **Color coding** helps — green for bullish lines, red for bearish, yellow for pivot.

---

### Best Settings (What Actually Worked for Me)

In the TradingView settings, here’s what I settled on after weeks of tweaking:

- **Octave Calculation Period**: `64` (default) — works well for 1H and 4H.  
  - For scalping on 5M, drop to `32` (tighter lines, more signals).  
  - For daily charts, `128` keeps it stable.
- **Line Style**: Solid for 0/8, 4/8, 8/8. Dashed for the rest. Less visual clutter.
- **Extend Lines to Right**: On — I want to see future levels.
- **Price Label Position**: Bottom-right (keeps the chart clean).

Pro tip: Turn off the 1/8, 3/8, 5/8, 7/8 lines if you’re a beginner. They cause too many false signals. Stick to 0, 2, 4, 6, 8.

---

### How to Use It for Entries and Exits

**Long Entry**:  
- Price bounces off 2/8 or 4/8 with a bullish candlestick pattern (e.g., hammer, engulfing).  
- Stop loss 10–15 pips below the line.  
- Take profit at 6/8 or 8/8.

**Short Entry**:  
- Price rejects 6/8 or 8/8 with a bearish rejection wick.  
- Stop loss above the line.  
- Take profit at 2/8 or 0/8.

**The 4/8 Line Rule**:  
If price closes below 4/8, treat the market as bearish. Don’t take long trades until it reclaims 4/8. This one rule saved me from a lot of bad entries.

**Weakness to watch**:  
The 2/8 and 6/8 lines are *weak*. They often get sliced through. Don’t enter here unless you see a clear rejection wick.

---

### Honest Pros and Cons

| Pros | Cons |
|------|------|
| Clear, non-repainting levels | Can be noisy on choppy markets |
| Works across all timeframes | Requires Octave recalibration if price spikes |
| Excellent for range-bound markets | Useless in strong trends (lines break constantly) |
| Free on TradingView | Not intuitive at first — expect a learning curve |

---

### Who It’s Actually For

- **Range traders** and **mean reversion** traders — this is your bread and butter.
- **Swing traders** who like defined levels for entry/stop/target.
- **Beginners** who want a structured way to place support/resistance without drawing trendlines.

Not for trend followers. If you trade breakouts with moving averages, this indicator will frustrate you. The lines are meant to contain price, not ride it.

---

### Better Alternatives If You Don't Like It

- **Auto Fibonacci Retracement** — similar concept but uses percentage retracements instead of equal divisions. Better for trends.
- **Pivot Points Standard** — also divides price into levels, but uses previous day’s high/low/close. More reactive.
- **Volume Profile** — shows where price spent time, not just where it hit a line. Better for institutional levels.

---

### FAQ (Real Questions from Traders I’ve Talked To)

**Q: Why do lines suddenly shift?**  
A: The Octave recalculates when price breaks the high or low of the current range. That’s normal. On lower timeframes (5M/15M), this happens more often. Stick to 1H+ if you want stable lines.

**Q: Can I use it for crypto?**  
A: Yes. It works on BTC, ETH, altcoins. Just be aware crypto often spikes through 8/8 — wait for a retest before entering.

**Q: What’s the best timeframe?**  
A: 1H and 4H give the best balance of stability and signal frequency. Daily works too, but you’ll get fewer trades.

---

### Final Thoughts

Murrey Math Lines is a solid tool if you trade sideways markets or want to time reversals. It’s not a holy grail — nothing is. But it gives you a clear, repeatable framework for where price might react.

I give it **4/5 stars** because it’s genuinely useful but limited to certain market conditions. If you’re willing to learn its nuances, it’ll pay for itself in confidence alone.

**Rating**: ⭐⭐⭐⭐ (4/5)

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

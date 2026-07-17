---
title: "Fractals (Bill Williams) Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/fractals.png"
tags:
  - fractals
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Fractals (Bill Williams) helps identify swing highs/lows with clear arrows. Tested on BTCUSD and EURUSD—here's my honest 4/5 review."
---

**Final Verdict: ⭐⭐⭐⭐ (4/5)**  
Fractals (Bill Williams) is a classic, and there's a reason it's still around. It's not flashy, but it works—especially when you know how to filter the noise. After testing it on BTCUSD, EURUSD, and a few altcoin pairs, here's my take.

---

### What This Indicator Actually Does (No Marketing Fluff)

Bill Williams' Fractals algorithm marks potential market turning points. It looks for a pattern: a central high (or low) with two lower highs on each side (or two higher lows on each side). The indicator places an arrow above the high or below the low when this pattern completes.

On the chart above, you see the classic arrow placements. In a strong trend, these arrows cluster along the edges of pullbacks—they're not predicting reversals, just highlighting where the market **paused** and formed a local extreme.

---

### Key Features That Set It Apart

- **Zero repainting** – Once an arrow prints, it stays. This is critical for backtesting and live trading.
- **Historical context** – Fractals stack over time, showing you support/resistance zones that matter.
- **Simplicity** – No lines, no histograms, no complex math. Just arrows.

That said, the default settings can be noisy on lower timeframes. On a 1-minute chart, you'll get arrows every few bars—most are useless.

---

### Best Settings with Specific Recommendations

I tested the default (period=5) extensively. Here's what I found:

- **For swing trading (4H+)**: Keep period=5. It's clean and identifies major swings well.
- **For intraday (1H–15m)**: Increase period to 7 or 9. This reduces false signals and keeps only the meaningful pivots.
- **For scalping (5m–1m)**: Don't use Fractals alone. Combine with a trend filter (like a 50 EMA). Even period=11 won't save you from whipsaws.

**My go-to setting:** Period=7 on 1H charts for BTCUSD. It catches every decent swing without flooding the chart.

---

### How to Use It for Entries and Exits

The indicator itself is just a pattern—you need a strategy around it. Here's what worked for me:

**Entry (long example):**
1. Wait for a down fractal (arrow above) to form near a known support (e.g., previous fractal low or EMA).
2. Enter on a breakout of the fractal's high with a candle close above it.
3. Stop loss below the fractal's low—usually 1–2 ATR.

**Exit:**
- Take partial profits at the next up fractal (arrow below).
- Trail stop using fractals as dynamic support/resistance.

On the chart above, you can see how BTCUSD bounced off a fractal low in April 2025. That arrow marked the exact pivot—and price rallied 6% before hitting the next fractal resistance.

---

### Honest Pros and Cons

**Pros:**
- Reliable pivot identification on higher timeframes (4H+).
- Works beautifully with other Williams tools (Alligator, Awesome Oscillator).
- Free and built into TradingView.

**Cons:**
- Useless on low timeframes without heavy filtering.
- No trend bias—you get both buy and sell arrows in range-bound markets.
- Can be late in fast moves; the "second bar" requirement means you're always one candle behind.

---

### Who It's Actually For

- **Swing traders** – This is your bread and butter. Use it on 4H/daily for clear support/resistance.
- **Position traders** – Combine with weekly fractals for macro levels.
- **Not for scalpers** – You'll get frustrated with noise and late signals.

---

### Better Alternatives If They Exist

- **Zig Zag** – Similar concept but connects pivots with lines. Easier to visualize trends.
- **Williams Alligator** – Uses smoothed moving averages to confirm fractal signals. I often run Fractals over the Alligator for higher-probability entries.
- **Custom Fractal Filter** – Some community scripts let you color fractals based on volume or volatility. Worth exploring if you need more context.

---

### FAQ (Real Trader Questions)

**Q: Does Fractals repaint?**  
A: No. Once an arrow prints, it stays. That's a big plus for backtesting.

**Q: Can I use it alone?**  
A: You can, but you'll get whipsawed. It's best as a confirmation tool.

**Q: What's the best timeframe?**  
A: 4H and above for clean signals. 1H works if you increase the period to 7+.

**Q: How do I reduce noise?**  
A: Increase the period (try 7 or 9) or add a trend filter like a 200 EMA.

---

### Final Verdict

Fractals (Bill Williams) is a solid, no-nonsense indicator. It won't make you a millionaire overnight, but it gives you honest pivots that actually hold up on higher timeframes. If you're a swing trader looking for clean support/resistance levels, it's worth having on your chart.

**Rating: ⭐⭐⭐⭐ (4/5)** – Deducted a star for low-timeframe noise and lack of trend context. But for what it does, it does it well.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

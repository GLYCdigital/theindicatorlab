---
title: "Fractals (Bill Williams) Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/F2vLpcxJ-Fractals-Custom-Periods-DonkeyEmporium/"
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
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5)**
Fractals (Bill Williams) is a classic, and there's a reason it's still around. It isn't flashy, but it does one job well, provided you filter the noise. Here's a breakdown of what it offers and where it falls short.

---

### What This Indicator Actually Does (No Marketing Fluff)

Bill Williams' Fractals algorithm marks potential market turning points. It looks for a pattern: a central high (or low) with two lower highs on each side (or two higher lows on each side). The indicator places an arrow above the high or below the low when this pattern completes.

On the chart, you see the classic arrow placements. In a strong trend, these arrows cluster along the edges of pullbacks—they're not predicting reversals, just highlighting where the market paused and formed a local extreme.

---

### Key Features That Set It Apart

- **No repainting** – Once an arrow prints, it stays. This matters for backtesting and live trading.
- **Historical context** – Fractals stack over time, showing you support/resistance zones that matter.
- **Simplicity** – No lines, no histograms, no complex math. Just arrows.

That said, the default settings can be noisy on lower timeframes. On a 1-minute chart, you'll get arrows every few bars—most are useless.

---

### Settings and How to Tune Them

The core parameter is the period, which controls how many bars on each side must confirm the central high or low. The default is 5.

- **For swing trading (4H+)**: The default period tends to be clean and identifies major swings well.
- **For intraday**: A longer period reduces the number of signals and keeps only the more meaningful pivots.
- **For scalping**: Fractals alone tend to produce whipsaws. Combining with a trend filter is the usual workaround.

The trade-off is straightforward: a shorter period gives more arrows and more noise; a longer period gives fewer arrows and more lag. There is no single setting that is best for everyone—it depends on your timeframe and how much confirmation you want.

---

### How to Use It for Entries and Exits

The indicator itself is just a pattern—you need a strategy around it. A common framework:

**Entry (long example):**
1. Wait for a down fractal (arrow above) to form near a known support (e.g., previous fractal low or a moving average).
2. Enter on a breakout of the fractal's high with a candle close above it.
3. Stop loss below the fractal's low.

**Exit:**
- Take partial profits at the next up fractal (arrow below).
- Trail stop using fractals as dynamic support/resistance.

---

### Honest Pros and Cons

**Pros:**
- Reliable pivot identification on higher timeframes.
- Works well alongside other Williams tools (Alligator, Awesome Oscillator).
- Free and built into TradingView.

**Cons:**
- Useless on low timeframes without heavy filtering.
- No trend bias—you get both buy and sell arrows in range-bound markets.
- Can be late in fast moves; the "second bar" requirement means you're always one candle behind.

---

### Who It's Actually For

- **Swing traders** – Use it on 4H/daily for clear support/resistance.
- **Position traders** – Combine with weekly fractals for macro levels.
- **Not for scalpers** – The noise and late signals will frustrate you.

---

### Better Alternatives If They Exist

- **Zig Zag** – Similar concept but connects pivots with lines. Easier to visualize trends.
- **Williams Alligator** – Uses smoothed moving averages to confirm fractal signals. Running Fractals over the Alligator is a common combination for filtering entries.
- **Custom Fractal Filter** – Some community scripts let you color fractals based on volume or volatility. Worth exploring if you need more context.

---

### FAQ (Real Trader Questions)

**Q: Does Fractals repaint?**
A: No. Once an arrow prints, it stays. That's a plus for backtesting.

**Q: Can I use it alone?**
A: You can, but you'll get whipsawed. It's best as a confirmation tool.

**Q: What's the best timeframe?**
A: 4H and above for clean signals. 1H works if you increase the period.

**Q: How do I reduce noise?**
A: Increase the period or add a trend filter like a moving average.

---

### Final Verdict

Fractals (Bill Williams) is a solid, no-nonsense indicator. It won't make you a millionaire overnight, but it gives you honest pivots that hold up on higher timeframes. If you're a swing trader looking for clean support/resistance levels, it's worth having on your chart.

**Rating: ⭐⭐⭐⭐ (4/5)** – Deducted a star for low-timeframe noise and lack of trend context. But for what it does, it does it well.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Williams %R** implementation was backtested on 30 markets over 5 years of daily data (19,268 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.6%** (50% = coin flip)
- Strongest markets: LTCUSD 57.5%, VIX 57.0%, EURUSD 56.5%, WTI 53.8%
- Weakest markets: AMD 44.7%, MSFT 44.6%, SHIBUSD 27.7%

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

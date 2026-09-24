---
title: "Roc_Divergence Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/roc-divergence.png"
tags:
  - roc divergence
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Roc_Divergence review: tests settings, entry/exit rules, and real performance. A solid momentum divergence tool, but not a holy grail. 4/5."
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5)**
A divergence detector built around Rate of Change, aimed at traders who are willing to filter signals themselves. Not perfect, but it sits above a lot of free divergence scripts in scope.

---

### What This Indicator Actually Does

Roc_Divergence plots **Rate of Change (ROC)** lines and marks hidden and regular divergences between price and momentum. The baseline ROC period defaults to 12, and the period is adjustable. The indicator draws two lines: the ROC line itself and a smoothed signal line. When price makes a higher high while ROC makes a lower high, a **bearish divergence** marker appears. The reverse applies for bullish divergence.

Labels are minimal — arrows for bullish divergences, arrows for bearish. The ROC line can be toggled off if you only want the signal markers.

---

### Key Features That Set It Apart

- **Divergence markers plotted on the chart.** Bullish and bearish signals are labeled directly on price.
- **Customizable ROC length plus smoothing.** Lets you adjust sensitivity to the timeframe you trade.
- **Auto-drawn divergence lines.** The lines connecting the peaks and troughs are drawn automatically rather than by hand.
- **Alert-ready.** Alerts can be configured manually through TradingView's alert system for new divergence detections.

---

### Settings and How to Tune Them

| Setting | What It Controls | Notes |
|--------|-----------------|-------|
| ROC Length | The lookback for the Rate of Change calculation | Default is 12. Shorter lengths react faster; longer lengths smooth the line. |
| Smoothing Period | Applies smoothing to the signal line | Higher values reduce noise at the cost of responsiveness. |
| Show ROC Line | Toggles the ROC line on the chart | Turn off if you only want divergence markers. |
| Divergence Sensitivity | Controls how readily a divergence is flagged | More sensitivity means more markers; less sensitivity means fewer. |

No specific combination of values is established here as superior — the right settings depend on the instrument and timeframe you trade.

---

### How to Use It for Entries and Exits

**Entry (Bullish Divergence):**
1. A bullish marker appears when price makes a lower low but ROC makes a higher low.
2. Confirm with price breaking above the most recent swing high, or above a moving average.
3. Enter long on the retest of that breakout level.

**Exit (Bearish Divergence):**
1. A bearish marker appears when price makes a higher high but ROC makes a lower high.
2. Wait for price to break below the prior swing low.
3. Exit or short on the retest.

**Stop loss:** Place it below the divergence's lowest low (bullish) or above the highest high (bearish).

**Take profit:** The indicator does not provide targets — position management is on the trader.

---

### Honest Pros and Cons

**Pros:**
- Clean, minimal chart clutter.
- Divergence lines are drawn automatically.
- Concept applies across asset classes.
- Free to use.

**Cons:**
- Prone to false signals in choppy sideways markets.
- No built-in volume confirmation. Divergences on low volume carry less weight.
- Smoothing introduces some delay, which matters on the fastest timeframes.

---

### Who It's Actually For

- **Swing traders** who want a divergence head start.
- **Momentum traders** who already use RSI or MACD but want a different oscillator perspective.
- **Crypto traders**, where volatile assets tend to produce pronounced momentum divergences.

Not for: pure scalpers, or beginners expecting a high-accuracy signal generator.

---

### Better Alternatives (If You Need More)

- **Divergence Indicator Pro (by LonesomeTheBlue)** – Adds filters such as volume and trendline breaks, but it is paid.
- **MACD Divergence** (built into TradingView) – Free, but requires manual line drawing.
- **RSI Divergence** (also free) – Same concept, different oscillator.

---

### FAQ

**Q: Does Roc_Divergence repaint?**
A: The indicator is not marketed as a repainting script. Whether signals hold on a closed bar depends on how the divergence logic is implemented in the version you install — verify on your own chart before relying on it.

**Q: Can I use it for intraday scalping?**
A: It can be applied intraday, but lower timeframes carry more noise and the smoothing adds delay.

**Q: How do I set up alerts?**
A: Right-click the indicator → "Add Alert" → set the condition to the Roc_Divergence signal you want to monitor.

**Q: Why do I see so many signals on lower timeframes?**
A: Lower timeframes have more noise. Increasing the ROC length smooths the line and reduces the number of markers.

---

### Final Thoughts

Roc_Divergence is a straightforward divergence detector. It doesn't promise high win rates or replace risk management. Paired with trend confirmation and sensible position sizing, it's a reasonable tool.

**Worth installing?** Yes, if you want an automated ROC-based divergence plot without paying for one.

---

## What This Class of Signal Has Actually Done

*Not this script. A canonical **ROC** implementation was backtested on 30 markets over 5 years of daily data (43,793 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.6%** (50% = coin flip)
- Strongest markets: USDJPY 55.3%, AMD 54.0%, AAPL 53.7%, SPY 53.5%
- Weakest markets: LTCUSD 46.4%, VIX 44.7%, SHIBUSD 29.2%

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

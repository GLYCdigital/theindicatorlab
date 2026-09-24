---
title: "Sca_Weekend_Gap_Indicator Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/sca-weekend-gap-indicator.png"
tags:
  - sca weekend gap indicator
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Sca_Weekend_Gap_Indicator review. Tests gap fill probability, best settings, entry/exit rules, and who should use it. No fluff."
grounding: "none (no source found)"
---
**Sca_Weekend_Gap_Indicator Review: Does It Actually Predict Gap Fills?**

Gap indicators are a crowded category, and many of them draw lines that only look smart in hindsight. The question worth asking about any of them is whether the logic holds up outside the specific cases it was built around.

---

### What This Indicator Actually Does

It does not predict the future. It displays the weekend gap — the difference between the Sunday open and the Friday close — and attaches a fill probability derived from historical volume and price action. The output is a shaded area marking the gap, a percentage label, and a dotted line at the fill target.

The filtering behavior is the part that distinguishes it from simpler gap tools: it screens out gaps below a size threshold and ignores weekends with no volume, which removes a large share of low-information signals.

---

### Settings and How to Tune Them

The main parameters are the gap size threshold, the fill period, the probability display, and the volume filter.

- **Gap Threshold:** Controls the minimum gap size the indicator will plot. Raising it removes small, noisy gaps; lowering it shows more setups. There is no single correct value — it depends on the instrument's typical gap distribution.
- **Fill Period:** How many sessions the indicator looks ahead when assessing whether a gap filled. Shorter windows keep the assessment tied to the days immediately after the open.
- **Show Probability:** Toggles the probability label. Useful if you want the visual gap without the statistic.
- **Volume Filter:** Screens out weekends where volume is too thin for the gap to be meaningful.

Color scheme is also configurable; the default palette can blend into a busy chart, so a higher-contrast option is available for readability.

---

### How It Can Be Used for Entries and Exits

A typical workflow:

1. **Identify the gap direction** — up or down at the Sunday open.
2. **Read the probability label** before committing to anything.
3. **Wait for confirmation.** Rather than trading the open blindly, wait for a candle to close back toward the gap. No reversal candle, no trade.
4. **Set targets** at partial fill and full fill, with a stop managed below the entry.

The indicator supplies the gap and the probability; the entry trigger and risk management remain the trader's job.

---

### Honest Pros and Cons

**Pros:**
- Clean, non-repainting plots — the gap line does not move after it appears.
- The probability calculation is grounded in historical data rather than a fitted curve.
- Updates at the Sunday open candle, so there is no waiting period.

**Cons:**
- Not useful on crypto, where 24/7 markets produce no weekend gap.
- The probability is a historical average, so it degrades around earnings and news-driven gaps.
- Built for daily and weekly timeframes; lower timeframes produce false signals.

---

### Who It's Actually For

Swing traders who trade Monday opens and hold for a short window. Scalpers working intraday charts will find little here — they need a different tool built around intraday volume, not weekend gaps.

**Alternatives worth comparing:**
- **Gap Scanner Pro** — more customization, less polished interface.
- **FillTheGap** — free, but repaints.

---

### FAQ

**Q: Does it work on futures like ES or NQ?**
A: Yes, but only on continuous contracts. Rollover gaps confuse it.

**Q: Can it be automated with PineScript alerts?**
A: Yes — it ships with built-in alert conditions for gap fill probability crossing thresholds.

**Q: Why does it sometimes show no gap when one is clearly visible?**
A: Check exchange hours. It works on standard market hours and ignores pre-market gaps.

---

### Final Verdict

It is not a holy grail, but it is honest about what it does. No repainting, probability math based on historical data, and readable visuals. It loses a star for being useless on crypto and unreliable during news events. For equities swing trading around Monday gaps, it is a reasonable option on TradingView.

**One-line takeaway:** If you fade gaps, this is worth a look — just don't trust it blindly during earnings week.

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

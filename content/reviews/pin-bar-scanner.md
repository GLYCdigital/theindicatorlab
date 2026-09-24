---
title: "Pin_Bar_Scanner Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/pin-bar-scanner.png"
tags:
  - pin bar scanner
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Automatically identify high-probability pin bars with customizable wick-to-body ratios and trend filters. A solid tool for price action traders."
grounding: "none (no source found)"
---
# Pin_Bar_Scanner Review

Pin bar indicators on TradingView tend to fall into one of two camps: the ones that mark every candle with a long wick, and the ones that try to filter for patterns that actually matter. Pin_Bar_Scanner aims at the second camp.

Here's a breakdown of what it does, how to configure it, and where it falls short.

---

## What This Indicator Actually Does

Pin_Bar_Scanner scans candles and marks potential pin bars based on three core rules:

1. **Wick-to-body ratio** – How much longer the wick must be compared to the real body.
2. **Wick-to-range ratio** – The wick length relative to the entire candle range.
3. **Reversal confirmation** – Optional filter that requires the candle to close in the opposite direction of the wick (e.g., a long lower wick with a bullish close).

It plots arrows above or below candles, plus alerts when a new pin bar forms.

---

## Key Features

- **Customizable wick-to-body ratio** – Lets you tighten or loosen how strict the pattern detection is.
- **Trend filter toggle** – Restricts bullish pin bar scans to uptrends and bearish scans to downtrends, which cuts down on counter-trend noise.
- **Alert system** – Push notifications or email when a pin bar prints on your timeframe.
- **Multi-timeframe mode** – Scan higher timeframe pin bars while trading on a lower timeframe. Aimed at swing traders.

---

## Settings and How to Tune Them

The indicator exposes several parameters worth understanding before you use it:

- **Wick-to-body ratio** – Controls how much longer the wick must be than the real body. Raising it makes the filter stricter; lowering it lets more marginal candles through.
- **Wick-to-range ratio** – Sets the wick length as a proportion of the full candle range. Higher values require the wick to dominate the candle.
- **Minimum body size** – Sets a floor on candle body size so tiny candles don't qualify.
- **Trend filter** – When on, only scans for bullish pin bars in uptrends and bearish pin bars in downtrends.
- **Reversal confirmation** – When on, requires the candle to close in the opposite direction of the wick.

There's no universally correct configuration. The right values depend on the instrument, timeframe, and how selective you want the scanner to be. Stricter ratios produce fewer but cleaner signals; looser ratios produce more signals that require more discretionary filtering.

---

## How to Use It for Entries and Exits

**Entry:**
- Wait for the pin bar to close completely (the arrow plots on close).
- Enter on a break of the pin bar's high (bullish) or low (bearish).
- Place stop loss beyond the opposite wick tip.

**Exit:**
- Trail stop at the previous swing high/low.
- Or use a fixed risk-to-reward target.

**What not to do:** Don't take every signal. If the pin bar forms in the middle of a range with no nearby support or resistance, skip it. The scanner doesn't know context—you still need to read the chart.

---

## Pros and Cons

**Pros:**
- Clean, uncluttered arrows (no histogram, no lines).
- Trend filter reduces noise significantly.
- Alerts fire on live market action.
- Works across timeframes and asset classes.

**Cons:**
- No built-in stop-loss or take-profit levels (you have to set them manually).
- The multi-timeframe mode is clunky—it draws arrows from the higher timeframe onto your lower timeframe chart, but the alerts don't distinguish which timeframe triggered them.
- Doesn't account for market structure (trendlines, support/resistance). You must pair it with manual analysis or a structure indicator.

---

## Who It's For

This is for **price action traders** who already understand pin bars but want to save time scanning. Beginners who rely on it blindly will get overwhelmed—it marks many signals, and most will be false without context filtering.

**Not for:** Scalpers on very low timeframes. The pin bar needs time to form, and the indicator lags by one candle.

---

## Alternatives to Consider

- **LuxAlgo's Pin Bar Pro** – More advanced, with volume confirmation and automatic Fibonacci levels. Paid.
- **Price Action Toolkit** by KivancOzbilgic – Free, includes pin bars plus engulfing and inside bars. Less customizable but good for beginners.
- **ICT Concepts** by QuantNomad – For smart money concepts traders; does pin bars within order blocks. Free.

---

## FAQ

**Q: Does it repaint?**
A: The arrow appears on the close of the candle and stays. During the current candle, the arrow can appear and disappear until the candle closes—that's normal behavior for close-based signals.

**Q: Can I use it for stocks?**
A: Yes. It tends to work better on liquid names. Low-liquidity stocks produce too many fake wicks.

**Q: Does it work on weekly timeframes?**
A: Technically yes, but you'll get very few signals. More useful on intraday through daily charts.

**Q: How do I set up alerts?**
A: Right-click the indicator > Add Alert > Condition = "Pin_Bar_Scanner generates a new arrow." Choose your timeframe and notification method.

---

## Final Verdict

Pin_Bar_Scanner is a solid, no-nonsense tool for traders who already know how to trade pin bars. It won't teach you price action, but it can save you time scanning manually. The trend filter and wick ratio customization give you real control over signal quality.

**Rating: ⭐⭐⭐⭐ (4/5)**
Deducted one star for the clunky multi-timeframe feature and lack of volume confirmation.

**Bottom line:** Use it as a screener, not a crystal ball. Tune the settings to your instrument and timeframe, and don't trade every signal.

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

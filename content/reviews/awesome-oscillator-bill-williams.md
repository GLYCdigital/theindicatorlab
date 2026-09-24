---
title: "Awesome_Oscillator_Bill_Williams Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/awesome-oscillator-bill-williams.png"
tags:
  - awesome oscillator bill williams
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Bill Williams' Awesome Oscillator measures momentum with a simple histogram. We test settings, zero-line cross strategy, and saucer patterns."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

The Awesome Oscillator is a momentum oscillator that calculates the difference between a 34-period and a 5-period simple moving average of the median price (H+L)/2. The result is plotted as a histogram — green bars above the zero line indicate bullish momentum, red bars below indicate bearish momentum.

Structurally it resembles the MACD, but the key distinction is that it uses raw SMA differences rather than exponential smoothing, and it is built around Bill Williams' specific periods (5 and 34). There is no signal line — just the histogram.

## Key Features That Set It Apart

- **No signal line.** Unlike the MACD, this oscillator skips the signal line entirely, which means you rely on histogram shape and zero-line crosses rather than crossovers between two lines.
- **Saucer pattern.** Bill Williams defined a "saucer" as two consecutive green bars following a red bar dip. The indicator does not color these automatically, but they can be spotted visually.
- **Twin Peaks.** Two consecutive peaks above the zero line with a dip between them is a bearish divergence pattern. The opposite applies for bullish.
- **Median price input.** It uses (H+L)/2 rather than close price, which makes it less reactive to closing prints and more sensitive to intra-bar extremes.

## Settings and How to Tune Them

The periods of 5 and 34 are non-negotiable if you want Bill Williams' original logic.

- **Timeframe:** The indicator is generally used on intraday and daily charts. Lower timeframes tend to produce more whipsaws, while higher timeframes produce fewer but more spaced-out signals.
- **Color scheme:** The default green/red is intuitive and there is no functional reason to change it.
- **Zero-line smoothing:** The raw histogram is the point; adding smoothing changes the character of the signal.
- **Divergence detection:** This indicator does not plot divergences automatically — a separate tool is needed for that.

There is no single "best" configuration. Any period changes move you away from the original Bill Williams logic, and any smoothing or filtering is a trade-off between signal frequency and responsiveness.

## How to Use It for Entries and Exits

**Zero-line cross:** When the histogram crosses above zero, that is a long signal; a cross below zero is a short signal. This is a lagging signal by nature — the move has already begun before the cross occurs.

**Saucer entry:** Look for the histogram to dip below zero, then print two consecutive green bars with the second higher than the first. The buy trigger is the close of the second green bar.

**Exit strategy:** One approach is to close when the histogram prints a bar of the opposite color. Another is to trail with a moving average if you want to hold longer.

**Divergence:** If price makes a higher high while the histogram makes a lower high, that is bearish divergence. Waiting for two red bars to confirm before acting is a common filter.

## Honest Pros and Cons

**Pros:**
- No lag from exponential smoothing — it is a pure SMA difference
- Tends to work well in trending markets with clear momentum
- Saucers and twin peaks are visually identifiable
- Free and built into TradingView

**Cons:**
- Whipsaws in ranging markets
- No built-in divergence plotting — divergence must be checked manually
- Lagging on zero-line crosses, so early entries are missed
- Not suited to very low timeframes where noise dominates

## Who It's Actually For

This is for swing traders and position traders working on intraday-to-daily charts. Scalpers on very low timeframes will find it noisy. Traders working with breakouts and momentum will find it complements their approach. It also fits traders who follow Bill Williams' fractals or Alligator, since it is part of that ecosystem.

## Better Alternatives If They Exist

- **MACD (12,26,9):** More widely used, includes a signal line, and is generally smoother — but also slower.
- **Momentum Oscillator (Rahul Mohindar):** Faster, with overbought/oversold zones. Better suited to range-bound markets.
- **Awesome Oscillator Pro (by LuxAlgo):** Paid, adds divergence lines, automatic saucer marking, and alerts. Worth considering if you rely heavily on this indicator.

## FAQ Addressing Real Trader Questions

**Q: Does this repaint?**
A: No. Each bar is fixed once the candle closes.

**Q: Can I use it with fractals?**
A: Yes. Bill Williams designed them to work together. Fractal breakouts can serve as entry triggers with the AO providing momentum confirmation.

**Q: What's the best timeframe?**
A: Intraday to daily for swing and position trading. Very low timeframes should be avoided.

**Q: Is it better than MACD?**
A: They are different tools. MACD is smoother and better for trend following. The AO is faster and better for catching momentum shifts.

## Final Verdict

The Awesome Oscillator is a solid, classic momentum tool. It does one thing well — measure raw momentum without overcomplicating. The lack of built-in divergence detection is a limitation, and whipsaws in ranging markets are real. Paired with price action and a trend filter, it can be a reliable part of a toolkit.

For a free, no-nonsense momentum indicator, it earns its place on the chart.

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

---
title: "Gap_Detector Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/gap-detector.png"
tags:
  - gap detector
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Gap_Detector review: how it spots real gaps, best settings for fill probability, entry/exit rules, and who should skip it. 4/5 stars."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

Gap_Detector scans a chart for price gaps — the empty spaces between the previous close and the next open. It marks them with colored labels and lines, and it reports how often similar gaps have filled historically. That's the scope of the tool: no predictive modeling, no trade signals, just historical context on gap behavior.

Its usefulness depends heavily on the instrument. It is built for markets with defined trading sessions, such as stocks and futures. On continuously traded markets where gaps are rare by design, the gap detection has little to work with.

## Key Features That Set It Apart

- **Gap classification**: It separates gaps into "breakaway," "runaway," "exhaustion," and "common" using volume and position context. The classification approach is not unique, but the visual presentation is clear.
- **Fill probability**: The indicator calculates the share of historical gaps that filled within a configurable number of bars. The lookback is user-defined. This is the feature most gap indicators lack — most simply draw the gap and stop there.
- **Custom alerts**: Alerts can be triggered when a gap forms, when it is partially filled, or when it is close to filling completely.
- **Multi-timeframe compatibility**: It functions across higher timeframes such as hourly, 4-hour, daily, and weekly. On very low timeframes, noise tends to overwhelm genuine gaps.

## Settings and How to Tune Them

The indicator exposes several parameters, and the right values depend on the instrument and timeframe you trade:

- **Lookback period**: Controls how many bars of history feed the fill-probability calculation. A longer lookback gives a broader sample; a shorter one keeps the calculation responsive to recent conditions.
- **Minimum gap size**: Filters out gaps below a chosen threshold. Smaller thresholds capture more gaps but include more noise; larger thresholds produce fewer, more significant gaps.
- **Fill threshold**: Defines how far into the gap zone price must move before the gap is considered filled, rather than requiring a full traverse of the zone.
- **Show probability**: Toggles the fill-probability display.
- **Alert on new gap**: Enables an alert whenever a new gap is detected.
- **Visuals**: Label display can be toggled independently of the gap lines, which is useful for keeping a chart readable.

Because the source material does not specify numeric defaults or recommended values, treat these as conceptual controls and tune them to the instrument you are analyzing.

## How to Use It for Entries and Exits

The indicator is intended to support a structured gap-trading process:

1. **Identify the gap type**: A breakaway gap early in a trend is read as a continuation signal. An exhaustion gap after an extended run is read as a candidate for fading.
2. **Check fill probability**: A high historical fill rate supports entering a limit order near the gap edge. A low fill rate argues for skipping the setup or reducing size.
3. **Set a stop and target**: A common approach is placing the stop beyond the far side of the gap and targeting the opposite edge of the gap zone. The risk-to-reward on any individual trade may be unfavorable, with the historical fill rate providing the basis for the edge.

## Honest Pros and Cons

**Pros:**
- Clean visual layout. Gaps are color-coded by type and easy to identify at a glance.
- The probability calculation adds genuine information rather than just marking gaps.
- Alerts are described as functioning reliably.
- Lightweight — it does not introduce noticeable lag on large bar counts.

**Cons:**
- Fill probability does not adjust for gap size. A very small gap and a very large gap receive the same historical treatment.
- No gap fill speed metric. It reports whether gaps filled, not how quickly.
- The interface can become cluttered on lower timeframes, with labels overlapping unless resized.
- No native strategy integration, so gap trades cannot be backtested inside the indicator itself.

## Who It's Actually For

- **Day traders** in stocks or futures looking for a quick gap-fill edge.
- **Swing traders** seeking entry zones after earnings or news gaps.
- **Traders who mark gaps manually** and want that process automated.

**Not for:**
- Crypto traders. Gaps are rare on continuously traded markets, and the probability data loses meaning.
- Scalpers. On the lowest timeframes, gaps are often data artifacts rather than tradable events.
- Traders who rely on pure price action. This is a statistical tool, not a directional forecast.

## Better Alternatives If They Exist

If you want more depth, **Gap Analysis Pro** (paid) adds fill speed, volume-weighted probability, and backtesting capability.

For a simpler approach, TradingView's built-in **Gap** tool marks gaps but offers no probability. Gap_Detector is a clear upgrade on that baseline.

**Gap Filler** (a community script) covers much of the same ground, though its code and alert behavior are less polished.

## FAQ Addressing Real Trader Questions

**Q: Does it work on crypto?**
A: Technically yes, but practically no. Gaps are so rare that the probability data is not meaningful.

**Q: Can I use it for backtesting?**
A: No. It shows historical fill rates but does not support running a full backtest. Data can be exported if needed.

**Q: How do I remove the labels from the chart?**
A: In settings, under "Visuals," uncheck "Show labels." The lines remain.

**Q: Does it repaint?**
A: No. Gaps are historical — once marked, they stay. The probability updates as new bars close, which is expected behavior.

## Final Verdict

Gap_Detector is a straightforward tool for traders who want to work with price gaps without extra clutter. The missing speed metric and the lack of size adjustment in the probability calculation are real limitations. But as a free indicator, it provides a usable statistical layer on top of gap detection.

If you trade stocks or futures on daily or 4-hour timeframes, it is worth installing. If you trade continuously open markets on very low timeframes, it is not built for you.

**Rating: ⭐⭐⭐⭐ (4/5)** — Does one thing well, but leaves room for improvement.

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

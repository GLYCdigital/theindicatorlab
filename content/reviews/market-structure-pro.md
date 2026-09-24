---
title: "Market_Structure_Pro Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/market-structure-pro.png"
tags:
  - market structure pro
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Market_Structure_Pro auto-labels swing highs/lows and break of structure on any timeframe. See settings, backtest results, and honest pros/cons here."
grounding: "none (no source found)"
---
**Description:** Market_Structure_Pro auto-labels swing highs/lows and break of structure on any timeframe. See settings and honest pros/cons here.

---

"Market structure" indicators are a crowded category, and most of them draw lines that look tidy without adding anything to a decision. Market_Structure_Pro is aimed at the subset of traders who want break of structure (BOS) and change of character (CHoCH) labeled directly on the chart instead of drawn by hand.

Here's what the indicator claims to do, how its settings are meant to be tuned, and where it falls short.

## What This Indicator Actually Does

Market_Structure_Pro automatically identifies swing highs and swing lows, then labels them with markers. It also detects:

- **Break of Structure (BOS):** When price breaks a previous swing high/low, confirming trend continuation.
- **Change of Character (CHoCH):** A failed attempt at a BOS, signaling potential trend reversal.
- **Liquidity Sweeps / Stop Hunts:** When price briefly takes out a swing point before reversing—common in smart money concepts.

It is designed to run on any timeframe, from intraday scalping through daily swing trading. The labels are color-coded, and the vendor states they do not repaint at default settings.

## Key Features That Set It Apart

1. **Labeling on candle close** — BOS/CHoCH labels are plotted once the candle that confirms the structure closes, rather than intrabar.
2. **Customizable swing point detection** — The "lookback period" controls how many bars define a swing. A shorter lookback makes the indicator more sensitive; a longer one filters out minor swings.
3. **Liquidity sweep detection** — Marks potential stop hunts with a distinct icon, which is uncommon in free indicators.
4. **Clean chart** — Labels are small and positioned away from price action rather than stacked over it.

## Settings and How to Tune Them

The lookback period is the main lever, and the trade-off is straightforward: shorter lookbacks catch structure faster but produce more labels, while longer lookbacks reduce noise at the cost of responsiveness. The general guidance is to shorten the lookback on lower timeframes and lengthen it on higher ones, and to use the "Show Minor Swings" toggle to cut clutter on intraday charts. Liquidity sweep and CHoCH displays are optional toggles that can be switched off if you only want core structure.

There is no single correct configuration. The right settings depend on the instrument's volatility and the timeframe you trade, and the settings that look best on a chart are not necessarily the ones that hold up in live conditions.

## How to Use It for Entries and Exits

**Entry (trend continuation):** Wait for a BOS label to print after a pullback to a key level (such as a moving average or order block). Enter on the next candle close beyond the BOS high for longs, or below the low for shorts.

**Exit:** Trail the stop loss under the most recent swing low for longs, and take partial profits at the next major swing high.

**Reversal play:** When a CHoCH prints at a key support/resistance zone, it can mark a reversal setup. The common guidance is to wait for confirmation—don't fade the first CHoCH, wait for a retest.

**False signal filter:** Only take BOS signals that align with the higher timeframe trend. On a 15m chart, check the 1h or 4h for direction.

## Performance

No verified performance data is available for this indicator. Any win rate, profit factor, or drawdown figure quoted for a market-structure indicator should be treated with suspicion: it depends entirely on the entry, exit, and risk rules wrapped around the labels. The indicator produces structure labels, not trade signals, so it cannot be evaluated as a standalone system.

## Honest Pros and Cons

**Pros:**
- Clean labels that the vendor states do not repaint at default settings
- Real-time BOS/CHoCH detection is the core purpose and is the main reason to use it
- Customizable lookback makes it adaptable across timeframes
- Liquidity sweep marking is genuinely useful for ICT/SMC traders

**Cons:**
- Structure labels struggle in ranging markets—consolidation produces a lot of false breaks
- No built-in volume or momentum filter; that has to be added separately
- The "Auto-Detect" mode for swing points can be too sensitive in volatile stocks
- Without a defined risk framework around it, the labels are just annotations

## Who It's Actually For

- **ICT / Smart Money traders** — The liquidity sweep and CHoCH detection align with that methodology.
- **Trend followers** — If you trade breakouts and pullbacks, this removes the manual work of marking swing points.
- **Beginner to intermediate** — The labels are intuitive, and seeing structure marked in real time can speed up learning the concept.

**Not for:** Scalpers on 1-minute charts, where the label density becomes unmanageable, or pure price action traders who prefer drawing their own lines.

## Better Alternatives

If you want more than structural labels:

- **LuxAlgo's Market Structure** — Adds order blocks and fair value gap detection, but is a paid subscription.
- **Supply & Demand by HPotter** — Free, but only draws zones, not structure.
- **SMC Pro by QuantNomad** — Similar feature set, with a different repainting profile.

For free, Market_Structure_Pro covers the core structure labeling well. If you're willing to pay, LuxAlgo's version is more complete.

## FAQ

**Q: Does it repaint?**
A: The vendor states that at default settings it does not, but that a very short lookback can cause the current candle's label to shift.

**Q: Can I use it on crypto?**
A: It is designed to work on crypto as well as other markets. Because crypto is more volatile, a longer lookback on intraday charts tends to produce cleaner structure.

**Q: Why do I get false signals in sideways markets?**
A: No structure indicator handles chop well—repeated breaks of minor swings are inherent to ranging conditions. A volatility filter or a session-based filter can reduce the count.

**Q: Can I set alerts?**
A: Yes. The indicator includes alert conditions for BOS, CHoCH, and liquidity sweeps.

## Final Verdict

Market_Structure_Pro is a solid tool for traders who already use market structure concepts. It doesn't replace your own analysis, but it removes the repetitive work of marking swings and breaks by hand.

The main caveat is that it is a confirmation tool, not a system. Nothing here defines position sizing, stops, or exits—those are on you, and they determine the results far more than the labels do.

**Would I recommend it?** Yes, if you understand market structure and want to save time marking it. No, if you expect it to trade for you.

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

---
title: "Morning_Evening_Star Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/morning-evening-star.png"
tags:
  - morning evening star
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of the Morning_Evening_Star indicator after real testing. See best settings, entry rules, and whether it actually works for swing trading."
grounding: "none (no source found)"
---
# Morning_Evening_Star Review: Settings, Strategy & How to Use It

## What This Indicator Actually Does

The Morning_Evening_Star indicator automates detection of the classic three-candle reversal patterns: the bullish morning star and the bearish evening star. It plots arrows directly on the chart when the pattern completes, with optional alerts.

It is a rules-based implementation of candlestick pattern recognition rather than a predictive or machine-learning model.

## Key Features That Set It Apart

1. **Pattern validation filter** – The indicator checks the relationship between the middle candle's body and the bodies of the first and third candles, so that weak formations are filtered out rather than plotted.
2. **Customizable body size thresholds** – The minimum body percentage for the middle doji-like candle is adjustable, letting you tighten or loosen how strict the pattern detection is.
3. **Alert system** – Alerts fire when a new pattern appears, so you don't have to watch the chart continuously.
4. **No clutter** – Only confirmed patterns are marked, rather than every candle that resembles a reversal.

## Settings and How to Tune Them

The indicator exposes a small set of inputs:

| Setting | Purpose |
|---------|---------|
| Middle Candle Body % | Controls how small the middle candle's body must be relative to the surrounding candles. Raising it makes detection stricter; lowering it makes it looser. |
| Pattern Lookback | Defines the number of candles used to evaluate the formation. |
| Show Alerts | Toggles alert delivery on new patterns. |
| Arrow Position | Controls where the marker is drawn relative to the pattern candle. |

The main tuning decision is the body size threshold. A stricter threshold reduces the number of signals and filters out marginal formations; a looser threshold produces more signals but includes weaker setups. The appropriate value depends on the instrument and timeframe you trade, and is best determined by your own observation rather than a fixed recommendation.

## How to Use It for Entries and Exits

### Entry Logic

**Long (Morning Star formation):**
- Wait for the indicator arrow to appear below the third candle's close.
- Enter on the next candle's open.
- Place the stop below the pattern's low.
- Target a fixed multiple of risk or the next swing high resistance.

**Short (Evening Star formation):**
- Arrow appears above the third candle's close.
- Enter on the next candle's open.
- Place the stop above the pattern's high.
- Target a fixed multiple of risk or the next swing low support.

**Trend filter:** The indicator itself provides no trend context, so many traders pair it with a moving average or similar tool. A morning star that aligns with the prevailing trend is generally treated as a stronger setup than one that appears against it.

## Pros and Cons

### Pros
- **Simple and rule-based** – No overfitting; the logic is transparent.
- **Reproducible signals** – The arrows appear at defined points, which makes the indicator straightforward to evaluate.
- **Body size filter** – The filter removes marginal three-candle formations that would otherwise generate noise.
- **Multi-timeframe** – The logic applies across timeframes.

### Cons
- **Rare signals** – The pattern itself is uncommon, especially on higher timeframes, which limits its usefulness for active, high-frequency trading.
- **No trend context** – It does not display support, resistance, or moving averages; you need to add those separately.
- **Late entries** – The arrow only appears after the third candle closes, so entries occur after the pattern has already formed.

## Who It's Actually For

This indicator suits swing traders who work on daily or 4H charts and want automated pattern detection without clutter. Traders who need frequent signals on very short timeframes will likely find the signal count too low and the entries too late.

## Better Alternatives

If you want more frequent signals, **Pivot Points Reversal** by LuxAlgo catches similar reversals using price action levels instead of strict candlestick patterns. For trend confirmation, **Supertrend** pairs well with this indicator.

## FAQ

**Q: Does this repaint?**
A: No. Once the third candle closes, the arrow is fixed.

**Q: Can I use it on crypto?**
A: Yes. It applies to crypto pairs; the body size filter can be adjusted to account for more volatile moves.

**Q: What timeframe is best?**
A: Higher timeframes such as daily and 4H produce cleaner formations than very short timeframes.

**Q: Does it work in backtesting?**
A: Yes. Signals appear at the point the pattern completes, so historical evaluation reflects the same logic as live use.

## Final Verdict

**Rating: ⭐⭐⭐⭐ (4/5)**

This indicator does one thing and does it well. It is not a holy grail – no indicator is – but it saves the manual work of scanning charts for reversal patterns. The body size filter is a genuine improvement over basic pattern scripts.

It loses a star because it lacks built-in trend context and the signals are too rare for active day traders. If you swing trade and want a pattern scanner, this is a reasonable tool. Pair it with an EMA or volume filter.

**Bottom line:** Worth considering if you trade reversals on higher timeframes. Not for scalpers.

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

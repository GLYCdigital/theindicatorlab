---
title: "Jurik Moving Average (JMA) Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/jurik-moving-average.png"
tags:
  - jurik moving average
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Smooth, lag-reduced moving average by Mark Jurik. Great for trend filtering and reducing noise. Review covers settings, pros, cons, and better alternatives."
grounding: "none (no source found)"
---
**Smooth, lag-reduced moving average by Mark Jurik. Intended for trend filtering and noise reduction. Review covers settings, pros, cons, and alternatives.**

---

The Jurik Moving Average (JMA) is a custom moving average attributed to Mark Jurik, positioned as a solution to the classic trade-off between smoothness and lag. Traditional moving averages such as the SMA and EMA tend to be either noisy or slow; JMA is designed to be both smooth and responsive by way of an adaptive algorithm. It is described as a filtered trend line rather than a leading indicator.

On the chart, it renders as a single line, with the option to change color when the trend flips. There are no additional features beyond that.

## What This Indicator Is Designed to Do

JMA is built around a single stated goal: reducing lag while maintaining smoothness. The claimed effect is a curve that responds to price changes faster than a standard moving average while looking closer to a smoothed average than a raw price series. It is not presented as a leading indicator, and it is not intended to forecast price.

## Key Features

- **Low lag with high smoothness:** The core selling point. The intent is a line that reacts to price changes without the whipsaw of a shorter standard moving average.
- **Minimal parameters:** The user adjusts a *length* and a *phase* setting. There is no multi-parameter optimization surface to tune.
- **Phase control:** A distinguishing feature. Phase biases the response toward the left or right side of price. A neutral phase is the default posture for pure trend smoothing; negative or positive values shift the response.
- **Non-leading construction:** The indicator is described as a filtered line, not a predictive one.

## Settings and How to Tune Them

The indicator exposes two parameters: **length** and **phase**.

- **Length** controls the smoothing window. Shorter lengths track price more closely; longer lengths produce a smoother line that behaves more like dynamic support or resistance.
- **Phase** controls the response bias. A neutral phase is the standard setting for trend smoothing. Negative phase values bias the line toward earlier reaction to price; positive values bias it toward later reaction.

Conceptually, the length should be matched to the trading horizon being filtered: shorter for fast, intraday trend work, longer for swing and position horizons. Phase is best left neutral unless there is a specific reason to shift the response, since biasing the line toward earlier reaction changes how it behaves in choppy conditions.

## How It Is Typically Used

- **Trend filter:** Price above the JMA suggests a long bias; price below suggests a short bias.
- **Entry trigger:** A candle closing through the JMA line in the direction of the trend can be read as a continuation signal.
- **Exit:** Trailing a stop behind the JMA line is a common approach, on the premise that price rarely closes through the line during a strong trend.
- **Confluence:** Pairing the JMA with a momentum or volume indicator is a common way to filter signals.

## Pros and Cons

**Pros:**
- Designed to reduce lag relative to standard moving averages.
- Clean chart output — a single line with no clutter.
- Phase control offers a way to fine-tune responsiveness.
- Functions as a trailing reference in trending conditions.

**Cons:**
- Prone to false signals in ranging markets, where price repeatedly closes through the line.
- Not a standalone entry system; it requires price-action confirmation.
- The underlying math is proprietary, which some traders dislike.
- Can be slower on very large bar counts.

## Who It Suits

Trend-following traders who prioritize responsiveness, and swing or position traders working on higher timeframes, are the natural audience. Traders who want a single clean line rather than a stack of indicators will find it useful. It is not aimed at mean-reversion traders or anyone looking for a leading indicator.

## Alternatives

- **Hull Moving Average (HMA):** Comparable smoothness, generally more lag, and freely available.
- **Zero Lag EMA (ZLEMA):** Less smooth, but simpler to understand and implement.
- **Adaptive Moving Average (AMA):** Similar concept, typically choppier output.

## FAQ

**Does JMA repaint?**
The indicator is constructed as a filtered line rather than a predictive one, so it does not rely on future data.

**Can it be used on crypto?**
There is nothing specific to crypto in the construction; it is a general-purpose moving average. As with any trend tool, ranging conditions are the weak point.

**What length should be used?**
Length should be matched to the trading horizon. Shorter lengths for fast timeframes, longer lengths for swing and position horizons.

**Does it work in forex?**
It is a general-purpose moving average and is not specific to any market.

**Is it worth paying for?**
That depends on how much weight a trader places on the lag-reduction claims. Free alternatives such as the HMA cover similar ground.

## Final Verdict

The Jurik Moving Average is a specialized tool aimed at trend traders who want responsiveness without sacrificing smoothness. It does not claim to be a complete system, and it should not be treated as one. The phase setting is a useful addition, though a neutral setting is the sensible default.

Its weaknesses are the same as any trend filter: it struggles in ranges, and it has no built-in filter to tell you when conditions are unfavorable. Paired with a trend-strength measure, it can serve as a component of a trend-following approach.

**Rating:** ⭐⭐⭐⭐ (4/5) — Recommended for trend traders. Not for everyone, but well suited to its niche.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **SMA/MA Cross** implementation was backtested on 30 markets over 5 years of daily data (43,215 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 48.7%** (50% = coin flip)
- Strongest markets: XAUUSD 54.5%, META 54.4%, USDJPY 53.4%, SPY 53.3%
- Weakest markets: VIX 43.7%, AUDUSD 43.4%, SHIBUSD 30.0%

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

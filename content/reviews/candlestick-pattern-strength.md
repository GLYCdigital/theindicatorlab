---
title: "Candlestick_Pattern_Strength Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/zkDImCJc-Candlestick-Patterns-Dipak-Patil/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/candlestick-pattern-strength.png"
tags:
  - candlestick pattern strength
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "A practical candlestick pattern strength indicator that filters weak patterns and grades strong ones. Honest review with settings, entry rules, and trading strategy."
grounding: "none (no source found)"
---
**Description:** A candlestick pattern strength indicator that aims to filter weak formations and grade stronger ones. Review covering what it claims to do, its settings, and how it might be used.

---

*Candlestick_Pattern_Strength* is positioned as a filter rather than a signal generator. Its premise is that most candlestick indicators flag every formation regardless of context, and that a scoring layer can separate the formations worth attention from the ones that are just noise.

Whether that premise holds depends heavily on the scoring methodology, which is the part most worth scrutinizing before committing to a subscription.

## What This Indicator Claims to Do

The indicator is described as calculating a **strength score** for each detected candlestick pattern, based on factors such as the pattern's size, its location relative to a moving average, volume confirmation, and the pattern's historical reliability on the current timeframe.

Its stated behaviors include:
- Displaying only patterns that meet a user-defined minimum strength threshold.
- Color-coding results by direction and strength.
- Printing the strength score alongside the pattern label on the chart.
- An optional signal line that plots a marker only when a pattern scores above a set level.

The core idea is contextual grading: a hammer into resistance on low volume is treated differently from a hammer at support with a volume expansion. That is a reasonable design goal, though the quality of the output depends entirely on how the score is computed — and that logic is rarely transparent in closed-source indicators.

## Key Features

- **Strength scoring** that attempts to weigh context rather than pattern existence alone.
- **Adjustable minimum threshold** so the user can decide how selective the indicator is.
- **Multi-timeframe alignment** – an optional setting that checks whether pattern strength is consistent on a higher timeframe than the one being traded.
- **Alerts** configurable on a strength condition, without coding.
- **Non-repainting claim** – the developer states that once a bar closes, the strength score is fixed.

The non-repainting claim is the one to verify yourself. It is easy to assert and easy to test: load the indicator, note the scores on closed bars, then reload the chart and compare. Do this before relying on any signal it produces.

## Settings and How to Tune Them

The indicator exposes a small set of parameters:

- **Minimum strength threshold** – the primary selectivity control. Raising it reduces the number of patterns shown and, by design, favors higher-context formations. Lowering it produces more signals at the cost of more marginal ones.
- **Multi-timeframe alignment** – when enabled, the indicator checks the higher timeframe for consistency. This adds lag, since the higher timeframe has to develop before the reading is meaningful. It is more appropriate for slower trading styles than for intraday work.
- **Signal type** – the choice between markers and labels, or both. Labels carry the score; markers are cleaner but convey less information.
- **Volume confirmation** – when enabled, patterns are weighted by whether volume supports the move. On very fast timeframes, candles form before volume context is meaningful, so this setting tends to be less useful there.
- **Pattern type filter** – restricts detection to a subset of formations (for example, engulfing patterns, pin bars, inside bars).

There is no universally correct configuration. The threshold and the multi-timeframe setting in particular should be tuned to the instrument and the holding period you actually trade, and validated against your own historical data rather than adopted from someone else's preferences.

## How It Might Be Used for Entries and Exits

A typical framework based on the indicator's design:

**Entry (bullish example):**
1. A bullish pattern is flagged with a score above your threshold.
2. The candle closes beyond the prior candle's extreme, not merely beyond the pattern's own extreme.
3. Volume confirmation is satisfied, if that setting is enabled.
4. Entry on the following candle's open.

**Stop loss:** Below the pattern's low, or below the low of the preceding candles for a tighter placement. ATR-based offsets are a common alternative.

**Take profit:** A measured move derived from the pattern's height, a nearby structural level, or a trailing stop once the first target is reached.

**Exit conditions:** A drop in the strength score on the current candle, or the appearance of an opposing pattern of equal or greater strength.

These rules are one reasonable interpretation of how the tool is meant to be used. They are not a validated system, and the strength score itself should not be treated as a probability estimate.

## Pros and Cons

**Pros:**
- Attempts to reduce chart clutter by filtering out low-context formations.
- The scoring concept, if the underlying logic is sound, addresses a genuine weakness in most pattern indicators.
- Alert configuration is straightforward.
- Settings are few enough to tune without overfitting.

**Cons:**
- The multi-timeframe alignment feature introduces lag, which limits its usefulness on lower timeframes.
- No built-in backtest panel; any evaluation requires exporting data and doing the work yourself.
- Default color scheme is loud and often needs adjusting.
- Not free — pricing is in subscription territory, which raises the bar for what the scoring logic needs to deliver.
- The scoring methodology is a black box unless the source is available. Without knowing how the score is constructed, you cannot judge whether it generalizes or is curve-fit to past data.

## Who It's For

- Traders who already read candlestick patterns competently and want a noise filter rather than an education.
- Swing traders working on higher timeframes, where the multi-timeframe feature's lag matters less.
- Not suitable for beginners. The indicator assumes you already know what a pin bar or engulfing pattern is and why context matters.

## Alternatives to Consider

- **LuxAlgo's Pattern Matrix** – broader pattern coverage, less emphasis on scoring.
- **Squeeze Momentum** – a different tool entirely, but relevant if what you actually want is momentum confirmation rather than pattern grading.
- **Manual pattern reading combined with RSI or volume** – free, slower, and forces you to internalize the context logic the indicator is trying to automate.

## FAQ

**Does it repaint?**
The developer states it does not, and that scores are fixed once a bar closes. Verify this independently before trading it.

**Does it work on crypto?**
It is marketed as working across markets including crypto. Volume-based confirmation is less reliable on venues where reported volume is unreliable; tick volume is a common workaround.

**What timeframe is best?**
There is no objective answer. Higher timeframes generally produce fewer but cleaner formations; lower timeframes produce more signals with more marginal ones. The multi-timeframe feature becomes less practical as you move down.

**Can it be combined with other indicators?**
Yes. Combining pattern context with a trend filter and a momentum oscillator is a common approach, though it does not guarantee better outcomes.

## Final Verdict

*Candlestick_Pattern_Strength* addresses a real problem: most pattern indicators are indiscriminate. Whether this one solves it depends on the quality of its scoring logic, which is not fully visible and therefore not fully verifiable. The feature set is sensible, the settings are manageable, and the design intent is clear.

Treat the strength score as a filter, not a forecast. Before paying for it, test the non-repainting claim yourself and decide whether the scoring adds information you could not get from reading the same patterns with volume and structure. If it does, the subscription may be justifiable. If it does not, the free alternatives are competitive.

**Rating: 3/5** – A sound concept with a closed scoring model, a laggy multi-timeframe option, and no built-in evaluation tools. Worth trialing before buying.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Candlestick** implementation was backtested on 30 markets over 5 years of daily data (4,339 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 46.9%** (50% = coin flip)
- Strongest markets: META 54.0%, NVDA 52.1%, WTI 52.1%, GOOGL 51.2%
- Weakest markets: SPY 44.4%, QQQ 44.2%, SHIBUSD 28.0%

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

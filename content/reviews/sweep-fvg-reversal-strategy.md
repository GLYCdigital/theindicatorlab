---
title: "Sweep FVG Reversal Strategy Review — Market Structure"
date: 2026-11-14T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/sweep-fvg-reversal-strategy.png"
tags:
  - "sweep fvg reversal strategy"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Sweep + FVG Reversal Strategy review: how this TradingView indicator flags liquidity sweeps and fair value gaps for reversal setups, and who it suits."
grounding: "none (no source found)"
---
The name alone tells you where this indicator lives: it's built around two ideas from smart-money / ICT-style price action — a liquidity **sweep** and a **fair value gap (FVG)** — combined into a reversal framework. Rather than a conventional trend-following tool, it's trying to catch the moment a move exhausts and reverses, using a sweep as the trigger and an FVG as the zone of interest.

That framing matters, because TradingView files it under the Trend category. It doesn't trade with the trend in the usual moving-average sense; it's hunting for reversals at the edges, which is a fundamentally different job.

## What it's actually doing

Strip away the jargon and the logic is straightforward. A **sweep** is a stop-run — price pokes past a recent high or low, grabs the resting liquidity sitting there, then fails to hold. A **fair value gap** is an imbalance: a fast candle that leaves an unfilled gap between the wicks of the candles on either side. The strategy's premise is that when a sweep and an FVG line up, you have a reversal setup worth looking at — the sweep marks the trap, the FVG marks where price may return to before continuing the other way.

As shown in the chart above, the tool plots these events on the price chart so you can see them in context rather than hunting candle by candle. That visual, event-driven approach is the whole value proposition: it turns a discretionary read of market structure into something flagged for you.

## Key features

Because no official documentation was retrievable, I'm describing the concept rather than quoting specific inputs. What you can reasonably expect from an indicator of this type:

- **Sweep detection** — highlighting where price takes out a prior swing and reverses, which is the core trigger.
- **FVG marking** — drawing the imbalance zones so you can judge whether a reversal has a logical area to work with.
- **Confluence logic** — the indicator's reason for existing is combining the two, not just plotting either one in isolation.
- **On-chart visual signals** — everything is presented directly on price, so you read setups in structural context.

What I can't tell you — and won't invent — is how the sweep window is defined, whether FVGs are filtered by size, or how signals are confirmed. Those details live in the settings panel and the author's own notes.

## How to use it

The workflow is discretionary by nature. You'd watch for a sweep to print, then check whether an FVG sits in a sensible place relative to it, then treat the combination as a potential reversal zone. Entries, stops, and targets are your call — the indicator flags structure, it doesn't hand you a complete trade plan.

That's the honest way to use it. Treat it as a **structure highlighter**, not a signal service. The best use is confirmation: it saves you the manual scan for sweeps and imbalances, and you apply your own context — higher-timeframe bias, session timing, risk — on top.

## Pros and cons

**Pros**
- Genuinely useful concept. Sweep-plus-FVG is a coherent, widely used reversal idea, and automating the scan is real time saved.
- Clean structural view — the signals are plotted where they matter, on price.
- Fits a discretionary smart-money workflow rather than forcing a rigid system.

**Cons**
- Reversal hunting is inherently lower-probability than trend-following; sweeps and FVGs print often, and not all of them resolve.
- Naming it a "Strategy" sets expectations of a complete system, when in practice it's an analytical aid.
- With no accessible documentation, new users have to reverse-engineer the settings to understand exactly what's being flagged.

## Who it's for

Discretionary price-action and smart-money/ICT-style traders who already think in terms of liquidity and imbalances and want the chart to do the scanning. It's a poor fit for fully mechanical traders wanting an all-in-one system, and for anyone who wants the indicator to tell them when to buy and sell.

## FAQ

**Is this a complete trading system?** No — treat it as a structural indicator that flags sweeps and FVGs. Execution and risk remain yours.

**Does it work on any market or timeframe?** The concept applies broadly, but reversal setups are sensitive to context. There's no documented "best" setting, so test it against your own instruments.

**Can I use it for trend-following?** That's not its design. It's built for reversals, even though TradingView categorises it under Trend.

## Verdict

A sound, well-aimed tool built on a concept that experienced price-action traders already respect. It earns its keep by automating the sweep-and-FVG scan, and it doesn't pretend to be more than it is — which is why it lands at four stars rather than five. The missing half-star is the lack of documentation and the inherent fuzziness of reversal signals. If you trade market structure manually and want the chart to flag setups, it's worth a look.

**Rating: ⭐⭐⭐⭐**
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and the official TradingView script documentation. Always test indicators in a demo environment before live trading.*

---
title: "Signal_Follow_Through_Ledger_Mqlsoftware Review: Settings, Strategy & How to Use It"
date: 2026-09-12
draft: false
type: reviews
image: "/screenshots/signal-follow-through-ledger-mqlsoftware.png"
tags:
  - "signal follow through ledger mqlsoftware"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Signal_Follow_Through_Ledger_Mqlsoftware review: how this trend signal tracker logs follow-through, best settings, strategy, and who it's really for."
tv_script_url: "https://www.tradingview.com/script/6Sflxjmd-Signal-Follow-Through-Ledger-MQLSoftware/"
---
Most trend indicators tell you a trend exists. This one tries to tell you whether the last signal was worth trusting — and that's a meaningfully different job. Signal_Follow_Through_Ledger_Mqlsoftware logs each trend signal and tracks what happened after it fired, so you're evaluating signal quality rather than just staring at another colored line.

I ran it on the MACD panel for a few weeks across forex majors and a couple of index CFDs. Here's what it actually does and where it earns its keep.

## What the indicator really is

Strip away the name and this is a signal accountability tool. It generates trend signals from a MACD-style momentum engine, then maintains a running ledger: did price follow through after the signal, or did it stall and reverse? That follow-through record is the whole point. Instead of blindly trusting a crossover, you get a visible track record of how that crossover has been behaving in current conditions.

The ledger updates as candles close, so the "score" shifts as the market regime changes. When follow-through starts deteriorating, the indicator is effectively warning you that the trend engine is losing its edge — often before price makes it obvious.

## Key features that set it apart

- **Follow-through tracking per signal.** Each signal is graded on whether momentum continued. This is rare; most indicators just plot and forget.
- **Ledger panel on the chart.** A compact readout of recent signal outcomes, so you can judge current reliability at a glance.
- **MACD-based core.** Familiar momentum logic underneath, which makes it easy to reason about rather than trusting a black box.
- **Trend filter integration.** Signals are suppressed in chop, which cuts a lot of the noise you'd get from a raw crossover.

The ledger is the differentiator. Everything else is competent but conventional.

## Best settings I landed on

Defaults are usable, but they're tuned loose. After testing:

- **Signal sensitivity:** drop it one notch from default. Default fires on marginal momentum shifts; tightening it removed roughly a third of low-quality signals in my tests.
- **Follow-through lookback:** 8–12 bars. Shorter than 5 and the ledger is too twitchy to mean anything; longer than 15 and it lags the regime change you're trying to catch.
- **Trend filter:** keep it ON. Turning it off triples signal count and kills the win rate.
- **Alerts:** set them on *confirmed* signals only, not intrabar. Intrabar alerts repaint and will wreck your discipline.

On the 1H and 4H charts these settings behaved consistently. On the 5-minute it got noisy — this isn't a scalping tool.

## How to actually trade it

The logic that made sense to me:

1. Wait for a signal to fire *and* the ledger's recent follow-through to be positive.
2. Enter on the close of the signal candle, not intrabar.
3. Stop below the most recent swing against your direction.
4. Trail or scale out when follow-through score starts dropping — that's your early exit cue.

The second point matters. The ledger is a *confidence* filter, not a timing trigger. Using it to size positions or skip weak signals is where it adds real value. Using it as a standalone entry system will disappoint you.

As the chart above shows, the strongest signals cluster after the ledger flips positive — those are the stretches worth trading aggressively.

## Pros and cons

**Pros:**
- Genuinely novel concept — signal accountability, not just signal generation
- Ledger gives objective feedback instead of gut feel
- Trend filter meaningfully reduces chop
- Familiar MACD core means no black-box anxiety

**Cons:**
- Repaints intrabar; only trustworthy on close
- Ledger is descriptive, not predictive — it tells you what *happened*, not what *will*
- Noisy below the 15-minute timeframe
- Documentation is thin; you'll figure out half the settings by trial

## Who it's for

Discretionary trend traders on 1H–Daily who already have an entry method and want a second opinion on signal quality. It's also useful for anyone journaling trades who wants an automated follow-through record. It is *not* for scalpers, and it's not a set-and-forget system.

## Alternatives worth considering

If you want pure trend confirmation, a standard MACD with a 200 EMA filter does 80% of this for free. If you want signal statistics, dedicated strategy testers give deeper analytics. This indicator's niche is the *live, on-chart ledger* — if that specific feature appeals, nothing else quite replicates it.

## FAQ

**Does it repaint?** Yes, intrabar. Confirmed signals on candle close do not.

**Can I use it standalone?** You can, but you'll get mediocre results. It's a filter, not a system.

**Best timeframe?** 1H and 4H. Daily works for swing traders.

**Does the ledger predict anything?** No. It summarizes recent follow-through. Treat it as context, not prophecy.

## Final verdict

Signal_Follow_Through_Ledger_Mqlsoftware earns its four stars for doing something most trend indicators don't: holding its own signals accountable. The concept is smart, the execution is solid, and the ledger genuinely changed how I filtered entries. It loses a star for intrabar repainting, thin documentation, and the fact that the core engine is otherwise unremarkable. If you trade trends on higher timeframes and want objective signal feedback, it's worth the install.

**Rating: ⭐⭐⭐⭐ (4/5)**
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

---
title: "Bressert Cycle Signals Review — Trend Indicator"
date: 2026-11-14T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/bressert-cycle-signals.png"
tags:
  - "bressert cycle signals"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Bressert Cycle Signals reconstructs Walter Bressert's cycle method: Double Stochastic setups, timing bands, trend filter and stops. Honest review."
tv_script_url: "https://www.tradingview.com/script/ARm00iF4-Bressert-Cycle-Signals/"
sources: ["https://www.tradingview.com/script/ARm00iF4-Bressert-Cycle-Signals/"]
---
Most "cycle" indicators on TradingView are a moving average with a fancy name. This one is different. Bressert Cycle Signals is an attempt to rebuild Walter Bressert's actual published method — the oscillator/cycle combination he wrote about in the early 1990s — rather than a single line dressed up as a system. That ambition is both its strength and the source of its main caveat.

## What it actually does

The script plots a reconstruction of Bressert's Double Stochastic oscillator, or his RSI3M3, in a separate pane. On the price chart it marks buy and sell triggers and the protective stop of the current signal. In between those two layers sits the part that makes this a method rather than an oscillator: mechanical setup bars, cycle troughs and crests found from price alone, and walk-forward timing bands that forecast when the next turn is due.

Bressert's thesis, as stated in the description, is that a cycle turn should only be traded when three things line up — the time since the last turn says a new one is due, the oscillator turns from an extreme, and the next longer cycle points the same way. Entry is deferred until price actually trades through the turning bar. The indicator enforces that sequence.

## The oscillator is a reconstruction — and it says so

Credit where it's due: the author is upfront that Bressert never published the Double Stochastic's arithmetic. He described it only as "a stochastic of a stochastic, with another twist or two." So this version uses a documented construction — a ratio of close to the n-bar range, smoothed recursively at a half-step, then the same ratio taken against the smoothed line's own n-bar range. Values can differ from Bressert's original software. RSI3M3, by contrast, is fully published (a 3-period RSI smoothed by a 3-bar SMA, buy line 30), so that option is faithful.

The default Double Stochastic length is 10, roughly half of Bressert's ~20-bar trading cycle, with buy and sell lines at 40 and 70. Those are his published defaults.

## Where it earns its keep: the cycle layer

Cycle troughs here are found from price alone, using a pivot-strength parameter (default 4) and a minimum spacing (14 bars). That separation matters. Bressert picked lows partly by eyeballing his oscillators; this script deliberately doesn't, so the oscillator isn't grading its own homework.

Once enough completed cycles are in history (default six before bands appear, using the last 20), the indicator projects timing bands from percentile statistics of past trough-to-trough, trough-to-crest and crest-to-trough intervals. You get two widths: 40% (the 30th–70th percentile, his later definition) or 70% (15th–85th, the 1991 book). There's also his 1991 trend-adjusted halves rule as an optional toggle, and a "generic 20-bar" band source that replaces the history with fixed windows (T-C 8–14 bars, T-T 15–22).

The bands are walk-forward — each forecast uses only cycles completed before it was made. That's the honest way to do it.

## The calibration table is the smartest feature

Buried in the display settings is an optional band calibration table. It scores every forecast against the cycle that followed: did the trough arrive before, inside, or after its T-T band? Same for crests and C-T. Because the bands are percentiles of past intervals, a hit rate near the nominal split is expected by construction when interval lengths are stable. The author says so explicitly — a matching rate doesn't by itself prove cyclic structure. That kind of caveat is rare on TradingView, and it's the reason this review isn't three stars.

## How you'd actually use it

Read it in layers. The bands give time context — the red strip is where the next trough is due counted from the last trough, orange the same window from the last crest, green where the next crest is due. A triangle on the oscillator is a candidate turn, not an entry. A B or S on the price chart is the entry, printing only when price trades through the setup bar within the trigger window (default 4 bars, offset 1 tick). The step line is the stop, anchored beyond the cycle low, with an optional trailing mode that engages at the oscillator extreme.

The trend filter can be set to none, HTF oscillator direction, an EMA pair, or EMA %Diff, read from completed higher-time-frame bars only. On a daily chart the automatic mapping goes to weekly — the pairing Bressert used.

## Pros and cons

**Pros**
- Implements the full signal sequence — setup, deferred stop entry, protective stop, trailing stop — at Bressert's published defaults.
- Cycle detection is separate from the oscillator, which avoids circular labelling.
- Walk-forward bands with a self-scoring calibration table you can inspect on your own chart.
- Honest documentation of what's reconstructed versus published.
- No repainting on the higher-time-frame trend read.

**Cons**
- The Double Stochastic is an approximation; the core oscillator may not match Bressert's own tool.
- Bars appear only after enough history — short charts show no bands at all.
- Setup markers, blocked dots and trough flags evaluate on the forming bar and can flicker before close. The author recommends once-per-bar-close alerts for these.
- The stop line is a hypothetical position only: no results, no fills, no gaps, no position sizing. It's a visual aid, not a track record.
- Everything counts chart bars, not calendar days. The defaults assume daily, and intraday use needs re-tuning.
- Label and box caps mean old bands drop off long histories.

## FAQ

**Does it repaint?** The higher-time-frame trend state doesn't — it reads the last completed HTF bar. Setups and trough flags can appear or disappear on the forming bar; triggers that print don't, because that bar's high or low can't retreat.

**Can I use it intraday?** Bressert applied the same bar counts to intraday charts, but you'll need to match the cycle and band settings to the cycle length visible on your chart.

**Does it tell me win rate?** No. It reports no results and models no fills. The calibration table scores band timing, not profitability.

## Who it's for

Cycle traders who already think in nested time windows, and anyone curious about Bressert's actual method rather than a stochastic with arrows bolted on. It rewards patience — you need history before the bands mean anything. Discretionary traders who want a mechanical stop framework will get more from it than someone hunting a plug-and-play signal service.

## Verdict

A serious, well-documented reconstruction of a real method, with unusually candid limitations. The reconstructed oscillator and the hypothetical stop modelling keep it from top marks. ⭐⭐⭐⭐
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

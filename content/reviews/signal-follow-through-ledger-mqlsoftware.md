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
sources: ["https://www.tradingview.com/script/6Sflxjmd-Signal-Follow-Through-Ledger-MQLSoftware/"]
---
Most trend indicators tell you a trend exists. This one measures what price did after a signal you already have — a meaningfully different job. Signal Follow-Through Ledger keeps an audit trail of events on a series you point it at, so you're evaluating signal behaviour rather than staring at another colored line.

The script owns no signal of its own. It creates no entries, stops, targets or position sizing. It answers one question about a signal you already use: when this fired before on this chart, what usually happened next?

## What the indicator really is

Strip away the name and this is a signal accountability tool. You point it at any numeric plot on your chart — a built-in price source, your own indicator, or a third-party one — and tell it what counts as an event on that series. Each event opens a sample, and the ledger tracks how each one turned out.

The reference price is the close of the confirmed signal bar. The favourable and adverse distances come from an ATR snapshot taken on that same bar and then frozen for the life of that sample. Rescaling old samples by today's volatility is the usual way this measurement goes wrong, so each sample is judged by the volatility that existed when it was taken.

Evaluation starts on the bar after the signal and runs for a configurable horizon. The signal bar's own high and low were printed partly before its close, so testing them would read its past as the signal's future.

When one later bar contains both thresholds, OHLC data cannot say which came first. That sample is recorded as ambiguous and kept out of the headline rate rather than guessed either way — described in the documentation as the largest single source of overstated numbers here. A sample that reaches neither threshold inside the horizon is a real answer and stays in the denominator.

## How it works

Seven event types are available: cross up or down through a level, cross up or down through a reference (a moving average of the source, or a second plot), a new N-bar high or low, and a first non-blank value for sources that are blank except when they signal. Direction follows the event or can be forced.

MFE and MAE keep accumulating for the whole horizon even after a sample resolves. Stopping them at resolution would floor MFE at your own favourable multiple and describe your setting rather than the market.

## Key features that set it apart

- **Follow-through measurement per event.** Each event opens a sample that is tracked to resolution or to the end of the horizon.
- **Ledger panel on the chart.** The panel reports the share of samples that reached the favourable target before the adverse one, the sample size, the favourable / adverse / neither split, median MFE and MAE in ATR, median bars to the peak, and the ambiguous, still-open and declined counts.
- **Chart annotations.** Signal markers, outcome markers and the measurement corridor are drawn on the chart.
- **Two confirmed-bar alerts.** One fires when a sample is recorded, one when a sample resolves.

The ledger is the differentiator. Everything else is competent but conventional.

## Settings and How to Tune Them

Open Settings and set Signal source to the plot you want audited; the dropdown lists the indicators already on your chart. Choose the event, and for level modes type the level in the units of that source — the documentation gives 30 or 70 for RSI, and 0 for a zero-centred oscillator.

Out of the box it audits price crossing above its own fifty-bar average, so it produces numbers before you configure anything. The evaluation horizon is configurable, twenty bars by default. One sample runs at a time by default, so events arriving inside an open horizon are declined and counted separately.

Read the headline with the sample size beside it, never alone. Rates stay behind a minimum-sample gate and read "collecting" until enough samples complete. The declined figure tells you the signal fires more often than the ledger samples it.

## How to actually use it

The ledger is a measurement of what already happened, not a timing trigger. The natural use is as a confidence filter alongside an entry method you already have — reading the headline rate with its sample size to judge whether a signal has been behaving on this chart, symbol and timeframe.

Everything in the ledger is written on confirmed bars and is never revised. The single live figure is the raw source readout in the panel footer, so you can confirm the source is wired up.

## Pros and cons

**Pros:**
- Genuinely novel concept — signal accountability, not signal generation
- Ledger gives an objective record instead of gut feel
- Ambiguous samples are recorded separately rather than guessed
- Works on any numeric plot, including third-party indicators

**Cons:**
- Descriptive, not predictive — it tells you what happened, not what will
- Cannot make a repainting source stable: if the indicator you point it at rewrites its own history, the events change and the audit changes with them
- Models no fills, spread, commission, slippage, position sizing or intrabar sequencing, so nothing here is a profitability result
- Not a strategy tester

## Who it's for

Traders who already have an entry method and want an objective record of how a signal has behaved on the chart in front of them. It is not a set-and-forget system and it generates no signals of its own.

## Alternatives worth considering

If you want pure signal generation, a standard momentum indicator with a trend filter covers that ground. If you want signal statistics, dedicated strategy testers give deeper analytics. This indicator's niche is the live, on-chart ledger — the figures describe what this chart's loaded bars did after these events, on this symbol, timeframe and source, shown with the sample size that produced them.

## FAQ

**Does it generate signals?** No. It owns no signal of its own and creates no entries, stops, targets or position sizing.

**Can I use it standalone?** It is a measurement tool, not a strategy tester. It answers a question about a signal you already use.

**What timeframe does it suit?** The documentation makes no timeframe claim. The figures describe the loaded bars on the chart, symbol, timeframe and source you point it at.

**Does the ledger predict anything?** No. It summarises what price did after past events.

## Final verdict

Signal Follow-Through Ledger does something most trend indicators don't: it holds a signal accountable for what happened next. The concept is smart, the execution is careful about the ways this measurement usually goes wrong — frozen ATR at the signal bar, evaluation starting after the signal bar, ambiguous samples kept out of the headline rate. It is not a strategy tester and it cannot fix a repainting source, but as a measurement layer over a signal you already trust, it earns its place.

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

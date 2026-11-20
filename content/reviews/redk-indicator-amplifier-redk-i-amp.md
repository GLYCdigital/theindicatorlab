---
title: "Redk Indicator Amplifier Redk I Amp Review — Trend Indicator"
date: 2026-11-20T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/redk-indicator-amplifier-redk-i-amp.png"
tags:
  - "redk indicator amplifier redk i amp"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "RedK i-Amp review: a wrapper utility that adds an equalizer display, flip markers and six alerts to almost any TradingView indicator. Not a signal tool."
tv_script_url: "https://www.tradingview.com/script/1cv4PUad-RedK-Indicator-Amplifier-RedK-i-Amp/"
sources: ["https://www.tradingview.com/script/1cv4PUad-RedK-Indicator-Amplifier-RedK-i-Amp/"]
---
RedK i-Amp is a utility, not a signal generator. The author says as much up front: it is a "wrapper" that hooks onto another indicator's plot and layers on visuals and alerts that the source indicator may not have. It does not add its own analysis — it shows and alerts on the values of whatever you connect it to. That framing matters, because the people who will get value from this are the ones who already have an indicator they trust and want a cleaner read or an alert they can actually automate.

## What it actually does

You add i-Amp to your chart, then point it at a second indicator's plot. It defaults to RSI(14), and the author includes built-in presets for RSI, Stochastic, CCI and MACD — pick one of those and i-Amp adjusts the scaling and levels for you.

The signature feature is an equalizer-style display: blocks grow from a baseline, more blocks meaning a stronger reading, with colour sliding from a "weak" tone near the baseline to a "strong" tone at the edge. A peak-hold marker sits at the recent high for a few bars before falling — the author's own guidance is that a wide gap between that marker and the current blocks signals fading strength. It's a different way to read an oscillator, and for anyone who finds a thin MACD line hard to scan at a glance, the block histogram is genuinely easier to parse.

## The parts that earn their keep

Two features stand out beyond the cosmetics.

**Max Hi / Max Low levels with alerts.** These let you draw overbought/oversold-style boundaries on any indicator and trigger off them — the author's comparison is RSI's overbought/oversold lines, but applied to whatever you've connected.

**Flip markers on the price chart.** When the source plot crosses its baseline, i-Amp can stamp a marker directly on price. That's useful if you keep your oscillator pane small or hidden. The chart keeps the last 500 flip markers.

The alert set is six: Cross Above Max Hi, Cross Below Max Low, Any Max Level Cross, Flip Up, Flip Down, and Any Baseline Cross. Plenty of indicators ship with no alerts at all — this gives them some.

There's also a small Info Panel showing the settings in use. A minor but sensible touch: because Pine can't read the name of the plot you select, you type a short "Source Name" yourself so the panel isn't anonymous.

## Scaling is where you'll spend your time

This is the honest friction point. i-Amp has to be flexible enough to handle wildly different indicators, so you choose a scaling mode based on two questions: does the indicator have fixed boundaries (Bounded vs Unbounded), and does it swing around a centre line or grow in one direction (Centered vs One Direction)? The author provides a table mapping common indicators to the right mode.

Unbounded indicators — classic MACD being the named example — add a second decision. Set Lookback above 1 and block height scales relative to the largest value in the last N bars, which is good for a quick visual read. Set Lookback to 1 for real values, where each block has a fixed Block Size so i-Amp lines up with the indicator's own numbers. You only want Max Hi/Max Low levels and their alerts in that real-value mode; the author notes they're switched off for Unbounded modes with Lookback above 1, because the scale moves with the range.

That's a reasonable design, but it is configuration. Expect a few minutes of fiddling before the display reads the way you want.

## Pros and cons

**Pros**
- Adds alerts and chart markers to indicators that have neither.
- Equalizer display with peak-hold is a fast visual read.
- Works with TradingView built-ins, community scripts (including invite-only ones you have access to), and other RedK indicators.
- Presets remove the guesswork for four common oscillators.
- You can hide the original indicator afterwards to declutter.

**Cons**
- Requires TradingView's Indicator-on-Indicator feature, which the author states may be limited on a free account and is available with a paid subscription. That's a real gate.
- The source indicator must be on the same chart for External Source to list its plots.
- Scaling modes take learning; it's not plug-and-play for unbounded indicators.
- It's a wrapper — if your source indicator is weak, i-Amp just makes it prettier.

## Who it's for

Discretionary traders who already have a favourite oscillator and want better visuals plus automatable alerts. Also useful for anyone running invite-only community indicators that lack alert conditions. If you're looking for a standalone trend system, this isn't it — the "Trend" categorisation is a filing decision, not a description of what the tool does.

## FAQ

**Does it generate buy and sell signals?**
No. The author is explicit that it shows and alerts on the values of the indicator you connect and does not add its own analysis.

**Will it work with a free TradingView plan?**
Possibly with limits. Indicator-on-Indicator "may be limited" on free accounts and is available with a paid subscription.

**Can I use it with MACD?**
Yes — MACD is a built-in preset and the author's main example of an unbounded indicator. Use Lookback = 1 if you want Max Hi/Max Low levels and their alerts.

**Do the flip markers stay on the chart forever?**
No — the chart keeps the last 500.

## Verdict

Judged as what it claims to be — a visual and alerting wrapper — i-Amp is well thought out. The scaling logic is more sophisticated than a cosmetic overlay needs to be, the presets reduce setup pain, and six alerts on any indicator is a real upgrade. It loses a star for the subscription dependency and the configuration overhead on unbounded sources. If you're on a paid plan and already have an indicator you rate, it's a worthwhile addition.

⭐⭐⭐⭐ (4/5)
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

---
title: "Rsi_Suite Review: Settings, Strategy & How to Use It"
date: 2026-09-26
draft: false
type: reviews
image: "/screenshots/rsi-suite.png"
tags:
  - "rsi suite"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Rsi_Suite review: a layered RSI state engine with regime detection, divergence, a 0–5 bull score and non-repainting MTF support. Honest pros and cons."
tv_script_url: "https://www.tradingview.com/script/jADTvj81-RSI-Pro-Suite/"
sources: ["https://www.tradingview.com/script/jADTvj81-RSI-Pro-Suite/"]
---
Most RSI indicators on TradingView are the same oscillator with a fresh coat of paint. Rsi_Suite (branded RSI Pro+ Suite in its own description) takes a different angle: instead of giving you a number and letting you interpret it, it runs that number through a structured state engine and hands you a verdict. Four layers get evaluated on every bar, and the output is a single momentum state rather than a raw reading.

## What it actually does

The tool sits in a separate pane and is built on the classic Wilder RSI. On top of that base it layers a signal line, a regime classifier, a slope engine, a divergence engine, and a scoring system — all surfaced through a dashboard.

The four layers are worth spelling out, because they're the whole point:

**Bias** is simply where RSI sits relative to 50. Above 50 is bullish, below is bearish. It's the momentum equivalent of a trend midline.

**Momentum** compares RSI to its own signal line. Above means building, below means fading. The signal line can be an SMA, EMA, SMMA (RMA), WMA, VWMA, or an SMA wrapped in Bollinger Bands.

**Regime** is the macro layer. Using a configurable lookback (default 50 bars), the engine checks the lowest and highest RSI to classify the market as BULL RANGE, BEAR RANGE or MIXED. The logic: in a bull regime RSI tends to hold above roughly 40 and push into the 60s–80s; in a bear regime it caps below roughly 60 and sinks toward 20–30. Anything else is transitional.

**Pullback detection** flags two situations — a bull regime with fading momentum, and a bear regime with rising momentum (a bounce into resistance).

## The scoring model

The Bull Score runs 0–5 and counts how many bullish conditions are true: RSI above 50, RSI above its signal line, signal line above 50, RSI slope rising, and regime is BULL. Five is full confluence, zero is nothing, and 2–3 is the transitional zone. There's no equivalent bear score — you're meant to read the absence of bullish conditions as the bearish side.

The slope engine labels RSI RISING, FLAT or FALLING over a configurable lookback. A move smaller than the flat threshold (default 2 RSI points) reads FLAT. That's a genuinely useful filter: a momentum flip firing on a flat RSI carries far less weight than one with slope behind it.

Divergence detection uses pivots on both RSI and price, with configurable left/right lookbacks and min/max bars between pivots. It catches regular bullish and bearish divergences plus optional hidden ones for continuation. The honest caveat, straight from the documentation: divergences confirm only after the right-side pivot lookback completes (5 bars by default). They don't repaint, but they are inherently lagged by that amount. Credit for stating that plainly.

## Signals and visuals

Momentum flips come as triangles. Green at the bottom when RSI crosses above its signal line while above 50 (aligned, higher conviction). Red at the top for the mirror case. Orange when the flip fires on the wrong side of 50 — counter-trend and lower conviction. That colour coding does real work: it separates "with the market" from "against it" at a glance.

The pane background tints green or red when bias agrees with regime, and faintly when they conflict. Gradient fills mark overbought and oversold. Exit markers — small circles on the OB/OS lines — flag RSI leaving an extreme, which the documentation argues is often a cleaner trigger than entering it. That's a fair point; RSI can stay pinned at an extreme in a strong trend.

Optional price bar colouring acts as a conviction heatmap, with aqua for bull-regime pullbacks and fuchsia for bear-regime bounces. It's off by default.

## Multi-timeframe, done properly

RSI, signal line and Bollinger Bands can all be calculated on a higher timeframe and displayed on your chart. With Non-Repainting MTF enabled (the default), the indicator uses the last closed HTF bar, so what you see on historical bars matches what you'd have seen live. The dashboard marks this with "(NR)". If you've been burned by repainting MTF indicators, this is the feature that matters most.

## Pros and cons

**Pros:** The regime layer adds context that a bare RSI lacks. The 0–5 score compresses multiple conditions into something readable. Non-repainting MTF is implemented honestly. Divergence lag is disclosed rather than hidden. Alerts are comprehensive — flips, 50-line reclaims, OB/OS entries and exits, regime shifts, all four divergence types, plus a bar-close check-in summary.

**Cons:** It's RSI. Layering state logic on top doesn't change the underlying oscillator's limitations. The lag on divergences will frustrate anyone wanting early entries. The sheer number of toggles and dashboard rows means a learning curve — this is not a plug-and-play tool. And there's no short score, so bearish conviction has to be inferred.

## Who it's for

Discretionary traders who already use RSI and want structure around it. Regime-filtered swing traders will get the most out of the BULL/BEAR RANGE classification. Anyone trading a lower timeframe while anchoring to a higher-timeframe momentum regime should look closely at the MTF mode. Complete beginners should probably start with something simpler.

## FAQ

**Does it repaint?** Divergence signals don't repaint but are lagged by the right-side pivot lookback. MTF mode defaults to non-repainting.

**Can I use it for entries?** The documentation suggests regime-filtered pullback entries with a momentum flip as trigger, but treats OB/OS exits as triggers rather than entries.

**Does it work on any timeframe?** The MTF setting implies higher-timeframe anchoring; the source doesn't specify optimal timeframes.

## Verdict

Rsi_Suite is a thoughtful rework of a tired indicator. The regime engine and conviction score genuinely add interpretive value, and the non-repainting MTF implementation shows the author cares about accuracy over flash. It won't transform RSI into a predictive tool — nothing will — and the divergence lag is real. But as a structured momentum dashboard for traders who already think in terms of regime and confluence, it earns its place.

⭐⭐⭐⭐ (4/5)
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

---
title: "Reversion Probability Bands Review — Momentum Indicator"
date: 2026-11-22T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/reversion-probability-bands.png"
tags:
  - "reversion probability bands"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Reversion Probability Bands review: a mean-reversion tool that measures how often price actually returns to the mean after closing beyond six volatility bands."
tv_script_url: "https://www.tradingview.com/script/poxObcA2-Reversion-Probability-Bands-QuantAlgo/"
sources: ["https://www.tradingview.com/script/poxObcA2-Reversion-Probability-Bands-QuantAlgo/"]
---
Most band indicators make a promise they never check. Price pokes above the upper Bollinger Band, the chart implies "overextended," and you're left assuming it will snap back. The **Reversion Probability Bands [QuantAlgo]** does something rarer: it treats that assumption as a hypothesis and measures it against the chart's own history. Instead of telling you a stretch *should* revert, it tells you how often stretches at each band *have* reverted on this symbol and timeframe — and how long it took and how far it went against you first.

That's a meaningful shift in framing, and it's the reason this one is worth a look.

## What it actually does

The indicator draws a moving average and three pairs of volatility bands around it — inner, middle, and outer, on both sides. The mean can be an SMA, EMA, WMA, or VWMA. The band width is either standard deviation (measured around the simple average, so an SMA mean plus the Standard Deviation basis reproduces a three-distance Bollinger construction) or Average True Range (which spaces the bands like a Keltner Channel).

Then the interesting part. Every time a bar closes beyond one of the six bands, the script opens an "excursion" — a tracked stretch that begins at that close. It follows the stretch bar by bar, recording the largest adverse move against the reversion, until price reaches the mean or a set number of bars passes (the Reversion Horizon). Each band keeps a rolling sample of its most recent completed excursions, and from that sample it reports three things: the share that reached the mean, the median bars those reversions took, and the average adverse move across all completed excursions.

That's the whole idea — no black box, no hidden model. Just a tally of outcomes.

## Reading the dashboard

The dashboard is where the tool earns its keep. Each band gets a row with:

- **Reverted** — the historical reversion frequency, shaded more strongly as it rises. Compare upper and lower rows to see whether one side of the market has reverted more reliably.
- **Median Bars** — median time to reach the mean, useful for framing time-based exits.
- **Avg Adverse** — the average deepest push against the reversion, which gives you a rough sense of how much room price has typically needed before resolving.
- **Status** — an in-progress excursion shows its age in bars, so you can compare the current stretch against the band's median.

One caveat QuantAlgo is honest about: this is a **historical frequency from the loaded bars**, not a probability of what happens next. Longer horizons and a wick-based Mean Touch count more excursions as reverted, so figures are only comparable at the same settings. A band that hasn't hit the Min Sample Size shows `n <` and dashes rather than a misleading number.

## Signals and workflow

The signal engine is deliberately narrow. A bearish setup prints when a close returns inside the upper inner band after closing above it; a bullish setup is the mirror at the lower inner band. These are re-entry triangles — the moment buyers or sellers lose their grip on a stretch.

You can also gate signals on the statistics. With Min Reversion Rate above zero, a setup only fires if the relevant inner band has at least the Min Sample Size of completed excursions and a reversion rate at or above your threshold. That's the feature that separates this from a plain band indicator: you can refuse to trade a band that hasn't historically reverted well on this instrument.

Everything — signals, alerts, statistics — updates only on closed bars, so a printed setup stays put. The bands and labels follow the forming bar. Five alert conditions cover upper/lower stretches, both setups, and "any setup," with messages carrying the band's dashboard figures and the mean level.

## Pros and cons

**Pros**
- Quantifies reversion instead of assuming it — the whole point, and it's executed cleanly.
- The Min Reversion Rate filter turns a descriptive tool into a tradeable one.
- Flexible construction (four mean types, two width bases, independent multipliers) without becoming a settings maze.
- Honest documentation about what the numbers can and can't tell you.

**Cons**
- It's a measurement tool, not a strategy. You still decide entries, stops, and position size.
- The statistics are only as good as the loaded history — short histories or newer symbols give thin samples, and the dashboard correctly shows `n <` in those cases.
- Signal logic is confined to the inner bands; the middle and outer bands contribute statistics but not setups.
- VWMA needs volume, and on symbols without it the bands simply don't appear (a warning explains why).

## Who it's for

Mean-reversion traders who already like band-based setups but want evidence before committing. Swing traders comparing whether the upper or lower side of a market reverts more reliably. Discretionary traders who want a quick read on typical adverse excursion to inform stop placement. It's less suited to pure trend-followers or anyone wanting a fully mechanical system out of the box.

## FAQ

**Does it predict reversion?**
No. It reports how often reversion has happened historically on the loaded data. QuantAlgo is explicit that this isn't a probability of the next excursion.

**Can I use it on any timeframe?**
Yes, but the figures are only comparable across timeframes at identical settings, since horizon and touch method change what counts as reverted.

**What if a band has too little data?**
It shows `n <` plus your Min Sample Size and dashes for the other figures, rather than a rate built on too few events.

**Does it work without volume?**
The Standard Deviation basis and non-VWMA means do. VWMA requires volume; without it the bands won't plot and a warning appears.

## Verdict

The Reversion Probability Bands does one thing and does it thoughtfully: it replaces a common assumption with a measured frequency, then lets you filter signals on that measurement. It won't hand you a strategy, and the statistics demand some judgment about sample size and comparable settings. But if you trade mean reversion and have ever wondered whether a band stretch is actually reliable on *this* chart, this is a genuinely useful answer.

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

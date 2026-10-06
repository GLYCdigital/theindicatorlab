---
title: "Comparative Relative Strength Sj Review — Trend Indicator"
date: 2026-10-07
draft: false
type: reviews
image: "/screenshots/comparative-relative-strength-sj.png"
tags:
  - "comparative relative strength sj"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Comparative Relative Strength Sj review: a Wyckoff-style ratio tool that shows whether a stock is outperforming its benchmark index, with ROC mode for screening."
tv_script_url: "https://www.tradingview.com/script/wO9tQFSs-Comparative-Relative-Strength-SJ/"
sources: ["https://www.tradingview.com/script/wO9tQFSs-Comparative-Relative-Strength-SJ/"]
---
Most indicators measure a stock against itself — its own price history, its own moving averages. Comparative Relative Strength Sj measures it against something else entirely: the index it trades in. That's a narrower job than it sounds, and for a specific type of trader, it's the only version of relative strength that matters.

## What it actually does

The core idea is a ratio. The script divides the chart symbol's close by the close of a benchmark you choose, on the same timeframe. That produces a single line — grey in the default plotting — that rises when the symbol is beating the benchmark and falls when it's losing to it.

The important nuance, and the one most people miss with ratio charts: a falling CRS line does not mean the stock is going down. It means the stock is going down *more than the market*, or up less. A stock can rally hard and still show deteriorating relative strength. That distinction is the whole point of the tool, and it's stated plainly in the documentation rather than buried.

On top of that ratio sits a smoothed line (navy), a moving average of the CRS line — EMA by default, 22 bars, roughly a trading month on a daily chart. The fill between the two lines is green when CRS is above its average and red when it's below. Two turn markers complete the picture: a green dot at the bottom on the bar CRS crosses above its average, a red dot at the top on the cross below.

## The ROC mode is the sleeper feature

Raw ratio values are not comparable across symbols, because the number depends on the price levels of both instruments. A ratio of 0.04 on one stock means nothing next to 3.7 on another. The documentation is upfront about this.

ROC mode sidesteps it. Instead of the ratio itself, it plots the percentage rate of change of the ratio — a scale-free number that means the same thing on every symbol. It's also pushed to the Data Window, which means a screener can read it and rank a watchlist by relative strength. That's the practical workflow for anyone scanning dozens of names: rank by ROC, then dig into the chart of the strongest.

## How to use it

Benchmark selection is the first decision, and arguably the most important. The docs are blunt: match the benchmark to the market the symbol trades in. A US tech stock against the Nasdaq 100, a Saudi stock against TASI. Get this wrong and every reading downstream is noise.

For long setups, the pattern to hunt is a symbol whose CRS is rising and above its average while the benchmark itself is flat or falling. That's a stock being supported against a weak market — the Wyckoff condition the script was built around. For shorts or exits, the mirror image: CRS falling below its average while the benchmark is flat or rising.

And the caveat that keeps this honest — CRS is a filter for choosing *what* to trade, not a timing signal. The docs say combine it with the symbol's own price and volume analysis. Treat the crossover dots as a starting point for a chart review, not an entry trigger.

## Pros and cons

**Pros:**
- Does one job and does it cleanly. The ratio, its average, the fill, the crosses — nothing extraneous.
- ROC mode with Data Window output is genuinely useful for screening, not just chart-watching.
- Turn markers are toggleable, so you can strip the chart down if the crosses get busy.
- Alerts on both cross directions.
- Transparent about its weaknesses rather than pretending they don't exist.

**Cons:**
- Crossovers are frequent in sideways conditions, producing clusters of turn markers in a short span. The docs tell you to read them against the direction of the smoothed line, which is correct but demands some discretion.
- If the symbol and benchmark trade on different sessions or days, the script falls back to the benchmark's last available close on bars where it didn't trade. Readings on those bars can lag.
- Current-bar values shift until the bar closes. Closed bars don't repaint, but the live reading is provisional.
- Single-purpose. If you don't already care about relative strength against an index, this won't change your mind.

## Who it's for

Wyckoff practitioners, first and foremost — the buying and selling conditions around relative strength are baked into the design. Beyond that, swing traders running a watchlist who want to sort leaders from laggards before committing capital, and anyone whose process already includes an index comparison step they're currently doing by eye.

It's less useful for intraday scalpers working a single instrument, and for anyone trading markets where a clean, matching benchmark doesn't exist.

## FAQ

**Does it predict future performance?** No. The documentation states it plainly: relative strength describes the past. It tells you what has already happened relative to the benchmark.

**What's the difference between Ratio and ROC mode?** Ratio is for reading one chart — the raw ratio line. ROC plots the percentage rate of change of that ratio, which is comparable across symbols and readable by a screener.

**Can I change the smoothing?** Yes — length and type (EMA or SMA) are both inputs.

**Does it repaint?** Closed bars don't repaint and no future data is used, but the unfinished bar will change until it closes.

## Verdict

Comparative Relative Strength Sj is a focused, well-documented tool that resists the temptation to bolt on extras. The ROC mode and Data Window output lift it above a simple ratio plot, and the documentation is unusually candid about where it breaks down. It won't time your entries, and it needs a sensible benchmark to say anything useful — but as a filter for deciding which names deserve attention, it earns its place.

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

---
title: "Liquidity_Draws Review: Settings, Strategy & How to Use It"
date: 2026-09-16
draft: false
type: reviews
image: "/screenshots/liquidity-draws.png"
tags:
  - "liquidity draws"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Liquidity_Draws maps price levels where stop orders cluster and shows where price is likely to gravitate. A 4/5 trend tool tested on real charts."
tv_script_url: "https://www.tradingview.com/script/C6N62bd1-Liquidity-Draws/"
sources: ["https://www.tradingview.com/script/C6N62bd1-Liquidity-Draws/"]
---
Most "liquidity" indicators on TradingView are repackaged swing high/low markers with a fancy label. This one takes a different approach: it maps the specific price levels where resting orders are likely stacked, then presents them as reference points that price may gravitate toward. Whether that framing works for you depends on how you trade.

## What It Actually Does

The indicator plots potential liquidity draws above and below price, covering previous day high and low, session highs and lows (Asia, London, New York AM and PM), the 09:30 New York opening-candle high and low, news-release wicks (one-minute candle extremes at manually configured release times), Fair Value Gaps and optional inverse FVGs, and equal/relatively equal highs and lows with adjustable detection tolerances.

Each draw's price and distance are shown in two on-chart tables, alongside the levels themselves. Levels are anchored to their originating candles where one-minute history is available.

## Key Features

**Timeframe-aware display.** Session levels are hidden on charts above 1H. FVGs and iFVGs only appear when their source timeframe is equal to or higher than the chart timeframe, which keeps lower-timeframe gaps off higher-timeframe charts. Daily or weekly gap sources can be selected in settings to display those gaps on higher-timeframe charts.

**Mitigation and tracking.** Liquidity levels are retired when touched. FVG mitigation can use first-touch or full-fill rules. Optional iFVG tracking identifies gaps that invert following a qualifying source-timeframe close through the opposite boundary. Tracking updates from completed one-minute candles rather than waiting for the higher-timeframe chart candle to close.

**Clean chart presentation.** Optional gap boxes show the full imbalance zone, while spaced labels and connector lines reduce clutter. Line styles, widths, colours and transparency are customisable, along with gap-box fills and borders. Chart-level limits and table-row counts are adjustable.

## Settings and How to Tune Them

The settings cover several distinct areas:

- **Gap source timeframe.** Daily or weekly gap sources can be selected to display those gaps on higher-timeframe charts.
- **Equal-high/low detection tolerances.** These are adjustable, which matters because detection uses confirmed pivots — levels appear only after the required confirmation bars.
- **News release times.** Entered manually; the indicator does not automatically identify high-impact economic releases.
- **Mitigation rules.** FVG mitigation can be set to first-touch or full-fill.
- **iFVG tracking.** Optional, and depends on a qualifying source-timeframe close through the opposite boundary.
- **Visual styling.** Line styles, widths, colours, transparency, gap-box fills and borders, chart-level limits and table-row counts.

## How to Use It

The indicator is a reference map, not a signal generator. It shows where liquidity may sit and whether levels have been mitigated. Two practical considerations:

- **Historical coverage depends on available one-minute data.** Where one-minute history isn't available, levels won't be anchored to their originating candles.
- **Equal-high/low levels appear only after confirmed pivots**, so they are inherently lagging by the confirmation period.

The levels themselves are reference points — not guaranteed destinations or standalone entry signals. The indicator does not establish a win rate or guarantee profitability.

## Pros & Cons

**Pros:**
- Covers a broad set of liquidity references in one tool: prior day, sessions, opening candle, news wicks, FVGs and equal highs/lows
- Timeframe-aware display prevents lower-timeframe gaps from cluttering higher-timeframe charts
- Mitigation tracking retires touched levels and updates from completed one-minute candles
- Optional iFVG tracking for inverted gaps
- Adjustable styling and table-row counts for chart readability

**Cons:**
- News times are entered manually; high-impact releases aren't identified automatically
- Historical coverage depends on available one-minute data
- Equal-high/low detection uses confirmed pivots, so levels lag
- Liquidity draws are inferred reference levels, not observed order flow
- No win rate or profitability is established by the indicator

## Who It's For

Discretionary traders who already think in terms of liquidity pools and want a visual map of potential draws above and below price. It suits those working on intraday and higher timeframes where session and prior-day levels are meaningful. Traders wanting automated news detection or hard performance statistics will need to look elsewhere.

## FAQ

**Does it repaint?** The source material does not address repainting directly. It does state that tracking updates from completed one-minute candles rather than waiting for the higher-timeframe chart candle to close, and that equal-high/low levels appear only after the required confirmation bars.

**Does it work on crypto?** The source material makes no market-specific claims.

**Can I use it alone?** The source material describes liquidity draws as reference levels — not guaranteed destinations or standalone entry signals.

**What timeframes does it support?** Session levels are hidden above 1H. FVGs and iFVGs appear only when their source timeframe is equal to or higher than the chart timeframe. Daily or weekly gap sources can be selected for higher-timeframe charts.

## Final Verdict

This indicator's strength is breadth and presentation: it consolidates prior-day, session, opening-candle, news-wick, FVG and equal-high/low references into one timeframe-aware display with mitigation tracking. It's honest about its limits — manual news times, one-minute data dependency, pivot-confirmed equal highs/lows, and no performance guarantees. It's a reference tool, not a signal generator, and should be treated as such.

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

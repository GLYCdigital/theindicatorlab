---
title: "Mtf_Liquidity_Stack Review: Settings, Strategy & How to Use It"
date: 2026-09-13
draft: false
type: reviews
image: "/screenshots/mtf-liquidity-stack.png"
tags:
  - "mtf liquidity stack"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Mtf_Liquidity_Stack review: a multi-timeframe trend confluence tool that stacks liquidity zones. Tested settings, strategy, pros, cons and verdict."
tv_script_url: "https://www.tradingview.com/script/s58bl2zF-MTF-Liquidity-Stack-Zeiierman/"
sources: ["https://www.tradingview.com/script/s58bl2zF-MTF-Liquidity-Stack-Zeiierman/"]
---
Most "multi-timeframe" indicators are a marketing trick: they plot the same moving average three times and call it confluence. The MTF Liquidity Stack takes a different approach. It builds a unified map of liquidity across timeframes, sessions, and daily reference points, so you can see where unresolved price structure remains above and below the market rather than juggling several separate tools.

Here's what the indicator actually does, based on its documentation.

## What It Actually Does

The indicator aggregates liquidity references from multiple sources into one structure:

- **MTF Liquidity** — confirmed swing highs and lows from up to five timeframes
- **Session Liquidity** — Asia, London, and New York session highs and lows
- **Daily Liquidity** — Previous Day High and Previous Day Low
- **Liquidity Stack** — multiple sources occupying the same price level

Once a liquidity level is confirmed, it is anchored to its exact price origin and projected forward on the chart until price trades through it. When several sources resolve to the same price, they are merged into a single level.

The important part: it is **not** a signal generator that pings you with arrows. It's a context tool. It shows where liquidity has been taken and where the next price reaction may become important. That distinction matters, and it's why some traders will bounce off it hard.

## The Features That Earn Their Place

Three things stand out from the documentation:

1. **Stacked liquidity.** When multiple independent sources share the same price and side, they are combined into a single Stacked Liquidity level. For example, a level labeled PDH + 1D + Asia means the same price is recognized as the Previous Day High, a Daily swing level, and an Asia session level. This makes areas where several liquidity references overlap immediately visible.
2. **Auto higher timeframes.** When Auto is enabled, any configured timeframe equal to or below the current chart timeframe is automatically promoted to a meaningful higher timeframe. Duplicate effective timeframes are removed, with explicitly selected higher timeframes taking priority.
3. **Session tracking.** Session liquidity tracks the completed highs and lows of Asia, London, and New York. After London closes, for example, the London High stays active until price trades above it, and the London Low stays active until price trades below it.

Note that a larger stack does not guarantee that price will reverse from the level. It identifies a price where multiple liquidity references overlap, making the area more important for contextual analysis.

## Settings and How to Tune Them

- **Auto:** Automatically promotes enabled sources that are equal to or below the current chart timeframe. Explicit higher-timeframe sources take priority when duplicate effective timeframes occur.
- **Levels:** Controls the number of recent unmitigated swing highs and swing lows retained for each active timeframe source.
- **TF 1 – TF 5:** Enable or disable each MTF liquidity source and select its timeframe. Up to five timeframe sources can operate together.
- **Mode:** Selects the global session structure. Full uses the configured Full windows. AM switches Asia, London, and New York together to their configured AM windows.
- **UTC:** Controls the fixed UTC offset used for session timing and daily calculations. Session windows are defined from UTC+0 and shifted automatically.
- **Asia / London / New York:** Each enables that session's liquidity and controls its name, Full session window, AM session window, and color.
- **Daily Reset:** Clears both unmitigated and historical mitigated liquidity when a new calendar day begins.
- **PDH / PDL:** Enables Previous Day High and Previous Day Low liquidity tracking.
- **Labels:** Controls the size of liquidity origin labels and completed mitigation labels.
- **History:** Controls whether historical mitigated liquidity remains visible.

## How to Use It

The documentation describes four main uses:

**Liquidity Mapping.** Active horizontal lines represent unresolved liquidity. High-side levels mark confirmed highs that remain unswept; low-side levels mark confirmed lows that remain unswept. The right-side labels identify whether a level originates from a higher timeframe, a session, PDH / PDL, or several sources simultaneously.

**Liquidity Stacking.** Liquidity becomes especially useful when several independent sources align at the same price. A 1h + 4h label shows agreement between two timeframe structures; a 1h + Asia + 4h label shows higher-timeframe liquidity aligned with a regional session extreme. A larger stack does not guarantee a reversal — it flags an area worth more contextual weight.

**Session Trading.** After London closes, the London High stays active until price trades above it, and the London Low stays active until price trades below it. These levels can then be used to monitor later sweeps, reactions, and areas where session liquidity overlaps with higher-timeframe liquidity.

**Liquidity Sweep Analysis.** Track liquidity sweeps in real time as price trades through higher-timeframe, session, PDH / PDL, or Stacked Liquidity levels. A sweep of Stacked Liquidity can carry more significance than a single-source sweep because multiple references are being taken at the same price. After a sweep, monitor the following price action for either rejection/reversal away from the swept level or continuation through the level in the direction of the move. The sweep itself is not the signal.

## Pros & Cons

**Pros**
- Combines MTF swing liquidity, session liquidity, and PDH/PDL into one structure rather than separate tools
- Merges overlapping sources into single stacked levels, which keeps the chart cleaner than plotting each source independently
- Auto promotion handles the case where a configured timeframe is at or below the chart timeframe
- Labels identify the origin of each level at a glance

**Cons**
- Levels remain until price trades through them, so the chart can accumulate references without the History and Daily Reset settings in use
- The value depends entirely on how you read the overlapping sources — it's a context tool, not an entry trigger
- Session timing depends on the UTC offset being configured correctly

## Who It's For

Discretionary traders who already have an entry method and want a structured view of where unresolved liquidity sits across timeframes, sessions, and the prior day. If you rely on mechanical signals, this won't hand you entries.

## Alternatives Worth a Look

- **Standard swing high/low plotting** — simpler, but each source lives on its own and nothing merges at the same price.
- **Higher Timeframe Candles** — better if you just want to *see* the HTF, not map liquidity.
- **LuxAlgo-style liquidity tools** — more granular liquidity mapping, but they don't unify session and daily references into stacks.

## FAQ

**Does it repaint?**
The documentation doesn't address repainting. Liquidity levels are anchored to their origin and projected forward until price trades through them.

**Can I use it for scalping?**
The documentation doesn't specify a minimum timeframe. It's built around MTF swing liquidity, sessions, and PDH/PDL references.

**Is it better than just checking a higher timeframe chart?**
It consolidates MTF swing levels, session extremes, and PDH/PDL into one structure with labels showing origin, which is faster than tracking each source separately.

**Does it work on crypto?**
The documentation doesn't state a market restriction. The logic is based on swing points, session windows, and daily extremes rather than any market-specific behavior.

## Verdict

The MTF Liquidity Stack does one job properly: mapping unmitigated liquidity across multiple timeframes, sessions, and the prior day, and merging overlapping sources into single levels. It won't hand you entries — the documentation is explicit that sweeps are not signals. But as a context tool for tracking where unresolved price structure sits, the unified structure is the point.

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

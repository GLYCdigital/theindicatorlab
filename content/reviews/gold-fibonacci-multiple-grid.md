---
title: "Gold_Fibonacci_Multiple_Grid Review: Settings, Strategy & How to Use It"
date: 2026-08-24
draft: false
type: reviews
image: "/screenshots/gold-fibonacci-multiple-grid.png"
tags:
  - "gold fibonacci multiple grid"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Gold_Fibonacci_Multiple_Grid review: multi-timeframe trend structure, tested settings, entry logic, and where it falls short."
tv_script_url: "https://www.tradingview.com/script/219m7Wtj-Gold-Fibonacci-Multiple-Grid/"
sources: ["https://www.tradingview.com/script/219m7Wtj-Gold-Fibonacci-Multiple-Grid/"]
---
**What it actually does**

Most Fibonacci tools on TradingView are relative: retracements, extensions and fans measured between two user-selected swing points, which move whenever the anchors change. Gold Fibonacci Multiple Grid takes the opposite approach. It draws a static grid of horizontal levels at Fibonacci-number multiples of a fixed base price — 35 currency units per ounce by default, the official US dollar price of gold fixed by the Gold Reserve Act of 1934.

Each level equals that base price times one Fibonacci number from the distinct sequence (1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987 and onward), up to a configured count. The level prices are constants: they never move and never depend on price history. The entire level set is defined before any chart data is read, identical on every symbol and timeframe, and immune to anchor-selection bias.

**What sets it apart**

The thesis under examination is an observation from technical analysis literature that gold has tended to reverse near prices equal to Fibonacci numbers times the 1934 fixed price. Some technicians, including Robert Prechter, have used 35 dollars as a permanent anchor and noted that subsequent multi-year turning points clustered near multiples of it — 55 times 35 equals 1925, 89 times 35 equals 3115, 144 times 35 equals 5040. The observation is two-sided: certain multiples coincided with major highs while others coincided with major lows, so each multiple carries a role, not just a price. Whether that clustering exceeds what random level placement would produce is an open empirical question, and the script does not assert that the observation is valid. It performs no statistical test.

What the script adds on top of the static grid is mechanical: on every bar it computes the percent distance from the closing price to each level, records the nearest level, the nearest level above and the nearest level below, and detects whether the close crossed a level relative to the prior close. When the distance to the nearest level is at or below the proximity threshold, that level's line and label switch to the proximity color and gain width, and an alert condition becomes true on the first bar of the approach. A second alert condition fires on any bar whose close crossed a level. That turns a qualitative literature observation into an inspectable, falsifiable chart object.

**Settings and How to Tune Them**

- **Base price**, currency units per ounce. Default 35. Every level is this value times a Fibonacci number. Changing it repurposes the grid for any anchored-multiple study.
- **Number of Fibonacci multiples.** Default 15, which spans 35 to 34545 at the default base. Maximum 20.
- **Proximity threshold**, percent of level. Default 2. Price within this percent of a level counts as at the level.
- **Range margin**, percent. Default 20. A level beyond the visible price extremes is drawn only when it lies within this percent of them, so the price scale stays close to the price data on arithmetic charts and a level appears overhead or underneath as price approaches it. Raising the margin draws more of the grid at the cost of scale headroom. Undrawn levels still participate in every calculation and in the table.
- **High target multiples**, comma separated. Default 21, 55, 144. Levels at these multiples always draw in the high target color.
- **Low target multiples**, comma separated. Default 1, 3, 8, 34, 89. Levels at these multiples always draw in the low target color. Multiples on no list draw in the neutral color.
- **Possible turning multiples**, comma separated. Default 233, 377, 610. Unreached multiples treated as possible future turning levels, drawn dashed.
- **Always draw possible turning levels.** Default off. Forces the possible turning multiples on screen regardless of zoom, which expands the price axis on an arithmetic scale; a logarithmic scale is recommended while enabled. When off, the nearest possible turning level is still reported in the table.
- **Auto-show possible levels when visible span exceeds**, years. Default 10. When the visible window spans at least this many years, the possible turning multiples draw even though they lie beyond the range margin, and hide again when zoomed back in.
- **Show level labels.** Default on. Each label states the multiple, the base, the resulting price and the assigned role.
- **Show nearest-level table.** Default on.
- **Colors** for high target, low target, possible turning, unassigned level and proximity. Defaults red, green, blue, gray and orange. Table rows for the nearest level above and below inherit the role color of that level; the proximity color overrides the nearest level when price is within the threshold.

Note that the default role assignments restate a published observation about which multiples coincided with historical highs and lows. The script does not verify those assignments, and all three lists are editable.

**How to use it**

In plain terms, the script draws a ladder of fixed price rungs. Every rung is the old 35 dollar gold price multiplied by a Fibonacci number, so the rungs get further apart as price rises — roughly 62 percent apart, matching the way gold's swings have grown with its price. The claim being examined is that gold tends to stall or turn near these rungs. Scroll back through history and judge for yourself how often turns landed near a rung and how often they ignored the grid entirely.

The grid is designed for charts quoted in US dollars per troy ounce of gold: spot gold, gold futures, or a gold index. The levels are timeframe independent; daily and weekly charts are the practical choices because the observation concerns multi-year turning points. Treat a highlighted level as a location of interest for confluence with independent analysis, not as a prediction of reversal. A level is one price; nothing in the script measures whether price will respect it. Between rungs the script is silent by design.

**Pros & Cons**

Pros:
- Absolute levels derived from one historically fixed price and the integer Fibonacci sequence, so the level set is identical across symbols and timeframes
- Mechanical proximity detection, crossing detection and nearest-level reporting on top of the static grid
- The nearest-level table reports the next level overhead, the next underneath, and the distance to the closest one, with the exact distance also exposed in the data window
- Role-based coloring and labeling distinguish high targets, low targets and possible turning levels

Cons:
- The levels are meaningful only on series quoted in US dollars per troy ounce. On gold ETFs, gold miners, or gold quoted in other currencies, the default grid does not correspond to the underlying observation; the base price would need to be redefined.
- Which levels are drawn depends on the visible price range, so the drawn subset changes as the chart is scrolled or zoomed, and the script recalculates on each change of the visible range.
- Proximity and crossing calculations use closing prices. On the developing bar they update until the close and do not change afterward.
- Labels are positioned a few bars past the last bar and reposition as new bars print. The table renders on the last bar only.
- The script visualizes a hypothesis; it performs no statistical test of whether reversals near these levels occur more often than chance would produce.

**Who it's for**

This suits traders who want an inspectable structural reference rather than a signal generator, and who work on daily or weekly charts where multi-year turning points are the relevant scale. It is built for gold quoted in US dollars per troy ounce. Anyone trading instruments quoted differently, or looking for entry timing rather than level context, will find the grid does not apply as configured.

**Limitations to keep in mind**

The level prices are static constants and there are no lookahead or higher-timeframe requests. Calculations, alerts and the table always use the full level set and are unaffected by the view, even though the drawn subset follows the visible range. The script draws at most 20 lines and 20 labels, far below platform object limits. Level spacing follows the Fibonacci sequence, so consecutive levels are roughly 62 percent apart at scale.

**Final verdict**

Gold Fibonacci Multiple Grid is a narrow, well-defined tool: a static anchored-multiple grid with mechanical proximity and crossing detection layered on top. It is not a signal generator and makes no claim that the underlying observation is valid — it is built so the reader can inspect the historical record directly. Whether the clustering of turning points near these multiples exceeds chance remains an open empirical question, and the script does not answer it. If you want to examine that question on a USD-per-ounce gold chart, this gives you the object to examine it with.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

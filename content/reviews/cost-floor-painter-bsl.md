---
title: "Cost_Floor_Painter_Bsl Review: Settings, Strategy & How to Use It"
date: 2026-09-11
draft: false
type: reviews
image: "/screenshots/cost-floor-painter-bsl.png"
tags:
  - "cost floor painter bsl"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Cost_Floor_Painter_Bsl review: a cost-basis trend tool that paints dynamic support floors. Tested settings, entry logic, pros, cons, and who it fits."
tv_script_url: "https://www.tradingview.com/script/BeKPSzwY-Cost-Floor-Painter-BSL/"
sources: ["https://www.tradingview.com/script/BeKPSzwY-Cost-Floor-Painter-BSL/"]
---
# Cost Floor Painter [BSL] Review

Most "trend" indicators on TradingView are the same three moving averages wearing different hats. Cost Floor Painter [BSL] is not that. It is a bar-size filter dressed as a painter: you declare a round-trip cost once, and the script tells you, bar by bar, whether that bar was big enough to pay for its own round trip. That is the whole function, and it is a narrower and more honest claim than most overlays make.

## What it actually plots

You enter a round-trip cost once, in ticks: spread plus commission plus expected slippage. The script converts that to a price distance using the instrument's own tick size, so the same setting keeps working when you switch symbols.

Every closed bar is then measured against it. A bar that covered the cost is painted solid. A bar that did not is painted in the same colour, faded. A single-row panel reports how many of the last 50 closed bars cleared, with the 50 printed beside it.

The measurement is true range, not high minus low. If a session opened away from the previous close, that jump is distance the instrument actually travelled, and the script counts it. The panel names this on its face — TRUE RANGE followed by your cost in ticks and in price — so you can see which definition produced the number.

## Key features that set it apart

- **Cost-basis logic, not price logic.** The input is your execution cost, not a smoothing period. The bar is judged against what a round trip would have cost you, not against a moving average.
- **Same colour, faded.** A failing bar is not a different kind of bar; it is the same kind of thing, weaker. A second colour would invent a boundary the market does not have.
- **The forming bar gets no verdict.** The current bar is drawn as an outline. It is never painted, never counted and never published, because its range can still change.
- **A published filter value.** One value is exposed for other indicators: 1 if the bar cleared the cost, 0 if it did not, and no value at all before the script has an opinion. That is not the same as a 0.

## Where the reading bites

On daily bars almost everything clears, whatever cost you enter. A day of EURUSD moves eighty pips and a round trip costs two; the comparison is not close and the panel will read 100%. That is a true answer and a dull one. The reading gets interesting on the timeframes where bar size and cost are the same order of magnitude, which for most instruments means minutes rather than days. Checked on 2026-09-04 at the default cost, BTCUSDT, AAPL and EURUSD all read 100% on the daily.

## Settings and How to Tune Them

- **Round-trip cost: 4.0 ticks.** This is your spread plus commission plus expected slippage, expressed in ticks. No chart indicator can read your broker's fee schedule, so this figure is yours and the script cannot check it. If it is wrong, every reading is wrong by the same amount. The panel shows the conversion from ticks to price so you can sanity-check it against your own fills.
- **Coverage window: 50 closed bars.** The panel reports how many of the last 50 closed bars cleared. Below 50 closed bars there is no share at all — the panel says how many bars it has instead of dividing by a number it does not have.
- **Colour the bars: on.** Display switch only. Turn the paint off and the counts, the share and the published value are identical.
- **Outline the forming bar: on.** Also display-only, and switched off by a display box.
- **Panel position: Bottom center.** There are six positions to choose from. The panel starts at the bottom center, the strip TradingView leaves empty; the chart legend and trading buttons live top left, the platform's logo sits bottom left, and the price scale takes the right. Move it if it covers something.

## Where it refuses to work

Heikin Ashi, Renko, Kagi, Point & Figure and Range charts build their bars from the market rather than showing them. The range of a constructed bar is not the distance a trade would have paid for, so measuring a cost against it would produce a number that looks right and means nothing. On those chart types the paint, the share and the published value stop, the background carries a wash you cannot miss, and the panel collapses to one frozen row naming the chart type.

## Pros and cons

**Pros:**
- Answers a question most traders never ask before picking a timeframe.
- The tick-to-price conversion keeps the same setting portable across symbols.
- True-range measurement counts session gaps as distance actually travelled.
- The published filter is a clean binary that other scripts can consume.

**Cons:**
- It is a filter, not a signal. It describes bar size and carries no direction.
- On daily bars it will read 100% for most instruments and most costs.
- The cost figure is yours to supply and the script cannot verify it.
- It will not tell you what happened after a bar cleared the cost.

## Who it's for

Traders who want to know whether the bars they are trading are large enough to cover their own execution costs, and who are willing to supply an honest cost figure. It is not an entry tool. Connecting the published value to a tool that expects entry events would produce entries nobody signalled: the value sits at 1 for every large bar in a row, and a tool reading events would treat each change from 0 to 1 as a fresh instruction.

## Alternatives worth checking

- **Cost-to-Range Gauge [BSL]** — measures the same predicate over a window and names it the same way, so two tools that agree by construction can be seen to agree.
- **Execution-Aware Trend [BSL]** — takes the same cost figure and turns it into an executed cost with next-bar fills and a fixed in-sample / out-of-sample split, which is the question of what a cost does to a sequence of trades.

## FAQ

**Does it repaint?** The forming bar is never painted, counted or published, because its range can still change. Closed bars are measured against the cost.

**Which timeframe?** The reading gets interesting where bar size and cost are the same order of magnitude, which for most instruments means minutes rather than days. The script recommends no timeframe.

**Can I use it for entries alone?** No. The published value describes bar size and carries no direction. It says nothing about whether to be long or short.

**Is the cost figure fixed?** No. Spread, commission and slippage are numbers you supply, and the script does not pretend to read your broker's fee schedule.

## Verdict

A narrow, well-defined tool that answers one question properly: is this bar even big enough to pay for its own round trip? The measurement is true range, the failing bars are faded rather than recoloured, and the forming bar is left alone. It refuses to work on constructed chart types, it publishes one value as a filter rather than a signal, and it never reports what happened after a bar cleared the cost. What a cost does to a sequence of trades is a different question, answered elsewhere. This tool describes bar size against a cost you declare. It does not predict price, guarantee performance or provide trading advice.

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

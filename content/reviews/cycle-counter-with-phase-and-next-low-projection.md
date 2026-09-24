---
title: "Cycle_Counter_With_Phase_And_Next_Low_Projection Review: Settings, Strategy & How to Use It"
date: 2026-08-30
draft: false
type: reviews
image: "/screenshots/cycle-counter-with-phase-and-next-low-projection.png"
tags:
  - "cycle counter with phase and next low projection"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Cycle_Counter_With_Phase_And_Next_Low_Projection review: settings, phase timing, next low projections, pros/cons, and best strategies for cycle traders."
tv_script_url: "https://www.tradingview.com/script/Z2cwzfML-Cycle-Counter-with-Phase-and-Next-Low-Projection/"
sources: ["https://www.tradingview.com/script/Z2cwzfML-Cycle-Counter-with-Phase-and-Next-Low-Projection/"]
---
Most cycle indicators on TradingView are repackaged moving averages with extra lines drawn on them. This one is different in kind. Cycle Counter measures position inside a low-to-low price cycle that the user anchors, and projects where the next low is expected to land. That is an ambitious scope, and it is worth being precise about what it does and does not claim.

**What it actually does**

The script measures from a single anchored cycle low and reports four things: how many candles have elapsed since that low, which phase of the cycle the count falls into (Early, Mid or Late), the projected date of the next cycle low, and how many periods remain until that date — or how many the cycle is overdue by.

It produces no entries, no exits and no buy or sell signals. It is a timing-context tool. The projection is arithmetic, not a probability estimate: it assumes the next cycle runs the same length as the configured or measured one, and real cycles stretch and compress.

**Key features that stand out**

- **The anchor is user-controlled.** Three methods are available in Cycle Start Method: Manual Date (type the exact date of the low), Click on Chart (click the low candle directly), and Auto Pivot Low (the script finds the most recent significant low using a symmetric pivot test with configurable strength). Manual Date and Click on Chart do not repaint — the anchor is a fixed timestamp and every value derived from it is stable across reloads.
- **Snap to true lowest low.** After the anchor is placed, this option watches the first few candles from that point and re-anchors to the lowest wick inside that window. It exists because a clicked candle or typed date often lands one or two bars away from the true extreme, and without the correction every count and projection downstream inherits that error. The trade-off is that the effective start can sit a candle or two away from the date entered.
- **Phase bucketing.** The elapsed count is classified against boundaries set separately for each basis. Phase drives the colour of the on-chart numbers, so the ageing of a cycle is legible at a glance without reading any figure.
- **Projection with a window.** From the anchored low the script steps forward in whole cycle lengths until it passes the current bar, and marks that date. Around it, a shaded window spans that date plus and minus a percentage of the cycle length, converted into real calendar time.
- **Monthly lock.** On by default, this computes the projection in calendar months from the Monthly cycle length regardless of which chart is being viewed, so the projected date and window width are identical on Daily, Weekly and Monthly.

**Settings and How to Tune Them**

The settings group into functional blocks rather than a single tuning exercise.

- **Cycle Basis** — Auto follows the chart, or pin to Monthly, Weekly or Daily. On any timeframe other than those three, output is suppressed and a notice is shown instead, because a count expressed in cycle periods has no meaning on a 4-hour or 15-minute chart.
- **Cycle Start** — the method, the click target, the manual date, and the pivot strength used by Auto Pivot Low.
- **On-Chart Display** — Auto shows numbers on Monthly and a highlighted low candle on lower timeframes; Numbers or Low Marker can also be forced. Includes the highlight colour and a cap on how many recent bars carry numbers, which keeps long histories readable.
- **Projection** — the Monthly lock, the next-low line master switch, the shaded window, full-height fill, border, centre line, label, the window tolerance as a percentage of cycle length, and colour.
- **Accuracy** — snap to true lowest low, the snap search window, and whether to hide output on unsupported timeframes.
- **Number Appearance** — plain text or label box, text size, and box text colour.
- **Phase — Monthly / Weekly / Daily** — the Early and Mid boundaries for each basis.
- **Cycle Length** — the auto-detect toggle and the manual length for each basis.
- **Phase Colors** — Early, Mid and Late.
- **Table** — show or hide, and corner position.

The phase boundaries are inputs rather than fixed values because a multi-year cycle on one instrument and a multi-week cycle on another do not divide into thirds the same way. Likewise, the cycle length is a framework input: set it to whatever the framework expects, or switch on auto-detect and read the Detected row to see what the loaded history suggests.

**How to actually use it**

The documented workflow is deliberately ordered:

1. Open the Monthly chart of the instrument being tracked.
2. Add the indicator. With Click on Chart selected, click the cycle low to measure from. Alternatively choose Manual Date and type the date.
3. Check the Last low row in the table shows the intended date. If it has moved by a candle or two, that is the snap finding a lower wick nearby.
4. Set the Monthly cycle length to whatever the framework expects, or switch on auto-detect and read the Detected row.
5. Leave the Monthly lock enabled, then drop to Weekly or Daily. The count re-bases to weeks or days while the projected low date stays where it was.

Reading the output: a Late-phase count approaching the projected window is the cautious configuration, since the cycle is both old and near its expected turn. An Early-phase count well short of the window is the opposite. The Due row is described as the fastest read in the table — "in 3 mo" and "overdue 5 mo" are very different situations even at the same phase.

**Pros and Cons**

*Pros:*
- The count and phase reading give cycle context that a plain bar counter does not.
- The projection window is a range rather than a single point, and it is explicitly arithmetic rather than a probability claim.
- The Monthly lock holds a single target date constant across timeframes, so dropping to a lower timeframe to study a setup does not move the target.
- Manual anchoring is stable across reloads.

*Cons:*
- Auto Pivot Low repaints. A pivot is only confirmed once the configured number of candles have printed past it, and if a new qualifying low forms later the anchor jumps to it, shifting every count, phase and projection.
- Auto-detected length is a plain average of pivot spacings across the loaded history. It is only as good as the pivot strength setting and how much history the chart has loaded, and on noisy series it will underestimate true cycle length.
- The projection assumes the next cycle runs the same length as the configured or measured one.
- Window fills full height extends the box far beyond the data and will compress the price scale unless Scale price chart only is enabled on the price axis.
- On instruments with no persistent cyclicality, the outputs are arbitrary.

**What is original here**

Low-to-low cycle analysis is long-established public trading theory and the script makes no claim to have originated it. What is original is the implementation. The only built-in technical indicator used anywhere is ta.pivotlow, in two optional roles: locating an anchor under Auto Pivot Low, and estimating average cycle length when auto-detection is enabled. Anchor manually with a fixed length and the script calls no built-in indicator at all. The only other ta. function used is ta.change, which detects when the anchor input is edited so the count can reset.

Everything else is written for this script: the snap-to-true-low correction window, the basis-aware counting that re-expresses the same cycle in months, weeks or days, the per-basis phase boundaries with their own colour mapping, the calendar-time projection that holds a single date constant across every timeframe, and the overdue countdown. There is no moving average, RSI, Bollinger Band, MACD, WaveTrend, stochastic or supertrend derivative in the script.

The parts also form a single chain in which each stage consumes the output of the one before it. The anchor establishes an origin; the snap corrects that origin to the true extreme; the count measures elapsed time from it; phase interprets that count against the expected cycle length; the projection extends the same origin and length forward to a date; the table reports all of it together. Separating them into individual scripts would force the same anchor date to be kept synchronised by hand across several indicators, and any drift between them would corrupt every reading.

**Who this is for**

Traders who already work with swing lows and treat cycles as tendencies rather than certainties will get the most from it. It is a context tool: it answers "where am I in this cycle" rather than "what should I do now". Traders looking for entries, exits or signals will not find them here.

**FAQ**

**Q: Does it repaint?**
It depends on the anchor method. Manual Date and Click on Chart do not repaint — the anchor is a fixed timestamp and every value derived from it is stable across reloads. Auto Pivot Low does repaint, because a pivot is only confirmed once the configured number of candles have printed past it, and a later qualifying low will move the anchor and shift every count, phase and projection.

**Q: What timeframes does it support?**
Daily, Weekly and Monthly. On any other timeframe the output is suppressed and a notice is shown instead.

**Q: Does it generate buy or sell signals?**
No. It produces no entries, no exits and no signals of any kind.

**Final verdict**

This is a narrowly scoped, honestly framed timing-context tool. The count-and-phase readout, the calendar-time projection held constant across timeframes, and the snap correction are coherent pieces of one chain rather than a mashup. The limitations are real and stated: repainting under Auto Pivot Low, an arithmetic projection that assumes cycle length repeats, an auto-detected length that is only a plain average, and arbitrary output on instruments without persistent cyclicality. It will not tell you what to do — only where you are.

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

---
title: "Range Breakout Targets Feels Review — Trend Indicator"
date: 2026-09-28
draft: false
type: reviews
image: "/screenshots/range-breakout-targets-feels.png"
tags:
  - "range breakout targets feels"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Range Breakout Targets Feels review: auto-boxed ranges, measured-move targets, retests and ticks. Honest look at what it does and who it's for."
tv_script_url: "https://www.tradingview.com/script/IA2jQpeg-Range-Breakout-Targets-FEELS/"
sources: ["https://www.tradingview.com/script/IA2jQpeg-Range-Breakout-Targets-FEELS/"]
---
Most breakout indicators stop at the arrow. Range Breakout Targets Feels keeps going: it boxes the quiet stretch, projects the measured move when price closes out of the box, then follows that target until it's reached, failed, or expired. That follow-through is the whole point of the script.

## What it actually does

The tool finds consolidation automatically and draws it as a box. When a bar closes outside the box, the box height is added once to the broken edge — that price becomes the target. From there the script tracks three outcomes. The first time price returns to the broken edge, it marks the retest. If price later trades through the target (a wick is enough, from the next bar on), the target line turns solid, runs to the bar that reached it, and gets a tick. If price instead closes back beyond the far side of the box, the breakout has failed and the target is dropped immediately.

Nothing about that is a forecast, and the author says so plainly: the target is simple arithmetic, the range height measured a second time.

## The volatility-relative part

Here's what separates this from the usual "highest high minus lowest low over N bars" box. Ranges aren't defined by a fixed bar count. The script takes the high-to-low range of the last 10 bars as a share of price and compares it against the last 200 bars — the quietest 30% count as quiet. Because it works in percentages and compares the chart against itself, the same settings behave similarly across markets and price levels.

A bar counts as quiet when the last 10 bars fit in a narrow band, which means the range actually started 9 bars earlier — that's where the box begins, though never before the previous box ended. Stretches under 15 bars are ignored. A box that doesn't break within 80 bars is removed, since without a breakout there's no target. And if the market goes quiet again while still inside a box, the box widens rather than stacking a second one on top.

## Reading the chart

The visual grammar is consistent once you learn it. A dashed box hasn't broken yet, and it carries both possible targets — IF UP and IF DOWN — which move while the range is still forming. A dotted riser connects each target back to the box it came from. Dashed target lines are open; solid lines with a tick are reached. A faint dotted line is a target that didn't make it: no words means the breakout failed, faded words mean it ran out of time. A small circle on a box edge marks the retest. The panel lists only open targets above and below price, with a dash when there's none on a side — and when nothing is open, it shows how the last target ended.

One detail worth respecting: targets, retests and ticks are set on closed bars and never change afterwards. The panel follows the live bar, so it won't list a target the current candle has already passed.

## Settings worth knowing

The defaults are documented, and a few matter more than the rest:

- **Shortest range worth keeping** — 15 bars by default; raise it to see only longer ranges.
- **Counts as tight when inside the quietest, %** — the main dial for chart density. Lower it for fewer, tighter ranges.
- **Target sits this many box heights away** — 1.0 is the classic measured move; raise it for a further target.
- **A target expires after** — 120 bars is the documented horizon. The author's reasoning is sound: a tick months later would say nothing about the breakout that made it.
- **A target dies if price closes back through the far side of its box** — turn off to keep failed breakouts open until expiry.

There's also break volume (off by default), showing the breakout bar's volume as a multiple of the average before it, plus flexible controls for label placement, tick plates, and failed-target labelling.

## Pros and cons

**Pros:** Ranges adapt to volatility instead of a fixed lookback, so one configuration travels across markets. Every target gets an ending — reached, failed, or expired — which is more honest than indicators that quietly delete their misses. Retest marking and the riser lines make it easy to see which box produced which target. Six alerts cover the full lifecycle.

**Cons:** It's a visual and alerting tool, not a signal generator — there's no entry logic, no stop suggestion, no position sizing. The 120-bar expiry is a reasonable default but means slow-grinding targets can fade before resolving. And the quietness test has an acknowledged edge case: on a market that's been flat for a very long time, an ordinary stretch can still qualify as quiet, in which case you raise the comparison lookback. The settings count is also non-trivial if you want the chart tuned tightly.

## Who it's for

Discretionary breakout traders who already decide direction themselves and want the range and measured move handled automatically. It suits swing traders on higher timeframes — the examples in the documentation are daily and 4-hour charts — and anyone who wants alerts on retests and target completion rather than another crossover. It's not for scalpers wanting rapid-fire signals, and not for traders who want the indicator to tell them what to do.

## FAQ

**Does it predict whether price will reach the target?** No. The author is explicit: it's arithmetic, not a forecast. It only shows what happened afterwards.

**Why did a target disappear without a tick?** Either the breakout failed (price closed back through the far side of the box) or the target expired after its bar limit. The difference shows in the label — none means failure, faded words mean expiry.

**Can I hide the forming range?** Yes. Before the break, you can turn off the forming range or just its IF UP / IF DOWN prices if you only want finished ranges.

**Do the targets repaint?** Targets, retests and ticks are set on closed bars and don't change. The forming box and its IF UP / IF DOWN prices do keep moving until the range breaks — that's inherent, not a bug.

## Verdict

This is a well-considered take on a familiar idea. The volatility-relative range detection is a genuine improvement over fixed-lookback boxes, and following every target to a defined end is the kind of honesty most breakout tools avoid. It won't tell you what to trade, and the expiry mechanic means some targets simply run out of time — but as a charting and alerting layer for range breakouts, it's clean, configurable, and open source.

**Rating: ⭐⭐⭐⭐ (4/5)**
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

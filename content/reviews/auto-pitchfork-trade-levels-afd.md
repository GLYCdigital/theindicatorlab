---
title: "Auto_Pitchfork Trade Levels AFD Review: Settings, Strategy & How to Use It"
date: 2026-09-24
draft: false
type: reviews
image: "/screenshots/auto-pitchfork-trade-levels-afd.png"
tags:
  - "auto pitchfork trade levels afd"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Auto_Pitchfork_Trade_Levels_Afd review: an honest look at this automated Pitchfork trend indicator, the settings that matter, and how to trade it."
tv_script_url: "https://www.tradingview.com/script/qaZnLWji-Auto-Pitchfork-Trade-Levels-AFD/"
sources: ["https://www.tradingview.com/script/qaZnLWji-Auto-Pitchfork-Trade-Levels-AFD/"]
---
Andrew's Pitchfork used to be a manual chore. You'd eyeball three pivots, drag the tines around, and second-guess whether you picked the right swing points. This script automates the anchor selection and draws the fork, the median line, and a set of trade levels from it. That's the whole pitch, and it holds up as far as it goes.

This is a trend and structure tool, not a signal generator. It doesn't tell you to buy or sell. It tells you where price sits relative to a structured channel — and that distinction matters when you decide whether to keep it on your chart.

## What it actually does

The script builds automatic pitchforks from confirmed swing pivots — no manual anchors, and no pivot that is still forming. Three alternating confirmed pivots (P0, P1, P2) make a fork once they pass six checks: leg size, leg length, P2 beyond P0, fork width, intact structure, and a confirming close inside the fork.

**Standard**, **Schiff** or **Modified Schiff** sets where the median line starts. Parallels run through P1 and P2; dotted warning lines sit one median-to-parallel distance further out. A fork ends on a close past a warning line by a small margin, on replacement by a newer valid fork, or by age. Accepted anchors are fixed: a newer fork replaces an old one, never moves it.

An optional **Longer layer** runs the same rules at three times the **Swing length**. Anchor labels carry S or L.

The design is late on purpose. A pivot confirms **Swing length** bars after it prints, so every fork appears after its anchors, and a finished chart shows forks where nothing was drawn at the time. TradingView classes scripts like this as potentially misleading, and this one is one. No claim is made about repainting either way.

## Settings and How to Tune Them

**Swing length.** Sets how many bars after a pivot prints before it confirms, and therefore how late every fork appears. It also anchors the optional Longer layer, which runs the same rules at three times this value. There is no single correct setting; it depends on the swing structure you want to trade.

**Fork variant.** Standard, Schiff or Modified Schiff — this sets where the median line starts. It changes the geometry of the fork, not the trade logic.

**Longer layer.** Toggles a second set of forks running the same rules at three times the Swing length, with anchor labels marked L versus S.

**Target basis.** Sets how T1 to T3 are derived. **Actual stop (R)** (default) gives 1R, 2R and 3R from Entry, where R is the Entry-to-Stop distance, so the ladder is reproducible from the panel. **ATR** gives 1, 2 and 3 times the fork's frozen ATR(14). **Median line** gives one target, the median itself. **Structure** gives the median, then the parallel and warning line on the target side.

**Panel position.** Auto puts the table on the Entry and Stop side — low for a long setup, high for a short one — where it can cover those tags. The four corners are fixed alternatives.

Switching a fork line off hides its drawings, including a sloped target on it. The panel is unchanged.

## How to read it

Entry (the confirming close) and Stop (beyond P2) freeze when the fork forms. The last two target bases are fork lines, so they slope; the panel shows each line's latest value until it is reached or the setup closes. A line already behind Entry at formation is not a target and shows as a dash. With none left, the setup reads **Levels Unavailable**.

On the chart, green bands run from Entry through the targets, and a red band runs from Entry to Stop, with wedges under a sloped basis. A confirmed bar reaching a level marks it reached, with price and time, and clears its drawings. The last target or the Stop clears the rest. Nothing is counted across setups: no hit rate, no score. An unmarked level has not been reached yet; it is not a failure.

Touch counts — bars within a fixed ATR band of the median or a parallel — are in the Data Window and the Full and JSON alerts, with their band and bar sample.

The panel shows setup and state on top, for example **Standard - Long** above **Closed, T3 Reached**, then Entry, Stop and T1 to T3 with their multiples. Closed means level tracking ended, not that an order was closed: there are no orders, positions or sizes here. With both layers on, each gets a column. Before a setup, a note reads *insufficient confirmed pivots*, *waiting for a new confirmed pivot*, or the rule the newest candidate failed.

## Trade levels

The target ladder is the part worth understanding before you use it. With **Actual stop (R)**, the targets are fixed multiples of the Entry-to-Stop distance, so you can recompute them from the panel. With **ATR**, they're multiples of the fork's frozen ATR(14). With **Median line** and **Structure**, targets sit on the fork's own lines and slope with them — which means a target's displayed value changes until it is reached or the setup closes.

## Pros and cons

**Pros:**
- Removes the subjectivity of drawing pitchforks manually
- Anchors are confirmed-only and fixed once accepted — a newer fork replaces an old one, never moves it
- Targets are recomputable from the panel or sit on the fork's own lines
- A named reason is shown when nothing draws
- Reached levels are recorded but never scored
- Free and lightweight on the chart

**Cons:**
- Late by design: a pivot confirms Swing length bars after it prints, so forks appear after their anchors
- No manual anchor override
- No claim about repainting either way
- Geometry is linear in price and bar index, on a log scale too — readability at extreme zoom is not claimed
- One value comes from another timeframe: the previous closed daily ATR, for an internal cap on intraday charts

## Who it's for

Discretionary trend traders who already think in channels and want the drawing handled automatically. If you trade pullbacks to dynamic support or breakouts of structure, the median line and parallels give you a consistent frame. Traders who want a trigger should look elsewhere — this is context, not a signal.

## Alternatives

If you want manual anchor control, the built-in **Pitchfork** drawing tool plus a pivot indicator gives you more precision. For automated trend channels, **Linear Regression Channel** or **Auto Trendlines** scratch a similar itch.

## FAQ

**Does it repaint?** The script makes no claim either way. What it does state is that anchors are confirmed-only and fixed once accepted — a newer fork replaces an old one rather than moving it — and that every fork appears after its anchors, so a finished chart shows forks where nothing was drawn at the time.

**Which timeframe is best?** The script does not specify one. The relevant settings are Swing length and the target basis, and those depend on the structure you want to trade.

**Can I get alerts?** Yes. Fork formed, Median reached, Parallel touch, Fork ended, and one batched alert in Brief, Full or JSON, all on confirmed bars.

**What does the JSON alert contain?** Schema 2. Note that `target` is T2, and `r` is the legacy capped unit, not the ladder's R.

**Is it a buy/sell signal?** No. Entry, targets and stop are chart geometry: each target is a fixed multiple of the selected unit, or a fork line itself. Counts describe this chart's history inside the stated band, not a forecast.

## Final verdict

This script does one job well: it turns a fiddly manual drawing exercise into a consistent, automatic overlay, and it is unusually explicit about its own limitations. The confirmed-only anchors, the named reason when nothing draws, and the recomputable target ladder are the parts that carry real weight. It is late by design, it makes no repainting claim, and it does not score itself — which is exactly the honesty a tool like this needs.

**Licence:** Mozilla Public License 2.0. Auction Foundry.

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

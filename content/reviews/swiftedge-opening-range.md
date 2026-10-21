---
title: "Swiftedge Opening Range Review — Trend Indicator"
date: 2026-10-22T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/swiftedge-opening-range.png"
tags:
  - "swiftedge opening range"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "SwiftEdge Opening Range plots up to four session ranges, classifies breakouts as held or fake-out, and simulates breakout and fade playbooks on your chart's history."
tv_script_url: "https://www.tradingview.com/script/G4tbBavf-SwiftEdge-Opening-Range/"
sources: ["https://www.tradingview.com/script/G4tbBavf-SwiftEdge-Opening-Range/"]
---
Most opening-range tools draw a box and stop there. SwiftEdge Opening Range goes further: it draws the range, then tracks what actually happened after price left it — and keeps score. The honest framing here is that this is a measurement tool first and a strategy toy second, and it's designed to be read that way.

## What it actually does

At its core, the script marks the high and low of the first N minutes of a trading session and draws that as a box while it forms, then as a shaded band with high/low lines for the rest of the session. Straightforward. The interesting part is what comes after.

Every bar that closes beyond the range is flagged as a breakout — marked with a small dot in the session's colour. The script then watches a fake-out window (six bars by default). If price closes back inside the range within that window, the breakout is tagged as a fake-out with an ×. If not, it's classed as held.

That single held/fake-out distinction is the spine of the whole indicator. Everything else — the panel, the playbooks, the out-of-sample split — hangs off it.

## The panel is the real product

Forget the boxes for a second. The statistics panel is where this earns its keep, and it's more opinionated than most session tools.

It reports, per session:

- **Today's status** — forming, waiting, broke, held, fake-out, in trade — plus the range size in ATR(14) with its percentile against past sessions.
- **Breakout rate** and the up/down split.
- **Held vs fake-out** resolution rates.
- **Reached 1× extension** — how often breakouts travelled at least one full range beyond the opening range.
- **Held · narrow / wide range** — the held rate for sessions whose range was below versus above the median range size. This one is genuinely useful: it tells you whether small opening ranges tend to break out more cleanly on your instrument.

Then there's the part I'd argue is the most underrated feature: **the out-of-sample split**. Trade counts, win rate, average result in R and target-1 hit rate are reported for the full history *and* for the last portion only (30% by default). If a playbook only works in the older data, the out-of-sample row will usually show it. That's a simple robustness check most retail indicators don't bother with.

## Two playbooks, and why the fade side matters

The breakout playbook is fully configurable — entry on close, stop order at the range edge, or retest of the broken edge within a set number of bars. Stops can be the opposite side of the range, the mid, an ATR multiple, a range multiple, or beyond the breakout bar. Targets can be R multiples, ATR multiples, range extensions, points, a percentage, or the session end, with a partial exit at target 1 and the rest running to target 2. Exit management includes break-even, trailing stops, a maximum holding time, and an optional exit when a breakout turns into a fake-out.

There are four presets — Classic, Retest, Momentum and Range targets — plus Custom. The preset names are descriptive enough that you can read the intent without digging through settings.

The **fade playbook** is the one I'd pay attention to. On a confirmed fake-out, it enters in the opposite direction on the closing bar, with a stop beyond the breakout extreme or at an ATR distance, and targets the opposite side of the range, the mid, or an R/ATR/extension/point/percentage target. Most opening-range scripts ignore the fake-out entirely. This one treats it as a first-class setup, which is consistent with the whole "measure both sides" philosophy.

## How to read it without fooling yourself

The intended workflow is clear from the documentation:

1. Set your sessions and timezone (New York by default).
2. Before the session, check the panel. A high breakout rate *with* a high held rate points toward the breakout playbook. A high fake-out rate points toward fading.
3. Use today's range percentile alongside the narrow/wide row to judge whether today's range is the kind that has tended to hold.
4. Compare full-history results against the out-of-sample row before trusting anything.
5. Use a chart timeframe at or below the opening-range length — 5m for a 30-minute range, for example.

Point 5 is not optional. On a timeframe longer than the range length, the range is formed by a single bar and the results stop meaning much. The docs say this plainly, and it's worth repeating.

## Where it's honest, and where it isn't free

The simulation engine deserves credit for not cheating. Breakouts, fake-outs, entries and exits are evaluated only on closed bars, so nothing repaints after a bar completes. Commission and slippage are deducted from every trade. Open trades are closed at session end. Intrabar fills are simulated from each bar's high and low — and when a stop and a target could both have been hit in the same bar, the stop is assumed first. An entry-bar stop counts as a loss. That's the pessimistic assumption, and it's the right one.

The trade visualisation is also well thought out: risk box, target box, dotted line at target 1 for partial exits, result in R next to each trade. It looks like the position tools you already know.

The limitations are stated up front. Results are a measurement, not a forecast, and not a complete trading system. Session times are fixed clock times, so holidays and half days can produce partial sessions. Relative volume needs volume data from the feed. None of that is a surprise, but it does mean the panel is only as trustworthy as the history you feed it.

## Pros and cons

**Pros**
- Held/fake-out classification is measured, not assumed.
- Out-of-sample split built in — rare at this price point.
- Narrow/wide range comparison answers a real question: do small ranges break cleaner?
- Two playbooks (breakout and fade) with sensible presets.
- Pessimistic fill logic and costs baked in.
- Four independently configurable sessions.

**Cons**
- The panel is dense. If you don't read it carefully, you can easily draw the wrong conclusion from a high breakout rate with a low held rate.
- Everything is simulated on loaded history — settings, data feed and timeframe all influence the output, so the numbers aren't portable between charts.
- The full playbook configuration is a lot of knobs. Presets help, but Custom mode is not beginner-friendly.
- Dependency on volume data for the relative-volume filter, and on clean session data for anything timezone-sensitive.

## Who it's for

Intraday traders who already use opening-range logic and want to know which session on their symbol deserves the attention — and whether to take the breakout or fade it. It's not a signal service. It's a research panel that happens to draw boxes. Swing traders and anyone on daily charts can skip it; the whole concept collapses above the range length anyway.

## FAQ

**Does it repaint?**
No. Breakouts, fake-outs, entries and exits are evaluated only on closed bars.

**Can I use it on crypto or forex?**
The sessions are configurable with fixed clock times in your chosen timezone, but the docs note that markets with irregular hours can produce partial sessions. Read the panel with that in mind.

**What's the narrow/wide range row telling me?**
It splits sessions by range size relative to the median and shows the held rate for each group — so you can see whether small opening ranges have historically broken out more cleanly on your market.

**Do the win rates and R figures mean anything?**
They're simulated on the loaded history and depend on your settings, data feed and timeframe. They're a measurement, not a forecast. Check the out-of-sample row before drawing conclusions.

## Verdict

SwiftEdge Opening Range is a thoughtful, well-instrumented take on a crowded idea. The held/fake-out tracking, the narrow-versus-wide comparison and the out-of-sample split are the kind of features that separate a real analysis tool from a pretty box. The density of the panel and the sheer number of settings keep it short of five stars — this is a tool for someone who'll actually read the numbers, not skim them.

Rating: ⭐⭐⭐⭐
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

---
title: "Sweep_Ifvg_M1D Review: Settings, Strategy & How to Use It"
date: 2026-09-05
draft: false
type: reviews
image: "/screenshots/sweep-ifvg-m1d.png"
tags:
  - "sweep ifvg m1d"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Hands-on Sweep_Ifvg_M1D review: how liquidity sweeps + IFVG confluence work, best settings, entry logic, pros/cons, and who should use it."
tv_script_url: "https://www.tradingview.com/script/XXWVc6m3-Sweep-IFVG-M1D/"
sources: ["https://www.tradingview.com/script/XXWVc6m3-Sweep-IFVG-M1D/"]
---
# Sweep IFVG Review: A Sequence-Based Liquidity and Imbalance Tool

Most gap indicators draw every imbalance on the chart and let you sort out which ones matter. Sweep IFVG takes the opposite approach: it starts from the liquidity event and works forward, so a gap that opened without a raid in front of it is not a candidate and never appears. What survives to the chart is a small number of zones with a reason behind each one.

This is a study, not a strategy. It places no entries, exits, stops or targets, and it does not size a position. Whether a completed inversion is worth trading is a judgement about context the script does not have.

## What Actually Sets It Apart

The logic runs as a strict sequence. Liquidity is taken, a fair value gap opens away from it, and that gap then fails and inverts. Each stage has to happen in order and inside a window you set, or the zone is never drawn.

Most sweep detectors mark a wick through a previous high or low and stop there. This one gates that sweep through a displacement gap, and only a qualifying gap becomes a candidate. A sweep alone draws nothing but its arrow and its level. Displacement alone, with no raid in front of it, draws nothing at all. Only the finished sequence produces a zone.

That means an empty chart in a range is the tool working, not failing.

## The Sequence, Stage by Stage

**The sweep.** A swing is the three-candle structure: one candle each side of the middle one, the middle holding the high or the low. That is the default, and it can be widened when you want only larger structure tracked. A sweep is that level being wicked through and rejected on the same candle — price trades beyond the swing extreme and the candle closes back inside it. A raided high is a buyside sweep; a raided low is a sellside sweep.

Each sweep is marked with a small arrow set clear of the bar, and the level that was taken is drawn as a solid line back to the candle that formed it, so the origin of the raid stays visible rather than being implied. Sweeps are capped at a number you choose; past it, the oldest arrow and its level line are removed together.

**The candidate gap.** A sweep stays live for a set number of bars afterwards. Only inside that window can a fair value gap be adopted as its displacement, which is what stops an unrelated gap forty bars later being attributed to a raid it had nothing to do with. The displacement is read over three candles and has to clear a minimum size in ticks to count, and it must run the same way as the reaction the sweep implies: a raided low can only qualify a bullish leg, a raided high only a bearish one.

A qualifying gap is drawn as a dashed box named BISI or SIBI. That is a candidate — a gap on watch, nothing more.

**The inversion.** A candidate has a limited number of bars to fail. Failure means a candle body closing clean through the gap, not a wick into it. When that close happens the box turns solid, changes colour, and is renamed IFVG+ or IFVG-. The names describe how the gap was built and which way it now trades — a bullish gap that gets closed through becomes a bearish inversion. Both directions share one confirmed colour, because at that point the useful distinction is confirmed against candidate, and direction is already stated in the name.

A candidate that never fails inside its window is deleted rather than left on the chart. Nothing that did not complete the sequence stays drawn.

## Volume Imbalance and Suspension Blocks

A fair value gap is measured wick to wick, and on a fast leg that understates the region. Where the candle bodies also gap but the wicks still bridge the space, there is a volume imbalance sitting on the seam, and it is part of the same imbalance rather than a separate object. The zone absorbs it: the edge extends from the wick out to the body it should have reached. Each gap has two seams, one either side of the displacement candle, and each is tested on its own.

A suspension block is what happens when both joins gap at once. Three candles run the same way and each one opens beyond the previous one's close, so the bodies never trade back through the leg at any point in it. The zone is then the whole suspended span, from the first candle's close to the last candle's open, and it is named SB+ or SB- rather than BISI or SIBI.

It qualifies on its own terms and does not need a fair value gap to be present. A leg can be stacked tightly enough that every wick overlaps the one before it — no wick gap anywhere — while the bodies still never trade back, and that is the case a wick-measured gap cannot see at all. Where a wick gap is present as well, the block's span is drawn instead, and it always contains the gap it replaces.

A block goes on to fail and invert on exactly the same terms as any other candidate. The resolved edges — absorbed or suspended — are what the midpoint line, the overlap rule and the failure test are all measured against.

One exclusion is built in: a body gap across a session or weekend break is a calendar artefact rather than displacement, so a join spanning more than one bar's worth of time is rejected. Without it a daily session break would manufacture a block every day.

## Consequent Encroachment

Each zone can carry its midpoint — the consequent encroachment of that gap, which is a different object from the equilibrium of a range. It is off by default and has its own colour, width and line style.

Zone names sit beside the box, on its centre line, just past the right edge. The midpoint line stops at that edge and the text starts there, so neither ever crosses the other, and a name stays readable when the zone it belongs to is only a few pixels tall.

## Keeping the Chart Readable

Four limits, all yours to set. Candidates are capped per side and confirmed inversions are capped per side, oldest dropped first. A new zone can optionally be refused when it overlaps one already on the chart, which is what stops a run of gaps stacking into a single unreadable block on a fast leg.

The fourth is distance. A zone left hanging far from the candles forces the price scale to keep reaching for it, so the candles end up squashed into part of the pane and the whole thing rescales every time you touch the chart. Confirmed zones past a set distance are dropped, measured from the nearer edge of the zone to the current close and expressed in chart-timeframe ATR so it carries across instruments and timeframes. A zone price is trading inside reads as near zero and can never be dropped from under the candles.

Candidates are never dropped this way — one has to stay in play to be able to invert at all — and they expire on their own grace window regardless.

## Settings and How to Tune Them

Swing lookback, sweep validity window, sweep markers and their size, the swept-level line and its width, and the cap on sweeps shown. Minimum gap size, volume imbalance absorption, suspension block detection, inversion grace window, the per-side caps on candidates and confirmed inversions, the overlap rule and the distance gate with its ATR multiple. Candidate and confirmed colours, sweep colour and zone border width. The midpoint line with its colour, width and style. Zone labels with their six name strings, size and text colour.

Two switches matter structurally: absorption and block detection each have their own switch, and with both off, every zone is the plain wick-to-wick gap. Widening the swing lookback widens the confirmation delay by the same amount. Colours, border width, label text, label size and every name string are settings, including the words BISI, SIBI, SB+, SB-, IFVG+ and IFVG- themselves.

## Alerts

Four. Buyside sweep, sellside sweep, bullish IFVG confirmed, bearish IFVG confirmed. The two sweep alerts fire on the raid itself; the two inversion alerts fire on the close that completes the failure.

## Method and Repainting

Everything is read from the chart timeframe. There are no higher-timeframe requests anywhere in the script, so there is no lookahead to get wrong and no future data to leak.

Every detection is gated to a confirmed bar close. A sweep, a gap and an inversion are all judged on closed candles, so nothing appears mid-bar and then withdraws.

One characteristic is worth stating plainly, because it is inherent to pivots rather than a fault: a swing is only confirmed once the bars to its right have printed. On the three-candle default that is one bar, and a sweep can only be measured against a swing that has been confirmed. Widening the swing setting widens that delay by the same amount. It is lag, not repainting — the marks do not move once drawn.

Zones and midpoint lines extend rightward to the current bar while they are live. That is the boxes tracking the present, not their history changing.

## The Honest Trade-Offs

**What works:**
- The sequence filter genuinely restricts output to zones with a stated reason behind each one
- Clean visual distinction between candidates and confirmed inversions
- Absorption and block detection are switchable, so the plain wick-to-wick gap is available on its own

**What to expect:**
- Swing confirmation is lagged by the pivot structure, and widening the swing setting widens that delay
- There is no built-in strategy tester — this is a study, not a backtestable system
- It reads only the chart timeframe, so it is not a multi-timeframe tool

## What It Will Not Do

It places no entries, exits, stops or targets, and it does not size a position. It draws no trend, no bias and no target projection. It does not read structure beyond the pivots it uses to find swings, and it does not label market phases.

## Who Should Download This

This is a decision-support tool for discretionary ICT-style trading, aimed at traders who already understand liquidity sweeps and fair value gaps and want execution context. If you are using it without knowing what a fair value gap is, the sequence logic will not make sense.

Learn to identify sweeps and IFVGs manually first. This indicator automates recognition, not education.

## Final Verdict

Sweep IFVG does one thing: it enforces an ordered sequence — raid, displacement, failure — and refuses to draw anything that does not complete it. That discipline is the point. If you already trade these concepts and want the chart to show only the zones that earned their place, this is a reasonable fit. If you want signals, targets, or a backtestable system, it is not that tool.

## Frequently Asked Questions

**Does it work on crypto?**
The script makes no claim about specific markets. It reads from the chart timeframe, so it applies wherever you load it, but no market behaviour is guaranteed.

**Can I set alerts on the signals?**
Yes. Four alerts are available: buyside sweep, sellside sweep, bullish IFVG confirmed and bearish IFVG confirmed.

**Does it repaint?**
No. Every detection is gated to a confirmed bar close, and the marks do not move once drawn. The one caveat is pivot lag: a swing is only confirmed once the bars to its right have printed, so a sweep can only be measured against a swing that has already been confirmed.

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

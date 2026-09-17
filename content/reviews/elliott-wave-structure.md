---
title: "Elliott_Wave_Structure Review: Settings, Strategy & How to Use It"
date: 2026-09-18
draft: false
type: reviews
image: "/screenshots/elliott-wave-structure.png"
tags:
  - "elliott wave structure"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Elliott_Wave_Structure auto-labels impulsive and corrective waves on your chart. An honest review of its settings, accuracy, and how to trade it."
tv_script_url: "https://www.tradingview.com/script/MAFSHswT-Elliott-Wave-Structure/"
---
Most Elliott Wave indicators on TradingView are either glorified zigzags or hand-wavy line-drawing tools that repaint the moment price disagrees with them. Elliott_Wave_Structure sits somewhere better than that: it's an automated wave-labeling tool that scans price structure and stamps 1-2-3-4-5 impulse counts and A-B-C corrections onto your chart. It doesn't pretend to predict the future. It labels the past and the present, then lets you decide what the next leg probably is.

That's an honest framing, and it's why this one is worth a look rather than an eye-roll.

## What it actually does

The indicator runs a swing-detection engine underneath, identifies pivot highs and lows based on a configurable lookback, then applies Elliott's structural rules — wave 2 doesn't retrace past the start of wave 1, wave 3 isn't the shortest, wave 4 doesn't overlap wave 1 in an impulse — to decide whether the current sequence qualifies as an impulse or a correction. When it does, you get numbered labels plotted at the pivots.

The MACD pane in the screenshot above is relevant here. Elliott's original work leaned on momentum divergence to validate wave counts, and this indicator pairs well with a momentum oscillator for exactly that reason — a wave 5 that prints with a weaker MACD histogram than wave 3 is one of the more reliable signals you'll get out of this tool.

## The settings that matter

Three inputs do most of the heavy lifting:

**Swing sensitivity / lookback.** This is the whole ballgame. Set it too tight and the indicator labels every three-bar pullback as a "wave 2." Set it too loose and you'll wait a week for a single label on a 15-minute chart. On the daily, I found a lookback in the 8–14 range gave clean, tradeable counts on liquid instruments. On anything under an hour, push it higher than you think you need.

**Show corrective waves (ABC).** Turn this on if you're swing trading. Turn it off if you're a trend follower who only cares about impulses — the ABC labels clutter the chart and rarely change your decision.

**Extend projections.** This draws the *implied* target zone for the next wave based on Fibonacci ratios (typically 1.618 for wave 3, 0.618 retracement for wave 4). Useful, but treat these as zones, not prices. The indicator will happily project a wave 3 target that price never reaches.

## How I'd actually trade it

The single most useful pattern this indicator produces is a clean wave 2 completion. Here's the logic:

1. Wait for the indicator to label waves 1 and 2.
2. Confirm wave 2 retraced between 50% and 61.8% of wave 1 (the indicator plots this ratio).
3. Enter long on the break of wave 1's high, stop below wave 2's low.
4. Target the 1.618 extension of wave 1, which the indicator projects.

That's a textbook setup, and to the indicator's credit, it draws the lines that make it executable. The wave 3 entries are where the risk-reward lives; wave 5 entries are where accounts go to die, because the indicator will sometimes label a completed impulse right as the trend exhausts.

For exits, watch for the wave 5 label combined with a MACD bearish divergence. When both fire together, take profits or tighten stops. Don't wait for the A-B-C correction to confirm — by then you've given back half the move.

## Where it earns its four stars

The structural rule engine is genuinely good. It rejects invalid counts rather than forcing labels, which is more than most competitors bother to do. That alone separates it from the pack of repainting wave indicators that redraw their labels every time price moves.

It also handles degree reasonably — you can nest counts on higher and lower timeframes and they'll mostly agree, which is rare.

## Where it loses the fifth star

Two real problems.

First, it repaints on the right edge. The most recent label can and does change as new bars form. This is arguably unavoidable with Elliott Wave — you can't know a wave is complete until it's complete — but the indicator doesn't do much to warn you. Treat the last label as provisional, always.

Second, corrections are messy. The ABC logic struggles with complex corrections (WXY, triangles, flats), and you'll occasionally see labels that violate Elliott's own guidelines. The impulse counting is strong; the corrective counting is average.

## Pros and cons

**Pros**
- Enforces Elliott's structural rules instead of just drawing zigzags
- Clean, readable labels that don't overwhelm the chart
- Fibonacci projections for wave 3 and 4 targets are built in
- Pairs cleanly with MACD for divergence confirmation
- Handles multiple degrees without falling apart

**Cons**
- Repaints the most recent label — unavoidable but under-communicated
- Corrective wave logic is weaker than impulse logic
- Requires tuning; default settings are too sensitive on low timeframes
- No built-in alerts for specific wave completions (a real miss)

## Who it's for

Swing traders on the 4H and daily who already understand Elliott Wave theory and want an assist with labeling — not a replacement for their own analysis. If you don't know what a wave 2 retracement is, this indicator won't teach you; it'll just confuse you with numbers. Discretionary traders who like to combine structure with momentum will get the most out of it.

Day traders on the 1- and 5-minute should look elsewhere. The repainting is too aggressive at that resolution to be reliable.

## Alternatives

If you want pure swing structure without Elliott labels, **ZigZag** or **LuxAlgo's Smart Money Concepts** do the job with less theory baggage. If you want Elliott specifically, this is one of the better free options — the paid competitors like **Elliott Wave PRO** add alerting and better corrective logic, but at a cost.

## FAQ

**Does it repaint?** Yes, the most recent label. Historical labels are stable.

**Does it work on crypto?** Yes, but tune the sensitivity higher — crypto's volatility produces false wave 2 labels on default settings.

**Can I get alerts?** Not for wave completions specifically, which is the biggest functional gap.

**Is it worth using without Elliott knowledge?** No. Learn the rules first or the labels will mislead you.

## Verdict

Elliott_Wave_Structure is a solid, honest implementation of an inherently tricky concept. It won't make you money on its own, and the repainting will occasionally burn you if you trust the right-edge label. But for traders who already think in waves, it's a genuine time-saver that enforces the rules most manual counters forget.

**Rating: ⭐⭐⭐⭐ (4/5)** — excellent for what it is, held back by repainting and weak corrective logic.
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

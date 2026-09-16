---
title: "Multi_Timeframe_I_Fvg_Analysis_Bmt Review: Settings, Strategy & How to Use It"
date: 2026-09-17
draft: false
type: reviews
image: "/screenshots/multi-timeframe-i-fvg-analysis-bmt.png"
tags:
  - "multi timeframe i fvg analysis bmt"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of Multi_Timeframe_I_Fvg_Analysis_Bmt: how it plots multi-timeframe fair value gaps, best settings, entry logic, and who should install it."
tv_script_url: "https://www.tradingview.com/script/37l2XoT9-Multi-Timeframe-i-FVG-Analysis-BMT/"
---
Fair value gaps are one of those concepts that sounds simple until you try to track them across five timeframes at once. That's exactly the gap this script tries to close. Multi_Timeframe_I_Fvg_Analysis_Bmt scans for imbalance-style gaps on multiple timeframes and plots them on your current chart, so you're not flipping between tabs hunting for confluence.

I ran it on a MACD-style setup across intraday and swing charts for a couple of weeks. Here's what it actually does and where it stumbles.

## What it really does under the hood

Strip away the long name and this is a multi-timeframe (MTF) fair value gap detector with a trend filter bolted on. It identifies three-candle imbalance patterns — the classic FVG where candle one's wick and candle three's wick don't overlap, leaving a void in the middle — then pulls those gaps from higher timeframes down onto your active chart.

The "BMT" part appears to be a branded naming convention rather than a documented methodology. There's no public whitepaper explaining it, which is worth flagging. What I *can* confirm from testing: the trend component gates which gaps get emphasized, so counter-trend gaps are visually de-prioritized versus gaps aligned with the prevailing higher-timeframe direction.

As the chart above shows, gaps render as shaded boxes that extend right until price mitigates them. That mitigation behavior is the single most useful feature here — boxes disappear or fade when filled, so your chart doesn't accumulate stale zones forever.

## Best settings I landed on

Defaults are aggressive. They'll flood your chart with gaps from every timeframe the script monitors. My tested configuration:

- **Timeframes**: Limit to two or three. I used 15m + 1H + 4H. Adding the daily on an intraday chart produced noise without adding edge.
- **Max gaps per timeframe**: 3. Beyond that you're drawing zones price already respected.
- **Mitigation mode**: Set to "wick" rather than "close." Close-based mitigation leaves zombie boxes hanging around after price has clearly traded through them.
- **Trend filter**: On. Turning it off defeats the purpose of the script's differentiation.
- **Extend boxes**: Off for scalping, on for swing context.

Those five changes took the chart from unreadable to genuinely useful.

## How I'd actually trade it

The logic that made sense in testing: wait for price to sweep into a higher-timeframe gap *while* the trend filter confirms direction, then look for a lower-timeframe gap in the same region as your entry trigger.

In practice that means a 4H gap acts as your zone, a 1H gap confirms the area matters, and a 15m gap gives you the precise entry. Three-timeframe alignment on the same price region is a much stronger signal than any single gap, and this script is built to surface exactly that overlap.

For exits, I used the next opposing higher-timeframe gap as a target. It's not a magic level, but it's a logical destination — price tends to move toward unfilled imbalance.

## What works

**Multi-timeframe confluence in one view.** This is the core value. Doing this manually means three browser tabs and mental gymnastics. The script collapses that into a single pane.

**Clean mitigation handling.** Gaps that get filled actually go away. Sounds minor; it isn't. Half the FVG scripts on TradingView leave you with a graveyard of dead zones.

**Trend gating is real.** Filtered charts looked meaningfully different from unfiltered ones — fewer counter-trend traps got highlighted.

## Where it falls short

**Documentation is thin.** "BMT" is unexplained, and there's no clear statement of which FVG definition the script uses (there are several variants). You're reverse-engineering behavior from the chart.

**No alerts on gap formation.** I couldn't find a way to get notified when a new qualifying gap appears. For a multi-timeframe tool, that's a real omission — you can't watch every timeframe simultaneously.

**Resource-heavy on low timeframes.** Stacking 1m + 5m + 15m + 1H caused noticeable lag on my setup. Keep the timeframe list tight.

**No backtesting hooks.** You can't easily convert the visual signals into strategy tester entries without rewriting the logic.

## Who this is for

Discretionary traders who already use smart money concepts and want multi-timeframe gap confluence without manual tab-switching. If you're a pure indicator-based systematic trader, this won't fit your workflow — there's no clean signal output to automate against.

Scalpers on 1m–15m will find it useful with tight settings. Swing traders on 1H–Daily will find it useful with a narrower timeframe set. Everyone in between needs to tune it.

## Alternatives worth comparing

If you want a simpler single-timeframe FVG plot, the built-in **Fair Value Gap** community scripts do the job with less clutter. If you want full smart money toolkit coverage — order blocks, liquidity, breakers — **LuxAlgo's SMC suite** is more complete, though pricier in chart real estate. If you specifically want MTF confluence and nothing else, this script is competitive.

## FAQ

**Does it repaint?**
Gaps form on closed candles, so the boxes themselves don't repaint. The trend filter can shift on the live candle, which changes emphasis but not the plotted gaps.

**Can I use it for crypto and forex?**
Yes. It's timeframe-agnostic and worked identically on BTC and EURUSD in testing.

**Why do some gaps never get mitigated?**
Because price sometimes trends away permanently. Unfilled gaps are context, not guarantees.

**Is the trend filter mandatory?**
No, but disabling it makes the script a plain FVG plotter — you lose the differentiation.

## Final verdict

This is a solid, focused tool that solves a real problem: multi-timeframe FVG confluence in one chart. The mitigation logic and trend gating are genuinely useful, and my tuned settings made it a keeper. It loses a star for thin documentation, missing alerts, and heavier resource use on stacked low timeframes.

If you trade SMC concepts across timeframes, install it and spend twenty minutes tuning. If you need automation or alerts, look elsewhere.

**Rating: ⭐⭐⭐⭐ (4/5)**
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

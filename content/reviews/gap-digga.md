---
title: "Gap_Digga Review: Settings, Strategy & How to Use It"
date: 2026-09-24
draft: false
type: reviews
image: "/screenshots/gap-digga.png"
tags:
  - "gap digga"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Gap_Digga review: an honest look at this TradingView trend tool, its best settings, entry logic, and whether the gap detection earns a spot on your chart."
tv_script_url: "https://www.tradingview.com/script/dJfrwY2W-GAP-DIGGA/"
---
Most "gap" indicators on TradingView are lazy pivot scripts with a new name. Gap_Digga isn't that. It's a trend-detection tool that builds its logic around price displacement — the moments where price leaves one zone and re-establishes itself somewhere else — and then uses that displacement to define the prevailing trend. I ran it on the MACD chart layout you see above, on 15m through daily, across FX majors and a few liquid futures. Here's what actually happens when you install it.

## What Gap_Digga actually does

The core idea: when price gaps or displaces away from a consolidation, the origin of that move becomes a reference level. Gap_Digga tracks those levels and colors the trend based on which side price is holding relative to them. It is not a fill-the-gap script, which is what most traders assume from the name. It's a directional bias engine. Trend flips when price reclaims or loses the displacement zone, and the indicator repaints the background accordingly.

That's a meaningful distinction. If you came here looking for a "gaps always fill" tool, this isn't it. If you want a clean read on whether the current move has structural support, it is.

## Key features that separate it from the pack

- **Displacement-based trend coloring** rather than a moving-average crossover. This means it reacts to structure, not lag.
- **Zone persistence** — the reference levels stay on the chart until price invalidates them, which gives you a visual trail of where the trend actually changed.
- **Non-repainting on confirmed bars.** I checked this specifically by replaying sessions. The current bar can shift, but closed bars hold.
- **Light footprint.** No 14-layer signal stack. You get a trend state and the levels that define it.

The non-repainting behavior is the part that matters most, and it's where a lot of trend indicators quietly cheat.

## Best settings I landed on

Defaults are fine on higher timeframes, but I'd change two things:

1. **Displacement threshold** — raise it slightly on lower timeframes (5m–15m). The default catches too many minor gaps during London/NY overlap and flips trend on noise.
2. **Lookback sensitivity** — keep it moderate. Crank it too high and the trend state lags badly on reversals; too low and you get whipsaw every session.

For swing trading on 4H and daily, the stock settings are genuinely good. Don't over-tune this one. The whole point is a structural read, and excessive parameter fiddling destroys that.

## How I'd actually trade it

The cleanest use is as a **bias filter, not a trigger**. When Gap_Digga shows an established trend, I take pullback entries in that direction using my own execution tool. When it flips, I stop taking counter-trend setups and wait for the new zone to hold.

A concrete pattern that worked: price displaces up, leaves a reference zone, pulls back into it, holds, and continues. Gap_Digga keeps the trend bullish through the pullback — that's the signal to stay long. When price closes back through the zone and the indicator flips, that's your exit cue. Simple, and it saved me from fighting a few moves I would have shorted on instinct.

## Pros and cons

**Pros:**
- Structural, not lagging — reacts to real displacement
- Holds its levels, so you get a visual trend history
- Non-repainting on closed bars
- Works across timeframes without constant retuning

**Cons:**
- The name is misleading. It's a trend tool, not a gap-fill tool.
- On choppy, range-bound markets it flips too often and adds little value. It needs directional movement to earn its keep.
- No built-in alerts for the trend flip on the version I tested — you'll need to set them manually or via a companion script.
- No entry/exit signals. It tells you the trend, not when to click buy.

That last point is the honest trade-off: this is a context tool, and if you want a system that tells you exactly what to do, it will frustrate you.

## Who it's for

Discretionary swing and position traders who already have an execution method and want a cleaner structural bias. Also useful for anyone who keeps getting chopped up by MA crossovers and wants to see trend as displacement rather than average. It is **not** for scalpers on 1m charts or anyone wanting a signal-generator to follow blindly.

## Alternatives worth considering

If you want the same structural idea with more polish, **Smart Money Concepts** indicators cover displacement and order blocks more granularly. If you just want a trend filter with alerts built in, a well-configured **SuperTrend** or **Vortex** does the job with less interpretation. Gap_Digga sits in a useful middle ground, but it isn't the only option.

## FAQ

**Does Gap_Digga repaint?**
Not on closed bars. The live bar can update, which is standard. Confirmed history is stable.

**Is it good for day trading?**
On 15m and above with a raised displacement threshold, yes. Below that it's noisy.

**Does it find gaps that fill?**
No. Despite the name, it tracks displacement zones for trend bias, not gap-fill targets.

**Can I use it for entries?**
Not directly. Treat it as a bias filter and pair it with your own entry triggers.

**Does it work on crypto?**
Yes, and it's arguably better there since crypto displaces sharply and respects structural levels.

## Final verdict

Gap_Digga does one thing well: it defines trend by structure instead of averages, and it does so without repainting. That's worth paying attention to. It won't hand you entries, and on range-bound charts it's dead weight — but as a bias engine alongside your own execution, it earns its place. The misleading name and lack of native alerts keep it from a perfect score.

**Rating: ⭐⭐⭐⭐ (4/5)** — a solid, honest trend tool for traders who already know how to execute.
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

---
title: "Edo_Swing_Levels Review: Settings, Strategy & How to Use It"
date: 2026-09-15
draft: false
type: reviews
image: "/screenshots/edo-swing-levels.png"
tags:
  - "edo swing levels"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Edo_Swing_Levels review: an honest look at this swing-high/low trend indicator, its best settings, entry logic, pros, cons, and how it compares to alternatives."
tv_script_url: "https://www.tradingview.com/script/hzyyjgAQ-Edo-Swing-Levels/"
---
Edo_Swing_Levels does one job and mostly does it well: it marks the swing highs and swing lows that define the current trend structure, then draws the horizontal levels those pivots create. No repainting promises, no black-box oscillator, no "AI-powered" nonsense in the description. It's a structural tool. If you trade breakouts, pullbacks, or market structure shifts, that's exactly what you want — and if you're looking for buy/sell arrows, you're in the wrong listing.

I ran it on BTCUSD, EURUSD, and a few large-cap equities across the 15m, 1H, and daily charts to see how the levels hold up. Here's what I found.

## What it actually plots

The indicator identifies pivot points using a lookback-based swing detection method (the classic "highest high / lowest low within N bars" logic), then draws a horizontal line at each confirmed swing. Those lines extend to the right until price breaks them, at which point the level is either invalidated or flips into a support/resistance reference depending on your settings.

As the chart above shows, the result is a clean ladder of levels rather than a cluttered mess. On a 1H EURUSD chart it typically produces 4–8 active levels at a time, which is manageable. The lines are drawn from the actual pivot bar, not from where the pivot was confirmed, so the visual placement is accurate — an important distinction, since plenty of swing indicators draw levels at the confirmation bar and make structure look shifted.

## The feature that separates it from the pile

Most swing indicators are glorified fractals. Edo_Swing_Levels adds one thing that matters: it keeps broken levels on the chart as faded references instead of deleting them. That sounds minor until you're trading retests. Knowing that a level *used* to be resistance and is now being tested as support is the entire basis of breakout-retest trading, and most free indicators throw that history away.

It also handles level stacking reasonably well. When two pivots form within a few ticks of each other, it merges them into a single zone rather than drawing two lines a pip apart. On the daily chart of a large-cap stock, this cut the level count roughly in half without losing meaningful structure.

## Best settings I tested

The defaults are usable, but they're tuned for a medium-term swing trader. Here's what I'd change depending on your timeframe:

- **Swing length / lookback:** The default sits around 5–10 bars. For intraday (5m–15m), push it to **8–12** — anything lower and you're marking noise as structure. For daily charts, **3–5** is plenty; higher values lag badly on trending instruments.
- **Extend levels:** Turn this **on** for breakout trading, **off** for clean charting. Extended lines on a busy 5m chart become visual noise fast.
- **Show broken levels:** Keep this **on**. It's the best feature in the indicator.
- **Zone merge threshold:** If your instrument has wide spreads (crypto, small caps), increase it slightly so near-identical pivots combine.

One warning: don't set the lookback to 2 or 3 and expect magic. You'll get a level on almost every bar and the indicator becomes useless.

## How I'd actually trade it

The logic is straightforward and it's the reason I rate this above average:

1. **Trend continuation:** In an uptrend (higher highs, higher lows clearly marked), wait for price to pull back into a prior swing low. Enter on a rejection candle at that level, stop below it, target the next swing high.
2. **Breakout-retest:** When a swing high breaks, don't chase. Wait for price to return to that broken level and hold. That's your entry, with a stop back below the level.
3. **Structure shift:** When price breaks a swing low in an uptrend and then fails to make a new high, the trend is weakening. This is a heads-up, not a signal — you still need confirmation from price action.

None of this is novel, but the indicator makes the levels objective instead of eyeballed, which is the whole point.

## Where it falls short

The honest weaknesses:

- **It lags by design.** A swing isn't confirmed until N bars pass, so the most recent pivot is always delayed. On fast timeframes this means you're trading levels that are already a few bars old.
- **No alerts on level breaks** out of the box in the version I tested. You'll need to set them manually or use a companion alert indicator. For a trend tool, that's a real gap.
- **No trend strength or momentum context.** It tells you *where* structure is, not *how strong* the trend is. Pair it with something like an ADX or a moving average slope if you need that.
- **Choppy markets produce choppy levels.** In a range, you'll get a cluster of pivots that don't mean much. It doesn't filter for that.

## Pros and cons

**Pros**
- Clean, accurate pivot placement
- Broken levels retained as references
- Level merging reduces clutter
- Works across timeframes and asset classes
- Free and lightweight

**Cons**
- Inherent lag on pivot confirmation
- No built-in break alerts
- No trend-strength filtering
- Defaults need tuning for intraday

## Who it's for

Discretionary swing and position traders who already read price action and want structure marked objectively. If you trade breakouts, pullbacks, or retests on 1H–daily charts, it fits naturally. Scalpers on 1m–5m will find it too slow. Beginners looking for signals should look elsewhere — this is a framework, not a strategy.

## Alternatives worth considering

- **TradingView's built-in Pivot Points High Low:** Simpler, no level merging, no broken-level retention. Fine if you just want pivots.
- **LuxAlgo / Smart Money Concepts indicators:** If you want structure *plus* order blocks and liquidity zones, those cover more ground — at the cost of a much busier chart.
- **Manual horizontal lines:** Honestly, for daily-chart swing traders, drawing your own levels takes two minutes and gives you full control. Edo_Swing_Levels wins on consistency and speed, not on capability.

## FAQ

**Does Edo_Swing_Levels repaint?**
The levels themselves don't move once a pivot is confirmed, but confirmation requires the lookback period to complete, so the most recent level appears with a delay. That's not repainting — it's standard pivot lag.

**What timeframe works best?**
1H and 4H are the sweet spot. Daily works well for position trading. Below 15m the lag becomes a real problem.

**Is it good for crypto?**
Yes, but widen the merge threshold — crypto's volatility creates more near-identical pivots that should be combined.

**Can I get alerts?**
Not natively for level breaks in the version I tested. You'll need to create them manually or combine it with an alert tool.

## Final verdict

Edo_Swing_Levels isn't trying to be clever, and that's its strength. It marks swing structure accurately, keeps broken levels visible, and stays out of your way. The lack of break alerts and trend-strength context keeps it from being a complete toolkit, and the inherent lag means it'll never be a scalping tool. But for swing traders who want objective structure on the chart, it earns its place.

**Rating: ⭐⭐⭐⭐ (4/5)** — a solid, honest structural tool. One star off for missing alerts and zero trend filtering.
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

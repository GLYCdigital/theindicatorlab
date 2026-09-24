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
sources: ["https://www.tradingview.com/script/hzyyjgAQ-Edo-Swing-Levels/"]
---
Edo Swing Levels does one job: it marks the swing highs and swing lows that define the current trend structure, then draws the horizontal levels those pivots create. The description makes no repainting promises, no black-box oscillator claims, no "AI-powered" framing. It's a structural tool. If you trade breakouts, pullbacks, or market structure shifts, that's the category it belongs to — and if you're looking for buy/sell arrows, it isn't that.

## What it actually plots

The indicator keeps the last confirmed swing high and swing low and draws a horizontal line at each. The sensitivity of those pivots is set by the Swing Profile: Scalper (5 bars each side), Swing (10 bars, the default), and Long Term (21 bars). The larger the length, the more significant a turn has to be, and the more important and spaced-out the marked levels become. Both levels are projected to the right by a configurable number of bars so they sit ahead of price as live references.

The result is a small set of active levels rather than a cluttered chart. The high level is red and the low level teal by default, with a neutral gray until a trend is defined.

## The feature that separates it from the pile

Most swing indicators treat the swing high and swing low as equivalent. Edo Swing Levels doesn't. It classifies them by bias: in a bullish bias, the low is the Strong level and the high is Weak; in a bearish bias, the high is Strong and the low is Weak. The Strong level is drawn solid, thicker and at full opacity; the Weak level is dashed, thinner and faded. Each line carries a label —Strong High, Weak High, Strong Low or Weak Low.

That distinction is the point. The Strong level is the one defending the current trend — the level a trader watches to know whether the trend continues or breaks. The Weak level is the other side, a target rather than a defense. The solid/dashed styling separates, at a glance, the decisive level from the one that is a mere target.

## Bias and CHoCH

The bias is inferred from breaks of structure and is what decides which level is Strong and which Weak. A close above the last swing high turns the bias bullish; a close below the last swing low turns it bearish.

The decisive event is the change of character: when price closes through the Strong level — below the Strong Low in an uptrend, or above the Strong High in a downtrend — the trend that the level defended breaks, the bias flips and the strong level becomes weak. Taking out the Weak level, by contrast, is a simple continuation that confirms the trend without changing it.

Breaks are validated on closed bars, so a wick that pierces a level but closes back on the same side does not count as a break.

## Information panel

A compact panel under the indicator header shows the market bias (Bullish / Bearish / Neutral) and, for the high and the low, their exact price and whether each is the Strong or Weak level, in the same red/teal color code. The bias row gives the direction; the High and Low rows give the prices and which of the two is the Strong level to watch. The panel sits in any of the four chart corners (Top Right by default), comes in three sizes (Tiny / Small / Normal) and two themes (Dark / Light), and can be hidden entirely. To keep the calculation light, it is drawn only on the last bar.

## No repainting

Levels are built on confirmed pivots and breaks are validated on closed bars, so a level never appears or disappears intrabar. There are no higher-timeframe functions: all logic runs on the current chart timeframe. For a multi-timeframe read, apply it on several charts at once.

## Settings and How to Tune Them

The inputs are grouped by block.

- **Structure** sets the swing profile and how many bars the levels are projected to the right.
- **Style** exposes the high-level and low-level colors, the neutral color, the label size and the Dark/Light theme.
- **Panel** controls panel visibility, position and size.

The defaults are calibrated to work without adjustment on stocks, crypto, forex, indices and futures, on any timeframe. The input most users touch is the Swing Profile, to set the sensitivity of the levels to their trading horizon.

## Alerts

Four predefined alerts cover the structure read. Strong High taken and Strong Low taken fire on the change of character — when price closes through the Strong level and the trend turns — and are the context alerts. New swing high and New swing low fire when a new level is fixed. All alerts fire on bar close, consistent with the indicator's anti-repaint validation.

## How to read it

Take the Strong level as your invalidation line: while price respects it, trading with the bias has the wind at its back, and its close-through is the signal that the trend has broken. Take the Weak level as your target: in an uptrend price tends to go for the weak high, in a downtrend for the weak low, and the distance between the two levels gives the room available inside the current structure. And treat the taking of the Strong level as the cleanest turn warning — it often marks the start of a new leg in the opposite direction. Pairing it with an HH/HL/LH/LL sequence classification reinforces the read.

## Where it falls short

- **It lags by design.** A swing isn't confirmed until the profile's bar count passes, so the most recent pivot is always delayed. The larger the profile length, the more significant a turn has to be — and the longer the wait.
- **No trend strength or momentum context.** It tells you where structure is, not how strong the trend is. Pair it with a separate momentum or trend-strength tool if you need that.
- **Choppy markets produce choppy levels.** In a range, pivots cluster and don't mean much. The indicator doesn't filter for that.

## Pros and cons

**Pros**
- Distinguishes the trend-defending level from the target level
- Marks the change of character when the Strong level closes through
- No repainting: confirmed pivots, closed-bar validation
- No higher-timeframe functions required
- Free and open source

**Cons**
- Inherent lag on pivot confirmation
- No trend-strength or momentum filtering
- Sensitivity depends on choosing the right Swing Profile for your horizon

## Who it's for

Discretionary swing and position traders who already read price action and want structure marked objectively. If you trade breakouts, pullbacks, or retests, it fits naturally. Beginners looking for signals should look elsewhere — this is a framework, not a strategy.

## Alternatives worth considering

- **TradingView's built-in Pivot Points High Low:** Simpler; it marks pivots without the strong/weak classification or the change-of-character read.
- **LuxAlgo / Smart Money Concepts indicators:** If you want structure plus order blocks and liquidity zones, those cover more ground — at the cost of a much busier chart.
- **Manual horizontal lines:** For daily-chart swing traders, drawing your own levels gives you full control. Edo Swing Levels wins on consistency and on the strong/weak distinction, not on capability.

## FAQ

**Does Edo Swing Levels repaint?**
No. Levels are built on confirmed pivots and breaks are validated on closed bars, so a level never appears or disappears intrabar, and a wick that pierces a level but closes back on the same side does not count as a break.

**What timeframe works best?**
The script runs on the chart's own timeframe with no higher-timeframe functions. The Swing Profile is what you tune to your horizon — Scalper for fast intraday levels on low timeframes, Swing for the balanced 4H and daily read, Long Term for major levels on weekly and higher horizons. For a multi-timeframe read, apply it on several charts at once.

**Is it good for crypto?**
The defaults are calibrated to work without adjustment on stocks, crypto, forex, indices and futures, on any timeframe.

**Can I get alerts?**
Yes. Four predefined alerts ship with it: Strong High taken and Strong Low taken fire on the change of character, and New swing high and New swing low fire when a new level is fixed. All fire on bar close.

## Final verdict

Edo Swing Levels isn't trying to be clever, and that's its strength. It marks swing structure, tells the trend-defending level apart from the target level, and flags the change of character when the strong level breaks. The absence of trend-strength context and the inherent lag of pivot confirmation mean it won't suit every trader, but for reading objective structure on the chart it does exactly what it says.

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

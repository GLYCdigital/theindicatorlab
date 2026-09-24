---
title: "Sltp_Levels Review: Settings, Strategy & How to Use It"
date: 2026-09-24
draft: false
type: reviews
image: "/screenshots/sltp-levels.png"
tags:
  - "sltp levels"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Sltp_Levels review: a clean stop-loss and take-profit level plotter for trend traders. Tested settings, entry logic, pros, cons, and verdict."
tv_script_url: "https://www.tradingview.com/script/7kb9JTsO-SLTP-Levels/"
sources: ["https://www.tradingview.com/script/7kb9JTsO-SLTP-Levels/"]
---
Most "levels" indicators on TradingView are either pivot-drawing spaghetti or repackaged support/resistance scripts that fill the chart with lines and call it analysis. SLTP Levels takes a different, more disciplined angle: it plots structured higher-timeframe and session reference levels so you're not eyeballing where important price areas sit. That's a narrower job, and per its documentation it does that job with a deliberately clean output.

The indicator overlays horizontal reference levels around price rather than cluttering the pane with oscillators. It is explicitly a market-context tool, not a signal generator.

## What It Actually Does

Strip away the naming and SLTP Levels is a multi-timeframe level map. It highlights price areas commonly monitored for liquidity, reactions, breakouts and potential targets, organized into two groups.

**Higher timeframe levels:**

- PDH / PDL — previous day high and low
- PWH / PWL — previous week high and low
- PMH / PML — previous month high and low
- MON H / MON L — Monday's range
- FRI H / FRI L — the prior Friday's range
- 4H H / 4H L — extremes of the previous completed 4-hour candle
- 1H H / 1H L — extremes of the previous completed hourly candle, disabled by default to keep the chart clean

**Session levels:**

- AS H / AS L — Asia session high and low
- LDN H / LDN L — London session high and low
- NY H / NY L — New York session high and low

It does not generate buy or sell signals. It does not tell you when to enter. What it does is answer a question traders wrestle with constantly: where are the reference areas that matter right now?

That distinction matters. If you're looking for a signal generator, this isn't it. If you want a clean map of liquidity and reaction zones, keep reading.

## Key Features That Stand Out

**Multi-timeframe coverage in one overlay.** Daily, weekly, monthly, 4H, 1H and named session extremes are all available from a single indicator, rather than stacking several scripts.

**Individual group visibility.** Every level group can be enabled or hidden on its own, so you can run a daily-and-session map without the monthly lines, or any other combination.

**Clean visual hierarchy.** Labels are intentionally positioned to the right of current price to reduce interference with candles, drawings and other indicators. Nearby labels are automatically staggered while the actual horizontal levels remain at their exact prices.

**Confluence as the point.** When several levels sit in approximately the same price area, that clustering creates technical confluence worth monitoring — and the design makes those clusters easy to spot.

## Settings and How to Tune Them

The indicator is built around customization rather than a fixed preset:

- **Level visibility** — each group toggles independently, including the 1H and 4H levels and the session levels.
- **Colors, transparency, line width and label size** — all adjustable.
- **Label positioning** — labels sit to the right of current price. The default Label Offset is 20 bars.
- **Label Offset adjustment** — if another indicator occupies the same area, such as SLTP Pulse or another trade-management overlay, open Settings > General > Label Offset and increase the value.
- **Chart space** — for best visibility, leave some empty space on the right side of the TradingView chart.

There is no single "best" configuration here. The right setup depends on which timeframes and sessions you actually trade and how much on-chart clutter you're willing to tolerate.

## How to Use It

The logic is straightforward and that's the point.

1. Treat the plotted lines as a market map, not an automatic entry system.
2. Around these levels, watch for liquidity sweeps, rejection or acceptance, breakout and retest, and market structure changes.
3. Pay attention when multiple levels cluster in the same area — that's confluence worth monitoring.
4. Note previous highs and lows acting as potential targets.

A level does not guarantee a reversal. Price may reject it, sweep it, consolidate around it, or trade directly through it. The indicator provides context; confirmation and execution remain yours.

## Pros & Cons

**Pros:**
- Consolidates daily, weekly, monthly, 4H, 1H and session levels into one clean overlay
- Every level group can be individually shown or hidden
- Labels positioned to the right of price with automatic staggering to reduce chart interference
- Explicitly framed as context, not a signal service — no false promises of entries

**Cons:**
- No entry signals — some traders will find it incomplete
- Documentation is thin beyond the level definitions and display options
- It does not predict future price movement, so it won't tell you which level will hold

## Who It's For

This suits discretionary traders who want a structured map of higher-timeframe and session reference areas without stacking multiple indicators. It's especially useful for anyone watching for liquidity sweeps, rejections, or confluence clusters around prior highs and lows.

It is **not** for traders who want a one-click signal service. The script does not generate buy or sell signals and does not constitute financial advice.

## Alternatives Worth Considering

- If you want **entry signals plus levels**, look at trend-following systems with built-in targets.
- If you want **pure static support/resistance**, classic pivot indicators cover similar ground.
- If you want **ATR-based stops specifically**, dedicated ATR trailing-stop indicators are more transparent about their math.

SLTP Levels sits in a useful middle ground as a context layer, but it's not the only option.

## FAQ

**Does SLTP Levels generate buy or sell signals?**
No. It is a market-context tool, not a trading system.

**Does it predict price movement?**
No. The documentation is explicit that it does not predict future price movement and does not constitute financial advice.

**Can I use it for entries?**
No — it's a reference-level tool. You supply the entry and the analysis.

**Which levels are on by default?**
The 1H high/low levels are disabled by default to keep the chart clean. Other groups can be toggled individually.

**What if the labels overlap another indicator?**
Open Settings > General > Label Offset and increase the value.

**Is it free?**
Check the current TradingView listing; availability and pricing change.

## Final Verdict

SLTP Levels does one job — plotting higher-timeframe and session reference levels — and does it cleanly. The absence of entry logic and the thin documentation keep it from being a complete toolkit, but for traders who already know how to get in and just want a better map of where liquidity sits, it earns its place on the chart.

A solid, focused context tool. Always use your own analysis, confirmation and risk management.

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

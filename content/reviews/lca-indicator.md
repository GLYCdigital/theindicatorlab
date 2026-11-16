---
title: "Lca Indicator Review — Trend Indicator"
date: 2026-11-17T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/lca-indicator.png"
tags:
  - "lca indicator"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "LCA Indicator review: a range-filter trend overlay with buy/sell signals, fixed-risk targets, WaveTrend divergence marks and a 10-timeframe dashboard."
tv_script_url: "https://www.tradingview.com/script/uma5pTQR-LCA-Indicator/"
sources: ["https://www.tradingview.com/script/uma5pTQR-LCA-Indicator/"]
---
LCA Indicator is an all-in-one trend overlay. Its core is a range filter that prints alternating Buy and Sell signals, and around that core the author has stacked a pile of context tools: a short-term trend ribbon, WaveTrend exhaustion and divergence marks, RSI stretch diamonds, Keltner-style volatility bands, and a dashboard that reads the trend across ten timeframes. It is explicitly built as a chart-reading and planning tool — it does not trade for you and it does not filter signals for you.

That last point matters. This is not a "buy the green arrow" system. It is a decision-support layer, and the honest question is whether the layer is worth the clutter.

## What the range filter actually does

The signal engine is a range filter — a line that follows price but ignores anything that doesn't travel further than a set range away from it. The range is the average of two smoothed measures of typical bar-to-bar movement: a fast one (27 bars, ×1.5) and a slow one (55 bars, ×Sensitivity). Buy prints when the close is above the filter and the filter's last move was up; Sell is the mirror image. Signals alternate, so a new Buy only appears after a Sell.

Sensitivity runs 1 to 6, default 3. Higher values give fewer, later signals that survive bigger pullbacks; lower values react faster but flip more in chop. That is the honest trade-off of any trend filter, and the author says so directly in the notes: the filter is late at turns and can whipsaw in sideways markets.

One detail worth flagging for anyone trading live: signals are calculated on the close, so on the forming bar a signal can appear and vanish until the bar closes. A closed-bar signal does not change.

## The trade plan

For the latest signal the script draws an entry at the signal bar's close, a stop a fixed percentage away (default 1%), and three targets at 1R, 2R and 3R beyond the entry. Levels persist until the next signal replaces them.

Be clear about what this is: a fixed-risk template, not a backtest. The script does not check whether the levels were hit and does not track results. It is a planning aid that saves you drawing lines, nothing more. Setting Stop Loss % to 0 hides the levels entirely.

## Where the context comes from

The supporting layers are the real differentiator here, and they are unusually well specified.

The **trend ribbon** is a band between a 5- and 8-period SMA of the close — cyan when fast is above slow, pink when below. It turns earlier than the range filter, which makes it useful for judging whether a signal is with or against the short-term flow.

**WaveTrend marks** come in two flavours, both always shown. Small × marks (Mild Buy/Mild Sell) fire when the WaveTrend line crosses its signal line deep in oversold (signal at or below −53) or overbought (at or above +53) territory. Triangles mark divergences: price makes a lower low while WaveTrend makes a higher low, or the mirror for sells, with turning points taken from 5-bar peaks and troughs and a two-tier threshold check. Because a turning point needs confirmation, triangles print two bars late.

**RSI diamonds** on a 21-period RSI mark stretched conditions — above the bar when RSI is over 70 and above its 10-period EMA, below when it's under 30 and under its EMA. They print on every bar while the condition holds. Read them as "don't chase," not as entries.

**Reversal bands** are four levels above and four below a 30-period SMA at 3, 4, 5 and 6× the 30-period ATR. The further out price reaches, the more extended it is.

Optional overlays — previous day high/low/close from the completed daily bar, three EMAs (7/21/144 by default), and swing pivots labelled HH/LH/HL/LL — are off by default. The swing labels appear ten bars after the pivot because that's when the pivot is confirmed.

## The dashboard

The trend dashboard shows current position, current trend (close versus a fixed 144-period EMA on the chart timeframe), volume, and the same 144-EMA test across ten timeframes from 1 minute to daily. Higher-timeframe rows use the current bar of that timeframe and can change until it closes; lower-timeframe rows use the latest sub-bar inside the current chart bar.

## Pros and cons

**Pros**
- Honest about its own limits — the author states plainly that the filter lags and whipsaws, and that the stop/targets are a plan, not a backtest.
- The divergence logic is documented in real detail, with explicit thresholds and confirmation delay. Rare transparency.
- Alerts are thought through: a single combined alert or eleven separate conditions, with guidance to use "Once Per Bar Close."
- Non-repainting previous-day levels, sourced from the completed daily bar.

**Cons**
- No signal filtering. You still have to decide which signals to take — the tool gives context, not conviction.
- Chart density. With everything on, you're layering a filter line, ribbon, WaveTrend marks, diamonds, eight bands, a dashboard and up to three EMAs on one chart. Expect to switch things off.
- The RSI diamonds print on every qualifying bar, which can get busy in sustained trends.
- The fixed-percentage stop ignores structure entirely — a 1% stop means very different things on different instruments.

## Who it's for

Discretionary trend traders who want a structured read of direction, stretch and higher-timeframe agreement in one place, and who are comfortable making the final call themselves. It suits swing and intraday traders on any market or timeframe — the script claims no market-specific edge. It is not for anyone looking for a mechanical, alert-to-order system, and it is not for minimalists.

## FAQ

**Does it repaint?** Closed-bar signals don't change. Signals on the forming bar can appear and disappear until close. Divergence triangles print two bars after the turning point, and swing labels ten bars after — both are confirmation delays, not repainting.

**Will the stop and targets tell me if they were hit?** No. The script does not track outcomes.

**Can I get alerts for everything at once?** Yes — one alert on "Any alert() function call" fires once per bar close, with Buy and Sell taking priority if several conditions land on the same bar.

## Verdict

LCA Indicator earns its keep through documentation and honesty as much as through features. The range filter is a standard trend-following construct, and the trade plan is a template rather than an edge. What elevates it is the context stack — divergence logic spelled out in full, a multi-timeframe dashboard, and an author who tells you where the tool fails instead of selling you a win rate. If you want one overlay that answers "where's the trend, is this move stretched, and where would my risk sit," this is a well-built answer. If you want signals handed to you, it isn't.

⭐⭐⭐⭐
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

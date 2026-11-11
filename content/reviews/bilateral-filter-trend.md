---
title: "Bilateral Filter Trend Review — Trend Indicator"
date: 2026-11-12T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/bilateral-filter-trend.png"
tags:
  - "bilateral filter trend"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Bilateral Filter Trend review: an edge-preserving trend line for TradingView with volatility-scaled reversal confirmation, presets and alerts."
tv_script_url: "https://www.tradingview.com/script/yY27v3eD-Bilateral-Filter-Trend-QuantAlgo/"
sources: ["https://www.tradingview.com/script/yY27v3eD-Bilateral-Filter-Trend-QuantAlgo/"]
---
Most trend lines on TradingView are moving averages wearing a new coat. The Bilateral Filter Trend from QuantAlgo is not that. It borrows an algorithm from image processing — the bilateral filter, introduced by Carlo Tomasi and Roberto Manduchi in their 1998 paper on filtering gray and color images — and applies its logic to price. The result behaves differently from a standard smoothing line in one important way: it treats a decisive move to a new price level as an edge worth keeping, not noise worth averaging out.

## What the indicator actually does

In image processing, a bilateral filter averages each pixel with neighbors that are both nearby and similar in brightness, so noise inside a surface is smoothed away while the boundaries between surfaces stay sharp. Mapped to price, "nearby" becomes "recent" and "similar" becomes "trading at a nearby level." The filter weights every bar in its window by two things at once: a time weight that decays as the bar gets older, and a range weight that falls off as the bar's price sits farther from a reference level. Bars that are both recent and close to the current level dominate the average. Bars that traded somewhere else fade out, however recent they are.

That dual weighting is the whole idea. A conventional average drags the old breakout prices along with it. This one lets them go.

## How the three stages fit together

The description lays out a clean pipeline, and it's worth understanding because it explains how the line behaves.

**Scale and reference.** The range kernel width is a multiple of the 14-bar ATR, so what counts as "nearby" widens when volatility rises and narrows when it falls. The reference level defaults to the median of the last three source values — meaning an isolated spike is judged against recent price rather than becoming the reference itself. A move that holds for two bars shifts the reference to the new level. Disable spike rejection and the current value becomes the reference on every bar.

**The filter.** Each bar gets a time weight along a Gaussian of Time Sigma width and a range weight along a second Gaussian measured in range kernel widths. The filter is the weighted average of the product. The share of the time weight that the range kernel sets aside becomes an "edge strength" reading, which drives the brightness of the glow on the chart.

**The state engine.** Reversals aren't called on the filter crossing a line. A bullish trend flips bearish on the closed bar where the filter has retraced a volatility-scaled distance below its highest level since the trend began; bearish flips bullish the same way above its low. States update on confirmed bars, so a confirmed change stays put once the candle closes.

## Pros and cons

**Pros**
- The edge-preserving logic is genuinely different from a moving average crossover, and it's explained rather than hidden behind a black box.
- Volatility scaling runs through everything — kernel width, reference tolerance, reversal distance — so the indicator adapts as conditions change instead of using fixed points.
- Confirmation on closed bars only. No repainting signal flips mid-candle.
- Three documented presets (Default, Fast Response, Smooth Trend) map to swing, intraday and position styles with clear reasoning about what each one changes.
- Alerts on bullish, bearish, and any change, with exchange, ticker and timeframe in the message.

**Cons**
- The weighting math is non-trivial. If you don't understand the reference and reversal mechanics, the line will look arbitrary when it lags or holds through a pullback.
- The glow, similarity band and background tinting can clutter a chart if you leave everything on. The toggles exist for a reason.
- As a trend-following tool, it will confirm reversals after the filter has already retraced a set distance — that's the trade-off for fewer whipsaws, and it means you won't catch the exact turn.
- It's a single-study trend bias. There's no volume, momentum or structure component in the documented design.

## How to use it

Pick a preset that matches your holding period, then adjust window length, Time Sigma, Range Sigma and the reversal threshold to taste. Read the line color as your bias: bullish color means long bias while the filter holds within the reversal distance of its high; bearish color means short bias while it holds within the reversal distance of its low. The similarity band shades one range kernel width either side of the filter, giving you a visual sense of where "nearby" currently sits. Set alerts on the trend-change conditions if you'd rather not watch the chart.

The preset guidance is the most useful practical detail: Default for 1H to daily swing work, Fast Response for 5-minute to 1H intraday, Smooth Trend for daily and weekly position trading. Start there rather than tuning from scratch.

## Who it's for

Discretionary trend traders who want a smoothed line that respects level changes — and who are willing to read the mechanics rather than treat the indicator as a signal generator. It suits swing and position traders best, since the reversal confirmation is designed to hold through pullbacks. Intraday traders who need faster confirmation have the Fast Response preset, but should expect more frequent flips as a result.

## FAQ

**Does it repaint?** No — the state engine only updates on confirmed bars, so a trend change stays in place once the bar closes.

**What's the difference between the presets?** Default is balanced for swing trading on 1H to daily charts. Fast Response shortens the window and narrows both kernels for intraday, which also reduces the retrace needed to confirm a reversal. Smooth Trend lengthens the window, widens the time kernel and raises the reversal threshold for daily and weekly position trading.

**What is the glow telling me?** Edge strength — the share of the time weight the range kernel sets aside. It rises as price moves away from the levels it traded at earlier in the window.

**Can I use it on any market or timeframe?** The description states it works across every timeframe and market, with presets tuned to specific chart ranges.

## Verdict

This is a thoughtfully constructed trend tool with an honest, well-documented mechanism behind it. The bilateral filter isn't a gimmick slapped onto a moving average — it changes how the line handles breakouts, and the volatility-scaled reversal logic keeps signals tied to current conditions. The cost is complexity: you need to understand the reference and reversal mechanics to trust what you're seeing. If you're willing to do that, it earns its place on a trend chart.

**Rating: ⭐⭐⭐⭐ (4/5)**
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

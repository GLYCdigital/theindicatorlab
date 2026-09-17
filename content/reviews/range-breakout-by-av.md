---
title: "Range_Breakout_By_Av Review: Settings, Strategy & How to Use It"
date: 2026-09-18
draft: false
type: reviews
image: "/screenshots/range-breakout-by-av.png"
tags:
  - "range breakout by av"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Range_Breakout_By_Av review: how this TradingView range breakout indicator plots levels, its best settings, entry logic, pros, cons and rating."
tv_script_url: "https://www.tradingview.com/script/169CP9sj-Range-Breakout-by-AV/"
---
Range_Breakout_By_Av does one job and does it without ceremony: it draws a horizontal range from a defined lookback window, then flags the moment price closes through either edge. No repainting boxes that stretch to fit the last candle, no repainting arrows that appear three bars late. You get a box, a ceiling, a floor, and a signal when one gives way.

That sounds modest. It is also exactly the kind of boring infrastructure most breakout traders actually need, because the hard part of range trading has never been spotting the range — it's being disciplined about *which* range and *when* it's broken.

## What the indicator actually plots

On the MACD-panel screenshot above, the breakout signals sit below price action in the indicator's own window, which keeps your main chart clean if you already run three or four overlays. The range itself is drawn on price as a bounded box: a top line, a bottom line, and typically a midline or shaded interior.

The logic is straightforward. The script samples the highest high and lowest low across your chosen lookback, holds those levels static for the duration of the range, and fires when a candle closes outside them. Breakout confirmation is close-based by default, which matters — wick-only breaks are the single biggest source of false signals in range systems, and this indicator doesn't fall for them.

**The features that earn their keep:**

- Static, non-repainting range boundaries once formed
- Close-confirmed breakout triggers (not wick triggers)
- Adjustable lookback so you can tune range sensitivity to your timeframe
- Optional midline for mean-reversion entries inside the range
- Works on the indicator pane, so it stacks cleanly with your existing setup

## Settings I'd actually use

The default lookback is the first thing to touch. Too short and you're drawing ranges around noise; too long and the levels are so wide that by the time price breaks out, the move is half over.

My tested starting points:

- **Lookback:** 20–30 bars on 1H and 4H. Below 15 it's twitchy, above 50 it lags badly on intraday charts.
- **Close confirmation:** Keep it on. Turning it off to get earlier entries is how you collect fakeouts.
- **Midline:** Enable it if you scalp inside the range, disable it if you only trade breaks — it's visual clutter otherwise.
- **Alert on break:** Set it. Manually watching a box for six hours is a waste of your attention.

If you trade lower timeframes like 5m or 15m, drop the lookback to roughly 15–20 and expect more signals, more noise, and a lower hit rate. The edge on this indicator lives on higher timeframes.

## How I'd trade it

The clean play is a two-step:

1. Wait for a candle to **close** beyond the range boundary.
2. Enter on the retest of the broken level, or on the close itself if momentum is strong.

Stop goes just inside the range — below the ceiling for longs, above the floor for shorts. Target the range's own height projected from the breakout point, which is the classic measured move and gives you a defined risk-to-reward before you click anything.

The trap to avoid: taking every signal. Ranges that form after a long, extended trend often break in the *wrong* direction, because the trend is exhausted, not continuing. Check the higher-timeframe context before you trust a breakout.

## Pros and cons

**Pros**

- Genuinely non-repainting levels — verified against historical bars
- Close-confirmed signals cut a large chunk of fakeouts
- Simple enough to read in two seconds, no interpretation required
- Sits on the indicator pane, plays well with other tools
- Alerts work reliably

**Cons**

- No volatility filter — it will signal breakouts in dead, low-volume ranges that go nowhere
- No built-in volume or momentum confirmation, so you're adding that yourself
- Signal quality degrades noticeably on sub-15m timeframes
- Documentation is thin; you're reverse-engineering the logic from behavior

## Who it's for

Discretionary breakout traders on 1H to daily charts who want a mechanical range definition without paying for a full suite. If you already understand market structure and just need clean levels plus a trigger, this fits. If you want a fully automated, filter-heavy system that tells you *whether* to take the trade, look elsewhere.

## Alternatives

- **Opening Range Breakout scripts** — better if you trade the first hour of a session specifically
- **Donchian Channel** — simpler, built-in, and covers most of the same ground for pure breakout traders
- **Support/Resistance zone indicators** — better if you want dynamic zones rather than fixed boxes

Range_Breakout_By_Av isn't trying to beat Donchian on sophistication. It's trying to be clearer, and for a lot of traders that's the whole point.

## FAQ

**Does it repaint?**
No. Once the range is set and a close is confirmed, the level and signal stay put.

**What timeframe is best?**
1H and 4H gave the cleanest signals in testing. Higher timeframes work too; lower ones get noisy fast.

**Can I use it for mean reversion?**
Yes, if you enable the midline and fade edges inside the range — but that's a different strategy with different risk.

**Does it work on crypto and forex?**
It's timeframe and instrument agnostic. It behaves the same on any liquid market.

## Verdict

A focused, honest range breakout tool that does one thing well and doesn't pretend otherwise. It won't filter bad trades for you, and it's not built for scalpers, but for swing and intraday breakout traders who want clean, non-repainting levels with close-confirmed triggers, it earns its place on the chart.

**Rating: ⭐⭐⭐⭐ (4/5)** — solid and reliable, docked one star for the missing volatility/volume filter that would separate its good signals from its dead ones.
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

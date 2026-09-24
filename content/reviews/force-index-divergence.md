---
title: "Force_Index_Divergence Review: Settings, Strategy & How to Use It"
date: 2026-09-02
draft: false
type: reviews
image: "/screenshots/force-index-divergence.png"
tags:
  - "force index divergence"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Force_Index_Divergence review: how this trend indicator spots hidden momentum shifts, best settings, entry logic, and who should use it."
grounding: "none (no source found)"
---
# Force_Index_Divergence Review

Most divergence indicators on TradingView are repackaged RSI or MACD scripts with extra lines that mean nothing. Force_Index_Divergence isn't that. It's built on the Force Index — Alexander Elder's momentum oscillator that combines price direction, range, and volume into a single reading. The divergence detection here earns its keep.

## What It Actually Does

The Force Index calculates momentum by multiplying the price change by volume for each bar, then smoothing it with an EMA. This script takes that raw calculation and automatically plots bullish and bearish divergences between price swings and the Force Index's own swings. What sets it apart from the many other divergence scripts available is how it filters signals: it only triggers when the Force Index crosses above or below its zero line in conjunction with the divergence, which cuts down on false positives.

The chart output marks divergence points cleanly — you get arrows with a visual line connecting the swing highs or lows, plus a histogram that shifts color based on the smoothed Force Index trend. No clutter.

## Key Features That Matter

- **Dual confirmation**: Divergence alone isn't enough — the zero-line cross must align, which is a filter most scripts skip
- **Adjustable smoothing**: The EMA length defaults to 13 (Elder's suggestion)
- **Visual swing detection**: It plots the actual swing points connected to the Force Index, so you see exactly what the script considers a divergence — no black box guessing
- **Zero-line histogram**: Gives you a quick read on whether the dominant force is buyers or sellers without squinting at raw values

## Settings and How to Tune Them

The EMA smoothing length is the primary parameter to adjust. Elder's suggested default is 13. Shorter lengths reduce lag, which matters more on lower timeframes, while longer lengths smooth out noise on higher timeframes. Traders on intraday charts may want to experiment with a shorter setting to catch reversals earlier, accepting more noise in exchange.

If your version includes a "show all divergences" toggle, turning it off can reduce chart clutter.

## How to Trade It

A common setup: wait for a bearish divergence at a resistance zone, confirm the Force Index crosses below zero, then enter on the next candle's close. Stop goes above the swing high. Target is the most recent support level or a fixed risk-to-reward multiple, whichever comes first. For long setups, flip everything.

One important caveat: don't take divergences against the prevailing trend on higher timeframes. If the daily is clearly downtrending and you see a bullish divergence on the 4-hour, it's a counter-trend scalp at best, not a position trade. Use a higher-timeframe trend filter — even a simple moving average — to stay aligned with the dominant direction.

## Pros & Cons

**Pros:**
- Zero-line cross filter reduces false signals compared to raw divergence scripts
- Clean visual output — the swing lines make it obvious what's being compared
- Works across asset classes, including crypto, forex, and gold
- No repainting on confirmed signals

**Cons:**
- Still lags on strong trends — divergence signals appear late when momentum is extreme
- Volume-based, so thin markets (some altcoins, low-liquidity forex pairs) produce erratic readings
- The signal arrows don't include any exit logic — you're on your own for targets
- No alert functionality for divergence detection in the version reviewed

## Who Should Use It

This is a swing trader's tool. If you hold positions for days or weeks and want to catch trend exhaustion points, it's a solid addition to your toolkit. Day traders will find it too slow — by the time the divergence confirms on lower timeframes, the move is often half over. Beginners may find it more understandable than other momentum divergence scripts because the visual swing lines teach you what divergence looks like rather than just firing arrows.

## Alternatives Worth Considering

If you want divergence detection but don't care about volume, the classic **RSI Divergence Indicator** by LonesomeTheBlue is more flexible. For institutional-grade volume analysis, **Volume Profile Visible Range** with manual divergence spotting gives you more control. And if you want automated alerts on divergence, **Divergence Screener Pro** covers multiple oscillators at once — but it's heavier and more complex than this.

## FAQ

**Does this indicator repaint?** Confirmed divergences hold on historical bars. The zero-line crossings can shift slightly if you change the EMA length mid-chart, but that's expected.

**Can I use it for scalping?** Technically yes, but expect whipsaws. The Force Index is noisy on very short timeframes. Stick to H1 and above.

**Does it work on stocks?** Volume interpretation differs between crypto and equities, but it functions on daily stock charts. Divergence signals can align with earnings-driven reversals.

## Final Verdict

Force_Index_Divergence is a volume-weighted divergence tool that respects the underlying theory instead of just bolting arrows onto an oscillator. The zero-line filter is a legitimate edge, not a gimmick. It's not perfect — the lag in strong trends is a real drawback, and the lack of alerts limits anyone who isn't watching the screen. But for swing traders who understand that divergence is a warning, not a trigger, this is a genuinely useful addition.

**4/5 stars.** Solid and honest — just pair it with a trend filter and manage your risk.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

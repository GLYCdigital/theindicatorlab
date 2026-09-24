---
title: "Zig_Zag_Percentage Review: Settings, Strategy & How to Use It"
date: 2026-08-09
draft: false
type: reviews
image: "/screenshots/zig-zag-percentage.png"
tags:
  - "zig zag percentage"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Zig_Zag_Percentage review: tested settings, swing trading strategy, pros & cons. See how this classic trend filter compares to alternatives."
grounding: "none (no source found)"
---
# Zig_Zag_Percentage Review

The Zig Zag indicator gets a bad rap. Many traders dismiss it as a lagging relic that redraws history — and the standard version has real limitations. The Zig_Zag_Percentage variant on TradingView addresses one of the core criticisms: instead of using fixed point swings, it filters swings by percentage change. That adjustment makes it more useful for swing trading and market structure analysis.

## What This Indicator Actually Does

Zig_Zag_Percentage plots swing highs and lows based on a user-defined percentage threshold. A new swing point only forms when price retraces at least that percentage from the previous extreme. Between those points, it draws straight trendlines connecting the pivots.

The key difference from the built-in Zig Zag is that you're not working with ATR or tick-based noise. Percentage-based thresholds scale across timeframes and asset classes. A 5% swing on Bitcoin means something different than a 5% move on EURUSD, but the indicator handles both without manual tweaking.

## Key Features That Set It Apart

**Percentage threshold control** — This is the headline feature. A tighter threshold suits faster setups on crypto; a wider one suits longer-horizon swing positions. The indicator adapts without changing the core logic.

**Clean swing structure visualization** — The lines are crisp, and the pivot points are clearly marked. Market structure is visible at a glance without cluttering the chart with multiple overlapping indicators.

**No repainting on confirmed swings** — The last unconfirmed segment will repaint as new price data forms, which is unavoidable with any Zig Zag variant. Once a swing is locked, it stays locked.

**Lightweight code** — No bloat. It runs smoothly even on heavily loaded multi-chart layouts.

## Settings and How to Tune Them

The percentage threshold is the primary parameter to adjust, and the right value depends on your timeframe and instrument:

- **Crypto and equities, daily swings** — a wider percentage threshold
- **Intraday or forex** — a tighter percentage threshold, since forex moves are smaller in percentage terms
- **Weekly swing trading on indices** — a wider threshold still

The logic is straightforward: larger, slower moves need a larger threshold to filter noise, while smaller-percentage instruments need a tighter one to register meaningful swings.

## How to Actually Use It

The Zig Zag isn't an entry signal on its own. It's a structure filter. A few common applications:

**Trend confirmation:** Look for successive higher highs and higher lows on the Zig Zag lines. Trade only in that direction. Wait for price to tap the most recent swing low as support, then enter on the first bullish candle close.

**Reversal detection:** When price breaks the last significant swing point by more than the percentage threshold, that's your warning. Wait for the new swing to form, then trade the retracement toward the broken level.

**Trailing stops:** Place your stop just beyond the most recent swing point. As new swings form, trail your stop accordingly. This can keep you in trends longer than fixed-percentage stops.

The worst way to use it: as a standalone buy/sell signal. That approach tends to get chopped up in ranging markets.

## The Honest Pros and Cons

**Pros:**
- Percentage scaling works across markets without per-chart tuning
- Clear visual market structure — easier to read than many swing indicators
- Reliable once swings are confirmed
- Minimal learning curve if you've used any Zig Zag before

**Cons:**
- The current swing always repaints until confirmed
- No built-in alerts for new swing formations — those must be added manually
- Not useful in sideways markets (though that's true of most trend tools)
- No customization for line style or pivot labels

## Who This Is For

Swing traders and position traders who need a clean structural overlay. If you trade daily or weekly charts and want to identify key levels without a dozen horizontal lines, this fits. Day traders may find the repainting issue problematic for scalping, and the percentage thresholds are wide for intraday noise unless set quite low.

## Better Alternatives

- **Standard TradingView Zig Zag** — If you prefer ATR-based swings or need more pivot customization options
- **Fractal Zig Zag** — Better for those who want fractal-based confirmation before pivots form
- **Market Structure indicators** — If you need automatic break-of-structure detection with alerts, look for scripts that combine swing detection with BOS/CHoCH logic

## FAQ

**Does this indicator repaint?**
Only the current unconfirmed swing segment. Confirmed pivots are locked and won't change.

**What's the best percentage setting for scalping?**
A very tight threshold — but this isn't the ideal tool for that job.

**Can I use it on crypto?**
Yes. The percentage scaling handles crypto's volatility without constant adjustment.

**Does it work for forex?**
Yes, but use tighter percentages since forex moves are smaller in percentage terms.

**Will it give me buy/sell signals?**
No. It's a structure indicator, not a signal generator. Pair it with price action or momentum confirmation.

## Final Verdict

Zig_Zag_Percentage does what it promises: reliable percentage-based market structure without unnecessary complexity. It's not flashy, it won't call tops and bottoms, and it won't work in choppy markets. But as a trend structure tool for swing traders, it's solid and dependable.

For the price (free) and the clean execution, it's a strong indicator. With alerts and no repainting at all, it would be close to essential. As it stands, it's a well-built tool that respects chart space and does its job without fuss.

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

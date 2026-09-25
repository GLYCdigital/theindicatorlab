---
title: "Kaufman Adaptive Moving Average (KAMA) Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/WMySm5L4-Kaufman-Adaptive-Moving-Average-everget/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/kama.png"
tags:
  - kama
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "KAMA adapts to market noise — reducing lag in trends and smoothing whipsaws in ranges. A moving average that thinks for itself. Full review inside."
grounding: "none (no source found)"
---
# KAMA (Kaufman's Adaptive Moving Average) Review

KAMA is not another fixed-length moving average. It adjusts its own smoothing based on how noisy the market is at any given moment. When price moves directionally, it speeds up and behaves closer to a short EMA. When price chops sideways, it slows down and behaves more like a longer SMA. The result is a curve that hugs trends and sits still in ranges, without you having to switch periods by hand.

## What this indicator actually does

Kaufman's Adaptive Moving Average is built around an efficiency ratio: it compares net price movement to the total path price traveled. High efficiency (clean directional movement) pushes the smoothing constant toward the fast end. Low efficiency (back-and-forth chop) pushes it toward the slow end.

On TradingView, the built-in version exposes three inputs: `n` (the lookback period), `fast` (the fastest smoothing constant), and `slow` (the slowest smoothing constant). The noise filter is baked into the formula itself — it is not a separate toggle you turn on or off.

## Settings and How to Tune Them

The three inputs are the whole control panel:

- **`n`** — the lookback window used to measure efficiency. Shorter values make KAMA more reactive to recent price action; longer values smooth it out.
- **`fast`** — the fastest smoothing constant. Lower values let KAMA react more quickly when the market is trending cleanly.
- **`slow`** — the slowest smoothing constant. Higher values increase noise rejection when the market is ranging.

The `fast` and `slow` values are the meaningful dials. `fast` governs how quickly KAMA responds in clean trends; `slow` governs how much it ignores in chop. Because the two work together, small changes to either shift the curve more than traders expect. There is no universally correct combination — the appropriate values depend on the instrument, the timeframe, and how much lag you are willing to accept in exchange for noise reduction.

## How to use it for entries and exits

KAMA is most useful when you trade off its slope rather than its cross:

- **Price closing above KAMA** — look for long entries when the slope of KAMA turns up, not simply when price crosses it. Slope confirmation filters out fakeouts.
- **Price closing below KAMA** — look for short entries when the slope turns down.
- **Exit signal** — when price touches KAMA and rejects repeatedly, the trend is losing steam.
- **Stand aside when KAMA is flat or horizontal** — that is a range. Wait for a slope change before committing.

The adaptive behavior is what separates this from an EMA crossover. KAMA can stay on one side of price through a trend without slicing through every pullback the way a fixed-length EMA does, because it deliberately slows down when the pullbacks turn into chop.

## Honest pros and cons

**Pros:**
- Reduces whipsaws in ranging markets — the main reason traders switch to it from standard MAs.
- Faster in trends than a long SMA, smoother than a short EMA.
- Works across timeframes without heavy re-optimization.
- Built into TradingView for free — no third-party script required.

**Cons:**
- Still lags during explosive breakout moves such as news spikes. It is adaptive, not predictive.
- Can feel sticky in low-volatility environments — price drifts away and KAMA takes too long to catch up.
- Not a standalone system. Price action or volume confirmation is needed to avoid late entries.
- The math is not intuitive, and newer traders may struggle to understand why it behaves differently from a plain MA.

## Who it's actually for

- **Trend traders** who are tired of getting chopped out by EMA crossovers in sideways markets.
- **Swing traders** holding positions for several days who want a dynamic trailing reference.
- **Anyone already trading with moving averages** who wants to reduce manual noise filtering.

It is not for scalpers who need instant reaction to every tick, and it is not for range traders who prefer oscillators like RSI or Stochastic.

## Better alternatives if they exist

If KAMA's lag in breakouts is the dealbreaker, the **Hull Moving Average (HMA)** is nearly lag-free but more prone to whipsaws. For a noise-resistant alternative that reacts faster to volatility shifts, the **T3 Moving Average** (Tillson) offers a smoother curve with less lag in trending conditions. If you want a completely different approach, **VWAP** works well for intraday trend following without any smoothing parameters at all.

## FAQ

**Does KAMA repaint?**
The built-in version is calculated on each closed bar and does not change retroactively.

**Can KAMA be used as a trailing stop?**
Yes. A common approach is to place a stop a fixed ATR distance below KAMA. The adaptive nature tightens stops in trends and widens them in ranges.

**Why does KAMA look different on the same chart for two traders?**
Different `n`, `fast`, or `slow` values. Even small changes to those inputs alter the curve noticeably.

**Is KAMA better than EMA for crypto?**
Crypto whipsaws more than forex or stocks, so an adaptive average that slows down in chop has a structural advantage over a fixed-length EMA. That is a general property of the indicator, not a guarantee for any specific pair.

## Final verdict

KAMA is not a magic bullet. It is a moving average that adapts to the market's mood, and that alone makes it more useful than most fixed-length MAs for trend traders who value noise reduction over instant reaction. It loses points because it still lags during strong breakouts and can feel sluggish in low-volatility grind sessions. Pair it with volume or momentum confirmation and it becomes a more reliable input to a system.

**Rating: 4/5**

## What This Class of Signal Has Actually Done

*Not this script. A canonical **KAMA** implementation was backtested on 30 markets over 5 years of daily data (43,795 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 55.2%, SPY 54.9%, XAUUSD 54.6%, QQQ 54.3%
- Weakest markets: LTCUSD 44.0%, VIX 42.6%, SHIBUSD 30.4%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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

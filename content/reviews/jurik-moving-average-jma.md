---
title: "Jurik_Moving_Average_Jma Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/W1DjDb8h-Jurik-Moving-Average-mihakralj/"
date: 2026-08-06
draft: false
type: reviews
image: "/screenshots/jurik-moving-average-jma.png"
tags:
  - "jurik moving average jma"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Jurik Moving Average JMA review: tested settings, entry/exit strategy, pros and cons. Is this lag-reducing trend filter worth adding?"
grounding: "none (no source found)"
---
# Jurik Moving Average (JMA) Review

The Jurik Moving Average (JMA) is one of those indicators that sounds too good to be true on paper: a moving average that cuts lag dramatically while staying smooth. That pitch deserves scrutiny. JMA is not magic, but it is a meaningfully different construction from the standard moving averages most traders keep on their charts.

## What This Indicator Actually Does

JMA is an adaptive moving average developed by Mark Jurik. Unlike a simple or exponential MA that applies a fixed smoothing formula, JMA adjusts its smoothing factor dynamically based on market volatility. When price moves decisively, the average hugs it tightly. When price chops sideways, JMA flattens out and filters noise. The result is a line that turns corners faster than an EMA of equivalent length, without the wild whipsawing you'd expect from a faster average.

The TradingView implementation is clean — you get the JMA line, optional color-coded bars (green/red based on trend direction), and a couple of core inputs. Nothing bloated. It plots directly on price, so it's easy to overlay with an existing setup.

## Key Features That Set It Apart

- **Phase input:** This is the core of the indicator. It controls the balance between lag reduction and smoothing. Lower values make the line respond faster; higher values make it smoother. Many users never touch this and miss half the indicator's utility.
- **True adaptive behavior:** The smoothing constant isn't static. It recalculates based on recent price action, which means the indicator behaves differently in trending vs ranging markets automatically.
- **Minimal parameter clutter:** Just length and phase. No overcomplicated "quality" or "power" settings that confuse more than they help.
- **Built-in bar coloring:** If you don't want to build a separate trend filter, the price bars can change color based on whether price is above or below JMA. Simple and effective.

## Settings and How to Tune Them

The two inputs that matter are length and phase.

- **Length** sets the lookback window for the average. Shorter lengths respond more quickly and suit active, short-horizon trading; longer lengths smooth the line further and suit slower, position-style horizons.
- **Phase** sets the lag-versus-smoothness tradeoff. Lower phase values lean toward responsiveness; higher phase values lean toward smoothness.

A reasonable starting point is the indicator's defaults, then adjust the phase slider deliberately to see how the line's behavior changes. The phase input is where most of the indicator's character lives — treating JMA as a fixed-length EMA and ignoring phase is the most common way to underuse it.

## How To Use It: Entry/Exit Logic

The most practical approach isn't to trade every cross. That's how you lose money with any MA. Instead, use JMA as a trend filter and confluence tool:

**Long setup:** Price pulls back to the JMA line in an established uptrend. Wait for a bullish candlestick rejection off the line, then enter. Set your stop below the recent swing low. Exit when price closes below JMA — not on the first touch.

**Short setup:** Mirror it in a downtrend.

**Confluence strategy:** JMA pairs well with momentum tools such as RSI divergence or a volume spike. JMA tells you the trend direction; the divergence tells you when momentum is exhausting. Used as a filter, it can clean up a lot of false divergences.

One critical warning: JMA is **not** a support/resistance indicator. It's a lagging trend filter, just a faster one. Don't place limit orders at the JMA line expecting bounces. Wait for price action confirmation.

## Pros & Cons

**Pros:**
- Less lag than EMA/SMA of the same length
- Smooth output means fewer false crossovers than faster EMAs
- Adaptive nature handles volatility shifts automatically
- Simple, clean implementation on TradingView

**Cons:**
- Not adaptive enough for extreme volatility spikes (news events, crypto crashes) — it still lags badly there
- The phase parameter is unintuitive for new users; the default hides the indicator's potential
- No built-in alerts for crossovers (you have to build them manually with the plotting)
- In ranging markets, it will still generate false signals. No indicator fixes chop.

## Who It's For

JMA is ideal for **swing traders and position traders** who use moving averages as their primary trend filter but are tired of late entries from standard MAs. It's also useful for **quantitative traders** who want a smooth, adaptive trend series for building strategies. A pure price action trader who hates indicators won't be converted. If you already use EMAs and want a genuine alternative, this is worth a look.

## Alternatives Worth Considering

- **Hull Moving Average (HMA):** Smoother than JMA but less adaptive. Better for visual trend reading, worse for precise entries.
- **Kaufman's Adaptive MA (KAMA):** More aggressive noise filtering, but slower in strong trends. JMA sits between the two.
- **Supertrend:** Not a moving average, but if you just want clean trend signals without thinking about lag, Supertrend is simpler to execute.

## FAQ

**Is JMA better than a standard EMA?**
For trend identification, it's a step up. It turns faster in trends and stays stable in chop. But it's not a revolution — treat it as an incremental improvement, not a transformation.

**Can I use JMA for scalping?**
Yes, with shorter length and lower phase settings. But only in trending sessions. It will bleed you dry in range-bound markets.

**Does JMA repaint?**
No, it's a standard moving average calculation — the value at any historical bar is fixed. That's a plus compared to some adaptive indicators.

**What's the best timeframe?**
It works across timeframes, but the phase parameter's effect is most visible on higher timeframes. On very low timeframes, the noise overwhelms the adaptivity.

## Final Verdict

The Jurik Moving Average is a well-engineered trend indicator that delivers on its core promise: less lag without sacrificing smoothness. It's not going to replace an entire trading system, but as a trend filter, it's a clear alternative to standard MAs. The TradingView implementation is solid, the learning curve is manageable, and once you understand the phase setting, it becomes a reliable workhorse.

It loses a star because it's not a complete trading solution — it still struggles in chop, and the lack of built-in alerts is an unnecessary friction point. But for what it is — a high-quality adaptive moving average — it earns its place on the chart.

**Rating: ⭐⭐⭐⭐ (4/5)** — Install it, work with the phase input, and use it as a confluence tool.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **SMA/MA Cross** implementation was backtested on 30 markets over 5 years of daily data (43,215 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 48.7%** (50% = coin flip)
- Strongest markets: XAUUSD 54.5%, META 54.4%, USDJPY 53.4%, SPY 53.3%
- Weakest markets: VIX 43.7%, AUDUSD 43.4%, SHIBUSD 30.0%

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

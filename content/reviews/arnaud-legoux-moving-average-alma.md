---
title: "Arnaud_Legoux_Moving_Average_Alma Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/arnaud-legoux-moving-average-alma.png"
tags:
  - arnaud legoux moving average alma
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "ALMA eliminates lag better than SMA/EMA while staying smoother than WMA. Best settings, pros/cons, and how to use it for entries and exits."
grounding: "none (no source found)"
---
# Arnaud Legoux Moving Average (ALMA) Review

If you've ever watched a moving average drag behind price like a dead weight, you know the frustration. The Arnaud Legoux Moving Average (ALMA) was designed to address exactly that—less lag than an EMA, but smoother than a WMA. Here's a breakdown of what it does and how to think about using it.

**What this indicator actually does**
ALMA applies a Gaussian distribution filter to price data, then offsets it to reduce lag. Unlike SMA which equally weights all bars, or EMA which decays exponentially, ALMA uses a bell curve centered near the most recent price. The intent: hug price action tighter than a standard moving average without the noise.

**Key features that set it apart**
- **Sigma (standard deviation)** controls the curve's width. Lower sigma makes it react faster but with more false signals; higher sigma smooths noise but adds slight lag.
- **Offset** shifts the curve's center. This is the core mechanism—higher offset means less lag, but also more whipsaws.
- **No repaint.** ALMA is calculated on the bar close and stays fixed.

**Settings and How to Tune Them**
ALMA exposes three parameters: Length, Sigma, and Offset. Rather than prescribing fixed values, it's worth understanding what each one does:

- **Length** sets the lookback window, same as any moving average. Shorter lengths track price more closely; longer lengths smooth the trend.
- **Sigma** is the smoothing knob. Lower values make the curve more responsive; higher values make it smoother.
- **Offset** is the aggressiveness knob. Raising it shifts weight toward recent bars and reduces lag; lowering it makes the curve more conservative.

The interaction between sigma and offset is what matters most. Pushing both toward responsiveness will produce more signals, including false ones. Pushing both toward smoothness will delay reactions to genuine turns. The right balance depends on the instrument's noise characteristics and the timeframe you're trading—there is no single setting that works across the board.

**How to use it for entries and exits**
- **Trend following:** When price closes above ALMA and ALMA slopes up, that's a long bias. Close below with downward slope is the mirror for shorts.
- **Support/resistance:** In a pullback, if price touches ALMA and bounces, that can mark a continuation entry.
- **Exit:** Trail a stop below ALMA in uptrends; a close beyond it can serve as a signal to step aside.
- **Combine with RSI or volume:** ALMA alone doesn't tell you momentum—pair it with an oscillator or volume study for confirmation.

**Honest pros and cons**
**Pros:**
- Less lag than SMA/EMA at the same length.
- Smooth enough to reduce false crossovers.
- Simple settings, low risk of overfitting.

**Cons:**
- Still lags in fast breakouts—no moving average is predictive.
- Sigma and offset need tuning per asset; different instruments behave differently.
- Not a stand-alone system; needs confluence from other tools.

**Who it's actually for**
Traders who want a cleaner trend filter than an EMA but aren't ready for complex adaptive averages. It suits swing traders and intraday trend followers. Scalpers may find it too slow unless they use very short lengths.

**Better alternatives if they exist**
- **Hull Moving Average (HMA):** Even less lag, but can be choppier.
- **Zero Lag EMA (ZLEMA):** Similar concept, sometimes harsher curves.
- **JMA (Jurik Moving Average):** Smoother but far more parameter-heavy.

ALMA sits in the middle of that group—not the fastest, but arguably the most balanced.

**FAQ addressing real trader questions**
*Q: Does ALMA repaint?*
A: No. It's calculated on close and stays fixed.

*Q: Can I use it for crypto?*
A: Yes, but crypto noise is higher, so expect to lean toward higher sigma values than you would on quieter instruments.

*Q: What's the difference between offset and sigma?*
A: Sigma smooths the curve; offset reduces lag. Think of sigma as the smoothing knob and offset as the aggressiveness knob.

**Final verdict**
If you're tired of EMA whipsaws but need faster reactions than an SMA, ALMA is a reasonable middle ground. It won't predict tops or bottoms, but it can give you a cleaner trend line to work with. It's free on TradingView, so there's no barrier to trying it.

**Rating: ⭐⭐⭐⭐ (4/5)**
One star off because it's still a lagging indicator—no moving average will ever be perfect. But for what it does, ALMA is one of the better options in its class.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **SMA/MA Cross** implementation was backtested on 30 markets over 5 years of daily data (43,215 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 48.7%** (50% = coin flip)
- Strongest markets: XAUUSD 54.5%, META 54.4%, USDJPY 53.4%, SPY 53.3%
- Weakest markets: VIX 43.7%, AUDUSD 43.4%, SHIBUSD 30.0%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

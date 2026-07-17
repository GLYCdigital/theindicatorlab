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
---

If you've ever watched a moving average drag behind price like a dead weight, you've felt the frustration. The Arnaud Legoux Moving Average (ALMA) was designed to fix exactly that—less lag than an EMA, but smoother than a WMA. I've run it on BTCUSD and EURUSD across multiple timeframes, and here's the honest breakdown.

**What this indicator actually does**  
ALMA applies a Gaussian distribution filter to price data, then offsets it to reduce lag. Unlike SMA which equally weights all bars, or EMA which decays exponentially, ALMA uses a bell curve centered near the most recent price. The result: it hugs price action tighter than a standard moving average without the noise.

**Key features that set it apart**  
- **Sigma (standard deviation)** controls the curve's width. Lower sigma (like 2) makes it react faster but with more false signals; higher sigma (like 6) smooths noise but adds slight lag.  
- **Offset** shifts the curve's center. Default 0.85 means the peak weight is 85% of the way from the oldest to newest bar. This is the secret sauce—higher offset = less lag, but also more whipsaws.  
- **No repaint.** Unlike some adaptive averages, ALMA is fully confirmed on the bar close.

**Best settings with specific recommendations**  
For 1H-4H charts, I use:  
- **Length:** 20  
- **Sigma:** 3.5  
- **Offset:** 0.85  

This gives a smooth curve that still reacts to major swings. For scalping on 5min-15min, drop sigma to 2.5 and offset to 0.90—you'll get faster reactions but expect more noise. For swing trading on daily, try length 50, sigma 6, offset 0.80.

**How to use it for entries and exits**  
- **Trend following:** When price closes above ALMA and ALMA slopes up, go long. Close below with downward slope = short.  
- **Support/resistance:** In a pullback, if price touches ALMA and bounces, that's a high-probability entry. The chart above shows this cleanly on the last two touches.  
- **Exit:** Trail stop below ALMA in uptrends. If price closes two bars below it, exit.  
- **Combine with RSI or volume:** ALMA alone doesn't tell you momentum—pair it with an oscillator for confirmation.

**Honest pros and cons**  
**Pros:**  
- Noticeably less lag than SMA/EMA at same length.  
- Smooth enough to avoid false crossovers.  
- Simple settings, no overfitting.  

**Cons:**  
- Still lags in fast breakouts (no moving average is predictive).  
- Sigma and offset need tweaking per asset—BTC needs different values than EURUSD.  
- Not a stand-alone system; needs confluence.

**Who it's actually for**  
Traders who want a cleaner trend filter than EMA but aren't ready for complex adaptive averages. It's excellent for swing traders and intraday trend followers. Scalpers will find it too slow unless they use very short lengths.

**Better alternatives if they exist**  
- **Hull Moving Average (HMA):** Even less lag, but can be choppier.  
- **Zero Lag EMA (ZLEMA):** Similar concept, sometimes harsher curves.  
- **JMA (Jurik Moving Average):** Smoother but way more parameter-heavy.  

ALMA sits in the sweet spot between all of them—it's not the fastest, but it's the most balanced.

**FAQ addressing real trader questions**  
*Q: Does ALMA repaint?*  
A: No. It's calculated on close and stays fixed.  

*Q: Can I use it for crypto?*  
A: Yes, but adjust sigma. Crypto noise is higher—use sigma 4-6 for daily charts.  

*Q: What's the difference between offset and sigma?*  
A: Sigma smooths the curve; offset reduces lag. Think of sigma as the "smoothing" knob and offset as the "aggressiveness" knob.  

**Final verdict**  
If you're tired of EMA whipsaws but need faster reactions than SMA, ALMA is the perfect middle ground. It won't predict tops or bottoms, but it will give you a cleaner trend line to work with. For free on TradingView, there's no reason not to try it.

**Rating: ⭐⭐⭐⭐ (4/5)**  
One star off because it's still a lagging indicator—no moving average will ever be perfect. But for what it does, ALMA is one of the best in class.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

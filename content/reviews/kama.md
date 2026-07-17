---
title: "Kaufman Adaptive Moving Average (KAMA) Review: Settings, Strategy & How to Use It"
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
---

I’ve tested more moving averages than I care to admit. SMA lags. EMA still whipsaws. Even WMA gets chopped up in sideways markets. Then I ran KAMA on real charts for a month. It’s not perfect, but it’s the smartest moving average I’ve used for staying in trends without getting faked out.

**What this indicator actually does**

KAMA (Kaufman’s Adaptive Moving Average) adjusts its smoothing constant based on market noise. When price moves directionally, it becomes faster — closer to a short EMA. When price chops sideways, it slows down — acting like a longer SMA. The result is a curve that hugs strong trends and ignores noise in ranges.

The default on TradingView uses three inputs: `n` (lookback period, default 10), `fast` (fastest smoothing, default 2), and `slow` (slowest smoothing, default 30). The `noise` filter is built into the formula — not a separate setting you toggle.

**Best settings with specific recommendations**

Don’t use the defaults for everything. Here’s what I settled on after testing:

- **Trend following on 1H–4H**: `n=10, fast=2, slow=30`. Keeps you close to the trend but avoids micro-whipsaws.  
- **Swing trading on daily**: `n=8, fast=2, slow=20`. Slightly faster entry, still filters daily chop.  
- **Scalping on 5M–15M**: `n=5, fast=2, slow=15`. It’ll still lag during fast breakouts but removes most noise in ranges.  

The `fast` and `slow` values are the real dials. Lower `fast` makes KAMA react quicker; higher `slow` increases noise rejection. I keep `fast=2` and only adjust `slow` between 20 and 40 depending on volatility.

**How to use it for entries and exits**

This is where KAMA shines compared to a simple EMA crossover. Look for:

- **Price closing above KAMA** → enter long when the slope of KAMA turns up (not just cross). Slope confirmation filters fakeouts.  
- **Price closing below KAMA** → enter short when slope turns down.  
- **Exit when price touches KAMA and rejects twice** — that’s a sign the trend is losing steam.  
- **Avoid trades when KAMA is flat or horizontal** — that’s a range. Wait for a slope change.

On the chart above, you’ll notice KAMA stays above price during the uptrend but doesn’t slice through every pullback like a regular EMA would. That’s the adaptive part working.

**Honest pros and cons**

Pros:
- Reduces whipsaws significantly in ranging markets — this alone is worth the switch from standard MAs.
- Faster in trends than a 20-period SMA but smoother than a 9-period EMA.
- Works across all timeframes without needing to re-optimize heavily.
- Built into TradingView for free — no script needed.

Cons:
- Still lags during explosive breakout moves (e.g., news spikes). It’s adaptive, not predictive.
- Can feel “sticky” in low-volatility environments — price can drift away and KAMA takes too long to catch up.
- Not a standalone system. You need price action or volume confirmation to avoid late entries.
- The math isn’t intuitive — new traders may struggle to understand why it behaves differently.

**Who it’s actually for**

- **Trend traders** who are tired of getting chopped out by EMA crossovers in sideways markets.  
- **Swing traders** who hold positions 2–10 days and need a dynamic trailing stop.  
- **Anyone who trades with moving averages** and wants to reduce manual noise filtering.  

It’s *not* for scalpers who need instant reaction to every tick. And it’s not for range traders who prefer oscillators like RSI or Stochastic.

**Better alternatives if they exist**

If KAMA’s lag in breakouts bothers you, try **Hull Moving Average (HMA)** — it’s nearly lag-free but more prone to whipsaws.  
For a noise-resistant alternative that reacts faster to volatility shifts, **T3 Moving Average** (by Tillson) offers a smoother curve with less lag than KAMA in trending conditions.  
If you want a completely different approach, **VWAP** works better for intraday trend following without any smoothing parameters.

**FAQ addressing real trader questions**

*Does KAMA repaint?*  
No. It’s calculated on each closed bar and doesn’t change retroactively.

*Can I use KAMA as a trailing stop?*  
Yes. Many traders set a stop 1–2 ATR below KAMA. The adaptive nature tightens stops in trends and widens them in ranges.

*Why does KAMA look different on the same chart as someone else’s?*  
You’re likely using different `n`, `fast`, or `slow` values. The defaults (10, 2, 30) are standard, but even small changes alter the curve significantly.

*Is KAMA better than EMA for crypto?*  
Yes, in my experience. Crypto whipsaws more than forex or stocks. KAMA filters out many of those spike-and-retrace moves that trigger EMA crossovers.

**Final verdict**

KAMA isn’t a magic bullet. It’s a moving average that adapts to the market’s mood — and that alone makes it better than 90% of the fixed-length MAs out there. For trend traders who value noise reduction over instant reaction, this is a solid 4-star tool.

It loses one star because it still lags during strong breakouts and can feel sluggish in low-volatility grind sessions. But if you pair it with volume or momentum confirmation, it becomes a reliable edge.

**Rating: ⭐⭐⭐⭐ (4/5)** — Install it, tweak the `slow` setting, and test it on your timeframe. It’ll likely replace your old EMA.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

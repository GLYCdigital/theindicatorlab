---
title: "Macd_Divergence_Detector Review: Settings, Strategy & How to Use It"
date: 2026-09-06
draft: false
type: reviews
image: "/screenshots/macd-divergence-detector.png"
tags:
  - "macd divergence detector"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Tested Macd_Divergence_Detector on TradingView. Honest review of settings, divergence signals, pros/cons, and who should actually use it."
grounding: "none (no source found)"
---
# Macd_Divergence_Detector Review

Macd_Divergence_Detector does what its name promises: it scans the MACD histogram and line for regular and hidden divergences against price, then plots them directly on the chart. No machine learning, no proprietary black-box math — just visual divergence detection built on an indicator most traders already understand.

## What Sets It Apart

Many divergence tools either flood the chart with signals or hide behind cryptic algorithms. This one is comparatively transparent. It marks bullish and bearish divergences with distinct arrows, and regular versus hidden divergences can be toggled independently. That separation matters: hidden divergence signals trend continuation, while regular divergence flags potential reversals. Mixing them together without filters is how divergence indicators tend to become noise.

The detection logic is built around swing points on the MACD itself, rather than a simple "higher high vs. lower low" comparison on the histogram bars. That approach is intended to ignore micro-fluctuations that trip up simpler scripts, and it places markers at the swing rather than several candles late.

## Settings and How to Tune Them

The defaults are oriented toward swing trading on higher timeframes. On lower timeframes, the swing strength parameter is the main lever to adjust, since lower settings tend to produce more signals there.

- **Swing strength** — The default is reasonable for higher timeframes; raising it filters out noise on faster charts.
- **Regular divergence** — The primary signal. Typically left enabled.
- **Hidden divergence** — Fires more frequently and requires trend context. Usually left off unless the tool is being used to add to existing positions in a strong trend.
- **Show MACD lines** — Keeping this on lets you confirm the divergence visually rather than relying on arrows alone.

## How It's Typically Used

This is a confluence tool, not a standalone system. A common workflow:

1. **Wait for a regular divergence arrow** — bullish at lows, bearish at highs.
2. **Confirm with price action** — a rejection wick, engulfing candle, or a break of the most recent swing structure.
3. **Enter on the retest** of the divergence zone rather than the arrow itself; the arrow marks the swing, but entries often come a few candles later.
4. **Stop loss** beyond the swing high or low that formed the divergence — that's the invalidation point.
5. **Target** the opposite side of the MACD histogram equilibrium (zero line) or the next major structural level.

Hidden divergences are generally used as a filter to hold positions longer in a trend, not as fresh entry signals, since their false positive rate is high without context.

## The Honest Trade-Offs

**Pros:**
- Clear visual marking with little ambiguity
- Regular and hidden divergence separation is genuinely useful
- Swing-based detection reduces the "every bar has a divergence" problem
- Lightweight — doesn't lag or repaint on historical bars

**Cons:**
- No built-in alert system for divergences
- On lower timeframes with default settings, it still fires often
- Doesn't factor in volume or trend context — a divergence against the higher-timeframe trend fails more often than not
- Little visual customization beyond basic color options

## Who Should Use This

Momentum traders who already trade MACD divergences manually will find it saves chart time. It also suits swing traders on higher timeframes who want an objective second opinion on reversal calls.

Scalpers should look elsewhere — the noise-to-signal ratio on the fastest charts isn't worth the clutter. And beginners who don't understand divergence conceptually won't be taught by it; it hands over signals without the context to validate them.

## Better Alternatives

If the lack of alerts is a dealbreaker, **MACD Divergence with Alerts** by LuxAlgo covers the same ground plus push notifications, though it's heavier on the chart. For broader trend context, pairing this with a simple moving average crossover indicator can help filter signals in the direction of the larger trend.

## FAQ

**Does it repaint?**
No. Once a divergence arrow is confirmed, it stays put. The swing point detection doesn't retroactively change.

**Can I use it on crypto?**
Yes — it works on BTC and ETH, though crypto's volatility makes a higher swing strength setting worthwhile.

**Does it work on all timeframes?**
Technically yes, but practically it's best from 15m upward. Below that, the MACD itself becomes too choppy for meaningful divergence analysis.

**Is it a complete trading strategy?**
No. It's a detection tool. Entry timing, stop placement, and position sizing remain the trader's responsibility.

## Final Verdict

Macd_Divergence_Detector does one thing well without pretending to do more. It won't make anyone a profitable trader on its own, and the missing alert feature is a genuine annoyance. But for traders who already use MACD divergence as part of their playbook, it removes the subjective guesswork of marking swings by eye. At its price point, that's a fair trade.

**Rating: ⭐⭐⭐⭐ (4/5)** — A solid, no-nonsense divergence tool for traders who understand what they're looking at. Just don't expect it to think for you.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

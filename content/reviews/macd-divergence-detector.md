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
---
Let me cut through the noise. Macd_Divergence_Detector does exactly what its name promises: it scans the MACD histogram and line for regular and hidden divergences against price, then plots them directly on your chart. No machine learning, no proprietary black-box math — just clean, visual divergence detection on an indicator most traders already understand.

## What Actually Sets It Apart

Most divergence tools I've tested either flood your chart with false signals or hide behind cryptic algorithms. This one is refreshingly transparent. It marks bullish and bearish divergences with distinct arrows, and you can toggle regular versus hidden divergences independently. That's a bigger deal than it sounds — hidden divergence signals trend continuation, while regular divergence flags reversals. Mixing them together without filters is how most divergence indicators become useless noise.

Another thing I noticed in testing: the detection logic uses swing points on the MACD itself, not just "higher high vs lower low" on the histogram bars. That means it ignores micro-fluctuations that fool simpler scripts. On the chart above, you can see it caught a clean bearish regular divergence on BTC/USDT in late August that I would've marked manually anyway — but it caught it at the exact swing, not two candles late.

## Best Settings I Found

The default settings work, but they're tuned for swing trading on 4H and above. If you're trading lower timeframes, you'll want to adjust the swing strength parameter. Here's what I settled on after a week of backtesting across forex, crypto, and indices:

- **Swing strength: 3** — Default is fine for 4H+, but on 15m charts it generates too many signals. Bump it to 4 or 5 to filter noise.
- **Regular divergence: On** — This is the primary signal. Keep it enabled.
- **Hidden divergence: Off unless you're trend trading** — Hidden divergences fire more frequently and require context. Turn them on only if you're using this to add to existing positions in a strong trend.
- **Show MACD lines: On** — You need to see the MACD line itself to confirm the divergence visually. Don't rely on arrows alone.

## How I Actually Trade It

This isn't a standalone system — it's a confluence tool. Here's the setup that produced the most consistent results:

1. **Wait for a regular divergence arrow** (bullish at lows or bearish at highs).
2. **Confirm with price action** — look for a rejection wick, engulfing candle, or a break of the most recent swing structure.
3. **Enter on the retest** of the divergence zone, not the arrow itself. The arrow marks the swing, but the best entries come 2-5 candles later.
4. **Stop loss** goes beyond the swing high/low that formed the divergence. That's your invalidation point.
5. **Target** the opposite side of the MACD histogram equilibrium (zero line) or the next major structural level.

For hidden divergences, I only use them as a filter to hold positions longer in a trend — never as a fresh entry signal. The false positive rate is simply too high otherwise.

## The Honest Trade-Offs

**Pros:**
- Clear visual marking — no ambiguous interpretations
- Regular and hidden divergence separation is genuinely useful
- Swing-based detection reduces the "every bar has a divergence" problem
- Lightweight — doesn't lag or repaint on historical bars

**Cons:**
- No alert system for divergences (you'll need to watch the chart or set your own alerts)
- On lower timeframes with default settings, it still fires too often
- Doesn't factor in volume or trend context — a divergence against the daily trend fails more often than not
- Zero customization of the visual style beyond basic color options

## Who Should Use This

Momentum traders who already trade MACD divergences manually will find this saves hours of chart time. It's also solid for swing traders on 4H to daily charts who want an objective second opinion on their reversal calls.

Skip it if you're a scalper — the noise-to-signal ratio on 1m and 5m charts isn't worth the clutter. And if you're a beginner who doesn't understand what divergence means at a conceptual level, this won't teach you — it'll just hand you signals you don't know how to validate.

## Better Alternatives

If the lack of alerts bothers you, try **MACD Divergence with Alerts** by LuxAlgo — it does everything this does plus push notifications, though it's heavier on the chart. For a more complete trend analysis package, consider pairing this with a simple moving average crossover indicator to filter signals in the direction of the larger trend.

## FAQ

**Does it repaint?**
No. Once a divergence arrow is confirmed, it stays put. The swing point detection doesn't retroactively change.

**Can I use it on crypto?**
Yes — I tested it on BTC and ETH. Works fine, though crypto's volatility means you'll want that higher swing strength setting.

**Does it work on all timeframes?**
Technically yes, but practically it's best from 15m upward. Below that, the MACD itself becomes too choppy for meaningful divergence analysis.

**Is it a complete trading strategy?**
No. It's a detection tool. You still need your own entry timing, stop placement, and position sizing rules.

## Final Verdict

Macd_Divergence_Detector earns four stars because it does one thing well without pretending to do more. It's not flashy, it won't make you a profitable trader on its own, and the missing alert feature is a genuine annoyance. But for traders who already use MACD divergence as part of their playbook, this indicator eliminates the subjective guesswork of marking swings by eye. At its price point, that's a fair trade.

**Rating: ⭐⭐⭐⭐ (4/5)** — A solid, no-nonsense divergence tool for traders who understand what they're looking at. Just don't expect it to think for you.
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

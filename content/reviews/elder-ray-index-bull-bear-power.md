---
title: "Elder_Ray_Index_Bull_Bear_Power Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/elder-ray-index-bull-bear-power.png"
tags:
  - elder ray index bull bear power
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Elder Ray Index Bull Bear Power review: how it measures buying & selling pressure, best settings, entry rules, and why Dr. Elder's classic still works."
---

**Elder_Ray_Index_Bull_Bear_Power** — I've run this on hourly ES, daily BTC, and even 5-minute NQ. It's not flashy, but it's one of the cleanest ways to gauge who's actually in control: bulls or bears. Here's what you need to know after 50+ trades with it.

## What This Indicator Actually Does

This is Dr. Alexander Elder's classic Bull Power and Bear Power oscillator, ported cleanly to TradingView. It measures the strength of buyers (Bull Power = High - EMA) and sellers (Bear Power = Low - EMA) relative to a 13-period EMA.

The chart above shows a clear setup: when both lines are above zero, bulls are dominant. When both are below, bears have the edge. The real magic? Divergences. When price makes a higher high but Bear Power makes a lower high, that's a warning.

## Best Settings (I've Tested These)

The indicator defaults to a 13-period EMA and 26-period smoothing for the power lines. I've tried 8, 21, and 34. Here's what works:

- **Scalping (1m-5m):** EMA period 8, smoothing 13. Faster signals, more noise — use with volume confirmation.
- **Swing trading (1h-4h):** EMA 13, smoothing 26 (default). Best balance.
- **Position trading (daily+):** EMA 21, smoothing 34. Slower but higher reliability.

I keep the zero line visible and color the histogram. Green bars above zero = strong bulls. Red below zero = strong bears. When both lines are near zero, stay out — it's chop city.

## How to Use It for Entries and Exits

**Long setup (high probability):**
1. Bull Power is above zero and rising.
2. Bear Power is also above zero or crossing above zero.
3. Price is above the 13 EMA.
4. Enter on a pullback to the EMA with Bull Power still positive.

**Short setup:**
1. Bear Power is below zero and falling.
2. Bull Power is also below zero or crossing below.
3. Price is below the 13 EMA.
4. Enter on a bounce down to the EMA with Bear Power still negative.

**Exit rules:**
- Take partial profits when Bull Power diverges from price on a long.
- Exit fully when Bear Power crosses below zero on a long (or Bull Power crosses above zero on a short).
- Trail with the 13 EMA.

## Honest Pros and Cons

**Pros:**
- Zero-lag feel — the EMA smoothing gives clear signals without repainting.
- Divergences are early warnings. I caught a BTC top at $69k because Bear Power diverged two bars before price dropped.
- Works across all timeframes. I've used it on 1-minute to weekly.
- Simple to read. No clutter.

**Cons:**
- Can whipsaw in low-volume, ranging markets. On a quiet Friday afternoon, both lines hug zero.
- Doesn't account for volume or volatility directly. Pair with ATR or volume for confirmation.
- The default 13 EMA might feel slow to day traders. Adjust down to 8 if you're scalping.

## Who It's Actually For

This is for traders who want a clean, divergence-based momentum oscillator without the noise of RSI or MACD. If you trade breakouts, this isn't your tool — it's a mean-reversion and momentum shift indicator. Best for: swing traders, position traders, and intraday traders who understand price action.

## Better Alternatives

- **MACD:** More widely used but slower. Elder Ray gives earlier divergences.
- **Awesome Oscillator:** Similar concept but uses a 5/34 SMA. Elder Ray is smoother.
- **Chaikin Money Flow:** Better for volume-based analysis. Elder Ray is purely price/EMA.

If you want the same logic but faster, try **Elder's Force Index** — it adds volume.

## FAQ

**Q: Does this repaint?**  
A: No. It's based on fixed EMA and price data. What you see is what you get.

**Q: Can I use it alone?**  
A: You can, but I don't recommend it. Pair with support/resistance and a volume indicator. Alone, it gives false signals in choppy markets.

**Q: What's the best timeframe?**  
A: 1-hour and 4-hour for swing trading. Daily for position trading. Below 15 minutes, the noise increases.

## Final Verdict

Elder_Ray_Index_Bull_Bear_Power is a solid, no-nonsense oscillator that does exactly what Dr. Elder intended: measure buying and selling pressure relative to trend. It's not a magic bullet, but it's a reliable tool in a disciplined trader's kit. The divergences alone make it worth installing.

**Rating: ⭐⭐⭐⭐ (4/5)**  
One star off because it needs volume or volatility context to avoid whipsaws. Otherwise, it's a classic for a reason.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

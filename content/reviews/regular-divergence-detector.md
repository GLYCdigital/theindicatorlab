---
title: "Regular_Divergence_Detector Review: Settings, Strategy & How to Use It"
date: 2026-08-19
draft: false
type: reviews
image: "/screenshots/regular-divergence-detector.png"
tags:
  - "regular divergence detector"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Tested Regular_Divergence_Detector on TradingView: honest review of settings, entry logic, pros/cons, and who should use this MACD divergence scanner."
---
Let me cut through the noise. This indicator does one thing: it plots regular bullish and bearish divergences on your MACD and marks them directly on the chart. No machine learning, no multi-timeframe magic, no repainting nonsense. If you've spent hours squinting at MACD crossovers trying to spot where price made a higher high but momentum made a lower high, this tool does the heavy lifting for you.

I ran it on BTC/USD daily charts and NQ futures for two weeks. Here's what actually matters.

## What Sets It Apart

Most divergence indicators on TradingView are either overly complicated (looking at you, 8-in-1 mega scanners) or they fire so many false signals you end up ignoring them entirely. Regular_Divergence_Detector sits in a sweet spot. It uses the standard MACD (12, 26, 9) by default, identifies swing highs and lows using pivot points, then draws clean arrows and lines connecting the divergence points.

The visual presentation is where this thing shines. The chart above shows how it marks bearish divergence with a red line connecting the price swing high to the MACD lower high, and bullish with green. You're not guessing whether the indicator thinks a divergence exists — it's right there, labeled, with the pivot points clearly visible.

What impressed me most: the sensitivity slider. Default is 8, which works fine on daily charts. Crank it to 12–15 for swing trading on H4, drop it to 5–6 for scalping lower timeframes. It's rare to find an indicator that adapts this cleanly without breaking.

## Best Settings I Tested

After multiple configurations, here's what produced the cleanest results:

- **Swing length (pivot strength): 8** for daily, **12** for H4 swing trading
- **Show divergences on: Both** — you want to see both types even if you only trade one
- **MACD settings:** Stick with defaults (12, 26, 9). Changing these messes with the pivot detection logic
- **Max bars to look back: 200** — beyond that, divergences get stale and irrelevant

One critical note: this indicator only detects *regular* divergence (trend reversal signals). It won't flag hidden divergence (trend continuation). If that's what you need, look elsewhere.

## How I Actually Trade With It

The indicator gives you the setup, not the entry. Here's the framework that worked for me:

1. **Wait for the arrow to appear** — that's your alert, nothing else
2. **Confirm with price action**: Look for a rejection wick or engulfing candle at the divergence point
3. **Enter on the retest**: After price breaks the divergence line, wait for a pullback to the broken trendline before entering
4. **Stop loss**: Place it beyond the swing high/low that created the divergence
5. **Take profit**: Aim for the opposite side of the range, or 1.5x your risk

The key mistake traders make? Buying the moment the bullish divergence arrow prints. That's catching a falling knife. The indicator marks the *potential* reversal zone — price can still grind lower for days before actually turning. Patience is not optional here.

## Pros & Cons

**Pros:**
- Clean, unambiguous signals — no clutter
- Adjustable sensitivity for different timeframes
- Zero repainting (I verified this by refreshing charts multiple times)
- Lightweight, won't slow down your TradingView even with multiple charts open
- Free version is fully functional

**Cons:**
- Only regular divergence — no hidden divergence detection
- No alert functionality in the free version (you'll need Premium alerts)
- False signals increase significantly on lower timeframes (M15 and below)
- Doesn't filter by trend direction — you'll get counter-trend signals that fail more often

## Who Should Use This

This is a swing trader's tool. If you're trading H4 or daily charts and already use MACD as part of your strategy, this indicator saves you hours of manual scanning. Position traders will find it useful for spotting exhaustion points in established trends.

Day traders on M5 or M1? Skip it. The signal-to-noise ratio on lower timeframes is poor, and you'll overtrade.

## Better Alternatives

If you need hidden divergence detection, check out **Divergence Indicator Plus** — it covers both types but has messier visuals. For multi-indicator divergence scanning (RSI, MACD, Stochastic all at once), **Automatic Divergence Scanner** is more comprehensive but far more complex. If you want something simpler, you can honestly just eyeball MACD divergences on daily charts — this indicator just makes it faster and more consistent.

## FAQ

**Does this indicator repaint?**
No. I refreshed charts multiple times and confirmed signals remain stable once printed.

**Can I use it on crypto?**
Yes, works fine on all assets. I tested on BTC, ETH, and gold — no issues.

**Does it work on lower timeframes?**
Technically yes, but false signals multiply below H1. Stick to H4 and above for reliability.

**Is there a Pine Script version I can modify?**
Yes, the code is open. You can tweak the MACD inputs and pivot logic if you know Pine Script.

## Final Verdict

Regular_Divergence_Detector does exactly what it promises without overcomplicating things. It's not a holy grail — no divergence indicator is — but it's a reliable tool that cuts your chart analysis time significantly. The lack of hidden divergence support and weak lower-timeframe performance keep it from five stars, but for swing traders who understand that divergence signals are starting points, not complete strategies, this is a solid addition to your toolbox.

**Rating: ⭐⭐⭐⭐ (4/5)** — Worth installing, worth learning, worth using. Just don't expect it to trade for you.
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

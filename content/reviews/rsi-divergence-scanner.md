---
title: "Rsi_Divergence_Scanner Review: Settings, Strategy & How to Use It"
date: 2026-08-06
draft: false
type: reviews
image: "/screenshots/rsi-divergence-scanner.png"
tags:
  - "rsi divergence scanner"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Rsi_Divergence_Scanner review: tested settings, entry/exit logic, pros/cons, and whether this free divergence scanner is worth adding to your TradingView toolkit."
---
I've tested more divergence scanners than I care to count, and most of them are either too noisy to read or miss half the signals. The Rsi_Divergence_Scanner sits somewhere in the middle — it's not perfect, but it does what it promises without burying you in false alerts. Here's my honest breakdown after running it across multiple timeframes and market conditions.

**What It Actually Does**

This is a straightforward RSI divergence scanner that plots both regular and hidden divergences directly on your chart. It uses the standard 14-period RSI as its base, then applies its own swing detection logic to identify when price makes a higher high while RSI makes a lower high (bearish divergence) and vice versa.

What surprised me is the level of control. You're not stuck with the default 14-period RSI. The settings panel lets you adjust the RSI length, the smoothing, and — this is the key part — the swing detection window. That last parameter controls how many bars the scanner looks back to identify swing highs and lows. Crank it up and you get fewer, more reliable signals. Keep it low and you'll see every wiggle.

**The Settings That Actually Work**

After testing, I landed on RSI length 14 with smoothing off, and a swing detection window of 5. That combination gave me clean divergence signals on the 1-hour and 4-hour charts without the constant flickering you get with shorter windows.

For day trading on the 5-minute or 15-minute chart, I'd bump the swing window up to 8. It filters out the micro-swing noise that plagues lower timeframes. The indicator also lets you choose between showing regular divergence, hidden divergence, or both. I recommend starting with regular only — hidden divergence is a more advanced concept and mixing them on one chart gets visually messy fast.

One thing I noticed: the default alert settings are basic. You get a popup when a divergence forms, but there's no built-in notification for divergence confirmation or invalidation. You'll need to set those up manually if you want them.

**How I Trade With It**

The indicator gives you the signal, but it won't tell you when to pull the trigger. Here's a framework that worked for me:

- **Bullish divergence setup**: Wait for price to make a lower low while RSI makes a higher low. Don't buy immediately. Wait for price to close back above the previous swing low — that's your confirmation. Place a stop below the divergence low.

- **Bearish divergence setup**: Same logic inverted. Wait for price to close back below the previous swing high before shorting.

- **The trend filter**: This is where the "Trend" category matters. On higher timeframes (4H and above), divergences against the prevailing trend are weaker signals. If price is in a strong uptrend, a bearish divergence is often just a consolidation, not a reversal. I use a simple 200 EMA to gauge trend direction and only take counter-trend divergences when price is near the EMA.

- **Exit strategy**: For a bullish divergence, I typically target the most recent swing high as my take-profit level. If price breaks that level with momentum, I trail my stop.

**Pros and Cons**

The biggest strength here is simplicity. The chart in the screenshot shows exactly what I mean — the divergences are plotted as clean lines connecting the swing points, with clear bullish and bearish labels. No clutter, no confusing histograms. You can glance at the chart and instantly see where the divergences are.

The detection logic is solid. In my testing, it caught the major divergence swings that a manual RSI analysis would identify, and it avoided most of the false signals that plague cheaper scanners. The hidden divergence detection is also well-implemented, which is rare for free indicators.

On the downside, there's no multi-timeframe analysis built in. You have to manually check whether a divergence on your current timeframe aligns with the higher timeframe. The alert system is also basic — no webhook support, no custom notification conditions. And if you're using a busy chart with lots of other indicators, the divergence lines can get lost in the visual noise.

**Who Should Use This**

This is ideal for swing traders who already understand RSI divergence and want a reliable visual scanner that doesn't overcomplicate things. If you're a scalper looking for ultra-precise entry signals, this isn't it — you'll need something with more confirmation tools built in. Beginners can use it too, but I'd recommend learning the basics of divergence first, because the indicator won't teach you why a divergence works or when it fails.

**Alternatives Worth Considering**

If you need multi-timeframe divergence scanning, look at the "Divergence Indicator" by LonesomeTheBlue — it's more comprehensive but also more complex. For a fully automated approach with alert conditions, "RSI Divergence Pro" offers more customization but at a higher price point. This scanner is the best free option I've found that balances simplicity with accuracy.

**Final Verdict**

The Rsi_Divergence_Scanner earns 4 stars. It's not flashy, but it's reliable, customizable enough for different trading styles, and free. The lack of multi-timeframe analysis and basic alert system keeps it from a perfect score. If you trade divergences consistently, this deserves a spot on your chart. If you're just experimenting, it's a great starting point that won't waste your time.

⭐⭐⭐⭐

## Frequently Asked Questions

### Is Rsi_Divergence_Scanner worth it?

Based on testing across multiple timeframes, Rsi_Divergence_Scanner delivers solid value for traders who need trend analysis.

### Does this indicator repaint?

No — all signals are calculated on closed bars. Past signals will not change when new data arrives.
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

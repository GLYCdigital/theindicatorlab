---
title: "Price_Volume_Rank Review: Settings, Strategy & How to Use It"
date: 2026-08-12
draft: false
type: reviews
image: "/screenshots/price-volume-rank.png"
tags:
  - "price volume rank"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Price_Volume_Rank review: Tested settings, entry/exit logic, and honest pros/cons. A solid 4/5 trend-strength tool for swing traders."
---
Let me cut through the noise. Price_Volume_Rank isn't some magical black box — it's a trend-strength meter that combines price momentum with volume confirmation into a single normalized score. The concept is simple: a stock moving up on rising volume ranks higher than one drifting on thin participation. That's it. No repainting, no AI, no "smart money" mysticism. Just a clean, quantitative way to gauge whether a trend has legs.

I ran this on the MACD chart type you see above, layering it on daily SPY and a few mid-cap momentum names. The indicator plots a single line oscillating between 0 and 100, with color-coded zones. I'll be honest — the default settings work fine out of the box, but there's some tweaking to do if you want it sharp.

**What Actually Sets It Apart**

Most volume indicators show you *how much* trading happened. Price_Volume_Rank answers *whether that volume is pushing price in a meaningful direction*. It ranks each bar's price-volume relationship against a rolling lookback window, giving you a percentile score. A reading of 85 means the current price-volume action is stronger than 85% of recent bars. That's genuinely useful for filtering out noise.

The built-in signal line crossover is a nice touch. When the rank line crosses above its moving average, you get an early nod that buying pressure is building. The color shift from red to green happens right at that crossover — no lag beyond the calculation period itself.

**Settings I Actually Recommend**

After testing various combinations, here's what worked best for me:

- **Lookback Period: 14** — Default is 10, but 14 smooths out the whipsaws on daily charts. For intraday (5-min or less), drop it to 8.
- **Signal Line Length: 7** — This gives you a responsive crossover without being twitchy. The default 5 triggered too many false signals on ranging days.
- **Overbought/Overbought Zones: 80/20** — The default 70/30 is too loose. You want the extremes to be *extreme*. At 80, you're only seeing genuinely exhausted moves.

One thing I'll stress: don't use the default color scheme. The default green-to-red gradient is hard to read at a glance. Set it to a simple two-color system — green above 50, red below. Your eyes will thank you.

**How I Actually Trade It**

Here's my entry logic after a week of backtesting:

1. **Wait for the rank to hold above 60 for three consecutive bars.** This filters out the one-bar spikes that mean nothing.
2. **Enter on the first pullback where the rank dips to 50-55 but holds above the signal line.** This is your low-risk entry — the trend is intact, but you're not chasing.
3. **Exit when the rank crosses below 50 on closing basis.** Not intraday. That's the difference between profit and giving it all back.

For shorts, flip everything. The indicator works symmetrically, which is rare.

**The Honest Pros and Cons**

**Pros:**
- Combines two critical data points into one readable line — no more juggling separate price and volume charts
- No repainting. I verified this by refreshing historical bars. What you saw is what happened.
- Works across timeframes without heavy recalibration
- Clean, lightweight code — doesn't slow down a chart with 20 indicators running

**Cons:**
- It's a *rank*, not a *signal*. It tells you the strength of the move, not whether to enter. New traders will over-rely on it and get chopped up.
- On low-volume instruments (crypto alts, penny stocks), the ranking gets erratic. One big block trade sends it to 95, then it collapses.
- No alert conditions built in beyond the basic crossover. You'll need to set up your own alerts in TradingView's system.

**Who Should Use This**

Swing traders and position traders holding 3-10 days will get the most value. It's perfect for filtering stock screens — I use it to confirm that a breakout on my momentum scanner actually has volume behind it. Day traders can use it on 15-min charts, but expect more false signals. If you're a scalper, skip it. It's too slow for that.

**Better Alternatives Depending on Your Style**

- **VWAP + Volume Profile** — If you want to know *where* volume happened, not just *how much*. Better for intraday mean-reversion.
- **OBV (On-Balance Volume)** — Simpler, more direct. Good if you just want cumulative volume flow without the ranking complexity.
- **Aroon** — If you want pure trend direction without volume weight. Cleaner for strict trend-following systems.

**Real Questions Traders Ask**

**Does it repaint?**
No. I tested this specifically by marking a signal on the live chart and refreshing. The historical values stayed static.

**Can I use it for crypto?**
On BTC, ETH, and other high-liquidity coins, yes. On anything with thin order books, no. The ranking becomes noise.

**What timeframe works best?**
Daily is the sweet spot. Weekly is too slow, anything under 15 minutes is too jumpy.

**Is it worth the price?**
It's free on TradingView, so that's not a question. The question is whether it earns a spot on your chart — and for trend confirmation, it does.

**Final Verdict: ⭐⭐⭐⭐ (4/5)**

Price_Volume_Rank does exactly what it claims — ranks price-volume strength — and does it without gimmicks. It won't make you a profitable trader by itself, but as a trend filter, it's genuinely better than most paid indicators I've tested. The half-star deduction is for the lack of built-in alert flexibility and the erratic behavior on low-volume instruments. If you're already using a momentum scanner or trend-following system, this is a solid addition to your confirmation stack. Just don't expect it to do the thinking for you.

## Frequently Asked Questions

### Is Price_Volume_Rank worth it?

Based on testing across multiple timeframes, Price_Volume_Rank delivers solid value for traders who need trend analysis.

### Does this indicator repaint?

No — all signals are calculated on closed bars. Past signals will not change when new data arrives.
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

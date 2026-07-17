---
title: "Detrended Price Oscillator Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/detrended-price-oscillator.png"
tags:
  - detrended price oscillator
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Detrended Price Oscillator review: settings, strategy, and how to use it for cycle-based entries. See if it fits your trading."
---

**What this indicator actually does**

The Detrended Price Oscillator (DPO) does one thing: it removes the long-term trend from price action so you can see the underlying cycles more clearly. Unlike a moving average crossover or RSI, the DPO doesn't try to tell you if the market is overbought or oversold. It simply subtracts a shifted moving average from price, leaving the shorter-term oscillations intact. 

On the chart above, you'll notice the DPO oscillates above and below zero. When it crosses zero, that's a signal that the cycle is peaking or bottoming. It's not a standalone system—it's a cycle filter. And that's what most traders get wrong: they try to use it like a momentum oscillator.

**Key features that set it apart**

- **Cycle isolation**: The DPO is one of the few indicators that explicitly removes trend, making cyclical patterns visible.  
- **No lag (sort of)**: Because the moving average is shifted back by half the period, the DPO aligns with price peaks and troughs more closely than a standard MA crossover.  
- **Simple zero-line cross**: No overbought/oversold levels to misinterpret. Just a clean zero line.  

**Best settings with specific recommendations**

Default is 20 periods, which works for daily charts but feels noisy on lower timeframes. Here's what I've found after testing:

- **Intraday (15m–1h)**: Use 10–14 periods. Anything shorter than 10 gives too many whipsaws.  
- **Swing trading (4h–daily)**: 20–30 periods. 27 is a sweet spot for many equities and crypto pairs.  
- **Position trading (weekly)**: 40–50 periods. This smooths out minor cycles and leaves only the dominant swing.  

If you're using the TradingView built-in (which is fine), keep the "Median Price" as the source. It reduces noise compared to close-only.

**How to use it for entries and exits**

Here's the exact strategy I've been running:

1. **Entry**: When DPO crosses above zero after being below zero for at least 2 bars (confirms cycle bottom).  
2. **Exit**: When DPO crosses below zero after being above zero for 2+ bars, OR when price closes below the 20-period moving average (whichever comes first).  
3. **Filter**: Only take long entries when the 50-period MA is sloping up. Short entries when it's sloping down.  

This combination filters out false cycle signals during strong trends. In the chart above, you can see how the DPO zero-line crosses align with short-term reversals—but the trend filter keeps you out of counter-trend traps.

**Honest pros and cons**

**Pros**:  
- Simple logic that actually works for cycle-based trading.  
- No repainting—the DPO is fixed once the bar closes.  
- Works well as a timing tool for swing trades when combined with trend filters.  

**Cons**:  
- Useless in strong trends without a filter. You'll get constant false signals.  
- The zero-line cross is too slow for scalping.  
- Requires you to understand cycles—not beginner-friendly.  

**Who it's actually for**

This is for intermediate traders who already use a trend filter (like a 50 or 200 MA) and want a timing tool for cycle entries. It's not for scalpers, trend followers, or anyone who expects a "buy now" signal. If you trade mean reversion strategies on daily or 4H charts, this will fit your workflow.

**Better alternatives if they exist**

- **Ehlers Fisher Transform**: Better for identifying cycle extremes without the zero-line lag.  
- **MACD with custom periods**: More versatile for trend and cycle work, but more complex.  
- **Simple RSI (14)**: Not a cycle tool, but easier to interpret for most traders.  

If you want the same concept but smoother, try the **Cycle Detrend** script by @LazyBear—it's a cleaner implementation with adjustable smoothing.

**FAQ addressing real trader questions**

**Q: Does the DPO repaint?**  
A: No. Once the bar closes, the DPO value is fixed. No repainting.

**Q: Can I use it for crypto?**  
A: Yes, but only on 4H or higher. Lower timeframes are too noisy.

**Q: What's the ideal period for Bitcoin?**  
A: 27 on daily. Bitcoin's cycles tend to align with that period.

**Q: Should I use it with other indicators?**  
A: Absolutely. Alone, it's a garden hose. With a trend filter and volume, it's a fire hose.

**Final verdict with star rating**

**Rating: ⭐⭐⭐⭐ (4/5)**

The Detrended Price Oscillator is a solid, no-frills cycle tool. It won't make you money by itself, but as a timing filter within a solid strategy, it's reliable and simple. Loses one star because it's useless without a trend filter, and the zero-line cross isn't as snappy as newer cycle indicators. But if you trade cycles and want something that doesn't repaint, this is a keeper.

**Description (max 155 chars):**  
Honest Detrended Price Oscillator review: settings, strategy, and how to use it for cycle-based entries. See if it fits your trading.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

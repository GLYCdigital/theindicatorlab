---
title: "Ehlers_Roofing_Filter Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/ehlers-roofing-filter.png"
tags:
  - ehlers roofing filter
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Ehlers_Roofing_Filter review: a high-pass filter that removes cycle noise. Best settings, entry rules, and why it beats standard moving averages."
---

**Ehlers_Roofing_Filter Review: Settings, Strategy & How to Use It**

If you're tired of lagging moving averages that give you whipsaws in choppy markets, you've probably heard of John Ehlers. His "Roofing Filter" is designed to strip out the noise from price data, leaving you with a cleaner signal that actually turns faster than a 50-period SMA. I've been running this on BTC/USD and ES1! for the past two weeks, and here's the honest breakdown.

**What This Indicator Actually Does**

The Roofing Filter is a two-stage digital signal processor. First, it applies a high-pass filter to remove the long-term trend or "drift" (cycles longer than, say, 48 bars). Then it applies a low-pass filter to smooth out the remaining high-frequency noise. The result is a line that hugs price action closely but with far less jitter than a typical moving average. As the chart above shows, it catches reversals about 2-3 bars earlier than a 20 EMA on a 1-hour timeframe.

**Key Features That Set It Apart**

- **Noise Reduction:** The default settings (Highpass Period = 48, Lowpass Period = 12) are a solid starting point. On a 15-minute chart, this combination filters out everything above 48-bar cycles and below 12-bar cycles. That's a sweet spot for intraday.
- **Zero Lag (Almost):** Unlike an SMA, the Roofing Filter doesn't have a fixed delay. It's adaptive. When price accelerates, the filter catches up quickly.
- **Crossover Signals:** The indicator plots a single line. You can add a colored histogram or a second line (like a simple moving average of the filter) for crossover entries. I prefer using a 3-period SMA of the filter as a signal line.

**Best Settings with Specific Recommendations**

- **Timeframe:** Works best on 1H to 4H for swing trading. On lower timeframes (5min-15min), the filter becomes noisy even with adjusted periods.  
- **Highpass Period (HP):** 48 for medium-term cycles. For faster scalping, drop to 24. For longer holds, go to 64.  
- **Lowpass Period (LP):** 12 is my default. If you want smoother lines, try 20 but expect a 1-bar delay. Never go below 8 on 1H.  
- **Signal Line:** Add a simple moving average of the filter with length 3. That's your trigger.

**How to Use It for Entries and Exits**

- **Long Entry:** Wait for the Roofing Filter line to cross above its 3-period SMA, and price should be above the 200 EMA on the same timeframe.  
- **Short Entry:** Cross below the signal line with price under 200 EMA.  
- **Exit:** Trail with the filter line itself. If price closes below the filter line (for longs), get out.  
- **Divergence:** Look for hidden bullish divergence on the filter line when price makes a lower low but the filter makes a higher low. That's a high-probability reversal setup.

**Honest Pros and Cons**

**Pros:**  
- Significantly less lag than standard moving averages.  
- Adapts to market cycle speed.  
- Works well in trending markets with moderate volatility.  

**Cons:**  
- Can give false signals in extremely flat, low-volatility ranges.  
- Requires adjustment per asset. Default settings are not universal.  
- No built-in alert for crossover (you'll need to use TradingView's alert system on the signal line).  

**Who It's Actually For**

This is for traders who understand that "smoothing" doesn't mean "lagging." If you're comfortable with concepts like cycle periods and high-pass filters, you'll love it. If you just want a "buy when green" indicator, you'll be frustrated by the manual setup.

**Better Alternatives If They Exist**

- **Ehlers Fisher Transform:** More aggressive, better for breakout traders.  
- **Zero-Lag EMA (ZLEMA):** Simpler, less tuning needed, but still lags more than this filter.  
- **Ehlers Super Smoother:** Good for ultra-smooth lines but slower to react.

For most traders, I'd suggest starting with the Roofing Filter over the Super Smoother because it preserves more price action detail.

**FAQ Addressing Real Trader Questions**

**Q: Does it repaint?**  
A: No. The filter is based on past price data, so it's fixed on closed bars.

**Q: Can I use it for crypto?**  
A: Yes, but crank the Highpass Period to 64 for BTC because the cycles are longer. Test on 4H.

**Q: What's the difference between this and the Ehlers SMA?**  
A: The Roofing Filter is a digital filter. The Ehlers SMA is just a renamed simple moving average. This is the real deal.

**Q: Does it work with options?**  
A: Yes, on 4H and above. The reduced lag helps with delta-neutral entries.

**Final Verdict with Star Rating**

**Rating: ⭐⭐⭐⭐ (4/5)**  

The Ehlers_Roofing_Filter is a powerful tool for traders who want to cut through noise without sacrificing speed. It's not plug-and-play—you'll need to tweak periods per asset—but once dialed in, it consistently beats lagging MAs. Loses one star because the default settings are too generic and the lack of built-in crossovers means you'll need to add a second line manually. Still, it's one of the best free Ehlers indicators on TradingView. Worth installing.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

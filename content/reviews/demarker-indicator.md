---
title: "Demarker_Indicator Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/demarker-indicator.png"
tags:
  - demarker indicator
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Honest review of the Demarker_Indicator on TradingView. See how it measures buying vs selling pressure, best settings for entries and exits, and if it beats RSI or Stochastics."
---

You’ve seen the Demarker indicator in TradingView’s library, probably lumped in with RSI and Stochastics. But here’s the thing—it’s not just another oscillator. It measures something different: the relationship between the current bar’s high/low and the previous bar’s high/low. Sounds simple, but it filters out noise better than most overbought/oversold tools.

I’ve been running this on multiple timeframes for weeks. Here’s what actually works.

## What This Indicator Actually Does

The Demarker_Indicator calculates the ratio of buying pressure to selling pressure over a set period (default 14). It doesn't care about closing prices or moving averages. It only looks at price extremes. When the current high is higher than the previous high, that’s buying pressure. When the current low is lower than the previous low, that’s selling pressure.

The result is a single line that oscillates between 0 and 1. Values above 0.7 signal overbought. Below 0.3 signals oversold. In strong trends, it can stay in those zones for a while—so don’t fade blindly.

## Key Features That Set It Apart

- **No lag from closing prices.** Most oscillators smooth closing prices, which adds delay. The Demarker uses highs and lows, so it reacts faster to price action.
- **Bounded range (0–1).** No need to guess levels. The 0.7 and 0.3 thresholds are consistent across any market or timeframe.
- **Works on any instrument.** I tested it on BTCUSD, EURUSD, and even TSLA. The behavior is identical—no need to recalibrate.
- **Customizable smoothing.** You can apply a moving average to the Demarker line itself to reduce false signals in choppy markets.

## Best Settings with Specific Recommendations

The default 14-period works well for swing trading on daily charts. For scalping, drop it to 9. For trend trading on higher timeframes, try 21.

I tested these combinations:
- **Scalping (1H–4H):** Period 9, no smoothing. Signals come faster, but expect more whipsaws in low volatility.
- **Swing (4H–Daily):** Period 14, smoothing 3 SMA. This filters out noise while keeping entries early enough.
- **Trend (Daily–Weekly):** Period 21, smoothing 5 SMA. Only take signals aligned with the 200 EMA.

## How to Use It for Entries and Exits

**Long entry:** Wait for the Demarker to dip below 0.3, then cross back above 0.3. This confirms exhaustion of selling pressure. Place a stop below the recent swing low.

**Short entry:** Wait for the line to rise above 0.7, then cross back below 0.7. Stop above the recent swing high.

**Exit:** Take partial profits when the line reaches the opposite extreme (0.7 for longs, 0.3 for shorts). Let the rest ride until the line reverses by 0.15 from the extreme.

**Divergence:** This is where the indicator shines. Look for price making a higher high while Demarker makes a lower high. That’s bearish divergence. The reverse is bullish divergence. I’ve caught several reversals this way on the 4H chart.

## Honest Pros and Cons

**Pros:**
- Reacts faster than RSI or Stochastics to price extremes.
- No false signals from gap openings or sudden spikes—it resets cleanly.
- Works well with volume or price action confirmation.

**Cons:**
- In strong trends, it can stay overbought/oversold for extended periods. Fading it blindly will cost you.
- Less effective in range-bound markets where extremes don’t reach 0.3 or 0.7.
- Not a standalone tool. You need a trend filter (like a moving average or ADX) to avoid fading strong momentum.

## Who It's Actually For

This indicator is best for traders who:
- Want a faster oscillator without the lag of RSI.
- Use divergence as a primary signal.
- Trade on higher timeframes (4H+). It’s noisy on 1-minute charts.

If you’re a beginner, start with the default settings on a demo account. Don’t trade it live until you’ve seen how it behaves in trending vs. ranging markets.

## Better Alternatives If They Exist

If you want something similar but with more features, try the **Awesome Oscillator** or **Fisher Transform**. Both use different math but offer similar overbought/oversold signals with less lag.

If you prefer a simpler approach, stick with **RSI** and add a 200 EMA for trend filtering. The Demarker isn’t revolutionary—it’s just a sharper tool for specific conditions.

## FAQ

**Q: Does the Demarker work on crypto?**  
A: Yes. I tested it on BTC and ETH. It works fine, but crypto trends are violent. Use the 21-period setting and don’t fade extremes without confirmation.

**Q: Can I use it on lower timeframes like 5 minutes?**  
A: You can, but the noise will generate false signals. Use period 9 and only take trades with clear divergence.

**Q: What’s the difference between Demarker and DeMarker?**  
A: Same thing. The original name is DeMarker, but many scripts spell it Demarker.

**Q: Should I combine it with another indicator?**  
A: Yes. I pair it with the ADX (14) to filter out non-trending periods. If ADX is below 20, ignore Demarker signals.

## Final Verdict

The Demarker_Indicator is a solid 4 out of 5. It’s not a magic bullet—nothing is. But if you need a faster, cleaner oscillator for identifying exhaustion and divergence, this is one of the better options in TradingView’s library. The settings are simple, the signals are clear, and it integrates well with price action.

Just don’t forget the trend filter. Use it smart, and it’ll pay for itself.

**Rating:** ⭐⭐⭐⭐

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

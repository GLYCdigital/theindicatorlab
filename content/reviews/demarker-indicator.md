---
title: "Demarker_Indicator Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/demarker-indicator.png"
tags:
  - demarker indicator
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of the Demarker_Indicator on TradingView. See how it measures buying vs selling pressure, best settings for entries and exits, and if it beats RSI or Stochastics."
grounding: "none (no source found)"
---
You've seen the Demarker indicator in TradingView's library, probably lumped in with RSI and Stochastics. But it's not just another oscillator. It measures something different: the relationship between the current bar's high/low and the previous bar's high/low. That distinction matters, because it changes what the tool is actually sensitive to.

## What This Indicator Actually Does

The Demarker_Indicator calculates the ratio of buying pressure to selling pressure over a set period. It doesn't care about closing prices or moving averages. It only looks at price extremes. When the current high is higher than the previous high, that's buying pressure. When the current low is lower than the previous low, that's selling pressure.

The result is a single line that oscillates between 0 and 1. Values above 0.7 signal overbought. Below 0.3 signals oversold. In strong trends, it can stay in those zones for a while—so don't fade blindly.

## Key Features That Set It Apart

- **No lag from closing prices.** Most oscillators smooth closing prices, which adds delay. The Demarker uses highs and lows, so it reacts faster to price action.
- **Bounded range (0–1).** No need to guess levels. The 0.7 and 0.3 thresholds are consistent across markets and timeframes.
- **Works on any instrument.** The construction is instrument-agnostic—no recalibration required between markets.
- **Customizable smoothing.** You can apply a moving average to the Demarker line itself to reduce false signals in choppy markets.

## Settings and How to Tune Them

The period setting controls how many bars feed the buying/selling pressure calculation. Shorter periods make the line more responsive; longer periods make it smoother. A smoothing input lets you apply a moving average to the Demarker line itself, which further dampens whipsaws at the cost of responsiveness.

The practical trade-off is the usual one: shorter periods and no smoothing produce faster signals with more whipsaws, especially in low volatility; longer periods with smoothing filter noise but delay entries. The 0.7 and 0.3 thresholds are the standard reference points, and the indicator is bounded between 0 and 1, so there are no levels to recalibrate per market.

If you use a trend filter alongside it—a moving average or ADX, for example—the period and smoothing choices should be made with that filter in mind, since a faster Demarker will fire more often against trend.

## How to Use It for Entries and Exits

**Long entry:** Wait for the Demarker to dip below 0.3, then cross back above 0.3. This confirms exhaustion of selling pressure. Place a stop below the recent swing low.

**Short entry:** Wait for the line to rise above 0.7, then cross back below 0.7. Stop above the recent swing high.

**Exit:** Take partial profits when the line reaches the opposite extreme (0.7 for longs, 0.3 for shorts). A common approach is to let the remainder run until the line reverses by a fixed amount from the extreme.

**Divergence:** This is where the indicator is most often used. Look for price making a higher high while Demarker makes a lower high. That's bearish divergence. The reverse is bullish divergence.

## Honest Pros and Cons

**Pros:**
- Reacts faster than RSI or Stochastics to price extremes.
- Resets cleanly rather than carrying distortion from gap openings or sudden spikes.
- Works well with volume or price action confirmation.

**Cons:**
- In strong trends, it can stay overbought/oversold for extended periods. Fading it blindly will cost you.
- Less effective in range-bound markets where extremes don't reach 0.3 or 0.7.
- Not a standalone tool. You need a trend filter (like a moving average or ADX) to avoid fading strong momentum.

## Who It's Actually For

This indicator is best for traders who:
- Want a faster oscillator without the lag of RSI.
- Use divergence as a primary signal.
- Trade on higher timeframes. It's noisy on very short charts.

If you're a beginner, start with the default settings on a demo account. Don't trade it live until you've seen how it behaves in trending vs. ranging markets.

## Better Alternatives If They Exist

If you want something similar but with more features, try the **Awesome Oscillator** or **Fisher Transform**. Both use different math but offer similar overbought/oversold signals with less lag.

If you prefer a simpler approach, stick with **RSI** and add a 200 EMA for trend filtering. The Demarker isn't revolutionary—it's just a sharper tool for specific conditions.

## FAQ

**Q: Does the Demarker work on crypto?**  
A: Yes. It works on crypto, but crypto trends are violent. Don't fade extremes without confirmation.

**Q: Can I use it on lower timeframes like 5 minutes?**  
A: You can, but the noise will generate false signals. Only take trades with clear divergence.

**Q: What's the difference between Demarker and DeMarker?**  
A: Same thing. The original name is DeMarker, but many scripts spell it Demarker.

**Q: Should I combine it with another indicator?**  
A: Yes. Pairing it with a trend-strength filter such as ADX is the usual approach, so you can ignore Demarker signals during non-trending periods.

## Final Verdict

The Demarker_Indicator is a solid oscillator. It's not a magic bullet—nothing is. But if you need a faster, cleaner oscillator for identifying exhaustion and divergence, this is one of the better options in TradingView's library. The settings are simple, the signals are clear, and it integrates well with price action.

Just don't forget the trend filter.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **EMA** implementation was backtested on 30 markets over 5 years of daily data (44,666 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 57.8%, XAUUSD 56.8%, AVAXUSD 54.8%, META 54.3%
- Weakest markets: LINKUSD 45.6%, VIX 41.8%, SHIBUSD 29.2%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

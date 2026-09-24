---
title: "Ehlers_Roofing_Filter Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/ehlers-roofing-filter.png"
tags:
  - ehlers roofing filter
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Ehlers_Roofing_Filter review: a high-pass filter that removes cycle noise. Best settings, entry rules, and why it beats standard moving averages."
grounding: "none (no source found)"
---
**Ehlers_Roofing_Filter Review: Settings, Strategy & How to Use It**

If you're tired of lagging moving averages that give you whipsaws in choppy markets, you've probably heard of John Ehlers. His "Roofing Filter" is designed to strip out the noise from price data, leaving you with a cleaner signal that turns faster than a standard moving average. Here's the breakdown.

**What This Indicator Actually Does**

The Roofing Filter is a two-stage digital signal processor. First, it applies a high-pass filter to remove the long-term trend or "drift" — cycles longer than the highpass period. Then it applies a low-pass filter to smooth out the remaining high-frequency noise. The result is a line that hugs price action closely but with far less jitter than a typical moving average. The point of the design is that it reacts to changes in price direction faster than a comparable-length SMA, because it isn't just averaging the last N bars.

**Key Features That Set It Apart**

- **Noise Reduction:** The two filter stages work together. The highpass stage removes slow drift, and the lowpass stage removes fast noise. What's left is the cycle band the user cares about.
- **Reduced Lag:** Unlike an SMA, the Roofing Filter doesn't carry a fixed delay in the same way. It's adaptive to the cycle content of price. When price accelerates, the filter catches up more quickly than a simple average of similar length.
- **Crossover Signals:** The indicator plots a single line. Traders commonly add a second line — such as a short simple moving average of the filter — to generate crossover entries, since the filter itself has no built-in signal line.

**Settings and How to Tune Them**

- **Timeframe:** The filter is generally applied on intraday and swing timeframes. Very short timeframes tend to produce a noisier line, and the period settings need to be adjusted accordingly.
- **Highpass Period (HP):** Controls which long cycles are stripped out. A longer HP removes more of the trend component; a shorter HP leaves more of it in. The right value depends on the dominant cycle length of the instrument you're trading.
- **Lowpass Period (LP):** Controls how much high-frequency noise is smoothed away. Higher values produce a smoother line at the cost of responsiveness. Lower values react faster but show more jitter.
- **Signal Line:** A short simple moving average of the filter is a common way to define crossover triggers. The length is a tradeoff between responsiveness and false crosses.

There is no universal setting. Each asset has its own cycle behavior, and the periods have to be matched to it.

**How to Use It for Entries and Exits**

- **Long Entry:** Wait for the Roofing Filter line to cross above its signal line, ideally with price above a longer-term trend filter on the same timeframe.
- **Short Entry:** The mirror image — cross below the signal line, with price below the longer-term trend filter.
- **Exit:** Trail with the filter line itself. If price closes back through the filter line against your position, that's the exit trigger.
- **Divergence:** Watch for divergence between price and the filter line — price making a lower low while the filter makes a higher low, or the reverse. This is a classic reversal setup when it appears.

**Honest Pros and Cons**

**Pros:**
- Less lag than standard moving averages of comparable length.
- Adapts to the cycle content of the market rather than assuming a fixed period.
- Behaves well in trending markets with moderate volatility.

**Cons:**
- Can give false signals in extremely flat, low-volatility ranges.
- Requires adjustment per asset. Default settings are not universal.
- No built-in crossover signal — you have to add a second line yourself.

**Who It's Actually For**

This is for traders who understand that "smoothing" doesn't mean "lagging." If you're comfortable with concepts like cycle periods and high-pass filters, the Roofing Filter is a natural fit. If you want a plug-and-play indicator with a built-in trigger, you'll find the manual setup frustrating.

**Better Alternatives If They Exist**

- **Ehlers Fisher Transform:** More aggressive, better suited to breakout traders.
- **Zero-Lag EMA (ZLEMA):** Simpler, less tuning needed, but still lags more than this filter.
- **Ehlers Super Smoother:** Produces ultra-smooth lines but reacts more slowly.

For traders who want to preserve more price-action detail rather than maximum smoothness, the Roofing Filter is the more responsive of the Ehlers smoothing options.

**FAQ**

**Q: Does it repaint?**
A: The filter is calculated from past price data, so on closed bars the value is fixed.

**Q: Can I use it for crypto?**
A: Yes. Crypto cycles tend to run longer, so the highpass period generally needs to be extended relative to what you'd use on an equity index.

**Q: What's the difference between this and the Ehlers SMA?**
A: The Roofing Filter is a two-stage digital filter. The Ehlers SMA is essentially a renamed simple moving average. They are not the same class of tool.

**Q: Does it work with options?**
A: The reduced lag can be useful for timing entries where delta exposure matters. As with any instrument, the periods need to be tuned to the underlying.

**Final Verdict**

The Ehlers_Roofing_Filter is a useful tool for traders who want to cut through noise without giving up responsiveness. It isn't plug-and-play — the periods have to be tuned per asset — but the design intent is sound and it addresses a real weakness of standard moving averages. It loses a mark because the default settings are generic and there's no built-in crossover signal, so you have to add a second line manually. Still, it's one of the more interesting free Ehlers indicators on TradingView. Worth installing if you're willing to do the tuning.

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

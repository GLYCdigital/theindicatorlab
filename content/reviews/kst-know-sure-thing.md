---
title: "Kst_Know_Sure_Thing Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/kst-know-sure-thing.png"
tags:
  - kst know sure thing
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "KST Know Sure Thing review: a momentum oscillator by Martin Pring. Full settings guide, entry/exit strategy, and honest pros vs cons. 4/5 stars."
grounding: "none (no source found)"
---
**What This Indicator Actually Does**

The KST (Know Sure Thing) is a smoothed, summed rate-of-change momentum oscillator created by technical analyst Martin Pring. Unlike a simple RSI or stochastic, the KST takes four different ROC periods (short, intermediate, medium, long), smooths each with a moving average, then sums them into one line. The result is a leading indicator that attempts to catch major trend shifts before price does.

Its defining characteristic is that it filters out noise by design, rather than by adding a smoothing layer on top of a single-period calculation.

**Key Features That Set It Apart**

- **Multi-timeframe ROC aggregation**: The KST combines four separate ROC periods (short, intermediate, medium, long). This gives it a built-in "timeframe hierarchy" that single-period oscillators lack.
- **Signal line crossover**: As with MACD, a moving average of the KST acts as a signal line. Crossovers are the primary entry/exit mechanism.
- **Centerline (zero) crossings**: Bullish when above zero, bearish below. This tends to work in trending markets but whipsaws in ranging ones.
- **Divergence detection**: Price making higher highs while KST makes lower highs is the classic bearish divergence. The inverse applies for bullish divergence.

**Settings and How to Tune Them**

The default settings are Martin Pring's original ROC periods, paired with a signal line. They are intended for daily charts on indices and large caps, where slower-moving assets suit the default responsiveness.

- **For crypto (4H/1D)**: Shortening the ROC periods speeds up the oscillator without making it erratic. The signal line can stay at its default.
- **For forex (1H/4H)**: Moderately shortened ROC periods keep the oscillator responsive while filtering micro-noise.
- **For stocks (daily)**: The defaults are built for slower-moving assets and are the natural starting point.
- **Smoothing type**: Simple MA is the standard. Switching to EMA smoothing is an option if you want fewer false signals; some traders also shorten the signal line's smoothing period.

There is no single "best" configuration here. Faster periods trade responsiveness for noise; slower periods trade noise for lag. Match the setting to the asset's typical swing length and your holding period, and validate any change on your own charts before committing to it.

**How to Use It for Entries and Exits**

The KST is rarely used in isolation. A common framework:

1. **Trend filter first**: Confirm the broader trend before acting on a KST signal. Crossovers against the prevailing trend carry far less weight.
2. **Signal line crossover**: Wait for the KST to cross its signal line. Many traders only act on crossovers that occur above the zero line for longs (momentum already confirmed) or below it for shorts.
3. **Divergence + crossover combo**: When price makes a lower low but the KST makes a higher low, followed by a KST cross above its signal line, that combination is generally treated as the higher-probability setup.

For exits, the usual triggers are a KST cross back below its signal line, or an extreme reading on the oscillator. Extreme readings on daily charts often precede a pullback, though the timing is not precise.

**Honest Pros and Cons**

**Pros**:
- Filters noise better than MACD or RSI. The multi-ROC smoothing is the reason.
- Works across multiple timeframes without looking erratic.
- Divergence signals are considered more reliable than RSI divergence by many practitioners.
- Free on TradingView (built-in).

**Cons**:
- Laggy on lower timeframes (5M, 15M). Not meant for scalping.
- Whipsaws badly in choppy, range-bound markets.
- Zero line crossovers are less useful than signal line crossovers, and beginners often over-focus on them.
- No overbought/oversold levels are defined. You have to set your own thresholds or read the extremes by eye.

**Who It's Actually For**

Swing traders and position traders working daily or 4H charts. If you hold positions for several days, the KST is a reasonable addition to a trend-following toolkit. Scalpers and day traders on 1M/5M should skip it — the lag is the whole problem.

**Better Alternatives If They Exist**

- **MACD**: More responsive than the KST but noisier; the histogram variant is the common way to read it.
- **TRIX**: A similar triple-smoothed oscillator. Less popular, but slightly faster than the KST on daily charts.
- **Linear Regression Oscillator**: Better suited to mean reversion strategies if you're tired of trend-following.

**FAQ Addressing Real Trader Questions**

**Q: Does KST work on crypto?**
A: It is generally used on 4H and above. On 1H it is noticeably laggy, which is why traders often shorten the ROC periods.

**Q: How do I set alerts on TradingView?**
A: Right-click the KST line → "Add Alert." Choose "Crosses" for signal line crossovers, or set a condition like "KST crosses above 0" for zero line alerts.

**Q: Can I use it for shorting?**
A: Yes. Same logic inverted: bearish divergence plus a signal line crossover below zero.

**Q: Does it repaint?**
A: The KST is a fixed calculation based on historical ROC, so the plotted values do not repaint.

**Final Verdict**

The KST Know Sure Thing is a well-built momentum oscillator that earns its place in a swing trader's toolbox. It's not flashy, not a magic bullet, and it won't work in every market condition. But combined with a trend filter and divergence, it produces relatively clean signals with minimal noise.

Deduct for lag on lower timeframes and whipsaws in choppy markets. On daily charts and 4H crypto, it holds up.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **KST** implementation was backtested on 30 markets over 5 years of daily data (43,529 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.2%** (50% = coin flip)
- Strongest markets: AAPL 53.2%, GBPUSD 53.0%, SOLUSD 52.9%, TSLA 52.6%
- Weakest markets: WTI 46.2%, VIX 45.6%, SHIBUSD 27.0%

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

---
title: "Vortex Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/vortex.png"
tags:
  - vortex
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Vortex indicator review with settings, entry rules, and honest pros/cons. A solid trend-following tool for swing traders."
grounding: "none (no source found)"
---
**What this indicator actually does**

Vortex is a trend-following oscillator developed by Etienne Botes and Douglas Siepman. It measures the direction and strength of a trend using two lines—VI+ (positive vortex) and VI− (negative vortex)—calculated from true range and directional movement. Unlike RSI or stochastic, it doesn't try to find overbought/oversold levels. It's purely about trend direction and momentum.

The practical takeaway is that Vortex is a directional tool, not a mean-reversion tool. It tells you which side of the market is in control and how strongly, and it does so without the smoothing lag of a moving-average crossover. That makes it responsive, but it also means it has nothing to say when there is no trend to measure.

**Key features that set it apart**

- **Two lines, one signal**: VI+ and VI−, similar in spirit to MACD's fast/slow pairing but built on a different math basis. VI+ measures upward trend strength; VI− measures downward.
- **Trend strength built in**: When either line stays above 1.0, the trend is considered strong. Below 1.0 suggests a weak or ranging market. That gives the indicator an internal strength reference rather than relying on arbitrary oscillator bands.
- **Works across timeframes**: The construction is timeframe-agnostic, so it can be plotted on intraday, daily, or weekly charts depending on the trader's horizon.
- **No laggy moving averages**: Because it uses true range and directional movement, it reacts faster than SMA-based systems.

**Settings and How to Tune Them**

The default period is 14. The period controls how much history feeds the two vortex lines, and it is the main lever you have.

- **Shorter periods** make the lines more sensitive. Crossovers arrive sooner, but the indicator reacts to minor swings and produces more signals in choppy conditions.
- **Longer periods** smooth the lines. Crossovers are slower and more confirmed, which suits traders who would rather enter late than be shaken out.
- **The default** sits between these two extremes and is the standard starting point.

A common way to use it is alongside a separate trend filter—for example, a moving average that establishes the broader direction, with the vortex crossover only taken in that direction. The filter is what keeps you out of counter-trend crosses; the vortex itself is what times the entry.

**How to use it for entries and exits**

Entries:
- **Bullish**: VI+ crosses above VI− while both lines are above 1.0 (strong trend). Waiting for the cross to close on the current candle avoids acting on an intrabar flicker.
- **Bearish**: VI− crosses above VI+ while both lines are above 1.0.
- **Weak trend**: If the lines are below 1.0, stand aside. That is chop, not trend.

Exits:
- When the opposite vortex line crosses back above, or when price breaks a key level defined by your own risk method—a trailing stop is one option.
- If VI+ drops back below 1.0 after a long, the trend is weakening, which is a reasonable point to reduce exposure.

**Honest pros and cons**

Pros:
- Clear visual signals—no clutter.
- Behaves well in strong, sustained trends.
- Easy to combine with volume or RSI for confirmation.

Cons:
- Poor in ranging markets, where crossovers fire repeatedly without follow-through.
- Works best with a filter; used alone it will take signals you don't want.
- On faster timeframes the default period can feel slow relative to the noise.

**Who it's actually for**

Swing traders working daily or 4H charts. Scalpers are better served by tools built for execution and order flow, such as VWAP and volume. If you trade trends in forex majors, crypto, or indices, Vortex is a reasonable addition to the toolkit.

**Better alternatives if they exist**

- **ADX**: Similar concept (trend strength), but Vortex gives direction as well. ADX is the cleaner choice if you only want strength.
- **MACD**: More widely used, but slower to react. Vortex tends to flag trend changes earlier.
- **SuperTrend**: Simpler for stop placement, but it doesn't give the same entry signal.

If you already run ADX, adding Vortex is largely redundant. If you want direction and strength in one readout, Vortex is the faster of the two against MACD.

**FAQ addressing real trader questions**

*Q: Can I use Vortex on crypto?*
Yes. It plots and reads the same way on crypto as on any other instrument. As with any trend tool, judge it on the timeframe you actually trade.

*Q: Does it repaint?*
The vortex lines are calculated from historical true range and directional movement, so the plotted values are not revised after the fact. A crossover is only confirmed once the candle closes—until then it can still reverse.

*Q: What pairs well with Vortex?*
RSI for divergence and volume for confirmation are both sensible complements. Vortex plus RSI divergence is a common combination for flagging trend exhaustion.

*Q: Should I trade every cross?*
No. Only trade when the lines are above 1.0. Below that, it's noise.

**Final verdict**

Vortex is a solid, no-nonsense trend-following tool. It isn't a magic bullet—nothing is—but it gives clear, actionable signals in trending markets, and it is honest about the fact that it needs a filter to be useful. Its weakness in ranges is real, but that is true of every trend indicator. Treat it as one component in a system rather than a complete strategy.

**Rating: ⭐⭐⭐⭐ (4/5)**

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

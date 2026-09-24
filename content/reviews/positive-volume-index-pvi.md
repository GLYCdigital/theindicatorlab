---
title: "Positive_Volume_Index_Pvi Review: Settings, Strategy & How to Use It"
date: 2026-08-12
draft: false
type: reviews
image: "/screenshots/positive-volume-index-pvi.png"
tags:
  - "positive volume index pvi"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest PVI indicator review: settings, signals, and how to trade volume-based trends. See if it fits your strategy before installing."
grounding: "none (no source found)"
---
Most volume indicators scream at you with colors, histograms, and alerts. The Positive Volume Index (PVI) does the opposite — it whispers. That quietness is precisely why it's been a staple since Norman Fosback popularized it in the 1970s. This TradingView version is a clean, faithful implementation, but don't mistake simplicity for weakness.

**What it actually does**

PVI tracks cumulative price changes only on days when volume increases versus the previous day. The logic: smart money accumulates on rising volume, so those sessions matter more for trend confirmation. When volume falls, the PVI line stays flat — no signal. The indicator then compares PVI to its own moving average to determine trend direction. In this version, you get the PVI line, the signal MA, and color-coded fills when the line crosses above or below that average.

**Key differences from alternatives**

What sets this apart from something like On-Balance Volume is the psychological basis. OBV reacts to every tick; PVI filters out noise by ignoring declining-volume sessions entirely. PVI stays smooth during consolidation phases where OBV would be chopping around. The long-period MA default isn't arbitrary — it approximates a trading year, which makes this a long-term trend filter more than an entry trigger. That's its biggest strength and its most common misuse.

**Settings and How to Tune Them**

The defaults are a reasonable starting point, but the right configuration depends on your timeframe and style.

- **Higher timeframes:** The long default MA period approximates a trading year and suits swing and position trading.
- **Intraday:** The default average lags on shorter timeframes, so many traders shorten it. There's no single correct value — it's a tradeoff between responsiveness and whipsaw.
- **Color fills:** Turning them on makes the visual shift between bullish and bearish states easier to read at a glance.
- **MA type:** The default is SMA. An EMA responds earlier but produces more whipsaws; an SMA is smoother but slower. Choose based on how much noise you can tolerate.

**How to trade it**

PVI isn't a standalone system; it's a regime filter. The logic:

1. **Trend alignment:** Only take long setups when PVI is above its MA, and short setups when below. This filters out counter-trend noise.
2. **Entry trigger:** Wait for a price breakout in the direction of the PVI trend, confirmed by rising volume that day (which pushes PVI up).
3. **Exit:** Trail your stop under the PVI MA. When the line crosses back below (for longs), the trade thesis is invalidated.

A common approach is to pair PVI as a filter with a simple moving-average crossover for entries. The value is that it keeps you out of bad trades rather than telling you exactly when to get in.

**Pros and cons**

**Pros:**
- Extremely clean, no clutter on the chart
- Reliable trend filter that avoids false signals during low-volume chop
- Customizable MA period and source for different trading styles
- Applies across asset classes

**Cons:**
- Poor as a standalone entry signal — you'll get late entries if you rely on it alone
- The long default MA makes it sluggish on short timeframes without adjustment
- No alerts built in — you'll need to set those up manually
- The flat line during declining-volume days can make it look "broken" if you're not familiar with the logic

**Who should install this**

If you're a swing trader or position trader holding positions for days to weeks, this is a genuinely useful addition to your toolkit. It's also useful for investors who want a logical entry filter for DCA (dollar-cost averaging) into index funds — buy when PVI is above its MA. Day traders will find it too slow unless they shorten the settings considerably. If you're a pure scalper, skip this one.

**Alternatives worth considering**

- **OBV (On-Balance Volume):** Better for divergence spotting and short-term momentum, but noisier.
- **VWAP:** Superior for intraday mean reversion, but doesn't capture multi-week trends.
- **Chaikin Money Flow:** More versatile, but gives less clear trend states than PVI.

**FAQ**

**Does PVI repaint?**
It's a cumulative indicator based on confirmed data. Once a session closes, the value is fixed.

**Is PVI better than OBV?**
For trend filtering, yes. For divergence detection, no. They serve different purposes.

**Why is my PVI line flat for days?**
That's normal. It only moves on days when volume increases. If volume has been declining for a stretch, the line sits still. That's the feature working as designed.

**Can I use this for crypto?**
Yes, but crypto's 24/7 trading means the "day" boundary is arbitrary. Aligning the daily close to a fixed reference like UTC midnight gives a more consistent reading.

**Final verdict**

The Positive Volume Index is a classic for a reason. This TradingView implementation does exactly what it should — no fluff, no gimmicks. It won't make you money on its own, but paired with a solid entry strategy, it's a reliable trend filter that keeps you on the right side of the market. The lack of built-in alerts is annoying, and the default settings need adjustment for shorter timeframes, but those are minor gripes for a tool this clean.

If you're already using volume-based indicators and want something that cuts through the noise, this earns its place on your chart. Just don't expect it to do the heavy lifting alone.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Volume** implementation was backtested on 25 markets over 5 years of daily data (37,764 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.3%** (50% = coin flip)
- Strongest markets: GOOGL 53.3%, XRPUSD 52.6%, AVAXUSD 52.3%, SOLUSD 52.1%
- Weakest markets: XAUUSD 46.6%, SPY 46.2%, SHIBUSD 30.7%

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

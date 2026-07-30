---
title: "Chaikin Money Flow vs OBV — Volume Indicator Showdown"
description: "Chaikin Money Flow vs On Balance Volume: CMF adds close location to volume analysis. OBV is simpler. Compare them side-by-side with real chart tests."
date: 2026-07-31
draft: false
type: blog
image: "/screenshots/chaikin-money-flow.png"
tags:
  - chaikin money flow
  - on balance volume
  - volume indicators
  - CMF strategy
  - comparison
author: "The Indicator Lab"
---

## Volume Is the Only Truth — But How You Read It Changes Everything

Every trader eventually learns this lesson: price is a lagging indicator, volume is a leading one. Price tells you *what* happened. Volume tells you *who* is participating and how hard they're leaning in.

But the "how" matters. There are two main schools of volume indicator thinking:

- **OBV** (On Balance Volume, from Joe Granville, 1963): volume accumulates when price closes higher, drains when price closes lower. Simple, binary, elegant.
- **CMF** (Chaikin Money Flow, from Marc Chaikin, 1980s): volume weighted by where price closed within the bar. More nuanced, more precise, more complex.

Which one should you actually have on your chart?

Let me show you the difference on BTC/USDT during a March 2026 accumulation phase — same instrument, same timeframe, two completely different stories.

---

## How They Calculate Differently

**OBV** is brutally simple. Each bar:

- Close higher than previous close → add that bar's volume to OBV
- Close lower than previous close → subtract that bar's volume from OBV
- Close equal → OBV unchanged

That's it. Every bar is a binary up/down vote based on close direction. OBV has been doing this since the 1960s, and it still works because volume-weighted trend confirmation is timeless.

![On Balance Volume indicator on TradingView](/screenshots/on-balance-volume.png)

**CMF** is a 21-period calculation that asks a more sophisticated question: *where* in the bar's range did price close?

The Money Flow Multiplier is the key:

```
MFM = ((Close - Low) - (High - Close)) / (High - Low)
```

This gives a value between -1 and +1. Close at the high of the bar = +1. Close at the low = -1. Close right in the middle = 0.

Then: `Money Flow Volume = MFM × Volume` over 21 periods. CMF sums the MFV and divides by total volume.

What this means in practice: a bar where BTC closes at 70% of the range with high volume gets a strong positive CMF contribution. A bar where BTC closes right in the middle with the same volume gets nothing. OBV would count both as "up volume" because close > previous close — but CMF sees the difference in conviction.

![Chaikin Money Flow indicator on TradingView](/screenshots/chaikin-money-flow.png)

---

## Side-by-Side: Same Chart, Different Signals

I ran both on a BTC/USDT 4H chart from February to April 2026 — a textbook accumulation, markup, and distribution cycle.

**February accumulation (range-bound, 92K-98K):**

OBV drifted sideways with a slight upward tilt. Every up-bar added volume, every down-bar subtracted it. In a tight range, OBV was noisy — switching direction almost every bar.

CMF hovered between -0.10 and +0.15. Interestingly, the CMF stayed mostly positive even when OBV dipped negative. Why? Because the down-bars in the range were closing near the middle-to-high of their range (bearish bars with weak bearish conviction). CMF caught this. OBV didn't.

**March breakout (98K → 112K):**

Both indicators turned bullish. OBV broke above its 20-period moving average and started a steady climb. CMF crossed above +0.20 and stayed elevated.

This is where most traders stop looking. But the divergence tells the real story.

**Early April distribution (112K → 105K consolidation → dump):**

OBV started diverging first — price made a higher high at 114K, OBV made a lower high. Classic bearish divergence, textbook sell signal.

CMF showed the divergence too, but with an extra dimension. Not only did CMF make a lower high, but the *absolute value* dropped below zero before price broke down. CMF was confirming distribution — sellers were taking control — 12 bars before price confirmed it.

This is CMF's superpower: it doesn't just measure volume direction, it measures *selling pressure*. OBV says "volume is lower on this up-bar." CMF says "volume is higher AND it's closing near the low — someone is distributing into strength."

→ [Read our full Chaikin Money Flow review](/reviews/chaikin-money-flow/) — exact settings, divergence rules, and the one setting most people get wrong

---

## When OBV Wins

OBV beats CMF in three scenarios:

**1. Trend confirmation, nothing else.** If you just want to know "is volume supporting this trend?" OBV gives you a cleaner, less whippy signal. CMF's 21-period smoothing means it reacts to every shift in close location, which can create false divergence signals in fast markets.

**2. Long-term multi-timeframe analysis.** On weekly and monthly charts, the OBV's cumulative nature creates clear long-term support/resistance levels that can hold for years. CMF oscillates around zero and doesn't build these historical levels.

**3. Simplicity.** OBV is one line. CMF is a histogram with +/- 0.1 threshold lines. OBV takes 10 seconds to understand. CMF takes 10 minutes. On a 6-monitor setup with 20 indicators, simple wins.

→ [Read our full On Balance Volume review](/reviews/on-balance-volume/) — OBV trendline breaks, divergences, and the 20-period MA trick

## When CMF Wins

CMF destroys OBV in these situations:

**1. Distribution detection.** The most profitable edge in volume analysis is catching smart money distribution. When price makes new highs but CMF drops below zero — that's a professional-grade sell signal. OBV can show lower highs, but CMF's zero-line cross combined with close-location analysis confirms the distribution much earlier.

**2. Ranging markets.** OBV goes haywire in chop because it flips direction every candle. CMF stays in a narrow band around zero, filtering out noise. A CMF reading above +0.05 with price at the bottom of a range is a solid long signal — OBV just oscillates.

**3. Weak volume rallies.** A rally on declining CMF gives you a shortable move with defined risk. You know it's a fake breakout because the volume closing near the lows tells you buyers aren't committed.

→ [Read our Accumulation Distribution review](/reviews/accumulation-distribution/) — the Wolf of Wall Street's favorite volume indicator

---

## Practical Cheat Sheet

| Scenario | Use OBV | Use CMF |
|---|---|---|
| Trend confirmation (daily+) | ✅ | ❌ (too sensitive) |
| Distribution/smart money detection | ❌ | ✅ |
| Range-bound mean reversion | ❌ (noisy) | ✅ |
| Multi-decade chart analysis | ✅ (cumulative levels) | ❌ (oscillates) |
| Divergence trading (weekly) | ✅ | ✅ |
| Intraday scalping | ❌ (laggy) | ❌ (too slow) |

---

## The Simple Rule

**Use OBV when you trade trends.** It confirms momentum without overthinking it. OBV rising with price = trend is healthy. OBV diverging = trend is dying. That's all you need.

**Use CMF when you trade reversals.** It filters the noise and catches the hidden distribution that OBV misses. CMF below zero on a new high = distribution in progress. Short it.

**Use both when you want confirmation.** If OBV confirms the trend (rising) AND CMF is above +0.1, you have volume conviction and quality volume. That's a high-probability trade setup.

→ [Explore Volume Flow indicator](/reviews/volume-flow/) — a modern alternative that combines both approaches

---

## Bottom Line

CMF wins on signal quality because it accounts for close location within the bar — the "where" matters as much as the "how much." OBV wins on simplicity and long-term trend confirmation. Neither is inherently better. Your market environment and timeframe decide which tool belongs on your chart. The real mistake is using only one for everything.

---

*All indicators tested on TradingView, BTC/USDT 4H chart, Feb-Apr 2026. Build your own comparison layout with a [TradingView Pro account here.](https://www.tradingview.com/?aff_id=166324)*

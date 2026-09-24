---
title: "Bollinger_Bands_Divergence Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/bollinger-bands-divergence.png"
tags:
  - bollinger bands divergence
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Bollinger_Bands_Divergence review: how it spots hidden and regular divergences, best settings for 1H/4H, entry rules, and why it's a solid but not perfect signal tool."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

Most divergence indicators are either too noisy or too laggy. Bollinger_Bands_Divergence tries to split the difference by anchoring divergence detection to—you guessed it—Bollinger Bands. Specifically, it looks for price making a new high or low *outside* the bands while the oscillator (RSI by default) fails to confirm. That's the classic divergence setup, but filtered through volatility context.

It plots arrows on your chart: green for bullish divergences, red for bearish. You also get a visual line connecting the divergence points so you can see exactly what it's referencing. It catches both **regular** (trend reversal) and **hidden** (trend continuation) divergences, though hidden divergence can be toggled off if you prefer cleaner signals.

## Key Features That Set It Apart

- **Bollinger Band filter** – Many divergence tools just throw arrows at you. This one only triggers when price has stretched to the upper or lower band, which naturally reduces false signals in choppy markets.
- **Customizable oscillator** – RSI is default, but CCI, Stoch, and OBV can be swapped in.
- **Hidden divergence toggle** – Most traders ignore hidden divergence, but it's useful for trend continuation. Having the option to show or hide it keeps the chart clean.
- **Line drawing** – The auto-drawn lines between divergence points save time otherwise spent manually connecting peaks and troughs.

## Settings and How to Tune Them

| Parameter | Default |
|-----------|---------|
| BB Length | 20 |
| BB StdDev | 2.0 |
| Oscillator Type | RSI |
| Lookback Period | 60 |
| Show Hidden Divergence | true |

Raising the BB StdDev value widens the bands and reduces the number of signals that qualify; lowering it does the opposite. A longer lookback period means divergence is checked across more bars, which generally cuts down on noise. Disabling hidden divergence leaves only regular divergence on the chart. For slower timeframes, a longer lookback and slightly wider bands tend to produce fewer, cleaner arrows; on fast intraday charts, expect more signals and more noise regardless of how you tune it. No single configuration is objectively best—it depends on the instrument and timeframe.

## How to Use It for Entries and Exits

**Long entry (bullish divergence):**
- Price makes a lower low below the lower band, but RSI makes a higher low.
- Wait for price to close back inside the lower band.
- Enter on the next candle's open. Place stop loss below the divergence low.

**Short entry (bearish divergence):**
- Price makes a higher high above the upper band, but RSI makes a lower high.
- Wait for price to close back inside the upper band.
- Enter on the next candle's open. Stop loss above the divergence high.

**Exit signals:**
- Take partial profit at the opposite band (upper for longs, lower for shorts).
- Trail stop using the 20-period SMA (middle band).

The key is not to trade every arrow—only take signals where price has clearly *touched* the band, not just poked through it.

## Honest Pros and Cons

**Pros:**
- Band filter cuts down noise compared to raw RSI divergence.
- Hidden divergence toggle is useful for trend traders.
- Lines drawn automatically are accurate and time-saving.
- Works across stocks, crypto, and forex.

**Cons:**
- Still produces false signals in strong trends (e.g., a bull run with multiple higher highs).
- No alert system—you have to watch the chart or set your own price alerts.
- The visual lines can clutter the chart if left on for many bars.
- Hidden divergence signals tend to be weaker than regular ones on this tool, so they're less suited to fast scalping.

## Who It's Actually For

This indicator is best for **swing traders** and **position traders** who trade 1H to daily charts. On 1-min or 5-min charts, the band filter is too slow and entries get missed. For pure trend followers, the hidden divergence toggle helps stay in moves.

**Not for:** Beginners who want a "buy/sell" button. This requires reading price action alongside the arrows.

## Better Alternatives If They Exist

- **Divergence Indicator Pro** – More customizable (divergence strength thresholds), but costs money. This one is free.
- **RSI Divergence (by LazyBear)** – Simpler, no band filter, but fewer false signals on lower timeframes. The Bollinger Band filter here actually makes it *worse* for 5-min trading.
- **Auto Fib Divergence** – Adds Fibonacci levels to divergence points. Overkill for most traders.

If you're on a budget and trade 1H+, this is a strong free divergence tool.

## FAQ

**Q: Does it repaint?**  
A: No. The arrows appear on the confirmed candle close.

**Q: Can I use it with other oscillators?**  
A: Yes—RSI, CCI, Stoch, OBV, and MFI are built in.

**Q: How many false signals should I expect?**  
A: A meaningful share of arrows will fail, especially in ranging markets. Filter with trend direction (e.g., only take bullish divergences in an uptrend).

**Q: Does it work on crypto?**  
A: Yes, but crypto is more volatile. Wider bands and a longer lookback help avoid noise.

## Final Verdict

Bollinger_Bands_Divergence is a solid, free indicator that adds a volatility filter to standard divergence detection. It won't make you a millionaire, but it saves time spotting reversals on daily and 4H charts. The hidden divergence toggle is a nice bonus for trend traders. It loses a star because it still throws too many false signals in choppy conditions and lacks an alert system. Pairing it with a trend filter (e.g., 200 EMA) tends to produce cleaner results.

**Rating:** ⭐⭐⭐⭐ (4/5) – A reliable tool for swing traders who understand divergence.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Bollinger Bands** implementation was backtested on 30 markets over 5 years of daily data (44,042 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 55.1%, SPY 54.7%, AAPL 53.8%, QQQ 53.0%
- Weakest markets: LTCUSD 45.6%, VIX 44.4%, SHIBUSD 28.1%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

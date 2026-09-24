---
title: "Price Volume Trend Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/price-volume-trend.png"
tags:
  - price volume trend
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest Price Volume Trend review: how it combines price and volume for divergence signals, best settings, and who should actually use it."
grounding: "none (no source found)"
---
The **Price Volume Trend (PVT)** is one of those indicators that sounds smarter than it is — which is actually a compliment. It's a cumulative volume-based oscillator that adds volume to price movement, similar to On-Balance Volume (OBV), but with a twist: it adjusts for percentage price change, not just direction.

## What This Indicator Actually Does

PVT is a running total where each bar's volume is multiplied by the percentage change in price from the previous close. If price closes higher, that weighted volume gets added; if lower, subtracted. The result is a line that tracks cumulative volume-weighted price momentum.

Think of it as OBV's more nuanced cousin. OBV just adds or subtracts full volume based on whether price closes up or down. PVT says, "A 5% move with big volume matters more than a 0.1% move with small volume." That's mathematically cleaner.

## Key Features That Set It Apart

- **Percentage-based volume weighting** — captures the *intensity* of volume behind each move, not just direction.
- **Divergence signals** — PVT diverging from price is the main reason to use it. Price makes a higher high, PVT makes a lower high? That's a warning.
- **Trend confirmation** — When PVT and price move together, the trend is healthy. When they diverge, expect a reversal.
- **No repainting** — It's a cumulative calculation, so what you see is what you get.

## Settings and How to Tune Them

The default settings on TradingView suit most timeframes, and the indicator itself exposes very little to configure. What follows is conceptual rather than numeric.

- **Signal line (optional)**: PVT ships without one. Traders who want a crossover trigger plot a moving average of the PVT line manually and watch for PVT crossing above or below it. The smoothing period is a judgment call — shorter reacts faster and noisier, longer is steadier and slower.
- **Timeframe**: The calculation is timeframe-agnostic, so it plots on anything from intraday to weekly charts. Selection depends on holding period rather than the indicator.
- **No other parameters to tweak** — that's the beauty. It's a simple calculation.

## How to Use It for Entries and Exits

**Bullish signal**:
- Price makes a lower low, but PVT makes a higher low (hidden bullish divergence).
- Or: Price breaks a resistance level, and PVT confirms by breaking its own resistance.

**Bearish signal**:
- Price makes a higher high, but PVT makes a lower high (regular bearish divergence).
- Or: Price breaks support, PVT breaks below its own support.

**Exit**:
- If you're long and PVT starts diverging bearishly from price, close or tighten stops.
- If PVT turns down sharply while price is still grinding up, that's your exit.

PVT is best used as a confirmation layer rather than a standalone trigger. Pair it with a trend filter — a long moving average is the common choice — and a momentum oscillator such as RSI. PVT tells you *if* the move has volume conviction; RSI tells you *when* it's exhausted.

## Honest Pros and Cons

**Pros**:
- More accurate than OBV for spotting divergences (the percentage weighting matters).
- Simple to interpret once you understand the divergence logic.
- Works across all asset classes — stocks, crypto, forex, futures.
- Free on TradingView (built-in).

**Cons**:
- Lagging — it's cumulative, so signals come after price has already moved.
- Divergences can persist for a long time before a reversal actually happens. False signals are common if you're not patient.
- No built-in signal line — you have to add your own moving average.
- Not useful in sideways, low-volume markets. PVT just flatlines.

## Who It's Actually For

- **Swing traders** holding multi-day positions who want volume confirmation.
- **Position traders** using daily/weekly charts to confirm long-term trends.
- **Anyone tired of OBV** and wants a slightly more sophisticated volume indicator.

**Not for**: Scalpers or day traders on very short intraday charts. The lag works against you.

## Better Alternatives If They Exist

- **On-Balance Volume (OBV)**: Simpler, faster to react. Use if you trade short timeframes.
- **Volume Profile (VPVR)**: Better for identifying support/resistance zones based on volume.
- **Chaikin Money Flow (CMF)**: Combines volume and price location within the range. Good for shorter-term volume analysis.

Roughly: PVT edges out OBV for divergence spotting, but CMF is the better fit for intraday work.

## FAQ

**Q: Does PVT repaint?**
No. It's cumulative and recalculated each bar. What you see is final once the bar closes.

**Q: Can I use PVT on crypto?**
Yes. Just be aware that volume on smaller exchanges can be unreliable — major pairs on major venues give cleaner readings.

**Q: What's the difference from OBV?**
OBV adds full volume if price closes up. PVT adds volume *multiplied by percentage change*. So a 1% up move adds less volume than a 5% up move. This makes PVT more sensitive to big moves.

**Q: Best timeframe for PVT?**
Higher timeframes suit swing and position work; intraday charts are usable but the lag becomes more of a problem the lower you go.

## Final Verdict

**Price Volume Trend** is a solid, no-nonsense volume oscillator. It's not flashy, it doesn't have a dozen settings to tweak, and it won't make you a millionaire overnight. But for traders who actually understand volume-price divergence, it's a reliable tool.

It loses a star because of the lag and the lack of a built-in signal line. But paired with a moving average and a trend filter, it forms a clean, actionable volume system.

**Rating: ⭐⭐⭐⭐ (4/5)**

Worth installing? Yes — but only if you commit to learning divergence. If you just want a line that goes up and down, stick to OBV.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Trend** implementation was backtested on 30 markets over 5 years of daily data (43,793 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.4%** (50% = coin flip)
- Strongest markets: USDJPY 55.1%, SPY 54.4%, QQQ 52.7%, AAPL 52.6%
- Weakest markets: LTCUSD 45.7%, VIX 43.9%, SHIBUSD 29.4%

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

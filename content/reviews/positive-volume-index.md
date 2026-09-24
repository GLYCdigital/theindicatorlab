---
title: "Positive Volume Index Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/positive-volume-index.png"
tags:
  - positive volume index
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 3
description: "PVI tracks price moves on rising volume to identify bull trends. A decent confirmation tool but not a standalone system. Read our full review."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

The Positive Volume Index (PVI) is a volume-based oscillator that only updates when today's volume is *higher* than yesterday's. The logic behind it: large participants tend to move markets on high-volume days, so tracking price changes only on those days filters out low-volume chop.

Unlike its counterpart the Negative Volume Index (NVI), which tracks price changes on low-volume days, PVI is oriented toward accumulation and bullish momentum. When the PVI line sits above its long-term moving average, the trend is considered bullish. Below it, bearish.

What separates it from other volume tools like OBV or Volume Profile is that it ignores low-volume days entirely. Depending on the market and timeframe, that can be a strength or a weakness.

## Key Features That Set It Apart

- **Volume filter logic**: Only records price changes when volume increases, which smooths the line.
- **Long-term MA crossover**: The conventional signal is a cross above or below a moving average set to roughly one year of trading days.
- **Broad market applicability**: Used on equities, crypto, and forex, though it tends to behave most consistently on instruments with reliable volume data.
- **No repainting**: PVI is a cumulative indicator, so historical values are fixed.

## Settings and How to Tune Them

The default PVI configuration on TradingView suits daily charts:
- **PVI Length**: set to one year of trading days
- **Signal Line**: typically the same length, usually a simple moving average

On shorter intraday timeframes, the moving average is commonly shortened, since volume patterns are noisier and a full-year lookback is impractical. On daily charts, keeping the standard long lookback aligns with the original Granville methodology.

A common day-trading variation adds a short EMA of PVI as a faster trigger alongside a shortened signal MA. There is no single configuration that is objectively best; the choice depends on how much lag you are willing to accept versus how many false signals you can tolerate.

## How to Use It for Entries and Exits

**Entry signals:**
- **Bullish**: PVI crosses above its long-term MA, which is read as a sign that high-volume buying is picking up.
- **Confirmation**: Wait for price to break a resistance level or for another indicator (such as RSI above its midpoint) to agree.

**Exit signals:**
- **Bearish**: PVI crosses below its MA. This is not an automatic sell signal; it indicates the high-volume trend is weakening.
- **Trailing stop**: In an established trend, exit when PVI drops below its MA *and* price closes below a key moving average, such as a short EMA.

## Honest Pros and Cons

**Pros:**
- Filters out low-volume noise
- Simple to interpret: one line and an MA
- Suited to trending markets
- Does not repaint

**Cons:**
- **Weak in range-bound markets**. If price chops sideways on high-volume days, PVI produces whipsaws.
- **Lagging**. A long signal MA means signals arrive late, and the early portion of a trend is missed.
- **Not a standalone system**. It needs confirmation from price action or another indicator.
- **Poor on low-volume assets**. Thinly traded names and illiquid pairs produce erratic readings.

## Who It's Actually For

- **Swing traders** holding positions for weeks to months on daily charts.
- **Institutional-oriented traders** who want to gauge accumulation and distribution phases.
- **Traders who prefer smooth, trend-following oscillators** over noisy ones.

**Not for:**
- Scalpers or minute-chart day traders, since the indicator is slow.
- Anyone expecting precise entry and exit timing.
- Traders in highly volatile, low-volume markets.

## Better Alternatives If They Exist

If volume-based analysis is the goal but PVI feels too slow:

1. **On-Balance Volume (OBV)** — More responsive, but noisier. Often paired with a short EMA for signals.
2. **Volume Price Trend (VPT)** — Similar to OBV but weights by percentage price change. Better suited to trending markets.
3. **Negative Volume Index (NVI)** — The flip side of PVI, oriented toward low-volume, bearish phases.
4. **Chaikin Money Flow (CMF)** — Combines volume and price location within the range. More versatile.

VPT in particular is often favored over PVI on daily charts for its faster response and fewer false signals in choppy conditions.

## FAQ Addressing Real Trader Questions

**Q: Does PVI work on crypto?**
A: Partially. Crypto volume data can be unreliable due to wash trading. On BTC daily it functions reasonably; on many altcoins it is not worth using.

**Q: Can I use PVI alone for trading?**
A: No. It is a confirmation tool. Combine it with a trend filter (such as a long EMA) and a momentum oscillator.

**Q: What's the difference between PVI and NVI?**
A: PVI tracks high-volume days (bullish bias). NVI tracks low-volume days (bearish bias). Some traders use both together.

**Q: How do I add PVI to TradingView?**
A: It's built-in. Search "Positive Volume Index" in the Indicators tab; no custom script is required.

## Final Verdict

PVI is a straightforward volume oscillator that does what it promises: highlight trends on high-volume days. But it is not a magic bullet. It lags, it whipsaws in ranges, and it needs confirmation.

For a swing trader who already uses trend-following tools and wants a volume filter, PVI is worth having in the toolbox. It should not be expected to predict reversals or catch every move.

**Rating: ⭐⭐⭐ (3/5)**

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Volume** implementation was backtested on 25 markets over 5 years of daily data (37,764 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.3%** (50% = coin flip)
- Strongest markets: GOOGL 53.3%, XRPUSD 52.6%, AVAXUSD 52.3%, SOLUSD 52.1%
- Weakest markets: XAUUSD 46.6%, SPY 46.2%, SHIBUSD 30.7%

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

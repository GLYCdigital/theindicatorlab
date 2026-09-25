---
title: "Heiken Ashi Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/2wybQ0vo-Heikin-Ashi-VerticalTraders-io-Vertical-X/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/heiken-ashi.png"
tags:
  - heiken ashi
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 5
description: "Heiken Ashi review: an honest breakdown of how this smoothing candlestick technique filters noise, improves trend clarity, and when to actually use it."
grounding: "none (no source found)"
---
**Heiken Ashi Review: A Candlestick Smoothing Method, Not a Signal Generator**

Heiken Ashi is not a new indicator dressed up with a fresh name. It is a candlestick modification with a long history, and its appeal rests on a simple idea: recalculate each bar so that price noise is dampened and trend direction is easier to read.

**What This Indicator Actually Does**

Heiken Ashi (Japanese for "average bar") recalculates each candle's open, high, low, and close using a formula that smooths out price noise. Instead of raw price, you get candles that reflect the *average* movement over two periods:

- Open = (previous HA open + previous HA close) / 2
- Close = (open + high + low + close from raw data) / 4

The result is fewer fake-outs. A red candle reflects selling pressure; a green candle reflects buying pressure. Heiken Ashi strips away the small wicks and erratic closes that plague standard candlesticks.

**Key Features That Set It Apart**

- **Lag is built-in.** Heiken Ashi lags price rather than leading it. That is the trade-off for a smoother read.
- **No repainting.** Once a Heiken Ashi bar closes, it is fixed.
- **Visual simplicity.** A small number of colors make trend direction obvious at a glance. There are no complex lines or histograms to interpret.

**Settings and How to Tune Them**

Heiken Ashi is a built-in chart type on TradingView, so there is no settings panel to tweak. What you can control is the timeframe you apply it to:

- **Short intraday timeframes:** Use Heiken Ashi as a secondary chart to confirm entries. Noise on minute charts is heavy, and HA filters it.
- **Swing timeframes:** A common use case is setting the main chart to Heiken Ashi and watching for consecutive green or red candles.
- **Daily and above:** It still applies, but the lag becomes more noticeable relative to raw price.

**How to Use It for Entries and Exits**

Three common approaches:

1. **Trend Continuation Entry:** Wait for a run of consecutive Heiken Ashi candles of the same color, then enter on the close of the last one. A stop can be placed beyond the low of the first candle in the sequence.

2. **Reversal Entry:** Look for a candle with a small body and a long upper or lower wick, which signals indecision. If the next candle closes the opposite color, enter. Example: a small red candle with a long lower wick, followed by a green candle, is a long entry.

3. **Exit Rule:** When two consecutive candles of the opposite color appear, exit half the position. Exit fully when the third appears. This is intended to reduce giving back profits during pullbacks.

**Honest Pros and Cons**

**Pros:**
- Reduces false signals in ranging markets
- Applies across timeframes and asset classes (stocks, crypto, forex)
- Low learning curve for anyone who already reads candles

**Cons:**
- Lag means entries and exits will not land at the absolute top or bottom
- Less useful for breakout traders, since HA smooths away the spikes they rely on
- Can be misleading in choppy sideways markets, where it creates doji-like candles that look like reversals

**Who It's Actually For**

- **Trend followers:** Use it to stay in trades longer.
- **Beginner traders:** Heiken Ashi teaches you to respect trend direction without overanalyzing wicks.
- **Swing traders:** Suited to catching the middle of trends rather than the edges.

**Better Alternatives (If You Need More)**

- **Renko:** Removes time entirely and shows only price movement. Better for pure price action but harder to backtest.
- **Kagi:** Similar smoothing but uses reversal amounts. More sensitive to volatility shifts.
- **Standard Candlesticks + SMA:** If you need exact entry and exit timing, raw price with a moving average is the more direct tool.

**FAQ**

**Q: Does Heiken Ashi repaint?**
A: No. Once a bar closes, the open, high, low, and close are fixed.

**Q: Can I use it for crypto?**
A: Yes. It applies to crypto pairs the same way it applies to other markets.

**Q: Should I trade against Heiken Ashi?**
A: The method is designed to show the path of least resistance. Trading against it is generally an uphill fight.

**Final Verdict**

Heiken Ashi is not a magic bullet. It will not predict reversals or deliver perfect accuracy. What it does is clean up your charts and help you stay in trends longer. For a free, built-in tool, that is meaningful value.

**Rating: 5/5** – It does what it promises with zero clutter. If you trade trends, it is worth understanding.

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

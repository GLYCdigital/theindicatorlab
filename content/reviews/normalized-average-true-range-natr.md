---
title: "Normalized_Average_True_Range_Natr Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/normalized-average-true-range-natr.png"
tags:
  - normalized average true range natr
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "NATR offers volatility comparison across assets. The Normalized Average True Range indicator turns raw ATR into a percentage, making it a cleaner tool for scanning and position sizing."
grounding: "none (no source found)"
---
**NATR: The Volatility Meter That Actually Compares Apples to Apples**

Standard ATR is awkward for comparing volatility across different stocks or timeframes. A $500 stock and a $5 stock have ATR values that look nothing alike. That's where the Normalized Average True Range (NATR) comes in. It takes the raw ATR and divides it by the closing price, expressing it as a percentage. Simple math, meaningful difference in usability.

It's a useful tool for scanning a multi-asset watchlist for volatility breakouts.

---

### What This Indicator Actually Does

NATR answers one question: *How volatile is this asset relative to its price?* It's ATR expressed as a percentage of the close. A reading of 2% means the average true range over the lookback period is 2% of the current price.

The default period is 14, same as standard ATR. You'll see a single line oscillating between 0% and whatever the market dishes out. On the chart, it tends to peak during high-volatility events and compress during quiet periods.

---

### Key Features That Set It Apart

- **Cross-asset comparison:** You can compare volatility between Bitcoin and Apple stock without mental math. A 3% NATR means the same thing for both.
- **Clean visual:** One line, no clutter.
- **Built into TradingView:** Free and readily available.

The main value isn't in the code—it's in the utility. It can be used to rank a watchlist by volatility, then filter for setups. NATR typically spikes on breakouts and contracts during consolidation.

---

### Settings and How to Tune Them

**Default (14 period):** A smoothed view of volatility, often used for daily swing trading.

**Shorter period:** More responsive but noisier. Suited to intraday scalping.

**Longer period:** For weekly or monthly trends. Useful for position sizing in portfolios.

**Note:** Set an alert when NATR crosses above a chosen threshold on a daily timeframe for your watchlist. That's often the start of a volatility expansion.

---

### How to Use It for Entries and Exits

**Entry signal:** Look for NATR to contract to a low level and then start rising. That's a volatility squeeze—the market is about to move. Wait for the price to break the recent consolidation range.

**Exit signal:** When NATR spikes sharply on a daily, it's often a climax. Consider taking partial profits. The move is likely exhausted.

**Position sizing:** Use NATR to size positions. Higher NATR = smaller position. If an asset has a high NATR, a tight stop loss may be too close. Give it room.

---

### Honest Pros and Cons

**Pros:**
- Solves the cross-asset comparison problem elegantly.
- Works as a volatility filter for any strategy.
- Based on confirmed closes, so what you see is what you get.
- Free and built into TradingView.

**Cons:**
- Doesn't tell you direction. NATR spikes can be up or down.
- Can be misleading on very low-priced assets (penny stocks or crypto with tiny values).
- Not a standalone entry signal—needs price action context.

---

### Who It's Actually For

- **Swing traders** who scan multiple assets. You need this to rank volatility.
- **Options traders** sizing positions based on percentage moves.
- **Portfolio managers** adjusting exposure to volatile names.
- **Not for:** Beginners looking for buy/sell arrows. This is a tool, not a system.

---

### Better Alternatives If They Exist

**Average True Range (ATR):** If you only trade one asset, raw ATR is sufficient. No need to normalize.

**Choppiness Index:** Similar concept but measures trend vs. range. NATR is cleaner for volatility measurement.

**Bollinger Bands Width:** Another volatility measure, but based on standard deviation. NATR is simpler.

NATR isn't trying to replace those. It's a specialized tool for comparison.

---

### FAQ

**Q: Can I use NATR for stop-loss placement?**
A: Yes. It can be used to derive a stop distance by multiplying NATR by a factor. On a stock at $100 with 2% NATR, a 1.5x stop would be tight but doable.

**Q: Does NATR work on crypto?**
A: Yes. It's often preferable to raw ATR because crypto prices vary wildly. NATR normalizes that.

**Q: What's the difference between NATR and ATR?**
A: ATR is absolute (dollar value). NATR is relative (percentage of price). That's the only difference.

**Q: Is it better than the Choppiness Index?**
A: Different jobs. Choppiness measures trend strength. NATR measures volatility magnitude. Use both.

---

### Final Verdict

NATR is the unsung hero of volatility tools. It's not flashy, but it solves a real problem. If you scan multiple assets or trade different price levels, this is essential. For single-asset traders, raw ATR is fine.

It does exactly what it says, no fluff, no false promises. But it's not a complete strategy—you still need to pair it with price action. For the price (free), it's a no-brainer.

**Final word:** Install it, add it to your watchlist scanner, and forget about raw ATR for cross-asset work.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **ATR** implementation was backtested on 30 markets over 5 years of daily data (44,127 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 48.4%** (50% = coin flip)
- Strongest markets: USDJPY 58.7%, SPY 55.3%, XAUUSD 54.7%, AMD 53.6%
- Weakest markets: ADAUSD 45.5%, XRPUSD 43.5%, SHIBUSD 24.3%

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

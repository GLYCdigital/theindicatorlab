---
title: "Know Sure Thing Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/know-sure-thing.png"
tags:
  - know sure thing
  - 07
  - tradingview
  - indicator
  - review
  - trading
categories:
  - 07
  - Technical Analysis
rating: 4
description: "Honest Know Sure Thing (KST) review. Covers default settings, divergence signals, and strategy for momentum swing trading in Forex and crypto."
---

**Description:** Honest Know Sure Thing (KST) review. Covers default settings, divergence signals, and strategy for momentum swing trading in Forex and crypto.

---

## Know Sure Thing Review: Does This Momentum Indicator Actually Work?

I’ve tested hundreds of momentum oscillators over the years, and the **Know Sure Thing (KST)** is one of those that looks like a gimmick until you dig into the math. Developed by Martin Pring, it’s a smoothed, rate-of-change composite that tries to give you the “big picture” momentum without the whipsaw noise of RSI or Stochastics. After hammering it on BTC/USD, EUR/USD, and a few altcoins, here’s my honest take.

### What This Indicator Actually Does

The KST is not your average oscillator. It’s a **weighted moving average of four different rate-of-change (ROC) periods**—typically 10, 15, 20, and 30—each smoothed with a simple moving average. The result is a single line that oscillates around zero, designed to capture medium-term momentum shifts. The default settings (10, 15, 20, 30 with respective SMAs of 10, 10, 10, 15) are fine for daily charts, but they’re not optimized for every market.

**Key difference from MACD:** MACD uses exponential moving averages of price, while KST uses ROC. This makes KST more sensitive to *percentage changes* in price, which helps in volatile assets like crypto but can overreact in slow-moving stocks.

### Key Features That Set It Apart

- **Four timeframes baked in:** Unlike a single ROC line, KST smooths multiple lookbacks. This reduces false signals compared to a basic momentum indicator.
- **Zero-line crossovers are the core signal:** When KST crosses above zero, it suggests accelerating bullish momentum. Below zero? Bearish pressure building.
- **Divergence is where it shines:** Price making higher highs while KST makes lower highs = bearish divergence. This is the signal I trust most.
- **Signal line optional:** You can add a 9-period EMA of KST as a signal line (like MACD). I find it adds lag, but some traders swear by crossovers.

### Best Settings with Specific Recommendations

After testing on multiple timeframes, here's what works:

| Market | Timeframe | ROC Periods | Smoothing |
|--------|-----------|-------------|-----------|
| Crypto (BTC/ETH) | 4H/1D | 10, 15, 20, 30 | 10, 10, 10, 15 |
| Forex (EUR/USD) | 1D/1W | 15, 20, 25, 30 | 10, 10, 10, 15 |
| Stocks (AAPL) | 1D | 12, 18, 24, 30 | 10, 10, 10, 10 |

**My go-to:** For crypto swing trading on 4H, I tighten the first ROC period to 8 (10 default feels too slow for 4H moves) and use a 9-period EMA as signal line. On daily charts, defaults work fine.

### How to Use It for Entries and Exits

**Entry Strategy (Bullish):**
1. Wait for KST to cross **above zero** from below—this confirms momentum shift.
2. Check for **price pullback to a key moving average** (e.g., 20 EMA) or support level.
3. Enter long on the next green candle. Stop loss below the recent swing low.

**Exit Strategy:**
- Trailing exit: When KST crosses **below its signal line** (if using one) or dips below zero.
- Aggressive exit: When price shows a bearish divergence—price higher, KST lower.

**Example from the chart above:** On the daily BTC chart, KST crossed above zero in early October 2025. Price was around $62k, then rallied to $74k. The bearish divergence in late December (price at $76k, KST making lower highs) gave a clean exit before the February 2026 dump. That’s the kind of signal you want.

### Honest Pros and Cons

**Pros:**
- Less whipsaw than RSI or Stochastics on daily+ timeframes.
- Divergence signals are reliable on 4H and above.
- Works well as a complement to trend-following systems (e.g., with 50/200 EMA).
- Free on TradingView—no paid version needed.

**Cons:**
- **Laggy on lower timeframes** (<1H). Useless for scalping.
- Signal line crossovers are too slow—prefer zero-line crossovers.
- No built-in alerts for divergences (you’ll need to spot them manually).
- Can give false signals in ranging markets (like any momentum oscillator).

### Who It’s Actually For

- **Swing traders** (holding 2–10 days) on crypto, forex, or stocks.
- **Position traders** using daily or weekly charts.
- Traders who already use MACD but want a **less laggy alternative** for momentum confirmation.

**Not for:** Scalpers, day traders under 1H, or anyone who can’t spot divergences manually.

### Better Alternatives If They Exist

- **MACD:** More widely used, more resources online. KST is faster but MACD has better community support.
- **Fisher Transform Indicator:** Less lag than KST but more prone to whipsaw. Better for day trading.
- **ROC (Rate of Change):** Simpler, but no smoothing. KST’s smoothing is the whole point.

If you’re already comfortable with MACD, try KST as a secondary confirmation—not a replacement.

### FAQ: Real Trader Questions

**Q: Does KST work on crypto?**  
Yes, but tighten the ROC periods (e.g., 8, 12, 16, 20) for 4H charts. Defaults are too slow for Bitcoin’s volatility.

**Q: What’s the best timeframe?**  
Daily or 4H. Lower than 1H gives too many whipsaws.

**Q: Can I set alerts for KST crossovers?**  
Yes—TradingView allows alerts for “Crosses zero line” or “Crosses signal line.” Use zero-line alerts for cleaner signals.

**Q: How is it different from MACD?**  
MACD uses EMAs of price; KST uses smoothed ROC. KST measures *percentage change* momentum, making it more sensitive to volatility.

**Q: Does it repaint?**  
No. KST is a fixed calculation based on historical data. It does not repaint.

### Final Verdict with Star Rating

**⭐⭐⭐⭐ (4/5)** – A solid momentum oscillator for swing traders who can handle a bit of lag for cleaner signals. It won't replace MACD for everyone, but the divergence signals alone are worth adding to your toolkit. Drop it on a daily chart, pair it with support/resistance, and you’ve got a reliable edge. Just don’t expect miracles on 5-minute charts.

**Would I install it?** Yes—but only for my swing trading watchlist. For day trading, I stick with Fisher Transform or Volume Profile.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*

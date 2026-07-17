---
title: "Squeeze Momentum Indicator Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/squeeze-momentum-indicator.png"
tags:
  - squeeze momentum indicator
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of the Squeeze Momentum Indicator for TradingView. Real settings, entry/exit rules, pros/cons, and who this volatility-based tool actually works for."
---

**Final Verdict: ⭐⭐⭐⭐ (4/5)**  
A solid, well-known volatility breakout tool that pairs Bollinger Bands with Keltner Channels. It’s not magic, but if you understand its mechanics, it’s a reliable screener for momentum entries. Loses a star because it’s prone to whipsaws in choppy markets and can be confusing for beginners.

---

## What This Indicator Actually Does

The Squeeze Momentum Indicator (often called the “TTM Squeeze” after John Carter’s original) measures two things:  
1. **Volatility contraction** – When Bollinger Bands move inside Keltner Channels, a “squeeze” is happening (think coiled spring).  
2. **Momentum direction** – A histogram above/below zero shows whether the breakout is bullish or bearish.

It doesn’t predict direction—it alerts you that a big move is likely, then tells you which way the initial momentum is flowing. The dots on the chart (green/red) mark when the squeeze is on. As the chart above shows, you’ll see flat, low-volatility periods followed by explosive moves.

## Key Features That Set It Apart

- **Dual volatility measurement** – Uses Bollinger Bands (2.0, 20) and Keltner Channels (1.5, 20). When BBs are inside KCs, squeeze is on.  
- **Zero-line histogram** – Green bars above zero = bullish momentum; red bars below = bearish.  
- **Momentum color changes** – Some versions shift histogram color when momentum accelerates (e.g., lime green vs. dark green).  
- **Dot markers** – Red dots = squeeze on, green dots = squeeze released (breakout in progress).  

What it’s NOT: It’s not an entry signal alone. Many traders lose money treating a squeeze release as a buy/sell order. You need confluence.

## Best Settings (What I Actually Use)

Default settings (Bollinger 20, 2.0; Keltner 20, 1.5) work fine for most timeframes. But here’s my tweak:

- **Timeframe**: 1H or higher. Lower timeframes (5m, 15m) produce too many false signals.  
- **Bollinger Length**: 20  
- **Bollinger StdDev**: 2.0  
- **Keltner Length**: 20  
- **Keltner Multiplier**: 1.5 (default is fine)  
- **Histogram Lookback**: 20 (controls sensitivity—lower = more signals, higher = fewer)  
- **Momentum Threshold**: I ignore bars smaller than 0.5 in absolute value. They’re noise.

If you scalp, reduce Keltner multiplier to 1.3 for earlier squeeze detection, but expect more whipsaws.

## How to Use It for Entries and Exits

**Long Entry**:  
1. Wait for red dots (squeeze on) followed by green dots (squeeze released).  
2. First green histogram bar above zero = bullish momentum.  
3. Enter on a pullback to the 20 EMA or a minor support level (don’t chase).  
4. Stop loss below the recent swing low or the lower Keltner band.  
5. Target: 2x the recent squeeze range, or trail with the 20 EMA.

**Short Entry**: Same logic inverted—red histogram bar below zero after green dots.

**Exit**: The histogram turning back toward zero or changing color is your early exit signal. If momentum bars shrink, get out.

**Risk Management**: I use a 1.5x ATR stop. If the squeeze breaks in your favor but momentum stalls, exit. The indicator can’t save you from a failed breakout.

## Honest Pros and Cons

**Pros:**  
- Excellent for spotting explosive setups before they happen.  
- Works across all liquid markets: crypto, forex, stocks, futures.  
- Free version on TradingView is functional (no paid upgrade needed).  
- Combines volatility and momentum in one clean view.

**Cons:**  
- **Whipsaws in range-bound markets** – If there’s no trend, the squeeze releases both ways. You’ll get chopped.  
- **Lag on momentum direction** – The histogram starts printing AFTER the move begins. You’re not early, you’re joining.  
- **Overused** – Everyone sees the same squeeze. Expect false breaks if you’re trading alone.  
- **No volume confirmation** – A squeeze on low volume is less reliable. Pair with Volume Profile or OBV.

## Who It's Actually For

- **Swing traders** on 1H–4H charts who want to catch big moves after consolidation.  
- **Breakout traders** who understand that not every squeeze leads to a trend.  
- **Portfolio managers** screening for stocks about to make a move.  

**Not for:** Scalpers who need split-second entries, or beginners who don’t use stop losses.

## Better Alternatives If They Exist

- **VWAP Squeeze** – Adds volume-weighted average price to filter low-volume squeezes.  
- **Momentum Squeeze Pro** (paid) – Lets you adjust the momentum oscillator type (RSI, CCI, etc.) and adds alerts.  
- **Bollinger Bands %B + Keltner Channels** – If you want to build your own squeeze, plot %B inside KCs. Same logic, more control.

## FAQ

**Q: Does this indicator repaint?**  
A: No. The histogram and dots are fixed once the bar closes. Intraday, the dots may flicker, but that’s normal for any real-time indicator.

**Q: What’s the best timeframe?**  
A: 1H or 4H. Lower timeframes give too many false squeezes. Daily works for long-term holds.

**Q: Can I use it alone?**  
A: You can, but you’ll lose money. Always add a trend filter (e.g., 200 EMA slope) and a volume confirmation.

**Q: Why does the histogram show momentum but price doesn’t move?**  
A: Divergence. If histogram is making higher highs but price isn’t, a reversal is coming. Watch for it.

**Q: Is the free version good enough?**  
A: Yes. The built-in “Squeeze Momentum Indicator” on TradingView is identical to most paid versions.

---

**Bottom line:** A 4/5 star tool that’s earned its reputation—but only if you treat it as a screener, not a crystal ball. Use it to find setups, then confirm with price action and volume. If you do that, it’s a solid addition to your toolkit.

## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*
